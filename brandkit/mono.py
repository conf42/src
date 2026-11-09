import sys, os, subprocess, numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__))
from masters import LOGOS
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
def mask_of(im, mode):
    a = np.asarray(im.convert('RGBA')).astype(np.float32)
    alpha = a[..., 3] / 255
    if mode == 'alpha':
        ink = alpha > .5
    else:   # opaque and not near-white: white details stay holes
        lum = (.2126 * a[..., 0] + .7152 * a[..., 1] + .0722 * a[..., 2]) / 255
        ink = (alpha > .5) & (lum < .82)
    return ink
for key, m in LOGOS.items():
    if not m['mono']: continue
    im = Image.open(m['src'])
    ink = mask_of(im, m['mono'])
    ys, xs = np.where(ink); box = (xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)
    ink = ink[box[1]:box[3], box[0]:box[2]]
    # trace at a size where potrace keeps detail: longest side 3000
    h, w = ink.shape; k = 3000 / max(w, h)
    bm = Image.fromarray(((~ink) * 255).astype(np.uint8)).resize((round(w * k), round(h * k)), Image.LANCZOS).point(lambda v: 255 if v > 127 else 0).convert('1')
    pbm = os.path.join(OUT, key + '.pbm'); bm.save(pbm)
    svg = os.path.join(OUT, key + '-black.svg')
    subprocess.run(['potrace', pbm, '-s', '-o', svg, '--turdsize', '8', '--alphamax', '1.0', '--opttolerance', '0.2', '-M', '0'], check=True)
    os.remove(pbm)
    png = os.path.join(OUT, key + '-black-preview.png')
    subprocess.run(['rsvg-convert', '-w', '600', svg, '-o', png], check=True)
    print(key, im.size, '->', bm.size)
