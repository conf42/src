"""Factory fast track: gdrive.Drive.upload (resumable, picks up after a dropped piece) with a fake Drive. Offline.
    python factory/tests/test_fasttrack.py   (from the src repo root)"""
import os
import sys
import tempfile
import types

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
if "requests" not in sys.modules:                       # the Mac has no requests; the fake below replaces it anyway
    try:
        import requests  # noqa: F401
    except ImportError:
        sys.modules["requests"] = types.SimpleNamespace(RequestException=OSError, request=None, put=None)
from factory import gdrive  # noqa: E402


class R:
    def __init__(self, code, headers=None, j=None):
        self.status_code, self.headers, self._j, self.text = code, headers or {}, j or {}, ""

    def json(self):
        return self._j


def main():
    got, fails = bytearray(), []
    state = {"drop": True}

    def put(url, data=None, headers=None, timeout=None):
        rng = headers["Content-Range"]
        if rng.startswith("bytes */"):
            return R(308, {"Range": "bytes=0-%d" % (len(got) - 1)} if got else {})
        a, rest = rng[6:].split("-")
        b, size = rest.split("/")
        if int(a) == 10 and state["drop"]:              # the second piece is lost on the way once
            state["drop"] = False
            raise OSError("reset")
        assert int(a) == len(got), (a, len(got))
        got.extend(data)
        return R(200, j={"id": "F1"}) if len(got) == int(size) else R(308, {"Range": "bytes=0-%d" % (len(got) - 1)})

    gdrive.requests.put = put
    gdrive.requests.RequestException = OSError
    gdrive.time.sleep = lambda s: None
    d = gdrive.Drive(token="t")
    calls = []
    d._call = lambda m, u, **kw: calls.append((m, kw["json"])) or R(200, {"Location": "https://up/1"})
    path = os.path.join(tempfile.mkdtemp(), "Sunil Gattupalle - talk.mp4")
    blob = bytes(range(256)) * 1 + b"x" * 9
    open(path, "wb").write(blob)
    fid = d.upload(path, "FOLDER", chunk=10, log=lambda *a: None)
    empty = os.path.join(os.path.dirname(path), "empty.pdf")
    open(empty, "wb").close()
    seen = []
    gdrive.requests.put = lambda url, data=None, headers=None, timeout=None: seen.append(headers["Content-Range"]) or R(200, j={"id": "E"})
    e_id = d.upload(empty, "FOLDER", log=lambda *a: None)
    calls_down = []

    def down(url, data=None, headers=None, timeout=None):
        calls_down.append(1)
        return R(503)
    gdrive.requests.put = down
    try:
        d.upload(path, "FOLDER", chunk=10, log=lambda *a: None, tries=3)
        gave_up = False
    except RuntimeError:
        gave_up = True
    for what, ok in [("an empty file: one 'bytes */0'", e_id == "E" and seen == ["bytes */0"]),
                     ("Drive down for good: gives up after the cap", gave_up and len(calls_down) < 20),
                     ("uploaded whole, in order, after a dropped piece", fid == "F1" and bytes(got) == blob),
                     ("into the folder under its real name", calls[0][1] == {"name": "Sunil Gattupalle - talk.mp4",
                                                                            "parents": ["FOLDER"]})]:
        print("%s  %s" % ("ok  " if ok else "FAIL", what))
        if not ok:
            fails.append(what)
    try:
        from factory import cloud
        import datetime
        act = {"past": {"date": "2026-11-01"}, "today": {"date": "2026-11-19"}, "later": {"date": "2027-01-10"}, "x": {}}
        cases = [("sheet first: started events only", sorted(cloud.sheet_first(act, None, datetime.date(2026, 11, 19))) == ["past", "today"]),
                 ("sheet first: a named event even before it starts", sorted(cloud.sheet_first(act, ["later"])) == ["later"])]
    except ImportError as e:                             # the Mac has no requests: cloud.py checked in CI only
        cases = [("cloud.sheet_first skipped here (%s)" % e, True)]
    from factory import slides
    sd = tempfile.mkdtemp()
    open(os.path.join(sd, "Sunil Gattupalle - Harness - Conf42 MLOps 2026.pdf"), "wb").write(b"%PDF-1.4 tiny")
    open(os.path.join(sd, "Ada Lovelace - Conf42 MLOps 2026.pdf"), "wb").write(b"%PDF-1.4 done")
    tl = [{"speakers": n, "name1": n, "name2": "", "title": "t"} for n in ("Sunil Gattupalle", "Ada Lovelace")]
    try:
        slides.prepare(sd, {"title": "Conf42 MLOps 2026"}, tl)
    except Exception as e:                               # noqa: BLE001 - compress tools missing here: the rename came first
        print("     (prepare stopped after the rename: %s)" % str(e)[:80])
    have = sorted(os.listdir(sd))
    cases.append(("a deck named '<speaker> - <company> - <event>' is renamed for the site, not taken as done",
                  "Sunil Gattupalle - Conf42 MLOps 2026.pdf" in have and "Ada Lovelace - Conf42 MLOps 2026.pdf" in have))
    for what, ok in cases:
        print("%s  %s" % ("ok  " if ok else "FAIL", what))
        if not ok:
            fails.append(what)
    print("\nALL PASSED" if not fails else "\n%d FAILED" % len(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
