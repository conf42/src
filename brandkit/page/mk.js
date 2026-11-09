(function () {
  var ROOT = document.getElementById('mk'), C = window.MK || {}, MAIN = C.main || 'btn btn-primary', ALT = C.alt || 'btn btn-outline-secondary', ITEM = C.item || 'lg-glass';
  var KIT = ROOT.dataset.kit, HOME = new URLSearchParams(location.search).get('home') || ROOT.dataset.home || '';
  var data, brand = HOME || 'all', BY = {};
  function el(t, cls, html) { var e = document.createElement(t); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function mb(n) { return n > 1e6 ? (n / 1e6).toFixed(1) + ' MB' : Math.max(1, Math.round(n / 1e3)) + ' KB'; }
  function toast(t) { var x = document.getElementById('toast'); x.textContent = t; x.classList.add('on'); clearTimeout(toast.t); toast.t = setTimeout(function () { x.classList.remove('on'); }, 1500); }
  function src(f) { return f.file ? KIT + f.file : f.url; }               // the kit's own files from here; splashes from their sites
  function save(url, name) { return fetch(url).then(function (r) { return r.blob(); }).then(function (b) { var a = document.createElement('a'), u = URL.createObjectURL(b); a.href = u; a.download = name; document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(u); }, 30000); }); }

  // ---- forgiving search: synonyms, plurals, prefixes and small typos; every word must match, else the best partial matches
  var SYN = { gif: 'animation', gifs: 'animation', animated: 'animation', moving: 'animation', loop: 'animation', clip: 'animation', color: 'colour', colors: 'colour', colours: 'colour', colour: 'colour', pic: 'picture', pics: 'picture', photo: 'picture', image: 'picture', pfp: 'avatar', twitter: 'x', tweet: 'x',
              fb: 'facebook', yt: 'youtube', vector: 'svg', scalable: 'svg', bg: 'background', backdrop: 'background', wallpaper: 'background', poster: 'splash', art: 'artwork',
              icon: 'icon', animal: 'animal', pet: 'pet', dark: 'dark', light: 'light', reversed: 'white', inverted: 'white', mono: 'mono', grey: 'mono', gray: 'mono', hex: 'hex', zoom: 'zoom' };
  var STOP = { a: 1, an: 1, the: 1, for: 1, of: 1, with: 1, and: 1, me: 1, i: 1, want: 1, need: 1, please: 1, download: 1, file: 1, files: 1, get: 1, my: 1, our: 1, some: 1, to: 1, in: 1, on: 1, version: 1 };
  function norm(w) { w = SYN[w] || w; if (w.length > 4 && /ies$/.test(w)) w = w.slice(0, -3) + 'y'; else if (w.length > 3 && /[^s]s$/.test(w)) w = w.slice(0, -1); return SYN[w] || w; }
  function dist(a, b) {
    if (Math.abs(a.length - b.length) > 2) return 9; var p = [], i, j;
    for (j = 0; j <= b.length; j++) p[j] = j;
    for (i = 1; i <= a.length; i++) { var prev = p[0]; p[0] = i; for (j = 1; j <= b.length; j++) { var t = p[j]; p[j] = Math.min(p[j] + 1, p[j - 1] + 1, prev + (a[i - 1] === b[j - 1] ? 0 : 1)); prev = t; } }
    return p[b.length];
  }
  function hit(word, tags) {
    for (var i = 0; i < tags.length; i++) {
      var t = tags[i]; if (t === word || norm(t) === word) return 2;
      if (word.length >= 2 && t.indexOf(word) === 0) return 1.5;
      if (word.length >= 3 && Math.abs(t.length - word.length) <= 1 && dist(word, t) <= (word.length >= 8 ? 2 : 1)) return 1;
      if (word.length >= 6 && dist(word, t) <= 2) return .8;
    }
    return 0;
  }
  function query() { return document.getElementById('q').value.toLowerCase().replace(/[^a-z0-9#]+/g, ' ').split(' ').filter(function (w) { return w && !STOP[w]; }).map(norm); }
  function score(card, words) { var s = 0, all = true; words.forEach(function (w) { var h = hit(w, card.tagsN); s += h; if (!h) all = false; }); return { s: s, all: all }; }

  // ---- ZIP (store) -------------------------------------------------------------------------------------------------
  var CRC = (function () { var t = new Uint32Array(256); for (var n = 0; n < 256; n++) { var c = n; for (var k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1; t[n] = c >>> 0; } return t; })();
  function crc32(b) { var c = 0xffffffff; for (var i = 0; i < b.length; i++) c = CRC[(c ^ b[i]) & 255] ^ (c >>> 8); return (c ^ 0xffffffff) >>> 0; }
  function zip(files) {
    var enc = new TextEncoder(), parts = [], central = [], off = 0;
    files.forEach(function (f) {
      var name = enc.encode(f.name), crc = crc32(f.bytes), h = new DataView(new ArrayBuffer(30));
      h.setUint32(0, 0x04034b50, true); h.setUint16(4, 20, true); h.setUint32(14, crc, true); h.setUint32(18, f.bytes.length, true); h.setUint32(22, f.bytes.length, true); h.setUint16(26, name.length, true);
      parts.push(h, name, f.bytes);
      var c = new DataView(new ArrayBuffer(46));
      c.setUint32(0, 0x02014b50, true); c.setUint16(4, 20, true); c.setUint16(6, 20, true); c.setUint32(16, crc, true); c.setUint32(20, f.bytes.length, true); c.setUint32(24, f.bytes.length, true); c.setUint16(28, name.length, true); c.setUint32(42, off, true);
      central.push(c, name); off += 30 + name.length + f.bytes.length;
    });
    var cs = central.reduce(function (s, p) { return s + p.byteLength; }, 0), e = new DataView(new ArrayBuffer(22));
    e.setUint32(0, 0x06054b50, true); e.setUint16(8, files.length, true); e.setUint16(10, files.length, true); e.setUint32(12, cs, true); e.setUint32(16, off, true);
    return new Blob(parts.concat(central, [e]), { type: 'application/zip' });
  }
  function zipBtn(files, name, text, cls) {
    var size = files.reduce(function (s, f) { return s + (f.size || 0); }, 0), b = el('button', (cls === 'ghost' ? ALT + ' btn-sm' : MAIN) + ' mk-zip', esc(text) + ' <small>' + mb(size) + '</small>');
    b.type = 'button';
    b.addEventListener('click', function () {
      if (b.getAttribute('aria-disabled')) return; var label = b.innerHTML, done = 0; b.setAttribute('aria-disabled', 'true');
      Promise.all(files.map(function (f) {
        return fetch(src(f)).then(function (r) { return r.arrayBuffer(); }).then(function (x) { b.textContent = 'Packing ' + (++done) + ' / ' + files.length; return { name: f.file || ('splashes/' + f.url.split('/').pop()), bytes: new Uint8Array(x) }; });
      })).then(function (fs) { var a = document.createElement('a'), u = URL.createObjectURL(zip(fs)); a.href = u; a.download = name; document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(u); }, 60000); })
        .catch(function () { toast('Download failed - try again'); }).then(function () { b.innerHTML = label; b.removeAttribute('aria-disabled'); });
    });
    return b;
  }

  // ---- a splash's SVG is traced in the browser on click (ImageTracer.js, public domain): nothing extra stored ------------
  var tracer = null;
  function traceSvg(url, name, btn) {
    btn.textContent = 'Tracing...'; btn.setAttribute('aria-disabled', 'true');
    tracer = tracer || new Promise(function (ok, fail) { var s = document.createElement('script'); s.src = 'https://cdn.jsdelivr.net/npm/imagetracerjs@1.2.6/imagetracer_v1.2.6.js'; s.onload = function () { ok(window.ImageTracer); }; s.onerror = fail; document.head.appendChild(s); });
    tracer.then(function (T) {
      return new Promise(function (ok) {
        var img = new Image(); img.crossOrigin = 'anonymous';
        img.onload = function () {
          var w = Math.min(1200, img.naturalWidth), h = Math.round(img.naturalHeight * w / img.naturalWidth), c = document.createElement('canvas'); c.width = w; c.height = h;
          var x = c.getContext('2d'); x.drawImage(img, 0, 0, w, h);
          ok(T.imagedataToSVG(x.getImageData(0, 0, w, h), { numberofcolors: 48, pathomit: 6, ltres: 1, qtres: 1, blurradius: 1, roundcoords: 1, viewbox: true }));
        };
        img.src = url;
      });
    }).then(function (svg) {
      var a = document.createElement('a'), u = URL.createObjectURL(new Blob([svg], { type: 'image/svg+xml' })); a.href = u; a.download = name; document.body.appendChild(a); a.click(); a.remove(); setTimeout(function () { URL.revokeObjectURL(u); }, 30000);
    }).catch(function () { toast('Could not trace this one'); }).then(function () { btn.textContent = 'SVG'; btn.removeAttribute('aria-disabled'); });
  }

  // ---- cards -----------------------------------------------------------------------------------------------------------
  var FMT = ['png', 'svg', 'jpg', 'jpeg', 'webp', 'pdf', 'eps', 'json', 'css', 'gpl', 'txt'];
  function card(c) {
    var d = el('div', 'mk-item ' + ITEM); d.dataset.id = c.id;
    var byF = {}; c.files.forEach(function (f) { byF[f.fmt] = byF[f.fmt] || f; });
    var show = byF.png || byF.jpg || byF.jpeg || byF.webp || byF.svg || c.files[0];
    var pv = el('div', 'pv' + (c.dark ? ' dark' : '') + (c.section === 'banners' || c.section === 'splashes' ? ' full' : '') + (c.section === 'illustrations' ? ' fit' : '') + (c.alpha ? ' alpha' : ''));
    if (/^(png|jpe?g|webp|svg)$/.test(show.fmt)) { var i = el('img'); i.loading = 'lazy'; i.alt = c.title; i.src = show.preview || src(show); pv.appendChild(i); }
    else pv.innerHTML = '<b style="font-size:1.5rem;color:#9a9ca8">.' + show.fmt + '</b>';
    d.appendChild(pv);
    d.appendChild(el('div', 't', esc(c.title)));
    var px = (byF.png || byF.jpg || byF.jpeg || {}).px; d.appendChild(el('div', 's', (px ? px.replace('x', ' × ') + ' px' : '') + (c.section === 'splashes' ? '' : '')));
    var row = el('div', 'dl');
    var rast = byF.png || byF.jpg || byF.jpeg || (byF.mp4 ? null : byF.webp);
    if (rast) { var b1 = el('button', MAIN + ' btn-sm mk-big', rast.fmt === 'png' ? 'PNG' : rast.fmt.toUpperCase()); b1.type = 'button'; b1.title = mb(rast.size); b1.addEventListener('click', function () { save(src(rast), (rast.file || rast.url).split('/').pop()); }); row.appendChild(b1); }
    if (byF.svg) { var b2 = el('button', ALT + ' btn-sm mk-big', 'SVG'); b2.type = 'button'; b2.title = mb(byF.svg.size) + (byF.svg.traced ? ' · traced vector' : ''); b2.addEventListener('click', function () { save(src(byF.svg), byF.svg.file.split('/').pop()); }); row.appendChild(b2); }
    else if (c.browser_svg) { var b3 = el('button', ALT + ' btn-sm mk-big', 'SVG'); b3.type = 'button'; b3.title = 'Traced into a vector in your browser'; b3.addEventListener('click', function () { traceSvg(rast.preview && rast.url ? rast.url : src(rast), rast.url.split('/').pop().replace(/\.\w+$/, '.svg'), b3); }); row.appendChild(b3); }
    var lone = !rast && !byF.svg && !byF.mp4 ? c.files[0].fmt : '';   // a file card's one format is the big button, not a link too
    ['pdf', 'eps', 'json', 'css', 'gpl', 'txt'].forEach(function (k) { if (byF[k] && k !== lone) { var a = el('a', 'more', k); a.href = src(byF[k]); a.download = byF[k].file.split('/').pop(); a.title = mb(byF[k].size); row.appendChild(a); } });
    if (byF.mp4) { row.innerHTML = ''; [byF.webp, byF.mp4].forEach(function (f, i) { if (!f) return; var b = el('button', (i ? ALT : MAIN) + ' btn-sm mk-big', f.fmt === 'webp' ? 'WebP' : 'MP4'); b.type = 'button'; b.title = mb(f.size); b.addEventListener('click', function () { save(src(f), f.file.split('/').pop()); }); row.appendChild(b); }); }
    if (!rast && !byF.svg && !byF.mp4) { var first = c.files[0], b4 = el('button', MAIN + ' btn-sm mk-big', first.fmt.toUpperCase()); b4.type = 'button'; b4.addEventListener('click', function () { save(src(first), first.file.split('/').pop()); }); row.appendChild(b4); }
    var lk = el('a', 'more lk', 'link'); lk.href = '#'; lk.title = 'Copy the link (for docs, scripts and AI agents)';
    lk.addEventListener('click', function (e) { e.preventDefault(); navigator.clipboard.writeText(show.url || new URL(src(show), location.href).href); toast('Link copied'); });
    row.appendChild(lk); d.appendChild(row);
    return d;
  }
  function swatches(b) {
    var box = el('div', 'swatches');
    b.palette.forEach(function (p) {
      var x = el('div', 'sw ' + ITEM), rgb = 'rgb(' + p.rgb.join(', ') + ')', cm = 'cmyk(' + p.cmyk.join('%, ') + '%)', v = 'var(--' + b.key + '-' + p.name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') + ')';
      x.dataset.tags = 'colour color palette hex ' + p.name.toLowerCase() + ' ' + p.hex.slice(1) + ' ' + (p.used || '').toLowerCase();
      x.innerHTML = '<div class="c" title="Click to copy ' + p.hex.toUpperCase() + '" style="background:' + p.hex + (p.hex === '#ffffff' ? ';border-bottom:1px solid #eee' : '') + '"><span>' + p.hex.toUpperCase() + '</span></div><div class="t"><b>' + esc(p.name) + '</b>' + (p.used ? '<span class="u">' + esc(p.used) + '</span>' : '') +
        '<code>' + rgb + '</code><button class="copy" type="button" data-v="' + rgb + '">copy</button><br><code>' + cm + '</code><button class="copy" type="button" data-v="' + cm + '">copy</button><br><code>' + v + '</code><button class="copy" type="button" data-v="' + v + '">copy</button></div>';
      x.querySelector('.c').addEventListener('click', function () { navigator.clipboard.writeText(p.hex.toUpperCase()); toast(p.hex.toUpperCase() + ' copied'); });
      x.querySelectorAll('.copy').forEach(function (k) { k.addEventListener('click', function () { navigator.clipboard.writeText(k.dataset.v); toast(k.dataset.v + ' copied'); }); });
      box.appendChild(x);
    });
    return box;
  }

  // ---- page --------------------------------------------------------------------------------------------------------------
  function render() {
    var out = document.getElementById('out'); out.innerHTML = '';
    var words = query(), searching = words.length > 0, list = data.brands.filter(function (b) { return brand === 'all' || b.key === brand; }), shown = 0, navSecs = {};
    var matched = {};
    if (searching) {
      var sc = data.cards.map(function (c) { return { c: c, r: score(c, words) }; });
      var exact = sc.filter(function (x) { return x.r.all; });
      var best = Math.max.apply(null, sc.map(function (x) { return x.r.s; }));
      (exact.length ? exact : sc.filter(function (x) { return best > 0 && x.r.s >= best * .99; })).forEach(function (x) { matched[x.c.id + '|' + x.c.brand] = x.r.s; });
    }
    function keep(c) { return !searching || matched[c.id + '|' + c.brand] != null; }
    list.forEach(function (b) {
      var cards = data.cards.filter(function (c) { return c.brand === b.key && c.section !== 'splashes' && keep(c); });
      var colourHit = !searching || score({ tagsN: ['colour', 'color', 'palette', 'hex', 'rgb', 'cmyk', 'swatch', 'code'].concat(BY[b.key].tagsN) }, words).all;
      if (!cards.length && !colourHit) return;
      var blk = el('section', 'brand'); blk.id = 'b-' + b.key;
      var head = el('div', 'bhead ' + ITEM), av = data.cards.filter(function (c) { return c.brand === b.key && c.section === 'stickers'; })[0];
      head.style.setProperty('--tint', b.color);   // a wash of the brand's main colour on the glass, never a flat block
      head.innerHTML = (av ? '<img src="' + src(av.files[0]) + '" alt="">' : '') + '<div><h2>' + esc(b.name) + '</h2><div class="meta">' + esc(b.spelling) + ' · <a href="' + esc(b.site) + '" target="_blank" rel="noopener">' + esc(b.site.replace(/^https?:\/\//, '').replace(/\/$/, '')) + '</a></div></div><div class="sp"></div>';
      head.appendChild(zipBtn(data.items.filter(function (f) { return f.brand === b.key; }), b.key + '-mediakit.zip', 'Everything for ' + (b.short || b.name)));
      blk.appendChild(head);
      data.sections.forEach(function (s) {
        if (s.id === 'splashes') return;
        var cs = cards.filter(function (c) { return c.section === s.id; });
        if (s.id === 'colours') { if (!colourHit && !cs.length) return; }
        else if (s.id === 'about') { if (!cs.length) return; }
        else if (!cs.length) return;
        var sec = el('div', 'sec'); sec.id = 's-' + b.key + '-' + s.id; navSecs[s.id] = navSecs[s.id] || sec.id;
        var sh = el('div', 'sh', '<h3>' + esc(s.title) + '</h3><span class="n"></span><span class="sp"></span>');
        var files = [].concat.apply([], cs.map(function (c) { return c.files.filter(function (f) { return f.file; }); }));
        if (files.length > 1) sh.appendChild(zipBtn(files, b.key + '-' + s.id + '.zip', 'Download all', 'ghost'));
        sec.appendChild(sh); sec.appendChild(el('p', 'help', esc(s.help)));
        if (s.id === 'colours') { sec.appendChild(swatches(b)); var g0 = el('div', 'grid'); g0.style.marginTop = '14px'; cs.forEach(function (c) { g0.appendChild(card(c)); }); sec.appendChild(g0); }
        else if (s.id === 'about') { var ab = el('div', 'about ' + ITEM, '<p>' + esc(b.about) + '</p>'); var cp = el('button', MAIN + ' btn-sm', 'Copy'); cp.type = 'button'; cp.addEventListener('click', function () { navigator.clipboard.writeText(b.about); toast('Copied'); }); ab.appendChild(cp); sec.appendChild(ab); }
        else { var g = el('div', 'grid' + (s.id === 'banners' ? ' wide' : '') + (s.id === 'animations' ? ' anim' : '')); cs.forEach(function (c) { g.appendChild(card(c)); }); sec.appendChild(g); }
        sh.querySelector('.n').textContent = s.id === 'about' ? '' : (cs.length + (cs.length === 1 ? ' item' : ' items'));
        shown += cs.length + (s.id === 'colours' ? 1 : 0); blk.appendChild(sec);
      });
      out.appendChild(blk);
    });
    // event splashes: every conference, first row, then "show all"
    var sp = data.cards.filter(function (c) { return c.section === 'splashes' && (brand === 'all' || c.brand === brand) && keep(c); });
    if (sp.length) {
      var s = data.sections.filter(function (x) { return x.id === 'splashes'; })[0], sec = el('div', 'sec'); sec.id = 's-splashes'; navSecs.splashes = sec.id;
      sec.appendChild(el('div', 'sh', '<h3>' + s.title + '</h3><span class="n">' + sp.length + ' conferences</span>'));
      sec.appendChild(el('p', 'help', esc(s.help) + ' Click SVG to get a vector version (made in your browser).'));
      var g = el('div', 'grid wide' + (sp.length > 4 && !searching ? ' clip' : '')); sp.forEach(function (c) { g.appendChild(card(c)); }); sec.appendChild(g);
      if (sp.length > 4 && !searching) { var more = el('button', ALT + ' showmore', 'Show all ' + sp.length + ' event splashes'); more.type = 'button'; more.addEventListener('click', function () { g.classList.remove('clip'); more.remove(); }); sec.appendChild(more); }
      out.appendChild(sec); shown += sp.length;
    }
    document.getElementById('none').hidden = shown > 0;
    var nav = document.getElementById('nav'); nav.innerHTML = '';
    data.sections.forEach(function (s) { if (navSecs[s.id]) { var a = el('a', '', esc(s.title)); a.href = '#' + navSecs[s.id]; nav.appendChild(a); } });
    nav.appendChild(el('span', 'sp'));
    nav.appendChild(zipBtn(data.items.filter(function (f) { return brand === 'all' || f.brand === brand; }), (brand === 'all' ? 'all-brands' : brand) + '-mediakit.zip', brand === 'all' ? 'Download everything' : 'Download everything for ' + (BY[brand].short || BY[brand].name)));
  }

  fetch(KIT + 'brandkit.json', { cache: 'no-cache' }).then(function (r) { return r.json(); }).then(function (d) {
    data = d;
    d.brands.forEach(function (b) { BY[b.key] = b; b.tagsN = (b.name + ' ' + (b.short || '') + ' ' + b.key).toLowerCase().split(/[^a-z0-9]+/).filter(Boolean); });
    d.cards.forEach(function (c) { c.tagsN = c.tags.concat(c.title.toLowerCase().split(/[^a-z0-9]+/)).filter(Boolean); });
    if (brand !== 'all' && !BY[brand]) brand = 'all';
    function stickerOf(k) { var c = d.cards.filter(function (c) { return c.brand === k && c.section === 'stickers'; })[0]; return c && (c.files.filter(function (f) { return f.fmt === 'png'; })[0] || c.files[0]); }
    var box = document.getElementById('brands'), order = [{ key: 'all', name: 'All brands' }].concat(d.brands.slice().sort(function (a, b) { return (b.key === HOME) - (a.key === HOME); }));
    order.forEach(function (b) {
      var t = el('button', 'bt ' + ITEM); t.type = 'button'; t.setAttribute('aria-pressed', b.key === brand);
      var av = b.key === 'all' ? null : d.cards.filter(function (c) { return c.brand === b.key && c.section === 'stickers'; })[0];
      t.innerHTML = (av ? '<img src="' + src(av.files.filter(function (f) { return f.fmt === 'png'; })[0] || av.files[0]) + '" alt="">' : '<span class="all">' + d.brands.slice(0, 4).map(function (x) { var s = stickerOf(x.key); return s ? '<img src="' + src(s) + '" alt="">' : ''; }).join('') + '</span>') + esc(b.short || b.name);
      t.addEventListener('click', function () { brand = b.key; box.querySelectorAll('.bt').forEach(function (x) { x.setAttribute('aria-pressed', x === t); }); render(); });
      box.appendChild(t);
    });
    var U = d.base, home = brand !== 'all' ? brand : 'sreday', CMDS = { json: U + 'brandkit.json', md: U + 'brandkit.md', llms: U + 'llms.txt', one: 'curl -O ' + U + home + '/logos/' + home + '-logo-white.svg',
      brand: "curl -s " + U + "brandkit.json | jq -r '.items[] | select(.brand==\"" + home + "\") | .url' | xargs -n1 curl -sO",
      white: "curl -s " + U + "brandkit.json | jq -r '.items[] | select(.variant==\"white\" and .fmt==\"svg\") | .url' | xargs -n1 curl -sO",
      colors: "curl -s " + U + "brandkit.json | jq '.brands[] | {(.key): [.palette[] | {(.name): .hex}] | add}'" };
    document.querySelectorAll('.cmd').forEach(function (c) { var code = c.querySelector('code'); code.textContent = CMDS[code.dataset.k]; c.querySelector('.copy').addEventListener('click', function () { navigator.clipboard.writeText(code.textContent); toast('Copied'); }); });
    var q0 = new URLSearchParams(location.search).get('q'); if (q0) document.getElementById('q').value = q0;   // shareable searches: /mediakit/?q=white+logo
    render();
  });
  function top() { var h = document.querySelector('header.fixed-top, nav.fixed-top'); if (h) ROOT.style.setProperty('--mk-top', h.offsetHeight + 'px'); }   // sticky section bar sits under the site's fixed header
  top(); window.addEventListener('resize', top);
  var t0; document.getElementById('q').addEventListener('input', function () { clearTimeout(t0); t0 = setTimeout(render, 140); });
  document.querySelectorAll('.tries button').forEach(function (b) { b.addEventListener('click', function () { document.getElementById('q').value = b.textContent; render(); }); });
})();
