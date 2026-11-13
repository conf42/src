/**
 * "Conf42 upload" - Google Apps Script web app (Marek 2026-11-13): the door between conf42.com/record and Drive.
 *
 * At Stop the recorder (_templates/record.html) sends the recording + the slides PDF straight to the
 * "Auto upload" folder inside the Conf42 Speaker Workspace, one folder per upload (speakers who upload by hand keep
 * using the Workspace itself):
 *     Conf42 Speaker Workspace/Auto upload/<event slug>/<Speaker> (<yyyy-mm-dd hh-mm>)/
 *         <Speaker> - Conf42 <Event> <Year>.mp4
 *         <Speaker> - Conf42 <Event> <Year>.pdf      (when the speaker loaded slides)
 *         talk.json                                    (who, which talk, how the recording went, upload status)
 * The cloud factory (factory/factory/intake.py, GitHub Actions) reads the folder, tidies junk away and runs the rest.
 *
 *   POST {action:"start", event, talk, typed, video?, slides?, meta, folder_id?}
 *        checks the request, makes the folder (or reuses folder_id for "add slides later"), writes talk.json
 *        (status "uploading") and opens one Drive resumable session per file. The browser PUTs the bytes straight to
 *        Google in 8 MB chunks, so size is not limited by Apps Script.
 *   POST {action:"finish", folder_id, md5:{video, slides}}
 *        compares sizes + MD5 with what Drive got, sets talk.json status "complete" (or "damaged").
 *   GET  ?ping=1                         {ok, service, version} - the factory's doctor calls this daily
 *   GET  ?list=1&token=<UPLOAD_TOKEN>    {access_token, workspace_id}: a short-lived Drive token for the factory
 *   POST {action:"notify", token, subject, body}        the factory's pass report, mailed to NOTIFY_TO
 *   POST {action:"dispatch", token, event, ...}         "Run now" on conf42.com/factory -> GitHub workflow_dispatch
 *
 * Abuse guards (speakers have no login): honeypot, per-day caps on sessions AND bytes, per-talk cap, strict patterns,
 * sizes. Unmatched uploads are still stored (the factory holds them, it never processes a stranger's file).
 *
 * Deploy (one-time, as mark@sreday.com - the owner of the Speaker Workspace):
 *   1. https://script.google.com -> New project "Conf42 upload" -> paste this file; Project settings -> Show
 *      "appsscript.json" -> paste apps-script/conf42-upload.appsscript.json.
 *   2. Project settings -> Script properties: UPLOAD_TOKEN = a long random string (the factory's key),
 *      optional NOTIFY_TO (default: this account), GITHUB_PAT (fine-grained, actions:write on conf42/src only).
 *   3. Run selftest once from the editor (authorises Drive + mail + external requests, checks the folder).
 *   4. Deploy -> New deployment -> Web app -> Execute as: Me -> Who has access: Anyone. Copy the .../exec URL into
 *      metadata.yml -> record_upload_url, and set the GitHub secret UPLOAD_FEED = "<exec URL>?list=1&token=<UPLOAD_TOKEN>".
 *   Re-deploy after editing: Deploy -> Manage deployments -> edit -> New version (the URL stays the same).
 */

var VERSION = 1;
var WORKSPACE_ID = '1BBrIvD-vIxdPoDj9jUG5cjPnlD3YWNib';   // "Conf42 Speaker Workspace/Auto upload" (owner mark@sreday.com)
var ORIGINS = ['https://www.conf42.com', 'https://conf42.com'];
var TZ = 'Europe/London';
var MAX_VIDEO = 4.5 * 1024 * 1024 * 1024;   // 2 h at the recorder's bitrate is ~1.3 GB; 4K screen captures more
var MAX_SLIDES = 200 * 1024 * 1024;
var DAILY_SESSIONS = 80;                      // uploads started per day, all speakers together
var DAILY_BYTES = 200 * 1024 * 1024 * 1024;   // 200 GB a day
var PER_TALK = 6;                             // uploads per talk per day (re-takes are fine, floods aren't)
var REPO = 'conf42/src', WORKFLOW = 'factory-cloud.yml';

function doGet(e) {
  var p = (e && e.parameter) || {};
  if (p.list) {
    if (!tokenOk(p.token)) return respond({ ok: false, error: 'forbidden' });
    return respond({ ok: true, access_token: ScriptApp.getOAuthToken(), workspace_id: workspace().getId(), version: VERSION });
  }
  return respond({ ok: true, service: 'conf42-upload', version: VERSION });
}

function doPost(e) {
  var data;
  try { data = JSON.parse(e.postData.contents); } catch (err) { return respond({ ok: false, error: 'bad json' }); }
  if (data.website) return respond({ ok: true, honeypot: true });   // honeypot -> pretend success
  try {
    if (data.action === 'start') return respond(start(data));
    if (data.action === 'finish') return respond(finish(data));
    if (data.action === 'notify') return respond(notify(data));
    if (data.action === 'dispatch') return respond(dispatch(data));
  } catch (err) {
    Logger.log(data.action + ': ' + err + '\n' + (err.stack || ''));
    return respond({ ok: false, error: String(err.message || err).slice(0, 200) });
  }
  return respond({ ok: false, error: 'bad action' });
}

// ---- start --------------------------------------------------------------------------

function start(data) {
  var ev = data.event || {}, talk = data.talk || {}, errors = [];
  var slug = String(ev.slug || '');
  if (!/^[a-z][a-z0-9-]{2,40}$/.test(slug)) errors.push('event');
  var label = clean(ev.label, 100) || slug;
  var key = String(talk.k || '');
  if (!/^[A-Za-z0-9_]{0,100}$/.test(key)) errors.push('talk');
  var names = (talk.names || []).map(function (n) { return clean(n, 80); }).filter(String).slice(0, 4);
  var typed = clean(data.typed, 80);
  var speaker = names.join(' & ') || typed;
  if (!speaker) errors.push('name');
  var files = [];
  if (data.video) files.push(fileSpec('video', data.video, /\.mp4$/i, MAX_VIDEO, 'video/mp4', errors));
  if (data.slides) files.push(fileSpec('slides', data.slides, /\.pdf$/i, MAX_SLIDES, 'application/pdf', errors));
  if (!files.length) errors.push('files');
  if (errors.length) return { ok: false, error: 'invalid', fields: errors };

  var total = files.reduce(function (a, f) { return a + f.size; }, 0);
  var budget = spend(total, slug + '|' + (key || speaker.toLowerCase()));
  if (budget) return { ok: false, error: budget };

  var base = speaker.replace(/[\\\/:*?"<>|]+/g, ' ').replace(/\s+/g, ' ').trim().slice(0, 120) + ' - ' + label;
  var folder, info;
  if (data.folder_id) {                        // "add slides later": the same upload folder, if it really is one of ours
    folder = ownFolder(String(data.folder_id), slug);
    if (!folder) return { ok: false, error: 'not found' };
    info = readInfo(folder) || {};
  } else {
    var stamp = Utilities.formatDate(new Date(), TZ, 'yyyy-MM-dd HH-mm');
    folder = child(child(workspace(), slug), speaker.replace(/[\\\/:*?"<>|]+/g, ' ').slice(0, 120) + ' (' + stamp + ')');
    info = { conf42_upload: VERSION, created_at: new Date().toISOString(), files: {} };
  }
  info.event = { slug: slug, label: label };
  info.talk = { k: key, names: names, title: clean(talk.title, 300), slot_min: Number(talk.min) || 0 };
  info.typed = typed;
  info.matched = !!key;
  info.meta = sanitize(data.meta || {});
  info.status = 'uploading';
  info.updated_at = new Date().toISOString();
  var origin = ORIGINS.indexOf(String(data.origin || '')) >= 0 ? String(data.origin) : ORIGINS[0];
  var out = { ok: true, folder_id: folder.getId(), uploads: {} };
  files.forEach(function (f) {
    var name = base + (f.role === 'video' ? '.mp4' : '.pdf');
    var url = session(folder, name, f, origin);
    info.files[f.role] = { name: name, size: f.size, original_name: f.original, id: '', md5_browser: '', md5_drive: '', status: 'uploading' };
    out.uploads[f.role] = { upload_url: url, name: name };
  });
  writeInfo(folder, info);
  return out;
}

function fileSpec(role, f, pattern, max, type, errors) {
  var name = clean(f.name, 200), size = Number(f.size) || 0;
  if (!pattern.test(name)) errors.push(role + ' type');
  if (size <= 0 || size > max) errors.push(role + ' size');
  return { role: role, original: name, size: size, type: type };
}

// one per day for everyone + one per talk; null = fine, else the error the page shows
function spend(bytes, talkKey) {
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var day = Utilities.formatDate(new Date(), TZ, 'yyyyMMdd'), p = props();
    var raw = p.getProperty('budget');
    var b = raw ? JSON.parse(raw) : {};
    if (b.day !== day) b = { day: day, n: 0, bytes: 0, talks: {} };
    var t = b.talks[talkKey] || 0;
    if (b.n + 1 > DAILY_SESSIONS || b.bytes + bytes > DAILY_BYTES) return 'too many today';
    if (t + 1 > PER_TALK) return 'too many for this talk';
    b.n += 1; b.bytes += bytes; b.talks[talkKey] = t + 1;
    p.setProperty('budget', JSON.stringify(b));
    return null;
  } finally { lock.releaseLock(); }
}

// Drive API v3 resumable session opened with this script's token; Drive answers CORS for the given origin only
function session(folder, name, f, origin) {
  var res = UrlFetchApp.fetch('https://www.googleapis.com/upload/drive/v3/files?uploadType=resumable&supportsAllDrives=true&fields=id,name,size,md5Checksum', {
    method: 'post',
    contentType: 'application/json; charset=UTF-8',
    headers: {
      Authorization: 'Bearer ' + ScriptApp.getOAuthToken(),
      'X-Upload-Content-Type': f.type,
      'X-Upload-Content-Length': String(f.size),
      Origin: origin
    },
    payload: JSON.stringify({ name: name, parents: [folder.getId()], mimeType: f.type }),
    muteHttpExceptions: true
  });
  var h = lower(res.getAllHeaders());
  if (res.getResponseCode() !== 200 || !h.location) throw new Error('drive session: HTTP ' + res.getResponseCode() + ' ' + res.getContentText().slice(0, 200));
  return h.location;
}

// ---- finish -------------------------------------------------------------------------

function finish(data) {
  var folder = ownFolder(String(data.folder_id || ''), '');
  if (!folder) return { ok: false, error: 'not found' };
  var info = readInfo(folder);
  if (!info) return { ok: false, error: 'not found' };
  var md5 = data.md5 || {}, ok = true, report = {};
  Object.keys(info.files || {}).forEach(function (role) {
    var f = info.files[role];
    if (f.status === 'complete') { report[role] = 'complete'; return; }
    if (data.roles && data.roles.indexOf(role) < 0) { ok = ok && f.status === 'complete'; report[role] = f.status; return; }
    var got = newest(folder, f.name);
    if (!got) { f.status = 'missing'; ok = false; report[role] = 'missing'; return; }
    f.id = got.id; f.md5_drive = got.md5Checksum || ''; f.drive_size = Number(got.size) || 0;
    f.md5_browser = /^[0-9a-f]{32}$/.test(String(md5[role] || '')) ? String(md5[role]) : '';
    if (f.drive_size !== f.size) f.status = 'incomplete';
    else if (f.md5_browser && f.md5_drive && f.md5_browser !== f.md5_drive) f.status = 'damaged';
    else f.status = 'complete';
    if (f.status !== 'complete') ok = false;
    report[role] = f.status;
  });
  info.status = ok ? 'complete' : 'problem';
  info.finished_at = new Date().toISOString();
  writeInfo(folder, info);
  return { ok: true, complete: ok, files: report };
}

// the newest file with this name in the folder (Drive allows twins: a retried upload makes one)
function newest(folder, name) {
  var q = "'" + folder.getId() + "' in parents and name = '" + name.replace(/\\/g, '\\\\').replace(/'/g, "\\'") + "' and trashed = false";
  var r = UrlFetchApp.fetch('https://www.googleapis.com/drive/v3/files?supportsAllDrives=true&includeItemsFromAllDrives=true&orderBy=createdTime desc&pageSize=5' +
    '&fields=files(id,name,size,md5Checksum,createdTime)&q=' + encodeURIComponent(q), { headers: { Authorization: 'Bearer ' + ScriptApp.getOAuthToken() }, muteHttpExceptions: true });
  if (r.getResponseCode() !== 200) throw new Error('drive list: HTTP ' + r.getResponseCode());
  var files = JSON.parse(r.getContentText()).files || [];
  return files[0] || null;
}

// ---- factory helpers (token) ---------------------------------------------------------------

function notify(data) {
  if (!tokenOk(data.token)) return { ok: false, error: 'forbidden' };
  var to = props().getProperty('NOTIFY_TO') || Session.getEffectiveUser().getEmail();
  MailApp.sendEmail({ to: to, subject: clean(data.subject, 200) || 'Conf42 factory', body: String(data.body || '').slice(0, 50000), name: 'Conf42 factory' });
  return { ok: true };
}

// "Run now" on conf42.com/factory: the page knows no GitHub token, this script holds a narrow one
function dispatch(data) {
  if (!tokenOk(data.token)) return { ok: false, error: 'forbidden' };
  var pat = props().getProperty('GITHUB_PAT');
  if (!pat) return { ok: false, error: 'no GITHUB_PAT' };
  var inputs = { event: String(data.event || 'all').replace(/[^a-z0-9-]/g, '').slice(0, 40) || 'all' };
  if (data.dry_run) inputs.dry_run = 'true';
  var r = UrlFetchApp.fetch('https://api.github.com/repos/' + REPO + '/actions/workflows/' + WORKFLOW + '/dispatches', {
    method: 'post', contentType: 'application/json', muteHttpExceptions: true,
    headers: { Authorization: 'Bearer ' + pat, Accept: 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' },
    payload: JSON.stringify({ ref: 'main', inputs: inputs })
  });
  return r.getResponseCode() === 204 ? { ok: true } : { ok: false, error: 'github ' + r.getResponseCode() };
}

// ---- Drive bits ----------------------------------------------------------------------------

function workspace() {
  var id = props().getProperty('WORKSPACE_ID') || WORKSPACE_ID;
  try { return DriveApp.getFolderById(id); }
  catch (err) { throw new Error('No access to the Speaker Workspace ' + id + ' (' + err + ')'); }
}

function child(parent, name) {
  var it = parent.getFoldersByName(name);
  return it.hasNext() ? it.next() : parent.createFolder(name);
}

// an upload folder this script made: it has talk.json and sits in Workspace/<slug>/
function ownFolder(id, slug) {
  if (!/^[\w-]{10,}$/.test(id)) return null;
  try {
    var f = DriveApp.getFolderById(id), ps = f.getParents();
    if (!ps.hasNext()) return null;
    var ev = ps.next(), top = ev.getParents();
    if (!top.hasNext() || top.next().getId() !== workspace().getId()) return null;
    if (slug && ev.getName() !== slug) return null;
    return f.getFilesByName('talk.json').hasNext() ? f : null;
  } catch (err) { return null; }
}

function readInfo(folder) {
  var it = folder.getFilesByName('talk.json');
  if (!it.hasNext()) return null;
  try { return JSON.parse(it.next().getBlob().getDataAsString()); } catch (err) { return null; }
}

function writeInfo(folder, info) {
  var text = JSON.stringify(info, null, 2), it = folder.getFilesByName('talk.json');
  if (it.hasNext()) it.next().setContent(text);
  else folder.createFile('talk.json', text, 'application/json');
}

// ---- small things --------------------------------------------------------------------------

function sanitize(m) {   // the recorder's numbers and words about the recording; nothing else is kept
  var out = {};
  Object.keys(m).slice(0, 40).forEach(function (k) {
    if (!/^[a-z_]{1,30}$/.test(k)) return;
    var v = m[k];
    if (typeof v === 'number' && isFinite(v)) out[k] = v;
    else if (typeof v === 'boolean') out[k] = v;
    else if (typeof v === 'string') out[k] = v.slice(0, 300);
  });
  return out;
}
function clean(s, n) { return String(s == null ? '' : s).replace(/[\u0000-\u001f]+/g, ' ').replace(/\s+/g, ' ').trim().slice(0, n); }
function lower(h) { var o = {}; Object.keys(h).forEach(function (k) { o[k.toLowerCase()] = String(h[k]); }); return o; }
function props() { return PropertiesService.getScriptProperties(); }
function tokenOk(t) { var want = props().getProperty('UPLOAD_TOKEN'); return !!want && String(t || '') === want; }
function respond(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

// run once in the editor: authorises the scopes and proves the folder is reachable + writable
function selftest() {
  var w = workspace();
  var f = w.createFolder('_selftest ' + new Date().toISOString());
  writeInfo(f, { selftest: true });
  Logger.log('ok: %s can write to %s (%s)', Session.getEffectiveUser().getEmail(), w.getName(), w.getId());
  f.setTrashed(true);
  if (!props().getProperty('UPLOAD_TOKEN')) Logger.log('WARNING: set the UPLOAD_TOKEN script property');
}
