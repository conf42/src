"""YouTube thumbnails on conf42.com/<event>/teasers (Marek 2026-10-12): the last tab, one 1280x720 PNG per talk, as the
channel's thumbnails have always looked - the event's starfield and the speaker's base headshot, keyed out and centred.

    python -m build.youtube_thumbnails [--cached-only] [--prune]

The backgrounds are thumbnails/<event name>.png (Marek's templates, e.g. "DevSecOps.png", "Remix 2026.png": the event's
name, or its name and year). An event without one gets the shared starfield (thumbnails/DevOps.png, the one template
nothing clips) tinted with its metadata.yml colour, the colour its headshots were made in.

The key: a base headshot is a grey person on that same kind of tinted starfield, so the person is whatever carries no
tint. Per pixel, the tint left in it against the tint of the sky behind it (filled in from the clearly tinted pixels
around) gives its opacity; the person is then the blobs touching the bottom edge, holes filled, with the soft edge kept
only on the outline (hair). The headshot is scaled to the full 720 px height and centred, like the published ones.

Pages: teasers.py writes each event's talks into the page (<script id="th-data">); the PNGs land next to it as
conf42-<event>-<speaker>-thumbnail.png. Pillow + numpy only, about 0.5 s a picture, so like the teaser cards they are
drawn after the deploy: content-addressed cache in .cache/thumbnails/<key>.png (key: VERSION, the headshot's bytes,
the background's bytes or tint). --cached-only (the deploy) only copies cached pictures; without it (the render job)
the missing ones are drawn too, and rendered=<n> goes to $GITHUB_OUTPUT so the workflow queues one more deploy.
Past events are not on the teaser pages, so nothing here ever redraws them. Never fails the build.
"""
import glob
import hashlib
import json
import os
import re
import shutil
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO

try:
    import numpy as np
    from PIL import Image
    from scipy import ndimage
except ImportError:  # pragma: no cover
    print("WARN youtube_thumbnails: Pillow/numpy/scipy missing, no thumbnails")
    sys.exit(0)

ROOT = "docs"
TEMPLATES = "thumbnails"
BASE = "DevOps.png"          # the starfield tinted for events without a template of their own
W, H = 1280, 720
VERSION = "1"                # bump when the drawing changes: every thumbnail is redrawn
CACHE_DIR = os.path.join(os.environ.get("SITE_CACHE_DIR", ".cache"), "thumbnails")
PRUNE_DAYS = 14
DATA_RE = re.compile(r'<script type="application/json" id="th-data">(.*?)</script>', re.S)
_photos = {}


def photo(url):
    """the headshot's bytes (3 tries), or None"""
    if url not in _photos:
        _photos[url] = None
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "conf42-youtube-thumbnails"})
                _photos[url] = urllib.request.urlopen(req, timeout=20).read()
                break
            except Exception:
                time.sleep(1 + attempt)
    return _photos[url]


def template_for(names):
    """thumbnails/<name>.png for the first name that has one"""
    for n in names:
        p = os.path.join(TEMPLATES, n + ".png")
        if n and os.path.isfile(p):
            return p
    return None


def background(template, tint):
    """the 1280x720 sky: the event's template, or the shared starfield in its colour"""
    if template:
        return np.asarray(Image.open(template).convert("RGB").resize((W, H), Image.LANCZOS)).astype(float)
    lum = np.asarray(Image.open(os.path.join(TEMPLATES, BASE)).convert("RGB").resize((W, H), Image.LANCZOS)).astype(float)[..., 0] / 225.0
    c = np.array([int(tint[i:i + 2], 16) for i in (1, 3, 5)], float)
    c = (c / max(c.max(), 1)) ** 1.6                       # a little richer than the flat brand colour, as the templates are
    return 255 * np.tanh(lum[..., None] * c * 330 / 255)  # highlights soften towards white instead of clipping


def _fill(val, mask):
    """val (h x w x c) where mask (h x w, 0..1) is 0, filled smoothly from where it is known (pyramid push-pull)"""
    levels, v, m = [], val * mask[..., None], mask.copy()
    while min(m.shape) > 2:
        levels.append((v, m))
        h2, w2 = (m.shape[0] + 1) // 2, (m.shape[1] + 1) // 2
        pv, pm = np.zeros((h2 * 2, w2 * 2, v.shape[2])), np.zeros((h2 * 2, w2 * 2))
        pv[:v.shape[0], :v.shape[1]], pm[:m.shape[0], :m.shape[1]] = v, m
        v, m = pv.reshape(h2, 2, w2, 2, -1).sum((1, 3)), pm.reshape(h2, 2, w2, 2).sum((1, 3))
    out = v / np.maximum(m, 1e-6)[..., None]
    for v, m in reversed(levels):
        up = np.repeat(np.repeat(out, 2, 0), 2, 1)[:m.shape[0], :m.shape[1]]
        k = np.clip(m, 0, 1)[..., None]
        out = v / np.maximum(m, 1e-6)[..., None] * k + up * (1 - k)
    return out


def key_out(img):
    """(grey person, opacity) of a base headshot, both h x w floats; opacity None when the photo is not one (no tinted sky)"""
    P = np.asarray(img.convert("RGB")).astype(float)
    h, w, _ = P.shape
    chroma = P - P.mean(2, keepdims=True)                   # ~0 on the grey person
    top = chroma[: h // 2].reshape(-1, 3)                   # the sky's tint: the most tinted fifth of the upper half
    norm = np.linalg.norm(top, axis=1)
    c = np.median(top[norm >= np.percentile(norm, 80)], 0)
    if np.linalg.norm(c) < 8:                               # no tinted sky at all: not a base headshot
        return P.mean(2), None
    d = c / np.linalg.norm(c)
    p = (chroma * d).sum(2)                                 # how much of the sky's tint each pixel carries
    sky = (p > 7).astype(float)
    for _ in range(2):
        B = _fill(P, sky)
        a = np.clip(1 - p / np.maximum(((B - B.mean(2, keepdims=True)) * d).sum(2), 1), 0, 1)
        sky = (a < .08).astype(float) * (p > 3)
    lab, n = ndimage.label(a > .5)
    sizes = ndimage.sum(np.ones_like(lab), lab, range(n + 1))
    keep = np.zeros(n + 1, bool)
    for i in set(lab[-1][lab[-1] > 0]):                     # the people stand on the bottom edge (one or two of them)
        keep[i] = sizes[i] > .03 * h * w
    body = ndimage.binary_fill_holes(keep[lab])
    if not .08 < body.mean() < .95:
        return P.mean(2), None
    inside, outside = ndimage.distance_transform_edt(body), ndimage.distance_transform_edt(~body)
    alpha = np.where(inside > 4, 1.0, np.where(outside > 4, 0.0, a))
    alpha = ndimage.gaussian_filter(alpha, .9)              # a soft, photographic edge
    alpha = np.where(inside > 6, 1.0, np.where(outside > 6, 0.0, alpha))
    ramp = np.clip(np.minimum(np.arange(w), np.arange(w)[::-1]) / 24.0, 0, 1)
    alpha = alpha * ramp[None, :]                           # shoulders cut by the photo's own frame fade out
    grey = (P.mean(2) - (1 - alpha) * B.mean(2)) / np.maximum(alpha, 1e-3)   # without the sky shining through
    grey = np.where(alpha > .98, P.mean(2), np.clip(grey, 0, 255))
    return grey, alpha


def draw(head_bytes, sky):
    grey, alpha = key_out(Image.open(BytesIO(head_bytes)))
    h, w = grey.shape
    if alpha is None:                                       # not keyable: the photo as it is, edges faded
        yy, xx = np.mgrid[0:h, 0:w]
        alpha = np.clip(np.minimum.reduce([xx, w - 1 - xx, yy * 4, (h - 1 - yy) * 4]) / 30.0, 0, 1)
    fw = round(w * H / h)
    G = np.asarray(Image.fromarray(grey.astype(np.uint8)).resize((fw, H), Image.LANCZOS)).astype(float)
    A = np.asarray(Image.fromarray((alpha * 255).astype(np.uint8)).resize((fw, H), Image.LANCZOS)).astype(float)[..., None] / 255
    out = sky.copy()
    x0 = (W - fw) // 2
    sx0, sx1 = max(0, -x0), fw - max(0, x0 + fw - W)        # a photo wider than 16:9 is cut at the sides
    region = out[:, max(0, x0):max(0, x0) + sx1 - sx0]
    out[:, max(0, x0):max(0, x0) + sx1 - sx0] = A[:, sx0:sx1] * G[:, sx0:sx1, None] + (1 - A[:, sx0:sx1]) * region
    return Image.fromarray(np.clip(out + .5, 0, 255).astype(np.uint8))


def main():
    cached_only = "--cached-only" in sys.argv
    out = os.environ.get("GITHUB_OUTPUT")
    drawn, reused, left, used = 0, 0, 0, set()
    os.makedirs(CACHE_DIR, exist_ok=True)
    for page in sorted(glob.glob(os.path.join(ROOT, "*", "teasers.html"))):
        here = os.path.dirname(page)
        m = DATA_RE.search(open(page, encoding="utf-8").read())
        if not m:
            continue
        data = json.loads(m.group(1))
        template = template_for(data.get("templates") or [])
        bg_id = hashlib.sha256(open(template, "rb").read()).hexdigest() if template else "tint " + data.get("tint", "#838383")
        if not template:
            bg_id += hashlib.sha256(open(os.path.join(TEMPLATES, BASE), "rb").read()).hexdigest()
        talks = data.get("talks") or []
        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(photo, [t["photo"] for t in talks]))
        sky, n_drawn, n_left = None, 0, 0
        for t in talks:
            head = photo(t["photo"])
            if head is None:
                print("WARN youtube_thumbnails %s: %s could not be fetched" % (os.path.basename(here), t["photo"]))
                continue
            key = hashlib.sha256(("%s|%s|" % (VERSION, bg_id)).encode() + hashlib.sha256(head).digest()).hexdigest()
            used.add(key + ".png")
            cached, dest = os.path.join(CACHE_DIR, key + ".png"), os.path.join(here, t["file"])
            if os.path.exists(cached):
                shutil.copyfile(cached, dest)
                os.utime(cached)
                reused += 1
                continue
            if cached_only:
                n_left += 1
                continue
            try:
                if sky is None:
                    sky = background(template, data.get("tint") or "#838383")
                draw(head, sky).save(dest, "PNG", optimize=True)
                shutil.copyfile(dest, cached)
                n_drawn += 1
            except Exception as e:
                print("WARN youtube_thumbnails %s: %s: %s" % (os.path.basename(here), t["file"], e))
        drawn, left = drawn + n_drawn, left + n_left
        print("youtube_thumbnails %s: %d talks, %d drawn, %d left for the render job (%s)"
              % (os.path.basename(here), len(talks), n_drawn, n_left, template or "tinted " + data.get("tint", "")))
    if "--prune" in sys.argv:
        cut, gone = time.time() - PRUNE_DAYS * 86400, 0
        for f in glob.glob(os.path.join(CACHE_DIR, "*.png")):
            if os.path.basename(f) not in used and os.path.getmtime(f) < cut:
                os.remove(f)
                gone += 1
        print("youtube_thumbnails: pruned %d cache entries unused for %d days" % (gone, PRUNE_DAYS))
    print("youtube_thumbnails: %d drawn, %d from cache, %d left" % (drawn, reused, left))
    if out:
        with open(out, "a") as f:
            f.write("rendered=%d\n" % drawn)


if __name__ == "__main__":
    main()
