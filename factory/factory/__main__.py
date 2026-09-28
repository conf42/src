"""Conf42 factory command line.

  python -m factory match  <short_url> [zip/folder ...]   unzip + match videos to speakers, print the table
  python -m factory run    <short_url> [zip/folder ...]   the whole pipeline (resumes where it stopped)
  python -m factory slides <short_url> [zip/folder ...]   decks only: unzip, match, PDF, rename, compress < 5 MB
  python -m factory status <short_url>                    progress summary
  python -m factory retry  <short_url> "<speaker(s)>"     retry one talk from its failed step
  python -m factory serve                                 the local app on http://localhost:8042
"""
import json
import sys

from . import pipeline


def table(run):
    s = pipeline.summary(run.state)
    print("%s: %d videos matched, %d talks in the CSV" % (run.ev["title"], s["matched"], s["in_csv"]))
    for k, t in sorted(run.state["talks"].items()):
        print("  %-40s %s" % (k, t["matched"]))
    for u in s["unmatched"]:
        print("  NOT MATCHED  %-28s %s" % (u["file"], u["why"]))
    if s["missing_videos"]:
        print("  no video yet: " + ", ".join(s["missing_videos"]))


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd = argv[0]
    if cmd == "serve":
        from . import app
        app.serve()
        return
    run = pipeline.Run(argv[1])
    if cmd == "slides":
        run.collect(argv[2:])
        print(json.dumps(run.slides(), indent=1, ensure_ascii=False))
        return
    if cmd in ("match", "run"):
        run.collect(argv[2:])
        run.match()
        table(run)
        rep = run.slides()
        print("slides: %d decks ready, %d converted, %d compressed, %d not matched, missing: %s" % (
            len(rep["decks"]), len(rep["converted"]), len(rep["compressed"]), len(rep["unmatched"]), ", ".join(rep["missing"]) or "none"))
        if cmd == "run":
            run.run()
            print(json.dumps(pipeline.summary(run.state), indent=1))
    elif cmd == "status":
        print(json.dumps(pipeline.summary(run.state), indent=1))
    elif cmd == "retry":
        t = run.talk(argv[2])
        for step, v in list(t["steps"].items()):
            if v.get("status") in ("failed", "running"):
                del t["steps"][step]
        t["error"] = None
        run.save()
        run.run(only=[argv[2]])
    else:
        print(__doc__)


main(sys.argv[1:])
