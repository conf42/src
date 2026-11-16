"""The upload folders are emptied 120 days after a conference's kick-off (Marek 2026-11-16).

"Everything related to a conference should be sorted in 3 months" - so 120 days after the event's date in
metadata.yml (settings cloud_bin_after_days) the speakers' videos and decks leave the upload folders:

    Auto upload/<event>/<upload>/      our files (the upload script's account owns them) -> Drive's bin
    Auto upload/_factory/Rejected|Superseded/...   the same, by the event in the upload's talk.json
    Manual upload/                     the speakers' own files -> taken out of the folder
    the event's old upload folder      (cloud_drive_folders) the speakers' own files -> taken out of the folder

Google only lets an owner bin a file. Our own files go to the bin (Drive deletes them for good 30 days later, so
day 150 is the point of no return); a speaker's file can only be taken out of our folder - it stays in the speaker's
own Drive, on their quota.

Guardrails:
- only videos and decks: talk.json and the other small records stay, so conf42.com/<event>/factory keeps its history;
- only what is sorted out leaves: a talk that is on YouTube, a rejected or superseded upload. An upload that is still
  held, was never looked at, or was accepted but is NOT on YouTube is never cleaned - it is listed for Marek instead;
- a file in the Manual or an old folder that names no speaker of the event is listed, not removed;
- a Manual folder file is only an old event's when no upcoming or recent lineup claims it, and it was put there
  before that event + 30 days (a speaker who comes back next year keeps the new file);
- every file that leaves is written down in _db/factory_runs/<event>/cleanup.json (id, name, size, what was done) -
  a binned file can be restored from the bin by that id for 30 days.

    python -m factory cleanup [--dry-run]        (also the last step of every cloud pass)
"""
import datetime
import json
import os

from . import events, gdrive, intake, pipeline

KEEP = (".json", ".txt")


def now():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat()


def days(cfg):
    return int((cfg or {}).get("cloud_bin_after_days", 120))


def event_day(slug):
    """The event's kick-off date, or None (unknown event, no date)."""
    for e in events.all_events():
        if e.get("short_url") == slug:
            try:
                return datetime.date.fromisoformat(str(e.get("date", ""))[:10])
            except ValueError:
                return None
    return None


def due(slug, cfg, today=None):
    """True when the event's kick-off is cloud_bin_after_days or more behind us."""
    day = event_day(slug)
    return bool(day) and ((today or datetime.date.today()) - day).days >= days(cfg)


def media_file(f):
    name = (f.get("name") or "").lower()
    return f.get("mimeType") != gdrive.FOLDER and name.endswith(pipeline.VIDEO_EXT + pipeline.SLIDE_EXT)


def on_youtube(slug):
    """The talks of an event that have a video on YouTube."""
    p = os.path.join(intake.REPO_RUNS, slug, "youtube.json")
    if not os.path.exists(p):
        return set()
    with open(p, encoding="utf-8") as f:
        return {k for k, v in json.load(f).items() if (v or {}).get("id")}


class Cleanup:
    def __init__(self, drive, cfg, dry_run=False, today=None, log=print):
        self.d, self.cfg, self.dry, self.today, self.log = drive, cfg or {}, dry_run, today or datetime.date.today(), log
        self.lines, self.records = [], {}

    # ---- one file ----
    def out(self, slug, f, parent, where):
        """Bin our own file, take a speaker's out of the folder. Written down either way."""
        mine = bool(f.get("ownedByMe"))
        what = "binned" if mine else "taken out of the folder (the speaker's own file)"
        self.lines.append("- %s%s: `%s` (%.0f MB) - %s" % ("would be " if self.dry else "", what, f["name"], int(f.get("size") or 0) / 1e6, where))
        if self.dry:
            return
        try:
            if mine:
                self.d.trash(f["id"])
            else:
                self.d.remove_from(f["id"], parent)
        except Exception as e:                           # noqa: BLE001 - tried again next pass
            self.lines.append("  - not done: %s" % str(e)[:160])
            return
        self.records.setdefault(slug, []).append({"id": f["id"], "name": f["name"], "size": int(f.get("size") or 0), "from": where,
                                                  "done": "binned" if mine else "removed from the folder", "at": now()})

    def kept(self, f, why):
        self.lines.append("- kept: `%s` - %s" % (f["name"], why))

    # ---- Auto upload ----
    def upload_folder(self, slug, up, where, state=None, tube=None):
        """One upload's folder: its videos and decks go when the upload is sorted out - the talk is on YouTube, or it
        was rejected / superseded. Anything else (held, never looked at, accepted without a video) is kept and listed."""
        files = [f for f in self.d.children(up["id"]) if media_file(f)]
        if not files:
            return
        rec = ((state or {}).get("items") or {}).get(up["id"]) or {}
        outcome, talk = rec.get("outcome"), rec.get("talk")
        sorted_out = outcome in ("reject", "superseded") or (outcome == "accept" and (talk in (tube or set()) or talk == events.TEST_TALK))
        if not sorted_out:                               # held, never looked at, or accepted without a video: Marek's call
            why = ("%s was accepted but is not on YouTube" % talk if outcome == "accept" else
                   "still held (%s)" % (rec.get("reason") or "no reason")[:80] if outcome == "hold" else "never sorted by the factory")
            for f in files:
                self.kept(f, "%s - look at it (%s)" % (why, where))
            return
        for f in files:
            self.out(slug, f, up["id"], where)

    def auto(self):
        for evf in self.d.children(self.d.root, folders_only=True):
            slug = evf["name"]
            if slug == "_factory":
                self.factory_bins(evf["id"])
                continue
            if slug.startswith("_") or not due(slug, self.cfg, self.today):
                continue
            state, tube = intake.Intake(self.d).load(slug), on_youtube(slug)
            for up in self.d.children(evf["id"], folders_only=True):
                self.upload_folder(slug, up, "Auto upload/%s/%s" % (slug, up["name"]), state, tube)

    def factory_bins(self, fid, path="Auto upload/_factory", depth=3):
        """Rejected / Superseded uploads: the event comes from each upload's talk.json."""
        cutoff = (self.today - datetime.timedelta(days=days(self.cfg))).isoformat()
        for sub in self.d.children(fid, folders_only=True):
            inside = self.d.children(sub["id"])
            tj = next((f for f in inside if f["name"] == "talk.json"), None)
            if not tj:
                if depth > 0:
                    self.factory_bins(sub["id"], path + "/" + sub["name"], depth - 1)
                continue
            if (sub.get("createdTime") or "9")[:10] > cutoff:
                continue                                 # uploaded less than N days ago: its event can't be due yet
            try:
                slug = ((json.loads(self.d.text(tj["id"])).get("event") or {}).get("slug")) or ""
            except ValueError:
                slug = ""
            if slug and due(slug, self.cfg, self.today):
                for f in inside:
                    if media_file(f):
                        self.out(slug, f, sub["id"], "%s/%s" % (path, sub["name"]))

    # ---- the speakers' own folders ----
    def named_files(self, slug, files, where, parent_of):
        """Files of a folder speakers fill by hand, for one event that is due: a talk on YouTube leaves, the rest stays
        and is listed."""
        ev = events.event(slug)
        talk_list, tube = events.talks(ev), on_youtube(slug)
        for f in files:
            t, _ = events.match(f["name"], talk_list)
            if not t:
                self.kept(f, "no speaker of %s in the file name (%s)" % (ev["title"], where))
            elif t["speakers"] not in tube:
                self.kept(f, "%s has no video on YouTube - look at it (%s)" % (t["speakers"], where))
            else:
                self.out(slug, f, parent_of(f), where)

    def walk(self, fid, depth=2):
        """Every video and deck under a folder, with the folder it sits in."""
        out = []
        for f in self.d.children(fid):
            if f.get("mimeType") == gdrive.FOLDER:
                if depth > 0 and "overlay" not in f["name"].lower():
                    out += self.walk(f["id"], depth - 1)
            elif media_file(f):
                out.append(dict(f, _parent=fid))
        return out

    def old_folders(self):
        for slug, link in sorted((self.cfg.get("cloud_drive_folders") or {}).items()):
            if not link or not due(slug, self.cfg, self.today):
                continue
            from . import drive as linkdrive
            self.named_files(slug, self.walk(linkdrive.folder_id(str(link))), "the old %s folder" % slug, lambda f: f["_parent"])

    def manual(self):
        from . import cloud
        fid = cloud.manual_folder(self.cfg)
        if not fid:
            return
        files = self.walk(fid, 0)
        if not files:
            return
        # the lineups that still claim a file: upcoming and recent events (a speaker who is back keeps the new file)
        active = cloud.active_events(self.cfg)
        _, claimed, _ = cloud.manual_claims([{"title": f["name"]} for f in files], active)
        past = sorted((s for s in (e.get("short_url") for e in events.all_events())
                       if s and s not in active and due(s, self.cfg, self.today)
                       and (self.today - event_day(s)).days <= days(self.cfg) + 400), key=event_day, reverse=True)
        for f in files:
            if f["name"] in claimed:
                continue
            made = (f.get("createdTime") or "")[:10]
            for slug in past:
                try:
                    ev = events.event(slug)
                    t, _ = events.match(f["name"], events.talks(ev))
                except Exception:                        # noqa: BLE001 - an old lineup that won't load claims nothing
                    t = None
                if t and t["speakers"] != events.TEST_TALK and made and made <= (event_day(slug) + datetime.timedelta(days=30)).isoformat():
                    self.named_files(slug, [f], "Manual upload", lambda x: x["_parent"])
                    break

    # ---- the pass ----
    def run(self):
        for part in (self.auto, self.manual, self.old_folders):
            try:
                part()
            except Exception as e:                       # noqa: BLE001 - tidying up never stops a pass
                self.lines.append("- %s: not done (%s: %s)" % (part.__name__, type(e).__name__, str(e)[:200]))
        for slug, recs in self.records.items():
            p = os.path.join(intake.REPO_RUNS, slug, "cleanup.json")
            old = []
            if os.path.exists(p):
                with open(p, encoding="utf-8") as f:
                    old = json.load(f)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                json.dump(old + recs, f, indent=1, ensure_ascii=False)
                f.write("\n")
        if self.lines:
            self.lines.insert(0, "\n### Upload folders - %d days after the kick-off%s" % (days(self.cfg), " (dry run)" if self.dry else ""))
        return self.lines


def main(argv):
    lines = Cleanup(gdrive.Drive(), pipeline.settings(), dry_run="--dry-run" in argv).run()
    print("\n".join(lines) if lines else "nothing is due: no event is %d days past its kick-off" % days(pipeline.settings()))
    return 0
