"""Thin client for the Descript API (https://docs.descriptapi.com, open beta since May 2026).

The token is read from the DESCRIPT_API_TOKEN environment variable (Windows user variable) and is never
written anywhere by the factory. Every call returns parsed JSON; jobs are polled until they stop.
"""
import os
import subprocess
import datetime
import time

import requests

BASE = "https://descriptapi.com/v1"
LIVE_UPLOADS = set()     # import jobs this process is uploading to right now; any other waiting import is an orphan


def token():
    t = os.environ.get("DESCRIPT_API_TOKEN", "")
    if not t and os.name == "nt":   # a fresh `setx` is not visible to already-open shells: read the registry value
        t = subprocess.run(["powershell", "-NoProfile", "-Command",
                            "[Environment]::GetEnvironmentVariable('DESCRIPT_API_TOKEN','User')"],
                           capture_output=True, text=True).stdout.strip()
    if not t:
        raise RuntimeError("DESCRIPT_API_TOKEN is not set (Descript > Settings > API tokens)")
    return t


class _Progress:
    """File wrapper for the upload PUT: reports 'uploading 45% of 1.2 GB' every few seconds."""
    def __init__(self, f, size, on_progress):
        self.f, self.size, self.cb, self.sent, self.last = f, size, on_progress, 0, 0

    def __len__(self):
        return self.size

    def read(self, n=-1):
        chunk = self.f.read(n if n and n > 0 else 1024 * 1024)
        self.sent += len(chunk)
        if self.cb and (time.time() - self.last > 5 or self.sent >= self.size):
            self.last = time.time()
            self.cb("uploading %d%% of %.1f GB" % (100 * self.sent // max(self.size, 1), self.size / 1e9))
        return chunk


class Descript:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers["Authorization"] = "Bearer " + token()
        self.on_wait = None                          # set per request: shows "Descript busy" waits in the app

    def call(self, method, path, **kw):
        waited = 0
        for attempt in range(1000):
            r = self.s.request(method, BASE + path, timeout=120, **kw)
            if r.status_code == 429 and waited < 3600:                   # too many jobs at once: queue politely
                pause = max(int(float(r.headers.get("Retry-After", 0) or 0)), 30)
                if waited == 0:
                    print("Descript 429 on %s %s: %s" % (method, path, r.text[:200]), flush=True)
                if self.on_wait:
                    self.on_wait("Descript is busy (too many jobs at once), waiting in line - %d min so far" % (waited // 60))
                pid = (kw.get("json") or {}).get("project_id")
                if pid and waited and waited % 120 < pause:     # every ~2 min in line: is the line blocked by an orphan?
                    try:
                        gone = self.cancel_orphan_uploads(pid)
                        if gone:
                            print("cancelled %d orphan Descript upload(s) blocking the project" % len(gone), flush=True)
                    except Exception as ex:
                        print("orphan check failed: %s" % ex, flush=True)
                time.sleep(pause)
                waited += pause
                continue
            if r.status_code >= 500 and attempt < 6:                     # hiccup on Descript's side
                time.sleep(10 * (attempt + 1))
                continue
            if r.status_code == 402:
                raise RuntimeError("Descript says the plan is out of media minutes or AI credits (402)")
            if r.status_code >= 400:
                raise RuntimeError("Descript %s %s -> %s %s" % (method, path, r.status_code, r.text[:400]))
            return r
        raise RuntimeError("Descript %s %s kept failing (%s)" % (method, path, r.status_code))

    def json(self, method, path, **kw):
        return self.call(method, path, **kw).json()

    def wait(self, job_id, every=15, on_progress=None):
        while True:
            j = self.json("GET", "/jobs/" + job_id)
            if j.get("job_state") != "running":
                res = j.get("result") or {}
                if res.get("status") != "success":
                    raise RuntimeError("Descript job %s failed: %s" % (job_id, str(res)[:400]))
                return j
            if on_progress and j.get("progress"):
                on_progress(j["progress"].get("label", ""))
            time.sleep(every)

    # ---- the calls the factory uses -------------------------------------------------------
    def find_project(self, name):
        for p in self.json("GET", "/projects", params={"name": name, "limit": 100}).get("data", []):
            if p.get("name") == name:
                return p["id"]
        return None

    def cancel_orphan_uploads(self, project_id):
        """Descript runs ONE job per project at a time. An import whose file never arrives (its run was stopped, or
        Descript created the job but answered with an error so the file was never sent) waits forever and blocks
        every later job (429 "A job is already running for this project") - cancel those. Imports this process is
        uploading to (LIVE_UPLOADS) and ones younger than 2 minutes are left alone."""
        gone, now = [], datetime.datetime.now(datetime.timezone.utc)
        for j in self.json("GET", "/jobs", params={"project_id": project_id, "limit": 50}).get("data", []):
            created = j.get("created_at") or ""
            age = (now - datetime.datetime.fromisoformat(created.replace("Z", "+00:00"))).total_seconds() if created else 1e9
            if (j.get("job_state") == "running" and (j.get("progress") or {}).get("waiting_for_uploads")
                    and j["job_id"] not in LIVE_UPLOADS and age > 120):
                self.call("DELETE", "/jobs/" + j["job_id"])
                gone.append(j["job_id"])
        return gone

    def project(self, project_id):
        return self.json("GET", "/projects/" + project_id)

    def import_file(self, path, key, project_id=None, project_name=None, on_progress=None):
        """Upload one local video as its own composition; returns (project_id, composition_id, job)."""
        size = os.path.getsize(path)
        ctype = "video/quicktime" if path.lower().endswith(".mov") else "video/mp4"
        body = {"add_media": {key: {"content_type": ctype, "file_size": size}},
                "add_compositions": [{"name": key, "clips": [{"media": key}]}]}
        if project_id:
            body["project_id"] = project_id
        else:
            body["project_name"] = project_name
        self.on_wait = on_progress
        j = self.json("POST", "/jobs/import/project_media", json=body)
        url = j["upload_urls"][key]["upload_url"]
        LIVE_UPLOADS.add(j["job_id"])
        try:
            with open(path, "rb") as f:
                r = requests.put(url, data=_Progress(f, size, on_progress),
                                 headers={"Content-Type": "application/octet-stream"}, timeout=6 * 3600)
            if r.status_code >= 300:
                raise RuntimeError("upload of %s failed: %s %s" % (key, r.status_code, r.text[:200]))
        finally:
            LIVE_UPLOADS.discard(j["job_id"])
        done = self.wait(j["job_id"], 10, on_progress)
        comps = done["result"].get("created_compositions") or []
        return done["project_id"], comps[0]["id"], done

    def edit(self, project_id, composition_id, prompt, on_progress=None):
        self.on_wait = on_progress
        j = self.json("POST", "/jobs/agent", json={"project_id": project_id, "composition_id": composition_id, "prompt": prompt})
        return self.wait(j["job_id"], 20, on_progress)

    def publish(self, project_id, composition_id, resolution, access, on_progress=None):
        self.on_wait = on_progress
        j = self.json("POST", "/jobs/publish", json={"project_id": project_id, "composition_id": composition_id,
                                                      "media_type": "Video", "resolution": resolution, "access_level": access})
        return self.wait(j["job_id"], 20, on_progress)

    def srt(self, project_id, composition_id):
        return self.call("POST", "/export/transcript", json={"project_id": project_id, "composition_id": composition_id,
                                                             "format": "srt", "include_speaker_labels": "off"}).content
