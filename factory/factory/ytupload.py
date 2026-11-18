"""YouTube upload for the cloud factory (Marek 2026-11-13): every finished talk goes up UNLISTED with everything that
used to sit in "YouTube items.txt" - nobody copies anything any more - and the operator takes it from there (checks
it, makes it public / schedules it, fills the CSV's YouTube column).

Per talk, once (the video id lands in _db/factory_runs/<event>/youtube.json; a later pass never uploads it again):
  1. videos.insert, resumable: the final -14 LUFS MP4, title + description from youtube.block() (abstract / sessions
     / CFP / Discord links + chapters), tags from the talk's Keywords, category Science & Technology, not for kids,
     privacyStatus from settings youtube.privacy (default unlisted).
  2. thumbnails.set: the talk's 1280x720 thumbnail from conf42.com/<event>/teasers (build/youtube_thumbnails.py), as
     JPEG when the PNG is over YouTube's 2 MB.
  3. captions.insert: the proofread SRT (src/srt/<short_url>_<Name1>.srt).
  4. playlistItems.insert into "Conf42 <Name> <Year>" (made unlisted when it doesn't exist yet - an operator makes it
     public: a public playlist would show the unlisted videos).
  5. the link https://youtu.be/<id> into the YouTube column of the event's tab in Excels_for_WWW (Marek 2026-11-13;
     sheet_links below, through the "Conf42 upload" script) - only into an empty cell, never over a typed link.
Quota (2026-11): uploads have their own bucket (100 a day); thumbnail 50, captions 400, playlist 50 of 10,000 a day.

Auth: secret YOUTUBE_OAUTH_JSON = {"client_id", "client_secret", "refresh_token", "channel_id"} made once with
`python -m factory youtube-login <client_secret.json>` by the account that manages the Conf42 channel. The Google
Cloud consent screen must be "In production" (or Internal): in Testing mode refresh tokens die after 7 days.
"""
import io
import json
import os
import re
import time
import urllib.parse

import requests

from . import events, youtube

TOKEN_URL = "https://oauth2.googleapis.com/token"
API = "https://www.googleapis.com/youtube/v3"
UPLOAD = "https://www.googleapis.com/upload/youtube/v3"
SCOPES = "https://www.googleapis.com/auth/youtube.upload https://www.googleapis.com/auth/youtube.force-ssl"
REPO_RUNS = os.path.join(events.REPO, "_db", "factory_runs")


class YouTube:
    def __init__(self, creds=None):
        raw = creds or os.environ.get("YOUTUBE_OAUTH_JSON") or ""
        if not raw:
            raise LookupError("YOUTUBE_OAUTH_JSON not set")
        self.c = json.loads(raw) if isinstance(raw, str) else raw
        self.token, self.at = None, 0

    def auth(self):
        if self.token and time.time() - self.at < 45 * 60:
            return self.token
        r = requests.post(TOKEN_URL, data={"client_id": self.c["client_id"], "client_secret": self.c["client_secret"],
                                           "refresh_token": self.c["refresh_token"], "grant_type": "refresh_token"}, timeout=60)
        if r.status_code != 200:
            raise RuntimeError("YouTube sign-in failed (%s) - the refresh token may be revoked or expired: run "
                               "`python -m factory youtube-login` again" % r.text[:200])
        self.token, self.at = r.json()["access_token"], time.time()
        return self.token

    def call(self, method, url, **kw):
        for attempt in range(5):
            h = dict(kw.pop("headers", {}) or {}, Authorization="Bearer " + self.auth())
            r = requests.request(method, url, headers=h, timeout=kw.pop("timeout", 120), **kw)
            if r.status_code in (500, 502, 503, 504):
                time.sleep(3 * 2 ** attempt)
                continue
            if r.status_code == 401 and attempt == 0:
                self.token = None
                continue
            return r
        return r

    def check_channel(self, want=None):
        """The signed-in channel, which must be exactly `want` (settings youtube.channel_id): never upload elsewhere."""
        r = self.call("GET", API + "/channels", params={"part": "id,snippet", "mine": "true"})
        if r.status_code != 200:
            raise RuntimeError("YouTube: cannot read the channel (%s)" % r.text[:200])
        items = r.json().get("items") or []
        want = want or self.c.get("channel_id")
        if not want:
            raise RuntimeError("YouTube: no channel_id in settings.yml youtube - refusing to upload anywhere")
        if not items or items[0]["id"] != want:
            got = items[0] if items else None
            raise RuntimeError("YouTube: signed in to %s, not the Conf42 channel %s - nothing uploaded" %
                               (("%s (%s)" % (got["snippet"]["title"], got["id"])) if got else "no channel", want))
        return items[0]

    def upload(self, path, body, note=None):
        """Resumable videos.insert; resumes from YouTube's offset after a dropped chunk. Returns the video id."""
        size = os.path.getsize(path)
        r = self.call("POST", UPLOAD + "/videos", params={"uploadType": "resumable", "part": "snippet,status"},
                      json=body, headers={"X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)})
        if r.status_code == 403 and "quota" in r.text.lower():
            raise QuotaExceeded(r.text[:200])
        if r.status_code != 200 or "Location" not in r.headers:
            raise RuntimeError("YouTube upload refused: HTTP %d %s" % (r.status_code, r.text[:300]))
        url, sent, chunk, fails = r.headers["Location"], 0, 32 << 20, 0
        with open(path, "rb") as f:
            while True:
                f.seek(sent)
                data = f.read(chunk)
                end = sent + len(data) - 1
                try:
                    r = requests.put(url, data=data, timeout=600, headers={"Authorization": "Bearer " + self.auth(),
                                     "Content-Range": "bytes %d-%d/%d" % (sent, end, size)})
                except requests.RequestException:
                    r = None
                if r is not None and r.status_code in (200, 201):
                    return r.json()["id"]
                if r is not None and r.status_code == 308:
                    rg = r.headers.get("Range")
                    sent = int(rg.split("-")[1]) + 1 if rg else 0
                    fails = 0
                    if note:
                        note("youtube: %s %.0f%%" % (os.path.basename(path), 100.0 * sent / size))
                    continue
                fails += 1
                if fails > 8:
                    raise RuntimeError("YouTube upload kept failing (%s)" % (r.text[:200] if r is not None else "network"))
                time.sleep(min(120, 5 * 2 ** fails))
                q = requests.put(url, timeout=60, headers={"Authorization": "Bearer " + self.auth(), "Content-Range": "bytes */%d" % size})
                if q.status_code in (200, 201):
                    return q.json()["id"]
                rg = q.headers.get("Range") if q.status_code == 308 else None
                sent = int(rg.split("-")[1]) + 1 if rg else 0

    def thumbnail(self, video_id, data, mime):
        r = self.call("POST", UPLOAD + "/thumbnails/set", params={"videoId": video_id, "uploadType": "media"},
                      data=data, headers={"Content-Type": mime})
        return r.status_code == 200, r.text[:200]

    def captions(self, video_id, srt_text, lang="en"):
        meta = {"snippet": {"videoId": video_id, "language": lang, "name": "English", "isDraft": False}}
        boundary = "conf42factory"
        body = ("--%s\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n%s\r\n--%s\r\nContent-Type: application/octet-stream\r\n\r\n"
                % (boundary, json.dumps(meta), boundary)).encode() + srt_text.encode("utf-8") + ("\r\n--%s--" % boundary).encode()
        r = self.call("POST", UPLOAD + "/captions", params={"part": "snippet", "uploadType": "multipart"}, data=body,
                      headers={"Content-Type": "multipart/related; boundary=" + boundary})
        return r.status_code == 200, r.text[:200]

    def playlist(self, title, name=None, year=None):
        """The channel's playlist for the event: the exact title (case, punctuation and spaces ignored), else the one
        playlist whose title has "conf42", the event's name and its year (Marek 2026-11-18: he made the 2026 + 2027
        playlists by hand). Several such playlists: nothing is guessed or made (RuntimeError). None at all: made
        unlisted. Returns (id, made)."""
        norm = lambda t: " ".join(re.sub(r"[^a-z0-9]+", " ", str(t).lower()).split())
        want, exact, loose, page = norm(title), [], [], None
        words = [w for w in norm("conf42 %s %s" % (name or "", year or "")).split()] if name and year else []
        while True:
            params = {"part": "id,snippet", "mine": "true", "maxResults": 50}
            if page:
                params["pageToken"] = page
            d = self.call("GET", API + "/playlists", params=params).json()
            for p in d.get("items", []):
                t = norm(p["snippet"]["title"])
                if t == want:
                    exact.append(p["id"])
                elif words and all(w in t.split() for w in words) and norm(name) in t:
                    loose.append((p["id"], p["snippet"]["title"]))
            page = d.get("nextPageToken")
            if not page:
                break
        if exact:
            return exact[0], False
        if len(loose) == 1:
            return loose[0][0], False
        if len(loose) > 1:
            raise RuntimeError("several playlists could be this event's (%s) - add its playlist_url to metadata.yml"
                               % "; ".join(t for _, t in loose)[:200])
        r = self.call("POST", API + "/playlists", params={"part": "snippet,status"},
                      json={"snippet": {"title": title}, "status": {"privacyStatus": "unlisted"}})
        if r.status_code != 200:
            raise RuntimeError("playlist: %s" % r.text[:200])
        return r.json()["id"], True

    def add_to_playlist(self, playlist_id, video_id):
        r = self.call("POST", API + "/playlistItems", params={"part": "snippet"},
                      json={"snippet": {"playlistId": playlist_id, "resourceId": {"kind": "youtube#video", "videoId": video_id}}})
        return r.status_code == 200, r.text[:200]

    def playlist_items(self, playlist_id):
        """[(item id, video id, added at)] in the playlist's position order."""
        out, page = [], None
        while True:
            params = {"part": "snippet", "playlistId": playlist_id, "maxResults": 50}
            if page:
                params["pageToken"] = page
            r = self.call("GET", API + "/playlistItems", params=params)
            if r.status_code != 200:
                raise RuntimeError("playlist items: %s" % r.text[:200])
            d = r.json()
            out += [(i["id"], i["snippet"]["resourceId"].get("videoId"), i["snippet"].get("publishedAt") or "")
                    for i in d.get("items", [])]
            page = d.get("nextPageToken")
            if not page:
                return out

    def remove_item(self, item_id):
        r = self.call("DELETE", API + "/playlistItems", params={"id": item_id})
        return r.status_code in (200, 204), r.text[:200]

    def status(self, video_id):
        r = self.call("GET", API + "/videos", params={"part": "status,processingDetails", "id": video_id})
        items = r.json().get("items") or [] if r.status_code == 200 else []
        return items[0] if items else None


class QuotaExceeded(RuntimeError):
    pass


# ---- the parts that need no network (tested offline) -------------------------------------------------------------

def clean_text(s, limit):
    """YouTube refuses < and > in titles and descriptions; titles <= 100 chars, descriptions <= 5000 bytes."""
    s = s.replace("<", "‹").replace(">", "›")
    if limit == 100:
        return s[:100]
    b = s.encode("utf-8")
    if len(b) <= limit:
        return s
    return b[:limit].decode("utf-8", "ignore").rsplit("\n", 1)[0]


def valid_chapters(chapters, length=None):
    """The chapter lines YouTube will accept (first at 0:00, at least 3, each at least 10 s), or [] (then the
    description goes without them). Returns (chapters, note)."""
    def secs(at):
        p = [int(x) for x in str(at).split(":")]
        return p[0] * 3600 + p[1] * 60 + p[2] if len(p) == 3 else p[0] * 60 + p[1]
    try:
        cs = sorted(chapters or [], key=lambda c: secs(c["at"]))
    except (ValueError, KeyError, IndexError):
        return [], "chapters unreadable - left out"
    if not cs:
        return [], ""
    if secs(cs[0]["at"]) != 0:
        cs = [{"at": "0:00", "title": "Intro"}] + cs
    keep = [cs[0]]
    for c in cs[1:]:
        if secs(c["at"]) - secs(keep[-1]["at"]) >= 10 and (not length or secs(c["at"]) < length - 10):
            keep.append(c)
    if len(keep) < 3:
        return [], "fewer than 3 usable chapters - left out"
    return keep, "" if len(keep) == len(cs) else "%d chapter(s) too close together - dropped" % (len(cs) - len(keep))


def video_body(ev, cfg, row, chapters, written=None, keywords="", length=None):
    ch, note = valid_chapters(chapters, length)
    title, lines = youtube.block(ev, cfg, row, ch, written)
    if not ch:
        lines = [l for l in lines if l != "Chapters"]
    desc = "\n".join(lines[2:]).rstrip()
    tags = [t.strip() for t in re.split(r"[,;]", keywords or "") if t.strip()]
    tags = ["Conf42", "Conf42 %s" % ev["name"]] + tags
    while len(",".join(tags)) > 450:
        tags.pop()
    yt = cfg.get("youtube") or {}
    body = {"snippet": {"title": clean_text(title, 100), "description": clean_text(desc, 4900), "tags": tags,
                        "categoryId": str(yt.get("category_id") or 28), "defaultLanguage": "en", "defaultAudioLanguage": "en"},
            "status": {"privacyStatus": str(yt.get("privacy") or "unlisted"), "selfDeclaredMadeForKids": False,
                       "embeddable": True, "license": "youtube"}}
    return body, note


def thumbnail_for(ev, row):
    """(bytes, mime) of the talk's thumbnail from the live teasers page, or (None, why)."""
    base = "https://www.conf42.com/%s/" % ev["short_url"]
    try:
        page = requests.get(base + "teasers", timeout=60).text
    except requests.RequestException as e:
        return None, "teasers page unreachable (%s)" % e
    m = re.search(r'<script[^>]*id="th-data"[^>]*>(.*?)</script>', page, re.S)
    if not m:
        return None, "no thumbnails on the teasers page yet"
    try:
        data = json.loads(m.group(1))
    except ValueError:
        return None, "thumbnail data unreadable"
    talks = data.get("talks", data) if isinstance(data, dict) else data
    want = {n.strip().lower() for n in row["speakers"].split("&")}
    hit = None
    for t in talks if isinstance(talks, list) else []:
        names = {n.strip().lower() for n in str(t.get("name") or "").split("&")}
        if names == want:
            hit = t
            break
    if not hit or not hit.get("file"):
        return None, "no thumbnail for %s yet" % row["speakers"]
    r = requests.get(base + urllib.parse.quote(hit["file"]), timeout=60)
    if r.status_code != 200:
        return None, "thumbnail not drawn yet (%d)" % r.status_code
    data = r.content
    if len(data) <= 2 * 1024 * 1024:
        return (data, "image/png"), ""
    from PIL import Image
    im = Image.open(io.BytesIO(data)).convert("RGB")
    out = io.BytesIO()
    im.save(out, "JPEG", quality=90, optimize=True)
    return (out.getvalue(), "image/jpeg"), ""


# ---- one event -------------------------------------------------------------------------------------------------

def load(slug):
    p = os.path.join(REPO_RUNS, slug, "youtube.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save(slug, d):
    p = os.path.join(REPO_RUNS, slug, "youtube.json")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write("\n")


def redone_since(t, rec):
    """True when the talk was redone (a new video from the speaker, pipeline.redo) after the upload in `rec`: the
    new version then goes up as a new YouTube video and replaces the factory's link in the sheet, like its
    transcript and deck replace the old ones on the site (Marek 2026-11-14). YouTube cannot swap a video's file."""
    n = len(t.get("redone") or [])
    if not n or not rec.get("id"):
        return False
    if "redone" in rec:
        return n > rec["redone"]
    return t["redone"][-1].get("at", "")[:19] > (rec.get("uploaded_at") or "")[:19]   # uploads from before 2026-11-14


def event(run, cfg):
    """Upload the event's finished talks that are not on YouTube yet (or were redone since). Yields log lines. No
    secret = nothing happens."""
    try:
        yt = YouTube()
    except LookupError:
        yield "youtube: not configured (YOUTUBE_OAUTH_JSON) - skipped"
        return
    slug, ev = run.ev["short_url"], run.ev
    done = load(slug)
    rows = {r["speakers"]: r for r in youtube.talk_rows(ev)}
    raw = {t["speakers"]: t for t in events.talks(ev)}
    for msg in repair(yt, run, cfg, done, rows):
        yield msg
    todo = [k for k, t in sorted(run.state["talks"].items())
            if t.get("finished") and (not (done.get(k) or {}).get("id") or redone_since(t, done[k]))]
    if not todo:
        yield from playlist_order(yt, ev, cfg, done, run)
        yield from sheet_links(ev, done, raw)             # links of earlier passes that are not in the sheet yet
        return
    yt.check_channel((cfg.get("youtube") or {}).get("channel_id"))
    playlist_id = None
    for key in todo:
        t, row = run.state["talks"][key], rows.get(key)
        final = os.path.join(run.final_dir, "%s - %s.mp4" % (key, ev["title"]))
        if not row:
            yield "youtube: %s is not in the lineup any more - not uploaded" % key
            continue
        if not os.path.exists(final):
            # a fresh runner: the finished file is gone - publish + download + loudness again (no new edit credits)
            for step in ("publish", "download", "loudness", "qa"):
                t["steps"].pop(step, None)
            t.pop("finished", None)
            run.save()
            yield "youtube: %s - final video not on this runner, it is made again next pass" % key
            continue
        ch = ((t.get("steps") or {}).get("chapters") or {}).get("chapters") or []
        length = (t.get("probe") or {}).get("duration")
        body, note = video_body(ev, cfg, row, ch, t.get("yt_title"), (raw.get(key) or {}).get("keywords"), length)
        is_test = bool(row.get("test"))
        if is_test:                                       # the factory's own test talk: unlisted whatever the settings say
            body["snippet"]["title"] = clean_text("[TEST] " + body["snippet"]["title"], 100)
            body["status"]["privacyStatus"] = "unlisted"
        rec = {"title": body["snippet"]["title"], "privacy": body["status"]["privacyStatus"], "redone": len(t.get("redone") or [])}
        if is_test:
            rec["test"] = True
        old = done.get(key) or {}
        if old.get("id"):                                 # a redone talk: the new video replaces the old one
            rec["replaces"] = (old.get("replaces") or []) + [old["id"]]
            if old.get("sheet"):
                rec["sheet"] = old["sheet"]               # sheet_links swaps the factory's own link for the new one
        try:
            vid = yt.upload(final, body, run.note)
        except QuotaExceeded:
            yield "youtube: daily upload limit reached - the rest goes up tomorrow"
            break
        rec.update(id=vid, uploaded_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), studio="https://studio.youtube.com/video/%s/edit" % vid)
        if note:
            rec["note"] = note
        done[key] = rec
        save(slug, done)                                  # the id first: a crash later never uploads it twice
        thumb, why = thumbnail_for(ev, row)
        rec["thumbnail"] = yt.thumbnail(vid, *thumb)[0] if thumb else False
        if why:
            rec["thumbnail_note"] = why
        srt = run.srt_path(t)
        if os.path.exists(srt):
            with open(srt, encoding="utf-8-sig") as f:
                ok, msg = yt.captions(vid, f.read())
            rec["captions"] = ok
            if not ok:
                rec["captions_note"] = msg
        try:
            if is_test:
                raise RuntimeError("test talk - kept out of the playlist")
            if playlist_id is None:
                playlist_id, made, title = playlist_for(yt, ev, cfg)
                if made:
                    yield "youtube: made the playlist %s (unlisted - make it public when the talks are)" % title
            rec["playlist"] = yt.add_to_playlist(playlist_id, vid)[0]
        except Exception as e:                           # noqa: BLE001
            rec["playlist"] = False
            rec["playlist_note"] = str(e)[:200]
        st = yt.status(vid) or {}
        rec["upload_status"] = (st.get("status") or {}).get("uploadStatus")
        if (st.get("status") or {}).get("rejectionReason") or (st.get("status") or {}).get("failureReason"):
            rec["problem"] = (st["status"].get("rejectionReason") or st["status"].get("failureReason"))
        done[key] = rec
        save(slug, done)
        yield "youtube: %s -> %s (%s)%s" % (key, rec["studio"], rec["privacy"],
                                            "" if rec.get("thumbnail") else " - no thumbnail: " + rec.get("thumbnail_note", "refused"))
        if rec.get("replaces"):
            yield ("youtube: %s was redone - this is the new video. The old one is still on YouTube and in the playlist: "
                   "delete it at https://studio.youtube.com/video/%s/edit" % (key, rec["replaces"][-1]))
    yield from playlist_order(yt, ev, cfg, done, run)
    yield from sheet_links(ev, done, raw)


def playlist_id_from(url):
    """The list= id of a YouTube playlist link (metadata.yml playlist_url), or None."""
    q = urllib.parse.parse_qs(urllib.parse.urlparse(str(url or "")).query)
    pid = (q.get("list") or [""])[0]
    return pid if re.fullmatch(r"[\w-]{10,64}", pid) else None


def playlist_for(yt, ev, cfg):
    """The event's playlist: the one the site links (metadata.yml playlist_url, Marek 2026-11-18: "add talks to the
    corresponding playlist"), else found by title among the channel's playlists, else made unlisted - and then wired
    to the website: its link goes into the event's playlist_url in metadata.yml, pushed ("remember to rewire the
    playlist to the website"). Returns (id, made, title)."""
    pid = playlist_id_from(ev.get("playlist_url"))
    if pid:
        return pid, False, "playlist_url"
    title = str((cfg.get("youtube") or {}).get("playlist_title") or "Conf42 {name} {year}").format(name=ev["name"], year=ev["year"])
    pid, made = yt.playlist(title, ev.get("name"), ev.get("year"))
    ev["playlist_url"] = "https://www.youtube.com/playlist?list=%s" % pid
    WIRED.append((ev["short_url"], ev["playlist_url"], wire_site(ev["short_url"], ev["playlist_url"])))
    return pid, made, title


WIRED = []                                               # (short_url, url, result) - the pass log shows them


def set_playlist_url(text, slug, url):
    """metadata.yml text with the event's playlist_url set (the key added after short_url when missing). Only an
    empty value (~ / blank) is filled: a link somebody typed is never replaced. Returns (text, changed)."""
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if re.fullmatch(r"\s+short_url:\s*%s\s*" % re.escape(slug), l)), None)
    if start is None:
        raise LookupError("no event %s in metadata.yml" % slug)
    indent = re.match(r"\s*", lines[start]).group(0)
    top = start
    while top > 0 and not re.match(r"\s*- ", lines[top]):
        top -= 1
    end = start + 1
    while end < len(lines) and not re.match(r"\s*- \w+:", lines[end]) and not re.match(r"\S", lines[end]):
        end += 1
    for i in range(top, end):
        m = re.match(r"(\s*(?:- )?)playlist_url:\s*(.*)$", lines[i])
        if m and len(m.group(1).replace("- ", "  ")) == len(indent):
            if m.group(2).strip() not in ("", "~", "null", "''", '""'):
                return text, False
            lines[i] = "%splaylist_url: %s" % (m.group(1), url)
            return "\n".join(lines), True
    lines.insert(start + 1, "%splaylist_url: %s" % (indent, url))
    return "\n".join(lines), True


def wire_site(slug, url, git=None):
    """Write the playlist link into metadata.yml and push it (the event page's on-demand button uses it)."""
    path = os.path.join(events.REPO, "metadata.yml")
    try:
        if git is None:
            from .app import _git
            git = _git()
        git("-c", "gc.auto=0", "pull", "--rebase", "--autostash", "-q")
        with open(path, encoding="utf-8", newline="") as f:
            text = f.read()
        new, changed = set_playlist_url(text, slug, url)
        if not changed:
            return "metadata.yml already has a playlist_url for %s - left as it is" % slug
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(new)
        git("add", "--", "metadata.yml")
        git("commit", "-q", "-m", "factory: %s playlist_url -> the event's YouTube playlist" % slug, "--", "metadata.yml")
        for _ in range(3):
            if git("-c", "gc.auto=0", "push", "-q").returncode == 0:
                return "playlist wired to the website (metadata.yml playlist_url, pushed)"
            git("-c", "gc.auto=0", "pull", "--rebase", "--autostash", "-q")
        return "metadata.yml committed, push failed - the pass's own push takes it"
    except Exception as e:                               # noqa: BLE001 - never fails the pass
        return "metadata.yml not updated (%s) - add playlist_url: %s by hand" % (str(e)[:150], url)


def site_order(talks):
    """Talk keys in the order the event page shows them (build/events.py + event.html): keynotes, panels, then each
    track in the order it first appears, talks in CSV order inside it; banished talks after, the test talk never."""
    live = [t for t in talks if not t.get("banished")]
    out = [t["speakers"] for t in live if t.get("featured")]
    out += [t["speakers"] for t in live if t.get("panel") and t["speakers"] not in out]
    tracks = []
    for t in live:
        if not t.get("featured") and not t.get("panel") and t.get("track", "other") not in tracks:
            tracks.append(t.get("track", "other"))
    for tr in tracks:
        out += [t["speakers"] for t in live if not t.get("featured") and not t.get("panel") and t.get("track", "other") == tr]
    out += [t["speakers"] for t in talks if t.get("banished") and not t.get("test") and t["speakers"] not in out]
    return out


def readd_plan(current, wanted):
    """current: video ids in playlist order; wanted: our talks' video ids in page order. Marek 2026-11-18: add the
    talks to the playlist in the website order - works whatever the playlist's sorting is (except newest first), no
    "Manual" needed. The talks already in order at the front stay; from the first one out of place, the rest are taken
    out and added again in page order (missing ones simply added). Returns (keep, readd): readd in the order to add."""
    ours = [v for v in current if v in set(wanted)]
    k = 0
    while k < len(ours) and k < len(wanted) and ours[k] == wanted[k]:
        k += 1
    return wanted[:k], wanted[k:]


def playlist_order(yt, ev, cfg, done, run=None):
    """Every pass (Marek 2026-11-18): each uploaded talk is in the event's playlist, in the order of the event page,
    by adding the talks in that order (readd_plan) - no "Manual" sorting needed in YouTube Studio. Taking out and
    adding are 50 units each; a playlist already in order costs one list call. Never fails the pass. A pass stopped
    halfway (quota) leaves talks out of the playlist for a few hours: the next pass adds them, still in order."""
    if (cfg.get("youtube") or {}).get("playlist_sort") is False:
        return
    try:
        order = site_order(events.talks(ev))
        vid_of = {k: r["id"] for k, r in done.items() if r.get("id") and not r.get("test")}
        wanted = [vid_of[k] for k in order if k in vid_of]
        if not wanted:
            return
        pid = playlist_for(yt, ev, cfg)[0]
        # the order the talks were ADDED (publishedAt of the playlist item), which is what a playlist sorted by date
        # shows; adding in page order puts the positions right too, so the playlist is right however it is sorted
        items = [(i, v) for i, v, _ in sorted(yt.playlist_items(pid), key=lambda x: x[2])]
        keep, readd = readd_plan([v for _, v in items], wanted)
        if not readd:
            return
        key_of = {v: k for k, v in vid_of.items()}
        items_of = {}
        for i, v in items:
            items_of.setdefault(v, []).append(i)
        for v in readd:                                  # out first (a video twice in the playlist: every copy)
            for item in items_of.get(v, []):
                ok, msg = yt.remove_item(item)
                if not ok:
                    yield "youtube: playlist not sorted - could not take out %s (%s)" % (key_of[v], msg[:120])
                    return
        for n, v in enumerate(readd):                    # then back in, in the order of the event page
            ok, msg = yt.add_to_playlist(pid, v)
            if not ok:
                yield "youtube: playlist - %d of %d talks added back in order, then: %s (the next pass goes on)" % (
                    n, len(readd), msg[:160])
                return
            done[key_of[v]]["playlist"] = True
            done[key_of[v]].pop("playlist_note", None)
        save(ev["short_url"], done)
        yield "youtube: playlist in the event page's order (%d talks kept, %d added in order)" % (len(keep), len(readd))
    except Exception as e:                               # noqa: BLE001 - sorting never fails the pass
        yield "youtube: playlist not sorted (%s)" % str(e)[:200]
    finally:
        while WIRED:
            slug, url, res = WIRED.pop(0)
            yield "youtube: %s %s - %s" % (slug, url, res)


def repair(yt, run, cfg, done, rows):
    """What an upload could not finish is tried again every pass: the thumbnail, the captions, the playlist. YouTube's
    daily limit can fall between a video and its extras (2026-11-16: a video went up, its three extras were refused).
    Stops at the first refusal for the limit. Yields log lines."""
    slug, ev = run.ev["short_url"], run.ev
    playlist_id, changed = None, False
    limit = lambda text: "quota" in str(text).lower()
    for key, rec in sorted(done.items()):
        row, t = rows.get(key), run.state["talks"].get(key)
        if not rec.get("id") or rec.get("test") or not row or not t:
            continue
        got = []
        try:
            if rec.get("thumbnail") is False and not rec.get("thumbnail_note"):     # there was one, YouTube refused it
                thumb, _ = thumbnail_for(ev, row)
                if thumb:
                    ok, msg = yt.thumbnail(rec["id"], *thumb)
                    if not ok and limit(msg):
                        break
                    if ok:
                        rec["thumbnail"] = True
                        got.append("thumbnail")
            # captions False (refused) or None (no transcript yet at upload time). A later cloud pass has no work folder
            # copy of the transcript, so the shipped one in the repo's srt/ counts too (2026-11-18: Arpita Sheth +
            # Phoebe Wang, mlops2026, stayed without captions for two days)
            srt = run.srt_path(t)
            if not os.path.exists(srt):
                srt = os.path.join(events.REPO, "srt", os.path.basename(srt))
            if rec.get("captions") is not True and os.path.exists(srt):
                with open(srt, encoding="utf-8-sig") as f:
                    ok, msg = yt.captions(rec["id"], f.read())
                if not ok and limit(msg):
                    break
                if ok:
                    rec["captions"] = True
                    rec.pop("captions_note", None)
                    got.append("captions")
            if rec.get("playlist") is False and "test talk" not in str(rec.get("playlist_note") or ""):
                try:
                    if playlist_id is None:
                        playlist_id = playlist_for(yt, ev, cfg)[0]
                    ok, msg = yt.add_to_playlist(playlist_id, rec["id"])
                except RuntimeError as e:
                    ok, msg = False, str(e)
                if not ok and limit(msg):
                    break
                if ok:
                    rec["playlist"] = True
                    rec.pop("playlist_note", None)
                    got.append("playlist")
        finally:
            if got:
                changed = True
                done[key] = rec
                yield "youtube: %s - added later: %s" % (key, ", ".join(got))
    if changed:
        save(slug, done)


def sheet_post(body):
    """POST to the "Conf42 upload" script with the UPLOAD_FEED key. Returns its JSON answer."""
    u = urllib.parse.urlparse(os.environ.get("UPLOAD_FEED") or "")
    token = (urllib.parse.parse_qs(u.query).get("token") or [""])[0]
    if not token:
        raise LookupError("no UPLOAD_FEED")
    r = requests.post(urllib.parse.urlunparse(u._replace(query="")), data=json.dumps(dict(body, token=token)), timeout=120)
    r.raise_for_status()
    return r.json()


def sheet_links(ev, done, raw, post=None):
    """Every uploaded talk's link into the YouTube column of the event's tab in Excels_for_WWW (the tab is named like
    the event's CSV: _db/MLOPS_2026.csv -> MLOPS_2026). `done` (youtube.json) remembers the link written per talk
    ("sheet"), so a pass asks only for new ones; a cell that holds another link is left alone and noted
    ("sheet_note"). Never fails the pass. Yields log lines."""
    slug = ev["short_url"]
    tab = os.path.splitext(os.path.basename(ev.get("db_path") or ""))[0]
    rows = []
    for key, rec in sorted(done.items()):
        url = "https://youtu.be/%s" % rec.get("id")
        if not rec.get("id") or rec.get("test") or rec.get("sheet") == url or key not in raw:
            continue
        t = raw[key]
        rows.append({"key": key, "name1": t["name1"], "name2": t.get("name2") or "", "title": t.get("title") or "",
                     "url": url, "was": rec.get("sheet") or ""})
    if not rows or not tab:
        return
    try:
        d = (post or sheet_post)({"action": "sheet", "tab": tab, "rows": rows})
    except LookupError:
        return
    except Exception as e:                               # noqa: BLE001
        yield "sheet: links not written (%s)" % str(e)[:200]
        return
    if not d.get("ok"):
        yield "sheet: links not written (%s)%s" % (d.get("error"), " - the Conf42 upload script needs v7"
                                                   if d.get("error") == "bad action" else "")
        return
    wrote = []
    for r in rows:
        what, rec = (d.get("results") or {}).get(r["key"]) or "no answer", done[r["key"]]
        if what in ("written", "same"):
            rec["sheet"] = r["url"]
            rec.pop("sheet_note", None)
            wrote.append(r["key"])
        else:
            rec["sheet_note"] = what
            yield "sheet: %s - link not written (%s)" % (r["key"], what)
    save(slug, done)
    if wrote:
        yield "sheet: YouTube link in %s for %s" % (tab, ", ".join(wrote))
        if post is None:                                 # the real sheet: its CSV goes to the repo, emails left out
            from . import sheetcsv
            yield from sheetcsv.ship(ev)


def login(client_file, want=None):
    """One-time, on a PC with a browser: sign in as the account that manages the Conf42 channel; prints the JSON for
    the YOUTUBE_OAUTH_JSON secret. client_file = the OAuth client (type Desktop app) downloaded from Google Cloud."""
    import http.server
    import secrets
    import threading
    import webbrowser
    with open(client_file, encoding="utf-8") as f:
        c = json.load(f)
    c = c.get("installed") or c.get("web") or c
    state, got = secrets.token_urlsafe(16), {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            got.update({k: v[0] for k, v in q.items()})
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Done - you can close this tab and go back to the terminal.")

        def log_message(self, *a):
            pass
    srv = http.server.HTTPServer(("127.0.0.1", 0), H)
    redirect = "http://127.0.0.1:%d/" % srv.server_port
    url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode({
        "client_id": c["client_id"], "redirect_uri": redirect, "response_type": "code", "scope": SCOPES,
        "access_type": "offline", "prompt": "consent", "state": state})
    print("Opening the browser. Sign in as the account that manages the Conf42 YouTube channel:\n" + url)
    webbrowser.open(url)
    t = threading.Thread(target=srv.handle_request)
    t.start()
    t.join(600)
    if got.get("state") != state or "code" not in got:
        raise SystemExit("no sign-in came back: %s" % got.get("error", "timeout"))
    r = requests.post(TOKEN_URL, data={"code": got["code"], "client_id": c["client_id"], "client_secret": c["client_secret"],
                                       "redirect_uri": redirect, "grant_type": "authorization_code"}, timeout=60).json()
    if "refresh_token" not in r:
        raise SystemExit("Google gave no refresh token: %s" % r)
    creds = {"client_id": c["client_id"], "client_secret": c["client_secret"], "refresh_token": r["refresh_token"]}
    try:
        ch = YouTube(creds).check_channel(want)
    except RuntimeError as e:
        raise SystemExit(str(e) + " - run it again and, on Google's 'Choose an account or brand account' screen, "
                         "pick the Conf42 channel itself (not the personal account).")
    creds["channel_id"] = ch["id"]
    print("\nSigned in to the channel: %s (%s)\n\nPut this into the GitHub secret YOUTUBE_OAUTH_JSON (conf42/src):\n\n%s\n"
          % (ch["snippet"]["title"], ch["id"], json.dumps(creds)))
