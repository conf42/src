"""Intake rules on generated fixtures - one per row of the junk catalogue (plan section 3b). Offline: ffmpeg + pypdf only,
no Drive, no Claude.   python factory/tests/test_intake.py   (from the src repo root)"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from factory import intake, media  # noqa: E402

FF = None
ROW = {"speakers": "Ada Lovelace", "Name1": "Ada Lovelace", "Name2": "", "title": "Engines", "banished": False}
CFG = {"health_window_seconds": 60, "health_max_cut_seconds": 120, "health_calm_seconds": 15, "health_min_sound_percent": 15}


def ff(*args):
    r = media.run([FF, "-hide_banner", "-loglevel", "error", "-y"] + list(args))
    assert r.returncode == 0, r.stderr[-400:]


def clip(path, secs, video="testsrc2=s=320x180:r=10", audio="sine=f=440:sample_rate=48000", acodec="aac", extra=()):
    ff("-f", "lavfi", "-i", "%s:d=%d" % (video, secs), "-f", "lavfi", "-t", str(secs), "-i", audio,
       "-c:v", "libx264", "-preset", "ultrafast", "-pix_fmt", "yuv420p", "-c:a", acodec, "-ac", "1", "-shortest", *extra, path)
    return path


def info(seconds, names=("Ada Lovelace",), slot=30, **meta):
    return {"event": {"slug": "test2027", "label": "Conf42 Test 2027"}, "typed": names[0] if names else "",
            "talk": {"k": "Test_2027_Ada_Lovelace", "names": list(names), "title": "Engines", "slot_min": slot},
            "meta": dict({"seconds": seconds, "stop_reason": "stop"}, **meta)}


def main():
    global FF
    FF = media.tool("ffmpeg")
    tmp = tempfile.mkdtemp(prefix="intake-test-")
    results, fails = [], 0

    def check(name, got, want_outcome, want_text=None):
        nonlocal fails
        txt = " | ".join([got["reason"]] + got["flags"] + got["fixes"] + got.get("unclear", []))
        ok = got["outcome"] == want_outcome and (not want_text or want_text.lower() in txt.lower())
        fails += not ok
        results.append("%s %-34s %-7s %s" % ("ok  " if ok else "FAIL", name, got["outcome"], txt[:150]))

    p = lambda n: os.path.join(tmp, n)
    try:
        good = clip(p("good.mp4"), 240)
        check("good talk", intake.assess(good, info(240), ROW, None, CFG), "accept")
        check("40 s test take", intake.assess(clip(p("short.mp4"), 40), info(40), ROW, None, CFG), "reject", "too-short")
        check("4 min for a 30 min slot -> unclear", intake.assess(good, info(240, slot=30), ROW, None, CFG), "accept", "for a 30 min slot")
        check("silent (muted mic)", intake.assess(clip(p("silent.mp4"), 240, audio="anullsrc=r=48000:cl=mono"), info(240), ROW, None, CFG), "reject", "silent")
        check("black picture", intake.assess(clip(p("black.mp4"), 240, video="color=c=black:s=320x180:r=10"), info(240), ROW, None, CFG), "reject", "no-picture")
        check("frozen picture -> unclear", intake.assess(clip(p("frozen.mp4"), 240, video="color=c=gray:s=320x180:r=10"), info(240), ROW, None, CFG), "accept", "never changes")
        check("frozen + no Claude -> hold", intake.decide(p("frozen.mp4"), info(240), ROW, None, CFG, use_claude=False), "hold", "unclear")
        opus = clip(p("opus.mp4"), 240, acodec="libopus")
        check("Opus sound", intake.assess(opus, info(240), ROW, None, CFG), "accept", "re-encoded to AAC")
        loud = clip(p("clip.mp4"), 240, audio=r"aevalsrc=clip(4*sin(2*PI*440*t)\,-1\,1):s=48000")
        check("clipped sound", intake.assess(loud, info(240), ROW, None, CFG), "accept", "distorted")
        drop = clip(p("drop.mp4"), 420, audio="aevalsrc=if(between(t\\,150\\,230)\\,0\\,0.3*sin(2*PI*440*t)):s=48000:d=420")
        check("mic drops out mid-talk", intake.assess(drop, info(420), ROW, None, CFG), "accept", "no sound for")
        check("organizer test upload", intake.assess(good, info(240, names=("Mark Pawlikowski",)), None, "no speaker", CFG), "reject", "organizer")
        check("unmatched speaker", intake.assess(good, info(240, names=("Nobody Here",)), None, "no speaker", CFG), "hold", "unmatched")
        check("purged talk recorded anyway", intake.assess(good, info(240), ROW, "talk no longer in the lineup", CFG), "accept", "purged talk uploaded")
        check("test-ish name -> unclear", intake.assess(good, info(240, names=("test test",)), ROW, None, CFG), "accept", "looks like a test")
        check("ends early vs talk.json", intake.assess(good, info(400), ROW, None, CFG), "accept", "ends early")
        check("2 h limit", intake.assess(good, info(240, stop_reason="limit"), ROW, None, CFG), "accept", "2-hour limit")
        frag = clip(p("frag.mp4"), 300, extra=("-movflags", "frag_keyframe+empty_moov"))
        with open(frag, "rb") as f:
            data = f.read()
        with open(p("trunc.mp4"), "wb") as f:
            f.write(data[:int(len(data) * 0.7)])
        check("truncated fragmented MP4", intake.assess(p("trunc.mp4"), info(300, stop_reason="crash"), ROW, None, CFG), "accept", "recovered")
        with open(p("junk.mp4"), "wb") as f:
            f.write(b"<html>Sign in</html>" * 200)
        check("HTML page named .mp4", intake.assess(p("junk.mp4"), info(240), ROW, None, CFG), "reject", "corrupt")
        rep = intake.assess(opus, info(240), ROW, None, CFG)
        out = intake.prepare(opus, rep, p("prepared.mp4"))
        s = intake.streams(out)
        results.append("%s %-34s %s" % ("ok  " if s["audio"]["codec"] == "aac" and not media.fragmented(out) else "FAIL", "prepare() fixes Opus", s["audio"]["codec"]))
        fails += s["audio"]["codec"] != "aac"

        # slides
        from pypdf import PdfWriter
        w = PdfWriter(); w.add_blank_page(960, 540); w.add_blank_page(960, 540)
        w.write(p("blank.pdf"))
        w2 = PdfWriter(); w2.add_blank_page(960, 540); w2.encrypt("secret")
        w2.write(p("locked.pdf"))
        w3 = PdfWriter(); w3.add_blank_page(595, 842)
        w3.write(p("portrait.pdf"))
        open(p("empty.pdf"), "wb").close()
        with open(p("html.pdf"), "wb") as f:
            f.write(b"<!doctype html><title>Sign in</title>")
        for name, path, usable, text in [("blank slides", "blank.pdf", True, "blank"), ("locked slides", "locked.pdf", False, "password"),
                                         ("portrait / handouts", "portrait.pdf", True, "portrait"), ("0-byte slides", "empty.pdf", False, "empty"),
                                         ("HTML named .pdf", "html.pdf", False, "not a PDF")]:
            u, flags = intake.slides_check(p(path), {"slide_pages": 0})
            ok = u == usable and any(text.lower() in x.lower() for x in flags)
            fails += not ok
            results.append("%s %-34s usable=%s %s" % ("ok  " if ok else "FAIL", name, u, "; ".join(flags)))
        u, flags = intake.slides_check(p("blank.pdf"), {"slide_pages": 30})
        ok = any("30-page" in x for x in flags)
        fails += not ok
        results.append("%s %-34s %s" % ("ok  " if ok else "FAIL", "page count vs the deck shown", "; ".join(flags)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("\n".join(results))
    print("\n%d checks, %d failed" % (len(results), fails))
    return fails


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
