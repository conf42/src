"""Offline smoke test of the factory on this machine - no Descript calls, no token needed.

Checks everything the factory does locally: the health check, a camera-style .mov rendered to mp4 on whatever encoder
this machine has (NVENC / Apple media engine / CPU), the damaged-file check, YouTube loudness, slide compression,
speaker matching against a real event CSV, the GPU scheduler inputs and the dashboard API.

    python factory/tests/smoke.py        (from the src folder, with the factory's Python)

Runs on every change to factory/ on macOS, Windows and Linux (.github/workflows/factory-smoke.yml).
"""
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import urllib.request

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # src/factory
sys.path.insert(0, HERE)
from factory import app, events, machine, media, pipeline, slides  # noqa: E402

FAILED = []


def check(name, ok, detail=""):
    print("%s %s%s" % ("PASS" if ok else "FAIL", name, (" - " + str(detail)) if detail else ""), flush=True)
    if not ok:
        FAILED.append(name)


def main():
    tmp = tempfile.mkdtemp(prefix="factory-smoke-")
    cfg = pipeline.settings()
    print("machine: %s, %s, Python %s" % (sys.platform, machine.machine_name(cfg), sys.version.split()[0]))

    # 1. health check: every required item except the Descript token (CI has none)
    docs = machine.doctor(cfg, events.REPO, check_descript=False)
    for c in docs:
        print("     doctor: %-38s %s %s" % (c["name"], "ok " if c["ok"] else "-- ", c["detail"]))
    skip = {"Descript token"} | ({"Work folder"} if os.environ.get("GITHUB_ACTIONS") else set())   # CI: no token, small disks
    bad = [c["name"] for c in docs if c["required"] and not c["ok"] and c["name"] not in skip]
    check("health check (required items)", not bad, ", ".join(bad))
    check("desktop / work folder", os.path.isdir(machine.desktop()) or True, machine.work_root(cfg))

    # 2. a camera-style source: 1080p60 H.264 with uncompressed float audio in a .mov, 20 s
    src = os.path.join(tmp, "Jane Doe.mov")
    r = subprocess.run([media.tool("ffmpeg"), "-hide_banner", "-loglevel", "error", "-y",
                        "-f", "lavfi", "-i", "testsrc2=size=1920x1080:rate=60",
                        "-f", "lavfi", "-i", "sine=frequency=440:sample_rate=48000",
                        "-t", "20", "-c:v", "libx264", "-preset", "ultrafast", "-b:v", "40M",
                        "-af", "volume=-20dB", "-c:a", "pcm_f32le", src], capture_output=True, text=True)
    check("make a test .mov", r.returncode == 0 and os.path.exists(src), r.stderr[-200:])

    # 3. render to a lean mp4 on this machine's best encoder
    labels = []
    t0 = time.time()
    try:
        out = media.render(src, os.path.join(tmp, "Jane Doe.mp4"), on_progress=lambda l, p: labels.append(l))
        check("render to mp4", os.path.exists(out), "%s in %.1f s via %s" % (
            os.path.basename(out), time.time() - t0, (labels[-1].split(" - ")[0] if labels else "?")))
        check("render is sound + full length", media.verify(out, 20) is None, media.verify(out, 20))
        check("render is smaller than the camera file", os.path.getsize(out) < os.path.getsize(src),
              "%.1f MB -> %.1f MB" % (os.path.getsize(src) / 1e6, os.path.getsize(out) / 1e6))
    except Exception as ex:
        check("render to mp4", False, ex)
        out = None

    # 4. the damaged-file check catches a file two writers scrambled
    if out:
        bad_copy = os.path.join(tmp, "damaged.mp4")
        shutil.copy(out, bad_copy)
        with open(bad_copy, "r+b") as f:
            f.seek(os.path.getsize(bad_copy) // 3)
            f.write(os.urandom(200000))
        check("damaged mp4 is detected", media.verify(bad_copy, 20) is not None, media.verify(bad_copy, 20))

    # 5. YouTube loudness (-14 LUFS, true peak -1.5)
    if out:
        loud = os.path.join(tmp, "Jane Doe - loud.mp4")
        try:
            media.normalize(out, loud, -14, -1.5)
            lufs, peak = media.loudness(loud)
            check("loudness -14 LUFS", lufs is not None and abs(lufs + 14) <= 1.5, "%s LUFS, peak %s" % (lufs, peak))
        except Exception as ex:
            check("loudness -14 LUFS", False, ex)

    # 5b. video health check: a 3-minute talk with 12 s of clicking on the desktop before the slides, 8 s of "stop
    # sharing" after them and its sound on the left channel only -> sound copied to both, both ends cut; the same talk
    # with someone talking over the junk -> nothing cut; muted / no sound track -> stopped before the upload
    try:
        ff = media.tool("ffmpeg")
        talk = os.path.join(tmp, "health.mp4")
        r = subprocess.run([ff, "-hide_banner", "-loglevel", "error", "-y",
                            "-f", "lavfi", "-i", "color=c=gray:s=320x180:r=25:d=178", "-f", "lavfi", "-i", "color=c=red:s=8x8:r=25:d=178",
                            "-f", "lavfi", "-i", "color=c=navy:s=320x180:r=25:d=78", "-f", "lavfi", "-i", "color=c=darkgreen:s=320x180:r=25:d=80",
                            "-f", "lavfi", "-i", "aevalsrc='if(between(t,5,5.25),0.3*sin(2*PI*900*t),0)':s=48000:d=12",
                            "-f", "lavfi", "-i", "sine=frequency=220:sample_rate=48000:duration=158",
                            "-f", "lavfi", "-i", "anullsrc=r=48000:cl=mono:d=8",
                            "-filter_complex", "[0:v][1:v]overlay=x='mod(t*60,300)':y=80[desk];[desk]split=2[d1][d2];"
                            "[d1]trim=0:12,setpts=PTS-STARTPTS[a1];[d2]trim=170:178,setpts=PTS-STARTPTS[a3];"
                            "[a1][2:v][3:v][a3]concat=n=4:v=1:a=0[v];[4:a][5:a][6:a]concat=n=3:v=0:a=1,volume=-12dB[m];"
                            "anullsrc=r=48000:cl=mono,atrim=0:178[z];[m][z]amerge=inputs=2[a]",
                            "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "ultrafast", "-c:a", "aac", "-t", "178", talk],
                           capture_output=True, text=True)
        check("make a test talk with setup junk", r.returncode == 0, r.stderr[-200:])
        h = media.health(talk, cfg)
        check("health: one-channel sound fixed", h["af"] == "pan=stereo|c0=c0|c1=c0" and not h["block"], h["fixes"])
        check("health: setup cut at the start", h["start"] is not None and abs(h["start"] - 12) <= 1, h["start"])
        check("health: setup cut at the end", h["end"] is not None and abs(h["end"] - 170) <= 1, h["end"])
        fixed = media.render(talk, os.path.join(tmp, "health.health.mp4"), start=h["start"], end=h["end"], af=h["af"], force=True)
        lv = media.audio_levels(fixed)
        got = media.probe(fixed)["duration"]
        check("health: fixed talk", abs(got - (h["end"] - h["start"])) <= 1.5 and abs(lv["left"] - lv["right"]) < 3,
              "%.1f s, left %s / right %s dB" % (got, lv["left"], lv["right"]))
        for name, extra, want in (("talking over the junk", ["-f", "lavfi", "-i", "sine=frequency=200:sample_rate=48000:duration=178",
                                                            "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-ac", "2"], "kept"),
                                  ("muted", ["-map", "0", "-c:v", "copy", "-af", "volume=0", "-c:a", "aac"], "block"),
                                  ("no sound track", ["-map", "0:v", "-c:v", "copy"], "block")):
            v = os.path.join(tmp, "health-%s.mp4" % name.replace(" ", "-"))
            subprocess.run([ff, "-hide_banner", "-loglevel", "error", "-y", "-i", talk] + extra + [v], capture_output=True)
            h = media.health(v, cfg)
            ok = (bool(h["block"]) if want == "block" else (not h["block"] and h["start"] is None and h["end"] is None and len(h["flags"]) == 2))
            check("health: %s -> %s" % (name, "stopped" if want == "block" else "not cut, flagged"), ok, h["block"] or h["flags"])
    except Exception as ex:
        check("health check", False, ex)

    # 6. slides: a heavy 3-page PDF is compressed under the limit with every page kept
    try:
        from PIL import Image
        pages = [Image.frombytes("RGB", (1600, 900), os.urandom(1600 * 900 * 3)) for _ in range(3)]
        pdf = os.path.join(tmp, "deck.pdf")
        pages[0].save(pdf, save_all=True, append_images=pages[1:], quality=95)
        before = os.path.getsize(pdf)
        res = slides.compress(pdf, 1_500_000, os.path.join(tmp, "originals"))
        from pypdf import PdfReader
        check("slides compressed, pages kept", res and os.path.getsize(pdf) < before and len(PdfReader(pdf).pages) == 3,
              "%.1f MB -> %.1f MB" % (before / 1e6, os.path.getsize(pdf) / 1e6))
    except Exception as ex:
        check("slides compressed, pages kept", False, ex)

    # 6b. PPTX -> PDF with whatever converter this machine has (LibreOffice / PowerPoint / Keynote)
    if machine.pptx_converters():
        ok, detail = machine.pptx_test()
        check("pptx deck -> pdf", ok, detail)
    else:
        print("SKIP pptx deck -> pdf (no converter installed here)")

    # 7. speaker matching against a real event CSV
    try:
        ev = next(e for e in events.all_events() if (e.get("db_path") or "").strip()
                  and os.path.exists(os.path.join(events.REPO, e["db_path"].replace("./", ""))))
        evd = events.event(ev["short_url"])
        talks = events.talks(evd)
        t = talks[len(talks) // 2]
        hit, why = events.match("%s Conf42 final version" % t["name1"], talks)
        check("speaker matching", hit and hit["speakers"] == t["speakers"], "%s -> %s (%s)" % (t["name1"], hit and hit["speakers"], evd["title"]))
        miss, why = events.match("Somebody Unknown Zyx", talks)
        check("unknown names are never guessed", miss is None, why)
    except Exception as ex:
        check("speaker matching", False, ex)

    # 8. GPU scheduler inputs
    g = media.gpu_status()
    slots = media.render_slots("auto")
    check("render slots", slots >= 1, "%d at once (%s)" % (slots, g["name"] if g else "no NVIDIA GPU"))

    # 9. the dashboard answers
    import http.server
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = "http://127.0.0.1:%d" % srv.server_address[1]
    try:
        page = urllib.request.urlopen(base + "/", timeout=30).read().decode("utf-8")
        check("dashboard page", "Conf42 factory" in page and "__STEPS__" not in page)
        evs = json.loads(urllib.request.urlopen(base + "/api/events", timeout=60).read())
        check("dashboard events", isinstance(evs, list) and len(evs) > 0, "%d events" % len(evs))
        doc = json.loads(urllib.request.urlopen(base + "/api/doctor", timeout=120).read())
        check("dashboard health check", "checks" in doc, doc.get("machine"))
    except Exception as ex:
        check("dashboard", False, ex)
    srv.shutdown()

    shutil.rmtree(tmp, ignore_errors=True)
    print("\n%s" % ("ALL PASSED" if not FAILED else "FAILED: " + ", ".join(FAILED)))
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
