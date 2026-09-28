"""The local factory app: http://localhost:8042 (start it with run.cmd).

Shows every talk of an event with its steps, starts / retries runs (each run is its own background process, so
closing the browser never stops it), edits settings.yml, opens the output folder, and publishes a small status file
for the unlisted conf42.com/factory page.
"""
import datetime
import html
import json
import os
import shutil
import subprocess
import sys
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

import yaml

from . import events, pipeline
from .descript import Descript

PORT = 8042
PY = sys.executable
HERE = pipeline.HERE


def work_root():
    return os.path.join(pipeline.desktop(), pipeline.settings()["work_folder"])


def state_of(short_url):
    p = os.path.join(work_root(), short_url, "state.json")
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def event_list():
    today = datetime.date.today().isoformat()
    out = []
    for e in events.all_events():
        date = str(e.get("date", ""))
        started = os.path.exists(os.path.join(work_root(), e["short_url"], "state.json"))
        if started or date >= str(datetime.date.today().replace(year=datetime.date.today().year - 1)):
            out.append({"short_url": e["short_url"], "title": "Conf42 %s %s" % (e["name"], date[:4]), "date": date,
                        "started": started})
    return sorted(out, key=lambda x: (not x["started"], x["date"] < today, x["date"]))


_cache, _cache_lock = {}, threading.Lock()


def cached(key, seconds, fn):
    """Descript is asked at most every `seconds` however many browser tabs poll (it rate-limits with 429)."""
    with _cache_lock:
        hit = _cache.get(key)
        if hit and time.time() - hit[0] < seconds:
            return hit[1]
    try:
        val = fn()
    except Exception as ex:
        val = {"error": str(ex)[:300]}
    with _cache_lock:
        _cache[key] = (time.time(), val)
    return val


def runners(short_url):
    """Background factory processes for this event (python -m factory run|retry <short_url>), found by command line."""
    if os.name != "nt":
        return []
    ps = ("Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
          "Where-Object { $_.CommandLine -match '-m factory (run|retry) %s' } | "
          "ForEach-Object { '{0}|{1}|{2}' -f $_.ProcessId, $_.ParentProcessId, $_.CreationDate.ToString('s') }" % short_url)
    out = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True).stdout
    rows = [l.split("|") for l in out.split() if l.count("|") == 2]
    pids = {r[0] for r in rows}
    return [{"pid": int(r[0]), "since": r[2]} for r in rows if r[1] not in pids]   # the venv launcher's child is the same run


def descript_now(short_url):
    """What Descript is doing for this event's project right now: the job list, mapped to talk names."""
    st = state_of(short_url) or {}
    pid = st.get("project_id")
    if not pid:
        return {"jobs": [], "note": "no Descript project yet"}
    talks = st.get("talks", {})
    names = {t.get("composition_id"): k for k, t in talks.items() if t.get("composition_id")}
    by_job = {(t["steps"].get(s) or {}).get("job_id"): k for k, t in talks.items() for s in ("edit", "publish")}
    active = lambda step: [k for k, t in talks.items() if t.get("current") == step and not t.get("error")
                           and (t["steps"].get(step) or {}).get("status") == "running"
                           and not str((t["steps"].get(step) or {}).get("label", "")).startswith("Descript is busy")]
    uploading = active("upload")
    d = Descript()
    jobs = []
    for j in d.json("GET", "/jobs", params={"project_id": pid, "limit": 30}).get("data", []):
        pr, res = j.get("progress") or {}, j.get("result") or {}
        cid = pr.get("composition_id") or res.get("composition_id") or j.get("composition_id")
        kind = {"import/project_media": "upload", "agent": "edit", "publish": "publish"}.get(j.get("job_type"), j.get("job_type"))
        created = j.get("created_at", "")
        age_min = ((datetime.datetime.now(datetime.timezone.utc) -
                    datetime.datetime.fromisoformat(created.replace("Z", "+00:00"))).total_seconds() / 60) if created else 0
        state = j.get("job_state")
        note = pr.get("label", "") if state == "running" else res.get("status", "")
        if state == "running" and pr.get("waiting_for_uploads") and age_min > 60:
            state, note = "stale", "upload never arrived (left over from a stopped run); it blocks the project until the next run cancels it"
        talk = names.get(cid) or by_job.get(j.get("job_id")) or ""
        if not talk and kind == "upload":                                # finished imports name their composition
            talk = ", ".join(c.get("name", "") for c in res.get("created_compositions") or [])
        if not talk and state == "running" and kind in ("upload", "edit"):  # one job per project: it's the active talk
            talk = " / ".join(uploading if kind == "upload" else active("edit"))
        jobs.append({"talk": talk, "job": kind, "state": state, "note": note,
                     "percent": pr.get("percent"), "minutes": round(age_min)})
    comps = d.project(pid).get("compositions", [])
    return {"jobs": jobs, "project_url": "https://web.descript.com/" + pid, "compositions": len(comps),
            "uploading_now": uploading}


def spawn(args, short_url):
    log = open(os.path.join(work_root(), short_url, "run.log"), "a", encoding="utf-8")
    flags = 0x00000008 | 0x00000200 if os.name == "nt" else 0          # DETACHED_PROCESS | NEW_PROCESS_GROUP
    subprocess.Popen([PY, "-m", "factory"] + args, cwd=HERE, stdout=log, stderr=subprocess.STDOUT,
                     creationflags=flags, env={**os.environ, "PYTHONUTF8": "1"})


def publish_status():
    """Write src/_db/factory.json (no links, no tokens) for the unlisted conf42.com/factory page and push it."""
    data = {"updated": datetime.datetime.now().isoformat(timespec="seconds"), "events": []}
    for e in event_list():
        st = state_of(e["short_url"])
        if not st:
            continue
        talks = []
        for k, t in sorted(st["talks"].items()):
            qa = (t["steps"].get("qa") or {})
            talks.append({"speakers": k, "title": t.get("title", ""),
                          "steps": {s: (t["steps"].get(s) or {}).get("status", "") for s in pipeline.STEPS},
                          "finished": t.get("finished", ""), "error": bool(t.get("error")),
                          "minutes": qa.get("minutes_after"), "cut_percent": qa.get("cut_percent"),
                          "lufs": qa.get("lufs"), "flags": qa.get("flags", [])})
        data["events"].append({"short_url": e["short_url"], "title": e["title"], "talks": talks,
                               "missing_videos": pipeline.summary(st)["missing_videos"]})
    repo = events.REPO
    path = os.path.join(repo, "_db", "factory.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    git_exe = shutil.which("git") or r"C:\Program Files\Git\cmd\git.exe"   # detached runs have no git on PATH
    git = lambda *a: subprocess.run([git_exe, "-C", repo] + list(a), capture_output=True, text=True)
    git("add", "_db/factory.json")
    if git("diff", "--cached", "--quiet").returncode == 0:
        return "nothing changed"
    git("commit", "-m", "factory status update")
    git("pull", "--rebase", "-q")
    r = git("push", "-q")
    return "pushed" if r.returncode == 0 else "commit made, push failed: " + r.stderr[-200:]


PAGE_FILE = os.path.join(os.path.dirname(__file__), "dashboard.html")

# Expected seconds per step = a + b * video minutes + c * MB, then scaled by how long finished steps really took
# (median ratio, so the bars learn this PC's upload speed and Descript's pace). Seeds from 2026-09-28 Descript jobs.
DEFAULT_SECS = {"render": (5, 4, 0), "upload": (70, 0, 0.25), "edit": (75, 0, 0), "publish": (40, 14, 0),
                "download": (10, 0, 0.05), "srt": (8, 0, 0), "loudness": (5, 2.5, 0), "qa": (3, 1.2, 0)}


def expectations(st):
    talks = st.get("talks", {})
    def base(step, t):
        a, b, c = DEFAULT_SECS.get(step, (60, 0, 0))
        minutes = ((t.get("probe") or {}).get("duration") or 0) / 60 or 20
        return a + b * minutes + c * (t.get("size_mb") or 500)
    out = {}
    for step in pipeline.STEPS:
        ratios = sorted((t["steps"][step]["took"] / base(step, t)) for t in talks.values()
                        if (t["steps"].get(step) or {}).get("took"))
        f = min(6, max(0.25, ratios[len(ratios) // 2])) if ratios else 1
        for k, t in talks.items():
            out.setdefault(k, {})[step] = round(base(step, t) * f)
    return out


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, code, body, ctype="application/json"):
        b = body.encode("utf-8") if isinstance(body, str) else json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)
        if u.path == "/":
            with open(PAGE_FILE, encoding="utf-8") as f:
                return self.send(200, f.read().replace("__STEPS__", json.dumps(pipeline.STEPS)), "text/html")
        if u.path == "/api/events":
            return self.send(200, event_list())
        if u.path == "/api/state":
            st = state_of((q.get("e") or [""])[0])
            if not st:
                return self.send(200, {"state": None})
            ev = next((x for x in event_list() if x["short_url"] == st["event"]["short_url"]), {})
            return self.send(200, {"state": st, "summary": pipeline.summary(st), "expect": expectations(st),
                                   "title": ev.get("title", ""), "parallel": pipeline.settings().get("parallel_talks", 2)})
        if u.path == "/api/now":
            e = (q.get("e") or [""])[0]
            st = state_of(e) or {}
            ledger = {}
            try:
                with open(os.path.join(work_root(), "ledger.json"), encoding="utf-8") as f:
                    ledger = json.load(f)
            except (OSError, ValueError):
                pass
            mine = [v for v in ledger.values() if v.get("event") == e]
            queue = sorted(({"talk": k, "mb": t.get("size_mb"), "n": t["queued"]} for k, t in st.get("talks", {}).items()
                            if t.get("queued")), key=lambda x: x["n"])
            return self.send(200, {"queue": queue, "runners": cached("run:" + e, 10, lambda: runners(e)),
                                   "heartbeat": (st.get("runner") or {}).get("at") or st.get("updated"),
                                   "descript": cached("d:" + e, 20, lambda: descript_now(e)),
                                   "edits": len(mine),
                                   "credits": round(sum(float(v.get("credits") or 0) for v in mine), 1)})
        if u.path == "/api/settings":
            with open(os.path.join(HERE, "settings.yml"), encoding="utf-8") as f:
                return self.send(200, {"yaml": f.read()})
        self.send(404, {"msg": "not found"})

    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        body = json.loads(self.rfile.read(n) or b"{}")
        e = body.get("e", "")
        try:
            if self.path == "/api/start":
                os.makedirs(os.path.join(work_root(), e), exist_ok=True)
                spawn(["run", e], e)
                return self.send(200, {"msg": "started - progress below updates every 5 s"})
            if self.path == "/api/retry":
                spawn(["retry", e, body["speakers"]], e)
                return self.send(200, {"msg": "retrying " + body["speakers"]})
            if self.path == "/api/open":
                os.startfile(os.path.join(work_root(), e))
                return self.send(200, {"msg": ""})
            if self.path == "/api/publish":
                return self.send(200, {"msg": publish_status()})
            if self.path == "/api/settings":
                yaml.safe_load(body["yaml"])                       # refuse broken YAML
                with open(os.path.join(HERE, "settings.yml"), "w", encoding="utf-8") as f:
                    f.write(body["yaml"])
                return self.send(200, {"msg": "settings saved - the next run uses them"})
        except Exception as ex:
            return self.send(200, {"msg": "error: %s" % html.escape(str(ex))})
        self.send(404, {"msg": "not found"})


def serve():
    url = "http://localhost:%d" % PORT
    try:
        srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    except OSError:                                  # already running (another run.cmd): just show it
        webbrowser.open(url)
        return
    print("factory app on " + url)
    webbrowser.open(url)
    srv.serve_forever()
