"""The recorder's overlay, swapped after the fact (Marek 2026-11-15).

A speaker who is on two lineups can record talk A with conference B picked in conf42.com/record: the video then
carries B's overlay (title band, colours, date) on every frame. The overlay is a 1920 x 1080 picture, opaque
everywhere except its holes (the slides' window, the camera circles), drawn by docs/assets/js/overlays.js
(ovDrawNew) - the same code the recorder and the teasers' Overlays tab use. So the fix is exact and free: draw the
RIGHT conference's overlay and lay it over the video. Slides and camera show through the holes untouched.

    python -m factory overlay <video> <from short_url> <to short_url> [out.mp4]

- render(slug, kind, dest): the overlay PNG, drawn by headless Chrome from the live site's own overlays.js and the
  event's data on conf42.com/<slug>/teasers (no copy of the drawing code here, so it can never drift).
- kind_of(video, slug): which of the three overlays the recording used (default / co-talk / no-facecam), by comparing
  frames with each one where the overlay is opaque. Also the safety check: when none fits, nothing is swapped.
- swap(video, old, new, dest): the new overlay over the whole video, one encode, sound copied.
"""
import json
import os
import re
import shutil
import subprocess
import tempfile

import requests

from . import media

SITE = "https://www.conf42.com/"
KINDS = ("default", "no-facecam", "co-talk")
MAX_DIFF = 14.0          # mean difference (0-255) between a frame and the overlay it should carry; a match is 2-6

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<style>html,body{margin:0;padding:0;background:transparent;overflow:hidden}canvas{display:block}</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:wght@700&display=block">
<script src="%(site)sassets/js/overlays.js"></script></head><body><canvas id="c" width="1920" height="1080"></canvas>
<script>
var D = %(data)s, KIND = %(kind)s;
function pic(src) { var im = new Image(); im.crossOrigin = 'anonymous'; im.src = src;
  return new Promise(function (f) { im.onload = im.onerror = function () { f(im.naturalWidth ? im : null); }; }); }
Promise.all([document.fonts.load('700 32px Lato').catch(function () {}), pic('%(site)sassets/conf42/conf42_planet_white.png'),
             pic('%(site)sassets/conf42/conf42_sticker_2026.png')]).then(function (r) {
  ovDrawNew(document.getElementById('c'), KIND, D, { planet: r[1], sticker: r[2] && blend(r[2]) });
  document.title = 'drawn' + (r[1] && r[2] && document.fonts.check('700 32px Lato') ? '' : ' (assets missing)');
});
</script></body></html>
"""


def chrome():
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        p = shutil.which(name)
        if p:
            return p
    for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
        if os.path.exists(p):
            return p
    raise RuntimeError("no Chrome on this machine (the overlay is drawn by headless Chrome)")


def data(slug):
    """What the event's overlay shows: {color, pools, title, date, slug} from its teasers page."""
    r = requests.get(SITE + slug + "/teasers", timeout=60)
    r.raise_for_status()
    m = re.search(r'<script type="application/json" id="ov-data">(.*?)</script>', r.text, re.S)
    if not m:
        raise RuntimeError("conf42.com/%s/teasers has no overlay data" % slug)
    d = json.loads(m.group(1))
    if not d.get("title") or not d.get("color"):
        raise RuntimeError("conf42.com/%s/teasers: overlay data incomplete" % slug)
    return d


def render(slug, kind, dest, d=None):
    """The event's overlay as a 1920 x 1080 PNG with transparent holes. Returns dest."""
    from PIL import Image
    d = d or data(slug)
    with tempfile.TemporaryDirectory() as tmp:
        page = os.path.join(tmp, "overlay.html")
        with open(page, "w", encoding="utf-8") as f:
            f.write(PAGE % {"site": SITE, "data": json.dumps(d), "kind": json.dumps(kind)})
        shot = os.path.join(tmp, "shot.png")
        cmd = [chrome(), "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=1",
               "--window-size=1920,1080", "--default-background-color=00000000", "--virtual-time-budget=20000",
               "--user-data-dir=" + os.path.join(tmp, "profile"), "--screenshot=" + shot, "file:///" + page.replace("\\", "/").lstrip("/")]
        r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
        if not os.path.exists(shot):
            raise RuntimeError("Chrome drew no overlay: %s" % (r.stderr or "")[-300:])
        with Image.open(shot) as im:
            im = im.convert("RGBA")
            if im.size != (1920, 1080):
                raise RuntimeError("overlay came out %dx%d, not 1920x1080" % im.size)
            alpha = im.getchannel("A")
            opaque = sum(1 for a in alpha.resize((192, 108)).getdata() if a > 250) / (192 * 108.0)
            # default: ~35 % of the frame is overlay; the big window: ~20 %; nothing drawn = 0, no holes = 100
            if not .08 < opaque < .75:
                raise RuntimeError("the overlay for %s (%s) looks wrong: %.0f%% of it is opaque" % (slug, kind, opaque * 100))
            im.save(dest)
    return dest


def frames(video, n=3):
    """n frames spread over the video, as 480 x 270 RGB images."""
    from PIL import Image
    length = media.probe(video)["duration"] if hasattr(media, "probe") else 0
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(n):
            at = (length or 60) * (i + 1) / (n + 1)
            p = os.path.join(tmp, "f%d.png" % i)
            media.run([media.tool("ffmpeg"), "-hide_banner", "-loglevel", "error", "-y", "-ss", "%.2f" % at, "-i", video,
                       "-frames:v", "1", "-vf", "scale=480:270", p])
            if os.path.exists(p):
                with Image.open(p) as im:
                    out.append(im.convert("RGB").copy())
    return out


def difference(frame, overlay_png):
    """Mean difference (0-255) between a frame and an overlay where the overlay is fully opaque."""
    from PIL import Image, ImageChops, ImageStat
    with Image.open(overlay_png) as ov:
        ov = ov.convert("RGBA").resize((480, 270), Image.LANCZOS)
    mask = ov.getchannel("A").point(lambda a: 255 if a >= 254 else 0)
    if not mask.getbbox():
        return 255.0
    st = ImageStat.Stat(ImageChops.difference(frame, ov.convert("RGB")), mask)
    return sum(st.mean) / 3.0


def kind_of(video, slug, workdir, d=None):
    """(kind, difference, {kind: png}) - the overlay of `slug` the recording carries, the best of the three; kind is
    None when none fits (not this event's overlay, an OBS recording, a layout changed mid-talk)."""
    fr = frames(video)
    if not fr:
        return None, 255.0, {}
    d = d or data(slug)
    best, pngs = (None, 255.0), {}
    for kind in KINDS:
        pngs[kind] = render(slug, kind, os.path.join(workdir, "%s-%s.png" % (slug, kind)), d)
        diff = max(difference(f, pngs[kind]) for f in fr)     # every frame must carry it
        if diff < best[1]:
            best = (kind, diff)
    return (best[0] if best[1] <= MAX_DIFF else None), best[1], pngs


def swap(video, old_slug, new_slug, dest, log=print):
    """Lay new_slug's overlay over a recording made with old_slug's. Returns {"kind", "before", "after"} (the
    differences to the old overlay before and to the new one after); raises when the recording does not carry
    old_slug's overlay or the result does not carry the new one - then nothing is left at dest."""
    s = media.run([media.tool("ffprobe"), "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                   "-of", "csv=p=0", video]).stdout.strip().split(",")
    w, h = (int(s[0]), int(s[1])) if len(s) >= 2 and s[0].isdigit() else (0, 0)
    if not w or abs(w / float(h) - 16 / 9.0) > .01:
        raise RuntimeError("the video is %sx%s, not 16:9 - the overlay can't be swapped" % (w, h))
    with tempfile.TemporaryDirectory() as tmp:
        kind, before, _ = kind_of(video, old_slug, tmp)
        if not kind:
            raise RuntimeError("the video does not carry the %s overlay (closest difference %.0f)" % (old_slug, before))
        png = render(new_slug, kind, os.path.join(tmp, "new.png"))
        log("overlay: %s -> %s (%s layout, old overlay matched at %.1f)" % (old_slug, new_slug, kind, before))
        part = dest + ".%d.part.mp4" % os.getpid()
        r = media.run([media.tool("ffmpeg"), "-hide_banner", "-loglevel", "error", "-y", "-i", video, "-i", png, "-filter_complex",
                       "[1:v]scale=%d:%d:flags=lanczos[ov];[0:v][ov]overlay=0:0:format=auto,format=yuv420p[v]" % (w, h),
                       "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-c:a", "copy",
                       "-movflags", "+faststart", part])
        if r.returncode != 0 or not os.path.exists(part):
            if os.path.exists(part):
                os.remove(part)
            raise RuntimeError("overlay swap failed: " + (r.stderr or "")[-300:])
        after = max(difference(f, png) for f in frames(part)) if frames(part) else 255.0
        if after > MAX_DIFF:
            os.remove(part)
            raise RuntimeError("the swapped video does not carry the %s overlay (difference %.0f)" % (new_slug, after))
        os.replace(part, dest)
    return {"kind": kind, "before": round(before, 1), "after": round(after, 1)}


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    video, old, new = argv[:3]
    dest = argv[3] if len(argv) > 3 else os.path.splitext(video)[0] + " (%s overlay).mp4" % new
    print(swap(video, old, new, dest), "->", dest)
    return 0
