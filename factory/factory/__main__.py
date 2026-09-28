"""Conf42 factory command line.

  python -m factory match  <short_url> [zip/folder ...]   unzip + match videos to speakers, print the table
  python -m factory run    <short_url> [zip/folder ...]   the whole pipeline (resumes where it stopped)
  python -m factory slides <short_url> [zip/folder ...]   decks only: unzip, match, PDF, rename, compress < 5 MB
  python -m factory status <short_url>                    progress summary
  python -m factory retry  <short_url> "<speaker(s)>"     retry one talk from its failed step
  python -m factory serve                                 the local app on http://localhost:8042
  python -m factory doctor                                check this machine (tools, GPU, token, git, disk)
  python -m factory setup                                 one-time setup on a new machine (token, launcher, check)

  run ... --force   start even if another machine holds the event's lock (only when that machine is off)
"""
import getpass
import json
import os
import socket
import stat
import sys

from . import events, machine, pipeline


def print_doctor(check_descript=True):
    bad = 0
    for c in machine.doctor(pipeline.settings(), events.REPO, check_descript):
        mark = "OK  " if c["ok"] else ("FIX " if c["required"] else "opt ")
        bad += (not c["ok"] and c["required"])
        print("  %s %-38s %s" % (mark, c["name"], c["detail"]))
        if not c["ok"] and c["fix"]:
            print("       -> %s" % c["fix"])
    print("\n\n  ready to run." if not bad else "\n\n  %d thing(s) to fix before running." % bad)
    return bad


def setup():
    """One-time setup on a new machine: machine name, Descript token, Desktop launcher, health check."""
    here = pipeline.HERE
    local = os.path.join(here, "settings.local.yml")
    if not os.path.exists(local):
        name = input("Name for this machine [%s]: " % socket.gethostname()).strip() or socket.gethostname()
        with open(local, "w", encoding="utf-8") as f:
            f.write("# this machine only (git-ignored). Anything from settings.yml can be overridden here.\n"
                    "machine_name: %s\n# work_root: D:/talk-factory    # default: <Desktop>/talk-factory\n"
                    "render_parallel: auto\n" % name)
        print("wrote " + local)
    if not machine.read_token():
        print("\nDescript API token (Descript > Settings > API tokens). It is stored on this machine only, never in git.")
        tok = getpass.getpass("token (hidden): ").strip()
        if tok:
            print("stored as " + machine.store_token(tok))
    desk = machine.desktop()
    if os.name == "nt":
        path = os.path.join(desk, "Conf42 factory.cmd")
        with open(path, "w", encoding="utf-8") as f:
            f.write('@start "" "%s"\r\n' % os.path.join(here, "run.cmd"))
    else:
        path = os.path.join(desk, "Conf42 factory.command")
        with open(path, "w", encoding="utf-8") as f:
            f.write('#!/bin/bash\n"%s"\n' % os.path.join(here, "run.sh"))
        os.chmod(path, os.stat(path).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print("launcher: " + path + "\n\nchecking this machine:")
    return print_doctor()


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
    force = "--force" in argv
    argv = [a for a in argv if a != "--force"]
    if cmd == "doctor":
        sys.exit(1 if print_doctor() else 0)
    if cmd == "setup":
        sys.exit(1 if setup() else 0)
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
            run.run(force=force)
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
        run.run(only=[argv[2]], force=force)
    else:
        print(__doc__)


main(sys.argv[1:])
