# extend.py <kit dir> (Marek 2026-11-09, after the first ship): changes made to the published kit without a rebuild.
# 1. DevOps Not Dead is hidden (brand, cards, files).
# 2. Reliaburger gets its burger logo (masters/reliaburger/burger-v1.png, from the Reliaburger Drive folder): the yellow
#    page cut away outside the black outline (the art itself untouched), a colour vector (vtracer), one-colour vectors
#    traced from the black linework (potrace) in black and white, PNG/PDF/EPS, tiles; and the capybara mascot.
# 3. every file says whether it has transparency ("alpha"), so the page shows the subtle grid behind it.
# 4. brandkit.md and llms.txt are written again from brandkit.json.
import os, sys, json, shutil, hashlib, subprocess, numpy as np, vtracer
from PIL import Image

OUT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
K = json.load(open(os.path.join(OUT, 'brandkit.json'))); URL = K['base']

def row(brand, group, label, rel, fmt, **kw):
    p = os.path.join(OUT, rel); r = dict(brand=brand, group=group, label=label, file=rel, size=os.path.getsize(p), fmt=fmt, url=URL + rel,
                                         sha256=hashlib.sha256(open(p, 'rb').read()).hexdigest(),
                                         mime={'png': 'image/png', 'svg': 'image/svg+xml', 'pdf': 'application/pdf', 'eps': 'application/postscript'}[fmt])
    if fmt == 'png': r['px'] = '%dx%d' % Image.open(p).size
    r.update(kw); return r

# ---- 1. hide DND ----------------------------------------------------------------------------------------------------------
K['brands'] = [b for b in K['brands'] if b['key'] != 'devopsnotdead']
K['cards'] = [c for c in K['cards'] if c['brand'] != 'devopsnotdead']
K['items'] = [i for i in K['items'] if i['brand'] != 'devopsnotdead']
shutil.rmtree(os.path.join(OUT, 'devopsnotdead'), ignore_errors=True)

# ---- 2. Reliaburger: burger logo + capybara -------------------------------------------------------------------------------
if not any(c['id'].startswith('reliaburger|logos|') for c in K['cards']):
    d = os.path.join(OUT, 'reliaburger', 'logos'); os.makedirs(d, exist_ok=True)
    src = Image.open(os.path.join(HERE, 'masters', 'reliaburger', 'burger-v1.png')).convert('RGBA'); a = np.asarray(src).copy(); h, w = a.shape[:2]
    bg = a[5, 5, :3].astype(int); page = np.abs(a[..., :3].astype(int) - bg).sum(axis=2) < 90
    seen = np.zeros((h, w), bool); st = [(y, x) for y in (0, h - 1) for x in range(w)] + [(y, x) for x in (0, w - 1) for y in range(h)]
    while st:
        y, x = st.pop()
        if seen[y, x] or not page[y, x]: continue
        seen[y, x] = True; st += [(y + dy, x + dx) for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= y + dy < h and 0 <= x + dx < w]
    a[seen, 3] = 0; cut = Image.fromarray(a); cut = cut.crop(cut.getchannel('A').getbbox())
    base = os.path.join(d, 'reliaburger-burger-logo')
    big = cut.resize((cut.width * 2, cut.height * 2), Image.LANCZOS); big.save(base + '-color.png')
    vtracer.convert_image_to_svg_py(base + '-color.png', base + '-color.svg', colormode='color', hierarchical='stacked', mode='spline', color_precision=6,
                                    filter_speckle=4, layer_difference=16, corner_threshold=60, length_threshold=4.0, splice_threshold=45, path_precision=2)
    c = np.asarray(cut).astype(int); ink = (c[..., 3] > 128) & (c[..., :3].max(axis=2) < 70)     # the black linework
    pbm = base + '.pbm'
    Image.fromarray(((~ink) * 255).astype(np.uint8)).resize((cut.width * 3, cut.height * 3), Image.LANCZOS).point(lambda v: 255 if v > 127 else 0).convert('1').save(pbm)
    subprocess.run(['potrace', pbm, '-s', '-o', base + '-black.svg', '--turdsize', '10', '--alphamax', '1.0', '--opttolerance', '0.2'], check=True); os.remove(pbm)
    open(base + '-white.svg', 'w').write(open(base + '-black.svg').read().replace('fill="#000000"', 'fill="#ffffff"'))
    files = {'color': [], 'black': [], 'white': []}
    for v in files:
        if v != 'color':
            subprocess.run(['rsvg-convert', '-w', '1600', base + '-%s.svg' % v, '-o', base + '-%s.png' % v], check=True)
            for fmt in ('pdf', 'eps'):
                subprocess.run(['rsvg-convert', '-f', fmt, base + '-%s.svg' % v, '-o', base + '-%s.%s' % (v, fmt)], check=True)
        for fmt in ('png', 'svg', 'pdf', 'eps'):
            if os.path.isfile(base + '-%s.%s' % (v, fmt)):
                subprocess.run(['oxipng', '-q', '-o', '2', base + '-%s.png' % v]) if fmt == 'png' else None
                files[v].append(row('reliaburger', 'Logos', 'Burger logo, %s' % v, os.path.relpath(base + '-%s.%s' % (v, fmt), OUT), fmt, variant=v))
    nice = {'color': 'in colour', 'black': 'in black', 'white': 'in white (for dark backgrounds)'}
    new = []
    for i, v in enumerate(('color', 'black', 'white')):
        new.append(dict(id='reliaburger|logos|Burger logo|' + v, brand='reliaburger', section='logos', title='Burger logo ' + nice[v], files=files[v], order=i, dark=v == 'white',
                        tags=sorted(set(('logo logos brand burger reliaburger ' + {'color': 'colour color full-colour', 'black': 'black mono monochrome one-colour', 'white': 'white reversed knockout for-dark-backgrounds'}[v] + ' svg vector png pdf eps print').split()))))
    for tile, bgc, v in (('on-light', '#ffffff', 'color'), ('on-dark', '#181b19', 'white')):
        lo = Image.open(base + '-%s.png' % v).convert('RGBA'); W, H = 2400, 1350; lo.thumbnail((int(W * .62), int(H * .7)), Image.LANCZOS)
        can = Image.new('RGBA', (W, H), bgc); can.alpha_composite(lo, ((W - lo.width) // 2, (H - lo.height) // 2)); can.convert('RGB').save(base + '-%s.png' % tile)
        new.append(dict(id='reliaburger|logos|Burger logo|' + tile, brand='reliaburger', section='logos', title='Burger logo on a %s background' % tile[3:], order=3 if tile == 'on-light' else 4,
                        dark=tile == 'on-dark', files=[row('reliaburger', 'Logos', 'Burger logo ' + tile, os.path.relpath(base + '-%s.png' % tile, OUT), 'png', variant=tile, tile=True)],
                        tags=sorted(set('logo logos burger reliaburger preview background'.split() + [tile[3:]]))))
    shutil.copyfile(os.path.join(HERE, 'masters', 'reliaburger', 'burger-v1.png'), base + '-on-yellow.png')
    new.append(dict(id='reliaburger|logos|Burger logo|original', brand='reliaburger', section='logos', title='Burger logo on yellow (original)', order=5,
                    files=[row('reliaburger', 'Logos', 'Burger logo on yellow', os.path.relpath(base + '-on-yellow.png', OUT), 'png', variant='original')],
                    tags=sorted(set('logo logos burger reliaburger original yellow square'.split()))))
    m = os.path.join(OUT, 'reliaburger', 'mascots'); os.makedirs(m, exist_ok=True); cap = os.path.join(m, 'reliaburger-capybara')
    ci = Image.open(os.path.join(HERE, 'masters', 'reliaburger', 'capybara.png')).convert('RGBA'); ci.save(cap + '.png'); subprocess.run(['oxipng', '-q', '-o', '2', cap + '.png'])
    t = ci.copy(); t.thumbnail((1600, 1600)); t.save(cap + '.in.png')
    vtracer.convert_image_to_svg_py(cap + '.in.png', cap + '.svg', colormode='color', hierarchical='stacked', mode='spline', color_precision=6, filter_speckle=4,
                                    layer_difference=16, corner_threshold=60, length_threshold=4.0, splice_threshold=45, path_precision=2); os.remove(cap + '.in.png')
    new.append(dict(id='reliaburger|mascots|capybara', brand='reliaburger', section='mascots', title='Capybara', files=[
        row('reliaburger', 'Mascots', 'Capybara', os.path.relpath(cap + '.png', OUT), 'png'), row('reliaburger', 'Mascots', 'Capybara', os.path.relpath(cap + '.svg', OUT), 'svg', traced=True)],
        tags=sorted(set('mascot mascots pet pets animal capybara burger reliaburger character cute'.split()))))
    K['cards'] += new; K['items'] += [f for c in new for f in c['files']]
    order = {s['id']: i for i, s in enumerate(K['sections'])}
    K['cards'].sort(key=lambda c: (order[c['section']], [b['key'] for b in K['brands']].index(c['brand']) if c['brand'] in [b['key'] for b in K['brands']] else 99, c.get('order', 0)))

# ---- 3. transparency flags ------------------------------------------------------------------------------------------------
for c in K['cards']:
    alpha = None
    for f in c['files']:
        if f.get('file') and f['fmt'] in ('png', 'webp'):
            im = Image.open(os.path.join(OUT, f['file']))
            if im.mode in ('RGBA', 'LA', 'PA') or 'transparency' in im.info:
                ch = im.convert('RGBA').getchannel('A'); ch.thumbnail((400, 400)); f['alpha'] = ch.getextrema()[0] < 250
            else: f['alpha'] = False
            alpha = f['alpha'] if alpha is None else alpha
    for f in c['files']:
        if f['fmt'] == 'svg': f['alpha'] = True if alpha is None else alpha
    c['alpha'] = bool(alpha) if alpha is not None else any(f.get('alpha') for f in c['files'])
by = {f['file']: f for c in K['cards'] for f in c['files'] if f.get('file')}
K['items'] = [by.get(i['file'], i) for i in K['items']]
json.dump(K, open(os.path.join(OUT, 'brandkit.json'), 'w'), indent=1)

# ---- 4. brandkit.md + llms.txt ------------------------------------------------------------------------------------------
md = ['# Conf42 family media kit', '', 'Machine-readable index: %sbrandkit.json (every file with url, size, px, sha256, mime, alpha).' % URL, '',
      '```sh', '# every SREday file', "curl -s %sbrandkit.json | jq -r '.items[] | select(.brand==\"sreday\") | .url' | xargs -n1 curl -sO" % URL,
      '# one logo', 'curl -O %ssreday/logos/sreday-logo-white.svg' % URL, '```', '']
titles = {s['id']: s['title'] for s in K['sections']}
for b in K['brands']:
    md += ['## %s' % b['name'], '', b['about'], '', 'Name: %s. Website: %s' % (b['spelling'], b['site']), '', '| Colour | HEX | RGB | CMYK |', '|---|---|---|---|']
    md += ['| %s | `%s` | %s | %s |' % (c['name'], c['hex'].upper(), ' '.join(map(str, c['rgb'])), ' '.join(map(str, c['cmyk']))) for c in b['palette']] + ['']
    for s in K['sections']:
        cs = [c for c in K['cards'] if c['brand'] == b['key'] and c['section'] == s['id']]
        if not cs or s['id'] == 'colours': continue
        md += ['### ' + s['title'], ''] + ['- %s: %s' % (c['title'], ', '.join('[%s](%s)' % (f['fmt'].upper(), f['url']) for f in c['files'])) for c in cs] + ['']
open(os.path.join(OUT, 'brandkit.md'), 'w').write('\n'.join(md))
names = ', '.join(b['name'] for b in K['brands'])
open(os.path.join(OUT, 'llms.txt'), 'w').write('# Conf42 family media kit\n\n> Logos (SVG/PNG/PDF/EPS in colour, black and white), colours (HEX/RGB/CMYK, design tokens), banners, profile pictures, stickers, mascots, animations (WebP/MP4) and event splashes for %s.\n\n- [Index (JSON)](%sbrandkit.json): every file with url, size, px, sha256, mime\n- [Index (Markdown)](%sbrandkit.md)\n- [The page](https://www.conf42.com/mediakit/)\n' % (names, URL, URL))
print('brands', len(K['brands']), 'cards', len(K['cards']), 'files', len(K['items']), 'kit %.1f MB' % (sum(f['size'] for f in K['items']) / 1e6))
