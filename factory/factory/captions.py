"""The site's transcripts as real captions on the YouTube videos (Marek 2026-11-16).

Talks the cloud factory uploads get their SRT as an "English" caption track straight away (ytupload.py). Everything
uploaded before that only has YouTube's automatic captions - while a proofread transcript sits in src/srt. This puts
it on the video:

    python -m factory captions <short_url> [<short_url> ...] | all  [--dry-run] [--max N]

For every transcript srt/<short_url>_<Name1>.srt whose talk has a YouTube link in the event's CSV:
- the video must be on the Conf42 channel (settings youtube.channel_id) and must not have a caption track of its own
  yet (YouTube's automatic one does not count, and stays);
- the transcript must fit the video: its last cue ends within the video, and not before 60 % of it (a transcript of
  another cut would be out of step all the way) - otherwise it is listed and left;
- then the SRT goes up as the track "English". Nothing is replaced or deleted, ever.

What was done is kept in _db/factory_runs/<short_url>/captions.json, so a second run only does what is left. YouTube
limits how much one day may cost (a caption track is expensive): when the day's limit is reached the run stops and
says so; run it again the next day.
"""
import csv
import glob
import json
import os
import re
import time

from . import events, pipeline, ytupload

VIDEO_ID = re.compile(r"(?:v=|youtu\.be/|/embed/|/shorts/|/live/)([A-Za-z0-9_-]{11})")


def video_id(link):
    m = VIDEO_ID.search(link or "")
    return m.group(1) if m else None


def iso_seconds(d):
    """PT1H2M3S -> seconds."""
    m = re.match(r"^P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?$", d or "")
    if not m:
        return 0
    days, h, mi, s = (int(x or 0) for x in m.groups())
    return days * 86400 + h * 3600 + mi * 60 + s


def pairs(short_url):
    """[(srt path, video id, speakers)] for an event, and [why not] for the transcripts without a usable link."""
    ev = events.event(short_url)
    with open(ev["db_path"], encoding="utf-8-sig", newline="") as f:
        rows = [r for r in csv.DictReader(f) if (r.get("Name1") or "").strip()]
    out, skipped = [], []
    for path in sorted(glob.glob(os.path.join(events.REPO, "srt", short_url + "_*.srt"))):
        stem = os.path.splitext(os.path.basename(path))[0]
        fit = [r for r in rows for k in [("%s_%s" % (short_url, r["Name1"].strip())).replace(" ", "_")]
               if k == stem or k.startswith(stem) or stem.startswith(k)]
        ids = {video_id(r.get("YouTube")) for r in fit} - {None}
        if not fit:
            skipped.append("%s: no talk of the lineup has this name" % os.path.basename(path))
        elif not ids:
            skipped.append("%s: no YouTube link in the CSV" % os.path.basename(path))
        elif len(ids) > 1:
            skipped.append("%s: the speaker has %d videos in this event - not guessed" % (os.path.basename(path), len(ids)))
        else:
            out.append((path, ids.pop(), fit[0]["Name1"].strip()))
    return ev, out, skipped


def state_path(short_url):
    return os.path.join(pipeline.REPO_RUNS, short_url, "captions.json")


def load(short_url):
    p = state_path(short_url)
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save(short_url, d):
    p = state_path(short_url)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(d, f, indent=1, ensure_ascii=False, sort_keys=True)
        f.write("\n")


def ask(yt, method, url, **kw):
    """yt.call, with the day's limit as QuotaExceeded whatever the request was."""
    r = yt.call(method, url, **kw)
    if r.status_code == 403 and "quota" in r.text.lower():
        raise ytupload.QuotaExceeded(r.text[:200])
    return r


def videos(yt, ids):
    """{id: {"seconds", "channel"}} for the videos that exist (50 per request)."""
    out = {}
    for i in range(0, len(ids), 50):
        d = ask(yt, "GET", ytupload.API + "/videos", params={"part": "contentDetails,snippet", "id": ",".join(ids[i:i + 50]), "maxResults": 50}).json()
        for v in d.get("items", []):
            out[v["id"]] = {"seconds": iso_seconds(v["contentDetails"].get("duration")), "channel": v["snippet"].get("channelId")}
    return out


def own_tracks(yt, vid):
    """The caption tracks somebody uploaded (not YouTube's automatic one), or None when they can't be listed."""
    r = ask(yt, "GET", ytupload.API + "/captions", params={"part": "snippet", "videoId": vid})
    if r.status_code != 200:
        return None
    return [i for i in r.json().get("items", []) if (i.get("snippet") or {}).get("trackKind") != "asr"]


def fits(srt, seconds):
    """(True, "") when the transcript belongs to a video this long, else (False, why)."""
    cues = pipeline.srt_cues(srt)
    if len(cues) < 5:
        return False, "the transcript has only %d cues" % len(cues)
    end = cues[-1][1]
    if not seconds:
        return False, "YouTube gives no length for the video"
    if end > seconds + 5:
        return False, "the transcript runs to %d:%02d, the video is %d:%02d long" % (end // 60, end % 60, seconds // 60, seconds % 60)
    if end < .6 * seconds:
        return False, "the transcript ends at %d:%02d of a %d:%02d video" % (end // 60, end % 60, seconds // 60, seconds % 60)
    return True, ""


def event(yt, short_url, channel, dry=False, budget=None, log=print):
    """One event. Returns (added, left to do, lines). budget = [tracks still allowed this run] or None."""
    ev, todo, skipped = pairs(short_url)
    done = load(short_url)
    todo = [(p, v, who) for p, v, who in todo if not (done.get(v) or {}).get("ok")]
    if not todo:
        return 0, 0, []
    try:
        info = videos(yt, [v for _, v, _ in todo])
    except ytupload.QuotaExceeded:
        raise
    added, lines = 0, ["- %s" % s for s in skipped]
    for n, (path, vid, who) in enumerate(todo):
        if budget is not None and budget[0] <= 0:
            if not dry:
                save(short_url, done)
            return added, len(todo) - n, lines
        v = info.get(vid)
        name = os.path.basename(path)
        if not v:
            lines.append("- %s: video %s is not on YouTube (private or deleted?)" % (name, vid))
            continue
        if channel and v["channel"] != channel:
            lines.append("- %s: video %s is on another channel - left" % (name, vid))
            continue
        ok, why = fits(path, v["seconds"])
        if not ok:
            lines.append("- %s: %s - left (https://youtu.be/%s)" % (name, why, vid))
            done[vid] = {"file": name, "ok": False, "why": why, "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            continue
        if dry:
            log("  would add %s -> https://youtu.be/%s" % (name, vid))
            added += 1
            continue
        try:
            own = own_tracks(yt, vid)
            if own is None:
                lines.append("- %s: the video's captions can't be listed - left" % name)
                continue
            if own:
                done[vid] = {"file": name, "ok": True, "had": [(t["snippet"].get("language"), t["snippet"].get("name")) for t in own],
                             "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
                continue                                 # it has a real track already: nothing to add
            with open(path, encoding="utf-8-sig") as f:
                good, msg = yt.captions(vid, f.read())
            if not good and "quota" in msg.lower():
                raise ytupload.QuotaExceeded(msg)
        except ytupload.QuotaExceeded:
            save(short_url, done)
            raise
        if good:
            added += 1
            if budget is not None:
                budget[0] -= 1
            done[vid] = {"file": name, "ok": True, "added": True, "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
            log("  %s -> https://youtu.be/%s" % (name, vid))
        else:
            lines.append("- %s: YouTube refused the captions (%s)" % (name, msg[:120]))
        if added % 10 == 0:
            save(short_url, done)
    if not dry:
        save(short_url, done)
    return added, 0, lines


def all_events():
    return sorted({os.path.basename(p).split("_")[0] for p in glob.glob(os.path.join(events.REPO, "srt", "*.srt"))},
                  key=lambda s: (s[-4:], s), reverse=True)


def backlog(cfg, log=print):
    """A few caption tracks per cloud pass (settings captions_per_pass), newest events first, after the day's uploads:
    YouTube's daily allowance is small and the talks' own uploads come first. Returns the lines for the pass summary."""
    n = int(cfg.get("captions_per_pass", 0) or 0)
    if n <= 0:
        return []
    try:
        yt = ytupload.YouTube()
    except LookupError:
        return []
    channel = (cfg.get("youtube") or {}).get("channel_id")
    budget, lines, total = [n], [], 0
    try:
        yt.check_channel(channel)
        for slug in all_events():
            try:
                added, _, notes = event(yt, slug, channel, False, budget, log)
            except KeyError:
                continue
            total += added
            if budget[0] <= 0:
                break
    except ytupload.QuotaExceeded:
        lines.append("- YouTube's daily limit is reached - the rest another day")
    except Exception as e:                               # noqa: BLE001 - never fails a pass
        lines.append("- stopped: %s" % str(e)[:160])
    return ["", "### Captions on older videos - %d added this pass" % total] + lines


def main(argv):
    dry = "--dry-run" in argv
    mx = int(argv[argv.index("--max") + 1]) if "--max" in argv else None
    rest = [a for i, a in enumerate(argv) if not a.startswith("--") and (i == 0 or argv[i - 1] != "--max")]
    slugs = all_events() if not rest or rest == ["all"] else rest
    cfg = pipeline.settings()
    channel = (cfg.get("youtube") or {}).get("channel_id")
    yt = ytupload.YouTube()
    if not dry:
        try:
            yt.check_channel(channel)
        except RuntimeError as e:
            if "quota" not in str(e).lower():
                raise
            print("STOPPED: YouTube's daily limit is already used up - nothing added. Run it again tomorrow.")
            return 0
    budget, total = ([mx] if mx is not None else None), 0
    for slug in slugs:
        try:
            added, left, lines = event(yt, slug, channel, dry, budget)
        except KeyError as e:
            print("%s: skipped (%s)" % (slug, e))
            continue
        except ytupload.QuotaExceeded:
            print("STOPPED: YouTube's daily limit is reached - %d caption tracks added this run. Run it again tomorrow." % total)
            return 0
        total += added
        if added or lines:
            print("%s: %d caption track(s) %s%s" % (slug, added, "would be added" if dry else "added", (", %d left" % left) if left else ""))
            for l in lines:
                print("  " + l)
        if budget is not None and budget[0] <= 0:
            print("STOPPED at --max %d" % mx)
            break
    print("FINISHED: %d caption track(s) %s" % (total, "would be added" if dry else "added"))
    return 0
