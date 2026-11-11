"""The living blog's planner and linter (skill conf42-blog; never run in CI).

    python -m build.blog_plan plan [--from 2025-01-01] [--today YYYY-MM-DD]   -> JSON on stdout
    python -m build.blog_plan lint                                            -> problems, exit 1 if any
    python -m build.blog_plan add <draft.md>...       upsert drafts (front matter + Markdown body) into _db/blog.csv
    python -m build.blog_plan orphan                  set Status=orphaned on every row whose Ref is gone
    python -m build.blog_plan export <out.json>       the CSV as rows of values, for the Excels_for_WWW "blog" tab
    python -m build.blog_plan release <N>             publish the N newest Status=queued posts (Status -> empty)
    python -m build.blog_plan descript                missing transcripts of finished events from Descript into srt/

Drafts (blog/drafts/<ShortURL>.md, git-ignored) look like:
    ---
    Title: ...
    Description: ...
    Date: 2026-11-12
    ShortURL: 2026-11-12-some-words
    Type: talk
    Ref: talk:mlops2026/Jane Doe
    ---
    Markdown body...
The CSV is never hand-edited: `add` writes it with the csv module (quoting, CRLF as the Drive exports had it).

plan works out every post that SHOULD exist (from metadata.yml, the talk CSVs, sponsors.csv, WEBINARS.csv and the
sister repos next to this one), compares it with _db/blog.csv and reports:
  missing   posts to write, with their Ref, date and the files to read (due first, then backfill by event)
  orphaned  rows whose Ref is gone from the repo (the build already hides them; the skill sets Status=orphaned)
  enrich    talk/sponsored posts whose talk has since got its video or transcript
  waiting_transcript  talk/sponsored posts not proposed yet because the talk has no transcript in the repo
            (Marek 2026-11-10: posts only for talks whose transcript is uploaded), per event - plus rows with
            Status=waiting (written from the abstract before that rule, kept off the site)
  rewrite   Status=waiting rows whose transcript has arrived: rewrite from it, same ShortURL, Status back to empty
  crowded   dates holding more than MAX_PER_DAY posts
It also rewrites _db/sister_events.json, the snapshot the build resolves sister:<repo>/<folder> Refs against.

Date rules (Marek 2026-11-08):
  roundup    the day after the event
  sponsored  only sponsors who deliver a talk; 1 -> day 0, 2 -> -1/0, 3+ -> round robin -1/0/+1
  talk       spread evenly from today (backfill: event -30d) to the day before the event, several a day if needed
  plug       in-person SREday/LLMday/PLATFORMday/PEC event -14d (today when already closer), upcoming events only
  webinar    the webinar's day, once it has happened (the Snoop doc is the source)
"""
import argparse
import collections
import csv
import datetime
import glob
import io
import json
import os
import re
import subprocess
import urllib.parse
import urllib.request
import sys

import yaml

from .blog import BLOG_CSV, SISTER_JSON, WEBINARS_CSV, YOUTUBE_IN_BODY, Resolver, _norm, video_purged
from .shared import read_csv

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # the conf42 repo
GITHUB = os.path.dirname(HERE)
SISTER_REPOS = {   # repo folder -> brand
    "website": "SREday",
    "llmday": "LLMday",
    "platformday": "PLATFORMday",
    "2026.promptengineering.rocks": "PEC",
}
# CONF42 = 42% off, paid events only (Marek 2026-11-08). PLATFORMday is free except London 2027 Q2.
PAID_PLATFORMDAY = {"2027-london-q2"}
PARTNER_LEVELS = {"media", "newsletter", "podcast"}
TALK_BACKFILL_DAYS = 30
MAX_PER_DAY = 6
DUE_WINDOW_DAYS = 7
COLUMNS = ["ExternalURL", "Title", "Description", "Date", "ShortURL", "ThumbnailPath", "Body",
           "Type", "Event", "Ref", "Sponsor", "Author", "Updated", "Status", "Tags"]
TYPES = {"roundup", "sponsored", "talk", "plug", "webinar"}
WORDS = {"talk": (450, 1000), "sponsored": (600, 1500), "roundup": (600, 2000), "plug": (350, 900), "webinar": (400, 1300)}
SLOP = [
    r"in today'?s (fast[- ]paced|rapidly|ever)", r"\bdelve", r"game[- ]changer", r"\blandscape\b", r"no longer just",
    r"\bunlock(s|ing)?\b", r"\bseamless(ly)?\b", r"\bit'?s not (just )?\w+[^.]{0,40}, it'?s\b", r"\bStill\.\s*$",
    r"\bin the (ever-)?evolving\b", r"\bnavigat(e|ing) the complexities\b", r"\brevolutioni[sz]", r"\bharness the power\b",
    r"\btapestry\b", r"\bembark\b", r"\bmoreover\b", r"\bfurthermore\b", r"\bat the end of the day\b", r"\bbuckle up\b",
    r"\bsupercharg", r"\bcutting[- ]edge\b", r"\bparadigm shift\b", r"\btestament to\b", r"\bdeep dive\b",
]


def _date(s):
    return datetime.date.fromisoformat(str(s)[:10])


def load_context():
    from .events import get_enriched_metadata
    import contextlib
    with contextlib.redirect_stdout(io.StringIO()):   # the loader is chatty; plan prints JSON only
        ctx = get_enriched_metadata("./docs")
    ctx["sponsors"] = read_csv("./_db/sponsors.csv")
    return ctx


# ---------------------------------------------------------------- sister events

def sister_events():
    out = []
    for repo, brand in SISTER_REPOS.items():
        root = os.path.join(GITHUB, repo)
        for meta in glob.glob(os.path.join(root, "*", "metadata.yml")) + glob.glob(os.path.join(root, "past", "*", "metadata.yml")):
            folder = os.path.basename(os.path.dirname(meta))
            if not re.match(r"^\d{4}-", folder):
                continue
            try:
                with open(meta) as f:
                    m = yaml.safe_load(f) or {}
            except Exception:
                continue
            if not m.get("start_time"):
                continue
            date = _date(m["start_time"])
            domain = m.get("brand_domain") or ""
            hero = (m.get("hero_pictures") or [""])[0]
            talks_csv = os.path.join(os.path.dirname(meta), "_db", "talks.csv")
            # the sites' own rule: metadata registration_free wins (Chennai, Warsaw, Tel Aviv are free), else
            # PLATFORMday is free and the rest are paid
            if m.get("registration_free") is not None:
                paid = not m["registration_free"]
            else:
                paid = brand != "PLATFORMday" or folder in PAID_PLATFORMDAY
            out.append(dict(
                ref="sister:%s/%s" % (repo, folder), repo=repo, folder=folder, brand=m.get("brand_name") or brand,
                date=date.isoformat(), date_string=m.get("date_string") or "", city=m.get("city_name") or "",
                venue=m.get("location_string") or "", luma_evt=m.get("luma_evt") or "",
                luma_url=("https://luma.com/event/" + m["luma_evt"]) if m.get("luma_evt") else "",
                url="https://%s/%s" % (domain, folder) if domain else "", domain=domain, paid=paid,
                code="CONF42" if paid else "",
                image=(None if "/past/" in meta else _og_image("https://%s/%s/" % (domain, folder) if domain else ""))
                      or ("https://%s/photos/%s" % (domain, hero.split("/")[-1]) if domain and hero else ""),
                past="/past/" in meta, talks_csv=os.path.relpath(talks_csv, HERE) if os.path.exists(talks_csv) else "",
            ))
    for e in out:
        e["card"] = _card_copy(e["image"])
    out.sort(key=lambda e: (e["date"], e["ref"]))
    return out


def _og_image(url):
    """the event's own splash (Marek 2026-11-09: plugs show the sister event's splash, not a venue photo) - the og:image
    its live page publishes; "" when the page can't be read"""
    import urllib.request
    if not url:
        return ""
    try:
        html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "conf42-blog"}), timeout=20).read().decode("utf-8", "replace")
    except Exception:
        return ""
    m = re.search(r'<meta property="og:image" content="([^"]+)"', html)
    return m.group(1) if m else ""


CARD_DIR = "docs/assets/blog/sisters"


def _card_copy(url):
    """the sister cover for the blog card without its FREE / discount ball (Marek 2026-11-11: the 16:9 crop cut it to
    "FRE"): docs/assets/blog/sisters/<hash>.jpg, made once per cover; "" when there is no ball or the cover can't be
    read (the card then shows the cover as it is)"""
    import hashlib
    import urllib.request
    if not url or "/og/" not in url:
        return ""
    out = "%s/%s.jpg" % (CARD_DIR, hashlib.sha1(url.encode()).hexdigest()[:16])
    if os.path.exists(os.path.join(HERE, out)):
        return out.replace("docs/", "./", 1)
    try:
        from PIL import Image
        raw = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "conf42-blog"}), timeout=20).read()
        clean = remove_corner_ball(Image.open(io.BytesIO(raw)))
    except Exception:
        return ""
    if clean is None:
        return ""
    os.makedirs(os.path.join(HERE, CARD_DIR), exist_ok=True)
    clean.save(os.path.join(HERE, out), quality=88, optimize=True)
    return out.replace("docs/", "./", 1)


def remove_corner_ball(im):
    """-> image without the white sticker ball touching the top-right corner, or None when there is none."""
    from PIL import Image, ImageDraw, ImageFilter
    im = im.convert("RGB"); W, H = im.size; px = im.load()
    def white(p): return min(p) > 225
    # flood fill the white connected to the corner, within the top-right quarter
    x0, y1 = int(W * .62), int(H * .5)
    seed = next(((x, y) for y in range(0, 6) for x in range(W - 1, W - 7, -1) if white(px[x, y])), None)
    if not seed:
        return None
    seen = {seed}; stack = [seed]
    while stack:
        x, y = stack.pop()
        for nx, ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if x0 <= nx < W and 0 <= ny < y1 and (nx, ny) not in seen and white(px[nx, ny]):
                seen.add((nx, ny)); stack.append((nx, ny))
    if len(seen) < W * H * .01:
        return None
    # the ball's text is in the background colour: fill each row of the region from its leftmost white pixel to the edge
    rows = {}
    for x, y in seen:
        rows[y] = min(rows.get(y, W), x)
    mask = Image.new("L", (W, H), 0); d = ImageDraw.Draw(mask)
    for y, x in rows.items():
        d.line([(x, y), (W, y)], fill=255)
    mask = mask.filter(ImageFilter.MaxFilter(15))          # the anti-aliased rim
    m = mask.load(); out = im.copy(); o = out.load(); last = None
    for y in range(H):
        xs = [x for x in range(x0 - 10, W) if m[x, y]]
        if not xs:
            continue
        left = xs[0] - 4
        sample = [px[x, y] for x in range(max(0, left - 12), left)]
        c = tuple(sorted(s[i] for s in sample)[len(sample) // 2] for i in range(3))
        # the sky to the left of the ball is flat; a row that runs into line art (a tower top) keeps the sky above it
        lum = [sum(s) / 3 for s in sample]
        if last and (max(lum) - min(lum) > 18 or sum(c) / 3 > sum(last) / 3 + 12):
            c = last
        last = c
        for x in xs:
            o[x, y] = c
    # soften the patched rows so the fill blends with the sky gradient
    blur = out.filter(ImageFilter.GaussianBlur(6))
    out.paste(blur, mask=mask.filter(ImageFilter.GaussianBlur(4)))
    return out


def write_sister_json(events):
    with open(SISTER_JSON, "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=1)
        f.write("\n")


# ---------------------------------------------------------------- sources

def transcript_paths(event, talk):
    paths = []
    yid = talk.get("YouTubeId")
    if yid and os.path.exists("./assemblyai/%s.json" % yid) and os.path.getsize("./assemblyai/%s.json" % yid) > 2:   # an empty file is no transcript
        paths.append("assemblyai/%s.json" % yid)
    srt = ("srt/%s_%s.srt" % (event["short_url"], talk.get("Name1", ""))).replace(" ", "_")
    if "#" not in talk_ref(event, talk) and os.path.exists(srt) and os.path.getsize(srt) > 2:
        paths.append(srt)
    return paths


def transcript_text(event, talk):
    """Plain text of the talk's transcript (assemblyai text, else the srt without numbers/timestamps), or ''."""
    for p in transcript_paths(event, talk):
        try:
            if p.endswith(".json"):
                with open(p) as f:
                    return json.load(f).get("text") or ""
            with open(p) as f:
                lines = [l for l in f.read().splitlines() if l.strip() and not l.strip().isdigit() and "-->" not in l]
            return " ".join(lines)
        except Exception:
            continue
    return ""


def sponsor_of(event, talk, sponsors_by_id):
    """The sponsor id whose company delivers this talk, or None."""
    companies = {_norm(talk.get("Company1")), _norm(talk.get("Company2"))} - {""}
    for level, ids in (event.get("sponsors") or {}).items():
        if level in PARTNER_LEVELS:
            continue
        for sid in ids or []:
            names = {_norm(sid), _norm((sponsors_by_id.get(sid) or {}).get("name"))}
            if companies & names:
                return sid
    return None


def splash_for_sponsor(event, sid, sponsors_by_id):
    name = re.sub(r"\W+", "", (sponsors_by_id.get(sid) or {}).get("name") or sid).lower()
    # only this event's own sponsor splash (<EVENT><YEAR>_<Sponsor>.png); another event's would mislabel the post
    for f in sorted(glob.glob("./docs/assets/splash/*_*.png")):
        prefix, _, rest = os.path.basename(f)[:-4].partition("_")
        if prefix.lower() == event.get("short_url", "").lower() and name and name == re.sub(r"\W+", "", rest).lower():
            return f.replace("./docs/", "./")
    return ""


STATIC_SLIDES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "static", "slides")


def slides_path(event, talk):
    """The talk's deck in the sibling static repo (static/slides/), or ''. Marek 2026-11-10: use the slides for
    content (facts, numbers, structure), never visuals - read with pypdf."""
    from .shared import conventional_slides_name
    for name in ((talk.get("Slides") or "").strip().rsplit("/", 1)[-1], conventional_slides_name(event, talk)):
        if name and name.lower().endswith(".pdf"):
            p = os.path.normpath(os.path.join(STATIC_SLIDES, name))
            if os.path.exists(p):
                return p
    return ""


def talk_brief(event, talk):
    names = [n for n in (talk.get("Name1"), talk.get("Name2")) if n]
    return dict(
        title=talk.get("Title"), speakers=names,
        companies=[c for c in (talk.get("Company1"), talk.get("Company2")) if c],
        url="https://www.conf42.com/" + talk["short_url"], youtube=talk.get("YouTube") or "",
        keywords=talk.get("Keywords") or "", transcripts=transcript_paths(event, talk), slides=slides_path(event, talk),
        featured=(talk.get("Featured") or "").lower() == "yes",
    )


def talk_ref(event, talk):
    """"<event>/<Name1>" for a Ref; a speaker's 2nd+ talk at the same event (CSV order) gets "#<YouTubeId>",
    so each of their talks has its own post (Resolver.talk matches it)."""
    ref = "%s/%s" % (event["short_url"], talk["Name1"])
    for t in event.get("talks_raw") or []:
        if t is talk:
            return ref
        if _norm(t.get("Name1")) == _norm(talk["Name1"]):
            return ref + "#" + (talk.get("YouTubeId") or "")
    return ref


# ---------------------------------------------------------------- the plan

def spread(n, start, end):
    """n dates spread evenly over [start, end] (several per day when n > days)."""
    if end < start:
        end = start
    days = (end - start).days + 1
    return [start + datetime.timedelta(days=(i * days) // n) for i in range(n)]


def wanted_posts(ctx, sisters, since, today):
    sponsors_by_id = {s["id"]: s for s in ctx["sponsors"]}
    want = []
    for event in ctx["events"]:
        if "external_url" in event or not event.get("short_url") or event["date"] < since:
            continue
        talks = [t for t in event.get("talks_raw") or [] if (t.get("Name1") or "").strip()]
        if not talks:
            continue
        su, d = event["short_url"], event["date"]
        ev = dict(event=su, event_name="Conf42 %s %s" % (event["name"], event["year"]), event_date=d.isoformat(),
                  event_url="https://www.conf42.com/" + su, past=d < today)
        want.append(dict(ev, type="roundup", ref="event:" + su, date=d + datetime.timedelta(days=1),
                         image="", sources=dict(talks_csv=event.get("db_path"), talks=len(talks))))
        sponsored, plain = [], []
        for t in sorted(talks, key=lambda t: (t.get("Featured") or "").lower() != "yes"):
            sid = sponsor_of(event, t, sponsors_by_id)
            (sponsored if sid else plain).append((t, sid))
        offsets = [0] if len(sponsored) == 1 else [-1, 0] if len(sponsored) == 2 else [-1, 0, 1]
        for i, (t, sid) in enumerate(sponsored):
            s = sponsors_by_id.get(sid) or {}
            want.append(dict(ev, type="sponsored", ref="sponsor:%s/%s/%s" % (su, sid, talk_ref(event, t).split("/", 1)[1]),
                             date=d + datetime.timedelta(days=offsets[i % len(offsets)]), sponsor=sid,
                             sponsor_name=s.get("name"), sponsor_url=s.get("url"),
                             image=splash_for_sponsor(event, sid, sponsors_by_id), sources=talk_brief(event, t),
                             ready=bool(transcript_paths(event, t))))
        if is_remix(event):
            continue   # Remix re-airs earlier talks (Marek 2026-11-10): only the roundup + sponsored posts, no talk posts
        start = d - datetime.timedelta(days=TALK_BACKFILL_DAYS) if d <= today else today
        dates = spread(len(plain), start, d - datetime.timedelta(days=1)) if plain else []
        for (t, _), date in zip(plain, dates):
            # only once the transcript is in the repo (Marek 2026-11-10): posts are written from what was said
            want.append(dict(ev, type="talk", ref="talk:" + talk_ref(event, t), date=date, image="",
                             sources=talk_brief(event, t), ready=bool(transcript_paths(event, t))))
    for s in sisters:
        if s["past"] or _date(s["date"]) < today:
            continue
        want.append(dict(type="plug", ref=s["ref"], event="", event_name="%s %s" % (s["brand"], s["city"]),
                         event_date=s["date"], past=False, image=s["image"],
                         date=max(today, _date(s["date"]) - datetime.timedelta(days=14)),
                         sources=dict(s)))
    try:
        webinars = read_csv(WEBINARS_CSV)
    except Exception:
        webinars = []
    for w in webinars:
        if not w.get("Slug") or not w.get("Date") or _date(w["Date"]) < since:
            continue
        held = _date(w["Date"]) <= today
        want.append(dict(type="webinar", ref="webinar:" + w["Slug"], event="", event_name=w.get("Title"),
                         event_date=w["Date"], past=held, date=_date(w["Date"]), image="",
                         ready=held, sources=dict(title=w.get("Title"), luma=w.get("LumaURL"), youtube=w.get("YouTube"),
                                                  hosts=[w.get("Name1"), w.get("Name2")],
                                                  snoop_doc="Drive folder 'Snoop', title '%s HH:MM · %s'" % (w["Date"], w.get("Title")))))
    return want


def read_blog_rows(text=None):
    if text is None:
        with open(BLOG_CSV, encoding="utf-8") as f:
            text = f.read()
    return list(csv.DictReader(io.StringIO(text)))


def is_remix(event_or_ref):
    """Remix events re-air talks from earlier events, so they get no talk posts (Marek 2026-11-10)."""
    if isinstance(event_or_ref, dict):
        return (event_or_ref.get("name") or "").strip().lower() == "remix"
    return (event_or_ref or "").lower().startswith("talk:remix")


def plan(args):
    today = _date(args.today) if args.today else datetime.datetime.now(datetime.timezone.utc).date()
    since = _date(args.since)
    sisters = sister_events()
    write_sister_json(sisters)
    ctx = load_context()
    rows = read_blog_rows()
    have = {(r.get("Ref") or "").strip() for r in rows if (r.get("Ref") or "").strip()}
    want = wanted_posts(ctx, sisters, since, today)

    missing, waiting = [], collections.Counter()
    for w in want:
        if w["ref"] in have:
            continue
        if w.get("ready") is False:
            if w["type"] in ("talk", "sponsored"):
                waiting[w.get("event") or "?"] += 1   # no transcript yet: listed, not written
            continue
        w["date"] = w["date"].isoformat()
        w["due"] = not w["past"] or w["type"] == "plug" or _date(w["date"]) >= today - datetime.timedelta(days=DUE_WINDOW_DAYS)
        missing.append(w)
    due = sorted([m for m in missing if m["due"]], key=lambda m: m["date"])
    backlog = collections.OrderedDict()
    for m in sorted([m for m in missing if not m["due"]], key=lambda m: (m["event_date"], m["type"] != "roundup"), reverse=True):
        backlog.setdefault(m["event"] or m["ref"], []).append(m)
    # backfill order (Marek: roundups + sponsored for every 2025+ event first, then talk posts one event per run)
    first = [m for ms in backlog.values() for m in ms if m["type"] in ("roundup", "sponsored", "webinar")]
    talk_events = [dict(event=k, count=len([m for m in ms if m["type"] == "talk"])) for k, ms in backlog.items()
                   if any(m["type"] == "talk" for m in ms)]
    for i, te in enumerate(talk_events):   # the next event to backfill comes with its items (--all: every event)
        if i and not getattr(args, "all", False):
            break
        te["items"] = sorted([m for m in backlog[te["event"]] if m["type"] == "talk"], key=lambda m: m["date"])

    resolver = Resolver(ctx["events"], ctx["sponsors"])
    orphaned, enrich, rewrite = [], [], []
    for r in rows:
        ref = (r.get("Ref") or "").strip()
        if not ref or (r.get("Status") or "").strip().lower() in ("orphaned", "hidden"):
            continue
        ok, linked = resolver.resolve(ref)
        if not ok:
            orphaned.append(dict(ShortURL=r.get("ShortURL"), Ref=ref, Title=r.get("Title")))
            continue
        talk, event = linked.get("talk"), linked.get("event")
        if (r.get("Status") or "").strip().lower() == "waiting":
            # written from the abstract before "transcript first" (Marek 2026-11-10): off the site until the transcript
            # lands, then rewritten from it under the same ShortURL (re-`add`, Status back to empty)
            if talk and transcript_paths(event, talk):
                rewrite.append(dict(ShortURL=r.get("ShortURL"), Ref=ref, Title=r.get("Title"), transcripts=transcript_paths(event, talk),
                                    sources=talk_brief(event, talk)))
            else:
                waiting[r.get("Event") or "?"] += 1
            continue
        if talk and talk.get("YouTubeId") and talk["YouTubeId"] not in (r.get("Body") or ""):
            enrich.append(dict(ShortURL=r.get("ShortURL"), Ref=ref, youtube=talk.get("YouTube"),
                               transcripts=transcript_paths(event, talk)))

    # one video linked from two talks = a copy-paste slip in the sheet (Marek fixes the sheet; never write from it)
    by_video = collections.defaultdict(list)
    for ev in ctx["events"]:
        for t in ev.get("talks_raw") or []:
            yid = re.split(r"[?&#]", (t.get("YouTube") or "").strip().split("/")[-1])[0]
            if yid:
                by_video[yid].append("%s/%s" % (ev.get("short_url", "").replace(".html", ""), t.get("Name1")))
    shared_video = {y: who for y, who in by_video.items() if len({w.split("/", 1)[1] for w in who}) > 1}   # Remix re-airs: same speaker, fine
    per_day = collections.Counter([r.get("Date", "")[:10] for r in rows if r.get("Date", "") >= today.isoformat()] + [m["date"] for m in due])
    out = dict(
        today=today.isoformat(),
        due=due,
        backfill_next=first,
        backfill_talk_events=talk_events,
        orphaned=orphaned,
        enrich=enrich,
        shared_video=shared_video,
        waiting_transcript=dict(waiting.most_common()),
        rewrite=rewrite,
        crowded={d: n for d, n in sorted(per_day.items()) if n > MAX_PER_DAY},
        counts=dict(rows=len(rows), due=len(due), backfill_first=len(first),
                    backfill_talks=sum(e["count"] for e in talk_events), orphaned=len(orphaned), enrich=len(enrich),
                    waiting_transcript=sum(waiting.values()), rewrite=len(rewrite)),
    )
    json.dump(out, sys.stdout, indent=1, default=str, ensure_ascii=False)
    print()


# ---------------------------------------------------------------- lint

def _words(text):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’-]*", re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text or "")))


def _squash(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def lint(args):
    return lint_rows(read_blog_rows(), verbose=args.verbose)


def check(args):
    """lint drafts without touching _db/blog.csv (safe while other writers are busy)"""
    rows = read_blog_rows()
    by_slug = {r.get("ShortURL"): i for i, r in enumerate(rows)}
    only = set()
    for path in args.drafts:
        new = parse_draft(path)
        new.setdefault("Author", "Conf42")
        only.add(new.get("ShortURL"))
        if new.get("ShortURL") in by_slug:
            rows[by_slug[new["ShortURL"]]] = dict(rows[by_slug[new["ShortURL"]]], **new)
        else:
            rows.append(new)
    return lint_rows(rows, only=only, verbose=args.verbose)


def lint_rows(rows, only=None, verbose=False):
    try:
        old_text = subprocess.check_output(["git", "show", "HEAD:" + BLOG_CSV.lstrip("./")], cwd=HERE).decode()
        old = {r.get("ShortURL") or r.get("Title"): r for r in read_blog_rows(old_text)}
    except Exception:
        old = {}
    problems = []

    def bad(row, msg):
        problems.append("%s: %s" % (row.get("ShortURL") or row.get("Title"), msg))

    header = list(rows[0].keys()) if rows else []
    if header[:len(COLUMNS)] != COLUMNS:
        problems.append("header: expected %s" % ",".join(COLUMNS))

    # legacy rows (before 2025) are frozen
    for key, r in old.items():
        if r.get("Date", "") < "2025" and not (r.get("Ref") or "").strip() and key not in {x.get("ShortURL") or x.get("Title") for x in rows}:
            problems.append("%s: pre-2025 row deleted" % key)
    seen_slug, seen_ref = collections.Counter(), collections.Counter()
    for r in rows:
        seen_slug[r.get("ShortURL")] += 1
        if (r.get("Ref") or "").strip() and (r.get("Status") or "").lower() != "orphaned":
            seen_ref[r["Ref"].strip()] += 1
    ctx = None
    sisters = None
    talk_urls = None
    for r in rows:
        key = r.get("ShortURL") or r.get("Title")
        if only is not None and r.get("ShortURL") not in only:
            continue
        before = old.get(key)
        if before and before.get("Date", "") < "2025" and not (before.get("Ref") or "").strip():
            if any((before.get(c) or "") != (r.get(c) or "") for c in COLUMNS[:7]):
                bad(r, "pre-2025 row changed (leave the past ones as they are)")
            continue
        if before and before == r:
            continue   # untouched since the last commit
        if before and all((before.get(c) or "") == (r.get(c) or "") for c in COLUMNS[:7]):
            # a hand-written post that only got its Type/Ref: the text stays as written, the Ref must resolve
            if ctx is None:
                ctx = load_context()
                sisters = {s["ref"]: s for s in sister_events()}
                resolver = Resolver(ctx["events"], ctx["sponsors"])
                sponsors_by_id = {s["id"]: s for s in ctx["sponsors"]}
            if (r.get("Ref") or "").strip() and not resolver.resolve(r["Ref"])[0]:
                bad(r, "Ref does not resolve: %s" % r["Ref"])
            continue
        if r.get("ShortURL") and seen_slug[r["ShortURL"]] > 1:
            bad(r, "duplicate ShortURL")
        if (r.get("Ref") or "").strip() and seen_ref[r["Ref"].strip()] > 1:
            bad(r, "duplicate Ref")
        if (r.get("Status") or "").lower() in ("orphaned", "hidden"):
            continue
        typ = (r.get("Type") or "").strip()
        if not typ:
            continue   # a hand-written post without a type: nothing to check against
        if typ not in TYPES:
            bad(r, "unknown Type %r" % typ)
            continue
        for col in ("Title", "Description", "Date", "ShortURL", "Ref", "Body"):
            if not (r.get(col) or "").strip():
                bad(r, "empty " + col)
        if r.get("Title", "") != r.get("Title", "").strip():
            bad(r, "Title has leading/trailing whitespace")
        if len(r.get("Description") or "") > 170:
            bad(r, "Description over 170 chars (%d)" % len(r["Description"]))
        if typ == "talk" and is_remix(r.get("Ref")) and (r.get("Status") or "").lower() != "skipped":
            bad(r, "Remix re-airs talks: only the roundup and sponsored posts, no talk posts (Status skipped)")
        if typ in ("talk", "sponsored") and "Conf42" not in (r.get("Description") or ""):
            # the Description is the post's visible "In short" line, the passage AI answers quote: "<Speaker> at Conf42
            # <Event> <Year> on ..." keeps the attribution in the quote (2026-11-10)
            bad(r, "Description must say where the talk was: '<Speaker> at Conf42 <Event> <Year> on ...'")
        if (r.get("Event") or "").strip():
            # posts of an event live under it (Marek 2026-11-09: the conference is always in the URL, so similar talks
            # at two events - Remix re-airs, sponsors' repeat talks - never look like duplicates)
            if not re.match(r"^%s/[a-z0-9]+(-[a-z0-9]+)*$" % re.escape(r["Event"].strip()), r.get("ShortURL") or ""):
                bad(r, "ShortURL must be <Event>/lowercase-words (%s/...)" % r["Event"].strip())
        elif not re.match(r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(-[a-z0-9]+)*$", r.get("ShortURL") or ""):
            bad(r, "ShortURL must be YYYY-MM-DD-lowercase-words")
        elif r["ShortURL"][:10] != (r.get("Date") or "")[:10]:
            bad(r, "ShortURL date differs from Date")
        body = r.get("Body") or ""
        n = _words(body)
        lo, hi = WORDS[typ]
        if not lo <= n <= hi:
            bad(r, "%d words, %s posts want %d-%d" % (n, typ, lo, hi))
        for pat in SLOP:
            m = re.search(pat, body, re.I | re.M)
            if m:
                bad(r, "slop phrase %r" % m.group(0))
        m = re.search(r"\b(the CSV (says|lists|has|gives|row|entry)|in the CSV|CSV (row|listing)|listed (with|as|under) [A-Z])", body + " " + (r.get("Description") or ""))
        if m:   # our data is not the story; an empty Company1 means the speaker keeps the employer private (Marek 2026-11-09)
            bad(r, "talks about our data / the speaker's listing: %r" % m.group(0))
        if body.count("—") > max(2, n // 150):
            bad(r, "%d em dashes - write sentences" % body.count("—"))
        if re.match(r"^\s*#(?!#)", body):
            bad(r, "Body starts with a # heading (the page prints the Title)")

        if ctx is None:
            ctx = load_context()
            sisters = {s["ref"]: s for s in sister_events()}
            resolver = Resolver(ctx["events"], ctx["sponsors"])
            sponsors_by_id = {s["id"]: s for s in ctx["sponsors"]}
        ok, linked = resolver.resolve(r.get("Ref"))
        if not ok:
            bad(r, "Ref does not resolve: %s" % r.get("Ref"))
            continue
        # talk links must point at talks the repo still has (docs/ keeps pages of removed talks locally)
        if talk_urls is None:
            talk_urls = {t["short_url"] for e in ctx["events"] for t in (e.get("talks_raw") or []) if t.get("short_url")}
        for u in re.findall(r"conf42\.com/([A-Za-z0-9.\-]+_[A-Za-z0-9_.\-]+)", body):
            if u not in talk_urls and not u.startswith(("speaker_", "assets")):
                bad(r, "link to a talk that is not in the repo: /%s" % u)
        talk, event = linked.get("talk"), linked.get("event")
        if typ in ("talk", "sponsored") and talk and talk["short_url"] not in body:
            bad(r, "no link to the talk page /%s" % talk["short_url"])
        if typ == "roundup" and event and ("conf42.com/" + event["short_url"]) not in body:
            bad(r, "no link to the event page /%s" % event["short_url"])
        if typ == "sponsored":
            s = sponsors_by_id.get(r["Ref"].split(":", 1)[1].split("/")[1]) or {}
            dom = re.sub(r"^https?://(www\.)?", "", s.get("url") or "").split("/")[0]
            if dom and dom not in body:
                bad(r, "no link to the sponsor (%s)" % dom)
        if typ == "plug":
            s = sisters.get(r["Ref"]) or {}
            if s.get("luma_evt") and s["luma_evt"] not in body and "luma.com" not in body and "lu.ma" not in body:
                bad(r, "no Luma registration link")
            if s.get("paid") and "CONF42" not in body:
                bad(r, "paid event: the CONF42 code (42% off) is missing")
            if not s.get("paid") and "CONF42" in body:
                bad(r, "free event: drop the CONF42 code")
        if typ == "webinar" and "CONF42" in body:
            bad(r, "webinars are free: no code")

        # every quote must be in the source (the talk's transcript/abstract; roundups: any talk of the event)
        quotes = re.findall(r"[\"“]([^\"”]{25,400})[\"”]", body)
        if quotes and typ in ("talk", "sponsored", "roundup"):
            pool = []
            for t in ([talk] if talk else (event or {}).get("talks_raw") or []):
                pool += [transcript_text(event, t), t.get("Abstract") or "", t.get("Title") or ""]
            source = _squash(" ".join(pool))
            for q in quotes:
                if _squash(q) not in source:
                    bad(r, "quote not found in the transcript/abstract: %r" % q[:80])
        if verbose:
            print("ok-checked", key, typ, n, "words")
    for p in problems:
        print(p)
    print("lint: %d problem(s)" % len(problems))
    return 1 if problems else 0


def write_blog_rows(rows):
    with open(BLOG_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k) or "" for k in COLUMNS})


def parse_draft(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit("%s: no front matter" % path)
    meta = yaml.safe_load(m.group(1)) or {}
    row = {k: str(v).strip() if v is not None else "" for k, v in meta.items()}
    unknown = set(row) - set(COLUMNS)
    if unknown:
        raise SystemExit("%s: unknown fields %s" % (path, sorted(unknown)))
    row["Body"] = m.group(2).strip() + "\n"
    return row


def add(args):
    rows = read_blog_rows()
    by_slug = {r.get("ShortURL"): r for r in rows}
    today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    for path in args.drafts:
        new = parse_draft(path)
        slug = new.get("ShortURL")
        old = by_slug.get(slug)
        if old:
            if old.get("Date", "") < "2025" and not (old.get("Ref") or "").strip():
                raise SystemExit("%s: pre-2025 rows are frozen" % slug)   # legacy posts; typed rows (e.g. DevOps 2025 talks dated Dec 2024) stay editable
            changed = any((old.get(k) or "").strip() != (new.get(k) or "").strip() for k in ("Title", "Description", "Body", "ThumbnailPath"))
            if changed and old.get("Date", "")[:10] < today and "Updated" not in new:
                new["Updated"] = today   # a real edit of a live post moves dateModified / sitemap lastmod
            old.update(new)
            print("updated", slug)
        else:
            new.setdefault("Author", "Conf42")
            rows.append(new)
            by_slug[slug] = new
            print("added", slug)
    rows.sort(key=lambda r: (r.get("Date") or "")[:10], reverse=True)
    write_blog_rows(rows)


def replace(args):
    """Status=replaced:<new ShortURL> on an older post the new one supersedes (Marek 2026-11-09: duplicates -> keep the
    new post, purge the old). The old row stays for history; the build turns its URL into a redirect to the new post."""
    rows = read_blog_rows()
    by = {r.get("ShortURL"): r for r in rows}
    for pair in args.pairs:
        old, _, new = pair.partition("=")
        if old not in by or new not in by:
            raise SystemExit("unknown ShortURL in %r" % pair)
        by[old]["Status"] = "replaced:" + new
        print("replaced", old, "->", new)
    write_blog_rows(rows)


def release(args):
    """Status=queued holds a written post back (Marek 2026-11-09: big backfills go out over 2-3 days, not at once).
    Sponsored posts first (Marek 2026-11-11), then newest first: recent events are what readers (and crawlers) care
    about most."""
    rows = read_blog_rows()
    queued = sorted([r for r in rows if (r.get("Status") or "").strip().lower() == "queued"],
                    key=lambda r: ((r.get("Type") or "") == "sponsored", r.get("Date") or ""), reverse=True)
    for r in queued[:args.n]:
        r["Status"] = ""
        print("released", r.get("ShortURL"))
    write_blog_rows(rows)
    print("queued left: %d" % max(0, len(queued) - args.n))


def video_gone(yid):
    """True when YouTube says the video doesn't exist (deleted or private); a network hiccup counts as alive."""
    import urllib.error
    import urllib.request
    try:
        urllib.request.urlopen("https://www.youtube.com/oembed?format=json&url=https://youtu.be/" + yid, timeout=20)
        return False
    except urllib.error.HTTPError as e:
        return e.code in (401, 403, 404)
    except Exception:
        return False


def orphan(args):
    """Status=orphaned on rows whose Ref is gone, whose talk lost its YouTube link, or whose linked video YouTube no
    longer has (purged videos take their post with them, Marek 2026-11-09)."""
    import concurrent.futures
    ctx = load_context()
    resolver = Resolver(ctx["events"], ctx["sponsors"])
    rows = read_blog_rows()
    live = [r for r in rows if (r.get("Ref") or "").strip() and (r.get("Status") or "").lower() not in ("orphaned", "hidden")]
    why = {}
    for r in live:
        ok, linked = resolver.resolve(r["Ref"])
        if not ok:
            why[id(r)] = "Ref gone"
        elif video_purged(r, linked):
            why[id(r)] = "video link removed"
    ids = sorted({m.group(1) for r in live if id(r) not in why for m in YOUTUBE_IN_BODY.finditer(r.get("Body") or "")})
    if getattr(args, "offline", False):
        ids = []   # GitHub runners: YouTube may refuse datacenter IPs - only the repo-side checks (Ref gone, link removed)
    with concurrent.futures.ThreadPoolExecutor(24) as pool:
        dead = {y for y, gone in zip(ids, pool.map(video_gone, ids)) if gone}
    if len(dead) > max(10, len(ids) // 50):
        # a purge is a handful of videos; hundreds "gone" at once means YouTube refused us - write nothing
        raise SystemExit("orphan: %d of %d videos look deleted - YouTube is probably blocking the checks; nothing written"
                         % (len(dead), len(ids)))
    for r in live:
        if id(r) not in why and any(m.group(1) in dead for m in YOUTUBE_IN_BODY.finditer(r.get("Body") or "")):
            why[id(r)] = "video deleted on YouTube"
    # one video under two speakers' talks (a sheet slip): YouTube's title names the real speaker; the other post is held
    # back (hidden, not orphaned - it comes back once the sheet has the right link)
    by_video = collections.defaultdict(list)
    for r in live:
        if id(r) not in why:
            ok, linked = resolver.resolve(r["Ref"])
            yid = re.split(r"[?&#]", ((linked.get("talk") or {}).get("YouTubeId") or ""))[0]
            if yid:
                by_video[yid].append((r, linked["talk"].get("Name1") or ""))
    held = []
    for yid, posts in by_video.items():
        if getattr(args, "offline", False) or len({n for _, n in posts}) < 2:
            continue
        try:
            title = json.load(urllib.request.urlopen("https://www.youtube.com/oembed?format=json&url=https://youtu.be/" + yid, timeout=20))["title"]
        except Exception:
            continue
        for r, name in posts:
            if _norm(name) not in _norm(title):
                r["Status"] = "hidden"
                held.append(r)
                print("hidden", r.get("ShortURL"), r.get("Ref"), "- links %s, which is %r" % (yid, title))
    for r in live:
        if id(r) in why:
            r["Status"] = "orphaned"
            print("orphaned", r.get("ShortURL"), r.get("Ref"), "-", why[id(r)])
    write_blog_rows(rows)
    print("%d row(s) orphaned, %d held for a wrong video link (%d videos checked)" % (len(why), len(held), len(ids)))


def export(args):
    rows = read_blog_rows()
    values = [COLUMNS] + [[r.get(k) or "" for k in COLUMNS] for r in rows]
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(values, f, ensure_ascii=False)
    print("%d rows x %d columns -> %s" % (len(values), len(COLUMNS), args.out))


# ---------------------------------------------------------------- transcripts from Descript

DESCRIPT_API = "https://descriptapi.com/v1"


def _descript_token():
    t = os.environ.get("DESCRIPT_API_TOKEN", "").strip()
    path = os.path.join(os.path.expanduser("~"), ".conf42-factory", "descript_token")   # the factory's own (machine.py)
    if not t and os.path.exists(path):
        with open(path) as f:
            t = f.read().strip()
    return t


def _descript(token, path, params=None, body=None):
    url = DESCRIPT_API + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None,
                                 headers={"Authorization": "Bearer " + token, "Content-Type": "application/json"},
                                 method="POST" if body is not None else "GET")
    with urllib.request.urlopen(req, timeout=120) as r:
        raw = r.read()
    return raw if body is not None else json.loads(raw)


def _event_keys(event):
    """Names a Descript project may use for the event: "Large Language Models (LLMs)" -> llms / large language
    models, "Machine Learning" -> ml (Conf42 ML 2025)."""
    name = (event.get("name") or "").strip()
    bare = re.sub(r"\s*\(.*?\)", "", name).strip()
    keys = {_norm(name), _norm(bare)} | {_norm(x) for x in re.findall(r"\((.*?)\)", name)}
    words = bare.split()
    if len(words) > 1:
        keys.add("".join(w[0] for w in words).casefold())
    return keys


def _comp_people(name):
    """Speakers in a composition name: "A & B", "Kosseila_haddalene", "Shivam Tiwari-1" (a re-upload)."""
    name = re.sub(r"-\d+$", "", (name or "").replace("_", " ").strip())
    return {_norm(n) for n in re.split(r"\s*(?:&|,|\band\b)\s*", name)}


def descript(args):
    """Missing transcripts from Descript (Marek 2026-11-11): every talk of a finished event with no transcript in the
    repo is looked up in the event's Descript project ("Conf42 <name> <year>", one composition per talk named after
    its speakers) and its transcript exported to srt/<event>_<Name1>.srt, where plan finds it. A talk Descript does
    not have stays without a post."""
    token = _descript_token()
    if not token:
        print("descript: no DESCRIPT_API_TOKEN - skipped")
        return 0
    today = datetime.datetime.now(datetime.timezone.utc).date()
    projects, cursor = [], None
    while True:
        page = _descript(token, "/projects", dict(limit=100, **({"cursor": cursor} if cursor else {})))
        projects += [p for p in page.get("data", []) if (p.get("name") or "").startswith("Conf42 ")]
        cursor = (page.get("pagination") or {}).get("next_cursor")
        if not cursor:
            break
    got, missed = [], []
    for event in load_context()["events"]:
        if "external_url" in event or not event.get("short_url") or event["date"] >= today:
            continue
        todo = [t for t in event.get("talks_raw") or [] if (t.get("Name1") or "").strip()
                and "#" not in talk_ref(event, t) and not transcript_paths(event, t)]
        if not todo:
            continue
        keys, year = _event_keys(event), str(event.get("year"))
        proj = next((p for p in projects if p["name"].endswith(" " + year)
                     and _norm(p["name"][len("Conf42 "):-len(year) - 1]) in keys), None)
        comps = _descript(token, "/projects/" + proj["id"]).get("compositions", []) if proj else []
        for t in todo:
            who = [_norm(t.get(k)) for k in ("Name1", "Name2") if (t.get(k) or "").strip()]
            comp = next((c for c in comps if set(who) <= _comp_people(c.get("name"))), None)
            if not comp:
                missed.append("%s/%s" % (event["short_url"], t["Name1"].strip()))
                continue
            try:
                srt = _descript(token, "/export/transcript", body={"project_id": proj["id"], "composition_id": comp["id"],
                                                                 "format": "srt", "include_speaker_labels": "off"})
            except Exception as e:
                missed.append("%s/%s (%s)" % (event["short_url"], t["Name1"].strip(), e))
                continue
            if b"-->" not in srt:
                missed.append("%s/%s (empty export)" % (event["short_url"], t["Name1"].strip()))
                continue
            path = ("srt/%s_%s.srt" % (event["short_url"], t.get("Name1", ""))).replace(" ", "_")
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "wb") as f:
                f.write(srt)
            got.append(path)
    print("descript: %d transcripts fetched, %d not in Descript (no post for those)" % (len(got), len(missed)))
    for g in got:
        print("  + " + g)
    for m in missed:
        print("  - " + m)
    return 0


def main():
    cwd = os.getcwd()
    os.chdir(HERE)
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("plan")
    p.add_argument("--from", dest="since", default="2020-01-01")   # Marek 2026-11-10: every conference since 2020
    p.add_argument("--today")
    p.add_argument("--all", action="store_true", help="items for every backfill event, not just the next one")
    l = sub.add_parser("lint")
    l.add_argument("-v", "--verbose", action="store_true")
    a = sub.add_parser("add")
    a.add_argument("drafts", nargs="+")
    c = sub.add_parser("check")
    c.add_argument("drafts", nargs="+")
    c.add_argument("-v", "--verbose", action="store_true")
    op = sub.add_parser("orphan")
    op.add_argument("--offline", action="store_true", help="skip the YouTube checks (CI)")
    rp = sub.add_parser("replace")
    rp.add_argument("pairs", nargs="+", help="OLD_SHORTURL=NEW_SHORTURL")
    rl = sub.add_parser("release")
    rl.add_argument("n", type=int)
    sub.add_parser("descript")
    e = sub.add_parser("export")
    e.add_argument("out")
    args = ap.parse_args()
    if getattr(args, "drafts", None):
        args.drafts = [os.path.join(cwd, d) for d in args.drafts]
    if getattr(args, "out", None):
        args.out = os.path.join(cwd, args.out)
    if args.cmd == "plan":
        plan(args)
    elif args.cmd == "lint":
        sys.exit(lint(args))
    elif args.cmd == "check":
        sys.exit(check(args))
    else:
        {"add": add, "orphan": orphan, "export": export, "descript": descript, "release": release, "replace": replace}[args.cmd](args)


if __name__ == "__main__":
    main()
