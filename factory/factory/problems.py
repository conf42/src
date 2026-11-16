"""What needs a look, said on the factory's own pages (Marek 2026-11-16).

"Any failed runs and problems should be printed out in the factory. If I didn't ask you, I wouldn't know at all" -
two days of failed passes and a talk the factory could not see were only in a GitHub run's summary. Every cloud pass
now writes _db/factory_runs/problems.json, and conf42.com/<event>/factory and conf42.com/factory show it as one
yellow pill above the talks:

    {"updated": <when the pass ended>, "ok": <nothing failed>, "run": <the pass on GitHub>,
     "failed": ["chaos2026: KeyError ..."],                 what broke in the pass
     "events": {"mlops2026": [{"k": "fail" | "look", "t": "..."}]},
     "all": [{"k": ..., "t": ...}]}                         things that belong to no single event

Per event (items(), from the run's state, the intake, YouTube's records and the pass's own lines):
  fail  a talk that stopped with an error; a talk that needs a new video; a finished talk that is not on YouTube;
        an upload that could not be sorted; YouTube refusing a video
  look  an upload held for Marek; an upload rejected in the last 14 days; a video or deck in a folder that names no
        speaker, or that Drive would not hand out; a new version of a talk already made; a newer video on Drive;
        QA flags on a finished talk (setup screen at the start, loudness, a big cut); captions that did not go up

A pass that dies before it gets this far cannot write anything, so two more things cover that:
- the workflow's last step (`python -m factory problems-mark <outcome>`, always run) writes "the pass stopped before
  it finished" when the file is older than the pass;
- the pages themselves say so when the file is more than 30 hours old ("no pass has finished since ...").
"""
import datetime
import json
import os

from . import events, intake

PATH = os.path.join(intake.REPO_RUNS, "problems.json")
RECENT_DAYS = 14


def now():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def load(path=None):
    p = path or os.path.join(intake.REPO_RUNS, "problems.json")
    if os.path.exists(p):
        try:
            with open(p, encoding="utf-8") as f:
                return json.load(f)
        except ValueError:
            pass
    return {"events": {}, "all": [], "failed": []}


def item(kind, text):
    return {"k": kind, "t": " ".join(str(text).split())[:400]}


def items(slug, state, intake_state, youtube, lines=(), skipped=()):
    """The event's problems. state = the run's state.json, intake_state = intake.json, youtube = youtube.json,
    lines = the pass summary's lines for the event (cloud.one_event), skipped = files Drive would not hand out."""
    out = []
    talks = (state or {}).get("talks") or {}
    for key, t in sorted(talks.items()):
        if key == events.TEST_TALK:
            continue
        steps = t.get("steps") or {}
        if t.get("error"):
            step = next((s for s, v in steps.items() if (v or {}).get("status") == "failed"), None)
            out.append(item("fail", "%s: stopped%s - %s" % (key, (" at " + step) if step else "", str(t["error"])[:200])))
        if t.get("needs_new_video"):
            why = t["needs_new_video"] if isinstance(t["needs_new_video"], str) else ""
            out.append(item("fail", "%s needs a new video from the speaker%s" % (key, (" - " + why[:160]) if why else "")))
        yt = (youtube or {}).get(key) or {}
        if t.get("finished") and not yt.get("id"):
            out.append(item("fail", "%s is edited but not on YouTube yet (the daily limit, or the upload failed) - the next pass tries again" % key))
        if yt.get("problem"):
            out.append(item("fail", "%s: YouTube says %s (youtu.be/%s)" % (key, yt["problem"], yt.get("id"))))
        if yt.get("id") and yt.get("captions") is False:
            out.append(item("look", "%s: the captions did not go up (%s)" % (key, str(yt.get("captions_note") or "no reason given")[:120])))
        if t.get("drive_newer"):
            out.append(item("look", "%s: a newer video is on Drive (%s) - redo it?" % (key, str((t["drive_newer"] or {}).get("uploaded", ""))[:16])))
        for flag in ((steps.get("qa") or {}).get("flags") or []) if t.get("finished") else []:
            out.append(item("look", "%s: %s" % (key, flag)))
    for u in (state or {}).get("unmatched") or []:
        out.append(item("look", "video `%s` matches no speaker of the lineup (%s)" % (u.get("file"), str(u.get("why") or "")[:140])))
    cutoff = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=RECENT_DAYS)).isoformat()
    for rec in sorted(((intake_state or {}).get("items") or {}).values(), key=lambda r: r.get("decided") or ""):
        who = rec.get("folder") or "an upload"
        if rec.get("error"):
            out.append(item("fail", "upload %s could not be sorted (%s) - tried again every pass" % (who, str(rec["error"])[:160])))
        elif rec.get("outcome") == "hold":
            out.append(item("look", "upload %s is held: %s" % (who, rec.get("reason") or "no reason given")))
        elif rec.get("outcome") == "reject" and (rec.get("decided") or "") >= cutoff and rec.get("reason") not in ("marek", "organizer-test"):
            out.append(item("look", "upload %s was rejected (%s) - the speaker needs to record again" % (who, rec.get("reason"))))
        elif rec.get("flags") and rec.get("outcome") == "accept" and (rec.get("decided") or "") >= cutoff:
            for flag in rec["flags"]:
                if "re-filed" not in flag:
                    out.append(item("look", "%s: %s" % (rec.get("talk") or who, flag)))
    for name in skipped:
        out.append(item("look", "Drive would not hand out %s" % name))
    for l in lines:
        l = str(l)
        if l.startswith("- left:") and "is ignored" not in l:      # the same talk in a lower folder is normal, not a problem
            out.append(item("look", "in the upload folder, not taken: " + l[len("- left:"):].strip().replace("`", "")))
        elif l.startswith("- could not read it"):
            out.append(item("fail", "an upload folder could not be read" + l[len("- could not read it"):]))
    seen, uniq = set(), []
    for i in out:                                        # a flag can come from the intake and from the QA step
        if i["t"] not in seen:
            seen.add(i["t"])
            uniq.append(i)
    return uniq


def write(per_event, failed, extra=(), run=None, path=None):
    """The pass's result. Events the pass did not touch keep what they had."""
    p = path or os.path.join(intake.REPO_RUNS, "problems.json")
    d = load(p)
    d["events"] = dict(d.get("events") or {}, **per_event)
    d["events"] = {s: v for s, v in d["events"].items() if v}
    d.update(updated=now(), ok=not failed, failed=[str(f)[:300] for f in failed], run=run or "", all=list(extra))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    return d


def mark(outcome, started=None, run=None, path=None):
    """The workflow's last word (always run): when the pass did not succeed and wrote nothing itself (a crash, a
    time-out, a step before it failing), say so. Returns True when the file was changed."""
    if outcome == "success":
        return False
    p = path or os.path.join(intake.REPO_RUNS, "problems.json")
    d = load(p)
    if started and (d.get("updated") or "") >= started:
        return False                                     # the pass got to its own report (it says what failed)
    why = {"failure": "stopped with an error", "cancelled": "was cancelled or ran out of time", "skipped": "never started (a step before it failed)"}.get(outcome, outcome)
    d.update(updated=now(), ok=False, run=run or d.get("run") or "",
             failed=["the pass %s before it finished - nothing it found is listed here; open the run" % why])
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write("\n")
    return True
