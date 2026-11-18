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
    """A playlist that remembers when each video was added (a clock), like YouTube's publishedAt."""
    def __init__(self, items, added=None):
        self.clock = 0
        self.items = []                                  # [video id, added at] in position order
        for v in items:
            self.clock += 1
            self.items.append([v, (added or {}).get(v, self.clock)])
        self.calls = []

    def playlist(self, title, *a):
        self.calls.append(("by-title", title))
        return "PLbytitle", False

    def playlist_items(self, pid):
        self.calls.append(("list", pid))
        return [("item-" + v, v, "%06d" % t) for v, t in self.items]

    def add_to_playlist(self, pid, vid):
        self.calls.append(("add", pid, vid))
        self.clock += 100
        self.items.append([vid, self.clock])
        return True, ""

    def remove_item(self, item):
        self.calls.append(("remove", item))
        self.items = [x for x in self.items if "item-" + x[0] != item]
        return True, ""

    def by_date(self):
        return [v for v, _ in sorted(self.items, key=lambda x: x[1])]

    def by_position(self):
        return [v for v, _ in self.items]


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
    check("in order already: nothing to re-add", ytupload.readd_plan(["a", "x", "b"], ["a", "b"]) == (["a", "b"], []))
    check("from the first one out of place, the rest is re-added in order",
          ytupload.readd_plan(["a", "c", "b"], ["a", "b", "c", "d"]) == (["a"], ["b", "c", "d"]))

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
              and all(c[1] == "PLsite0000000000" for c in yt.calls if c[0] in ("add", "list")))
        check("the test talk never goes in", "vt" not in yt.by_position())
        talks_by_date = [v for v in yt.by_date() if v != "intro"]
        talks_by_pos = [v for v in yt.by_position() if v != "intro"]
        check("added in the page's order: right when sorted by date", talks_by_date == ["vk", "va", "vc", "vb"])
        check("... and by position (Manual)", talks_by_pos == ["vk", "va", "vc", "vb"])
        check("someone else's video stays", "intro" in yt.by_position())
        check("log says so", any("order" in l for l in log))
        yt.calls.clear()
        list(ytupload.playlist_order(yt, ev, {}, done))
        check("next pass: one list call, nothing else", [c[0] for c in yt.calls] == ["list"])
        # positions right but added in the wrong order (the 15 moves of 2026-11-18): fixed by re-adding
        ytm = FakeYT(["vk", "va", "vc", "vb"], added={"vk": 4, "va": 3, "vc": 2, "vb": 1})
        list(ytupload.playlist_order(ytm, ev, {}, done))
        check("moved-but-not-re-added playlist gets re-added in order", ytm.by_date() == ["vk", "va", "vc", "vb"])
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
    # playlist-fix: videos the factory never uploaded, matched by speaker + event title
    tk = [{"speakers": "Ada Lovelace", "name1": "Ada Lovelace", "track": "x", "featured": True},
          {"speakers": "Alan Turing", "name1": "Alan Turing", "track": "x"},
          {"speakers": "Grace Hopper", "name1": "Grace Hopper", "track": "x"},
          {"speakers": "Nobody Here", "name1": "Nobody Here", "track": "x"}]
    vids = [{"video": "v1", "title": "Machines | Alan Turing | Conf42 Platform Engineering 2026"},
            {"video": "v9", "title": "Machines again | Alan Turing | Conf42 MLOps 2026"},
            {"video": "v2", "title": "Compilers | Grace Hopper | Conf42 Platform Eng. 2026"},
            {"video": "v3", "title": "Engines | Ada Lovelace | Conf42 Platform Engineering 2026"},
            {"video": "v4", "title": "Engines (part 2) | Ada Lovelace | Conf42 Platform Engineering 2026"}]
    m = ytupload.match_videos(tk, ["Ada Lovelace", "Alan Turing", "Grace Hopper", "Nobody Here"], vids,
                              "Conf42 Platform Engineering 2026")
    check("matched by name + this event's title (not the same speaker's MLOps talk)", m.get("Alan Turing") == "v1"
          and m.get("Grace Hopper") == "v2")
    check("two candidates for a talk: none guessed", "Ada Lovelace" not in m and "Nobody Here" not in m)

    class FixYT(FakeYT):
        def items_full(self, pid, stop_before=None):
            if pid == "UPLOADS":
                return [{"item": "u-" + v["video"], "video": v["video"], "added": "", "title": v["title"], "published": "2026-11-05"}
                        for v in vids if v["video"] in ("v2",)]
            titles = {v["video"]: v["title"] for v in vids}
            return [{"item": "item-" + v, "video": v, "added": "%06d" % t, "title": titles.get(v, v), "published": ""}
                    for v, t in self.items]

        def uploads_id(self):
            return "UPLOADS"
    events_talks, events_event, ld = events.talks, events.event, ytupload.load
    events.talks = lambda ev: tk[1:3]
    events.event = lambda slug: {"short_url": slug, "name": "Platform Engineering", "year": "2026", "date": "2026-11-05",
                                 "title": "Conf42 Platform Engineering 2026", "playlist_url": "https://www.youtube.com/playlist?list=PLplatform00"}
    ytupload.load = lambda slug: {}
    try:
        fy = FixYT(["v1"])                               # Alan in the playlist, Grace only among the uploads
        out = []
        rc = ytupload.fix_playlist("platform2026", {}, fy, out.append)
        check("playlist-fix: found in the playlist + the uploads, put in page order",
              rc == 0 and fy.by_date() == ["v1", "v2"] and any("2 videos found" in l for l in out))
        out = []
        ytupload.fix_playlist("platform2026", {}, fy, out.append)
        check("playlist-fix again: nothing to do", any("already in the website's order" in l for l in out))
    finally:
        events.talks, events.event, ytupload.load = events_talks, events_event, ld
    print("\nALL PASSED" if not fails else "\n%d FAILED" % len(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
