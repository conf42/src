"""The upload folders are emptied 120 days after the kick-off (Marek 2026-11-16) - on a fake Drive.
Offline: no Drive, no Descript, no ffmpeg.   python factory/tests/test_cleanup.py   (from the src repo root)
"""
import datetime
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from factory import cleanup, cloud, events, gdrive, pipeline  # noqa: E402

FOLDER = gdrive.FOLDER


class FakeDrive:
    """tree: {folder id: [file dicts]}; text: {file id: str}."""
    root = "ROOT"

    def __init__(self, tree, text):
        self.tree, self.texts, self.binned, self.removed = tree, text, [], []

    def children(self, fid, folders_only=False):
        return [f for f in self.tree.get(fid, []) if not folders_only or f.get("mimeType") == FOLDER]

    def text(self, fid):
        return self.texts[fid]

    def trash(self, fid):
        self.binned.append(fid)

    def remove_from(self, fid, parent):
        self.removed.append((fid, parent))


def folder(i, name, made="2026-01-01T10:00:00Z"):
    return {"id": i, "name": name, "mimeType": FOLDER, "createdTime": made}


def file(i, name, mine=True, made="2026-01-01T10:00:00Z", size=1000):
    return {"id": i, "name": name, "mimeType": "video/mp4", "size": str(size), "ownedByMe": mine, "createdTime": made}


def main():
    tmp = tempfile.mkdtemp(prefix="cleanup-test-")
    fails = []

    def check(what, ok):
        print("%s  %s" % ("ok  " if ok else "FAIL", what))
        if not ok:
            fails.append(what)

    today = datetime.date(2027, 3, 20)
    dates = {"old2026": "2026-11-19", "edge2026": "2026-11-20", "new2027": "2027-03-10", "soon2027": "2027-04-10"}   # 121, 120, 10, -21 days
    names = {"old2026": "MLOps", "edge2026": "Edge", "new2027": "Chaos Engineering", "soon2027": "Golang"}
    lineups = {"old2026": ["Ada Lovelace", "Grace Hopper", "Alan Turing"], "edge2026": ["Edsger Dijkstra"],
               "new2027": ["Barbara Liskov"], "soon2027": ["Ada Lovelace"]}
    events.all_events = lambda: [{"short_url": s, "date": d, "name": names[s], "db_path": "x"} for s, d in dates.items()]
    events.event = lambda slug: {"short_url": slug, "name": names[slug], "title": "Conf42 %s" % names[slug], "db_path": __file__}
    events.talks = lambda ev: [{"name1": n, "name2": "", "speakers": n, "title": "Talk of " + n} for n in lineups[ev["short_url"]]]
    runs = cleanup.intake.REPO_RUNS = cloud.intake.REPO_RUNS = pipeline.REPO_RUNS = os.path.join(tmp, "runs")
    cfg = {"cloud_bin_after_days": 120, "cloud_manual_folder": "MANUAL", "cloud_drive_folders": {"old2026": "OLDFOLDER", "new2027": "NEWFOLDER"},
           "cloud_manual_days_after": 45, "cloud_manual_days_before": 75}

    class D(datetime.date):
        @classmethod
        def today(cls):
            return today
    cloud.datetime.date = D                              # the Manual folder's "still claimed" window follows the test's today

    def state(slug, items, tube):
        os.makedirs(os.path.join(runs, slug), exist_ok=True)
        with open(os.path.join(runs, slug, "intake.json"), "w", encoding="utf-8") as f:
            json.dump({"event": slug, "items": items}, f)
        with open(os.path.join(runs, slug, "youtube.json"), "w", encoding="utf-8") as f:
            json.dump({k: {"id": "yt-" + k} for k in tube}, f)
    state("old2026", {"U1": {"outcome": "accept", "talk": "Ada Lovelace"}, "U2": {"outcome": "accept", "talk": "Grace Hopper"},
                      "U3": {"outcome": "hold", "reason": "unmatched"}, "U7": {"outcome": "reject", "reason": "too-short"}}, ["Ada Lovelace", "Alan Turing"])
    state("edge2026", {"U5": {"outcome": "accept", "talk": "Edsger Dijkstra"}}, ["Edsger Dijkstra"])
    state("new2027", {"U4": {"outcome": "accept", "talk": "Barbara Liskov"}}, ["Barbara Liskov"])

    tree = {
        "ROOT": [folder("E-old", "old2026"), folder("E-edge", "edge2026"), folder("E-new", "new2027"), folder("F", "_factory"), folder("P", "_probe")],
        "E-old": [folder("U1", "Ada Lovelace (x)"), folder("U2", "Grace Hopper (x)"), folder("U3", "Nobody (x)"),
                  folder("U6", "Unseen (x)"), folder("U7", "Junk (x)"),
                  {"id": "rec", "name": "_recorded.json", "mimeType": "application/json"}],
        "U1": [file("u1v", "Ada Lovelace - Conf42 MLOps 2026.mp4"), file("u1s", "Ada Lovelace - Conf42 MLOps 2026.pdf"),
               {"id": "u1j", "name": "talk.json", "mimeType": "application/json", "ownedByMe": True}],
        "U2": [file("u2v", "Grace Hopper - Conf42 MLOps 2026.mp4")],
        "U3": [file("u3v", "Nobody - Conf42 MLOps 2026.mp4")],
        "U6": [file("u6v", "Unseen - Conf42 MLOps 2026.mp4")], "U7": [file("u7v", "Junk - Conf42 MLOps 2026.mp4")],
        "E-edge": [folder("U5", "Edsger Dijkstra (x)")], "U5": [file("u5v", "Edsger Dijkstra - Conf42 Edge 2026.mp4")],
        "E-new": [folder("U4", "Barbara Liskov (x)")], "U4": [file("u4v", "Barbara Liskov.mp4")],
        "F": [folder("F-rej", "Rejected"), folder("F-sup", "Superseded")],
        "F-rej": [folder("F-short", "too-short")],
        "F-short": [folder("R1", "Ada test (x)", "2026-11-01T10:00:00Z"), folder("R2", "Barbara test (x)", "2027-03-01T10:00:00Z")],
        "R1": [file("r1v", "Ada test.mp4"), {"id": "r1j", "name": "talk.json", "mimeType": "application/json"}],
        "R2": [file("r2v", "Barbara test.mp4"), {"id": "r2j", "name": "talk.json", "mimeType": "application/json"}],
        "F-sup": [folder("S1", "Ada older (x)", "2026-11-02T10:00:00Z")],
        "S1": [file("s1v", "Ada older.mp4"), {"id": "s1j", "name": "talk.json", "mimeType": "application/json"}],
        "MANUAL": [file("m1", "Alan Turing Conf42 MLOps 2026.mp4", False, "2026-11-10T10:00:00Z"),      # old event, on YouTube -> out
                   file("m2", "Grace Hopper.mp4", False, "2026-11-10T10:00:00Z"),                       # old event, NOT on YouTube -> kept
                   file("m3", "Ada Lovelace - Conf42 Golang 2027.mp4", False, "2027-03-15T10:00:00Z"),  # back for an upcoming event -> kept
                   file("m4", "Ada Lovelace.mp4", False, "2026-11-10T10:00:00Z"),                       # claimed by the upcoming lineup -> kept
                   file("m5", "holiday.mp4", False, "2026-01-01T10:00:00Z"),                            # nobody's -> untouched
                   file("m6", "Alan Turing.mp4", False, "2027-02-01T10:00:00Z")],                       # too late for that event -> untouched
        "OLDFOLDER": [folder("O-t", "Talks - your talk video recording"), folder("O-ov", "OBS overlays")],
        "O-t": [file("o1", "Alan_Turing_talk.mp4", False), file("o2", "Grace Hopper.mp4", False), file("o3", "my talk final.mp4", False)],
        "O-ov": [file("o9", "overlay.mp4", False)],
        "NEWFOLDER": [file("n1", "Barbara Liskov.mp4", False)],
    }
    text = {"r1j": json.dumps({"event": {"slug": "old2026"}}), "r2j": json.dumps({"event": {"slug": "new2027"}}),
            "s1j": json.dumps({"event": {"slug": "old2026"}})}

    check("due: 121 days after the kick-off", cleanup.due("old2026", cfg, today))
    check("due: exactly 120 days", cleanup.due("edge2026", cfg, today))
    check("not due: 119 days", not cleanup.due("edge2026", cfg, today - datetime.timedelta(days=1)))
    check("not due: an unknown event", not cleanup.due("nope", cfg, today))

    dry = FakeDrive(tree, text)
    lines = cleanup.Cleanup(dry, cfg, dry_run=True, today=today, log=lambda *a: None).run()
    check("dry run: nothing binned, nothing removed, nothing written", not dry.binned and not dry.removed
          and not os.path.exists(os.path.join(runs, "old2026", "cleanup.json")))
    check("dry run: says what would happen", any("would be binned" in x and "Ada Lovelace - Conf42 MLOps 2026.mp4" in x for x in lines))

    d = FakeDrive(tree, text)
    lines = cleanup.Cleanup(d, cfg, today=today, log=lambda *a: None).run()
    text_out = "\n".join(lines)
    check("Auto upload: the video and the deck of a talk on YouTube are binned", {"u1v", "u1s"} <= set(d.binned))
    check("Auto upload: talk.json and the event's records stay", "u1j" not in d.binned and "rec" not in d.binned)
    check("Auto upload: accepted but not on YouTube -> kept and listed", "u2v" not in d.binned and "Grace Hopper was accepted but is not on YouTube" in text_out)
    check("Auto upload: a held upload is kept and listed", "u3v" not in d.binned and "still held (unmatched)" in text_out)
    check("Auto upload: an upload the factory never sorted is kept and listed", "u6v" not in d.binned and "never sorted by the factory" in text_out)
    check("Auto upload: a rejected upload still in the event's folder is binned", "u7v" in d.binned)
    check("Auto upload: the event at exactly 120 days is cleaned", "u5v" in d.binned)
    check("Auto upload: an event 10 days old is not touched", "u4v" not in d.binned)
    check("_factory: rejected and superseded uploads of a due event are binned", {"r1v", "s1v"} <= set(d.binned))
    check("_factory: a recent event's rejected upload stays", "r2v" not in d.binned)
    check("Manual: a speaker's file is taken out of the folder, not binned", ("m1", "MANUAL") in d.removed and "m1" not in d.binned)
    check("Manual: no video on YouTube -> kept and listed", not any(x[0] == "m2" for x in d.removed) and "Grace Hopper has no video on YouTube" in text_out)
    check("Manual: a file an upcoming lineup claims is left alone", not any(x[0] in ("m3", "m4") for x in d.removed))
    check("Manual: nobody's file and a file put there long after the event are left alone", not any(x[0] in ("m5", "m6") for x in d.removed))
    check("old folder: a talk on YouTube leaves its subfolder", ("o1", "O-t") in d.removed)
    check("old folder: not on YouTube / no speaker named -> kept and listed", not any(x[0] in ("o2", "o3") for x in d.removed)
          and "no speaker of Conf42 MLOps in the file name" in text_out)
    check("old folder: the overlays folder is never looked at", not any(x[0] == "o9" for x in d.removed))
    check("old folder: a recent event's folder is not touched", not any(x[0] == "n1" for x in d.removed))
    rec = json.load(open(os.path.join(runs, "old2026", "cleanup.json"), encoding="utf-8"))
    check("every file that left is written down", {r["id"] for r in rec} == {"u1v", "u1s", "u7v", "r1v", "s1v", "m1", "o1"}
          and {r["done"] for r in rec} == {"binned", "removed from the folder"})
    check("the other event's record is its own", [r["id"] for r in json.load(open(os.path.join(runs, "edge2026", "cleanup.json"), encoding="utf-8"))] == ["u5v"])

    class Broken(FakeDrive):
        def children(self, fid, folders_only=False):
            raise RuntimeError("Drive is down")
    check("Drive trouble never stops the pass", any("not done" in x for x in cleanup.Cleanup(Broken({}, {}), cfg, today=today).run()))

    cloud.datetime.date = datetime.date
    shutil.rmtree(tmp, ignore_errors=True)
    print("\n%s" % ("ALL PASSED" if not fails else "%d FAILED: %s" % (len(fails), "; ".join(fails))))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
