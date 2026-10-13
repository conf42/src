"""YouTube thumbnails on conf42.com/<event>/teasers (Marek 2026-10-12): the last tab, one 1280x720 PNG per talk, as the
channel's thumbnails have always looked - the speaker's base headshot, keyed out and centred, on its own sky.

    python -m build.youtube_thumbnails [--cached-only] [--prune]

The sky (Marek 2026-10-12): the thumbnail's background is the headshot background stretched out to 16:9 - never a
template or the event's metadata colour (both came out in the wrong tint). A topic's headshots share one background across
the years ("_prompt", "_platform", ...), so thumbnails/<suffix>.png holds it clean, 500x400: per pixel, the median of
every headshot of that suffix that shows sky there (those that don't match the rest are left out), made once from the
static repo with

    python -m build.youtube_thumbnails --skies ../static/headshots [<suffix> ...]

(only the headshots of the 2025-2027 talk sheets: topics changed their background over the years)

and committed. A headshot whose suffix has no sky file yet gets its event's median the same way, from that event's photos.

The key: a base headshot is a grey person on a tinted starfield, so the person is whatever carries no tint. Per pixel,
the tint left in it against the tint of the sky behind it (filled in from the clearly tinted pixels around) gives its
opacity. The person is then the blobs touching the bottom edge, holes filled, with the soft edge kept only on the
outline (hair). The headshot is scaled to the full 720 px height and centred, like the published ones.

Pages: teasers.py writes each event's talks into the page (<script id="th-data">), and the PNGs land next to it as
conf42-<event>-<speaker>-thumbnail.png. It uses Pillow + numpy + scipy at about 0.6 s a picture, so like the teaser cards they are
drawn after the deploy. The cache is content-addressed in .cache/thumbnails/<key>.png, keyed on VERSION and the headshot's bytes
only: a new speaker's photo shifts the median a hair, but never redraws the others. --cached-only (the deploy) only copies cached
pictures. Without it (the render job) the missing ones are drawn too, and rendered=<n> goes to $GITHUB_OUTPUT so the workflow
queues one more deploy. Past events are not on the teaser pages, so nothing here ever redraws them. It never fails the build.
"""
import glob
import hashlib
import json
import os
import re
import shutil
import sys
import time
import urllib.parse
import urllib.request
import warnings
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
W, H = 1280, 720
SKIES = "thumbnails"         # <suffix>.png: a topic's clean headshot background; _starfield.png: the art behind the heads
VERSION = "2"                # bump when the drawing changes: every thumbnail is redrawn
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


def _fill(val, mask):
    """val (h x w x c) where mask (h x w) is 0, filled smoothly from where it is known: each unknown pixel takes the
    known pixels around it, blurred at the smallest scale (2 ... 128 px) that has enough of them (normalised convolution)"""
    known = mask > .5
    out = val.astype(float).copy()
    todo = ~known
    def blur(x, sigma):                                     # big blurs on a shrunk copy: same look, a fraction of the time
        f = max(1, sigma // 4)
        if f == 1:
            return ndimage.gaussian_filter(x, sigma)
        small = ndimage.gaussian_filter(ndimage.zoom(x, 1.0 / f, order=1), sigma / f)
        return ndimage.zoom(small, (x.shape[0] / small.shape[0], x.shape[1] / small.shape[1]), order=1)[:x.shape[0], :x.shape[1]]
    for sigma in (2, 4, 8, 16, 32, 64, 128):
        if not todo.any():
            break
        den = blur(known.astype(float), sigma)
        num = np.stack([blur(np.where(known, val[..., c], 0.0), sigma) for c in range(val.shape[2])], -1)
        here = todo & (den > .25)
        out[here] = num[here] / den[here][:, None]
        todo &= ~here
    if todo.any():
        out[todo] = val[known].mean(0) if known.any() else 0
    return ndimage.gaussian_filter(out, (1.5, 1.5, 0)) * (~known)[..., None] + out * known[..., None]


def key_out(img, plate=None):
    """(pixels, grey person, opacity, sky) of a base headshot: h x w(x3) floats and the mask of the pixels that are clearly
    sky (well clear of the person); opacity and sky are None when the photo is not one (no tinted sky). plate: the topic's
    clean sky (thumbnails/<suffix>.png) - a pixel that matches it is sky even when it carries no tint (the darkest night
    at the top is almost grey and was keyed as hair)"""
    P = np.asarray(img.convert("RGB")).astype(float)
    h, w, _ = P.shape
    chroma = P - P.mean(2, keepdims=True)                   # ~0 on the grey person
    top = chroma[: h // 2].reshape(-1, 3)                   # the sky's tint: the most tinted fifth of the upper half
    norm = np.linalg.norm(top, axis=1)
    c = np.median(top[norm >= np.percentile(norm, 80)], 0)
    if np.linalg.norm(c) < 8:                               # no tinted sky at all: not a base headshot
        return P, P.mean(2), None, None
    d = c / np.linalg.norm(c)
    p = (chroma * d).sum(2)                                 # how much of the sky's tint each pixel carries
    sky = (p > 7).astype(float)
    for _ in range(2):
        B = _fill(P, sky)
        a = np.clip(1 - p / np.maximum(((B - B.mean(2, keepdims=True)) * d).sum(2), 1), 0, 1)
        sky = (a < .08).astype(float) * (p > 3)
    if plate is not None and plate.shape == P.shape:
        a = np.minimum(a, np.clip((np.abs(P - plate).max(2) - 6) / 14.0, 0, 1))
    lab, n = ndimage.label(a > .5)
    sizes = ndimage.sum(np.ones_like(lab), lab, range(n + 1))
    keep = np.zeros(n + 1, bool)
    for i in set(lab[-1][lab[-1] > 0]):                     # the people stand on the bottom edge (one or two of them)
        keep[i] = sizes[i] > .03 * h * w
    body = ndimage.binary_fill_holes(keep[lab])
    if not .08 < body.mean() < .95:
        return P, P.mean(2), None, None
    inside, outside = ndimage.distance_transform_edt(body), ndimage.distance_transform_edt(~body)
    alpha = np.where(inside > 4, 1.0, np.where(outside > 4, 0.0, a))
    alpha = ndimage.gaussian_filter(alpha, .9)              # a soft, photographic edge
    alpha = np.where(inside > 6, 1.0, np.where(outside > 6, 0.0, alpha))
    ramp = np.clip(np.minimum(np.arange(w), np.arange(w)[::-1]) / 24.0, 0, 1)
    alpha = alpha * ramp[None, :]                           # shoulders cut by the photo's own frame fade out
    grey = (P.mean(2) - (1 - alpha) * B.mean(2)) / np.maximum(alpha, 1e-3)   # without the sky shining through
    grey = np.where(alpha > .98, P.mean(2), np.clip(grey, 0, 255))
    return P, grey, alpha, (outside > 5) & (a < .02)


def event_sky(keyed):
    """the event's headshot background (h x w x 3, NaN where none of them shows sky): per pixel, the median of the
    headshots that show it - only those of the usual size, so one odd photo can't skew it"""
    shape = max(((k[0].shape, sum(1 for x in keyed if x[0].shape == k[0].shape)) for k in keyed if k[3] is not None),
                key=lambda x: x[1], default=(None, 0))[0]
    stack = [np.where(k[3][..., None], k[0], np.nan) for k in keyed if k[3] is not None and k[0].shape == shape]
    if not stack:
        return None
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)     # "All-NaN slice": a pixel no headshot shows stays NaN
        return np.nanmedian(np.array(stack), 0)


def draw(keyed, ev_sky, whole=False):
    """whole: ev_sky is the topic's clean sky, used as it is; otherwise this headshot's own sky where it shows, the
    event's elsewhere, the rest filled. Either way stretched to 16:9."""
    P, grey, alpha, sky = keyed
    h, w = grey.shape
    bg = np.full(P.shape, np.nan)
    if ev_sky is not None and whole:
        bg = np.asarray(Image.fromarray(np.clip(ev_sky + .5, 0, 255).astype(np.uint8)).resize((w, h), Image.LANCZOS)).astype(float) \
            if ev_sky.shape != P.shape else ev_sky.copy()
    elif ev_sky is not None and ev_sky.shape == P.shape:
        bg = ev_sky.copy()
    if sky is not None and not whole:
        bg[sky] = P[sky]
    known = ~np.isnan(bg[..., 0])
    if not known.any():                                     # nothing to go on: the photo's own average colour
        bg, known = np.broadcast_to(P.reshape(-1, 3).mean(0), P.shape).copy(), np.ones((h, w), bool)
    bg = np.where(known[..., None], bg, _fill(np.nan_to_num(bg), known.astype(float)))
    sky_img = np.asarray(Image.fromarray(np.clip(bg + .5, 0, 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)).astype(float)
    if alpha is None:                                       # not keyable: the photo as it is, edges faded
        yy, xx = np.mgrid[0:h, 0:w]
        alpha = np.clip(np.minimum.reduce([xx, w - 1 - xx, yy * 4, (h - 1 - yy) * 4]) / 30.0, 0, 1)
    fw = round(w * H / h)
    G = np.asarray(Image.fromarray(np.clip(grey + .5, 0, 255).astype(np.uint8)).resize((fw, H), Image.LANCZOS)).astype(float)
    A = np.asarray(Image.fromarray((alpha * 255 + .5).astype(np.uint8)).resize((fw, H), Image.LANCZOS)).astype(float)[..., None] / 255
    out = sky_img
    x0 = (W - fw) // 2
    sx0, sx1 = max(0, -x0), fw - max(0, x0 + fw - W)        # a photo wider than 16:9 is cut at the sides
    region = out[:, max(0, x0):max(0, x0) + sx1 - sx0]
    out[:, max(0, x0):max(0, x0) + sx1 - sx0] = A[:, sx0:sx1] * G[:, sx0:sx1, None] + (1 - A[:, sx0:sx1]) * region
    return Image.fromarray(np.clip(out + .5, 0, 255).astype(np.uint8))


def topic_sky_file(url):
    m = re.search(r"_([A-Za-z0-9]+)\.(?:png|jpe?g|webp)$", urllib.parse.unquote(url))
    f = m and os.path.join(SKIES, m.group(1).lower() + ".png")
    return f if f and os.path.isfile(f) else None


_skies = {}


def topic_sky(url):
    f = topic_sky_file(url)
    if f and f not in _skies:
        _skies[f] = np.asarray(Image.open(f).convert("RGB")).astype(float)
    return _skies.get(f) if f else None


def recent_headshots(years=(2025, 2026, 2027)):
    """{suffix: [file name]} of the headshots in the talk sheets of these years (_db/<TOPIC>_<year>.csv): topics changed
    their background over the years (Marek 2026-10-12), so older headshots would blur the sky"""
    import csv
    out = {}
    for f in sorted(glob.glob("./_db/*_*.csv")):
        m = re.search(r"_(\d{4})\.csv$", f)
        if not m or int(m.group(1)) not in years:
            continue
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                pic = (row.get("Picture") or "").strip()
                s = re.search(r"_([A-Za-z0-9]+)\.png$", pic)
                if s:
                    out.setdefault(s.group(1).lower(), set()).add(pic)
    return {k: sorted(v) for k, v in out.items()}


def _hidden_sky(med, seen, cnt):
    """the sky where no headshot shows it (behind the heads): the same starfield art (thumbnails/_starfield.png, one of
    Marek's YouTube templates; the headshot sky is it stretched to 573x404 and cut at x 60) mapped to this topic's colours
    by a small polynomial fitted on the seen pixels, plus the smoothed leftover difference so it meets them without a
    seam. Seen pixels are kept as measured; the border between the two is feathered by how many headshots saw a pixel."""
    T = np.asarray(Image.open(os.path.join(SKIES, "_starfield.png")).convert("RGB").resize((573, 404), Image.LANCZOS)).astype(float)[:400, 60:560] / 255

    def feats(X):
        r, g, b = X[..., 0], X[..., 1], X[..., 2]
        return np.stack([r, g, b, np.ones_like(r), r * r, g * g, b * b, r * g, r * b, g * b], -1)
    coef, *_ = np.linalg.lstsq(feats(T[seen]), med[seen], rcond=None)
    pred = feats(T) @ coef
    diff = ndimage.gaussian_filter(_fill(np.where(seen[..., None], med - pred, 0), seen.astype(float)), (6, 6, 0))
    guess = np.clip(pred + diff, 0, 255)
    w = ndimage.gaussian_filter(np.clip((cnt - 4) / 12.0, 0, 1) * seen, 2)[..., None]
    w = np.where(seen[..., None], np.maximum(w, .0), 0)
    return w * med + (1 - w) * guess


def build_skies(folder, suffixes):
    """thumbnails/<suffix>.png for each suffix (all of them when none is named): the median sky of the 500x400 base
    headshots of that suffix in the 2025-2027 talk sheets, read from folder; a second pass leaves out the headshots whose
    sky differs from that median (another background)"""
    os.makedirs(SKIES, exist_ok=True)
    recent = recent_headshots()
    for suf in [x for x in (suffixes or sorted(recent)) if x != "remix"]:   # Remix: its own rainbow, keynotes only
        imgs, skies, names = [], [], []
        for f in [os.path.join(folder, n) for n in recent.get(suf, [])]:
            if not os.path.isfile(f):
                continue
            try:
                P, _, _, sky = key_out(Image.open(f))
            except Exception as e:
                print("WARN skies %s: %s" % (f, e))
                continue
            if sky is None or P.shape != (400, 500, 3):
                continue
            sky = ndimage.binary_erosion(sky, iterations=6)   # well clear of hair: a stray strand would ghost into the median
            imgs.append(P.astype(np.uint8)); skies.append(sky); names.append(os.path.basename(f))
        if not imgs:
            print("skies %s: no base headshots" % suf)
            continue
        I, M = np.array(imgs), np.array(skies)

        def median(keep):
            out = np.full(I.shape[1:], np.nan, np.float32)
            for r in range(0, I.shape[1], 40):              # in bands: the whole stack as floats would be gigabytes
                band = np.where(M[keep, r:r + 40, :, None], I[keep, r:r + 40].astype(np.float32), np.nan)
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", RuntimeWarning)
                    out[r:r + 40] = np.nanmedian(band, 0)
            return out
        keep = np.ones(len(I), bool)
        med = median(keep)
        dev = np.array([np.nanmean(np.abs(I[i][M[i]] - med[M[i]])) for i in range(len(I))])
        keep = dev <= max(4.0, 2.5 * np.nanmedian(dev))
        med = median(keep).astype(float)
        cnt = M[keep].sum(0)
        seen = ~np.isnan(med[..., 0]) & (cnt >= min(8, max(1, keep.sum() // 4)))   # too few views: filled instead
        full = _hidden_sky(np.nan_to_num(med), seen, cnt)
        Image.fromarray(np.clip(full + .5, 0, 255).astype(np.uint8)).save(os.path.join(SKIES, suf + ".png"), optimize=True)
        print("skies %s: %d headshots (%d left out: %s), %.1f%% of the sky seen"
              % (suf, keep.sum(), (~keep).sum(), ", ".join(n for n, k in zip(names, keep) if not k)[:300], seen.mean() * 100))


def main():
    if "--skies" in sys.argv:
        i = sys.argv.index("--skies")
        build_skies(sys.argv[i + 1], sys.argv[i + 2:])
        return
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
        talks = data.get("talks") or []
        with ThreadPoolExecutor(max_workers=8) as pool:
            list(pool.map(photo, [t["photo"] for t in talks]))
        keyed, ev_sky, n_drawn, n_left = {}, False, 0, 0

        def analysed(url):
            if url not in keyed:
                keyed[url] = key_out(Image.open(BytesIO(photo(url))), topic_sky(url))
            return keyed[url]
        for t in talks:
            head = photo(t["photo"])
            if head is None:
                print("WARN youtube_thumbnails %s: %s could not be fetched" % (os.path.basename(here), t["photo"]))
                continue
            sky_file = topic_sky_file(t["photo"])
            key = hashlib.sha256(("%s|%s|" % (VERSION, sky_file and hashlib.sha256(open(sky_file, "rb").read()).hexdigest())).encode()
                                 + hashlib.sha256(head).digest()).hexdigest()
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
                sky = topic_sky(t["photo"])
                if sky is None and ev_sky is False:         # no topic sky: the event's own, from all its headshots
                    ev_sky = event_sky([analysed(x["photo"]) for x in talks if photo(x["photo"]) is not None])
                draw(analysed(t["photo"]), sky if sky is not None else ev_sky, whole=sky is not None).save(dest, "PNG", optimize=True)
                shutil.copyfile(dest, cached)
                n_drawn += 1
            except Exception as e:
                print("WARN youtube_thumbnails %s: %s: %s" % (os.path.basename(here), t["file"], e))
        drawn, left = drawn + n_drawn, left + n_left
        print("youtube_thumbnails %s: %d talks, %d drawn, %d left for the render job"
              % (os.path.basename(here), len(talks), n_drawn, n_left))
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
