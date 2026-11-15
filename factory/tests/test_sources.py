"""The same talk in several places (Marek 2026-11-15): conf42.com/record > the Manual upload folder > the old folder.
Offline: no Drive, no Descript, no ffmpeg.   python factory/tests/test_sources.py   (from the src repo root)
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from factory import cloud, events, pipeline  # noqa: E402


def talks(*names):
    return [{"name1": n, "name2": "", "speakers": n, "title": "Talk of " + n} for n in names]


def main():
    tmp = tempfile.mkdtemp(prefix="sources-test-")
    fails = []

    def check(what, ok):
        print("%s  %s" % ("ok  " if ok else "FAIL", what))
        if not ok:
            fails.append(what)

    base = pipeline.settings()
    pipeline.settings = lambda: dict(base, work_root=tmp)
    pipeline.REPO_RUNS = cloud.intake.REPO_RUNS = os.path.join(tmp, "repo_runs")
    lineups = {"mlops2027": talks("Ada Lovelace", "Grace Hopper", "Alan Turing"),
               "chaos2027": talks("Ada Lovelace", "Edsger Dijkstra")}
    active = {"mlops2027": {"short_url": "mlops2027", "name": "MLOps", "title": "Conf42 MLOps 2027", "db_path": ""},
              "chaos2027": {"short_url": "chaos2027", "name": "Chaos Engineering", "title": "Conf42 Chaos Engineering 2027", "db_path": ""}}
    events.event = lambda slug: active[slug]
    events.talks = lambda ev: lineups[ev["short_url"]]

    # the Manual upload folder is one folder for every event
    files = [{"title": t} for t in (
        "Grace Hopper.mp4", "Grace_Hopper_slides.pdf",                 # one lineup has her
        "Ada Lovelace - Conf42 Chaos Engineering 2027.mp4",            # on both lineups, the file names the conference
        "Ada Lovelace.mp4",                                            # on both, no conference named: left
        "Edsger Dijkstra deck.pptx", "holiday.mp4", "notes.txt")]
    claims, owner, left = cloud.manual_claims(files, active)
    check("manual: a speaker of one lineup goes to that event", claims["mlops2027"] == {"Grace Hopper": {"video": True, "deck": True}})
    check("manual: the conference in the file name decides", claims["chaos2027"]["Ada Lovelace"] == {"video": True, "deck": False}
          and owner["Ada Lovelace - Conf42 Chaos Engineering 2027.mp4"] == "chaos2027")
    check("manual: on two lineups with no conference named -> left, not guessed",
          "Ada Lovelace.mp4" not in owner and any("Ada Lovelace.mp4" in x and "no single conference" in x for x in left))
    check("manual: a deck alone is claimed as a deck", claims["chaos2027"]["Edsger Dijkstra"] == {"video": False, "deck": True})
    check("manual: a file naming nobody is listed, other file types are not", any("holiday.mp4" in x for x in left) and not any("notes.txt" in x for x in left))

    # who owns a talk
    owned = {"Alan Turing": {"source": "conf42.com/record", "deck": False}}
    owned = cloud.with_manual(owned, {"Grace Hopper": {"video": True, "deck": True}, "Alan Turing": {"video": True, "deck": True},
                                      "Ada Lovelace": {"video": False, "deck": True}})
    check("order: conf42.com/record keeps its talk when the Manual folder has it too", owned["Alan Turing"]["source"] == "conf42.com/record")
    check("order: the Manual folder owns a talk it has a video of", owned["Grace Hopper"]["source"] == "the Manual upload folder")
    check("order: a deck alone in the Manual folder owns nothing", "Ada Lovelace" not in owned)

    run = pipeline.Run("mlops2027")
    tl = lineups["mlops2027"]

    def verdict(name, auto=owned, here="the old folder"):
        return cloud.legacy_verdict(run, auto, tl, name, 1000, "2026-11-01T10:00:00Z", None, here)
    v, why = verdict("Grace Hopper.mp4")
    check("old folder: a video of a Manual-folder talk is ignored", v == "ignore" and "came through the Manual upload folder" in why)
    v, why = verdict("Alan Turing.mp4", here="the Manual upload folder")
    check("manual: a video of a conf42.com/record talk is ignored", v == "ignore" and "came through conf42.com/record - the Manual upload folder is ignored" in why)
    check("a deck is taken from a lower source when the owner brought none", verdict("Alan Turing slides.pdf")[0] is True)
    check("a deck is ignored when the owner brought one", verdict("Grace Hopper slides.pdf")[0] == "ignore")
    check("a talk nobody above has is taken as before", verdict("Ada Lovelace.mp4")[0] is None)
    check("a set of talks still works (conf42.com/record, with deck)", verdict("Alan Turing slides.pdf", {"Alan Turing"})[0] == "ignore")

    # conf42.com/record owns accepted AND held talks, not rejected ones
    os.makedirs(os.path.join(cloud.intake.REPO_RUNS, "mlops2027"))
    cloud.intake.Intake(None).save("mlops2027", {"event": "mlops2027", "items": {
        "a": {"outcome": "accept", "talk": "Ada Lovelace", "slides_id": "x"},
        "b": {"outcome": "hold", "talk": "Grace Hopper", "slides_id": None},
        "c": {"outcome": "reject", "talk": "Alan Turing"}, "d": {"outcome": "hold", "reason": "unmatched"}}})
    o = cloud.auto_owned("mlops2027")
    check("record: accepted and held talks are owned, rejected ones fall to the next source",
          o == {"Ada Lovelace": {"source": "conf42.com/record", "deck": True}, "Grace Hopper": {"source": "conf42.com/record", "deck": False}})
    check("record: only accepted talks count as 'came through' for the restart", cloud.auto_talks("mlops2027") == {"Ada Lovelace"})

    # ---- the wrong conference picked in the recorder (Marek 2026-11-15: "whatever he says, goes") ----
    it = cloud.intake
    two = {"chaos2027": ("Chaos Engineering", "Chaos Engineering for AI Agents: Breaking Permissions, Tools, and Context on Purpose"),
           "mlops2027": ("MLOps", "Testing Agents for Permission Leaks: Authorization Evals in the Delivery Pipeline")}
    deck = "Conf42 MLOps 2026 Testing Agents for Permission Leaks Authorization evals in the delivery pipeline Ada Lovelace"
    name = "Testing Agents for Permission Leaks Authorization Evals in the Delivery Pipeline.pdf"
    hello = "Hi everyone and welcome to Conforded to MLOPS. I am Ada, a senior engineer"
    signs = it.conference_signs(deck, name, hello, two)
    check("wrong conference: deck, file name and greeting all point at the other event",
          len(signs["mlops2027"]) == 3 and not signs["chaos2027"])
    check("wrong conference: three signs, none for the filed event -> re-filed", it.wrong_conference("chaos2027", signs)[:2] == ("refile", "mlops2027"))
    check("right conference: the same signs for the filed event -> nothing", it.wrong_conference("mlops2027", signs)[0] is None)
    one = it.conference_signs("", "slides final.pdf", "Hello and welcome to Conf42 ML Ops, I am Ada", two)
    check("wrong conference: the greeting alone -> hold, not moved", it.wrong_conference("chaos2027", one)[:2] == ("hold", "mlops2027"))
    none = it.conference_signs("My talk about agents", "deck.pdf", "Hi, I am Ada and today we talk about agents", two)
    check("no signs -> stays where it was filed", it.wrong_conference("chaos2027", none) == (None, None, ""))
    both = it.conference_signs("Conf42 Chaos Engineering 2027", "x.pdf", "welcome to Conf42 MLOps", two)
    check("signs for both -> stays (one each)", it.wrong_conference("chaos2027", both)[0] is None)
    late = it.conference_signs("", "", " ".join(["word"] * 60) + " mlops", two)
    check("the conference named after the greeting is no sign", not late["mlops2027"])
    nested = it.conference_signs("Conf42 Platform Engineering 2027", "", "welcome to platform engineering",
                                 {"a": ("Engineering", "T one"), "b": ("Platform Engineering", "T two")})
    check("a name inside another event's name is never a sign", not nested["a"] and len(nested["b"]) == 2)

    class FakeDrive:
        root, moved, text = "ROOT", [], {}

        def folder(self, parent, name):
            return "%s/%s" % (parent, name)

        def move(self, fid, parent):
            self.moved.append((fid, parent))

        def put_text(self, fid, text, mime="application/json"):
            self.text[fid] = text
    lineups["chaos2027"] = [dict(t, banished=False) for t in lineups["chaos2027"]]
    cloud.intake.youtube.talk_rows = lambda ev: [{"speakers": t["speakers"], "title": t["title"]} for t in lineups[ev["short_url"]]]
    cloud.intake.youtube.talk_page = lambda ev, r: "%s_%s" % (ev["short_url"], r["speakers"].replace(" ", "_"))
    fd = FakeDrive()
    sorter = cloud.intake.Intake(fd, active=active)
    rec, info = {}, {"event": {"slug": "mlops2027"}, "talk": {"k": "mlops2027_Ada_Lovelace", "names": ["Ada Lovelace"], "title": "old"}, "typed": "Ada Lovelace"}
    sorter.refile("mlops2027", {"items": {}}, {"id": "UP", "name": "Ada (x)"}, {"talk.json": {"id": "TJ"}}, info, rec, "chaos2027", "the deck says so")
    import json as _json
    new = _json.loads(fd.text.get("TJ") or "{}")
    check("re-file: the folder moves to the other event", fd.moved == [("UP", "ROOT/chaos2027")] and sorter.refiled == ["chaos2027"])
    check("re-file: talk.json names the other event and talk, the original is kept",
          new.get("event", {}).get("slug") == "chaos2027" and new["talk"]["k"] == "chaos2027_Ada_Lovelace"
          and new["refiled"]["from"] == "mlops2027" and new["refiled"]["talk"]["k"] == "mlops2027_Ada_Lovelace")
    check("re-file: this event forgets the upload", rec["outcome"] == "refiled" and rec["done"] and rec["talk"] is None and rec["refiled_to"] == "chaos2027")
    fd2 = FakeDrive()
    fd2.moved, fd2.text = [], {}
    dry = cloud.intake.Intake(fd2, active=active, dry_run=True)
    dry.refile("mlops2027", {"items": {}}, {"id": "UP", "name": "Ada (x)"}, {"talk.json": {"id": "TJ"}}, info, {}, "chaos2027", "why")
    check("re-file: a dry run moves nothing", not fd2.moved and not fd2.text)

    shutil.rmtree(tmp, ignore_errors=True)
    print("\n%s" % ("ALL PASSED" if not fails else "%d FAILED: %s" % (len(fails), "; ".join(fails))))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
