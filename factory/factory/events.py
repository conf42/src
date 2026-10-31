"""Conf42 events and talks, read straight from the site repo (metadata.yml + _db/<EVENT>.csv)."""
import csv
import difflib
import io
import os
import re
import subprocess
import unicodedata

import yaml

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))   # factory/ lives inside src/


def all_events():
    with open(os.path.join(REPO, "metadata.yml"), encoding="utf-8") as f:
        meta = yaml.safe_load(f) or {}
    out = []

    def walk(o):
        if isinstance(o, dict):
            if o.get("short_url") and o.get("db_path") and o.get("name"):
                out.append(o)
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(meta)
    return out


def event(short_url):
    for e in all_events():
        if e["short_url"] == short_url:
            year = str(e.get("date", ""))[:4]
            return {"short_url": short_url, "name": e["name"], "year": year, "date": str(e.get("date", "")),
                    "db_path": os.path.normpath(os.path.join(REPO, e["db_path"])),
                    "title": "Conf42 %s %s" % (e["name"], year)}
    raise KeyError("no event with short_url %r in metadata.yml" % short_url)


def _row(r):
    n1, n2 = (r.get("Name1") or "").strip(), (r.get("Name2") or "").strip()
    return {"name1": n1, "name2": n2, "speakers": n1 + (" & " + n2 if n2 else ""), "title": r.get("Title", ""),
            "abstract": r.get("Abstract", ""), "keywords": r.get("Keywords", ""),
            "job1": r.get("JobTitle1", ""), "company1": r.get("Company1", ""),
            "job2": r.get("JobTitle2", ""), "company2": r.get("Company2", "")}


def talks(ev):
    """The event CSV's talks, then the banished ones (banished: True): talks an earlier upload of the CSV had and the
    current one dropped. A talk with a video keeps everything - matching, YouTube items, transcript, deck - whatever
    the spreadsheet says now (Marek 2026-10-31: "presence of the video has higher prio than the excel")."""
    with open(ev["db_path"], encoding="utf-8-sig", newline="") as f:
        out = [_row(r) for r in csv.DictReader(f) if (r.get("Name1") or "").strip()]
    return out + banished(ev, out)


_history = {}


def _csv_history(path):
    """Every committed version of the CSV, newest first, as row lists. Empty without git history (slim clone)."""
    key = (path, os.path.getmtime(path))
    if key not in _history:
        versions = []
        try:
            rel = os.path.relpath(path, REPO).replace(os.sep, "/")
            git = lambda *a: subprocess.run(["git", "-C", REPO] + list(a), capture_output=True, timeout=60)
            for h in git("log", "--format=%H", "--", rel).stdout.decode().split():
                r = git("show", "%s:%s" % (h, rel))
                if r.returncode == 0:
                    versions.append(list(csv.DictReader(io.StringIO(r.stdout.decode("utf-8-sig", "replace")))))
        except (OSError, subprocess.SubprocessError):
            pass
        _history[key] = versions
    return _history[key]


def banished(ev, current):
    """Talks in an earlier version of the CSV that are not in the current one (newest version of each row wins).
    A speaker still on the lineup under another spelling or with the same title is not banished - two rows for one
    person would make matching refuse both."""
    names = {_norm(t["name1"]) for t in current} | {_norm(t["name2"]) for t in current if t["name2"]}
    titles = {_norm(t["title"]) for t in current if t["title"]}
    out, seen = [], {t["speakers"] for t in current}
    for rows in _csv_history(ev["db_path"]):
        for r in rows:
            t = _row(r)
            n = _norm(t["name1"])
            if not n or t["speakers"] in seen or (t["title"] and _norm(t["title"]) in titles) \
                    or any(re.search("(^| )%s( |$)" % re.escape(n), x) or re.search("(^| )%s( |$)" % re.escape(x), n)
                           for x in names if x):
                continue
            seen.add(t["speakers"])
            t["banished"] = True
            out.append(t)
    return out


def _norm(s):
    s = re.sub(r"([a-z])([A-Z])", r"\1 \2", s)   # "PrateekJindal_..." -> "Prateek Jindal"
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\b(conf42|version|final|v\d+|edited|recording|talk|video|copy|slides?|deck|presentation|ppt|pptx|pdf|\d{4})\b", " ", s)
    return re.sub(r"[^a-z]+", " ", s).strip()


def match(filename, talk_list):
    """Map a video file name to one talk, or return (None, reason). Never guesses between close candidates."""
    stem = _norm(os.path.splitext(os.path.basename(filename))[0])
    exact = [t for t in talk_list if stem in (_norm(t["speakers"]), _norm(t["name1"]))
             or (t["name2"] and stem in (_norm(t["name2"] + " " + t["name1"]), _norm(t["name2"])))]
    if len(exact) == 1:
        return exact[0], "exact"
    inside = [t for t in talk_list if re.search("(^| )" + re.escape(_norm(t["name1"])) + "( |$)", stem)]
    if len(inside) == 1:                                   # e.g. "Emmy Eide slides", "Karan_Bansal_deck"
        return inside[0], "name in file name"
    words = set(stem.split())                              # first + last name both in the file name, e.g.
    fl = [t for t in talk_list                             # "Ashwin Krishnappa Kumar" -> "Ashwin Kumar"
          if len(_norm(t["name1"]).split()) >= 2 and {_norm(t["name1"]).split()[0], _norm(t["name1"]).split()[-1]} <= words]
    if len(fl) == 1:
        return fl[0], "first + last name in file name"
    scored = sorted(((max(difflib.SequenceMatcher(None, stem, _norm(t["speakers"])).ratio(),
                          difflib.SequenceMatcher(None, stem, _norm(t["name1"])).ratio()), t) for t in talk_list),
                    key=lambda x: -x[0])
    if scored and scored[0][0] >= 0.88 and (len(scored) == 1 or scored[0][0] - scored[1][0] >= 0.08):
        return scored[0][1], "close match (%.0f%%)" % (scored[0][0] * 100)
    best = ", ".join("%s %.0f%%" % (t["speakers"], s * 100) for s, t in scored[:2])
    return None, "no speaker in the CSV matches (closest: %s)" % best
