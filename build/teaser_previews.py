"""Small previews of the teaser PNGs (Marek 2026-10-10: the /<event>/teasers grid lagged and the carousel strip looked hazy).

    python -m build.teaser_previews

The page used to show every card as a live 1080 px card scaled down: 5 blurred blobs and 5 backdrop-filtered glass shards
each, so ~300 heavy layers for 30 talks, and Chrome's scaled-down blur left a haze over the photos. The page now shows
<file>.webp (720 px, ~30 KB) for every card whose PNG is published and keeps the live card only for the ones the render
job has not drawn yet. Downloads, the ZIP and the PDF still use the full PNGs.

Runs in the deploy job after `render_teasers --cached-only`: one WebP per published PNG, made fresh every deploy from the
PNG beside it, so it is never stale (~40 ms a card). Never fails the build; a card without a preview simply stays live on
the page. Kept out of render_teasers.py on purpose: its own hash is in every card's render
key, so editing it would redraw every card.
"""
import glob
import hashlib
import os
import shutil
import sys
import time

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    print("WARN teaser_previews: Pillow missing, no previews")
    sys.exit(0)

SIZE = 720           # sharp at the grid's ~360-440 px columns on a 2x screen
QUALITY = 80
# previews are content-addressed too (2026-10-12, with the YouTube thumbnails: 192 WebPs at ~60 ms each every deploy):
# .cache/previews/<sha of the PNG + settings>.webp. The render job makes and saves the new ones with the pictures it drew;
# the deploy copies them and only encodes what is missing. --prune drops entries unused for 14 days.
CACHE_DIR = os.path.join(os.environ.get("SITE_CACHE_DIR", ".cache"), "previews")
PRUNE_DAYS = 14


def main():
    made, reused, used = 0, 0, set()
    os.makedirs(CACHE_DIR, exist_ok=True)
    for png in sorted(glob.glob(os.path.join("docs", "*", "conf42-*.png"))):
        if not os.path.exists(os.path.join(os.path.dirname(png), "teasers.html")):
            continue
        try:
            with open(png, "rb") as f:
                key = hashlib.sha256(b"%d|%d|" % (SIZE, QUALITY) + f.read()).hexdigest() + ".webp"
            used.add(key)
            cached = os.path.join(CACHE_DIR, key)
            if os.path.exists(cached):
                shutil.copyfile(cached, png[:-4] + ".webp")
                os.utime(cached)
                reused += 1
                continue
            im = Image.open(png).convert("RGB")
            im.thumbnail((SIZE, SIZE), Image.LANCZOS)   # squares: 720 x 720; YouTube thumbnails (16:9): 720 x 405
            im.save(png[:-4] + ".webp", "WEBP", quality=QUALITY, method=6)
            shutil.copyfile(png[:-4] + ".webp", cached)
            made += 1
        except Exception as e:
            print("WARN teaser_previews: %s: %s" % (png, e))
    if "--prune" in sys.argv:
        cut, gone = time.time() - PRUNE_DAYS * 86400, 0
        for f in glob.glob(os.path.join(CACHE_DIR, "*.webp")):
            if os.path.basename(f) not in used and os.path.getmtime(f) < cut:
                os.remove(f)
                gone += 1
        print("teaser_previews: pruned %d cache entries unused for %d days" % (gone, PRUNE_DAYS))
    print("teaser_previews: %d made, %d from cache" % (made, reused))


if __name__ == "__main__":
    main()
