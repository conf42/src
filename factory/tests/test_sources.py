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

    # ---- captions on older videos never get in the way of the talks' own rollout (Marek 2026-11-16) ----
    import datetime as _dt
    night, noon = _dt.datetime(2027, 1, 5, 5, 30, tzinfo=_dt.timezone.utc), _dt.datetime(2027, 1, 5, 12, 30, tzinfo=_dt.timezone.utc)
    runs = cloud.intake.REPO_RUNS
    cloud.ytupload = __import__("factory.ytupload", fromlist=["x"])
    cloud.ytupload.REPO_RUNS = runs

    def event_state(slug, talks, tube):
        os.makedirs(os.path.join(runs, slug), exist_ok=True)
        with open(os.path.join(runs, slug, "state.json"), "w", encoding="utf-8") as f:
            _json.dump({"talks": talks}, f)
        with open(os.path.join(runs, slug, "youtube.json"), "w", encoding="utf-8") as f:
            _json.dump({k: {"id": "yt"} for k in tube}, f)
    event_state("mlops2027", {"Ada Lovelace": {"finished": "x"}}, ["Ada Lovelace"])
    check("captions: everything on YouTube, nothing in the making, end of YouTube's day -> clear",
          cloud.rollout_clear(["mlops2027"], [], {}, None, night) == (True, ""))
    ok, why = cloud.rollout_clear(["mlops2027"], [], {}, None, noon)
    check("captions: not in the middle of YouTube's day", not ok and "12:00 UTC" in why)
    ok, why = cloud.rollout_clear(["mlops2027"], ["chaos2027: KeyError"], {}, None, night)
    check("captions: not when something failed in the pass", not ok and "failed" in why)
    event_state("mlops2027", {"Ada Lovelace": {"finished": "x"}, "Grace Hopper": {"finished": "x"}}, ["Ada Lovelace"])
    ok, why = cloud.rollout_clear(["mlops2027"], [], {}, None, night)
    check("captions: not while a finished talk waits for its upload", not ok and "Grace Hopper" in why)
    event_state("mlops2027", {"Ada Lovelace": {}}, [])
    ok, why = cloud.rollout_clear(["mlops2027"], [], {}, None, night)
    check("captions: not while an accepted talk is still being made", not ok and "still being made" in why)
    event_state("mlops2027", {"Ada Lovelace": {"finished": "x"}}, ["Ada Lovelace"])
    check("captions: the hours are a setting", cloud.rollout_clear(["mlops2027"], [], {"captions_utc_hours": [10, 14]}, None, noon)[0])

    # ---- what needs a look, for the factory's pages (Marek 2026-11-16) ----
    from factory import problems
    state = {"talks": {"Ada Lovelace": {"finished": "x", "steps": {"qa": {"status": "done", "flags": ["picture changes at 0:00.2 - check the start"]}}},
                       "Grace Hopper": {"error": "Descript said no", "steps": {"edit": {"status": "failed"}}},
                       "Alan Turing": {"finished": "x", "steps": {}}, "Edsger Dijkstra": {"needs_new_video": "no sound"},
                       "Factory Test": {"error": "ignored"}},
             "unmatched": [{"file": "my talk final.mp4", "why": "no speaker in the CSV matches"}]}
    inbox = {"items": {"a": {"folder": "Nobody (x)", "outcome": "hold", "reason": "unmatched"},
                       "b": {"folder": "Junk (x)", "outcome": "reject", "reason": "too-short", "decided": problems.now()},
                       "c": {"folder": "Old junk (x)", "outcome": "reject", "reason": "too-short", "decided": "2020-01-01T00:00:00+00:00"},
                       "d": {"folder": "Broken (x)", "error": "RuntimeError: boom"},
                       "e": {"folder": "Ada (x)", "outcome": "accept", "talk": "Ada Lovelace", "decided": problems.now(),
                             "flags": ["distorted sound", "recorded under chaos2027 - re-filed here, the overlay is swapped"]}}}
    tube = {"Ada Lovelace": {"id": "yt1", "captions": False, "captions_note": "refused"}}
    got = problems.items("mlops2027", state, inbox, tube,
                         ["- left: `deck.pdf` - no speaker of the lineup in the file name - not taken",
                          "- left: `Ada Lovelace.mp4` - Ada Lovelace came through conf42.com/record - the old folder is ignored", "- taken: `x.mp4`"],
                         ["Blocked.mp4 (needs a Google sign-in)"])
    text = " || ".join("%s:%s" % (i["k"], i["t"]) for i in got)
    check("problems: a talk that stopped, with the step", "fail:Grace Hopper: stopped at edit - Descript said no" in text)
    check("problems: a finished talk that is not on YouTube", "fail:Alan Turing is edited but not on YouTube yet" in text)
    check("problems: a talk that needs a new video", "fail:Edsger Dijkstra needs a new video from the speaker - no sound" in text)
    check("problems: held, recently rejected and unsortable uploads", "look:upload Nobody (x) is held: unmatched" in text
          and "look:upload Junk (x) was rejected (too-short)" in text and "fail:upload Broken (x) could not be sorted" in text and "Old junk" not in text)
    check("problems: QA and intake flags, captions that did not go up", "look:Ada Lovelace: picture changes at 0:00.2" in text
          and "look:Ada Lovelace: distorted sound" in text and "the captions did not go up (refused)" in text)
    check("problems: a file nobody is named in, a file Drive would not hand out, a video matching nobody",
          "not taken: deck.pdf" in text and "Drive would not hand out Blocked.mp4" in text and "my talk final.mp4" in text)
    check("problems: a duplicate in a lower folder and a re-filed talk are normal, the test talk is not listed",
          "is ignored" not in text and "re-filed" not in text and "Factory Test" not in text)
    pp = os.path.join(tmp, "problems.json")
    d = problems.write({"mlops2027": got, "chaos2027": []}, [], [problems.item("look", "kept: x.mp4")], "https://github.com/conf42/src/actions/runs/1", pp)
    check("problems: the pass's report (events with nothing are left out)", d["ok"] and list(d["events"]) == ["mlops2027"] and d["all"][0]["t"] == "kept: x.mp4")
    d = problems.write({"chaos2027": [problems.item("fail", "x")]}, ["chaos2027: KeyError"], [], None, pp)
    check("problems: an event the pass did not touch keeps its list; a failure makes the pass not ok",
          not d["ok"] and sorted(d["events"]) == ["chaos2027", "mlops2027"] and d["failed"] == ["chaos2027: KeyError"])
    check("problems: a pass that reported itself is not overwritten by the workflow's last step", not problems.mark("failure", "2000-01-01T00:00:00+00:00", None, pp))
    check("problems: a green pass marks nothing", not problems.mark("success", "2999-01-01T00:00:00+00:00", None, pp))
    check("problems: a pass that died before its report says so", problems.mark("cancelled", "2999-01-01T00:00:00+00:00", "https://github.com/x", pp)
          and "ran out of time" in problems.load(pp)["failed"][0] and problems.load(pp)["ok"] is False and "mlops2027" in problems.load(pp)["events"])

    # ---- Talk Highlights (Marek 2026-11-16): the rules, without video or Claude ----
    from factory import highlights
    ev27 = {"short_url": "mlops2027", "title": "Conf42 MLOps 2027", "date": "2027-01-10"}
    check("highlights: from the set date on, never before it, off when switched off",
          highlights.since({"highlights_from": "2026-11-19"}, ev27) and not highlights.since({"highlights_from": "2027-02-01"}, ev27)
          and not highlights.since({}, ev27) and not highlights.since({"highlights_from": "2026-11-19", "highlights": False}, ev27))
    check("highlights: the PDF's name sits next to the deck's", highlights.name_for("Ada Lovelace", ev27) == "Ada Lovelace - Conf42 MLOps 2027 - Talk Highlights.pdf")
    picks = highlights.clean([{"n": 5, "caption": "  The   retry loop  "}, {"n": 2, "caption": "Config", "crop": [0, 0, 1, .9]},
                              {"n": 2, "caption": "twice"}, {"n": 99, "caption": "no such tile"}, {"n": 3, "caption": ""},
                              {"n": 4, "caption": "cut to nothing", "crop": [0, 0, .3, 1]}, {"n": 6, "caption": "whole", "crop": [0, 0, 1, 1]},
                              {"n": "7", "caption": "not a number"}], 10)
    check("highlights: Claude's picks are checked - known tiles, once, in talk order, tidy captions",
          [p["n"] for p in picks] == [2, 5, 6] and picks[1]["caption"] == "The retry loop")
    check("highlights: a crop is kept when most of the picture stays, a tile whose crop leaves too little goes",
          picks[0]["crop"] == [0.0, 0.0, 1.0, 0.9] and picks[2]["crop"] is None and 4 not in [p["n"] for p in picks])
    check("highlights: never more than the cap", len(highlights.clean([{"n": i, "caption": "x"} for i in range(1, 30)], 40)) == highlights.MAX_GOOD)

    class FakeRun:
        ev, cfg, dir = dict(ev27, db_path=""), {"highlights_from": "2026-11-19"}, os.path.join(tmp, "hl")
        slides_dir, inp = os.path.join(tmp, "hl", "slides"), os.path.join(tmp, "hl", "in")

        def talk(self, key):
            return {"source": "nothing.mp4"}
    os.makedirs(FakeRun.slides_dir)
    os.makedirs(FakeRun.inp)
    check("highlights: no original video on the machine -> none, with the reason", "not on this machine" in highlights.make(FakeRun(), "Ada Lovelace").get("none", ""))
    open(os.path.join(FakeRun.slides_dir, "Ada_Lovelace_slides.pdf"), "wb").close()
    check("highlights: slides in, then no highlights (a deck under the speaker's own file name counts)",
          highlights.make(FakeRun(), "Ada Lovelace") == {"none": "the talk has slides"})
    check("highlights: the test talk gets none", highlights.make(FakeRun(), events.TEST_TALK) == {"none": "the test talk"})
    FakeRun.cfg = {"highlights_from": "2028-01-01"}
    check("highlights: an event before the start date gets none", highlights.make(FakeRun(), "Grace Hopper") == {"none": "before highlights_from"})

    shutil.rmtree(tmp, ignore_errors=True)
    print("\n%s" % ("ALL PASSED" if not fails else "%d FAILED: %s" % (len(fails), "; ".join(fails))))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
