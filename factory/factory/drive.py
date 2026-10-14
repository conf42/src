"""Drive upload folders shared as "anyone with the link": list them and download their files with no browser and no
sign-in (Marek 2026-10-14: "make it work every time").

- list:     https://drive.google.com/embeddedfolderview?id=<folder>  (the public folder view: ids and titles, subfolders)
- size/time: a HEAD on the download link answers Content-Length and Last-Modified (the upload time) without the file
- download: https://drive.usercontent.google.com/download?id=<file>&export=download&confirm=t  (confirm=t skips Drive's
            "too large to scan for viruses" page)

Google Vids projects and other Google-native files have no download: their HEAD fails and they are skipped.
"""
import datetime
import email.utils
import html
import os
import re
import time
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (conf42 factory)"}
DL = "https://drive.usercontent.google.com/download?id=%s&export=download&confirm=t"
ENTRY = re.compile(r'<div class="flip-entry" id="entry-([^"]+)".*?<a href="([^"]+)".*?<div class="flip-entry-title">(.*?)</div>', re.S)


def folder_id(link):
    """A Drive folder link (…/folders/<id>?usp=…, …?id=<id>) or a bare id -> the id."""
    m = re.search(r"folders/([A-Za-z0-9_-]{10,})", link or "") or re.search(r"[?&]id=([A-Za-z0-9_-]{10,})", link or "")
    return m.group(1) if m else (link or "").strip()


def _open(url, method="GET"):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA, method=method), timeout=120)


def list_folder(fid, depth=3, path=""):
    """Every file under the folder: [{id, title, folder}]. Subfolders are followed (Talks, Slides), except the
    speakers' OBS overlays, which are templates we hand out, not uploads."""
    with _open("https://drive.google.com/embeddedfolderview?id=" + fid) as r:
        page = r.read().decode("utf-8", "replace")
    out = []
    for eid, href, title in ENTRY.findall(page):
        title = html.unescape(title).strip()
        if "/folders/" in href:
            if depth > 0 and "overlay" not in title.lower():
                out += list_folder(eid, depth - 1, path + title + "/")
        else:
            out.append({"id": eid, "title": title, "folder": path})
    return out


def head(fid, tries=3):
    """(size in bytes, upload time as ISO UTC) of a downloadable file; raises for Google-native files (Vids, Docs).
    Drive answers the odd 500 for a real file too, so it is asked up to three times."""
    for n in range(tries):
        try:
            with _open(DL % fid, "HEAD") as r:
                size = int(r.headers.get("Content-Length") or 0)
                lm = r.headers.get("Last-Modified")
            break
        except Exception:                                # noqa: BLE001
            if n == tries - 1:
                raise
            time.sleep(2 * (n + 1))
    up = email.utils.parsedate_to_datetime(lm).astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ") if lm else ""
    return size, up


def download(fid, dest, size=0, note=None):
    """Download to dest (via dest.part, so a broken download never looks finished); the size must match the HEAD."""
    part = dest + ".part"
    got, step = 0, max(size // 10, 1) if size else 0
    with _open(DL % fid) as r, open(part, "wb") as f:
        while True:
            chunk = r.read(8 << 20)
            if not chunk:
                break
            f.write(chunk)
            if note and step and (got + len(chunk)) // step > got // step:
                note("downloading %s: %d%% of %.0f MB" % (os.path.basename(dest), (got + len(chunk)) * 100 // size, size / 1e6))
            got += len(chunk)
    if size and got != size:
        os.remove(part)
        raise IOError("%s: got %d bytes, Drive says %d" % (os.path.basename(dest), got, size))
    os.replace(part, dest)
    return dest
