// conf42.com/record (Marek 2026-10-31): a Google Slides link -> the deck as PDF (?f=pdf) or .pptx (?f=pptx), so the
// recorder gets the slides and the speaker notes with one click. A page can't fetch these itself: Google's export
// links don't allow other sites. Only decks shared "Anyone with the link": the fetch here is anonymous (no token), so
// nothing that is private to this account can ever come out of it.
//
// Deploy once: script.google.com -> New project -> paste this file -> Deploy -> New deployment -> Web app,
//   Execute as: Me, Who has access: Anyone -> Deploy -> copy the ".../exec" URL into SLIDES_LINK in
//   _templates/record.html. A changed script needs Deploy -> Manage deployments -> edit -> New version (same URL).

function doGet(e) {
  var id = String(e.parameter.id || ''), f = e.parameter.f === 'pptx' ? 'pptx' : 'pdf';
  if (!/^[\w-]{20,100}$/.test(id)) return out({ error: 'bad link' });
  var r = UrlFetchApp.fetch('https://docs.google.com/presentation/d/' + id + '/export/' + f, { muteHttpExceptions: true, followRedirects: true });
  var h = {}, all = r.getAllHeaders();
  Object.keys(all).forEach(function (k) { h[k.toLowerCase()] = String(all[k]); });
  // a deck that isn't public sends Google's sign-in page (HTML) instead of the file
  if (r.getResponseCode() !== 200 || /text\/html/i.test(h['content-type'] || '')) return out({ error: r.getResponseCode() === 404 ? 'not found' : 'private' });
  var m = /filename\*=UTF-8''([^;]+)/i.exec(h['content-disposition'] || '') || /filename="([^"]+)"/i.exec(h['content-disposition'] || '');
  var name = m ? decodeURIComponent(m[1]) : 'slides.' + f;
  return out({ name: name, data: Utilities.base64Encode(r.getContent()) });
}

function out(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }
