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


def render(src, dst, max_short_side=1080, cq=21, on_progress=None):
    """Re-encode a source video to a lean H.264/AAC MP4 before the upload (camera .mov files are huge for no gain):
    GPU (NVENC) when there is one, else libx264; short side capped at max_short_side, audio kept at 48 kHz 192k so
    Studio Sound still gets a clean signal. Returns dst, or src when the render would not be smaller."""
    info = probe(src)
    w, h = info["width"], info["height"]
    big = w and h and min(w, h) > max_short_side
    size = ("-2:%d" % max_short_side) if h <= w else ("%d:-2" % max_short_side)
    audio = ["-map", "0:v:0", "-map", "0:a:0?", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart"]
    nvenc = ["-c:v", "h264_nvenc", "-preset", "p5", "-rc", "vbr", "-cq", str(cq), "-b:v", "0"]
    head = ["-hide_banner", "-loglevel", "error", "-y"]
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
                                   info["duration"], lambda pct: on_progress and on_progress(
                                       "rendering to mp4 on the %s - %d%%" % (how, pct), pct))
        if rc == 0 and verify(part, info["duration"]) is None:
            break
        if rc == 0:
            err = "rendered file failed the check: " + verify(part, info["duration"])
        if os.path.exists(part):
            os.remove(part)
    else:
        raise RuntimeError("render to mp4 failed: " + err[-300:])
    if os.path.getsize(part) >= os.path.getsize(src):
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


def normalize(src, dst, lufs, tp):
    """Two-pass loudnorm to the target; the video stream is copied untouched."""
    first = run([tool("ffmpeg"), "-hide_banner", "-nostats", "-i", src, "-af",
                 "loudnorm=I=%s:TP=%s:LRA=11:print_format=json" % (lufs, tp), "-f", "null", "-"]).stderr
    m = json.loads(first[first.rfind("{"):first.rfind("}") + 1])
    af = ("loudnorm=I={I}:TP={TP}:LRA=11:measured_I={mi}:measured_TP={mtp}:measured_LRA={mlra}:"
          "measured_thresh={mth}:offset={off}:linear=true").format(
        I=lufs, TP=tp, mi=m["input_i"], mtp=m["input_tp"], mlra=m["input_lra"], mth=m["input_thresh"], off=m["target_offset"])
    tmp = "%s.%d.part.mp4" % (dst, os.getpid())
    r = run([tool("ffmpeg"), "-hide_banner", "-loglevel", "error", "-y", "-i", src, "-c:v", "copy", "-af", af,
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", tmp])
    if r.returncode != 0 or not os.path.exists(tmp):
        raise RuntimeError("ffmpeg loudness step failed: " + r.stderr[-400:])
    os.replace(tmp, dst)
