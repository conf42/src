// conf42.com/record (Marek 2026-10-31): the recorder's helper for decks the page can't open on its own.
//   GET  ?id=<Google Slides id>&f=pdf|pptx   a Google Slides deck as PDF or .pptx (the notes)
//   GET  ?url=<link>                         a deck file shared by link: Google Drive, OneDrive, Dropbox. A PDF comes back
//                                            as it is; a PowerPoint (.pptx/.ppt) or .odp comes back as PDF + .pptx
//   POST ?f=convert&name=<file name>         body: the file, base64. A PowerPoint / .odp the speaker picked -> PDF
//                                            (+ .pptx for the notes from a .ppt / .odp)
// A page can't fetch these itself: Google's and the others' download links don't allow other sites. Links are fetched
// anonymously (no token), so only files shared "Anyone with the link" come out. Conversion goes through Google Slides:
// the file is put in this account's Drive for a few seconds and deleted. The drive.file scope (appsscript.json) means
// this script only ever sees the files it created itself - never anything else in the account.
//
// Lives in mark@sreday.com (project "conf42 record - Slides link"), never the personal gmail.
// Deploy once: script.google.com -> New project -> paste this file (and appsscript.json: Project Settings -> Show
// "appsscript.json" manifest file in editor) -> Deploy -> New deployment -> Web app, Execute as: Me, Who has access:
// Anyone -> Deploy -> copy the ".../exec" URL into SLIDES_LINK in _templates/record.html. A changed script needs
// Deploy -> Manage deployments -> edit -> New version (same URL); new scopes ask for authorization once, in the editor
// (Run -> selftest).

var MAX = 36 * 1024 * 1024;   // a file's bytes: base64 makes it a third bigger, and an answer stays under ~50 MB
var KINDS = { pdf: 'application/pdf', pptx: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
              ppt: 'application/vnd.ms-powerpoint', odp: 'application/vnd.oasis.opendocument.presentation' };

function doGet(e) {
  try {
    if (e.parameter.url) return out(fromLink(String(e.parameter.url)));
    var id = String(e.parameter.id || ''), f = e.parameter.f === 'pptx' ? 'pptx' : 'pdf';
    if (!/^[\w-]{20,100}$/.test(id)) return out({ error: 'bad link' });
    var r = fetchFile('https://docs.google.com/presentation/d/' + id + '/export/' + f);
    if (r.error) return out(r);
    return out({ name: r.name || 'slides.' + f, data: Utilities.base64Encode(r.bytes) });
  } catch (x) { return out({ error: String(x.message || x).slice(0, 200) }); }
}

function doPost(e) {
  try {
    var name = String(e.parameter.name || 'slides.pptx'), kind = kindOf(name, '');
    if (e.parameter.f !== 'convert' || !kind || kind === 'pdf') return out({ error: 'unsupported' });
    var bytes = Utilities.base64Decode(e.postData.contents);
    if (bytes.length > MAX) return out({ error: 'too big' });
    return out(converted(bytes, name, kind, false));   // the page has its own .pptx
  } catch (x) { return out({ error: String(x.message || x).slice(0, 200) }); }
}

// a share link -> its direct download (only these hosts: nothing else is ever fetched)
function fromLink(u) {
  var m, dl;
  if ((m = /^https:\/\/(?:drive|docs)\.google\.com\/(?:file\/d\/|open\?id=|uc\?(?:[^#]*&)?id=)([\w-]{20,})/.exec(u)))
    dl = 'https://drive.usercontent.google.com/download?id=' + m[1] + '&export=download&confirm=t';
  else if (/^https:\/\/(?:www\.)?dropbox\.com\/(?:s|scl)\//.test(u))
    dl = /[?&]dl=0/.test(u) ? u.replace(/([?&])dl=0/, '$1dl=1') : u + (u.indexOf('?') < 0 ? '?' : '&') + 'dl=1';
  else if (/^https:\/\/(?:1drv\.ms|onedrive\.live\.com)\//.test(u))
    dl = 'https://api.onedrive.com/v1.0/shares/u!' + Utilities.base64EncodeWebSafe(u).replace(/=+$/, '') + '/root/content';
  else return { error: 'unsupported link' };
  var r = fetchFile(dl);
  if (r.error) return r;
  var kind = kindOf(r.name, r.type);
  if (kind === 'key') return { error: 'keynote' };
  if (!kind) return { error: 'not a deck' };
  if (kind === 'pdf') return { files: [{ name: r.name || 'slides.pdf', data: Utilities.base64Encode(r.bytes) }] };
  return converted(r.bytes, r.name || 'slides.' + kind, kind, true);
}

// a PowerPoint / .odp -> Google Slides (for seconds) -> PDF, plus a .pptx for the notes: exported when the file wasn't
// one, the file itself when the page doesn't have it (a link)
function converted(bytes, name, kind, original) {
  var pdf, pptx, id = upload(bytes, name, KINDS[kind]);
  try {
    pdf = exportAs(id, 'pdf');
    if (kind !== 'pptx') pptx = exportAs(id, 'pptx');
  } finally { drop(id); }
  var base = name.replace(/\.[^.]+$/, ''), files = [{ name: base + '.pdf', data: Utilities.base64Encode(pdf) }];
  if (pptx || original) files.push({ name: base + '.pptx', data: Utilities.base64Encode(pptx || bytes) });
  return { files: files, converted: true };
}

function upload(bytes, name, type) {
  var auth = { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() };
  var s = UrlFetchApp.fetch('https://www.googleapis.com/upload/drive/v3/files?uploadType=resumable', {
    method: 'post', contentType: 'application/json; charset=UTF-8', muteHttpExceptions: true,
    headers: { Authorization: auth.Authorization, 'X-Upload-Content-Type': type },
    payload: JSON.stringify({ name: 'conf42 record - ' + name, mimeType: 'application/vnd.google-apps.presentation' }) });
  var loc = lower(s.getAllHeaders()).location;
  if (!loc) throw new Error('upload: ' + s.getResponseCode());
  var r = UrlFetchApp.fetch(loc, { method: 'put', contentType: type, payload: Utilities.newBlob(bytes, type), headers: auth, muteHttpExceptions: true });
  if (r.getResponseCode() >= 300) throw new Error(r.getResponseCode() === 413 ? 'too big' : 'Google couldn’t convert it (' + r.getResponseCode() + ')');
  return JSON.parse(r.getContentText()).id;
}

// the Slides export link has no size cap (the Drive API's export stops at 10 MB): that first, the API if it says no
function exportAs(id, f) {
  var auth = { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() };
  var r = UrlFetchApp.fetch('https://docs.google.com/presentation/d/' + id + '/export/' + f, { headers: auth, muteHttpExceptions: true });
  if (r.getResponseCode() === 200 && !/text\/html/i.test(lower(r.getAllHeaders())['content-type'] || '')) return r.getContent();
  r = UrlFetchApp.fetch('https://www.googleapis.com/drive/v3/files/' + id + '/export?mimeType=' + encodeURIComponent(KINDS[f]), { headers: auth, muteHttpExceptions: true });
  if (r.getResponseCode() !== 200) throw new Error(r.getResponseCode() === 403 ? 'too big' : 'export: ' + r.getResponseCode());
  return r.getContent();
}

function drop(id) {
  UrlFetchApp.fetch('https://www.googleapis.com/drive/v3/files/' + id, { method: 'delete', muteHttpExceptions: true,
    headers: { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() } });
}

// anonymous fetch: a file that isn't public answers with a sign-in page (HTML) instead
function fetchFile(u) {
  var r = UrlFetchApp.fetch(u, { muteHttpExceptions: true, followRedirects: true }), h = lower(r.getAllHeaders());
  if (r.getResponseCode() === 404) return { error: 'not found' };
  if (r.getResponseCode() !== 200 || /text\/html/i.test(h['content-type'] || '')) return { error: 'private' };
  var bytes = r.getContent();
  if (bytes.length > MAX) return { error: 'too big' };
  var cd = h['content-disposition'] || '', m = /filename\*=UTF-8''([^;]+)/i.exec(cd) || /filename="([^"]+)"/i.exec(cd);
  return { bytes: bytes, name: m ? decodeURIComponent(m[1]) : '', type: h['content-type'] || '' };
}

function kindOf(name, type) {
  var x = (/\.(\w+)$/.exec(name || '') || [])[1];
  x = x && x.toLowerCase();
  if (x === 'key') return 'key';
  if (KINDS[x]) return x;
  for (var k in KINDS) if (type.indexOf(KINDS[k]) === 0) return k;
  return '';
}

function lower(h) { var o = {}; Object.keys(h).forEach(function (k) { o[k.toLowerCase()] = String(h[k]); }); return o; }
function out(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

// run once in the editor after a change of scopes: asks for the authorization, then makes and deletes a tiny file the
// way a conversion does (only drive.file - the script can't open anything else in the account)
function selftest() {
  var auth = { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() };
  var r = UrlFetchApp.fetch('https://www.googleapis.com/upload/drive/v3/files?uploadType=media', { method: 'post', contentType: 'text/plain', payload: 'conf42 record selftest', headers: auth });
  var id = JSON.parse(r.getContentText()).id;
  drop(id);
  Logger.log('ok: made and deleted %s', id);
}
