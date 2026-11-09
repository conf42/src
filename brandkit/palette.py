# palette.py <kit dir> (Marek 2026-11-09: "the color palettes are BS ... study colors used ... make it true to the brands").
# Every colour below is one the brand really uses, with where: counted from each site's CSS/templates (2026-11-09) or
# measured from its logo, sticker and pets (k-means + exact pixel sampling). Nothing is derived or made up.
# Writes brands[].palette (+ color = the main one) into brandkit.json and the colour files (PNG, JSON, CSS, GIMP, W3C
# tokens); build.py's BRANDS colours follow the same main colours, so banners / profile pictures are drawn in them.
import os, sys, json, hashlib
from PIL import Image, ImageDraw, ImageFont

SHARED = [('Blue', '#098dcf', 'CFP button, links (shared site theme)'), ('Coral', '#ec645e', 'Sponsor button (shared site theme)'),
          ('Ink', '#141c25', 'headings and text'), ('Mist', '#f0f6fa', 'page background behind the glass')]
PALETTES = {
 'conf42': [('Blue', '#335eea', 'buttons and links on conf42.com'), ('Navy', '#1b2a4e', 'headings; the sticker outline'),
            ('Midnight', '#161c2d', 'dark sections'), ('Sky', '#7ea2d2', 'the sticker cloud'), ('Corgi', '#ea8a5a', 'the corgi, sticker accents'),
            ('Coral', '#df4759', 'highlights and alerts'), ('Mint', '#42ba96', 'live and success badges'), ('Paper', '#f9fbfd', 'page background')],
 'sreday': [('Plum', '#713660', 'stats band, social buttons, home glow')] + [('Sticker violet', '#5a4e72', 'the SREday sticker')] + SHARED[:2] +
           [('Orchid', '#c46aa0', 'home glow sweep'), ('Monkey orange', '#ea9244', 'the monkey')] + SHARED[2:],
 'llmday': [('Green', '#26986a', 'stats band, buttons, home glow'), ('Leaf', '#4bcb81', 'the sticker highlight'), ('Lime', '#8fdc6a', 'home glow sweep'),
            ('Teal', '#2ec4b6', 'home glow sweep')] + SHARED[:2] + [('Black', '#000000', 'the logo lettering')] + SHARED[2:],
 'platformday': [('Orange', '#e2971d', 'stats band, buttons, home glow'), ('Ember', '#d0562b', 'home glow sweep'), ('Sun', '#f5c84c', 'home glow sweep'),
                 ('Platypus', '#7b5947', 'the platypus'), ('Slate', '#415b78', 'home glow sweep, body text')] + SHARED[:2] + [('Black', '#000000', 'the logo lettering')] + SHARED[2:],
 'pec': [('Violet', '#6b40d8', 'stats band, buttons, home glow; the logo'), ('Pink', '#e8507a', 'home glow sweep'), ('Amber', '#f5ad37', 'the logo'),
         ('Red', '#ef4448', 'the logo'), ('Sky', '#29b7ec', 'the logo'), ('Green', '#6cde7c', 'the logo'), ('Teal', '#2bb3c0', 'home glow sweep')] + SHARED[2:],
 'reliaburger': [('Lettering pink', '#ea1e4e', 'the logo lettering'), ('Bun orange', '#f68a1e', 'the logo bun'), ('Lettuce', '#5aba42', 'the logo lettuce'),
                 ('Sauce', '#de2a96', 'the logo sauce'), ('Patty', '#7e421e', 'the logo patty'), ('Rust', '#a83b15', 'website accent'),
                 ('Peach', '#f49463', 'website highlights'), ('Ink', '#181b19', 'website text'), ('Sage', '#e4e9e3', 'website background')],
 'cfpninja': [('Bandana red', '#a21e1e', 'the ninja\'s bandana'), ('Frog green', '#96ba4e', 'the frog'), ('Moss', '#728a36', 'frog shading'),
              ('Laptop', '#4d5454', 'the laptop'), ('Cream', '#f6f5dd', 'eyes and highlights'), ('Ink', '#000000', 'outlines')],
 'certifiedfyi': [('Green', '#158c0f', 'the shield and ".fyi"'), ('Ink', '#151515', 'the word "certified"'), ('White', '#ffffff', 'the tick')],
 'badger': [('Orange', '#ea722a', 'the scanner brackets'), ('Ink', '#151515', 'the badger and the wordmark'), ('White', '#ffffff', 'the badger\'s stripes')],
}

OUT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
K = json.load(open(os.path.join(OUT, 'brandkit.json'))); URL = K['base']
FONT = os.path.join(HERE, 'fonts', 'Figtree%5Bwght%5D.ttf')

def rgb(h): h = h.lstrip('#'); return [int(h[i:i + 2], 16) for i in (0, 2, 4)]
def cmyk(h):
    r, g, b = [v / 255 for v in rgb(h)]; k = 1 - max(r, g, b)
    return [0, 0, 0, 100] if k >= 1 else [round(v * 100) for v in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k)]
def font(px, w):
    f = ImageFont.truetype(FONT, px)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
def slug(s): return ''.join(c if c.isalnum() else '-' for c in s.lower()).strip('-')

for b in K['brands']:
    pal = [dict(name=n, hex=h.lower(), rgb=rgb(h), cmyk=cmyk(h), used=u) for n, h, u in PALETTES[b['key']]]
    b['palette'] = pal; b['color'] = pal[0]['hex']
    d = os.path.join(OUT, b['key'], 'colours'); os.makedirs(d, exist_ok=True); k = b['key']
    json.dump(pal, open(os.path.join(d, k + '-palette.json'), 'w'), indent=1)
    open(os.path.join(d, k + '-palette.css'), 'w').write(':root {\n' + ''.join('  --%s-%s: %s;   /* %s */\n' % (k, slug(c['name']), c['hex'], c['used']) for c in pal) + '}\n')
    open(os.path.join(d, k + '-palette.gpl'), 'w').write('GIMP Palette\nName: %s\nColumns: %d\n#\n' % (b['name'], len(pal)) + ''.join('%3d %3d %3d\t%s\n' % (*c['rgb'], c['name']) for c in pal))
    json.dump({k: {'color': {slug(c['name']): {'$type': 'color', '$value': c['hex'], '$description': c['used']} for c in pal}}}, open(os.path.join(d, k + '-tokens.json'), 'w'), indent=1)
    W = 360 * min(len(pal), 5); rows = (len(pal) + 4) // 5; can = Image.new('RGB', (W, 420 * rows), '#ffffff'); dr = ImageDraw.Draw(can)
    for i, c in enumerate(pal):
        x, y = (i % 5) * 360, (i // 5) * 420
        dr.rounded_rectangle((x + 16, y + 16, x + 344, y + 236), 18, fill=c['hex'], outline='#e2e2e8' if sum(c['rgb']) > 700 else None, width=2)
        dr.text((x + 20, y + 252), c['name'], font=font(30, 700), fill='#14151a'); dr.text((x + 20, y + 292), c['hex'].upper(), font=font(26, 600), fill='#14151a')
        dr.text((x + 20, y + 328), 'RGB %d %d %d' % tuple(c['rgb']), font=font(20, 500), fill='#555'); dr.text((x + 20, y + 356), c['used'][:34], font=font(20, 500), fill='#777')
    can.save(os.path.join(d, k + '-palette.png'))
# refresh sizes / checksums of the colour files, and the main colour in build.py (banners + profile pictures)
for c in K['cards']:
    if c['section'] == 'colours':
        for f in c['files']:
            p = os.path.join(OUT, f['file']); f['size'] = os.path.getsize(p); f['sha256'] = hashlib.sha256(open(p, 'rb').read()).hexdigest()
            if f['fmt'] == 'png': f['px'] = '%dx%d' % Image.open(p).size
by = {f['file']: f for c in K['cards'] for f in c['files'] if f.get('file')}
K['items'] = [by.get(i['file'], i) for i in K['items']]
json.dump(K, open(os.path.join(OUT, 'brandkit.json'), 'w'), indent=1)
bp = os.path.join(HERE, 'build.py'); s = open(bp).read()
import re
for b in K['brands']:
    s = re.sub(r"(dict\(key='%s',[^\n]*?color=')#[0-9a-fA-F]{6}(')" % b['key'], r"\g<1>%s\g<2>" % b['color'], s, count=1)
open(bp, 'w').write(s)
print('\n'.join('%-12s %s' % (b['key'], ' '.join(c['hex'] for c in b['palette'])) for b in K['brands']))
