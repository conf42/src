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

Old upload folders (Marek 2026-11-13, MLOps 2026): an event whose speakers were sent the earlier link-shared Drive
folder ("Talks - your talk video recording" + "Slides - your deck in .pdf", free file names) has that folder in
settings.yml `cloud_drive_folders`. Each pass reads it after the intake, like `python -m factory drive` on a PC:
files are matched to the lineup by the speaker's name in the file name, new ones are downloaded and go through the
same pipeline. A talk that came through Auto upload ignores the old folder (the new way wins); a new version of a
talk that is already in Descript is never redone by itself (flagged "newer video on Drive - redo"); a file that
names no speaker is listed in the pass summary and left alone. Nothing in that folder is ever moved or deleted.

--dry-run: intake decides but moves nothing and writes nothing into the factory; no Descript, no YouTube.
The lock is the same as on the PCs (_db/factory.json, one machine per event); the cloud's machine id is "cloud".
"""
import datetime
import json
import os
import shutil
import tempfile

from . import app, drive as linkdrive, events, gdrive, intake, pipeline


def summary_md(lines):
    p = os.environ.get("GITHUB_STEP_SUMMARY")
    if p:
        with open(p, "a", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")


def legacy_folders(cfg, slugs=None):
    """{short_url: Drive folder id} - the events with an old link-shared upload folder (settings cloud_drive_folders)."""
    return {s: linkdrive.folder_id(str(link)) for s, link in (cfg.get("cloud_drive_folders") or {}).items()
            if link and (not slugs or s in slugs)}


def auto_talks(slug):
    """The talks of an event that came through Auto upload (accepted by the intake)."""
    p = os.path.join(intake.REPO_RUNS, slug, "intake.json")
    if not os.path.exists(p):
        return set()
    with open(p, encoding="utf-8") as f:
        return {r.get("talk") for r in json.load(f).get("items", {}).values() if r.get("outcome") == "accept" and r.get("talk")}


def legacy_verdict(run, auto, talk_list, name, size, up, old):
    """What the cloud does with one file of an old upload folder: (True / False / None for drive_fetch, why).
    The runner starts empty, so "fetched before" only counts once the talk is in Descript."""
    video = name.lower().endswith(pipeline.VIDEO_EXT)
    t, _ = events.match(name, talk_list)
    key = t["speakers"] if t else None
    if not key:
        return False, "no speaker of the lineup in the file name - not taken"
    if key in auto:
        return False, "%s came through conf42.com/record - the old folder is ignored" % key
    mine = run.state["talks"].get(key)
    if not video:
        if mine and mine.get("finished"):
            return None, "%s: deck (talk finished - only a changed deck is taken)" % key
        return True, "%s: deck" % key
    if not mine:
        return None, "%s: new talk" % key
    same = bool(old and old.get("size") == size and old.get("uploaded") == up) or size in (mine.get("sizes_seen") or [])
    if (mine["steps"].get("upload") or {}).get("status") == "done" or mine.get("finished"):
        return (None, "%s: already in Descript" % key) if same else \
               (False, "%s: NEW VERSION of a talk that is already in Descript - not redone by itself" % key)
    if os.path.isfile(os.path.join(run.inp, mine.get("source") or "-")):
        return None, "%s: source already here" % key
    return True, "%s: not in Descript yet - source fetched%s" % (key, " again" if same else "")


def legacy_plan(run, fid, auto):
    """Dry run of an old folder: one line per file, nothing downloaded."""
    talk_list, fetched, out = events.talks(run.ev), run.state.get("drive_fetched", {}), []
    for f in linkdrive.list_folder(fid):
        name = f["title"]
        if not name.lower().endswith(pipeline.VIDEO_EXT + pipeline.SLIDE_EXT):
            continue
        try:
            size, up = linkdrive.head(f["id"])
        except Exception as e:                           # noqa: BLE001
            out.append("- %s: skipped (%s)" % (name, str(e)[:80]))
            continue
        old = fetched.get(f["id"])
        verdict, why = legacy_verdict(run, auto, talk_list, name, size, up, old)
        get = verdict is True or (verdict is None and not (old and old.get("size") == size and old.get("uploaded") == up))
        out.append("- %s `%s` (%.0f MB, %s) - %s" % ("**TAKE**" if get else "leave", name, size / 1e6, up[:16], why))
    return out


def legacy_fetch(run, fid, auto):
    """Bring the new files of the event's old upload folder into the factory's input. Returns the lines for the
    pass summary (files taken, files left alone and why)."""
    talk_list, left = events.talks(run.ev), []

    def want(name, size, up, old):
        verdict, why = legacy_verdict(run, auto, talk_list, name, size, up, old)
        if verdict is False:
            left.append("- left: `%s` - %s" % (name, why))
        return verdict
    got = run.drive_fetch(fid, want=want)
    run.collect(got)
    for p in got:                                        # collect copied them into in/ + slides/: the runner's disk is small
        if os.path.isfile(p) and os.path.dirname(os.path.abspath(p)) == os.path.abspath(os.path.join(run.dir, "drive")):
            os.remove(p)
    return ["- taken: `%s`" % os.path.basename(p) for p in got] + left


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

    accepted = intake.Intake(drive, cfg, use_claude=use_claude, dry_run=dry).run(slugs)
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
    legacy = legacy_folders(cfg, slugs)
    if dry:
        for slug, fid in sorted(legacy.items()):
            lines.append("\n### %s - old upload folder" % slug)
            try:
                lines += legacy_plan(pipeline.Run(slug), fid, auto_talks(slug)) or ["- empty"]
            except Exception as e:                       # noqa: BLE001
                lines.append("- could not read it: %s" % e)
        summary_md(lines)
        print("\n".join(lines))
        return 0

    for slug in sorted(set(intake_events(slugs)) | set(legacy)):
        try:
            run = pipeline.Run(slug)
        except KeyError as e:
            print("cloud: %s skipped (%s)" % (slug, e))
            continue
        ready = rehydrate(run, drive, run.note)
        if slug in legacy:
            lines.append("\n### %s - old upload folder" % slug)
            try:
                lines += legacy_fetch(run, legacy[slug], auto_talks(slug)) or ["- nothing new"]
            except Exception as e:                       # noqa: BLE001 - Drive trouble must not stop the Auto upload talks
                run.note("cloud: old upload folder not read (%s)" % e)
                lines.append("- could not read it: %s" % e)
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
        run.publish(force=True)
    commit_intake("factory: cloud pass state (intake + youtube)")
    summary_md(lines)
    print("\n".join(lines))
    return 0


def run_url():
    if os.environ.get("GITHUB_RUN_ID"):
        return "%s/%s/actions/runs/%s" % (os.environ.get("GITHUB_SERVER_URL", "https://github.com"),
                                          os.environ.get("GITHUB_REPOSITORY", "conf42/src"), os.environ["GITHUB_RUN_ID"])
    return "local run"


def more_to_do(slugs=None):
    """True when an Auto upload event still has accepted talks that are not finished - or an event with an old upload
    folder any unfinished talk at all (the workflow then starts itself again after a time-out)."""
    legacy = legacy_folders(pipeline.settings(), slugs)
    for slug in sorted(set(intake_events(slugs)) | set(legacy)):
        p = os.path.join(intake.REPO_RUNS, slug, "state.json")
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            st = json.load(f)
        accepted = auto_talks(slug) | (set(st.get("talks", {})) if slug in legacy else set())
        if any(not t.get("finished") and not t.get("error") and not t.get("needs_new_video")
               for k, t in st.get("talks", {}).items() if k in accepted):
            return True
    return False
