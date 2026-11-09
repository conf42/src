# Brand kit (conf42.com/media-kit and every site's /media-kit/)

Built once on a Mac, committed as files, never in CI (Marek 2026-11-09: rebuild only when adding something).
Output: `docs/assets/brandkit/` = the files + `brandkit.json` (every file: url, size, px, sha256, mime), `brandkit.md`, `llms.txt`.
The page is `_templates/media-kit.html` here and `home/_templates/media-kit.html` in sreday (website), llmday, platformday,
PEC and devopsnotdead; every teasers page's Media kit tab reads the same `brandkit.json`.

Tools (all open source): potrace (one-colour logo vectors), vtracer (`pip install vtracer`, colour vectors of stickers, mascots,
banners), librsvg (`rsvg-convert`: PNG/PDF/EPS from SVG), Pillow, pngquant + oxipng, ffmpeg + img2webp (animations).
Masters come from Dropbox `_misc/` and the brand folders (paths in `masters.py` / `build.py`).

    python3 brandkit/mono.py  brandkit/mono                 # trace the one-colour logos (potrace)
    python3 brandkit/build.py docs/assets/brandkit https://www.conf42.com/assets/brandkit/
    python3 brandkit/enrich.py docs/assets/brandkit         # sections, search tags, vectors, splashes, animations
    python3 brandkit/slim.py  docs/assets/brandkit          # big pictures capped at 2400 px + pngquant

Logos are traced from the masters' own shapes and coloured exactly; stickers, mascots and pets ship as they are.
Event splashes are not copied: the index links them where they live (conf42.com/assets/splash, each site's events folder),
and their SVG is traced in the visitor's browser (ImageTracer.js) on click.
