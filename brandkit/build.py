# build.py <out dir>: the unified brand kit for every brand (Marek 2026-11-09).
# Masters are the best local originals (Dropbox _misc, brand folders, repos). Logos: one-colour vectors traced with potrace
# from the master's own shapes (never redrawn), coloured exactly; stickers, mascots and pets are shipped as they are.
# Social pictures are drawn with Pillow from the brand's sticker + a line of text, in the brand's colours.
import os, sys, json, subprocess, shutil, colorsys, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = sys.argv[1]
DB = '/Users/marek/Library/CloudStorage/Dropbox'
GH = '/Users/marek/Documents/GitHub'
FONTS = os.path.join(os.path.dirname(__file__), 'fonts')
MONO = os.path.join(os.path.dirname(__file__), 'mono')   # potrace output (mono.py): <key>-black.svg

def F(name):
    return os.path.join(FONTS, {'figtree': 'Figtree%5Bwght%5D.ttf', 'montserrat': 'Montserrat%5Bwght%5D.ttf', 'inter': 'Inter%5Bopsz,wght%5D.ttf'}[name])

BRANDS = [
 dict(key='conf42', name='Conf42', color='#2c3fb0', ink='#0f1a3d', font='figtree', site='https://www.conf42.com/',
      tagline='We build online\ndev communities', spelling='Conf42 (capital C, no space)',
      about='Conf42 is where it started, online, in 2020: 30+ online conferences a year on everything from SRE and Kubernetes to Python, Rust and AI. Every talk is free on YouTube, with transcripts and slides at conf42.com.',
      logos=[dict(id='wordmark', label='Wordmark', mono='conf42', color_png=DB + '/_misc/conf42 dark blue.png', color_hex='#1d2a52'),
             dict(id='mark', label='Mark (42)', mono='conf42-mark', color_hex='#2c3fb0')],
      sticker=GH + '/conf42/docs/assets/mediakit/conf42-sticker.png', avatar_from='mark',
      mascots=[('Corgi (404)', GH + '/conf42/docs/assets/conf42/404_corgi.png'), ('Bear with us', GH + '/conf42/docs/assets/conf42/bear_with_us.png')],
      art=[('Illustration, hero', GH + '/conf42/docs/assets/conf42/header_art_full.png'), ('Illustration, blog', GH + '/conf42/docs/assets/conf42/blog_art_full.png'),
           ('Illustration, podcast', GH + '/conf42/docs/assets/conf42/podcast_art_full.png'), ('Illustration, sponsors', GH + '/conf42/docs/assets/conf42/sponsors_art_full.png'),
           ('Space banner', GH + '/conf42/docs/assets/mediakit/conf42-banner.png')]),
 dict(key='sreday', name='SREday', color='#7b3fe4', ink='#1d1240', font='montserrat', site='https://www.sreday.com/',
      tagline='SRE, DevOps & platform\nengineering, in person', spelling='SREday (SRE in capitals, day in lower case)',
      about='SREday is where Site Reliability Engineers, DevOps practitioners and cloud architects meet face to face: talks from people running production at scale, hosted in the offices of companies like Harness, ING and Google.',
      logos=[dict(id='logo', label='Logo', mono='sreday', color_hex='#7b3fe4')],
      sticker=GH + '/llmday/home/assets/images/sreday_sticker.png', avatar_from='sticker',
      mascots=[('Monkey', DB + '/_misc/SREday Monkey New.png'), ('Monkey (404)', GH + '/website/home/assets/images/404.png')],
      art=[('Logo, round', DB + '/SREday/sreday logo.png'), ('Logo, horizontal', DB + '/SREday/sreday logo horizontal.png'), ('Brand gradient', DB + '/SREday/sreday gradient.jpg')]),
 dict(key='llmday', name='LLMday', color='#1f9d6b', ink='#0c2b20', font='montserrat', site='https://www.llmday.com/',
      tagline='AI & LLM engineering,\nin person', spelling='LLMday (LLM in capitals, day in lower case)',
      about='LLMday brings AI engineers, ML engineers and data scientists together in person to share what actually works with LLMs and agents in production: evaluation, RAG, guardrails, cost and everything in between.',
      logos=[dict(id='logo', label='Logo', mono='llmday', color_png=DB + '/_misc/LLMDAY LOGO.png')],
      sticker=DB + '/_misc/llmday_sticker_new.png', avatar_from='sticker',
      mascots=[('Baby llama', DB + '/_misc/baby llama.png'), ('Llama', DB + '/_misc/llmday llama.png'), ('Llama (404)', GH + '/llmday/home/assets/images/404.png')],
      art=[('Brand gradient', DB + '/LLMday/assets/gradient.png')]),
 dict(key='platformday', name='PLATFORMday', color='#e2971d', ink='#2a1c06', font='montserrat', site='https://www.platformday.com/',
      tagline='Platform engineering\n& DevEx, in person', spelling='PLATFORMday (PLATFORM in capitals, day in lower case)',
      about='PLATFORMday is for the people who build and run internal platforms: developer experience, infrastructure, golden paths and the tooling that ties them together, in person.',
      logos=[dict(id='logo', label='Logo', mono='platformday', color_png=DB + '/_misc/PLATFORMday LOGO.png')],
      sticker=DB + '/_misc/PLATFORMday sticker.png', avatar_from='sticker',
      mascots=[('Baby platypus', DB + '/_misc/baby platypus.png'), ('Platypus', DB + '/_misc/PLATFORMday platypus.png'), ('Platypus (404)', GH + '/platformday/home/assets/images/404.png')],
      art=[]),
 dict(key='pec', name='Prompt Engineering Conference', short='PEC', color='#d9467a', ink='#1e1530', font='montserrat', site='https://promptengineering.rocks/',
      tagline='The craft of prompting,\nagents & AI', spelling='Prompt Engineering Conference (short: PEC)',
      about='The Prompt Engineering Conference grew from its online beginnings in 2023 to a full day in London, co-located with LLMday London: the craft of prompting, agents and AI-assisted work.',
      logos=[dict(id='logo', label='Logo', svg_color=GH + '/2025.promptengineering.rocks/home/assets/images/logo-token.svg',
                  svg_white=GH + '/2025.promptengineering.rocks/home/assets/images/logo-white.svg', mono='pec', color_png=DB + '/_misc/PEC logo.png')],
      sticker=DB + '/_misc/PEC logo.png', avatar_from='pec-avatar',
      mascots=[('Avatar', GH + '/2025.promptengineering.rocks/home/assets/images/avatar.png')], art=[]),
 dict(key='devopsnotdead', name='DevOps Not Dead', short='DND', color='#2e9ad8', ink='#14202b', font='montserrat', site='https://www.devopsnotdead.com/',
      tagline='DevOps is not dead.\nCome and see.', spelling='DevOps Not Dead (short: DND)',
      about='DevOps Not Dead is an in-person event series co-created with Harness: practitioners talking honestly about delivering software, in London and New York.',
      logos=[], sticker=GH + '/website/home/assets/sister dnd.png', avatar_from='sticker', mascots=[], art=[]),
 dict(key='reliaburger', name='Reliaburger', color='#a83b15', ink='#181b19', paper='#fff7ef', font='inter', site='https://reliaburger.com/', light=True,
      tagline='One binary. A complete\ncontainer platform.', spelling='Reliaburger (one word)',
      about='Reliaburger is a container orchestrator in Rust by Miko Pawlikowski: one binary, a complete container platform, zero assembly. Source, design notes and a free book on GitHub.',
      logos=[], sticker=DB + '/_misc/clauding burger.png', avatar_from='sticker', flatten_white=True,
      mascots=[], art=[('Logo (v1)', GH + '/reliaburger/assets/images/reliaburger_logo_v1.jpg'), ('Burger', GH + '/reliaburger/docs/website/assets/burger-still.webp')]),
 dict(key='cfpninja', name='CFP Ninja', color='#c8262c', ink='#1c2a12', font='montserrat', site='https://cfp.ninja/',
      tagline='Find a stage.\nSubmit once.', spelling='CFP Ninja (cfp.ninja as the address)',
      about='CFP Ninja is the open Call for Papers platform every Conf42, SREday and LLMday CFP runs on. Speakers find open calls and submit once; organisers review in one place.',
      logos=[dict(id='mark', label='Mark', mono='cfpninja-mark', color_png=DB + '/_misc/cfpninja MINI.png', multi=True)],
      sticker=DB + '/_misc/cfpninja bigga logo.png', avatar_from='sticker', mascots=[], art=[]),
 dict(key='certifiedfyi', name='Certified FYI', color='#22a339', ink='#1b1f23', paper='#f4f7f4', font='montserrat', site='https://certified.fyi/', light=True,
      tagline='Verifiable certificates\nfor speakers & organisers', spelling='Certified FYI (certified.fyi as the address)',
      about='Certified FYI issues verifiable certificates of achievement: organisers issue them, speakers collect them on a public profile.',
      logos=[dict(id='logo', label='Logo', mono='certifiedfyi', color_png=DB + '/_misc/certified fyi.png', multi=True)],
      sticker=DB + '/_misc/certified fyi.png', avatar_from='mark-crop', mascots=[], art=[]),
 dict(key='badger', name='Badger', color='#f26b1d', ink='#151515', paper='#f6f4f1', font='montserrat', site='https://scan.sreday.com/', light=True,
      tagline='Event badges,\nprinted at the door', spelling='Badger (Snout by Badger for the lead scanner)',
      about='Badger prints attendee badges at the door of every SREday, LLMday and PLATFORMday; Snout by Badger is its sponsor lead scanner.',
      logos=[dict(id='badger', label='Badger', mono='badger', color_png=GH + '/badger/scanner/assets/badger-logo.webp', multi=True),
             dict(id='snout', label='Snout by Badger', mono='snout', color_png=GH + '/badger/scanner/assets/snout-logo.png', multi=True)],
      sticker=GH + '/badger/scanner/assets/badger-logo.webp', avatar_from='badger-head', mascots=[], art=[]),
]

# the social pictures (sizes from each platform's own help pages, 2026-11; LinkedIn's company cover is now 1512x256)
SOCIAL = [
 ('linkedin-company', 'LinkedIn company page cover', 1512, 256), ('linkedin-company-hd', 'LinkedIn company page cover, sharp (6:1)', 4200, 700),
 ('linkedin-profile', 'LinkedIn profile banner', 1584, 396), ('x-header', 'X (Twitter) header', 1500, 500),
 ('bluesky-banner', 'Bluesky banner', 3000, 1000), ('facebook-cover', 'Facebook cover', 1640, 624),
 ('youtube-banner', 'YouTube channel banner', 2560, 1440), ('og-image', 'Link preview (Open Graph)', 1200, 630),
 ('video-background', 'Zoom / Teams / Meet background', 1920, 1080), ('email-signature', 'Email signature banner', 1200, 300),
]

items = []   # kit.json rows
def add(b, group, label, path, **kw):
    rel = os.path.relpath(path, OUT)
    row = dict(brand=b['key'], group=group, label=label, file=rel, size=os.path.getsize(path))
    ext = path.rsplit('.', 1)[1].lower()
    if ext in ('png', 'jpg', 'jpeg', 'webp'):
        row['px'] = '%dx%d' % Image.open(path).size
    row.update(kw); items.append(row)

def hexrgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def shade(h, l):   # same hue, lightness l (0-1)
    r, g, b = [v / 255 for v in hexrgb(h)]; hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    r, g, b = colorsys.hls_to_rgb(hh, l, min(ss, .75)); return '#%02x%02x%02x' % (round(r * 255), round(g * 255), round(b * 255))

def trimmed(im):
    im = im.convert('RGBA'); bb = im.getchannel('A').point(lambda a: 255 if a > 8 else 0).getbbox()
    return im.crop(bb) if bb else im

def flatten_white(im):
    """Clean white page around an illustration -> transparent (flood fill from the edges only; the art is untouched)."""
    im = im.convert('RGBA'); a = np.asarray(im).copy(); h, w = a.shape[:2]
    white = (a[..., :3].min(axis=2) > 238)
    seen = np.zeros((h, w), bool); stack = [(0, x) for x in range(w)] + [(h - 1, x) for x in range(w)] + [(y, 0) for y in range(h)] + [(y, w - 1) for y in range(h)]
    while stack:
        y, x = stack.pop()
        if seen[y, x] or not white[y, x]: continue
        seen[y, x] = True
        if y > 0: stack.append((y - 1, x))
        if y < h - 1: stack.append((y + 1, x))
        if x > 0: stack.append((y, x - 1))
        if x < w - 1: stack.append((y, x + 1))
    a[seen, 3] = 0
    return Image.fromarray(a)

def opti(path):
    if path.endswith('.png'):
        subprocess.run(['oxipng', '-q', '-o', '2', '--strip', 'safe', path], check=False)

def svg_recolor(svg_text, fill):
    return svg_text.replace('fill="#000000"', 'fill="%s"' % fill)

def write_logo_set(b, lg, d):
    """SVG/PNG/PDF/EPS in colour, black and white, + on-light / on-dark tiles."""
    key = '%s-%s' % (b['key'], lg['id']) if lg['id'] not in ('logo', 'wordmark') else b['key'] + '-' + lg['id']
    os.makedirs(d, exist_ok=True)
    variants = {}
    if lg.get('mono'):
        base = open(os.path.join(MONO, lg['mono'] + '-black.svg')).read()
        variants['black'] = base
        variants['white'] = svg_recolor(base, '#ffffff')
        if lg.get('color_hex') and not lg.get('multi'):
            variants['color'] = svg_recolor(base, lg['color_hex'])
        elif lg.get('color_png') and not lg.get('multi') and not lg.get('svg_color'):
            # single-colour logo: the vector filled with the master's own ink colour
            a = np.asarray(Image.open(lg['color_png']).convert('RGBA')); ink = a[a[..., 3] > 200][:, :3]
            med = np.median(ink, axis=0).astype(int); lg['color_hex'] = '#%02x%02x%02x' % tuple(med)
            variants['color'] = svg_recolor(base, lg['color_hex'])
    if lg.get('svg_color'):
        variants['color'] = open(lg['svg_color']).read()
    if lg.get('svg_white'):
        variants['white'] = open(lg['svg_white']).read()
    for v, svg in variants.items():
        p = os.path.join(d, '%s-%s.svg' % (key, v)); open(p, 'w').write(svg)
        add(b, 'Logos', '%s, %s' % (lg['label'], {'color': 'colour', 'black': 'black', 'white': 'white'}[v]), p, variant=v, fmt='svg', bg='dark' if v == 'white' else 'light')
        for fmt in ('pdf', 'eps'):
            q = p[:-4] + '.' + fmt; subprocess.run(['rsvg-convert', '-f', fmt, p, '-o', q], check=True)
            add(b, 'Logos', '%s, %s' % (lg['label'], v), q, variant=v, fmt=fmt, print=True)
        png = p[:-4] + '.png'; subprocess.run(['rsvg-convert', '-w', '2000', p, '-o', png], check=True); opti(png)
        add(b, 'Logos', '%s, %s' % (lg['label'], {'color': 'colour', 'black': 'black', 'white': 'white'}[v]), png, variant=v, fmt='png', bg='dark' if v == 'white' else 'light')
    # a multi-colour logo without a colour vector: the master itself, trimmed, as the colour PNG
    if 'color' not in variants and lg.get('color_png'):
        im = trimmed(Image.open(lg['color_png'])); im.thumbnail((2000, 2000))
        png = os.path.join(d, '%s-color.png' % key); im.save(png); opti(png)
        add(b, 'Logos', '%s, colour' % lg['label'], png, variant='color', fmt='png', bg='light')
        variants['color'] = None
    # tiles: how to use it on light and on dark (clear space = a quarter of the logo height on every side)
    for tile, bgc, v in (('on-light', '#ffffff', 'color' if 'color' in variants else 'black'), ('on-dark', b['ink'], 'white')):
        src = os.path.join(d, '%s-%s.png' % (key, v))
        if not os.path.isfile(src): continue
        lo = Image.open(src).convert('RGBA'); W, H = 2400, 1350
        lo.thumbnail((int(W * .62), int(H * .5)), Image.LANCZOS)
        can = Image.new('RGBA', (W, H), bgc); can.alpha_composite(lo, ((W - lo.width) // 2, (H - lo.height) // 2))
        p = os.path.join(d, '%s-%s.png' % (key, tile)); can.convert('RGB').save(p); opti(p)
        add(b, 'Logos', '%s on %s' % (lg['label'], 'light' if tile == 'on-light' else 'dark'), p, variant=tile, fmt='png', tile=True)
    return key

def gradient(W, H, color, ink, light=False, paper=None):
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    cx, cy = W * .72, H * .95; r = np.sqrt(((xx - cx) / (W * 1.1)) ** 2 + ((yy - cy) / (H * 1.5)) ** 2)
    t = np.clip(r, 0, 1)[..., None]
    if light:
        c0, c1 = np.array(hexrgb(paper or '#ffffff'), np.float32), np.array(hexrgb(shade(color, .93)), np.float32)
        img = c1 * (1 - t) + c0 * t
    else:
        c0, c1 = np.array(hexrgb(shade(color, .22)), np.float32), np.array(hexrgb(shade(color, .40)), np.float32)
        img = c1 * (1 - t) + c0 * t
    return Image.fromarray(img.astype(np.uint8), 'RGB').convert('RGBA')

def font(b, px, weight=700):
    f = ImageFont.truetype(F(b['font']), px)
    try: f.set_variation_by_axes([weight] if b['font'] != 'inter' else [14, weight])
    except Exception: pass
    return f

def social(b, sticker, d):
    os.makedirs(d, exist_ok=True)
    light = b.get('light', False); txt_col = b['ink'] if light else '#ffffff'
    for sid, label, W, H in SOCIAL:
        can = gradient(W, H, b['color'], b['ink'], light, b.get('paper'))
        # the safe area: YouTube shows only the middle 1546x423 on every device; X crops 60 px top and bottom
        sw, sh = (1546, 423) if sid == 'youtube-banner' else (W, H - 120 if sid == 'x-header' else H)
        ox, oy = (W - sw) // 2, (H - sh) // 2
        lines = b['tagline'].split('\n')
        tall = sh / sw > .45
        st_h = int(sh * (.62 if tall else .78)); st = sticker.copy(); st.thumbnail((int(st_h * 1.6), st_h), Image.LANCZOS)
        fs = int(sh * (.085 if tall else .135)) if sid != 'email-signature' else int(sh * .17)
        f = font(b, fs, 700)
        tw = max(f.getbbox(l)[2] for l in lines); lh = int(fs * 1.12); th = lh * len(lines)
        gap = int(sw * .04)
        if tall:   # stacked: sticker over the words, both centred
            total = st.height + gap + th; y0 = oy + (sh - total) // 2
            sx, sy = ox + (sw - st.width) // 2, y0; tx, ty = None, y0 + st.height + gap
        else:      # one row: words, gap, sticker - centred as a group (never touching)
            total = tw + gap + st.width
            if total > sw * .9:
                k = sw * .9 / total; f = font(b, int(fs * k)); fs = int(fs * k); lh = int(fs * 1.12); th = lh * len(lines)
                tw = max(f.getbbox(l)[2] for l in lines); total = tw + gap + st.width
            x0 = ox + (sw - total) // 2
            tx, ty = x0, oy + (sh - th) // 2; sx, sy = x0 + tw + gap, oy + (sh - st.height) // 2
        sh_img = Image.new('RGBA', can.size, (0, 0, 0, 0)); a = st.getchannel('A').point(lambda v: int(v * .32))
        shadow = Image.new('RGBA', st.size, (0, 0, 0, 255)); shadow.putalpha(a); sh_img.alpha_composite(shadow, (sx, sy + int(st.height * .03)))
        can.alpha_composite(sh_img.filter(ImageFilter.GaussianBlur(st.height * .03)))
        can.alpha_composite(st, (sx, sy))
        dr = ImageDraw.Draw(can)
        for i, l in enumerate(lines):
            lw = f.getbbox(l)[2]
            x = tx if tx is not None else ox + (sw - lw) // 2
            dr.text((x, ty + i * lh), l, font=f, fill=txt_col)
        p = os.path.join(d, '%s-%s-%dx%d.png' % (b['key'], sid, W, H)); can.convert('RGB').save(p); opti(p)
        add(b, 'Social', label, p, platform=sid, fmt='png')

def avatars(b, src, d):
    os.makedirs(d, exist_ok=True)
    for shape in ('square', 'round'):
        for n in (1000, 400):
            can = Image.new('RGBA', (n, n), b['paper'] if b.get('light') else b['color'])
            im = src.copy(); pad = .2 if shape == 'round' else .14; im.thumbnail((int(n * (1 - 2 * pad)), int(n * (1 - 2 * pad))), Image.LANCZOS)
            can.alpha_composite(im, ((n - im.width) // 2, (n - im.height) // 2))
            if shape == 'round':
                m = Image.new('L', (n * 4, n * 4), 0); ImageDraw.Draw(m).ellipse((0, 0, n * 4 - 1, n * 4 - 1), fill=255); can.putalpha(m.resize((n, n), Image.LANCZOS))
            p = os.path.join(d, '%s-avatar-%s-%d.png' % (b['key'], shape, n)); can.save(p); opti(p)
            add(b, 'Avatars', 'Avatar, %s, %d px' % (shape, n), p, fmt='png', bg='light')

def cmyk(h):
    r, g, bb = [v / 255 for v in hexrgb(h)]; k = 1 - max(r, g, bb)
    if k >= 1: return (0, 0, 0, 100)
    return tuple(round(v * 100) for v in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - bb - k) / (1 - k), k))

def palette(b, d):
    os.makedirs(d, exist_ok=True)
    cols = [('Primary', b['color']), ('Ink', b['ink']), ('Dark', shade(b['color'], .22)), ('Light', shade(b['color'], .93)), ('Paper', b.get('paper', '#ffffff'))]
    b['palette'] = [dict(name=n, hex=h.lower(), rgb=list(hexrgb(h)), cmyk=list(cmyk(h))) for n, h in cols]
    json.dump(b['palette'], open(os.path.join(d, b['key'] + '-palette.json'), 'w'), indent=1)
    open(os.path.join(d, b['key'] + '-palette.css'), 'w').write(':root {\n' + ''.join('  --%s-%s: %s;\n' % (b['key'], c['name'].lower(), c['hex']) for c in b['palette']) + '}\n')
    open(os.path.join(d, b['key'] + '-palette.gpl'), 'w').write('GIMP Palette\nName: %s\nColumns: %d\n#\n' % (b['name'], len(cols)) + ''.join('%3d %3d %3d\t%s %s\n' % (*c['rgb'], b['name'], c['name']) for c in b['palette']))
    W, H = 2000, 700; can = Image.new('RGB', (W, H), '#ffffff'); dr = ImageDraw.Draw(can); fw = W // len(cols); f1 = font(b, 40, 700); f2 = font(b, 28, 500)
    for i, c in enumerate(b['palette']):
        dr.rectangle((i * fw, 0, (i + 1) * fw - 1, 470), fill=c['hex'], outline='#dddddd' if c['hex'] in ('#ffffff',) else None)
        y = 500
        for t, ff in ((c['name'], f1), (c['hex'].upper(), f2), ('RGB %d %d %d' % tuple(c['rgb']), f2), ('CMYK %d %d %d %d' % tuple(c['cmyk']), f2)):
            dr.text((i * fw + 24, y), t, font=ff, fill='#111111'); y += 46 if ff is f1 else 40
    p = os.path.join(d, b['key'] + '-palette.png'); can.save(p); opti(p)
    add(b, 'Colours', 'Palette', p, fmt='png')
    for ext, lab in (('json', 'Palette, JSON'), ('css', 'Palette, CSS variables'), ('gpl', 'Palette, GIMP / Inkscape')):
        add(b, 'Colours', lab, os.path.join(d, b['key'] + '-palette.' + ext), fmt=ext)

def copy_as_is(b, group, label, src, d, name):
    os.makedirs(d, exist_ok=True); ext = src.rsplit('.', 1)[1].lower()
    p = os.path.join(d, name + '.' + ('png' if ext == 'png' else ext)); shutil.copyfile(src, p); opti(p)
    add(b, group, label, p, fmt=ext, bg='light')

def slug(s):
    return ''.join(ch if ch.isalnum() else '-' for ch in s.lower()).strip('-').replace('--', '-')

brands_out = []
for b in BRANDS:
    root = os.path.join(OUT, b['key']); os.makedirs(root, exist_ok=True)
    print('==', b['name'])
    keys = [write_logo_set(b, lg, os.path.join(root, 'logos')) for lg in b['logos']]
    st = Image.open(b['sticker'])
    st = flatten_white(st) if b.get('flatten_white') else st.convert('RGBA'); st = trimmed(st)
    copy_as_is(b, 'Stickers', 'Sticker' if b['sticker'] not in [lg.get('color_png') for lg in b['logos']] else 'Logo, original', b['sticker'], os.path.join(root, 'stickers'), b['key'] + '-sticker')
    social(b, st, os.path.join(root, 'social'))
    av = st
    if b['avatar_from'] == 'mark':
        av = Image.open(os.path.join(root, 'logos', b['key'] + '-mark-white.png')).convert('RGBA')
    elif b['avatar_from'] == 'pec-avatar':   # PEC's own avatar artwork, as it is
        av = trimmed(Image.open(GH + '/2025.promptengineering.rocks/home/assets/images/avatar.png'))
    elif b['avatar_from'] == 'badger-head':
        av = trimmed(Image.open(GH + '/badger/scanner/assets/badger-head.png'))
    elif b['avatar_from'] == 'mark-crop':   # certified.fyi: the shield alone (the left part of the logo, as drawn)
        im = trimmed(Image.open(b['logos'][0]['color_png'])); a = np.asarray(im)[..., 3] > 8
        cols = np.where(a[: int(im.height * .55)].any(axis=0))[0]; av = trimmed(im.crop((cols.min(), 0, cols.max() + 1, int(im.height * .58))))
    avatars(b, av, os.path.join(root, 'avatars'))
    for label, src in b['mascots']:
        copy_as_is(b, 'Mascots', label, src, os.path.join(root, 'mascots'), '%s-%s' % (b['key'], slug(label)))
    for label, src in b['art']:
        if os.path.isfile(src): copy_as_is(b, 'Artwork', label, src, os.path.join(root, 'artwork'), '%s-%s' % (b['key'], slug(label)))
    palette(b, os.path.join(root, 'colours'))
    open(os.path.join(root, b['key'] + '-about.txt'), 'w').write('%s\n\n%s\n\nName: %s\nWebsite: %s\nPress: hello@sreday.com\n' % (b['name'], b['about'], b['spelling'], b['site']))
    add(b, 'Press', 'About text (boilerplate)', os.path.join(root, b['key'] + '-about.txt'), fmt='txt')
    brands_out.append({k: b[k] for k in ('key', 'name', 'color', 'ink', 'site', 'about', 'spelling', 'tagline', 'palette') if k in b} | {'short': b.get('short', ''), 'light': b.get('light', False)})

# ---- machine-readable index for scripts and agents: absolute URLs, checksums, types ----------------------------------
import hashlib, mimetypes
URL = (sys.argv[2] if len(sys.argv) > 2 else 'https://www.conf42.com/assets/brandkit/').rstrip('/') + '/'
mimetypes.add_type('application/postscript', '.eps'); mimetypes.add_type('text/plain', '.gpl')
for it in items:
    path = os.path.join(OUT, it['file'])
    it['url'] = URL + it['file']
    it['sha256'] = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    it['mime'] = mimetypes.guess_type(path)[0] or 'application/octet-stream'
# design tokens per brand (W3C Design Tokens format), next to the palette files
for bo in brands_out:
    tok = {bo['key']: {'color': {c['name'].lower(): {'$type': 'color', '$value': c['hex']} for c in bo['palette']}}}
    p = os.path.join(OUT, bo['key'], 'colours', bo['key'] + '-tokens.json'); json.dump(tok, open(p, 'w'), indent=1)
    b = next(x for x in BRANDS if x['key'] == bo['key']); add(b, 'Colours', 'Design tokens (W3C)', p, fmt='json')
    it = items[-1]; it['url'] = URL + it['file']; it['sha256'] = hashlib.sha256(open(p, 'rb').read()).hexdigest(); it['mime'] = 'application/json'
json.dump(dict(name='Conf42 family media kit', generated='2026-11-09', base=URL, index=URL + 'brandkit.json',
               usage='Every file: items[].url. Filter by brand, group (Logos, Colours, Social, Avatars, Stickers, Mascots, Artwork, Press), variant (color, black, white, on-light, on-dark) and fmt (svg, png, pdf, eps, ...).',
               brands=brands_out, items=items), open(os.path.join(OUT, 'brandkit.json'), 'w'), indent=1)
# brandkit.md: the same, as Markdown (readable by people, LLMs and grep)
md = ['# Conf42 family media kit', '', 'Machine-readable index: %sbrandkit.json (every file with url, size, px, sha256, mime).' % URL, '',
      '```sh', '# every SREday file', "curl -s %sbrandkit.json | jq -r '.items[] | select(.brand==\"sreday\") | .url' | xargs -n1 curl -sO" % URL,
      '# one logo', 'curl -O %ssreday/logos/sreday-logo-white.svg' % URL, '```', '']
for bo in brands_out:
    md += ['## %s' % bo['name'], '', bo['about'], '', 'Name: %s. Website: %s' % (bo['spelling'], bo['site']), '', '| Colour | HEX | RGB | CMYK |', '|---|---|---|---|']
    md += ['| %s | `%s` | %s | %s |' % (c['name'], c['hex'].upper(), ' '.join(map(str, c['rgb'])), ' '.join(map(str, c['cmyk']))) for c in bo['palette']]
    md += ['']
    for g in ('Logos', 'Social', 'Avatars', 'Stickers', 'Mascots', 'Artwork', 'Colours', 'Press'):
        rows = [i for i in items if i['brand'] == bo['key'] and i['group'] == g]
        if not rows: continue
        md += ['### %s' % g, ''] + ['- [%s (%s%s)](%s)' % (i['label'], i['fmt'].upper(), ', ' + i['px'] if i.get('px') else '', i['url']) for i in rows] + ['']
open(os.path.join(OUT, 'brandkit.md'), 'w').write('\n'.join(md))
open(os.path.join(OUT, 'llms.txt'), 'w').write('# Conf42 family media kit\n\n> Logos (SVG/PNG/PDF/EPS in colour, black and white), colours (HEX/RGB/CMYK, design tokens), social banners, avatars and mascots for Conf42, SREday, LLMday, PLATFORMday, Prompt Engineering Conference, DevOps Not Dead, Reliaburger, CFP Ninja, Certified FYI and Badger.\n\n- [Index (JSON)](%sbrandkit.json): every file with url, size, px, sha256, mime\n- [Index (Markdown)](%sbrandkit.md)\n' % (URL, URL))
tot = sum(i['size'] for i in items)
print('items', len(items), 'size %.1f MB' % (tot / 1e6))
