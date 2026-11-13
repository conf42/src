"""Google Drive API v3 with a short-lived token, for the cloud factory (intake.py).

The token comes from the "Conf42 upload" Apps Script (apps-script/conf42-upload.gs): GET <exec>?list=1&token=<key>
answers {access_token, workspace_id} - the script's own Drive token (mark@sreday.com, the owner of the Speaker
Workspace), valid about an hour. So the factory needs no Google Cloud project or OAuth client of its own: one secret,
UPLOAD_FEED = "<exec URL>?list=1&token=<UPLOAD_TOKEN>". A 401 fetches a fresh token once.
"""
import json
import os
import time

import requests

API = "https://www.googleapis.com/drive/v3"
FOLDER = "application/vnd.google-apps.folder"


class Drive:
    def __init__(self, feed=None, token=None, root=None):
        self.feed = feed or os.environ.get("UPLOAD_FEED") or ""
        self.token, self.root, self.at = token, root, 0
        if not self.token:
            self.refresh()

    def refresh(self):
        if not self.feed:
            raise RuntimeError("no UPLOAD_FEED (the Conf42 upload script's list URL) - see apps-script/conf42-upload.gs")
        r = requests.get(self.feed, timeout=60)
        r.raise_for_status()
        d = r.json()
        if not d.get("ok"):
            raise RuntimeError("Conf42 upload script: %s" % d.get("error"))
        self.token, self.at = d["access_token"], time.time()
        self.root = self.root or d.get("workspace_id")

    def _call(self, method, url, **kw):
        for attempt in range(5):
            if self.feed and time.time() - self.at > 45 * 60:
                self.refresh()
            h = dict(kw.pop("headers", {}) or {}, Authorization="Bearer " + self.token)
            r = requests.request(method, url, headers=h, timeout=kw.pop("timeout", 120), **kw)
            if r.status_code == 401 and self.feed and attempt == 0:
                self.refresh()
                continue
            if r.status_code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt * 3)
                continue
            if r.status_code >= 400:
                raise RuntimeError("Drive %s %s: HTTP %d %s" % (method, url.split("?")[0][-60:], r.status_code, r.text[:300]))
            return r
        raise RuntimeError("Drive %s: gave up after retries" % method)

    def children(self, folder_id, folders_only=False):
        q = "'%s' in parents and trashed = false" % folder_id
        if folders_only:
            q += " and mimeType = '%s'" % FOLDER
        out, page = [], None
        while True:
            params = {"q": q, "pageSize": 1000, "supportsAllDrives": "true", "includeItemsFromAllDrives": "true",
                      "fields": "nextPageToken,files(id,name,mimeType,size,md5Checksum,createdTime,modifiedTime,parents)"}
            if page:
                params["pageToken"] = page
            d = self._call("GET", API + "/files", params=params).json()
            out += d.get("files", [])
            page = d.get("nextPageToken")
            if not page:
                return out

    def get(self, file_id, fields="id,name,mimeType,size,md5Checksum,createdTime,modifiedTime,parents"):
        return self._call("GET", API + "/files/" + file_id, params={"fields": fields, "supportsAllDrives": "true"}).json()

    def text(self, file_id):
        return self._call("GET", API + "/files/" + file_id, params={"alt": "media", "supportsAllDrives": "true"}).text

    def put_text(self, file_id, text, mime="application/json"):
        self._call("PATCH", "https://www.googleapis.com/upload/drive/v3/files/" + file_id,
                   params={"uploadType": "media", "supportsAllDrives": "true"}, data=text.encode("utf-8"),
                   headers={"Content-Type": mime})

    def download(self, file_id, dest, size=0, note=None):
        """Streams to dest (via dest.part); checks the size when known. Returns dest."""
        part = dest + ".part"
        url = API + "/files/" + file_id
        if self.feed and time.time() - self.at > 30 * 60:
            self.refresh()                               # a big file outlives a stale token
        with requests.get(url, params={"alt": "media", "supportsAllDrives": "true"}, stream=True, timeout=600,
                          headers={"Authorization": "Bearer " + self.token}) as r:
            if r.status_code == 401 and self.feed:
                self.refresh()
                return self.download(file_id, dest, size, note)
            r.raise_for_status()
            got, last = 0, time.time()
            with open(part, "wb") as f:
                for chunk in r.iter_content(8 << 20):
                    f.write(chunk)
                    got += len(chunk)
                    if note and time.time() - last > 30:
                        note("downloading %s: %.0f of %.0f MB" % (os.path.basename(dest), got / 1e6, size / 1e6))
                        last = time.time()
        if size and os.path.getsize(part) != size:
            os.remove(part)
            raise RuntimeError("download of %s stopped at %d of %d bytes" % (dest, got, size))
        os.replace(part, dest)
        return dest

    def folder(self, parent, name):
        """The child folder `name` of parent, made when missing."""
        for f in self.children(parent, folders_only=True):
            if f["name"] == name:
                return f["id"]
        body = {"name": name, "mimeType": FOLDER, "parents": [parent]}
        return self._call("POST", API + "/files", params={"supportsAllDrives": "true", "fields": "id"}, json=body).json()["id"]

    def move(self, file_id, new_parent):
        old = ",".join(self.get(file_id, "parents").get("parents") or [])
        self._call("PATCH", API + "/files/" + file_id, params={"addParents": new_parent, "removeParents": old,
                                                               "supportsAllDrives": "true", "fields": "id,parents"}, json={})


def dumps(o):
    return json.dumps(o, indent=2, ensure_ascii=False)
