// conf42.com/record (Marek 2026-10-22): the recorder's engine, in a Web Worker so it keeps going at full speed when the
// speaker switches to another window for a demo (a hidden tab's own timers and animation frames are throttled).
// Every 1/60 s it draws the frame - the slide or the shared screen in the window, the camera(s) in the circle(s), the
// event's overlay on top - shows it on the page and, while recording, encodes it: WebCodecs H.264 1080p60 (VBR
// ~2.5 Mbit/s) + AAC 128k mono, muxed by mp4-muxer into a fragmented MP4 (every 2 s keyframe is a fragment, so a
// recording cut short by a crash still plays up to that point). The MP4 goes to two places at once: the file the
// speaker picked (written as it records, committed when it ends) and a copy in the browser's private storage (OPFS,
// written in place), which the page offers back as a download if the first one didn't make it.
// The picture follows the audio clock (samples counted), so the voice and the face never drift apart, even over 2 hours.
importScripts('vendor/mp4-muxer-5.1.3.min.js');

var W = 1920, H = 1080, FPS = 60, KEY_EVERY = 2 * FPS, VBITRATE = 2500000, MAX_US = 2 * 3600 * 1e6;
// the sound is what matters most (Marek 2026-10-22): the highest AAC bitrate the browser takes, mono
var ABITRATES = [320000, 256000, 192000, 128000];
var OPFS_MP4 = 'c42-recording.mp4', OPFS_META = 'c42-recording.json';

var cv = new OffscreenCanvas(W, H), x = cv.getContext('2d', { alpha: false });
var light = new OffscreenCanvas(32, 18), lx = light.getContext('2d', { willReadFrequently: true });
var geo = null, overlay = null, slide = null, source = 'slides', bg = '#111';
var frameNo = 0, previewEvery = 2, dx = null;
var rec = null;

function post(m, t) { self.postMessage(m, t || []); }

// a MediaStreamTrackProcessor's frames (sent over from the page): keep the newest, close the rest
function feed(readable, put) {
  var reader = readable.getReader(), live = { stop: function () { try { reader.cancel(); } catch (e) {} } };
  (function pump() {
    reader.read().then(function (r) {
      if (r.done) { put(null); return; }
      put(r.value); pump();
    }).catch(function () { put(null); });
  })();
  return live;
}
var cams = [{ feed: null, frame: null, zoom: 1 }, { feed: null, frame: null, zoom: 1 }], scr = { feed: null, frame: null };
function setFrame(slot) { return function (f) { if (slot.frame) slot.frame.close(); slot.frame = f; }; }

function cover(src, sw, sh, dx, dy, dw, dh, up, zoom) {
  // src scaled to fill dx,dy,dw,dh, cropped centred (up: a little nearer the top, where the face usually is); zoom > 1 crops in
  var s = Math.max(dw / sw, dh / sh) * (zoom || 1), cw = dw / s, ch = dh / s;
  x.drawImage(src, (sw - cw) / 2, (sh - ch) * (up ? .4 : .5), cw, ch, dx, dy, dw, dh);
}
function contain(src, sw, sh, r) {
  var s = Math.min(r[2] / sw, r[3] / sh), w = sw * s, h = sh * s;
  x.drawImage(src, r[0] + (r[2] - w) / 2, r[1] + (r[3] - h) / 2, w, h);
}

function draw() {
  x.fillStyle = bg; x.fillRect(0, 0, W, H);
  if (!geo) return;
  var r = geo.rect, f = scr.frame;
  x.save(); x.beginPath(); x.rect(r[0], r[1], r[2], r[3]); x.clip();
  if (source === 'screen' && f) contain(f, f.displayWidth, f.displayHeight, r);
  else if (source === 'slides' && slide) x.drawImage(slide, r[0] + (r[2] - slide.width) / 2, r[1] + (r[3] - slide.height) / 2);
  else if (source === 'none' && cams[0].frame) { var c = cams[0].frame; cover(c, c.displayWidth, c.displayHeight, r[0], r[1], r[2], r[3], true, cams[0].zoom); }   // no slides: the camera alone in the big window
  x.restore();
  geo.cams.forEach(function (g, i) {
    var c = cams[i].frame, d = 2 * g[2] + 6;
    if (!c) return;
    // clipped to the circle: the square around it reaches into the slides' window in co-talk (Marek 2026-10-23)
    x.save(); x.beginPath(); x.arc(g[0], g[1], d / 2, 0, 2 * Math.PI); x.clip();
    cover(c, c.displayWidth, c.displayHeight, g[0] - d / 2, g[1] - d / 2, d, d, true, cams[i].zoom);
    x.restore();
  });
  if (overlay) x.drawImage(overlay, 0, 0);
}

function brightness() {
  var sigs = [];
  cams.forEach(function (s, i) {
    if (!s.frame) return;
    lx.drawImage(s.frame, 0, 0, 32, 18);
    var p = lx.getImageData(0, 0, 32, 18).data, sum = 0, g = [];
    for (var k = 0; k < p.length; k += 4) { var l = .2126 * p[k] + .7152 * p[k + 1] + .0722 * p[k + 2]; g.push(l); sum += l; }
    sigs[i] = g;
    post({ type: 'light', slot: i, luma: sum / (p.length / 4) });
  });
  // the two cameras alike? (the page suggests removing the 2nd when it's one person twice): the correlation of the
  // two 32 x 18 grey pictures, 1 = the same picture
  if (sigs[0] && sigs[1]) post({ type: 'alike', r: corr(sigs[0], sigs[1]) });
}
function corr(a, b) {
  var n = a.length, ma = 0, mb = 0, sab = 0, saa = 0, sbb = 0, i;
  for (i = 0; i < n; i++) { ma += a[i]; mb += b[i]; }
  ma /= n; mb /= n;
  for (i = 0; i < n; i++) { var da = a[i] - ma, db = b[i] - mb; sab += da * db; saa += da * da; sbb += db * db; }
  return saa && sbb ? sab / Math.sqrt(saa * sbb) : 0;   // a flat picture (a camera still starting) proves nothing
}

// the clock: the wall clock, gently pulled onto the audio clock (samples counted). Audio arrives in bursts, so the
// offset between the two is smoothed over a few seconds: the picture runs evenly and still never drifts from the voice
function now() { return rec && rec.w0 ? ((rec.paused || performance.now()) - rec.w0) * 1000 + rec.off : 0; }   // stands still while paused
function heard(us) {
  var w = performance.now();
  if (!rec.w0) { rec.w0 = w; rec.off = us; return; }
  var err = us - ((w - rec.w0) * 1000 + rec.off);
  rec.off += Math.max(-2000, Math.min(2000, err * .005));
}

function tick() {
  draw();
  if (rec && rec.muxer && !rec.stopping && !rec.paused) {
    // on the 60 fps grid: frame n at n/60 s of the clock. Each tick fills the next slot (the timer's jitter is
    // absorbed); only when the loop is more than 3 frames behind (a stalled machine) are the slots in between left out
    var at = now() * FPS / 1e6, n = rec.lastN + 1;
    if (at > n + 3) n = Math.round(at);
    if (at >= n - .5) {
      if (rec.venc.encodeQueueSize < 10) {
        var vf = new VideoFrame(cv, { timestamp: Math.round(n * 1e6 / FPS), duration: Math.round(1e6 / FPS) });
        rec.venc.encode(vf, { keyFrame: n - rec.lastKey >= KEY_EVERY || rec.lastKey < 0 });
        if (n - rec.lastKey >= KEY_EVERY || rec.lastKey < 0) rec.lastKey = n;
        vf.close(); rec.frames++;
        rec.dropped += Math.max(0, n - rec.lastN - 1);
      } else rec.dropped++;
      rec.lastN = n;
    }
    if (now() >= MAX_US) stop('limit');
  }
  // the page's preview: its canvas was handed over to this worker, so the page itself does nothing per frame (posting
  // frames to the page to draw froze Chrome next to a painted backdrop, 2026-10-22)
  if (frameNo % previewEvery === 0 && dx) dx.drawImage(cv, 0, 0, dx.canvas.width, dx.canvas.height);
  if (frameNo % FPS === 0) brightness();
  if (rec && frameNo % 15 === 0) post({ type: 'tick', us: now(), bytes: rec.bytes, dropped: rec.dropped });
  frameNo++;
}
var next = performance.now(), stat = { n: 0, busy: 0, at: performance.now() };
(function loop() {
  var t = performance.now();
  try { tick(); } catch (e) { post({ type: 'error', message: 'frame: ' + e.message }); }
  stat.n++; stat.busy += performance.now() - t;
  if (t - stat.at > 2000) { post({ type: 'stats', fps: stat.n * 1000 / (t - stat.at), busy: stat.busy / stat.n }); stat = { n: 0, busy: 0, at: t }; }
  next += 1000 / FPS;
  var wait = next - performance.now();
  if (wait < -50) { next = performance.now(); wait = 0; }   // fell far behind (a busy machine): skip ahead, don't burst
  setTimeout(loop, Math.max(0, wait));
})();

// ── recording ──
function pickVideo(bitrate) {
  var tries = [];
  ['avc1.640033', 'avc1.64002A', 'avc1.4D402A', 'avc1.42E02A'].forEach(function (codec) {   // High 5.1, High 4.2, Main 4.2, Baseline 4.2
    ['prefer-hardware', 'no-preference'].forEach(function (hw) {
      tries.push({ codec: codec, width: W, height: H, bitrate: bitrate || VBITRATE, framerate: FPS, bitrateMode: 'variable',
                   latencyMode: 'quality', hardwareAcceleration: hw, avc: { format: 'avc' } });
    });
  });
  return tries.reduce(function (p, c) {
    return p.then(function (found) { return found || VideoEncoder.isConfigSupported(c).then(function (s) { return s.supported ? c : null; }, function () { return null; }); });
  }, Promise.resolve(null));
}
function pickAudio(rate) {
  var tries = [];
  ['aac', 'opus'].forEach(function (k) {
    ABITRATES.forEach(function (b) { tries.push([{ codec: k === 'aac' ? 'mp4a.40.2' : 'opus', sampleRate: rate, numberOfChannels: 1, bitrate: b, bitrateMode: 'constant' }, k]); });
  });
  return tries.reduce(function (p, t) {
    return p.then(function (found) { return found || AudioEncoder.isConfigSupported(t[0]).then(function (s) { return s.supported ? t : null; }, function () { return null; }); });
  }, Promise.resolve(null));
}

function write(data, pos) {
  rec.bytes = Math.max(rec.bytes, pos + data.byteLength);
  if (rec.sync) { try { rec.sync.write(data, { at: pos }); } catch (e) { rec.syncErr = e.message; } }
  if (rec.desk && !rec.deskErr) {
    var copy = data.slice();
    rec.deskChain = rec.deskChain.then(function () { return rec.desk.write({ type: 'write', position: pos, data: copy }); })
      .catch(function (e) { if (!rec.deskErr) { rec.deskErr = e.message || String(e); post({ type: 'warn', what: 'disk', message: rec.deskErr }); } });
  }
}
function meta(extra) {
  if (!rec.metaH) return;
  var m = JSON.stringify(Object.assign({ name: rec.name, started: rec.started, seconds: Math.round(now() / 1e6), bytes: rec.bytes }, extra || {}));
  try { var b = new TextEncoder().encode(m); rec.metaH.truncate(0); rec.metaH.write(b, { at: 0 }); rec.metaH.flush(); } catch (e) {}
}

function mono(d) {
  // the AudioData again, mono, on our own timeline (samples counted from the start)
  var n = d.numberOfFrames, ch = d.numberOfChannels, out = new Float32Array(n), tmp = new Float32Array(n);
  for (var c = 0; c < ch; c++) {
    d.copyTo(tmp, { planeIndex: c, format: 'f32-planar' });
    for (var i = 0; i < n; i++) out[i] += tmp[i] / ch;
  }
  var a = new AudioData({ format: 'f32-planar', sampleRate: d.sampleRate, numberOfFrames: n, numberOfChannels: 1,
                          timestamp: Math.round(rec.samples * 1e6 / d.sampleRate), data: out });
  rec.samples += n;
  return a;
}

function start(m) {
  if (rec) return;
  rec = { name: m.name, started: new Date().toISOString(), frames: 0, dropped: 0, bytes: 0, lastN: -1, lastKey: -1, samples: 0,
          w0: 0, off: 0, deskChain: Promise.resolve(), desk: null, sync: null, metaH: null, muxer: null };
  var r = rec;
  var opfs = navigator.storage.getDirectory().then(function (dir) {
    r.dir = dir;
    return Promise.all([dir.getFileHandle(OPFS_MP4, { create: true }), dir.getFileHandle(OPFS_META, { create: true })]);
  }).then(function (h) { return Promise.all([h[0].createSyncAccessHandle(), h[1].createSyncAccessHandle()]); })
    .then(function (s) { r.sync = s[0]; r.sync.truncate(0); r.metaH = s[1]; }, function (e) { post({ type: 'warn', what: 'opfs', message: e.message }); });
  var desk = m.handle ? m.handle.createWritable().then(function (w) { r.desk = w; }, function (e) { r.deskErr = e.message; post({ type: 'warn', what: 'disk', message: e.message }); }) : Promise.resolve();
  Promise.all([opfs, desk, pickVideo(m.vbitrate)]).then(function (res) {
    var vcfg = res[2];
    if (!vcfg) throw new Error('This browser cannot encode H.264 video.');
    r.venc = new VideoEncoder({ output: function (chunk, md) { r.muxer.addVideoChunk(chunk, md); }, error: function (e) { post({ type: 'error', message: 'video: ' + e.message }); } });
    r.venc.configure(vcfg);
    r.vcodec = vcfg.codec;
    var first = true;
    r.audio = feed(m.audio, function (d) {
      if (!d) return;
      if (r.stopping) { d.close(); return; }
      if (first) {
        first = false;
        var rate = d.sampleRate;
        pickAudio(rate).then(function (ac) {
          if (!ac) throw new Error('This browser cannot encode the sound (AAC or Opus).');
          r.aenc = new AudioEncoder({ output: function (chunk, md) { r.muxer.addAudioChunk(chunk, md); }, error: function (e) { post({ type: 'error', message: 'audio: ' + e.message }); } });
          r.aenc.configure(ac[0]);
          r.muxer = new Mp4Muxer.Muxer({
            target: new Mp4Muxer.StreamTarget({ onData: write }),
            video: { codec: 'avc', width: W, height: H, frameRate: FPS },
            audio: { codec: ac[1], sampleRate: rate, numberOfChannels: 1 },
            fastStart: 'fragmented', firstTimestampBehavior: 'cross-track-offset'
          });
          r.acodec = ac[1];
          r.metaTimer = setInterval(function () { meta(); if (r.sync) try { r.sync.flush(); } catch (e) {} }, 5000);
          meta();
          post({ type: 'started', video: r.vcodec, audio: ac[1] + ' ' + Math.round(ac[0].bitrate / 1000) + 'k' });
        }).catch(function (e) { post({ type: 'error', message: e.message }); });
        d.close(); return;
      }
      if (!r.muxer || r.paused) { d.close(); return; }   // paused: the sound isn't counted, so the timeline just continues
      var a = mono(d), rate2 = d.sampleRate;
      d.close();
      heard(r.samples * 1e6 / rate2);
      r.aenc.encode(a); a.close();
    });
  }).catch(function (e) { post({ type: 'error', message: e.message }); rec = null; });
}

function stop(why) {
  var r = rec;
  if (!r || r.stopping) return;
  r.stopping = true;
  if (r.audio) r.audio.stop();
  clearInterval(r.metaTimer);
  post({ type: 'finishing' });
  var seconds = now() / 1e6;
  Promise.resolve().then(function () { return r.venc && r.venc.state === 'configured' ? r.venc.flush() : null; })
    .then(function () { return r.aenc && r.aenc.state === 'configured' ? r.aenc.flush() : null; })
    .then(function () { if (r.muxer) r.muxer.finalize(); return r.deskChain; })
    .then(function () { return r.desk && !r.deskErr ? r.desk.close().catch(function (e) { r.deskErr = e.message; }) : null; })
    .then(function () {
      var onDisk = !!r.desk && !r.deskErr;
      meta({ finished: true, seconds: Math.round(seconds), onDisk: onDisk });
      try { if (r.sync) { r.sync.flush(); r.sync.close(); } } catch (e) {}
      try { if (r.metaH) r.metaH.close(); } catch (e) {}
      var clean = onDisk && r.dir ? Promise.all([r.dir.removeEntry(OPFS_MP4), r.dir.removeEntry(OPFS_META)]).catch(function () {}) : Promise.resolve();
      return clean.then(function () {
        post({ type: 'done', why: why || 'stop', seconds: seconds, bytes: r.bytes, onDisk: onDisk, diskError: r.deskErr || '',
               inBrowser: !onDisk && !!r.sync && !r.syncErr, dropped: r.dropped, frames: r.frames, video: r.vcodec, audio: r.acodec });
      });
    })
    .catch(function (e) { post({ type: 'error', message: 'finishing: ' + e.message }); })
    .then(function () { rec = null; });
}

self.onmessage = function (e) {
  var m = e.data;
  if (m.type === 'display') dx = m.canvas.getContext('2d', { alpha: false });
  else if (m.type === 'layout') { geo = m.geo; bg = m.bg || bg; }
  else if (m.type === 'overlay') { if (overlay) overlay.close(); overlay = m.bitmap; }
  else if (m.type === 'slide') { if (slide) slide.close(); slide = m.bitmap; }
  else if (m.type === 'source') source = m.source;
  else if (m.type === 'zoom') cams[m.slot].zoom = m.zoom;
  else if (m.type === 'cam') {
    var s = cams[m.slot];
    if (s.feed) s.feed.stop();
    setFrame(s)(null);
    s.feed = m.readable ? feed(m.readable, setFrame(s)) : null;
  } else if (m.type === 'screen') {
    if (scr.feed) scr.feed.stop();
    setFrame(scr)(null);
    scr.feed = m.readable ? feed(m.readable, setFrame(scr)) : null;
  } else if (m.type === 'start') start(m);
  else if (m.type === 'stop') stop('stop');
  // pause / resume (Marek 2026-10-23): nothing is written while paused; on resume the clock is moved on by the pause, so
  // the file plays straight through, and the first picture after it is a keyframe (a clean cut for the editors)
  else if (m.type === 'pause' && rec && !rec.paused && rec.w0) rec.paused = performance.now();
  else if (m.type === 'resume' && rec && rec.paused) { rec.w0 += performance.now() - rec.paused; rec.paused = 0; rec.lastKey = -KEY_EVERY; }
};
