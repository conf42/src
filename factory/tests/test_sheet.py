"""YouTube links into Excels_for_WWW (ytupload.sheet_links) against a fake "Conf42 upload" script. Offline.
    python factory/tests/test_sheet.py   (from the src repo root)"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from factory import ytupload  # noqa: E402


def main():
    fails = []

    def check(what, ok):
        print("%s  %s" % ("ok  " if ok else "FAIL", what))
        if not ok:
            fails.append(what)

    ytupload.REPO_RUNS = tempfile.mkdtemp(prefix="sheet-test-")
    ev = {"short_url": "test2027", "db_path": os.path.join("x", "_db", "TEST_2027.csv")}
    raw = {k: {"name1": k, "name2": "", "title": "Talk of " + k} for k in ("Ada Lovelace", "Grace Hopper", "Alan Turing", "Factory Test")}
    done = {"Ada Lovelace": {"id": "aaaaaaaaaaa"}, "Grace Hopper": {"id": "bbbbbbbbbbb"}, "Alan Turing": {},
            "Factory Test": {"id": "ttttttttttt", "test": True}, "Gone Speaker": {"id": "ggggggggggg"}}
    asked = []

    def post(body):
        asked.append(body)
        return {"ok": True, "results": {"Ada Lovelace": "written", "Grace Hopper": "kept: https://youtu.be/typedbyhand"}}
    log = list(ytupload.sheet_links(ev, done, raw, post))
    check("tab named like the event's CSV", asked[0]["tab"] == "TEST_2027")
    check("only uploaded lineup talks are sent, never the test talk", [r["key"] for r in asked[0]["rows"]] == ["Ada Lovelace", "Grace Hopper"])
    check("the link is the short form", asked[0]["rows"][0]["url"] == "https://youtu.be/aaaaaaaaaaa")
    check("written link remembered", done["Ada Lovelace"].get("sheet") == "https://youtu.be/aaaaaaaaaaa")
    check("a typed link is kept and noted", "sheet" not in done["Grace Hopper"] and done["Grace Hopper"]["sheet_note"].startswith("kept"))
    check("log says both", any("YouTube link in TEST_2027 for Ada Lovelace" in l for l in log) and any("Grace Hopper - link not written" in l for l in log))
    check("state saved", "aaaaaaaaaaa" in open(os.path.join(ytupload.REPO_RUNS, "test2027", "youtube.json"), encoding="utf-8").read())

    asked.clear()
    list(ytupload.sheet_links(ev, done, raw, post))
    check("next pass asks only for the one still missing", [r["key"] for r in asked[0]["rows"]] == ["Grace Hopper"])

    old = list(ytupload.sheet_links(ev, done, raw, lambda b: {"ok": False, "error": "bad action"}))
    check("an old script is reported, nothing breaks", len(old) == 1 and "needs v7" in old[0])

    def boom(body):
        raise RuntimeError("network down")
    check("a failed call never fails the pass", "not written (network down)" in list(ytupload.sheet_links(ev, done, raw, boom))[0])

    done["Ada Lovelace"]["id"] = "ccccccccccc"            # the talk was redone and uploaded again
    asked.clear()
    list(ytupload.sheet_links(ev, done, raw, lambda b: asked.append(b) or {"ok": True, "results": {"Ada Lovelace": "written"}}))
    ada = next(r for r in asked[0]["rows"] if r["key"] == "Ada Lovelace")
    redone(check)
    check("a new video replaces the factory's own earlier link", ada["was"] == "https://youtu.be/aaaaaaaaaaa"
          and done["Ada Lovelace"]["sheet"] == "https://youtu.be/ccccccccccc")
    print("\n%s" % ("ALL PASSED" if not fails else "%d FAILED: %s" % (len(fails), "; ".join(fails))))
    return len(fails)


def redone(check):
    r = ytupload.redone_since
    check("redone after the upload = uploaded again", r({"redone": [{"at": "2026-11-20T10:00:00"}]}, {"id": "x", "uploaded_at": "2026-11-14T06:00:00Z"})
          and r({"redone": [{}, {}]}, {"id": "x", "redone": 1}))
    check("not redone since = left alone", not r({"redone": [{"at": "2026-11-10T10:00:00"}]}, {"id": "x", "uploaded_at": "2026-11-14T06:00:00Z"})
          and not r({"redone": [{}]}, {"id": "x", "redone": 1}) and not r({}, {"id": "x"}))


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
