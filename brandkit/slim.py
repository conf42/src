# slim.py <kit dir>: reasonable quality, not heavy (Marek 2026-11-09). Logos and colours stay lossless (exact); big
# pictures are capped at 2400 px and compressed with pngquant at high quality (no visible change); sizes and checksums
# in brandkit.json are updated. Run once after enrich.py.
import os, sys, json, hashlib, subprocess
from PIL import Image
OUT = sys.argv[1]
K = json.load(open(os.path.join(OUT, 'brandkit.json')))
saved = 0
for c in K['cards']:
    if c['section'] in ('logos', 'colours', 'about', 'splashes', 'animations'): continue
    for f in c['files']:
        if not f.get('file') or f['fmt'] not in ('png', 'jpg', 'jpeg'): continue
        p = os.path.join(OUT, f['file']); before = os.path.getsize(p)
        if before < 900_000: continue
        im = Image.open(p)
        if max(im.size) > 2400:
            im.thumbnail((2400, 2400), Image.LANCZOS); im.save(p)
        if f['fmt'] == 'png':
            subprocess.run(['pngquant', '--quality', '80-96', '--speed', '1', '--skip-if-larger', '--force', '--ext', '.png', p], check=False)
            subprocess.run(['oxipng', '-q', '-o', '2', '--strip', 'safe', p], check=False)
        else:
            Image.open(p).convert('RGB').save(p, quality=88, optimize=True, progressive=True)
        after = os.path.getsize(p); saved += before - after
        f['size'] = after; f['px'] = '%dx%d' % Image.open(p).size; f['sha256'] = hashlib.sha256(open(p, 'rb').read()).hexdigest()
by = {f['file']: f for c in K['cards'] for f in c['files'] if f.get('file')}
K['items'] = [by.get(i['file'], i) for i in K['items']]
json.dump(K, open(os.path.join(OUT, 'brandkit.json'), 'w'), indent=1)
tot = sum(f['size'] for f in K['items'])
big = sorted(K['items'], key=lambda f: -f['size'])[:8]
print('saved %.1f MB; kit now %.1f MB' % (saved / 1e6, tot / 1e6))
for f in big: print('  %.1f MB  %s' % (f['size'] / 1e6, f['file']))
