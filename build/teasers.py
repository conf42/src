"""Talk teasers (Marek 2026-10-09): conf42.com/<event>/teasers - one 1080x1080 liquid-glass card per talk of an upcoming
event, plus a simplified LinkedIn carousel (a square PDF of the chosen talks). Hidden pages: noindex, never in the sitemap;
conf42.com/teasers/ lists them. A docs/<event>/ folder does not shadow the event page docs/<event>.html: Pages serves
/<event> from the file and /<event>/teasers from the folder (tested on gh-pages 2026-10-10). The card: the event's own colour (metadata.yml; Remix: a rainbow), three stacked glass
shards - the event card (logo, event, date) at the back, the speaker card (headshot whole, never cropped), the talk title
in front with the nameplate tucked under it - and an ONLINE pill. White text everywhere is kept readable: every tint behind
text is darkened until white on it passes WCAG AA (4.5:1).

The PNGs (conf42-<event>-<speaker>.png, next to the page in docs/<event>/) are drawn by build/render_teasers.py after the deploy with
headless Chrome (#sheet-<start>-<count>); until one exists the page draws that card in the browser (html-to-image).
"""
import colorsys
import datetime
import glob
import os
import re
import shutil
import unicodedata

from .shared import asset_version

RAINBOW = ["#ff5e7e", "#ffb547", "#4fd1a1", "#5aa8ff", "#a57bff"]
MOVED = ('<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex">'
         '<meta http-equiv="refresh" content="0; url=%(to)s"><link rel="canonical" href="%(to)s"><a href="%(to)s">Moved</a>')
PAST_FROM = datetime.date(2026, 1, 1)
TBD = re.compile(r"^\s*(tbd|tba|tbc|to be (announced|confirmed|decided))?\s*[.!]*\s*$", re.I)


def _shade(c, l, s=None, dh=0.0):
    r, g, b = (int(c[i:i + 2], 16) / 255 for i in (1, 3, 5))
    h, _, sat = colorsys.rgb_to_hls(r, g, b)
    r, g, b = colorsys.hls_to_rgb((h + dh) % 1, l, sat if s is None else s)
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))


def _rgba(c, a):
    return "rgba(%d,%d,%d,%s)" % (int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16), a)


def _lum(c):
    v = [int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    v = [x / 12.92 if x <= .03928 else ((x + .055) / 1.055) ** 2.4 for x in v]
    return .2126 * v[0] + .7152 * v[1] + .0722 * v[2]


def _safe(c, sat, l=.52, dh=0.0, ratio=4.6):
    """c as light as it can be (from lightness l down) while white text on it still passes WCAG AA: 4.5:1 for normal
    text (the page's buttons), 3:1 for large text (every card text is 22 px bold or bigger), with a little margin."""
    while 1.05 / (_lum(_shade(c, l, sat, dh)) + .05) < ratio and l > .1:
        l -= .01
    return _shade(c, l, sat, dh)


def scheme(event):
    """The CSS colours of an event's cards, built on its metadata.yml colour itself (Marek 2026-10-13: the cards only
    vaguely matched it). Hue, saturation and lightness are the event's own; the blobs vary around it a little
    (lightness +-0.1, hue +-0.015) to give the glass shards some punch. The base under them is the same colour,
    darker. The event shard is the colour as it is, darkened only as far as white large text needs (3:1).
    Remix is a rainbow."""
    c = str(event.get("color") or "#838383")
    if event.get("name", "").strip().lower() == "remix" or not re.match(r"^#[0-9a-fA-F]{6}$", c):
        return dict(base="#0d0b18", soft="#efe6ff", glass1=_rgba("#ffffff", .13), glass2=_rgba("#ffffff", .04),
                    dark1=_rgba("#14112a", .55), dark2=_rgba("#14112a", .38),
                    ev="linear-gradient(100deg,%s)" % ",".join(_rgba(_safe(x, .85, ratio=3.1), .9) for x in RAINBOW),
                    blobs=[RAINBOW[0], RAINBOW[3], RAINBOW[2], RAINBOW[1], RAINBOW[4]], ui=_safe("#a57bff", .85), rainbow=True)
    r, g, b = (int(c[i:i + 2], 16) / 255 for i in (1, 3, 5))
    _, l0, sat = colorsys.rgb_to_hls(r, g, b)
    at = lambda d: min(max(l0 + d, .1), .85)
    dark, light = _shade(c, max(l0 * .35, .06), sat), _shade(c, .86, sat)
    return dict(base=_shade(c, min(max(l0 * .7, .06), .4), sat), soft=light, glass1=_rgba(light, .13), glass2=_rgba(light, .04),
                dark1=_rgba(dark, .55), dark2=_rgba(dark, .38),
                ev="linear-gradient(145deg,%s,%s)" % (_rgba(_safe(c, sat, l0, ratio=3.1), .94), _rgba(_safe(c, sat, l0, dh=.015, ratio=3.1), .86)),
                blobs=[_shade(c, at(.04), sat), _shade(c, at(-.1), sat, dh=.015), _shade(c, at(.1), sat, dh=-.015), _shade(c, at(.02), sat), _shade(c, at(-.05), sat)],
                ui=_safe(c, sat, max(l0, .52)), rainbow=False)


def _slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def _event_name(event):
    return re.sub(r"\s*\([^)]*\)\s*$", "", event.get("name", "")).strip()   # "Site Reliability Engineering (SRE)" -> without the acronym


def cards(event):
    """The event's talks in website order (keynotes, then the rest as in the sheet), each with what its card shows."""
    talks = [t for t in event.get("talks_raw", []) if (t.get("Name1") or "").strip()]
    talks = [t for t in talks if (t.get("Featured") or "").lower() == "yes"] + [t for t in talks if (t.get("Featured") or "").lower() != "yes"]
    slug, out, used = event["short_url"].replace(".html", ""), [], {}
    for i, t in enumerate(talks):
        people = [((t.get("Name%d" % k) or "").strip(), (t.get("Company%d" % k) or "").strip()) for k in (1, 2)]
        people = [p for p in people if p[0]]
        title = (t.get("Title") or "").strip()
        photo = t.get("Picture") or ""
        has_photo = bool(re.search(r"/headshots/.+\.(png|jpe?g|webp)$", photo, re.I))
        missing = " and ".join(x for x, gone in (("photo", not has_photo), ("title", not title or TBD.match(title))) if gone)
        file = "conf42-%s-%s" % (slug, _slug(" ".join(n for n, _ in people)) or "talk")
        used[file] = used.get(file, 0) + 1
        if used[file] > 1:
            file += "-%d" % used[file]
        if len(people) == 2 and people[0][1] == people[1][1]:   # one company: "A & B" over it
            plate = [(people[0][0] + " & " + people[1][0], people[0][1])]
        else:
            plate = people
        names = [n for n, _ in people]
        first = " & ".join(n.split()[0] for n in names)
        last = " & ".join(n.split()[-1] for n in names)
        out.append(dict(i=i, title=title or "TBD", people=people, plate=plate, photo=photo if has_photo else "", missing=missing,
                        file=file + ".png", name=" & ".join(names), keynote=(t.get("Featured") or "").lower() == "yes", org=" & ".join(dict.fromkeys(c for _, c in people if c)),
                        first=first.lower(), last=last.lower(),
                        search=" ".join([title] + [n for n, _ in people] + [c for _, c in people]).lower()))
    return out


def _splash(event, base_folder):
    """The event's splash art for the Generic covers (Marek 2026-10-11), seen from docs/<event>/: its thumbnail_path,
    the .jpg next to it when there is one (the PNGs are ~2 MB); none when the file is missing."""
    p = str(event.get("thumbnail_path") or "").lstrip("./")
    if not p or not os.path.isfile(os.path.join(base_folder, p)):
        return ""
    jpg = os.path.splitext(p)[0] + ".jpg"
    return "../" + (jpg if os.path.isfile(os.path.join(base_folder, jpg)) else p)


def thumbnails(event, items):
    """What build/youtube_thumbnails.py needs for the Thumbnails tab (Marek 2026-10-12): every talk with a photo (a missing
    title doesn't matter here: the thumbnail is the speaker alone, on its topic's sky). Remix re-runs talks whose videos
    already have thumbnails, so it gets them for its keynotes only."""
    remix = (event.get("name") or "").strip().lower() == "remix"
    return dict(talks=[dict(file=c["file"][:-4] + "-thumbnail.png", photo=c["photo"], name=c["name"], i=c["i"],
                            search=c["search"], first=c["first"], last=c["last"])   # the tab sorts and searches by itself (past events have no cards)
                       for c in items if c["photo"] and (c["keynote"] or not remix)])


def overlays(event, ev):
    """What the Overlays tab draws (Marek 2026-10-13): the OBS recording overlays speakers record their talk in, 1920x1080
    with transparent holes, in the event's metadata.yml colour as it is, with "CONF42 <EVENT> <YEAR>" and "<MONTH> <DAY>"."""
    c = str(event.get("color") or "")
    c = c if re.match(r"^#[0-9a-fA-F]{6}$", c) else "#838383"
    _, l, sat = colorsys.rgb_to_hls(*(int(c[i:i + 2], 16) / 255 for i in (1, 3, 5)))
    # the New design (Marek 2026-10-13, "a-frost"): soft lighter and darker pools of the colour under white frosted glass
    pools = [_shade(c, min(l + d, .92), sat) for d in (.12, -.10, .09, -.08)]
    return dict(color=c, pools=pools, title=("Conf42 %s %d" % (ev["name"], ev["date"].year)).upper(),
                date=("%s %d" % (ev["date"].strftime("%B"), ev["date"].day)).upper(), slug=ev["slug"])


def _size(path):
    try:
        from PIL import Image
        with Image.open(path) as im:
            return "%d \u00d7 %d" % im.size
    except Exception:
        return ""


def upcoming(events, today=None):
    today = today or datetime.date.today()
    return [e for e in events if "external_url" not in e and e.get("short_url") and e.get("date") and e["date"] >= today - datetime.timedelta(days=1)]


def past(events, today=None):
    """Events that are over but keep a page with their Thumbnails and Overlays tabs (Marek 2026-10-13: both stay useful
    after the event - videos go up later, late recordings). From 2026 on: 2025 events never had thumbnails. Newest first."""
    today = today or datetime.date.today()
    keep = [e for e in events if "external_url" not in e and e.get("short_url") and e.get("date")
            and PAST_FROM <= e["date"] < today - datetime.timedelta(days=1)]
    return sorted(keep, key=lambda e: e["date"], reverse=True)


def generate(env, context, base_folder):
    """docs/<event>/teasers.html for every upcoming event with talks (and, Thumbnails + Overlays only, every past one since
    PAST_FROM), docs/teasers/index.html listing them, and
    docs/teasers/<event>.html forwarding the first links (Marek 2026-10-10: /<event>/teasers, like the sister sites)."""
    folder = os.path.join(base_folder, "teasers")
    # the pages and PNGs of events that are over must not linger: everything teaser-made is removed first
    # (render_teasers.py refills the PNGs, teaser_previews.py their WebP previews); an event folder holds nothing else, so an emptied one goes too
    shutil.rmtree(folder, ignore_errors=True)
    for old in glob.glob(os.path.join(base_folder, "*", "teasers.html")):
        d = os.path.dirname(old)
        for f in [old] + glob.glob(os.path.join(d, "conf42-*.png")) + glob.glob(os.path.join(d, "conf42-*.webp")):
            os.remove(f)
        if not os.listdir(d):
            os.rmdir(d)
    os.makedirs(folder, exist_ok=True)
    listed, over = [], []
    page = env.get_template("teasers.html")
    overlays_v = asset_version(base_folder, "assets/js/overlays.js")
    events = context.get("events") or []
    up = upcoming(events)
    for event in up + past(events):
        is_past = event not in up
        items = cards(event)
        if not items:
            continue
        slug = event["short_url"].replace(".html", "")
        ev = dict(name=_event_name(event), full=event.get("name"), slug=slug, date=event["date"],
                  date_text="%s %d %d" % (event["date"].strftime("%b"), event["date"].day, event["date"].year), iso=event["date"].isoformat(),
                  date_long="%s %d %d" % (event["date"].strftime("%B"), event["date"].day, event["date"].year))   # no comma (Marek 2026-10-12)
        ev["splash"] = _splash(event, base_folder)
        p = str(event.get("thumbnail_path") or "").lstrip("./")   # the splash art as it is, for the Generic tab's download:
        for ext in (".png", ".jpeg", ".webp"):                    # the original, not the 500 px .jpg the site shows (pick_picture_file)
            if os.path.isfile(os.path.join(base_folder, os.path.splitext(p)[0] + ext)):
                p = os.path.splitext(p)[0] + ext
                break
        ev["splash_full"] = "../" + p if p and os.path.isfile(os.path.join(base_folder, p)) else ""
        ev["splash_size"] = _size(os.path.join(base_folder, p)) if ev["splash_full"] else ""
        th = thumbnails(event, items)
        if is_past:   # Thumbnails and Overlays only: no cards (so render_teasers.py draws nothing), no Generic, no Carousel
            ev["splash"] = ""
        os.makedirs(os.path.join(base_folder, slug), exist_ok=True)
        with open(os.path.join(base_folder, slug, "teasers.html"), "w", encoding="utf-8") as f:
            f.write(page.render(ev=ev, cards=[] if is_past else items, sc=scheme(event), th=th, ov=overlays(event, ev), past=is_past, overlays_v=overlays_v, **context))
        with open(os.path.join(folder, slug + ".html"), "w", encoding="utf-8") as f:
            f.write(MOVED % {"to": "../%s/teasers" % slug})
        if is_past:
            over.append(dict(ev, n=len(th["talks"]), sc=scheme(event)))
            print("Writing out %s/teasers.html (past: %d thumbnails, overlays)" % (slug, len(th["talks"])))
            continue
        listed.append(dict(ev, n=len(items), ready=sum(1 for c in items if not c["missing"]), sc=scheme(event)))
        print("Writing out %s/teasers.html (%d cards)" % (slug, len(items)))
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as f:
        f.write(env.get_template("teasers_index.html").render(teaser_events=listed, past_events=over))
