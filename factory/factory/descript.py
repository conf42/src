"""Thin client for the Descript API (https://docs.descriptapi.com, open beta since May 2026).

The token is read from the DESCRIPT_API_TOKEN environment variable (Windows user variable) and is never
written anywhere by the factory. Every call returns parsed JSON; jobs are polled until they stop.
"""
import os
import subprocess
import time

import requests

BASE = "https://descriptapi.com/v1"


def token():
    t = os.environ.get("DESCRIPT_API_TOKEN", "")
    if not t and os.name == "nt":   # a fresh `setx` is not visible to already-open shells: read the registry value
        t = subprocess.run(["powershell", "-NoProfile", "-Command",
                            "[Environment]::GetEnvironmentVariable('DESCRIPT_API_TOKEN','User')"],
                           capture_output=True, text=True).stdout.strip()
    if not t:
        raise RuntimeError("DESCRIPT_API_TOKEN is not set (Descript > Settings > API tokens)")
    return t


class Descript:
    def __init__(self):
        self.s = requests.Session()
        self.s.headers["Authorization"] = "Bearer " + token()

    def call(self, method, path, **kw):
        waited = 0
        for attempt in range(1000):
            r = self.s.request(method, BASE + path, timeout=120, **kw)
            if r.status_code == 429 and waited < 3600:                   # too many jobs at once: queue politely
                pause = max(int(float(r.headers.get("Retry-After", 0) or 0)), 30)
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
        j = self.json("POST", "/jobs/import/project_media", json=body)
        url = j["upload_urls"][key]["upload_url"]
        with open(path, "rb") as f:
            r = requests.put(url, data=f, headers={"Content-Type": "application/octet-stream"}, timeout=6 * 3600)
        if r.status_code >= 300:
            raise RuntimeError("upload of %s failed: %s %s" % (key, r.status_code, r.text[:200]))
        done = self.wait(j["job_id"], 10, on_progress)
        comps = done["result"].get("created_compositions") or []
        return done["project_id"], comps[0]["id"], done

    def edit(self, project_id, composition_id, prompt, on_progress=None):
        j = self.json("POST", "/jobs/agent", json={"project_id": project_id, "composition_id": composition_id, "prompt": prompt})
        return self.wait(j["job_id"], 20, on_progress)

    def publish(self, project_id, composition_id, resolution, access, on_progress=None):
        j = self.json("POST", "/jobs/publish", json={"project_id": project_id, "composition_id": composition_id,
                                                      "media_type": "Video", "resolution": resolution, "access_level": access})
        return self.wait(j["job_id"], 20, on_progress)

    def srt(self, project_id, composition_id):
        return self.call("POST", "/export/transcript", json={"project_id": project_id, "composition_id": composition_id,
                                                             "format": "srt", "include_speaker_labels": "off"}).content
