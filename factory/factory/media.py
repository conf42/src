"""ffprobe / ffmpeg helpers: source probe, YouTube-level loudness, QA measurement."""
import glob
import json
import os
import re
import shutil
import subprocess

RESOLUTIONS = [(480, "480p"), (720, "720p"), (1080, "1080p"), (1440, "1440p"), (2160, "4K")]


def tool(name):
    found = shutil.which(name)
    if found:
        return found
    hits = glob.glob(os.path.expanduser(r"~\AppData\Local\Microsoft\WinGet\Packages\*FFmpeg*\*\bin\%s.exe" % name))
    if hits:
        return hits[0]
    raise RuntimeError("%s not found - install it with: winget install Gyan.FFmpeg" % name)


def run(args):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe(path):
    out = run([tool("ffprobe"), "-v", "error", "-show_entries", "stream=codec_type,width,height:format=duration",
               "-of", "json", path]).stdout
    d = json.loads(out or "{}")
    v = next((s for s in d.get("streams", []) if s.get("codec_type") == "video"), {})
    return {"width": v.get("width") or 0, "height": v.get("height") or 0,
            "duration": float((d.get("format") or {}).get("duration") or 0)}


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
    tmp = dst + ".part.mp4"
    r = run([tool("ffmpeg"), "-hide_banner", "-loglevel", "error", "-y", "-i", src, "-c:v", "copy", "-af", af,
             "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", tmp])
    if r.returncode != 0 or not os.path.exists(tmp):
        raise RuntimeError("ffmpeg loudness step failed: " + r.stderr[-400:])
    os.replace(tmp, dst)
