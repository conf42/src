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


PAGE = """<!doctype html><html><head><meta charset="utf-8"><title>Conf42 factory</title>
<style>
body{font-family:Segoe UI,Arial,sans-serif;margin:24px;color:#1a1a2e;background:#f6f7fb}
h1{margin:0 0 4px;font-size:22px} .sub{color:#666;margin-bottom:18px}
select,button,textarea,input{font:inherit} button{padding:7px 14px;border-radius:8px;border:1px solid #bbb;background:#fff;cursor:pointer}
button.go{background:#6b40d8;color:#fff;border-color:#6b40d8} .bar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:10px 0 18px}
table{border-collapse:collapse;width:100%;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 1px 4px rgba(0,0,0,.06)}
th,td{padding:8px 10px;border-bottom:1px solid #eee;text-align:left;font-size:14px;vertical-align:top}
th{background:#f0edfb;font-weight:600} .s{display:inline-block;min-width:74px;padding:2px 8px;border-radius:999px;font-size:12px;text-align:center}
.done{background:#dff5e6;color:#17693a}.running{background:#fff3cd;color:#8a6100}.failed{background:#fde2e1;color:#a4231c}.todo{background:#eee;color:#888}
.box{background:#fff;border-radius:10px;padding:12px 16px;margin:14px 0;box-shadow:0 1px 4px rgba(0,0,0,.06)} .warn{color:#a4231c}
pre{white-space:pre-wrap;font-size:12px;max-height:220px;overflow:auto;background:#fafafa;padding:8px;border-radius:6px}
textarea{width:100%;height:320px;font-family:Consolas,monospace;font-size:13px}
.mut{color:#888} .dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:middle}
.on{background:#22a355;box-shadow:0 0 0 4px rgba(34,163,85,.18);animation:pulse 1.6s infinite} .off{background:#bbb}
@keyframes pulse{50%{box-shadow:0 0 0 7px rgba(34,163,85,.05)}}
.pbar{height:8px;background:#eee;border-radius:9px;overflow:hidden;min-width:120px;margin-bottom:2px} .pbar i{display:block;height:100%;background:#6b40d8}
.lbl{display:block;font-size:11px;color:#8a6100;margin-top:3px;max-width:150px} .stale{background:#eee;color:#888}
#now table{box-shadow:none;margin-top:8px} #now td,#now th{font-size:13px;padding:6px 8px}
</style></head><body>
<h1>Conf42 factory</h1><div class="sub">Conf42 talk videos: Drive download &rarr; Descript &rarr; finished MP4 + SRT on the Desktop</div>
<div class="bar"><select id="ev"></select>
<button class="go" onclick="post('start')">Start / resume</button>
<button onclick="post('open')">Open output folder</button>
<button onclick="post('publish')">Publish status to conf42.com/factory</button>
<button onclick="toggle('set')">Settings</button><span id="msg"></span></div>
<div id="now" class="box"><b>Right now</b> <small class="mut">checking...</small></div>
<div id="sum" class="box"></div>
<table><thead><tr><th>Talk</th><th>Upload</th><th>Edit</th><th>Publish</th><th>Download</th><th>SRT</th><th>Loudness</th><th>QA</th><th></th></tr></thead><tbody id="rows"></tbody></table>
<div id="set" class="box" style="display:none"><b>settings.yml</b><textarea id="yml"></textarea><br><button class="go" onclick="saveSet()">Save settings</button></div>
<div class="box"><b>Log</b><pre id="log"></pre></div>
<script>
const $=id=>document.getElementById(id), steps=__STEPS__;
async function j(u,o){const r=await fetch(u,o);return r.json()}
async function load(){const es=await j('/api/events');$('ev').innerHTML=es.map(e=>`<option value="${e.short_url}">${e.title} (${e.date})${e.started?' - started':''}</option>`).join('');$('ev').onchange=()=>{refresh();now()};refresh()}
async function refresh(){const d=await j('/api/state?e='+$('ev').value);
 if(!d.state){$('sum').innerHTML='Not started. Put the Drive zips on the Desktop (or ask Claude), then press Start.';$('rows').innerHTML='';$('log').textContent='';return}
 const s=d.summary;$('sum').innerHTML=`<b>${s.finished.length}</b> of <b>${s.matched}</b> videos finished &middot; ${s.in_csv} talks in the CSV`+
 (s.unmatched.length?`<div class=warn>Not matched: ${s.unmatched.map(u=>u.file+' ('+u.why+')').join('; ')}</div>`:'')+
 (s.missing_videos.length?`<div>No video yet: ${s.missing_videos.join(', ')}</div>`:'')+
 (Object.keys(s.flagged).length?`<div class=warn>QA flags: ${Object.entries(s.flagged).map(([k,v])=>k+': '+v.join(', ')).join('; ')}</div>`:'');
 $('rows').innerHTML=Object.entries(d.state.talks).sort().map(([k,t])=>'<tr><td><b>'+k+'</b><br><small>'+(t.title||'')+'</small>'+(t.error?'<div class=warn><small>'+t.error+'</small></div>':'')+'</td>'+
  steps.map(st=>{const x=t.steps[st]||{};const c=x.status||'todo';return '<td><span class="s '+c+'" title="'+(x.label||x.error||'')+'">'+(c=='todo'?'-':c)+'</span>'+(c=='running'&&x.label?'<span class=lbl>'+x.label+'</span>':'')+'</td>'}).join('')+
  '<td>'+(t.error?`<button onclick="retry('${k.replace(/'/g,"\\\\'")}')">Retry</button>`:'')+'</td></tr>').join('');
 $('log').textContent=(d.state.log||[]).slice(-40).reverse().join('\\n')}
async function post(a){const r=await j('/api/'+a,{method:'POST',body:JSON.stringify({e:$('ev').value})});$('msg').textContent=r.msg||'';setTimeout(refresh,1500)}
async function retry(k){const r=await j('/api/retry',{method:'POST',body:JSON.stringify({e:$('ev').value,speakers:k})});$('msg').textContent=r.msg}
async function toggle(id){const b=$(id);b.style.display=b.style.display=='none'?'block':'none';if(id=='set')$('yml').value=(await j('/api/settings')).yaml}
async function saveSet(){const r=await j('/api/settings',{method:'POST',body:JSON.stringify({yaml:$('yml').value})});$('msg').textContent=r.msg}
function ago(iso){if(!iso)return '';const s=(Date.now()-new Date(iso))/1000;return s<90?Math.round(s)+' s ago':Math.round(s/60)+' min ago'}
function when(m){return m<90?m+' min ago':Math.round(m/60)+' h ago'}
function jrow(x,up){const cls=x.state=='running'?'running':x.state=='stale'?'stale':x.note=='success'?'done':'failed';
 const word=x.state=='stopped'?(x.note=='success'?'done':(x.note||'stopped')):x.state;
 const who=x.talk||'<span class=mut>-</span>';
 const prog=(x.state=='running'&&x.percent!=null?'<div class=pbar><i style="width:'+x.percent+'%"></i></div>'+x.percent+'% ':'')+(x.state=='running'||x.state=='stale'?x.note:'');
 return `<tr><td>${who}</td><td>${x.job}</td><td><span class="s ${cls}">${word}</span></td><td><small>${prog}</small></td><td><small>${when(x.minutes)}</small></td></tr>`}
async function now(){const e=$('ev').value;if(!e)return;const n=await j('/api/now?e='+e),d=n.descript||{},up=d.uploading_now||[];
 const run=n.runners&&n.runners.length?`<span class="dot on"></span><b>Factory is running</b> <span class=mut>(process ${n.runners.map(r=>r.pid).join(', ')}, started ${n.runners[0].since.replace('T',' ')}, last activity ${ago(n.heartbeat)})</span>`
  :`<span class="dot off"></span><b>Factory is not running</b> <span class=mut>(last activity ${ago(n.heartbeat)||'never'})</span>`;
 const jobs=d.jobs||[],running=jobs.filter(x=>x.state=='running'),rest=jobs.filter(x=>x.state!='running').slice(0,8);
 $('now').innerHTML=`<b>Right now</b><div style="margin:6px 0">${run}</div>`+(d.error?`<div class=warn>Descript did not answer: ${d.error}</div>`:
  `<div><b>Descript</b> <span class=mut>&middot; ${d.compositions||0} talks in the project &middot; ${n.edits} edits paid, about ${n.credits} AI credits</span>${d.project_url?` &middot; <a href="${d.project_url}" target=_blank>open the project in Descript</a>`:''}</div>`+
  (running.length?'':'<div class=mut style="margin-top:6px">No Descript job running at this moment (the factory may be uploading, downloading or measuring loudness).</div>')+
  '<div class=mut style="margin-top:4px"><small>Descript runs one job per project at a time, so talks take turns: a talk showing "Descript is busy" is waiting in line, not stuck.</small></div>'+
  `<table><thead><tr><th>Talk</th><th>Job</th><th>State</th><th>Progress</th><th>Started</th></tr></thead><tbody>${running.map(x=>jrow(x,up)).join('')}`+
  (rest.length?'<tr><td colspan=5 class=mut>recently finished</td></tr>'+rest.map(x=>jrow(x,[])).join(''):'')+'</tbody></table>')}
load().then(()=>{now();setInterval(now,20000)});setInterval(refresh,5000);
</script></body></html>"""


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
            return self.send(200, PAGE.replace("__STEPS__", json.dumps(pipeline.STEPS)), "text/html")
        if u.path == "/api/events":
            return self.send(200, event_list())
        if u.path == "/api/state":
            st = state_of((q.get("e") or [""])[0])
            return self.send(200, {"state": st, "summary": pipeline.summary(st) if st else None})
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
            return self.send(200, {"runners": cached("run:" + e, 10, lambda: runners(e)),
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
