"""The local factory app: http://localhost:8042 (start it with run.cmd).

Shows every talk of an event with its steps, starts / retries runs (each run is its own background process, so
closing the browser never stops it), edits settings.yml, opens the output folder, and publishes a small status file
for the unlisted conf42.com/factory page.
"""
import datetime
import html
import json
import os
import subprocess
import sys
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

import yaml

from . import events, pipeline

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
    git = lambda *a: subprocess.run(["git", "-C", repo] + list(a), capture_output=True, text=True)
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
</style></head><body>
<h1>Conf42 factory</h1><div class="sub">Conf42 talk videos: Drive download &rarr; Descript &rarr; finished MP4 + SRT on the Desktop</div>
<div class="bar"><select id="ev"></select>
<button class="go" onclick="post('start')">Start / resume</button>
<button onclick="post('open')">Open output folder</button>
<button onclick="post('publish')">Publish status to conf42.com/factory</button>
<button onclick="toggle('set')">Settings</button><span id="msg"></span></div>
<div id="sum" class="box"></div>
<table><thead><tr><th>Talk</th><th>Upload</th><th>Edit</th><th>Publish</th><th>Download</th><th>SRT</th><th>Loudness</th><th>QA</th><th></th></tr></thead><tbody id="rows"></tbody></table>
<div id="set" class="box" style="display:none"><b>settings.yml</b><textarea id="yml"></textarea><br><button class="go" onclick="saveSet()">Save settings</button></div>
<div class="box"><b>Log</b><pre id="log"></pre></div>
<script>
const $=id=>document.getElementById(id), steps=__STEPS__;
async function j(u,o){const r=await fetch(u,o);return r.json()}
async function load(){const es=await j('/api/events');$('ev').innerHTML=es.map(e=>`<option value="${e.short_url}">${e.title} (${e.date})${e.started?' - started':''}</option>`).join('');$('ev').onchange=refresh;refresh()}
async function refresh(){const d=await j('/api/state?e='+$('ev').value);
 if(!d.state){$('sum').innerHTML='Not started. Put the Drive zips on the Desktop (or ask Claude), then press Start.';$('rows').innerHTML='';$('log').textContent='';return}
 const s=d.summary;$('sum').innerHTML=`<b>${s.finished.length}</b> of <b>${s.matched}</b> videos finished &middot; ${s.in_csv} talks in the CSV`+
 (s.unmatched.length?`<div class=warn>Not matched: ${s.unmatched.map(u=>u.file+' ('+u.why+')').join('; ')}</div>`:'')+
 (s.missing_videos.length?`<div>No video yet: ${s.missing_videos.join(', ')}</div>`:'')+
 (Object.keys(s.flagged).length?`<div class=warn>QA flags: ${Object.entries(s.flagged).map(([k,v])=>k+': '+v.join(', ')).join('; ')}</div>`:'');
 $('rows').innerHTML=Object.entries(d.state.talks).sort().map(([k,t])=>'<tr><td><b>'+k+'</b><br><small>'+(t.title||'')+'</small>'+(t.error?'<div class=warn><small>'+t.error+'</small></div>':'')+'</td>'+
  steps.map(st=>{const x=t.steps[st]||{};const c=x.status||'todo';return '<td><span class="s '+c+'" title="'+(x.label||x.error||'')+'">'+(c=='todo'?'-':c)+'</span></td>'}).join('')+
  '<td>'+(t.error?`<button onclick="retry('${k.replace(/'/g,"\\\\'")}')">Retry</button>`:'')+'</td></tr>').join('');
 $('log').textContent=(d.state.log||[]).slice(-40).reverse().join('\\n')}
async function post(a){const r=await j('/api/'+a,{method:'POST',body:JSON.stringify({e:$('ev').value})});$('msg').textContent=r.msg||'';setTimeout(refresh,1500)}
async function retry(k){const r=await j('/api/retry',{method:'POST',body:JSON.stringify({e:$('ev').value,speakers:k})});$('msg').textContent=r.msg}
async function toggle(id){const b=$(id);b.style.display=b.style.display=='none'?'block':'none';if(id=='set')$('yml').value=(await j('/api/settings')).yaml}
async function saveSet(){const r=await j('/api/settings',{method:'POST',body:JSON.stringify({yaml:$('yml').value})});$('msg').textContent=r.msg}
load();setInterval(refresh,5000);
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
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = "http://localhost:%d" % PORT
    print("factory app on " + url)
    webbrowser.open(url)
    srv.serve_forever()
