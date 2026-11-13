"""The cloud factory (Marek 2026-11-13): one pass in GitHub Actions (.github/workflows/factory-cloud.yml).

    python -m factory cloud [<short_url> ...|all] [--dry-run] [--no-claude] [--no-youtube]

1. intake: tidy the new conf42.com/record uploads in Drive "Auto upload" (intake.py) - accepted talks land in the
   event's in/ + slides/, named after the talk.
2. factory: for every event that came through Auto upload (or that is named), the normal pipeline (pipeline.Run:
   render/health, Descript upload + edit + publish + download, SRT + proofread, chapters, loudness, QA, slides, ship).
   A fresh runner has no source files: talks that are not in Descript yet get theirs again from Drive (the intake
   record keeps the file id), talks already uploaded to Descript need none.
3. youtube: finished talks go up to YouTube, unlisted, with title / description / chapters / thumbnail / captions /
   playlist (ytupload.py; skipped until it is configured).
4. the run state, intake.json and conf42.com/factory are committed + pushed (app.publish_status does the status).

--dry-run: intake decides but moves nothing and writes nothing into the factory; no Descript, no YouTube.
The lock is the same as on the PCs (_db/factory.json, one machine per event); the cloud's machine id is "cloud".
"""
import datetime
import json
import os
import shutil
import tempfile

from . import app, events, gdrive, intake, pipeline


def summary_md(lines):
    p = os.environ.get("GITHUB_STEP_SUMMARY")
    if p:
        with open(p, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


def intake_events(slugs=None):
    """Events that have conf42.com/record uploads (an intake.json), or the ones named."""
    out = []
    if os.path.isdir(intake.REPO_RUNS):
        for slug in sorted(os.listdir(intake.REPO_RUNS)):
            if os.path.exists(os.path.join(intake.REPO_RUNS, slug, "intake.json")) and (not slugs or slug in slugs):
                out.append(slug)
    return sorted(set(out) | set(slugs or []))


def rehydrate(run, drive, log=print):
    """Source videos for talks not yet in Descript, from the intake records. Returns the talks that can run now."""
    st = intake.Intake(drive).load(run.ev["short_url"])
    by_talk = {}
    for fid, rec in st.get("items", {}).items():
        if rec.get("outcome") == "accept" and rec.get("talk") and rec.get("video_id"):
            if rec["talk"] not in by_talk or (rec.get("decided") or "") > (by_talk[rec["talk"]].get("decided") or ""):
                by_talk[rec["talk"]] = rec
    ready = []
    for key, t in run.state["talks"].items():
        if t.get("finished"):
            continue
        src = os.path.join(run.inp, t.get("source") or key + ".mp4")
        uploaded = (t["steps"].get("upload") or {}).get("status") == "done"
        if os.path.exists(src) or uploaded:
            ready.append(key)
            continue
        rec = by_talk.get(key)
        if not rec:
            log("cloud: %s has no source here and no Auto upload record - left for the PC that started it" % key)
            continue
        tmp = tempfile.mkdtemp(prefix="rehydrate-")
        try:
            raw = os.path.join(tmp, "video.mp4")
            meta = drive.get(rec["video_id"])
            drive.download(rec["video_id"], raw, int(meta.get("size") or 0), log)
            intake.prepare(raw, {"numbers": rec.get("numbers") or {}}, src)
            if rec.get("slides_id"):
                pdf = os.path.join(run.slides_dir, key + ".pdf")
                if not os.path.exists(pdf) and not os.path.exists(os.path.join(run.slides_dir, "%s - %s.pdf" % (key, run.ev["title"]))):
                    drive.download(rec["slides_id"], pdf)
            t["source"] = os.path.basename(src)
            ready.append(key)
            log("cloud: %s - source fetched again from Drive" % key)
        except Exception as e:                           # noqa: BLE001 - one talk must not stop the event
            log("cloud: %s - could not fetch its source (%s)" % (key, e))
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    run.save()
    return ready


def commit_intake(msg):
    git = app._git()
    git("add", "_db/factory_runs")
    if git("diff", "--cached", "--quiet").returncode == 0:
        return "nothing to commit"
    git("commit", "-q", "-m", msg)
    for _ in range(3):
        git("pull", "--rebase", "--autostash", "-q")
        if git("push", "-q").returncode == 0:
            return "pushed"
    return "push failed"


def main(argv):
    dry = "--dry-run" in argv
    use_claude = "--no-claude" not in argv
    youtube_on = "--no-youtube" not in argv
    rest = [a for a in argv if not a.startswith("--")]
    slugs = None if not rest or rest == ["all"] else rest
    cfg = pipeline.settings()
    drive = gdrive.Drive()
    started = datetime.datetime.now().isoformat(timespec="seconds")
    lines = ["## Conf42 cloud factory - %s%s" % (started, " (dry run)" if dry else "")]

    news = []                                            # what this pass decided / did: the mail (none = no mail)
    def heard(msg):
        print(msg)
        if " -> " in msg:
            news.append(msg.replace("intake: ", ""))
    accepted = intake.Intake(drive, cfg, use_claude=use_claude, dry_run=dry, log=heard).run(slugs)
    for slug in sorted(set(intake_events(slugs)) | set(accepted)):
        st = intake.Intake(drive).load(slug)
        items = sorted(st.get("items", {}).values(), key=lambda r: r.get("decided") or "", reverse=True)
        lines.append("\n### %s - intake" % slug)
        for r in items[:40]:
            lines.append("- **%s** %s%s%s" % ((r.get("outcome") or "waiting").upper(), r.get("folder"),
                                              (" - " + r["reason"]) if r.get("reason") else "",
                                              (" - " + "; ".join(r["flags"])) if r.get("flags") else ""))
    if not dry:
        print("intake state:", commit_intake("factory intake: conf42.com/record uploads sorted (cloud)"))
    if dry:
        summary_md(lines)
        print("\n".join(lines))
        return 0

    for slug in intake_events(slugs):
        try:
            run = pipeline.Run(slug)
        except KeyError as e:
            print("cloud: %s skipped (%s)" % (slug, e))
            continue
        ready = rehydrate(run, drive, run.note)
        run.match()
        run.slides()
        todo = [k for k in ready if not run.state["talks"][k].get("finished")] + \
               [k for k, t in run.state["talks"].items() if not t.get("finished") and k not in ready
                and os.path.exists(os.path.join(run.inp, t.get("source") or ""))]
        if todo:
            run.note("cloud: %d talk(s) to process: %s" % (len(todo), ", ".join(sorted(todo))))
            try:
                run.run(only=sorted(set(todo)))
            except SystemExit as e:                      # the lock: another machine has this event
                lines.append("\n### %s - not run: %s" % (slug, e))
                continue
        else:
            run.ship()                                   # nothing to edit - still ship what finished (slides added late)
        if youtube_on:
            try:
                from . import ytupload
                for msg in ytupload.event(run, cfg):
                    run.note(msg)
                    if "->" in msg or "limit" in msg or "made the playlist" in msg:
                        news.append(msg)
            except ImportError:
                pass
            except Exception as e:                       # noqa: BLE001 - YouTube trouble never undoes the factory's work
                run.note("youtube: %s" % e)
        s = pipeline.summary(run.state)
        lines.append("\n### %s - factory" % slug)
        lines.append("%d talks matched, %d finished" % (s["matched"], sum(1 for t in run.state["talks"].values() if t.get("finished"))))
        for k, t in sorted(run.state["talks"].items()):
            if t.get("error"):
                lines.append("- %s: **%s**" % (k, str(t["error"])[:200]))
                news.append("%s / %s: FAILED - %s" % (slug, k, str(t["error"])[:200]))
        if run.state.get("edits_paused"):
            news.append("%s: Descript edits PAUSED - %s (python -m factory unpause %s after a look)" % (slug, run.state["edits_paused"], slug))
        run.publish(force=True)
    commit_intake("factory: cloud pass state (intake + youtube)")
    if news:
        nl = chr(10)
        body = [("- " + n) for n in news] + ["", "Held uploads wait for you: python -m factory release <event> <folder id> "
                "accept|reject [\"<speaker>\"] (ids in _db/factory_runs/<event>/intake.json).", "Run: " + run_url()]
        notify("Conf42 factory: %d update%s" % (len(news), "" if len(news) == 1 else "s"), nl.join(body))
    summary_md(lines)
    print("\n".join(lines))
    return 0


def run_url():
    if os.environ.get("GITHUB_RUN_ID"):
        return "%s/%s/actions/runs/%s" % (os.environ.get("GITHUB_SERVER_URL", "https://github.com"),
                                          os.environ.get("GITHUB_REPOSITORY", "conf42/src"), os.environ["GITHUB_RUN_ID"])
    return "local run"


def notify(subject, body):
    """The pass report by mail, through the Conf42 upload script's notify action (same key as UPLOAD_FEED)."""
    import urllib.parse
    import requests
    feed = os.environ.get("UPLOAD_FEED") or ""
    u = urllib.parse.urlparse(feed)
    token = (urllib.parse.parse_qs(u.query).get("token") or [""])[0]
    if not token:
        return
    try:
        requests.post(urllib.parse.urlunparse(u._replace(query="")), data=json.dumps(
            {"action": "notify", "token": token, "subject": subject, "body": body}), timeout=60)
    except Exception as e:                               # noqa: BLE001 - a lost mail never fails the pass
        print("notify failed: %s" % e)


def more_to_do(slugs=None):
    """True when an Auto upload event still has accepted talks that are not finished (the workflow then starts
    itself again after a time-out)."""
    for slug in intake_events(slugs):
        p = os.path.join(intake.REPO_RUNS, slug, "state.json")
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            st = json.load(f)
        with open(os.path.join(intake.REPO_RUNS, slug, "intake.json"), encoding="utf-8") as f:
            accepted = {r.get("talk") for r in json.load(f).get("items", {}).values() if r.get("outcome") == "accept"}
        if any(not t.get("finished") and not t.get("error") for k, t in st.get("talks", {}).items() if k in accepted):
            return True
    return False
