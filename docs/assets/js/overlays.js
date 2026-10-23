// The Conf42 recording overlays (Marek 2026-10-13), shared by conf42.com/<event>/teasers#overlays (the PNGs speakers
// used to put into OBS) and conf42.com/record (the in-browser recorder, 2026-10-22), so both draw the very same overlay.
// ovDrawNew(cv, kind, d, a) = the New design, ovDraw(cv, kind, d, logo) = the Legacy one; kind is 'default', 'co-talk'
// or 'no-facecam'; d = build/teasers.py overlays(); a = {planet, sticker} images (sticker through blend()).
function ovText(x, cx, base, size, parts, track, maxW) {
  // parts: strings and null (a round bullet), in tracked capitals centred on cx with the baseline at base; shrinks to maxW
  var sp, dot, gap, w, items;
  function lay() {
    x.font = '700 ' + size + 'px Lato';
    sp = size * track; dot = size * (size > 28 ? .48 : .44); gap = size * .62; w = 0; items = [];
    parts.forEach(function (p, k) {
      if (k) { items.push({ gap: gap }); w += gap; }
      if (p === null) { items.push({ dot: true }); w += dot; return; }
      for (var i = 0; i < p.length; i++) { var cw = x.measureText(p[i]).width; items.push({ ch: p[i], w: cw }); w += cw + (i < p.length - 1 ? sp : 0); }
    });
  }
  lay();
  if (w > maxW) { var was = size; size = size * maxW / w; base -= (was - size) * .36; lay(); }   // too long: smaller, on the same middle line
  var at = cx - w / 2;
  items.forEach(function (it, k) {
    if (it.gap) { at += it.gap; return; }
    if (it.dot) { x.beginPath(); x.arc(at + dot / 2, base - size * .32, dot / 2, 0, 7); x.fill(); at += dot; return; }
    x.fillText(it.ch, at, base);
    at += it.w + (items[k + 1] && items[k + 1].ch ? sp : 0);
  });
}
function ovDraw(cv, kind, d, logo) {
  cv.width = 1920; cv.height = 1080;
  var x = cv.getContext('2d'), band = 'rgba(255,255,255,.1)';
  x.clearRect(0, 0, 1920, 1080);
  x.fillStyle = d.color; x.fillRect(0, 0, 1920, 1080);
  function hole(f) { x.save(); x.globalCompositeOperation = 'destination-out'; x.fillStyle = '#000'; f(); x.restore(); }
  function ring(cx, cy, ro, ri) {         // the facecam: a transparent disc in a white ring
    x.fillStyle = '#fff'; x.beginPath(); x.arc(cx, cy, ro, 0, 7); x.fill();
    hole(function () { x.beginPath(); x.arc(cx, cy, ri, 0, 7); x.fill(); });
  }
  if (kind === 'default') {
    x.fillStyle = band; x.fillRect(188, 20, 1732, 156);
    hole(function () { x.fillRect(373.1, 203.75, 1532.9, 862.25); });
    ring(188, 188, 167.5, 159);
    x.fillStyle = '#fff';
    ovText(x, 1112.5, 79, 32, [d.title], .16, 1440);
    ovText(x, 1112.5, 141, 32, [d.date, null, 'ONLINE'], .16, 1440);
  } else if (kind === 'co-talk') {
    x.fillStyle = band; x.fillRect(214.5, 40, 1491, 197);
    hole(function () { x.fillRect(336.66, 360.95, 1246.68, 701.25); });
    ring(214.5, 214.5, 174, 164.3); ring(1705.5, 214.5, 174, 164.3);
    x.fillStyle = '#fff';
    ovText(x, 960, 118, 32, [d.title], .16, 1100);
    ovText(x, 960, 180, 32, [d.date, null, 'ONLINE'], .16, 1100);
  } else {
    x.fillStyle = band; x.beginPath(); x.moveTo(0, 0); x.lineTo(125.5, 0); x.lineTo(0, 148); x.closePath(); x.fill();
    hole(function () { x.fillRect(84.87, 47.74, 1750.26, 984.52); });
    if (logo) x.drawImage(logo, 13, 10, 59 * logo.naturalWidth / logo.naturalHeight, 59);   // the planet, white, as on the original
    x.fillStyle = '#fff';
    ovText(x, 960, 1066, 24, [d.title, null, d.date, null, 'ONLINE'], .19, 1700);
  }
}
// the New design (Marek 2026-10-13, round-2 option "a-frost"): the same holes, band and text, the flat parts turned
// into white frosted glass on soft pools of the event colour, the sticker (or the planet) bottom-left. Drawn as the
// headless-Chrome mock-up was (glass = the teaser cards' shard style); the pools are pre-blurred radial gradients
function ovDrawNew(cv, kind, d, a) {
  cv.width = 1920; cv.height = 1080;
  var x = cv.getContext('2d');
  x.clearRect(0, 0, 1920, 1080);
  x.fillStyle = d.color; x.fillRect(0, 0, 1920, 1080);
  [[-200, -300, 900, 700], [1200, 600, 900, 700], [1300, -250, 800, 500], [-250, 650, 700, 600]].forEach(function (p, k) {
    var c = d.pools[k], r = parseInt(c.slice(1, 3), 16), g = parseInt(c.slice(3, 5), 16), b = parseInt(c.slice(5, 7), 16);
    var rgb = function (al) { return 'rgba(' + r + ',' + g + ',' + b + ',' + al + ')'; };
    x.save(); x.translate(p[0] + p[2] / 2, p[1] + p[3] / 2); x.scale(p[2] / 2 + 260, p[3] / 2 + 260);
    var gr = x.createRadialGradient(0, 0, 0, 0, 0, 1);
    [[0, .8], [.3, .72], [.55, .45], [.75, .18], [1, 0]].forEach(function (s) { gr.addColorStop(s[0], rgb(s[1])); });
    x.fillStyle = gr; x.fillRect(-1, -1, 2, 2); x.restore();
  });
  function rr(X, Y, W, H, R) { x.beginPath(); if (x.roundRect) x.roundRect(X, Y, W, H, R); else x.rect(X, Y, W, H); }
  function oval(cx, cy, r) { x.beginPath(); x.arc(cx, cy, r, 0, 7); }
  function ell(X, Y, W, H, px, py, rx, ry, al, stop) {      // a CSS radial-gradient ellipse highlight, white al -> 0 at stop
    x.save(); x.translate(X + W * px, Y + H * py); x.scale(W * rx, H * ry);
    var gr = x.createRadialGradient(0, 0, 0, 0, 0, 1);
    gr.addColorStop(0, 'rgba(255,255,255,' + al + ')'); gr.addColorStop(stop, 'rgba(255,255,255,0)');
    x.fillStyle = gr; x.fillRect(-2, -2, 4, 4); x.restore();
  }
  function glass(path, X, Y, W, H, edge, tint) {
    // the gradient's two white alphas and the border's: the glass about 20% brighter than the base under it (Marek
    // 2026-10-13: the backdrop saturate/brightness boost and a .22 wash made it stand out far too much on strong colours)
    tint = tint || [.15, .09, .34];
    if (edge) {                                           // the drop shadow, outside the shard only
      x.save(); x.beginPath(); x.rect(0, 0, 1920, 1080); path(true); x.clip('evenodd');
      x.shadowColor = 'rgba(0,0,0,.28)'; x.shadowBlur = 60; x.shadowOffsetY = 24; x.fillStyle = '#000'; path(); x.fill(); x.restore();
    }
    x.save(); path(); x.clip();
    var t = 145 * Math.PI / 180, dx = Math.sin(t), dy = -Math.cos(t), L = Math.abs(W * dx) + Math.abs(H * dy) , cx = X + W / 2, cy = Y + H / 2;
    var gr = x.createLinearGradient(cx - dx * L / 2, cy - dy * L / 2, cx + dx * L / 2, cy + dy * L / 2);
    gr.addColorStop(0, 'rgba(255,255,255,' + tint[0] + ')'); gr.addColorStop(1, 'rgba(255,255,255,' + tint[1] + ')');
    x.fillStyle = gr; x.fillRect(X, Y, W, H);
    ell(X, Y, W, H, .12, -.08, 1.1, .55, .1, .55); ell(X, Y, W, H, 1, 1.12, .7, .4, .05, .6);
    if (edge) {
      x.fillStyle = 'rgba(255,255,255,.5)'; x.beginPath(); x.rect(X - 10, Y - 10, W + 20, H + 20); x.translate(0, 1.5); path(true); x.translate(0, -1.5); x.fill('evenodd');
      x.fillStyle = 'rgba(255,255,255,.12)'; x.beginPath(); x.rect(X - 10, Y - 10, W + 20, H + 20); x.translate(0, -1); path(true); x.translate(0, 1); x.fill('evenodd');
      x.strokeStyle = 'rgba(255,255,255,' + tint[2] + ')'; x.lineWidth = 3; path(); x.stroke();   // a 1.5 px border inside the shard
    }
    x.restore();
  }
  function sub(f) { return function (keep) { if (keep) { var b = x.beginPath; x.beginPath = function () {}; f(); x.beginPath = b; } else f(); }; }
  function shard(X, Y, W, H, R) { glass(sub(function () { rr(X, Y, W, H, R); }), X, Y, W, H, true); }
  function camRing(cx, cy, ri) { var r = ri + 16; glass(sub(function () { oval(cx, cy, r); }), cx - r, cy - r, 2 * r, 2 * r, true, [.78, .5, .9]); }   // white milky glass, untinted (Marek: "visibly white with translucent features")
  var holes = [];
  x.fillStyle = '#fff';
  function words() { x.shadowColor = 'rgba(0,0,0,.22)'; x.shadowBlur = 12; x.shadowOffsetY = 1; }
  if (kind === 'default') {
    shard(250, 20, 1650, 156, 34); camRing(188, 188, 159);
    holes = [['r', 373.1, 203.75, 1532.9, 862.25, 26], ['c', 188, 188, 159]];
    x.save(); x.fillStyle = '#fff'; words();
    ovText(x, 1112.5, 79, 32, [d.title], .16, 1440); ovText(x, 1112.5, 141, 32, [d.date, null, 'ONLINE'], .16, 1440); x.restore();
    if (a.sticker) x.drawImage(a.sticker, 34, 796, 304, 304 * a.sticker.naturalHeight / a.sticker.naturalWidth);
  } else if (kind === 'co-talk') {
    shard(290, 40, 1340, 197, 40); camRing(214.5, 214.5, 164.3); camRing(1705.5, 214.5, 164.3);
    holes = [['r', 336.66, 360.95, 1246.68, 701.25, 26], ['c', 214.5, 214.5, 164.3], ['c', 1705.5, 214.5, 164.3]];
    x.save(); x.fillStyle = '#fff'; words();
    ovText(x, 960, 118, 32, [d.title], .16, 1100); ovText(x, 960, 180, 32, [d.date, null, 'ONLINE'], .16, 1100); x.restore();
    if (a.sticker) x.drawImage(a.sticker, 26, 806, 290, 290 * a.sticker.naturalHeight / a.sticker.naturalWidth);
  } else {
    glass(sub(function () { x.beginPath(); x.moveTo(0, 932); x.lineTo(0, 1080); x.lineTo(125.5, 1080); x.closePath(); }), 0, 932, 125.5, 148, false);
    holes = [['r', 84.87, 47.74, 1750.26, 984.52, 24]];
    if (a.planet) x.drawImage(a.planet, 13, 1011, 59 * a.planet.naturalWidth / a.planet.naturalHeight, 59);
    x.save(); x.fillStyle = '#fff'; words();
    ovText(x, 960, 1066, 24, [d.title, null, d.date, null, 'ONLINE'], .19, 1700); x.restore();
  }
  x.save(); x.globalCompositeOperation = 'destination-out'; x.fillStyle = '#000';
  holes.forEach(function (h) { if (h[0] === 'r') rr(h[1], h[2], h[3], h[4], h[5]); else oval(h[1], h[2], h[3]); x.fill(); });
  x.restore();
  holes.forEach(function (h) {                            // a hairline just outside each camera hole; the slides' window has
    if (h[0] !== 'c') return;                             // no outline, just its rounded corners (Marek 2026-10-13: "too much")
    x.lineWidth = 2; x.strokeStyle = 'rgba(255,255,255,.6)'; oval(h[1], h[2], h[3] + 1); x.stroke();
  });
}
function blend(im) {
  // the sticker's dark parts (its navy outline and sky) a bit see-through, so it sits in the event colour; the white
  // lettering and the bright illustration stay solid (Marek 2026-10-13, an exception to drawing logos as they are)
  var c = document.createElement('canvas'), x = c.getContext('2d');
  c.width = im.naturalWidth; c.height = im.naturalHeight; x.drawImage(im, 0, 0);
  try {
    var d = x.getImageData(0, 0, c.width, c.height), p = d.data;
    for (var i = 0; i < p.length; i += 4) {
      var l = (.2126 * p[i] + .7152 * p[i + 1] + .0722 * p[i + 2]) / 255, t = Math.min(1, Math.max(0, (l - .18) / .3));
      p[i + 3] *= .5 + .5 * t * t * (3 - 2 * t);
    }
    x.putImageData(d, 0, 0);
  } catch (e) { return im; }
  c.naturalWidth = c.width; c.naturalHeight = c.height;
  return c;
}
