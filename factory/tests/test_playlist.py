"""Playlist = the site's playlist_url, sorted like the event page (ytupload.playlist_order) with a fake YouTube. Offline.
    python factory/tests/test_playlist.py   (from the src repo root)"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from factory import events, ytupload  # noqa: E402


def row(name, track="ml", featured=False, panel=False, banished=False, test=False):
    return {"speakers": name, "track": track, "featured": featured, "panel": panel, "banished": banished, "test": test}


class FakeYT:
    def __init__(self, items):
        self.items = list(items)                         # video ids, playlist order
        self.calls = []

    def playlist(self, title, *a):
        self.calls.append(("by-title", title))
        return "PLbytitle", False

    def playlist_items(self, pid):
        self.calls.append(("list", pid))
        return [("item-" + v, v) for v in self.items]

    def add_to_playlist(self, pid, vid):
        self.calls.append(("add", pid, vid))
        self.items.append(vid)
        return True, ""

    def move(self, pid, item, vid, pos):
        self.calls.append(("move", pid, vid, pos))
        self.items.remove(vid)
        self.items.insert(pos, vid)
        return True, ""


def ev2_wired(y):
    """playlist_for without playlist_url wires the found playlist (wire_site faked)."""
    got = []
    real = y.wire_site
    y.wire_site = lambda slug, url, git=None: got.append((slug, url)) or "wired"
    try:
        ev = {"short_url": "c2027", "name": "MLOps", "year": 2027}
        log = list(y.playlist_order(FakeYT([]), ev, {}, {"A": {"id": "va"}}))
        return got == [("c2027", "https://www.youtube.com/playlist?list=PLbytitle")] and any("wired" in l for l in log) \
            and ev["playlist_url"].endswith("PLbytitle")
    finally:
        y.wire_site = real


def main():
    fails = []

    def check(what, ok):
        print("%s  %s" % ("ok  " if ok else "FAIL", what))
        if not ok:
            fails.append(what)

    talks = [row("A", "ml"), row("K", featured=True), row("B", "data"), row("C", "ml"), row("P", panel=True),
             row("D", "data"), row("Gone", banished=True), row("Factory Test", banished=True, test=True)]
    check("page order: keynotes, panels, tracks by first appearance, banished last, no test talk",
          ytupload.site_order(talks) == ["K", "P", "A", "C", "B", "D", "Gone"])
    check("list id from the site's playlist link",
          ytupload.playlist_id_from("https://www.youtube.com/playlist?list=PLIuxSyKxlQrCqfY7wceGZMeGnQ647UUYw")
          == "PLIuxSyKxlQrCqfY7wceGZMeGnQ647UUYw")
    check("no link, no id", ytupload.playlist_id_from(None) is None and ytupload.playlist_id_from("https://x.y/") is None)
    check("sorted already: no moves", ytupload.order_moves(["a", "b", "x"], ["a", "b"]) == [])
    cur = ["x", "c", "a", "b"]
    moves = ytupload.order_moves(cur, ["a", "b", "c"])
    for v, pos in moves:
        cur.remove(v)
        cur.insert(pos, v)
    check("our talks to the top in order, others after", cur == ["a", "b", "c", "x"])

    # a whole pass
    ytupload.REPO_RUNS = tempfile.mkdtemp(prefix="playlist-test-")
    events_talks = events.talks
    events.talks = lambda ev: talks
    try:
        ev = {"short_url": "test2027", "playlist_url": "https://www.youtube.com/playlist?list=PLsite0000000000"}
        done = {"A": {"id": "va"}, "B": {"id": "vb"}, "C": {"id": "vc"}, "K": {"id": "vk"}, "D": {},
                "Factory Test": {"id": "vt", "test": True}}
        yt = FakeYT(["vc", "intro", "va"])               # B and K missing, wrong order, one video of someone else's
        log = list(ytupload.playlist_order(yt, ev, {}, done))
        check("the site's playlist is used, no title lookup", not any(c[0] == "by-title" for c in yt.calls)
              and all(c[1] == "PLsite0000000000" for c in yt.calls if c[0] in ("add", "move", "list")))
        check("missing talks added, the test talk never", {c[2] for c in yt.calls if c[0] == "add"} == {"vb", "vk"})
        check("sorted like the page, other videos after", yt.items == ["vk", "va", "vc", "vb", "intro"])
        check("log says so", any("added" in l for l in log) and any("sorted" in l for l in log))
        yt.calls.clear()
        list(ytupload.playlist_order(yt, ev, {}, done))
        check("next pass: one list call, nothing else", [c[0] for c in yt.calls] == ["list"])
        yt2 = FakeYT([])
        list(ytupload.playlist_order(yt2, {"short_url": "test2027", "name": "MLOps", "year": 2027}, {}, done))
        check("no playlist_url: found by title", yt2.calls[0] == ("by-title", "Conf42 MLOps 2027"))
        yt3 = FakeYT([])
        list(ytupload.playlist_order(yt3, ev, {"youtube": {"playlist_sort": False}}, done))
        check("playlist_sort: false switches it off", yt3.calls == [])
        check("found by title: the link is wired to the website", ev2_wired(ytupload))
    finally:
        events.talks = events_talks

    # title matching against the channel's playlists (YouTube.playlist with a fake API)
    def channel(titles):
        yt = ytupload.YouTube.__new__(ytupload.YouTube)
        made = []

        class R:
            def __init__(self, code, d):
                self.status_code, self._d, self.text = code, d, ""

            def json(self):
                return self._d

        def call(method, url, **kw):
            if method == "GET":
                return R(200, {"items": [{"id": "PL%d" % i, "snippet": {"title": t}} for i, t in enumerate(titles)]})
            made.append(kw["json"]["status"]["privacyStatus"])
            return R(200, {"id": "PLnew"})
        yt.call = call
        return yt, made
    yt, made = channel(["Conf42 Golang 2026", "Conf42: MLOps 2026 ", "Conf42 MLOps 2025"])
    check("Marek's own playlist found despite the colon", yt.playlist("Conf42 MLOps 2026", "MLOps", 2026) == ("PL1", False) and not made)
    yt, made = channel(["Conf42 Golang 2026"])
    check("none found: made unlisted", yt.playlist("Conf42 MLOps 2026", "MLOps", 2026) == ("PLnew", True) and made == ["unlisted"])
    yt, made = channel(["Conf42 MLOps 2026 - talks", "Conf42 MLOps 2026 (backup)"])
    try:
        yt.playlist("Conf42 MLOps 2026", "MLOps", 2026)
        check("two candidates: nothing guessed or made", False)
    except RuntimeError:
        check("two candidates: nothing guessed or made", not made)

    # metadata.yml rewiring
    text = "events:\n  - name: A\n    short_url: a2027\n    playlist_url: ~\n    db_path: x\n  - name: B\n    short_url: b2027\n    db_path: y\n"
    t1, c1 = ytupload.set_playlist_url(text, "a2027", "https://www.youtube.com/playlist?list=PLa")
    check("an empty playlist_url is filled", c1 and "    playlist_url: https://www.youtube.com/playlist?list=PLa\n    db_path: x" in t1)
    t2, c2 = ytupload.set_playlist_url(text, "b2027", "https://www.youtube.com/playlist?list=PLb")
    check("a missing key is added to that event only", c2 and "short_url: b2027\n    playlist_url: https://www.youtube.com/playlist?list=PLb\n    db_path: y" in t2
          and "a2027\n    playlist_url: ~" in t2)
    t3, c3 = ytupload.set_playlist_url(t1, "a2027", "https://other")
    check("a typed link is never replaced", not c3 and t3 == t1)
    print("\nALL PASSED" if not fails else "\n%d FAILED" % len(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
