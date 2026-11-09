# refine.py <kit dir> (Marek 2026-11-09, second round on the published kit, no rebuild):
# 1. the "iterations" go: the on-light / on-dark preview tiles, the recoloured Conf42 wordmark + mark, the one-colour
#    CFP Ninja mark, and the duplicate boardroom video ("SRE monkeys" = a smaller copy of "Monkeys").
# 2. Reliaburger: the main logo is the PSD master (masters/reliaburger/reliaburger-logo.png, CMYK converted with its own
#    ICC profile), its one-colour versions traced from its black linework; the text-only lettering is added.
# 3. profile pictures + banners are drawn again on deeper, quieter brand backgrounds (a dark shade of the brand colour
#    with a soft glow; the light brands keep paper), so the sticker never sits on its own flat colour. SVGs re-traced.
# Then run extend.py again (transparency flags, brandkit.md, llms.txt).
import os, sys, json, hashlib, subprocess, colorsys, numpy as np, vtracer
from PIL import Image

OUT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
K = json.load(open(os.path.join(OUT, 'brandkit.json'))); URL = K['base']

# build.py's brands and drawing helpers, without running its build
src = open(os.path.join(HERE, 'build.py')).read()
ns = {'__file__': os.path.join(HERE, 'build.py')}; sys_argv = sys.argv; sys.argv = ['build.py', OUT]
exec(compile(src[:src.index('brands_out = []')], 'build.py', 'exec'), ns); sys.argv = sys_argv
B = {b['key']: b for b in ns['BRANDS']}

def gone(card):
    for f in card['files']:
        if f.get('file') and os.path.isfile(os.path.join(OUT, f['file'])): os.remove(os.path.join(OUT, f['file']))

def refresh(f):
    p = os.path.join(OUT, f['file']); f['size'] = os.path.getsize(p); f['sha256'] = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    if f['fmt'] == 'png': f['px'] = '%dx%d' % Image.open(p).size

def trace(png, svg):
    im = Image.open(png).convert('RGBA'); im.thumbnail((1600, 1600)); tmp = svg + '.in.png'; im.save(tmp)
    vtracer.convert_image_to_svg_py(tmp, svg, colormode='color', hierarchical='stacked', mode='spline', color_precision=6, filter_speckle=4,
                                    layer_difference=16, corner_threshold=60, length_threshold=4.0, splice_threshold=45, path_precision=2)
    os.remove(tmp)

# ---- 1. iterations out ----------------------------------------------------------------------------------------------------
DROP = lambda c: (c['section'] == 'logos' and (c['id'].endswith('|on-light') or c['id'].endswith('|on-dark'))) \
    or c['id'] in ('conf42|logos|Wordmark|color', 'conf42|logos|Mark (42)|color', 'cfpninja|logos|Mark|black', 'cfpninja|logos|Mark|white', 'sreday-sre-monkeys')
for c in K['cards']:
    if DROP(c): gone(c)
K['cards'] = [c for c in K['cards'] if not DROP(c)]
for c in K['cards']:
    if c['id'] == 'sreday-monkeys': c['title'] = 'Boardroom monkeys'; c['tags'] = sorted(set(c['tags']) | {'boardroom', 'meeting', 'outage'})

# ---- 2. Reliaburger: PSD master as the main logo, lettering added ------------------------------------------------------
M = os.path.join(HERE, 'masters', 'reliaburger'); d = os.path.join(OUT, 'reliaburger', 'logos'); base = os.path.join(d, 'reliaburger-burger-logo')
logo = Image.open(os.path.join(M, 'reliaburger-logo.png')).convert('RGBA'); logo = logo.crop(logo.getchannel('A').getbbox())
logo.save(base + '-color.png'); subprocess.run(['oxipng', '-q', '-o', '2', base + '-color.png']); trace(base + '-color.png', base + '-color.svg')
c = np.asarray(logo).astype(int); ink = (c[..., 3] > 128) & (c[..., :3].max(axis=2) < 70)
pbm = base + '.pbm'
Image.fromarray(((~ink) * 255).astype(np.uint8)).resize((logo.width * 2, logo.height * 2), Image.LANCZOS).point(lambda v: 255 if v > 127 else 0).convert('1').save(pbm)
subprocess.run(['potrace', pbm, '-s', '-o', base + '-black.svg', '--turdsize', '10', '--alphamax', '1.0', '--opttolerance', '0.2'], check=True); os.remove(pbm)
open(base + '-white.svg', 'w').write(open(base + '-black.svg').read().replace('fill="#000000"', 'fill="#ffffff"'))
for v in ('black', 'white'):
    subprocess.run(['rsvg-convert', '-w', '1600', base + '-%s.svg' % v, '-o', base + '-%s.png' % v], check=True)
    for fmt in ('pdf', 'eps'): subprocess.run(['rsvg-convert', '-f', fmt, base + '-%s.svg' % v, '-o', base + '-%s.%s' % (v, fmt)], check=True)
for cd in K['cards']:
    if cd['id'].startswith('reliaburger|logos|Burger logo|'):
        cd['title'] = cd['title'].replace('Burger logo', 'Logo'); cd['order'] = {'color': 0, 'black': 1, 'white': 2, 'original': 9}.get(cd['id'].rsplit('|', 1)[1], 5)
        for f in cd['files']: refresh(f)
let = os.path.join(d, 'reliaburger-lettering')
li = Image.open(os.path.join(M, 'reliaburger-lettering.png')).convert('RGBA'); li = li.crop(li.getchannel('A').getbbox()); li.save(let + '.png')
subprocess.run(['oxipng', '-q', '-o', '2', let + '.png']); trace(let + '.png', let + '.svg')
if not any(cd['id'] == 'reliaburger|logos|Lettering|color' for cd in K['cards']):
    files = []
    for fmt, mime in (('png', 'image/png'), ('svg', 'image/svg+xml')):
        rel = os.path.relpath(let + '.' + fmt, OUT); f = dict(brand='reliaburger', group='Logos', label='Lettering', file=rel, fmt=fmt, url=URL + rel, mime=mime, variant='color'); refresh(f); files.append(f)
    K['cards'].append(dict(id='reliaburger|logos|Lettering|color', brand='reliaburger', section='logos', title='Lettering (text only) in colour', order=3, files=files,
                           tags=sorted(set('logo logos lettering text wordmark words name type reliaburger colour color svg vector png'.split()))))

# ---- 3. profile pictures + banners on deeper, quieter backgrounds ------------------------------------------------------
hexrgb, shade = ns['hexrgb'], ns['shade']
def hsl(h, l, s):
    r, g, b = [v / 255 for v in hexrgb(h)]; hh, _, _ = colorsys.rgb_to_hls(r, g, b)
    r, g, b = colorsys.hls_to_rgb(hh, l, s); return np.array([r * 255, g * 255, b * 255], np.float32)
def gradient(W, H, color, ink, light=False, paper=None, cx=.74, cy=.86):
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - W * cx) / (max(W, H) * .9)) ** 2 + ((yy - H * cy) / (max(W, H) * .9)) ** 2)
    t = np.clip(r, 0, 1) ** .8; t = t[..., None]
    if light:
        c0 = np.array(hexrgb(paper or '#ffffff'), np.float32); c1 = hsl(color, .955, .35)
    else:
        c0 = hsl(color, .085, .42); c1 = hsl(color, .23, .52)      # deep edge -> soft glow, never the flat brand colour
    img = c1 * (1 - t) + c0 * t
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), 'RGB').convert('RGBA')
ns['gradient'] = gradient
def avatars(b, av, d):
    for shape in ('square', 'round'):
        for n in (1000, 400):
            can = gradient(n, n, b['color'], b['ink'], b.get('light', False), b.get('paper'), cx=.5, cy=.42)
            im = av.copy(); pad = .2 if shape == 'round' else .15; im.thumbnail((int(n * (1 - 2 * pad)), int(n * (1 - 2 * pad))), Image.LANCZOS)
            can.alpha_composite(im, ((n - im.width) // 2, (n - im.height) // 2))
            if shape == 'round':
                from PIL import ImageDraw
                m = Image.new('L', (n * 4, n * 4), 0); ImageDraw.Draw(m).ellipse((0, 0, n * 4 - 1, n * 4 - 1), fill=255); can.putalpha(m.resize((n, n), Image.LANCZOS))
            can.save(os.path.join(d, '%s-avatar-%s-%d.png' % (b['key'], shape, n)))
GH = ns['GH']
for key in [x['key'] for x in K['brands']]:
    b = B[key]; root = os.path.join(OUT, key)
    st = Image.open(b['sticker']); st = ns['flatten_white'](st) if b.get('flatten_white') else st.convert('RGBA'); st = ns['trimmed'](st)
    ns['items'].clear(); ns['social'](b, st, os.path.join(root, 'social'))
    av = st
    if b['avatar_from'] == 'mark': av = Image.open(os.path.join(root, 'logos', key + '-mark-white.png')).convert('RGBA')
    elif b['avatar_from'] == 'pec-avatar': av = ns['trimmed'](Image.open(GH + '/2025.promptengineering.rocks/home/assets/images/avatar.png'))
    elif b['avatar_from'] == 'badger-head': av = ns['trimmed'](Image.open(GH + '/badger/snout/assets/badger-head.png'))
    elif b['avatar_from'] == 'mark-crop':
        im = ns['trimmed'](Image.open(b['logos'][0]['color_png'])); a = np.asarray(im)[..., 3] > 8
        cols = np.where(a[: int(im.height * .55)].any(axis=0))[0]; av = ns['trimmed'](im.crop((cols.min(), 0, cols.max() + 1, int(im.height * .58))))
    avatars(b, av, os.path.join(root, 'avatars'))
    for cd in K['cards']:
        if cd['brand'] == key and cd['section'] in ('banners', 'avatars'):
            png = next(f for f in cd['files'] if f['fmt'] == 'png'); svg = next((f for f in cd['files'] if f['fmt'] == 'svg'), None)
            subprocess.run(['oxipng', '-q', '-o', '2', os.path.join(OUT, png['file'])]); refresh(png)
            if svg: trace(os.path.join(OUT, png['file']), os.path.join(OUT, svg['file'])); refresh(svg)
    print('redrawn', key)

order = {s['id']: i for i, s in enumerate(K['sections'])}; keys = [b['key'] for b in K['brands']]
K['cards'].sort(key=lambda c: (order[c['section']], keys.index(c['brand']) if c['brand'] in keys else 99, c.get('order', 0)))
by = {f['file']: f for cd in K['cards'] for f in cd['files'] if f.get('file')}
K['items'] = [f for cd in K['cards'] for f in cd['files'] if f.get('file')]
json.dump(K, open(os.path.join(OUT, 'brandkit.json'), 'w'), indent=1)
print('cards', len(K['cards']), 'files', len(K['items']), 'kit %.1f MB' % (sum(f['size'] for f in K['items']) / 1e6))
