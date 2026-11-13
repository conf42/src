"""The cloud factory's old upload folders (cloud.legacy_*, settings cloud_drive_folders) on a fake Drive. Offline: no
Drive, no Descript, no ffmpeg.   python factory/tests/test_legacy.py   (from the src repo root)

Walks one event through four passes, each on an empty runner like GitHub Actions:
  1. first pass: named files are taken, a talk that came through conf42.com/record and a nameless file are left
  2. the talks are not in Descript yet: their sources are fetched again, nothing is redone
  3. one talk is in Descript: its source is not fetched again
  4. its speaker uploads a new version: not taken, flagged for Marek
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from factory import cloud, drive, events, pipeline  # noqa: E402

TALKS = [{"name1": n, "name2": "", "speakers": n, "title": "Talk of " + n} for n in
         ("Ada Lovelace", "Grace Hopper", "Nicolo Brandizzi", "Alan Turing")]
FILES = {}   # id -> (title, folder, size, uploaded)


def fake_drive():
    drive.list_folder = lambda fid, depth=3, path="": [{"id": i, "title": f[0], "folder": f[1]} for i, f in FILES.items()]
    drive.head = lambda fid, tries=3: (FILES[fid][2], FILES[fid][3])

    def download(fid, dest, size=0, note=None):
        with open(dest, "wb") as f:
            f.write(b"x" * FILES[fid][2])
        return dest
    drive.download = download


def main():
    tmp = tempfile.mkdtemp(prefix="legacy-test-")
    fails = []

    def check(what, ok):
        print("%s  %s" % ("ok  " if ok else "FAIL", what))
        if not ok:
            fails.append(what)

    base = pipeline.settings()
    pipeline.settings = lambda: dict(base, work_root=tmp, cloud_drive_folders={"test2027": "https://drive.google.com/drive/folders/abcdefghijklmnop?usp=x"})
    events.event = lambda slug: {"short_url": slug, "title": "Conf42 Test 2027", "db_path": ""}
    events.talks = lambda ev: TALKS
    pipeline.REPO_RUNS = cloud.intake.REPO_RUNS = os.path.join(tmp, "repo_runs")
    fake_drive()
    FILES.update({
        "v1": ("Ada_Lovelace_conf42_talk.mp4", "Talks/", 1000, "2026-11-01T10:00:00Z"),
        "v2": ("Grace Hopper.mp4", "Talks/", 2000, "2026-11-02T10:00:00Z"),
        "v3": ("Brandizzi-conf42.mp4", "Talks/", 3000, "2026-11-03T10:00:00Z"),
        "v4": ("Alan Turing - Conf42 Test 2027.mp4", "Talks/", 4000, "2026-11-04T10:00:00Z"),
        "v5": ("my talk final.mp4", "Talks/", 5000, "2026-11-05T10:00:00Z"),
        "s1": ("Ada_Lovelace_conf42_slides.pdf", "Slides/", 100, "2026-11-01T10:00:00Z"),
        "s4": ("Alan Turing - Conf42 Test 2027.pdf", "Slides/", 400, "2026-11-04T10:00:00Z"),
    })
    check("settings: folder link -> id", cloud.legacy_folders(pipeline.settings()) == {"test2027": "abcdefghijklmnop"})
    check("settings: other events filtered out", cloud.legacy_folders(pipeline.settings(), ["mlops2026"]) == {})
    auto = {"Alan Turing"}                               # his talk came through conf42.com/record

    def fresh_runner(run):
        """A new runner: the work folder is gone, the state comes back (from the repo copy, in real life)."""
        state = run.state
        shutil.rmtree(run.dir)
        run = pipeline.Run("test2027")
        run.state = state
        run.save()
        return run

    # 1. first pass
    run = pipeline.Run("test2027")
    plan = "\n".join(cloud.legacy_plan(run, "abcdefghijklmnop", auto))
    check("dry run: takes the three named talks", plan.count("**TAKE**") == 4 and "Brandizzi-conf42.mp4` (0 MB, 2026-11-03T10:00) - Nicolo Brandizzi: new talk" in plan)
    check("dry run: downloads nothing", not os.listdir(run.inp))
    lines = cloud.legacy_fetch(run, "abcdefghijklmnop", auto)
    run.match()
    talks = run.state["talks"]
    check("pass 1: three talks matched", sorted(talks) == ["Ada Lovelace", "Grace Hopper", "Nicolo Brandizzi"])
    check("pass 1: sources named after the talk", sorted(os.listdir(run.inp)) == ["Ada Lovelace.mp4", "Grace Hopper.mp4", "Nicolo Brandizzi.mp4"])
    check("pass 1: the conf42.com/record talk is left", any("Alan Turing came through conf42.com/record" in l for l in lines)
          and not any("Alan Turing" in f for f in os.listdir(run.slides_dir)))
    check("pass 1: the nameless file is left and listed", any("my talk final.mp4` - no speaker" in l for l in lines))
    check("pass 1: deck taken", "Ada_Lovelace_conf42_slides.pdf" in os.listdir(run.slides_dir))
    check("pass 1: download folder emptied", not os.listdir(os.path.join(run.dir, "drive")))
    check("pass 1: nothing unmatched", not run.state["unmatched"])

    # 2. an empty runner, nothing in Descript yet
    run = fresh_runner(run)
    lines = cloud.legacy_fetch(run, "abcdefghijklmnop", auto)
    run.match()
    check("pass 2: sources fetched again", sorted(os.listdir(run.inp)) == ["Ada Lovelace.mp4", "Grace Hopper.mp4", "Nicolo Brandizzi.mp4"])
    check("pass 2: nothing redone", not any(t.get("redone") for t in run.state["talks"].values()))
    check("pass 2: deck fetched again", "Ada_Lovelace_conf42_slides.pdf" in os.listdir(run.slides_dir))

    # 3. Ada is in Descript, Grace is finished
    run.state["talks"]["Ada Lovelace"]["steps"]["upload"] = {"status": "done"}
    run.state["talks"]["Grace Hopper"]["steps"]["upload"] = {"status": "done"}
    run.state["talks"]["Grace Hopper"]["finished"] = pipeline.now()
    run = fresh_runner(run)
    lines = cloud.legacy_fetch(run, "abcdefghijklmnop", auto)
    run.match()
    check("pass 3: only the talk not in Descript is fetched", os.listdir(run.inp) == ["Nicolo Brandizzi.mp4"])
    check("pass 3: no flags", not any(t.get("drive_newer") for t in run.state["talks"].values()))

    # 4. Grace uploads a new version (a new file), Ada replaces hers in place
    FILES["v6"] = ("Grace Hopper v2.mp4", "Talks/", 2222, "2030-01-01T10:00:00Z")
    FILES["v1"] = ("Ada_Lovelace_conf42_talk.mp4", "Talks/", 1111, "2030-01-02T10:00:00Z")
    run = fresh_runner(run)
    lines = cloud.legacy_fetch(run, "abcdefghijklmnop", auto)
    run.match()
    check("pass 4: new versions are not taken", os.listdir(run.inp) == ["Nicolo Brandizzi.mp4"]
          and sum("NEW VERSION" in l for l in lines) == 2)
    check("pass 4: nothing redone", not any(t.get("redone") for t in run.state["talks"].values()))
    check("pass 4: the finished talk is flagged for Marek", bool(run.state["talks"]["Grace Hopper"].get("drive_newer")))
    shutil.rmtree(tmp, ignore_errors=True)
    print("\n%s" % ("ALL PASSED" if not fails else "%d FAILED: %s" % (len(fails), "; ".join(fails))))
    return len(fails)


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
