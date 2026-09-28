"""Conf42 events and talks, read straight from the site repo (metadata.yml + _db/<EVENT>.csv)."""
import csv
import difflib
import os
import re
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


def talks(ev):
    with open(ev["db_path"], encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        n1, n2 = (r.get("Name1") or "").strip(), (r.get("Name2") or "").strip()
        if n1:
            out.append({"name1": n1, "name2": n2, "speakers": n1 + (" & " + n2 if n2 else ""), "title": r.get("Title", "")})
    return out


def _norm(s):
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
