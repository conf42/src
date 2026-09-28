"""The factory pipeline: Drive download -> Descript -> finished MP4 + SRT on the Desktop.

One state file per event (Desktop/<work_folder>/<short_url>/state.json) records every step of every talk, so a run
can be stopped and restarted at any time: finished steps are skipped and a failed talk is retried on its own.

Steps per talk: match -> probe -> upload -> edit -> publish -> download -> srt -> loudness -> qa
"""
import datetime
import glob
import json
import os
import shutil
import threading
import time
import traceback
import zipfile
from concurrent.futures import ThreadPoolExecutor

import requests
import yaml

from . import events, media
from . import slides as slides_mod
from .descript import Descript

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIDEO_EXT = (".mp4", ".mov", ".m4v", ".mkv", ".webm", ".avi")
SLIDE_EXT = (".pdf", ".pptx", ".ppt", ".key", ".odp")
STEPS = ["upload", "edit", "publish", "download", "srt", "loudness", "qa"]


def settings():
    with open(os.path.join(HERE, "settings.yml"), encoding="utf-8") as f:
        return yaml.safe_load(f)


def desktop():
    return os.path.join(os.path.expanduser("~"), "Desktop")


def now():
    return datetime.datetime.now().isoformat(timespec="seconds")


class Run:
    def __init__(self, short_url):
        self.cfg = settings()
        self.ev = events.event(short_url)
        self.dir = os.path.join(desktop(), self.cfg["work_folder"], short_url)
        self.inp, self.out, self.srt_dir, self.slides_dir = (os.path.join(self.dir, d) for d in ("in", "out", "srt", "slides"))
        for d in (self.inp, self.out, self.srt_dir, self.slides_dir):
            os.makedirs(d, exist_ok=True)
        self.state_path = os.path.join(self.dir, "state.json")
        self.lock = threading.RLock()
        self.plock = threading.Lock()                 # only one talk creates the Descript project
        self.state = self._load()

    # ---- state ---------------------------------------------------------------------------
    def _load(self):
        if os.path.exists(self.state_path):
            with open(self.state_path, encoding="utf-8") as f:
                return json.load(f)
        return {"event": self.ev, "project_id": None, "talks": {}, "unmatched": [], "log": []}

    def save(self):
        with self.lock:
            self.state["updated"] = now()
            self.state["runner"] = {"pid": os.getpid(), "at": now()}      # heartbeat: the app shows whether a run is alive
            tmp = self.state_path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(self.state, f, indent=1, ensure_ascii=False)
            os.replace(tmp, self.state_path)

    def note(self, msg):
        with self.lock:
            self.state["log"] = (self.state["log"] + ["%s  %s" % (now(), msg)])[-200:]
            print(msg, flush=True)
            self.save()

    def talk(self, key):
        return self.state["talks"][key]

    def set(self, key, step, status, **extra):
        with self.lock:
            t = self.talk(key)
            t["steps"][step] = {"status": status, "at": now(), **extra}
            t["current"] = step if status == "running" else t.get("current")
            self.save()

    # ---- the ledger of paid Descript edits, shared by all events (Desktop/<work_folder>/ledger.json) ----------
    def ledger_path(self):
        return os.path.join(os.path.dirname(self.dir), "ledger.json")

    def ledger(self):
        try:
            with open(self.ledger_path(), encoding="utf-8") as f:
                return json.load(f)
        except (OSError, ValueError):
            return {}

    def record_edit(self, composition_id, key, credits):
        with self.lock:
            led = self.ledger()
            led[composition_id] = {"event": self.ev["short_url"], "speakers": key, "credits": credits, "at": now()}
            with open(self.ledger_path(), "w", encoding="utf-8") as f:
                json.dump(led, f, indent=1, ensure_ascii=False)

    # ---- 1. collect: unzip Drive downloads, split videos and slides ----------------------
    def collect(self, sources):
        for src in sources:
            files = []
            if os.path.isdir(src):
                files = [os.path.join(src, f) for f in os.listdir(src)]
            for z in (files if files else [src]):
                if z.lower().endswith(".zip"):
                    with zipfile.ZipFile(z) as zf:
                        for info in zf.infolist():
                            name = os.path.basename(info.filename)
                            if not name:
                                continue
                            dest = self.inp if name.lower().endswith(VIDEO_EXT) else self.slides_dir if name.lower().endswith(SLIDE_EXT) else None
                            if dest and not os.path.exists(os.path.join(dest, name)):
                                self.note("unzipping %s" % name)
                                with zf.open(info) as a, open(os.path.join(dest, name), "wb") as b:
                                    shutil.copyfileobj(a, b, 16 << 20)
                elif z.lower().endswith(VIDEO_EXT) and os.path.dirname(os.path.abspath(z)) != self.inp:
                    shutil.copy2(z, self.inp)

    # ---- 2. match: one video per talk, named after the speaker(s) exactly as on the site ---
    def match(self):
        talk_list = events.talks(self.ev)
        with self.lock:
            self.state["talks_in_csv"] = [t["speakers"] for t in talk_list]
            self.state["unmatched"] = []
            for path in sorted(glob.glob(os.path.join(self.inp, "*"))):
                if not path.lower().endswith(VIDEO_EXT):
                    continue
                if any(t["source"] == os.path.basename(path) for t in self.state["talks"].values()):
                    continue
                t, why = events.match(path, talk_list)
                if not t:
                    self.state["unmatched"].append({"file": os.path.basename(path), "why": why})
                    continue
                key = t["speakers"]
                if key in self.state["talks"]:
                    self.state["unmatched"].append({"file": os.path.basename(path), "why": "second video for %s" % key})
                    continue
                canonical = key + os.path.splitext(path)[1].lower()
                if os.path.basename(path) != canonical:
                    os.replace(path, os.path.join(self.inp, canonical))   # rename in place: the Desktop mirrors the site
                self.state["talks"][key] = {"speakers": key, "name1": t["name1"], "title": t["title"], "source": canonical,
                                            "matched": why, "steps": {}, "current": None, "error": None}
            self.save()

    def slides(self, talk_list=None):
        """Decks: match, one per talk, convert to PDF, rename for the site, compress under the limit (see slides.py).
        The report goes to slides.json (not state.json, so it never races a video run)."""
        rep = slides_mod.prepare(self.slides_dir, self.ev, talk_list or events.talks(self.ev),
                                 float(self.cfg.get("slides_max_mb", 5)))
        with open(os.path.join(self.dir, "slides.json"), "w", encoding="utf-8") as f:
            json.dump(rep, f, indent=1, ensure_ascii=False)
        return rep

    # ---- 3.-9. one talk through Descript and back ----------------------------------------
    def process(self, key):
        t, cfg, d = self.talk(key), self.cfg, Descript()
        done = lambda s: (t["steps"].get(s) or {}).get("status") == "done"
        src = os.path.join(self.inp, t["source"])
        final = os.path.join(self.out, "%s - %s.mp4" % (key, self.ev["title"]))
        raw = os.path.join(self.out, "_descript", key + ".mp4")
        srt_path = os.path.join(self.srt_dir, ("%s_%s.srt" % (self.ev["short_url"], t["name1"])).replace(" ", "_"))
        progress = lambda step: (lambda label: self.set(key, step, "running", label=label))
        try:
            with self.lock:
                t["error"] = None
            if "probe" not in t:
                t["probe"] = media.probe(src)
                t["resolution"] = media.pick_resolution(t["probe"]["width"], t["probe"]["height"], cfg["max_resolution"])
                self.save()
            # credit guard 1: a composition with this name already in the Descript project -> reuse it, never re-upload
            if not done("upload") and not self.state["project_id"]:
                with self.plock:
                    if not self.state["project_id"]:
                        self.state["project_id"] = d.find_project(cfg["project_name"].format(**self.ev))
            if not done("upload") and self.state["project_id"]:
                existing = {c["name"]: c for c in d.project(self.state["project_id"]).get("compositions", [])}
                if key in existing:
                    t["composition_id"] = existing[key]["id"]
                    self.set(key, "upload", "done", note="already in Descript, reused")
            if not done("upload"):
                self.set(key, "upload", "running", label="uploading %.0f MB" % (os.path.getsize(src) / 1e6))
                with self.plock:                                 # the first upload creates (or finds) the project
                    if not self.state["project_id"]:
                        self.state["project_id"] = d.find_project(cfg["project_name"].format(**self.ev))
                    if not self.state["project_id"]:
                        pid, cid, _ = d.import_file(src, key, project_name=cfg["project_name"].format(**self.ev),
                                                    on_progress=progress("upload"))
                        self.state["project_id"] = pid
                        self.save()
                        created = True
                    else:
                        created = False
                if created:
                    pass
                else:
                    pid, cid, _ = d.import_file(src, key, project_id=self.state["project_id"], on_progress=progress("upload"))
                t["composition_id"] = cid
                self.set(key, "upload", "done")
            pid, cid = self.state["project_id"], t["composition_id"]
            # credit guard 2: never pay for the same edit twice - the ledger of paid edits (survives a lost state file)
            # or a composition already shorter than its media (filler words / gaps were cut) means it's edited
            if not done("edit"):
                paid = self.ledger().get(cid)
                if not paid:
                    pr = d.project(pid)
                    comp = next((c for c in pr.get("compositions", []) if c["id"] == cid), {})
                    media_len = ((pr.get("media_files") or {}).get(key) or {}).get("duration") or 0
                    if comp and media_len and comp.get("duration", media_len) < media_len * 0.99:
                        paid = {"note": "composition already shorter than its media"}
                if paid:
                    self.set(key, "edit", "done", note="already edited in Descript, skipped (%s)" % (paid.get("note") or paid.get("at")))
            if not done("edit"):
                if self.state.get("edits_paused"):          # an earlier edit cost too much: no more paid edits this run
                    raise RuntimeError("edits paused: " + self.state["edits_paused"])
                self.set(key, "edit", "running")
                j = d.edit(pid, cid, cfg["edit_prompt"].format(composition=key, **cfg), on_progress=progress("edit"))
                credits = float(j["result"].get("ai_credits_used") or 0)
                self.record_edit(cid, key, credits)
                self.set(key, "edit", "done", report=j["result"].get("agent_response", ""), credits=credits, job_id=j.get("job_id"))
                cap = float(cfg.get("max_edit_credits") or 0)
                if cap and credits > cap:                   # e.g. the AI editor worked on the whole project
                    with self.lock:
                        self.state["edits_paused"] = "%s's edit cost %.1f AI credits (limit %g) - check it in Descript, then clear edits_paused in state.json" % (key, credits, cap)
                    self.note("EDITS PAUSED: " + self.state["edits_paused"])
            if not done("publish"):
                self.set(key, "publish", "running")
                j = d.publish(pid, cid, t["resolution"], cfg["publish_access"], on_progress=progress("publish"))
                self.set(key, "publish", "done", job_id=j.get("job_id"), share_url=j["result"].get("share_url"),
                         download_url=j["result"].get("download_url"), expires=j["result"].get("download_url_expires_at"))
            if not done("download"):
                self.set(key, "download", "running")
                os.makedirs(os.path.dirname(raw), exist_ok=True)
                with requests.get(t["steps"]["publish"]["download_url"], stream=True, timeout=600) as r:
                    r.raise_for_status()
                    with open(raw + ".part", "wb") as f:
                        for chunk in r.iter_content(16 << 20):
                            f.write(chunk)
                os.replace(raw + ".part", raw)
                self.set(key, "download", "done")
            if not done("srt"):
                self.set(key, "srt", "running")
                with open(srt_path, "wb") as f:
                    f.write(d.srt(pid, cid))
                self.set(key, "srt", "done", file=os.path.basename(srt_path))
            if not done("loudness"):
                self.set(key, "loudness", "running", label="ffmpeg to %s LUFS" % cfg["loudness_lufs"])
                media.normalize(raw, final, cfg["loudness_lufs"], cfg["true_peak_db"])
                self.set(key, "loudness", "done", file=os.path.basename(final))
            if not done("qa"):
                self.set(key, "qa", "running")
                lufs, peak = media.loudness(final)
                out = media.probe(final)
                cut = 100 * (1 - out["duration"] / t["probe"]["duration"]) if t["probe"]["duration"] else 0
                flags = []
                if lufs is None or abs(lufs - cfg["loudness_lufs"]) > cfg["qa_loudness_tolerance"]:
                    flags.append("loudness %s LUFS" % lufs)
                if cut > cfg["qa_max_cut_percent"]:
                    flags.append("edit removed %.0f%% of the talk" % cut)
                if out["height"] and t["probe"]["height"] and min(out["width"], out["height"]) < 480:
                    flags.append("low resolution")
                self.set(key, "qa", "done", lufs=lufs, peak=peak, minutes_before=round(t["probe"]["duration"] / 60, 1),
                         minutes_after=round(out["duration"] / 60, 1), cut_percent=round(cut, 1), flags=flags)
            with self.lock:
                t["current"] = None
                t["finished"] = now()
                self.save()
            self.note("done: %s" % key)
            self.publish()
        except Exception as ex:
            with self.lock:
                t["error"] = "%s: %s" % (t.get("current") or "?", ex)
                cur = t.get("current")
                if cur:
                    t["steps"][cur] = {"status": "failed", "at": now(), "error": str(ex)[:500]}
                self.save()
            self.note("FAILED %s at %s: %s" % (key, t.get("current"), ex))
            traceback.print_exc()

    def process_with_retries(self, key, attempts=3, pause=120):
        """A failed talk is retried by the run itself (Descript hiccups, a dropped upload); only a talk that failed
        every attempt keeps its error for Marek. Out of credits (402) or paused edits are not retried."""
        t = self.talk(key)
        for n in range(1, attempts + 1):
            with self.lock:
                t["queued"] = None
                t["retry"] = None
            self.process(key)
            err = t.get("error") or ""
            if not err or n == attempts or "402" in err or "edits paused" in err:
                return
            with self.lock:
                t["retry"] = "failed (%s) - trying again automatically in %d min, attempt %d of %d" % (
                    err[:120], pause // 60, n + 1, attempts)
                self.save()
            self.note("%s failed, retrying in %d min (attempt %d of %d)" % (key, pause // 60, n + 1, attempts))
            time.sleep(pause)

    def publish(self, force=False):
        """Push the progress to the unlisted page conf42.com/factory, at most every status_publish_minutes."""
        every = float(self.cfg.get("status_publish_minutes", 20)) * 60
        last = getattr(self, "_last_publish", 0)
        if not force and (every <= 0 or datetime.datetime.now().timestamp() - last < every):
            return
        self._last_publish = datetime.datetime.now().timestamp()
        try:
            from . import app
            self.note("status page: %s" % app.publish_status())
        except Exception as ex:
            self.note("status page not updated: %s" % ex)

    def run(self, only=None):
        keys = [k for k, t in self.state["talks"].items() if not t.get("finished") and (not only or k in only)]
        def size(k):                                 # smallest video first: quick uploads finish early and
            try:                                     # never queue behind a 1 GB file (one Descript job per project)
                return os.path.getsize(os.path.join(self.inp, self.state["talks"][k]["source"]))
            except (OSError, KeyError):
                return 0
        keys.sort(key=size)
        with self.lock:                              # a fresh queue: stale "running" steps and old errors are gone
            for i, k in enumerate(keys):
                t = self.state["talks"][k]
                for step in list(t["steps"]):
                    if (t["steps"][step] or {}).get("status") in ("running", "failed"):
                        del t["steps"][step]
                t.update(current=None, error=None, retry=None, queued=i + 1, size_mb=round(size(k) / 1e6))
            self.save()
        self.note("processing %d talk(s), %d at a time" % (len(keys), self.cfg["parallel_talks"]))
        if self.state.get("project_id"):             # uploads left hanging by a stopped run block the whole project
            try:
                gone = Descript().cancel_orphan_uploads(self.state["project_id"])
                if gone:
                    self.note("cancelled %d Descript upload(s) left over from a stopped run" % len(gone))
            except Exception as ex:
                self.note("could not check for leftover Descript uploads: %s" % ex)
        stop = threading.Event()
        def beat():                                  # keep the heartbeat fresh while Descript jobs are quiet
            while not stop.wait(30):
                self.save()
        threading.Thread(target=beat, daemon=True).start()
        with ThreadPoolExecutor(max_workers=max(1, int(self.cfg["parallel_talks"]))) as pool:
            list(pool.map(self.process_with_retries, keys))
        stop.set()
        self.note("run finished")
        with self.lock:
            self.state["runner"] = {"pid": None, "at": now(), "finished": True}
            tmp = self.state_path + ".tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(self.state, f, indent=1, ensure_ascii=False)
            os.replace(tmp, self.state_path)
        self.publish(force=True)


def summary(state):
    talks = state.get("talks", {})
    fin = [k for k, t in talks.items() if t.get("finished")]
    failed = [k for k, t in talks.items() if t.get("error")]
    running = {k: t.get("current") for k, t in talks.items() if t.get("current") and not t.get("error")}
    flagged = {k: t["steps"]["qa"]["flags"] for k, t in talks.items() if (t["steps"].get("qa") or {}).get("flags")}
    return {"matched": len(talks), "in_csv": len(state.get("talks_in_csv", [])), "finished": fin, "failed": failed,
            "running": running, "flagged": flagged, "unmatched": state.get("unmatched", []),
            "missing_videos": [s for s in state.get("talks_in_csv", []) if s not in talks]}
