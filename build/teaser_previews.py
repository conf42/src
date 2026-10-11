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
import os
import sys

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    print("WARN teaser_previews: Pillow missing, no previews")
    sys.exit(0)

SIZE = 720           # sharp at the grid's ~360-440 px columns on a 2x screen
QUALITY = 80


def main():
    made = 0
    for png in sorted(glob.glob(os.path.join("docs", "*", "conf42-*.png"))):
        if not os.path.exists(os.path.join(os.path.dirname(png), "teasers.html")):
            continue
        try:
            Image.open(png).convert("RGB").resize((SIZE, SIZE), Image.LANCZOS).save(png[:-4] + ".webp", "WEBP", quality=QUALITY, method=6)
            made += 1
        except Exception as e:
            print("WARN teaser_previews: %s: %s" % (png, e))
    print("teaser_previews: %d previews" % made)


if __name__ == "__main__":
    main()
