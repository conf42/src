# enrich.py <kit dir>: after build.py (Marek 2026-11-09).
# 1. sorts every file into plain-language sections and asset cards (one card = one picture, every format of it)
# 2. tags each card for the forgiving search ("logo" finds every asset that shows the logo, not just the files named so)
# 3. vectorises every brand picture with vtracer (open source), so each one has a PNG and an SVG
# 4. adds the event splashes of every conference from every repo (linked where they live, not copied)
import os, sys, json, re, glob, hashlib, yaml, vtracer
from PIL import Image

OUT = sys.argv[1]
GH = '/Users/marek/Documents/GitHub'
K = json.load(open(os.path.join(OUT, 'brandkit.json')))
URL = K['base']

SECTIONS = [  # order on the page, title, the one-line help a five-year-old can follow
 ('logos', 'Logos', 'Put these on slides, websites and posters.'),
 ('colours', 'Colours', 'Click a colour to copy its code.'),
 ('avatars', 'Profile pictures', 'For LinkedIn, X, Slack, YouTube and anywhere that asks for a picture.'),
 ('banners', 'Banners & covers', 'The wide pictures at the top of social media pages, video-call backgrounds and email signatures.'),
 ('stickers', 'Stickers', 'The stickers we hand out at events.'),
 ('mascots', 'Mascots & pets', 'Our animals, including the ones on the "page not found" screens.'),
 ('animations', 'Animations', 'Moving pictures for posts and slides: WebP for the web, MP4 for videos and slides.'),
 ('illustrations', 'Illustrations', 'Bigger drawings and backgrounds from our websites.'),
 ('splashes', 'Event splashes', 'The artwork of every conference we have run.'),
 ('about', 'About text', 'A paragraph about each brand, ready to paste.'),
]
GROUP2SEC = {'Logos': 'logos', 'Colours': 'colours', 'Avatars': 'avatars', 'Social': 'banners', 'Stickers': 'stickers',
             'Mascots': 'mascots', 'Artwork': 'illustrations', 'Press': 'about'}
TAGS = {
 'logos': 'logo logos brand wordmark mark icon symbol emblem trademark',
 'colours': 'colour color colours colors palette hex rgb cmyk swatch swatches code tokens css brand',
 'avatars': 'avatar avatars profile picture photo pfp icon round circle square logo social',
 'banners': 'banner banners cover header background social logo wallpaper',
 'stickers': 'sticker stickers logo laptop swag merch badge',
 'mascots': 'mascot mascots pet pets animal animals character characters cute drawing',
 'animations': 'animation animations animated moving motion gif loop video clip webp mp4 movie sticker',
 'illustrations': 'illustration illustrations art artwork drawing picture background',
 'splashes': 'splash splashes event events conference conferences artwork poster cover picture',
 'about': 'about text boilerplate description press bio blurb paragraph copy',
}
PLATFORM_TAGS = {'linkedin': 'linkedin', 'x-header': 'x twitter tweet', 'bluesky': 'bluesky bsky', 'facebook': 'facebook fb meta',
                 'youtube': 'youtube yt channel', 'og-image': 'og opengraph open graph link preview share sharing website',
                 'video-background': 'zoom teams meet google video call virtual background', 'email-signature': 'email mail signature gmail outlook'}
VARIANT_TAGS = {'color': 'colour color full-colour coloured', 'black': 'black mono monochrome one-colour dark-on-light',
                'white': 'white reversed knockout inverse light-on-dark for-dark-backgrounds', 'on-light': 'preview light white-background', 'on-dark': 'preview dark black-background'}
ANIMALS = {'monkey': 'monkey chimp ape', 'llama': 'llama alpaca', 'platypus': 'platypus', 'corgi': 'corgi dog puppy', 'bear': 'bear teddy', 'ninja': 'ninja frog'}

def stem(f):
    return re.sub(r'\.(png|svg|pdf|eps|jpe?g|webp|json|css|gpl|txt)$', '', f)

def vector(png_path, svg_path):
    im = Image.open(png_path).convert('RGBA'); im.thumbnail((1600, 1600))
    tmp = svg_path + '.in.png'; im.save(tmp)
    vtracer.convert_image_to_svg_py(tmp, svg_path, colormode='color', hierarchical='stacked', mode='spline', color_precision=6, filter_speckle=4,
                                     layer_difference=16, corner_threshold=60, length_threshold=4.0, splice_threshold=45, path_precision=2)
    os.remove(tmp)

assets = {}   # asset id -> card
for it in K['items']:
    sec = GROUP2SEC[it['group']]
    aid = '%s|%s|%s' % (it['brand'], sec, stem(it['file']) if sec != 'logos' else it['label'].split(',')[0].split(' on ')[0] + '|' + it.get('variant', ''))
    if sec == 'colours':
        aid = '%s|colours|%s' % (it['brand'], it['fmt'] if it['label'] != 'Palette' else 'palette')
    a = assets.setdefault(aid, dict(id=aid, brand=it['brand'], section=sec, files=[], tags=set()))
    a['files'].append(it)
    a['tags'].update(TAGS[sec].split())
    if sec == 'logos':
        base = it['label'].split(',')[0].split(' on ')[0]; v = it.get('variant', '')
        nice = {'color': 'in colour', 'black': 'in black', 'white': 'in white (for dark backgrounds)', 'on-light': 'on a light background', 'on-dark': 'on a dark background'}[v]
        a['title'] = '%s %s' % (base, nice); a['tags'].update(VARIANT_TAGS.get(v, '').split()); a['tags'].update(base.lower().split())
        a['dark'] = v in ('white', 'on-dark'); a['order'] = ['color', 'black', 'white', 'on-light', 'on-dark'].index(v)
    else:
        a['title'] = it['label']; a['tags'].update(re.findall(r'[a-z0-9]+', it['label'].lower()))
    if it.get('platform'):
        for k, t in PLATFORM_TAGS.items():
            if it['platform'].startswith(k): a['tags'].update(t.split())
    if it.get('print'): a['tags'].update('print vector'.split())
    a['tags'].add(it['fmt']);
    if it['fmt'] == 'svg': a['tags'].update('vector scalable'.split())
    if it['fmt'] == 'png': a['tags'].update('transparent raster image'.split())
    if '404' in it['label']: a['tags'].update('404 error not-found notfound page'.split())
    for an, t in ANIMALS.items():
        if an in it['label'].lower() or an in it['file']: a['tags'].update(t.split())

# vectorise every brand picture that has no SVG yet (logos already have traced vectors)
n = 0
for a in assets.values():
    if a['section'] in ('colours', 'about', 'logos'): continue
    pngs = [f for f in a['files'] if f['fmt'] in ('png', 'jpg', 'jpeg', 'webp')]
    if not pngs or any(f['fmt'] == 'svg' for f in a['files']): continue
    src = os.path.join(OUT, pngs[0]['file']); rel = stem(pngs[0]['file']) + '.svg'; dst = os.path.join(OUT, rel)
    vector(src, dst); n += 1
    a['files'].append(dict(brand=a['brand'], group=pngs[0]['group'], label=pngs[0]['label'], file=rel, size=os.path.getsize(dst), fmt='svg',
                           url=URL + rel, sha256=hashlib.sha256(open(dst, 'rb').read()).hexdigest(), mime='image/svg+xml', traced=True))
print('vectorised', n)

# event splashes, every conference in every repo, linked where they live (not copied)
splashes = []
m = yaml.safe_load(open(GH + '/conf42/metadata.yml'))
names, codes = {}, {}
for e in m.get('events') or []:
    if not isinstance(e, dict) or not e.get('thumbnail_path'): continue
    code = os.path.basename(e['thumbnail_path']).split('_Event_Splash')[0]
    names[code] = 'Conf42 %s %s' % (e['name'], e['date'].year)
    codes[re.sub(r'\d+$', '', code)] = e['name']
for p in sorted(glob.glob(GH + '/conf42/docs/assets/splash/*_Event_Splash.*')):
    code, ext = os.path.basename(p).split('_Event_Splash'); ext = ext.lower()
    if ext not in ('.png', '.jpg', '.jpeg'): continue
    s = next((x for x in splashes if x['code'] == code), None)
    if not s:
        yr = re.search(r'(\d{4})$', code); base = re.sub(r'\d+$', '', code)
        title = names.get(code) or 'Conf42 %s %s' % (codes.get(base, base.title()), yr.group(1) if yr else '')
        s = dict(code=code, brand='conf42', title=title.strip(), year=int(yr.group(1)) if yr else 0); splashes.append(s)
    url = 'https://www.conf42.com/assets/splash/' + os.path.basename(p)
    if ext == '.png': s['full'] = url; s['px'] = '%dx%d' % Image.open(p).size; s['size'] = os.path.getsize(p)
    else: s['preview'] = url
    s.setdefault('full', url); s.setdefault('size', os.path.getsize(p))
SITES = {'sreday': ('website', 'https://sreday.com', 'SREday'), 'llmday': ('llmday', 'https://llmday.com', 'LLMday'), 'platformday': ('platformday', 'https://platformday.com', 'PLATFORMday'),
         'pec': ('2026.promptengineering.rocks', 'https://promptengineering.rocks', 'Prompt Engineering Conference'), 'dnd': ('devopsnotdead', 'https://devopsnotdead.com', 'DevOps Not Dead')}
CITY = {'nyc': 'NYC', 'sf': 'San Francisco', 'online': 'Online'}
for pref, (repo, site, bname) in SITES.items():
    for p in sorted(glob.glob(GH + '/%s/home/assets/images/events/%s-*' % (repo, pref))):
        f = os.path.basename(p); parts = os.path.splitext(f)[0].split('-')[1:]
        yr = next((x for x in parts if re.fullmatch(r'\d{4}', x)), ''); q = next((x.upper() for x in parts if re.fullmatch(r'q\d', x)), '')
        city = ' '.join(CITY.get(x, x.capitalize()) for x in parts if x not in (yr, q.lower()))
        city = CITY.get('-'.join(x for x in parts if x not in (yr, q.lower())), city)
        url = '%s/assets/images/events/%s' % (site, f)
        splashes.append(dict(code=os.path.splitext(f)[0], brand='devopsnotdead' if pref == 'dnd' else pref, title=' '.join(x for x in (bname, city, yr, q) if x),
                             year=int(yr or 0), full=url, preview=url, px='%dx%d' % Image.open(p).size, size=os.path.getsize(p)))
splashes.sort(key=lambda s: (-s['year'], s['title']))
for s in splashes:
    words = set(re.findall(r'[a-z0-9]+', s['title'].lower())) | set(TAGS['splashes'].split())
    assets['%s|splashes|%s' % (s['brand'], s['code'])] = dict(id=s['code'], brand=s['brand'], section='splashes', title=s['title'], year=s['year'], tags=words,
        files=[dict(brand=s['brand'], file=None, url=s['full'], preview=s.get('preview', s['full']), fmt=s['full'].rsplit('.', 1)[1].lower(), size=s['size'], px=s['px'], label=s['title'])], browser_svg=True)
print('splashes', len(splashes))

# animations: every animated asset as an animated WebP (img2webp) and an MP4 (H.264), silent loops
import subprocess, tempfile, shutil
ANIMS = [
 ('sreday', 'Monkeys', GH + '/website/home/assets/monkeys GIF.gif', 'monkey monkeys'),
 ('sreday', 'Monkey dance', GH + '/website/home/assets/maupa GIF.gif', 'monkey dance dancing'),
 ('sreday', 'SRE monkeys', GH + '/website/home/assets/sre monkeys.mp4', 'monkey monkeys'),
 ('llmday', 'Llama', GH + '/llmday/home/assets/llama GIF.gif', 'llama alpaca'),
 ('llmday', 'Llama conspiracy', GH + '/llmday/home/assets/llama conspiracy GIF.gif', 'llama alpaca conspiracy'),
 ('devopsnotdead', 'Dance', GH + '/devopsnotdead/home/assets/dnd GIF.gif', 'dance dancing'),
 ('devopsnotdead', 'Nothing planned', GH + '/devopsnotdead/home/assets/images/devopsnotdead nothing planned.mp4', 'nothing planned'),
 ('reliaburger', 'Burger loop', GH + '/reliaburger/docs/website/assets/burger-loop.mp4', 'burger food'),
 ('conf42', 'Hero animation', GH + '/conf42/docs/assets/conf42/header_art.mp4', 'hero illustration'),
]
def slug(t): return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')
for bk, title, src, extra in ANIMS:
    d = os.path.join(OUT, bk, 'animations'); os.makedirs(d, exist_ok=True); base = '%s-%s' % (bk, slug(title))
    mp4, webp = os.path.join(d, base + '.mp4'), os.path.join(d, base + '.webp')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-vf', "scale='min(960,iw)':-2:flags=lanczos,format=yuv420p", '-c:v', 'libx264', '-crf', '23',
                    '-preset', 'slow', '-movflags', '+faststart', '-an', mp4], check=True)
    tmp = tempfile.mkdtemp()
    subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-vf', "fps=15,scale='min(720,iw)':-2:flags=lanczos", os.path.join(tmp, 'f%04d.png')], check=True)
    frames = sorted(glob.glob(tmp + '/f*.png'))
    subprocess.run(['img2webp', '-loop', '0', '-lossy', '-q', '72', '-m', '6', '-d', '67'] + frames + ['-o', webp], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.rmtree(tmp)
    files = []
    for path, fmt, mime in ((webp, 'webp', 'image/webp'), (mp4, 'mp4', 'video/mp4')):
        rel = os.path.relpath(path, OUT); row = dict(brand=bk, group='Animations', label=title, file=rel, size=os.path.getsize(path), fmt=fmt, url=URL + rel,
                                                   sha256=hashlib.sha256(open(path, 'rb').read()).hexdigest(), mime=mime, animated=True)
        if fmt == 'webp': row['px'] = '%dx%d' % Image.open(path).size
        files.append(row)
    assets['%s|animations|%s' % (bk, base)] = dict(id=base, brand=bk, section='animations', title=title, files=files,
                                                   tags=set(TAGS['animations'].split()) | set(extra.split()) | set(title.lower().split()))
    print('animation', base, '%.1f MB webp, %.1f MB mp4' % (os.path.getsize(webp) / 1e6, os.path.getsize(mp4) / 1e6))

# brand names and short names are search words on every card of that brand
bn = {b['key']: b for b in K['brands']}
cards = []
for a in assets.values():
    b = bn.get(a['brand'])
    if b: a['tags'].update(re.findall(r'[a-z0-9]+', (b['name'] + ' ' + b.get('short', '') + ' ' + b['key']).lower()))
    a['tags'] = sorted(a['tags'])
    for f in a['files']:
        f.setdefault('url', URL + f['file'] if f.get('file') else f.get('url'))
    cards.append(a)
order = {s[0]: i for i, s in enumerate(SECTIONS)}
cards.sort(key=lambda a: (order[a['section']], a.get('order', 0)))
K['sections'] = [dict(id=i, title=t, help=h) for i, t, h in SECTIONS]
K['cards'] = cards
K['items'] = [f for a in cards for f in a['files'] if f.get('file')]   # every file stored in the kit (splashes live on their sites)
K['splashes'] = len(splashes)
json.dump(K, open(os.path.join(OUT, 'brandkit.json'), 'w'), indent=1)
print('cards', len(cards), 'files', len(K['items']), 'kit %.1f MB' % (sum(f['size'] for f in K['items']) / 1e6))
