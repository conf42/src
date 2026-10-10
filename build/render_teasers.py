"""Render the conf42.com/teasers/<event> cards to 1080x1080 PNGs with headless Chrome (Marek 2026-10-09; the sister
sites' _build/render_teasers.py, simplified: one kind of picture, no slime, no thumbnails).

    python -m build.render_teasers [--cached-only] [--jobs N] [--prune]

For every docs/teasers/<event>.html (written by `make generate`, upcoming events only) it opens the page in headless
Chrome with #sheet-<start>-<count> (the page then shows only those cards, stacked at their true 1080 px size), takes one
screenshot and slices it into the files named by the cards' data-file attributes, next to the page. Never fails the
build: problems are printed as WARN and the page then draws a missing card in the browser.

Content-addressed cache: each card's PNG is kept in .cache/teasers/<key>.png. The key hashes this script, Chrome's major
version, the card's own HTML, what of the page can change a picture (its styles minus the /*tools*/ ... /*/tools*/ block,
its <link>s and the /*render*/ ... /*/render*/ script), the bytes of every local file they use and the bytes of the
headshots on conf42.github.io/static (a photo re-uploaded under the same name is redrawn; their ETags were tried first and
differ between GitHub's servers, so keys flipped and every run redrew). A card whose photo can't be fetched gets no key:
it is neither copied nor drawn this run (the page draws it), so a flaky download never loops deploys. Only cards whose key
is new are screenshotted. CI keeps .cache/ between runs with actions/cache; --prune drops entries unused for 14 days.

Fast deploys (a deploy takes at most 5 minutes, as on the sister sites):
  --cached-only   the deploy job: copy the PNGs whose key is cached, render nothing; a missing PNG is simply absent (the
                  page draws that card in the browser) - never a stale one
  --jobs N        the render job after the deploy: N headless Chromes at once; it prints rendered=<n> to $GITHUB_OUTPUT
                  so the workflow queues one more deploy only when it drew something new
"""
import glob
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

try:
    from PIL import Image
except ImportError:  # pragma: no cover
    print("WARN render_teasers: Pillow missing, no PNGs rendered")
    sys.exit(0)

ROOT = "docs/teasers"
CARD = 1080
CHUNK = 8            # cards per screenshot (8 * 1080 px tall, well under Chrome's surface limit)
BUDGET_MS = 12000    # virtual time for fonts + photos to settle before the screenshot
CACHE_DIR = os.path.join(os.environ.get("SITE_CACHE_DIR", ".cache"), "teasers")
PRUNE_DAYS = 14
with open(__file__, "rb") as _f:
    SCRIPT_HASH = hashlib.sha256(_f.read()).hexdigest()[:16]
CARD_RE = re.compile(r'class="tz-card" id="tz-card-\d+" data-file="([^"]+)"')
REF_RE = re.compile(r'(?:src|href)="([^"]+)"|url\(\s*[\'"]?([^\'")]+)[\'"]?\s*\)')
_photos = {}


def find_chrome():
    for env in ("CHROME_BIN", "CHROME_PATH"):
        if os.environ.get(env) and os.path.exists(os.environ[env]):
            return os.environ[env]
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        p = shutil.which(name)
        if p:
            return p
    for p in (r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
        if os.path.exists(p):
            return p
    return None


def photo(url):
    """sha256 of the remote headshot's bytes (3 tries), or None when it can't be fetched."""
    if url not in _photos:
        _photos[url] = None
        for attempt in range(3):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "conf42-render-teasers"})
                _photos[url] = hashlib.sha256(urllib.request.urlopen(req, timeout=20).read()).hexdigest()
                break
            except Exception:
                time.sleep(1 + attempt)
    return _photos[url]


def page_parts(page):
    """(context, [card html, ...]): each card is its .tz-slot block up to the next one; the context is everything else.
    Greyed-out slots (missing photo or title) are never drawn and are dropped."""
    with open(page, encoding="utf-8") as f:
        html = f.read()
    starts = [m.start() for m in re.finditer(r'<div class="tz-slot(?: tz-na)?"[ >]', html)]
    if not starts:
        return html, []
    end = html.find('<div id="cr-sec">', starts[-1])
    end = len(html) if end < 0 else end
    bounds = starts + [end]
    cards = [re.sub(r' id="tz-card-\d+"', "", html[bounds[i]:bounds[i + 1]]) for i in range(len(starts))]
    return html[:starts[0]] + html[end:], [c for c in cards if not c.startswith('<div class="tz-slot tz-na"')]


def render_context(context):
    styles = "".join(re.findall(r"<style[^>]*>(.*?)</style>", context, re.S))
    styles = re.sub(r"/\*tools\*/.*?/\*/tools\*/", "", styles, flags=re.S)
    links = "".join(re.findall(r"<link[^>]+>", context))
    script = re.search(r"/\*render\*/(.*?)/\*/render\*/", context, re.S)
    return styles + links + (script.group(1) if script else context)


def refs_digest(text, base_dir, h, outputs):
    for m in REF_RE.finditer(text):
        ref = (m.group(1) or m.group(2) or "").split("#")[0]
        h.update(ref.encode())
        if not ref or ref.startswith(("data:", "mailto:")) or os.path.basename(ref) in outputs:
            continue
        if ref.startswith(("http:", "https:")):
            if "/headshots/" in ref:
                h.update((photo(ref) or "unavailable").encode())
            continue
        try:
            with open(os.path.normpath(os.path.join(base_dir, ref.split("?")[0])), "rb") as f:
                h.update(hashlib.sha256(f.read()).digest())
        except OSError:
            h.update(b"missing")


def card_keys(page, chrome_version):
    context, cards = page_parts(page)
    outputs = set(CARD_RE.findall(open(page, encoding="utf-8").read()))
    ctx = hashlib.sha256(("%s|%s|%d|%d|" % (SCRIPT_HASH, chrome_version, CARD, BUDGET_MS)).encode())
    rc = render_context(context)
    ctx.update(rc.encode())
    print("render_teasers %s: page key %s" % (os.path.basename(page)[:-5], hashlib.sha256(rc.encode()).hexdigest()[:12]))   # differs between runs = every card redraws
    refs_digest(rc, os.path.dirname(page), ctx, outputs)
    urls = [m for c in cards for m in re.findall(r'src="(https://[^"]+/headshots/[^"]+)"', c)]
    with ThreadPoolExecutor(max_workers=8) as pool:   # the photos, all at once
        list(pool.map(photo, urls))
    keys = []
    for card in cards:
        if any(photo(u) is None for u in re.findall(r'src="(https://[^"]+/headshots/[^"]+)"', card)):
            keys.append("skip")   # its photo could not be fetched: left for the page this run
            continue
        h = ctx.copy()
        h.update(card.encode())
        refs_digest(card, os.path.dirname(page), h, outputs)
        keys.append(h.hexdigest())
    return keys


def runs_of(indices):
    runs = []
    for i in indices:
        if runs and runs[-1][-1] == i - 1 and len(runs[-1]) < CHUNK:
            runs[-1].append(i)
        else:
            runs.append([i])
    return runs


def shoot(chrome, url, height, out_png):
    cmd = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-sandbox", "--disable-dev-shm-usage",
           "--allow-file-access-from-files", "--force-device-scale-factor=1", "--window-size=%d,%d" % (CARD, height),
           "--virtual-time-budget=%d" % BUDGET_MS, "--screenshot=%s" % out_png, url]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    except subprocess.TimeoutExpired:
        return False, ["timed out after 180 s"]
    return os.path.exists(out_png), (r.stderr or "").strip().splitlines()[-1:]


def blank(tile):
    """A tile that is one flat colour (a page that did not load) is never published."""
    lo, hi = tile.convert("L").getextrema()
    return hi - lo < 12


def main():
    cached_only = "--cached-only" in sys.argv
    jobs = int(sys.argv[sys.argv.index("--jobs") + 1]) if "--jobs" in sys.argv else 1
    chrome = find_chrome()
    out = os.environ.get("GITHUB_OUTPUT")
    rendered_total, reused_total, missing_total, used = 0, 0, 0, set()
    if not chrome:
        print("WARN render_teasers: no Chrome/Chromium found, no PNGs rendered")
        pages = []
    else:
        pages = sorted(p for p in glob.glob(os.path.join(ROOT, "*.html")) if os.path.basename(p) != "index.html")
        r = subprocess.run([chrome, "--version"], capture_output=True, text=True)
        m = re.search(r"(\d+)\.", r.stdout or r.stderr or "")
        chrome_version = "Chrome %s" % (m.group(1) if m else "unknown")   # only the major version: build numbers change weekly
    os.makedirs(CACHE_DIR, exist_ok=True)
    for page in pages:
        event = os.path.basename(page)[:-5]
        files = CARD_RE.findall(open(page, encoding="utf-8").read())
        if not files:
            print("render_teasers %s: no cards" % event)
            continue
        keys = card_keys(page, chrome_version)
        if len(keys) != len(files):   # page layout not understood: render everything, cache nothing
            print("WARN render_teasers %s: %d pictures but %d slots, not caching" % (event, len(files), len(keys)))
            keys = [None] * len(files)
        missing = []
        skip = {i for i, k in enumerate(keys) if k == "skip"}
        if skip:
            print("WARN render_teasers %s: %d photos could not be fetched, those cards are left for the page" % (event, len(skip)))
        for i, (name, key) in enumerate(zip(files, keys)):
            if i in skip:
                continue
            cached = key and os.path.join(CACHE_DIR, key + ".png")
            if key:
                used.add(key + ".png")
            if cached and os.path.exists(cached):
                shutil.copyfile(cached, os.path.join(ROOT, name))
                os.utime(cached)   # last used now: --prune keeps it
                reused_total += 1
            else:
                missing.append(i)
        if cached_only:
            missing_total += len(missing)
            print("render_teasers %s: %d/%d from cache, %d left for the render job" % (event, len(files) - len(missing), len(files), len(missing)))
            continue
        url = "file:///" + os.path.abspath(page).replace("\\", "/")
        done = 0
        with tempfile.TemporaryDirectory() as tmp:
            def take(run):
                shot = os.path.join(tmp, "sheet-%d.png" % run[0])
                return run, shot, shoot(chrome, "%s#sheet-%d-%d" % (url, run[0], len(run)), CARD * len(run), shot)
            with ThreadPoolExecutor(max_workers=max(1, jobs)) as pool:
                for run, shot, (ok, err) in pool.map(take, runs_of(missing)):
                    if not ok:
                        print("WARN render_teasers %s: cards %d-%d not rendered %s" % (event, run[0], run[-1], err))
                        continue
                    sheet = Image.open(shot).convert("RGB")
                    for n, i in enumerate(run):
                        tile = sheet.crop((0, n * CARD, CARD, (n + 1) * CARD))
                        if blank(tile):
                            print("WARN render_teasers %s: %s came out blank, not published" % (event, files[i]))
                            continue
                        dest = os.path.join(ROOT, files[i])
                        tile.save(dest, "PNG", optimize=True)
                        if keys[i]:
                            shutil.copyfile(dest, os.path.join(CACHE_DIR, keys[i] + ".png"))
                            rendered_total += 1
                        done += 1
        print("render_teasers %s: %d drawn, %d from cache, %d of %d still missing" % (event, done, len(files) - len(missing), len(missing) - done, len(files)))
    if "--prune" in sys.argv:
        cut, gone = time.time() - PRUNE_DAYS * 86400, 0
        for f in glob.glob(os.path.join(CACHE_DIR, "*.png")):
            if os.path.basename(f) not in used and os.path.getmtime(f) < cut:
                os.remove(f)
                gone += 1
        print("render_teasers: pruned %d cache entries unused for %d days" % (gone, PRUNE_DAYS))
    print("render_teasers: %d drawn, %d from cache%s" % (rendered_total, reused_total, ", %d left for the render job" % missing_total if cached_only else ""))
    if out:
        with open(out, "a") as f:
            f.write("rendered=%d\n" % rendered_total)


if __name__ == "__main__":
    main()
