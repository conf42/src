"""ffprobe / ffmpeg helpers: source probe, YouTube-level loudness, QA measurement."""
import glob
import json
import os
import re
import shutil
import sys
import subprocess

RESOLUTIONS = [(480, "480p"), (720, "720p"), (1080, "1080p"), (1440, "1440p"), (2160, "4K")]


def tool(name):
    from . import machine
    found = machine.find_tool(name)
    if found:
        return found
    raise RuntimeError("%s not found - install it with: %s" % (name, machine.install_hint("ffmpeg")))


def run(args):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe(path):
    out = run([tool("ffprobe"), "-v", "error", "-show_entries", "stream=codec_type,width,height:format=duration",
               "-of", "json", path]).stdout
    d = json.loads(out or "{}")
    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), {})
    return {"width": v.get("width") or 0, "height": v.get("height") or 0,
            "duration": float((d.get("format") or {}).get("duration") or 0)}


def render(src, dst, max_short_side=1080, cq=21, on_progress=None, start=None, end=None, af=None, force=False):
    """Re-encode a source video to a lean H.264/AAC MP4 before the upload (camera .mov files are huge for no gain):
    GPU (NVENC) when there is one, else libx264; short side capped at max_short_side, audio kept at 48 kHz 192k so
    Studio Sound still gets a clean signal. Returns dst, or src when the render would not be smaller.
    start / end / af: the health check's fixes (seconds kept, an audio filter), applied in the same single encode;
    force: always write dst (a fixed file is needed even when it is not smaller)."""
    info = probe(src)
    w, h = info["width"], info["height"]
    big = w and h and min(w, h) > max_short_side
    size = ("-2:%d" % max_short_side) if h <= w else ("%d:-2" % max_short_side)
    audio = ["-map", "0:v:0", "-map", "0:a:0?"] + (["-af", af] if af else []) + \
        ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart"]
    nvenc = ["-c:v", "h264_nvenc", "-preset", "p5", "-rc", "vbr", "-cq", str(cq), "-b:v", "0"]
    head = ["-hide_banner", "-loglevel", "error", "-y"] + (["-ss", "%.3f" % start] if start else []) + \
        (["-to", "%.3f" % end] if end else [])
    expected = (end or info["duration"]) - (start or 0)
    scale = ["-vf", "scale=" + size] if big else []
    attempts = []   # (label, args) in the order this machine can use them; the CPU always last
    if gpu_status():                                  # NVIDIA: all on the GPU (NVDEC + NVENC), then CPU decode + NVENC
        attempts += [("GPU", head + ["-hwaccel", "cuda", "-hwaccel_output_format", "cuda", "-i", src]
                      + (["-vf", "scale_cuda=" + size] if big else []) + nvenc + audio),
                     ("GPU encoder", head + ["-i", src] + scale + ["-pix_fmt", "yuv420p"] + nvenc + audio)]
    if sys.platform == "darwin":                      # Apple: the media engine decodes and encodes
        attempts += [("Mac media engine", head + ["-hwaccel", "videotoolbox", "-i", src] + scale +
                      ["-pix_fmt", "yuv420p", "-c:v", "h264_videotoolbox", "-q:v", "62", "-allow_sw", "1"] + audio)]
    attempts += [("CPU", head + ["-i", src] + scale + ["-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "veryfast",
                                                      "-crf", str(cq - 1)] + audio)]
    part = "%s.%d.part.mp4" % (dst, os.getpid())     # per process: a leftover ffmpeg can never write into it
    err = ""
    for how, args in attempts:
        rc, err = _ffmpeg_progress([tool("ffmpeg")] + args + ["-progress", "pipe:1", "-nostats", part],
                                   expected, lambda pct: on_progress and on_progress(
                                       "rendering to mp4 on the %s - %d%%" % (how, pct), pct))
        if rc == 0 and verify(part, expected) is None:
            break
        if rc == 0:
            err = "rendered file failed the check: " + verify(part, expected)
        if os.path.exists(part):
            os.remove(part)
    else:
        raise RuntimeError("render to mp4 failed: " + err[-300:])
    if not force and os.path.getsize(part) >= os.path.getsize(src):
        os.remove(part)
        return src
    os.replace(part, dst)
    return dst


def verify(path, expected_seconds=None):
    """None when the video is sound, else what is wrong: the container must demux with no errors (a file two
    ffmpegs wrote into at once fails here in about a second) and last as long as the source (within 2 s)."""
    if not os.path.exists(path) or os.path.getsize(path) < 1024:
        return "missing or empty"
    r = run([tool("ffmpeg"), "-v", "error", "-i", path, "-map", "0", "-c", "copy", "-f", "null", "-"])
    errors = [l for l in r.stderr.splitlines() if l.strip()]
    if r.returncode != 0 or errors:
        return "%d stream errors, e.g. %s" % (len(errors), (errors or [r.stderr])[0][:120])
    if expected_seconds:
        got = probe(path)["duration"]
        if abs(got - expected_seconds) > 2:
            return "lasts %.0f s instead of %.0f s" % (got, expected_seconds)
    return None


def gpu_status():
    """NVIDIA GPU load for the render scheduler and the dashboard; None without nvidia-smi."""
    exe = shutil.which("nvidia-smi") or r"C:\Windows\System32\nvidia-smi.exe"
    try:
        r = subprocess.run([exe, "--query-gpu=name,utilization.gpu,utilization.encoder,utilization.decoder,memory.used,"
                            "memory.total,temperature.gpu,power.draw,encoder.stats.sessionCount,encoder.stats.averageFps",
                            "--format=csv,noheader,nounits"], capture_output=True, text=True, timeout=10)
        v = [x.strip() for x in r.stdout.strip().splitlines()[0].split(",")]
    except Exception:
        return None
    num = lambda x: float(x) if x.replace(".", "", 1).isdigit() else None
    return {"name": v[0], "gpu": num(v[1]), "encoder": num(v[2]), "decoder": num(v[3]), "vram_used": num(v[4]),
            "vram_total": num(v[5]), "temp": num(v[6]), "power": num(v[7]), "sessions": num(v[8]), "fps": num(v[9])}


def render_slots(setting):
    """How many renders may run at once: a number from settings, or 'auto' = go all out on an RTX 5090 (8 NVENC
    sessions, Marek 2026-09-28), 3 on another NVIDIA card, 2 on the CPU."""
    if str(setting).strip().isdigit():
        return max(1, int(setting))
    g = gpu_status()
    if not g:
        return 2
    return 8 if "5090" in g["name"] else 3


def _ffmpeg_progress(args, duration, cb):
    """Run ffmpeg with -progress pipe:1 and report the percentage done every couple of seconds."""
    import time
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8", errors="replace")
    last = 0
    for line in p.stdout:
        if line.startswith("out_time_us=") and duration:
            try:
                pct = min(99, int(int(line.split("=")[1]) / 1e6 / duration * 100))
            except ValueError:
                continue
            if time.time() - last > 2:
                last = time.time()
                cb(pct)
    err = p.stderr.read()
    return p.wait(), err


def pick_resolution(width, height, cap):
    """Largest Descript export size not above the source (short side) and not above the cap."""
    short = min(width, height) if width and height else 1080
    cap_px = dict((label, px) for px, label in RESOLUTIONS).get(cap, 1080)
    best = "480p"
    for px, label in RESOLUTIONS:
        if px <= short and px <= cap_px:
            best = label
    return best


def loudness(path):
    """Integrated loudness (LUFS) and true peak (dBTP) of a file."""
    err = run([tool("ffmpeg"), "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
    summary = err[err.rfind("Summary:"):]
    i = re.search(r"I:\s+(-?[\d.]+) LUFS", summary)
    tp = re.search(r"Peak:\s+(-?[\d.]+) dBFS", summary)
    return (float(i.group(1)) if i else None, float(tp.group(1)) if tp else None)


def early_cut(path, window=12, threshold=0.25):
    """Seconds into the video of the first hard picture change in its first `window` seconds, or None. A talk whose
    picture jumps right at the start usually opens on the speaker's setup (OBS, a desktop) before the slides
    (Marek 2026-10-13). On Feature Flags 2026 this caught exactly the one such talk out of 13."""
    r = run([tool("ffmpeg"), "-hide_banner", "-nostats", "-t", str(window), "-i", path, "-an",
             "-vf", "scale=320:-1,select='gt(scene\\,%s)',showinfo" % threshold, "-f", "null", "-"])
    m = re.search(r"pts_time:([0-9.]+)", r.stderr or "")
    return float(m.group(1)) if m else None


def normalize(src, dst, lufs, tp, start=None, end=None):
    """Two-pass loudnorm to the target; the video stream is copied untouched. start / end (seconds) keep only that
    part of the talk (the trim to the first and last words): the video then starts at the keyframe before `start`,
    and the player starts at `start` exactly."""
    cut = (["-ss", "%.3f" % start] if start else []) + (["-to", "%.3f" % end] if end else [])
    first = run([tool("ffmpeg"), "-hide_banner", "-nostats"] + cut + ["-i", src, "-af",
                 "loudnorm=I=%s:TP=%s:LRA=11:print_format=json" % (lufs, tp), "-f", "null", "-"]).stderr
    m = json.loads(first[first.rfind("{"):first.rfind("}") + 1])
    af = ("loudnorm=I={I}:TP={TP}:LRA=11:measured_I={mi}:measured_TP={mtp}:measured_LRA={mlra}:"
          "measured_thresh={mth}:offset={off}:linear=true").format(
        I=lufs, TP=tp, mi=m["input_i"], mtp=m["input_tp"], mlra=m["input_lra"], mth=m["input_thresh"], off=m["target_offset"])
    tmp = "%s.%d.part.mp4" % (dst, os.getpid())
    r = run([tool("ffmpeg"), "-hide_banner", "-loglevel", "error", "-y"] + cut + ["-i", src, "-c:v", "copy", "-af", af,
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", tmp])
    if r.returncode != 0 or not os.path.exists(tmp):
        raise RuntimeError("ffmpeg loudness step failed: " + r.stderr[-400:])
    os.replace(tmp, dst)


# ---- video health check: before the upload to Descript (Marek 2026-10-17) -----------------------------------------
# Descript can't trim a talk's setup junk (the speaker clicking around, the full desktop before the slides, "stop
# sharing" at the end), and an upload with a broken sound track wastes credits. So every rendered talk is checked here,
# locally: dead or one-sided sound is fixed or blocks the talk, and junk with no talking in it is cut off.
FPS, W, H = 2, 160, 90         # small grey frames, 2 a second: enough to see a slide change or a moving cursor


def audio_levels(path):
    """{"channels", "left", "right", "mono", "max"} in dB (mean volume; left/right only for 2 channels), or None when
    the file has no sound track."""
    out = run([tool("ffprobe"), "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=channels",
               "-of", "json", path]).stdout
    streams = json.loads(out or "{}").get("streams") or []
    if not streams:
        return None
    ch = int(streams[0].get("channels") or 1)
    if ch == 2:
        graph = ("[0:a:0]aformat=channel_layouts=stereo,asplit=2[a][b];[a]channelsplit=channel_layout=stereo[L][R];"
                 "[L]volumedetect@left[l];[R]volumedetect@right[r];[b]pan=mono|c0=0.5*c0+0.5*c1,volumedetect@mono[m]")
        maps = ["-map", "[l]", "-f", "null", "-", "-map", "[r]", "-f", "null", "-", "-map", "[m]", "-f", "null", "-"]
    else:
        graph, maps = "[0:a:0]volumedetect@mono[m]", ["-map", "[m]", "-f", "null", "-"]
    err = run([tool("ffmpeg"), "-hide_banner", "-nostats", "-i", path, "-filter_complex", graph] + maps).stderr
    lv = {"channels": ch}
    for name in ("left", "right", "mono"):
        m = re.search(r"volumedetect@%s @ [^\]]+\] mean_volume: (-?[\d.]+|-inf) dB" % name, err)
        if m:
            lv[name] = -91.0 if m.group(1) == "-inf" else float(m.group(1))
    peaks = [float(x) for x in re.findall(r"max_volume: (-?[\d.]+) dB", err)]
    lv["max"] = max(peaks) if peaks else -91.0
    return lv


def sound_runs(path, af, noise_db, length):
    """[(start, end)] of the stretches with sound (anything above noise_db that lasts), from ffmpeg's silencedetect."""
    err = run([tool("ffmpeg"), "-hide_banner", "-nostats", "-i", path, "-map", "0:a:0",
               "-af", (af + "," if af else "") + "silencedetect=noise=%.0fdB:d=0.4" % noise_db, "-f", "null", "-"]).stderr
    runs, pos, silent = [], 0.0, False
    for kind, at in re.findall(r"silence_(start|end): (-?[\d.]+)", err):
        at = max(0.0, float(at))
        if kind == "start":
            if at > pos:
                runs.append((pos, at))
            silent = True
        else:
            pos, silent = at, False
    if not silent and length - pos > 0.2:
        runs.append((pos, length))                      # sound right up to the end
    return runs


def talking(runs, a, b, longest=1.2, total=2.5):
    """True when someone talks between a and b: a stretch of sound of `longest` seconds or more, or `total` seconds
    of sound altogether. A cough, a sneeze, a click or a key press is shorter than that (Marek 2026-10-17: junk with
    the person talking is never cut)."""
    parts = [min(e, b) - max(s, a) for s, e in runs if e > a and s < b]
    parts = [p for p in parts if p > 0]
    return any(p >= longest for p in parts) or sum(parts) >= total


def picture_changes(path, start, seconds):
    """Share of the picture that changes between frames 0.5 s apart, from `start` for `seconds`: [(time, share)]."""
    p = subprocess.run([tool("ffmpeg"), "-hide_banner", "-loglevel", "error", "-ss", "%.3f" % max(0, start), "-t",
                        "%.3f" % seconds, "-i", path, "-an", "-vf", "fps=%d,scale=%d:%d,format=gray" % (FPS, W, H),
                        "-f", "rawvideo", "-"], capture_output=True)
    data, n = p.stdout, W * H
    frames = [data[i:i + n] for i in range(0, len(data) - n + 1, n)]
    out = []
    for i in range(1, len(frames)):
        a, b = frames[i - 1], frames[i]
        changed = sum(1 for x, y in zip(a, b) if abs(x - y) > 14)
        out.append((max(0, start) + i / float(FPS), changed / float(n)))
    return out


def _calm_runs(changes, busy, hard, need):
    """[(from, to)] of stretches at least `need` seconds long where the picture stays put (a slide, a title card):
    nothing moves beyond `busy`, and a hard change (a new slide) ends the stretch."""
    runs, first = [], None
    for at, share in changes:
        if share <= busy:
            if first is None:
                first = at - 1.0 / FPS
        else:
            if first is not None and at - 1.0 / FPS - first >= need:
                runs.append((first, at - 1.0 / FPS))
            first = None
    if first is not None and changes and changes[-1][0] - first >= need:
        runs.append((first, changes[-1][0]))
    return runs


def _junk(changes, busy, hard):
    """Setup activity in a stretch: a moving cursor / clicks (busy seconds) or picture jumps (a desktop -> slides)."""
    busy_secs = sum(1.0 / FPS for _, s in changes if busy < s < hard)
    jumps = sum(1 for _, s in changes if s >= hard)
    return busy_secs >= 1.5 or jumps >= 1, busy_secs, jumps


def health(path, cfg=None):
    """The video health check. Returns {"block": [...], "fixes": [...], "flags": [...], "af": audio filter or None,
    "start": seconds cut at the start or None, "end": where the talk ends or None, "audio": levels, "sound_percent"}.
    "block" = not good enough for a conference talk (no sound / muted / almost no sound): the talk is not uploaded."""
    cfg = cfg or {}
    window = float(cfg.get("health_window_seconds", 180))
    max_cut = float(cfg.get("health_max_cut_seconds", 120))
    calm_need = float(cfg.get("health_calm_seconds", 15))
    length = probe(path)["duration"]
    rep = {"block": [], "fixes": [], "flags": [], "af": None, "start": None, "end": None, "length": round(length, 1)}
    lv = audio_levels(path)
    rep["audio"] = lv
    if not lv:
        rep["block"].append("no sound track")
        return rep
    if lv["max"] < -50:
        rep["block"].append("the sound is muted (loudest moment %.0f dB)" % lv["max"])
        return rep
    if lv["channels"] == 2 and "left" in lv and "right" in lv:
        l, r, m = lv["left"], lv["right"], lv.get("mono", -91.0)
        if r < l - 30:
            rep["af"], how = "pan=stereo|c0=c0|c1=c0", "the sound was only on the left channel - copied to both"
        elif l < r - 30:
            rep["af"], how = "pan=stereo|c0=c1|c1=c1", "the sound was only on the right channel - copied to both"
        elif m < min(l, r) - 15:
            rep["af"], how = "pan=stereo|c0=c0|c1=c0", "the two channels cancel each other out - kept the left one"
        else:
            how = None
        if how:
            rep["fixes"].append(how)
    loud = lv.get("mono", lv["max"]) if lv["channels"] != 2 or not rep["af"] else max(lv.get("left", -91), lv.get("right", -91))
    noise = min(-30.0, max(-55.0, loud - 15))
    runs = sound_runs(path, rep["af"], noise, length)
    sound = sum(e - s for s, e in runs)
    rep["sound_percent"] = round(100 * sound / length, 1) if length else 0
    if length and rep["sound_percent"] < float(cfg.get("health_min_sound_percent", 15)):
        rep["block"].append("almost no sound - only %.0f%% of the video has any" % rep["sound_percent"])
        return rep
    # the picture: how much moves in the talk's middle is its normal level (a webcam corner moves all the time)
    mid = picture_changes(path, length / 2 - 30, 60) if length > 120 else []
    shares = sorted(s for _, s in mid)
    normal = shares[int(len(shares) * 0.9)] if shares else 0.0
    if normal > 0.10:
        rep["flags"].append("camera-style video (the picture moves all the time) - start and end not checked")
        return rep
    busy, hard = max(6.0 / (W * H), 2.5 * normal), 0.30      # busy: 6+ pixels move (a cursor) beyond the normal
    w = min(window, length / 3)
    head = picture_changes(path, 0, w)
    calm = _calm_runs(head, busy, hard, calm_need)
    if calm and calm[0][0] > 0.5:
        t0 = calm[0][0]
        seen, busy_s, jumps = _junk([c for c in head if c[0] <= t0 + 1.0 / FPS], busy, hard)
        if seen and t0 <= max_cut:
            if talking(runs, 0, t0):
                rep["flags"].append("setup on screen for the first %.0f s, but the speaker talks over it - not cut" % t0)
            else:
                rep["start"] = round(t0, 2)
                rep["fixes"].append("cut %.1f s of setup at the start (%.0f s of clicking, %d picture jump(s))" % (t0, busy_s, jumps))
        elif seen:
            rep["flags"].append("setup on screen for %.0f s at the start - longer than %.0f s, not cut" % (t0, max_cut))
    tail = picture_changes(path, length - w, w)
    calm = _calm_runs(tail, busy, hard, calm_need)
    if calm and length - calm[-1][1] > 1.5:
        t1 = calm[-1][1]
        seen, busy_s, jumps = _junk([c for c in tail if c[0] > t1], busy, hard)
        if seen and length - t1 <= max_cut:
            if talking(runs, t1, length):
                rep["flags"].append("setup on screen in the last %.0f s, but the speaker talks over it - not cut" % (length - t1))
            else:
                rep["end"] = round(t1 + 0.2, 2)
                rep["fixes"].append("cut %.1f s of setup at the end (%.0f s of clicking, %d picture jump(s))" % (length - t1, busy_s, jumps))
        elif seen:
            rep["flags"].append("setup on screen for %.0f s at the end - longer than %.0f s, not cut" % (length - t1, max_cut))
    return rep


def fix_audio(src, dst, af):
    """Only the sound needs fixing: the picture is copied as it is, the sound re-encoded through `af`."""
    tmp = "%s.%d.part.mp4" % (dst, os.getpid())
    r = run([tool("ffmpeg"), "-hide_banner", "-loglevel", "error", "-y", "-i", src, "-map", "0:v:0", "-map", "0:a:0",
             "-c:v", "copy", "-af", af, "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", tmp])
    if r.returncode != 0 or not os.path.exists(tmp):
        raise RuntimeError("ffmpeg sound fix failed: " + r.stderr[-300:])
    os.replace(tmp, dst)
    return dst
