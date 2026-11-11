"""The living blog (conf42.com/blog, Marek 2026-11-08): _db/blog.csv is written by Claude (skill conf42-blog) and the
build decides what is public. A post is shown only while
  - its Status is empty/published (hidden = manual kill, orphaned = the skill noticed its Ref is gone),
  - its Date is today or earlier (UTC) - future rows go live on the daily rebuild of their day,
  - its Ref still points at something in the repo: a talk deleted from the event CSV (speaker asked to be taken down)
    takes its post with it on the next build, transcript or not.
Invisible posts get no page, no index/home card, no sitemap/feed/llms.txt/404-index entry; the gh-pages deploy deletes
the stale HTML.

Ref (stable keys, not the talk short_url - that one changes with the Keywords):
  talk:<event short_url>/<Name1>              event:<event short_url>
  sponsor:<event short_url>/<sponsor id>/<Name1>
  webinar:<WEBINARS.csv Slug>                 sister:<repo>/<event folder>  (_db/sister_events.json, from blog_plan)
  empty = legacy row (pre-2025), always resolves.
"""
import datetime
import json
import os
import re
from xml.sax.saxutils import escape

import dateutil.parser
import markdown

from .shared import generate_speaker_url, make_remote_address, pick_picture_file, read_csv
from .teasers import _slug as _teaser_slug

SITE = "https://www.conf42.com/"
BLOG_CSV = "./_db/blog.csv"
WEBINARS_CSV = "./_db/WEBINARS.csv"
SISTER_JSON = "./_db/sister_events.json"
SPLASH_FOLDER = "./assets/splash/"
FEED_FILE = "blog.xml"
FEED_SIZE = 50
TRANSCRIPT_LD_CHARS = 20000
VISIBLE_STATUSES = {"", "published"}
# IndexNow (Bing, Yandex, Seznam, Naver; Bing feeds ChatGPT/Copilot search): the key is public by design - it is served
# at /<key>.txt to prove the site owns the pings. The morning cron run pings the posts that went live / changed today.
INDEXNOW_KEY = "fcd04983393834bd2826cd6a2f8503d1"
INDEXNOW_LIST = "./_indexnow.json"


# the one Conf42 entity every page's JSON-LD points at (@id), so engines tie talks, posts and events to the same brand
ORG_ID = SITE + "#organization"
ORG_SAME_AS = ["https://www.youtube.com/channel/UCXGkmsJSnu4SuG1BLWcLAGQ", "https://www.linkedin.com/company/49110720/",
               "https://luma.com/sre"]
ORG_REF = {"@type": "Organization", "@id": ORG_ID, "name": "Conf42", "url": SITE}


def site_jsonld():
    """Organization + WebSite (with the blog search as its SearchAction), on every page."""
    org = dict(ORG_REF, **{"@context": "https://schema.org", "alternateName": "Conf42.com",
                           "logo": {"@type": "ImageObject", "url": SITE + "assets/conf42/CONF42.QR.png"},
                           "description": "Conf42 runs free online tech conferences: SRE, DevOps, DevSecOps, Cloud Native, "
                                          "Platform Engineering, Observability, LLMs, AI agents, MLOps, Golang, Python, "
                                          "Rust, JavaScript and more.",
                           "sameAs": ORG_SAME_AS})
    site = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "#website", "name": "Conf42", "url": SITE,
            "publisher": {"@id": ORG_ID},
            "potentialAction": {"@type": "SearchAction", "target": SITE + "blog?q={search_term_string}",
                                "query-input": "required name=search_term_string"}}
    return [org, site]


def _same_as(talk, k):
    """The speaker's LinkedIn / X links exactly as the talk page shows them."""
    out = []
    li = (talk.get("LinkedIn%d" % k) or "").strip()
    if li:
        out.append(li if li.startswith("http") else "https://" + li)
    tw = (talk.get("Twitter%d" % k) or "").strip().lstrip("@")
    if tw:
        out.append(tw if tw.startswith("http") else "https://twitter.com/" + tw)
    return out


def people_jsonld(talk):
    """Person entries for a talk's speakers: name, speaker page, socials, job and company only where the sheet has them
    (an empty Company1 is the speaker's privacy - never filled in)."""
    out = []
    for k in (1, 2):
        name = (talk.get("Name%d" % k) or "").strip()
        if not name:
            continue
        person = {"@type": "Person", "name": name, "url": SITE + generate_speaker_url(name)}
        same = _same_as(talk, k)
        if same:
            person["sameAs"] = same
        if (talk.get("JobTitle%d" % k) or "").strip():
            person["jobTitle"] = talk["JobTitle%d" % k].strip()
        if (talk.get("Company%d" % k) or "").strip():
            person["worksFor"] = {"@type": "Organization", "name": talk["Company%d" % k].strip()}
        out.append(person)
    return out


def speaker_jsonld(speaker, items, url):
    """ProfilePage for /speaker_<Name>: the Person (from their newest talk's row) and the talks they gave at Conf42."""
    person = {"@type": "Person", "name": speaker, "url": url}
    for item in items:
        talk = item["talk"]
        found = [p for p in people_jsonld(talk) if _norm(p["name"]) == _norm(speaker)]
        if found:
            person = dict(found[0], url=url)
            if talk.get("Picture"):
                person["image"] = talk["Picture"]
            break
    person["performerIn"] = [{
        "@type": "Event", "name": i["talk"].get("Title") or "",
        "url": SITE + (i["talk"].get("short_url") or "").replace(".html", ""),
        "superEvent": event_ref(i["event"])} for i in items]
    return {"@context": "https://schema.org", "@type": "ProfilePage", "url": url, "mainEntity": person,
            "isPartOf": {"@id": SITE + "#website"}}


def event_jsonld(event):
    """Event (what event.html used to inline, plus who spoke and whether it is over) + the ItemList of its talk pages."""
    talks = [t for t in event.get("talks_raw") or [] if t.get("short_url")]
    status = "EventCompleted" if event.get("is_past") else "EventScheduled"
    data = {
        "@context": "https://schema.org", "@type": "Event",
        "name": "Conf42: %s %s" % (event.get("name"), event.get("year")),
        "url": SITE + event.get("short_url", "").replace(".html", ""),
        "startDate": event["date"].strftime("%Y-%m-%dT17:00:00Z"),
        "endDate": event["date"].strftime("%Y-%m-%dT23:00:00Z"),
        "eventStatus": "https://schema.org/" + status,
        "eventAttendanceMode": "https://schema.org/OnlineEventAttendanceMode",
        "location": {"@type": "VirtualLocation", "url": event.get("url") or SITE + event.get("short_url", "").replace(".html", "")},
        "image": [absolute(event.get("thumbnail_path") or "")],
        "description": (event.get("description") or "").replace("\n", " "),
        "offers": {"@type": "Offer", "url": event.get("url") or SITE, "price": "0", "priceCurrency": "USD",
                   "availability": "https://schema.org/InStock", "validFrom": "2021-01-01T00:00"},
        "organizer": ORG_REF,
        "isAccessibleForFree": True,
    }
    seen, performers = set(), []
    for t in talks:
        for p in people_jsonld(t):
            if p["name"] not in seen:
                seen.add(p["name"])
                performers.append({"@type": "Person", "name": p["name"], "url": p["url"]})
    if performers:
        data["performer"] = performers
    out = [data]
    if talks:
        out.append({"@context": "https://schema.org", "@type": "ItemList",
                    "name": "Talks at Conf42 %s %s" % (event.get("name"), event.get("year")),
                    "numberOfItems": len(talks),
                    "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": t.get("Title") or "",
                                         "url": SITE + t["short_url"].replace(".html", "")} for i, t in enumerate(talks)]})
    return out


def event_ref(event):
    return {"@type": "Event", "name": "Conf42 %s %s" % (event.get("name"), event.get("year")),
            "url": SITE + event.get("short_url", "").replace(".html", "")}


def released_on(event):
    """The day an event's talks went public (video, transcript, takeaways): the honest lastmod for its talk and event
    pages. None while it hasn't happened - no lastmod beats a made-up one."""
    if not event.get("released") or not event.get("release_at"):
        return None
    return event["release_at"].date().isoformat()


def _norm(s):
    return re.sub(r"\s+", " ", (s or "").strip()).casefold()


def absolute(path):
    """'./assets/x.png' / 'assets/x.png' / 'https://...' -> absolute URL (og:image, feed, JSON-LD)."""
    if not path:
        return ""
    if re.match(r"^https?://", path):
        return path
    return SITE + re.sub(r"^\./", "", path).lstrip("/")


class Resolver:
    """Looks Refs up in the data the build already loaded."""

    def __init__(self, events, sponsors):
        self.events = {e.get("short_url"): e for e in events if e.get("short_url")}
        self.sponsor_ids = {s.get("id") for s in sponsors or []}
        try:
            self.webinars = {w.get("Slug"): w for w in read_csv(WEBINARS_CSV) if w.get("Slug")}
        except Exception:
            self.webinars = {}
        try:
            with open(SISTER_JSON, encoding="utf-8") as f:
                self.sisters = {s["ref"]: s for s in json.load(f)}
        except Exception:
            self.sisters = {}

    def talk(self, short_url, name1):
        # "Name#YouTubeId" picks one of a speaker's several talks at the same event (blog_plan.talk_ref)
        name1, _, yid = name1.partition("#")
        event = self.events.get(short_url)
        if not event:
            return None, None
        for talk in event.get("talks_raw") or []:
            if _norm(talk.get("Name1")) == _norm(name1) and (not yid or talk.get("YouTubeId") == yid):
                return event, talk
        return event, None

    def resolve(self, ref):
        """-> (ok, dict(event=, talk=, webinar=, sister=, sponsor=)); ok False = the thing is gone."""
        ref = (ref or "").strip()
        if not ref:
            return True, {}
        kind, _, rest = ref.partition(":")
        if kind == "event":
            event = self.events.get(rest)
            return bool(event), dict(event=event)
        if kind == "talk":
            short_url, _, name1 = rest.partition("/")
            event, talk = self.talk(short_url, name1)
            return bool(talk), dict(event=event, talk=talk)
        if kind == "sponsor":
            parts = rest.split("/", 2)
            if len(parts) != 3:
                return False, {}
            short_url, sid, name1 = parts
            event, talk = self.talk(short_url, name1)
            levels = (event or {}).get("sponsors") or {}
            sponsoring = any(sid in (ids or []) for ids in levels.values())
            return bool(talk) and sponsoring, dict(event=event, talk=talk, sponsor=sid)
        if kind == "webinar":
            webinar = self.webinars.get(rest)
            return bool(webinar), dict(webinar=webinar)
        if kind == "sister":
            sister = self.sisters.get(ref)
            return bool(sister), dict(sister=sister)
        return False, {}


_LEADING_H1 = re.compile(r"^\s*#(?!#)[^\n]*\n")


def _body(text):
    """The page already prints the Title as its H1: drop a leading single-# heading from the Markdown."""
    return _LEADING_H1.sub("", text or "", count=1).strip()


def _youtube_id(talk):
    """The video id without a share link's "?si=..." tail."""
    return re.split(r"[?&#]", (talk or {}).get("YouTubeId") or "")[0]


YOUTUBE_IN_BODY = re.compile(r"(?:youtu\.be/|youtube\.com/(?:watch\?v=|embed/|live/))([\w-]{11})")


def video_purged(post, linked):
    """A talk whose video was out (the post links it) and whose YouTube cell is now empty: the speaker had the video taken
    down, maybe years later, and the post goes with it (Marek 2026-11-09). A new link (re-upload) keeps the post."""
    talk = linked.get("talk")
    return bool(talk) and not _youtube_id(talk) and bool(YOUTUBE_IN_BODY.search(post.get("Body") or ""))


def _image(post, linked, base_folder):
    """ThumbnailPath as given (local splash -> its 500px JPEG, or an absolute URL); empty -> from what the post is about."""
    path = (post.get("ThumbnailPath") or "").strip()
    talk = linked.get("talk")
    # a talk's post shows the talk's 16:9 YouTube thumbnail, never the headshot (Marek 2026-11-09): every talk on the blog has its video
    if _youtube_id(talk):
        return "https://i.ytimg.com/vi/%s/maxresdefault.jpg" % _youtube_id(talk)
    # before the video is out: the same thumbnail as drawn on the event's teaser page (2026+ events have one)
    event = linked.get("event")
    if talk and event and str(event.get("date"))[:4] >= "2026" and "/headshots/" in (talk.get("Picture") or ""):
        slug = event["short_url"].replace(".html", "")
        names = " ".join((talk.get("Name%d" % k) or "").strip() for k in (1, 2)).strip()
        return "https://www.conf42.com/%s/conf42-%s-%s-thumbnail.png" % (slug, slug, _teaser_slug(names))
    if path:
        return path if re.match(r"^https?://", path) else pick_picture_file(base_folder + "/", path)
    if talk and talk.get("Picture"):
        pic = talk["Picture"]   # generate.py has already made it a URL by the time posts load
        return pic if re.match(r"^https?://", pic) else make_remote_address("headshots", pic)
    if event and event.get("thumbnail_path"):
        return event["thumbnail_path"]
    webinar = linked.get("webinar")
    if webinar and webinar.get("Splash"):
        return pick_picture_file(base_folder + "/", SPLASH_FOLDER + webinar["Splash"])
    sister = linked.get("sister")
    if sister and sister.get("card") and os.path.exists(os.path.join(base_folder, sister["card"])):
        return sister["card"]   # the cover without its FREE / discount ball (blog_plan._card_copy)
    if sister and sister.get("image"):
        return sister["image"]
    return ""


def _iso_duration(minutes):
    try:
        return "PT%dM" % int(float(minutes))
    except (TypeError, ValueError):
        return None


def video_jsonld(talk, event, url):
    """schema.org VideoObject for a talk with a YouTube video, or None."""
    yid = _youtube_id(talk)
    if not yid:
        return None
    speakers = [n for n in ((talk.get("Name1") or "").strip(), (talk.get("Name2") or "").strip()) if n]
    data = {
        "@context": "https://schema.org",
        "@type": "VideoObject",
        "name": talk.get("Title") or "",
        "description": re.sub(r"\s+", " ", talk.get("Abstract") or talk.get("Title") or "").strip()[:2000],
        "thumbnailUrl": ["https://i.ytimg.com/vi/%s/hqdefault.jpg" % yid],
        "embedUrl": "https://www.youtube.com/embed/%s" % yid,
        "url": url,
        "inLanguage": "en",
        "publisher": ORG_REF,
    }
    if event and event.get("date"):
        data["uploadDate"] = event["date"].isoformat() + "T17:00:00Z"
        data["isPartOf"] = event_ref(event)
    duration = _iso_duration(talk.get("Duration"))
    if duration:
        data["duration"] = duration
    if speakers:
        data["actor"] = people_jsonld(talk)
    if (talk.get("Keywords") or "").strip():
        data["keywords"] = [k.strip() for k in talk["Keywords"].split(",") if k.strip()]
    # the same transcript text the page prints (talk.html's panel), capped: engines quote the talk from it
    chunks = ((talk.get("transcript") or {}).get("chunks") or []) if isinstance(talk.get("transcript"), dict) else []
    text = re.sub(r"\s+", " ", " ".join((c.get("text") or "") for c in chunks)).strip()
    if text:
        data["transcript"] = text[:TRANSCRIPT_LD_CHARS]
    return data


def _post_jsonld(post):
    author = (post.get("Author") or "").strip()
    data = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": post["Title"],
        "description": post["description"],
        "datePublished": post["date_iso"],
        "dateModified": post["updated_iso"],
        "mainEntityOfPage": post["canonical"],
        "url": post["canonical"],
        "author": {"@type": "Person", "name": author} if author and author != "Conf42" else ORG_REF,
        "publisher": dict(ORG_REF, logo={"@type": "ImageObject", "url": SITE + "assets/conf42/CONF42.QR.png"}),
        "isAccessibleForFree": True,
    }
    if post.get("image_abs"):
        data["image"] = [post["image_abs"]]
    if post.get("Tags"):
        data["keywords"] = [t.strip() for t in post["Tags"].split(",") if t.strip()]
    event = post["linked"].get("event")
    if event:
        data["about"] = event_ref(event)
    talk = post["linked"].get("talk")
    mentions = people_jsonld(talk) if talk else []
    sponsor = post["linked"].get("sponsor")
    if sponsor and post.get("Sponsor"):
        mentions.append({"@type": "Organization", "name": post["Sponsor"]})
    if mentions:
        data["mentions"] = mentions
    if talk and talk.get("short_url"):
        data["isBasedOn"] = SITE + talk["short_url"].replace(".html", "")
    crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Conf42", "item": SITE},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "blog"},
            {"@type": "ListItem", "position": 3, "name": post["Title"], "item": post["canonical"]},
        ],
    }
    out = [data, crumbs]
    video = video_jsonld(talk, event, post["canonical"]) if talk and (event or {}).get("released") else None
    if video:
        video.pop("transcript", None)   # the post doesn't print it; the talk page carries it
        video["url"] = SITE + talk["short_url"].replace(".html", "")
        out.append(video)
    return out


def _date(value):
    return dateutil.parser.parse(value).date() if (value or "").strip() else None


def _card_title(post, linked):
    """Event posts without a speaker (roundups) show the conference on a tinted pill under the card and drop it from the
    card title (Marek 2026-11-11); the post page keeps the full title."""
    title, event = post.get("Title") or "", (linked or {}).get("event")
    if not event or (linked or {}).get("talk"):
        return "", title
    pill = "Conf42 %s %s" % (event.get("name"), event.get("year"))
    m = re.match(r"\s*Conf42\b[^:\u2013\u2014]*?\b%s\b(?:\s+roundup)?\s*(?::|\s[-\u2013\u2014])\s*" % event.get("year"), title, re.I)
    if m and title[m.end():]:
        rest = title[m.end():]
        title = rest[0].upper() + rest[1:]
    return pill, title


def load_posts(context, base_folder, today=None, path=BLOG_CSV):
    """-> (visible posts newest first, [(ShortURL, reason)] of the rows kept off the site)."""
    today = today or datetime.datetime.now(datetime.timezone.utc).date()
    try:
        rows = read_csv(path)
    except Exception as e:
        print("Couldn't read blog posts", e)
        return [], []
    resolver = Resolver(context.get("events") or [], context.get("sponsors") or [])
    visible, dropped = [], []
    # a post replaced by one that is not out yet (queued, or dated later) stays up until its replacement is, then turns
    # into the redirect (Marek 2026-11-10: the 2020-24 announcements give way to the new roundups as they roll out)
    out_now = {(r.get("ShortURL") or "").strip() for r in rows if (r.get("Status") or "").strip().lower() in VISIBLE_STATUSES
               and (r.get("Date") or "")[:10] <= today.isoformat()}
    for row in rows:
        post = {k: (v.strip() if isinstance(v, str) and k != "Body" else v) for k, v in row.items() if k}
        slug = post.get("ShortURL") or post.get("ExternalURL") or post.get("Title")
        status = (post.get("Status") or "").lower()
        if status.startswith("replaced:") and status[len("replaced:"):] not in {s.lower() for s in out_now}:
            status = ""
        if status not in VISIBLE_STATUSES:
            dropped.append((slug, "status " + status))
            continue
        try:
            date = _date(post.get("Date"))
        except (ValueError, OverflowError):
            dropped.append((slug, "bad Date %r" % post.get("Date")))
            continue
        if not date:
            dropped.append((slug, "no Date"))
            continue
        if date > today:
            dropped.append((slug, "scheduled for %s" % date))
            continue
        ok, linked = resolver.resolve(post.get("Ref"))
        if not ok:
            dropped.append((slug, "Ref gone: %s" % post.get("Ref")))
            continue
        if video_purged(post, linked):
            dropped.append((slug, "video purged: %s" % post.get("Ref")))
            continue
        try:
            updated = max(_date(post.get("Updated")) or date, date)
        except (ValueError, OverflowError):
            updated = date
        post["linked"] = linked
        post["conf_pill"], post["card_title"] = _card_title(post, linked)
        post["Date"] = datetime.datetime.combine(date, datetime.time())
        post["date_iso"] = date.isoformat()
        post["updated_iso"] = updated.isoformat()
        post["updated"] = updated
        post["Body"] = _body(post.get("Body"))
        post["ThumbnailPath"] = _image(post, linked, base_folder)
        post["image_abs"] = absolute(post["ThumbnailPath"])
        if not post.get("ExternalURL"):
            # every post lives under /blog/ so it is never taken for a talk page (Marek 2026-11-11); ShortURL stays the key
            post["path"] = "blog/" + post["ShortURL"]
            post["canonical"] = SITE + post["path"]
            post["description"] = post.get("Description") or re.sub(r"\s+", " ", re.sub(r"[#*_>\[\]`]|\(http[^)]*\)", "", post["Body"]))[:200].strip()
            post["jsonld"] = _post_jsonld(post)
        visible.append(post)
    visible.sort(key=lambda p: (p["Date"], p.get("ShortURL") or ""), reverse=True)
    for slug in spread_images(visible):
        print("WARN blog: %s has the same picture as the post before it" % slug)
    return visible, dropped


def spread_images(posts):
    """No two cards in a row with the same picture (Marek 2026-11-09; a speaker back at the same event type a year
    later may share one, never side by side): a repeat swaps with a later post of the same day - order within a day
    means nothing. -> ShortURLs still repeating (none to swap with), for the build log."""
    left = []
    for i in range(1, len(posts)):
        if posts[i].get("ThumbnailPath") != posts[i - 1].get("ThumbnailPath"):
            continue
        for j in range(i + 1, len(posts)):
            if posts[j]["Date"] != posts[i]["Date"]:
                break
            if posts[j].get("ThumbnailPath") != posts[i - 1].get("ThumbnailPath"):
                posts[i], posts[j] = posts[j], posts[i]
                break
        else:
            left.append(posts[i].get("ShortURL"))
        if posts[i].get("ThumbnailPath") == posts[i - 1].get("ThumbnailPath") and posts[i].get("ShortURL") not in left:
            left.append(posts[i].get("ShortURL"))
    return left


def _rfc3339(iso_date):
    return iso_date + "T00:00:00Z"


def write_feed(posts, base_folder, now):
    """Atom feed of the newest posts, full content (conf42.com/blog.xml)."""
    items = [p for p in posts if not p.get("ExternalURL")][:FEED_SIZE]
    updated = max((p["updated_iso"] for p in items), default=now.date().isoformat())
    out = ['<?xml version="1.0" encoding="utf-8"?>',
           '<feed xmlns="http://www.w3.org/2005/Atom">',
           '<title>Conf42 Blog</title>',
           '<subtitle>Talks, speakers and sponsors of Conf42 online tech conferences</subtitle>',
           '<link href="%s%s" rel="self"/>' % (SITE, FEED_FILE),
           '<link href="%sblog"/>' % SITE,
           '<id>%sblog</id>' % SITE,
           '<updated>%s</updated>' % _rfc3339(updated),
           '<author><name>Conf42</name><uri>%s</uri></author>' % SITE]
    for p in items:
        html = markdown.markdown(p["Body"], extensions=["extra"])
        out += ['<entry>',
                '<title>%s</title>' % escape(p["Title"]),
                '<link href="%s"/>' % escape(p["canonical"]),
                '<id>%s</id>' % escape(p["canonical"]),
                '<published>%s</published>' % _rfc3339(p["date_iso"]),
                '<updated>%s</updated>' % _rfc3339(p["updated_iso"]),
                '<summary>%s</summary>' % escape(p["description"]),
                '<content type="html">%s</content>' % escape(html),
                '</entry>']
    out.append('</feed>')
    with open(os.path.join(base_folder, FEED_FILE), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("Writing out %s (%d posts)" % (FEED_FILE, len(items)))


# Every AI crawler is welcome (Marek 2026-11-10: training bots too - that is how "Conf42" gets into the models
# themselves). Search/user bots fetch pages for live answers; training bots feed the next model.
AI_SEARCH_BOTS = ("OAI-SearchBot", "ChatGPT-User", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User",
                  "Bingbot", "Googlebot", "Applebot", "DuckAssistBot", "MistralAI-User", "Meta-ExternalFetcher")
AI_TRAINING_BOTS = ("GPTBot", "ClaudeBot", "Google-Extended", "Applebot-Extended", "CCBot", "Meta-ExternalAgent",
                    "Amazonbot", "cohere-ai")


def write_robots(base_folder):
    """robots.txt: everyone welcome, every AI crawler named. Cloudflare's managed robots.txt (ai-train=no) must stay off
    in the dashboard, or it prepends a block that disallows the training bots."""
    lines = ["# Conf42: free online tech conferences. AI crawlers welcome. Index for AI: %sllms.txt" % SITE, "",
             "User-agent: *", "Allow: /", ""]
    for bot in AI_SEARCH_BOTS + AI_TRAINING_BOTS:
        lines += ["User-agent: " + bot, "Allow: /", ""]
    lines.append("Sitemap: %ssitemap.xml" % SITE)
    with open(os.path.join(base_folder, "robots.txt"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("Writing out robots.txt")


def write_llms(context, posts, base_folder):
    """llms.txt (llmstxt.org): what Conf42 is, its events and the newest posts, for AI search engines."""
    today = datetime.date.today()
    events = [e for e in context.get("events") or [] if e.get("short_url") and "external_url" not in e]
    upcoming = sorted([e for e in events if e.get("date") and e["date"] >= today], key=lambda e: e["date"])
    recent = sorted([e for e in events if e.get("date") and e["date"] < today], key=lambda e: e["date"], reverse=True)[:30]

    def ev(e):
        n = len(e.get("talks_raw") or [])
        return "- [Conf42 %s %s](%s%s): %s%s" % (e.get("name"), e.get("year"), SITE, e["short_url"], e["date"].isoformat(),
                                                ", %d talks" % n if n else "")

    lines = ["# Conf42", "",
             "> Conf42 runs free online tech conferences (SRE, DevOps, DevSecOps, Cloud Native, Kubernetes, Platform "
             "Engineering, Observability, LLMs, AI agents, MLOps, Golang, Python, Rust, JavaScript and more). Every talk "
             "has its own page with the video, abstract, speaker bio and transcript.", "",
             "## Upcoming events"] + [ev(e) for e in upcoming] + ["", "## Recent events"] + [ev(e) for e in recent]
    lines += ["", "## Blog", "- [All posts](%sblog): talk previews, conference roundups, sponsor keynotes, webinars" % SITE,
              "- [Every post as JSON](%sblog.json): title, Markdown URL, event, speakers, talk page, video, topics" % SITE,
              "- [Every post as Markdown links](%sblog.md)" % SITE]
    lines += ["- [%s](%s): %s" % (p["Title"], p["canonical"], p["description"]) for p in posts if not p.get("ExternalURL")][:60]
    hubs = context.get("topic_hubs") or []
    if hubs:
        lines += ["", "## Topics", "- [All topics](%stopics): every Conf42 talk grouped by subject" % SITE]
        lines += ["- [%s](%s): %d talks" % (h["name"], h["url"], len(h["talks"])) for h in sorted(hubs, key=lambda h: h["name"].lower())]
    # one file per event: every talk with its Markdown page (title, speakers, abstract, takeaways, transcript)
    os.makedirs(os.path.join(base_folder, "llms"), exist_ok=True)
    listed = sorted([e for e in events if e.get("date") and e.get("talks_raw")], key=lambda e: e["date"], reverse=True)
    lines += ["", "## Talks by event", "Each file lists every talk of one event with a link to its Markdown page."]
    for e in listed:
        slug = e["short_url"].replace(".html", "")
        talks = [t for t in e["talks_raw"] if t.get("short_url") and (t.get("Name1") or "").strip()]
        ev_lines = ["# Conf42 %s %s" % (e.get("name"), e.get("year")), "",
                    "> %s, online. %d talks. Event page: %s%s" % (e["date"].isoformat(), len(talks), SITE, slug), "", "## Talks"]
        for t in talks:
            who = " and ".join(n.strip() for n in (t.get("Name1"), t.get("Name2")) if (n or "").strip())
            ev_lines.append("- [%s](%s%s.md): %s" % ((t.get("Title") or "").strip(), SITE, t["short_url"].replace(".html", ""), who))
        with open(os.path.join(base_folder, "llms", slug + ".txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(ev_lines) + "\n")
        lines.append("- [Conf42 %s %s](%sllms/%s.txt): %d talks" % (e.get("name"), e.get("year"), SITE, slug, len(talks)))
    lines += ["", "## Optional", "- [Speakers](%sspeakers)" % SITE, "- [Podcast](%spodcast)" % SITE, "- [Atom feed](%s%s)" % (SITE, FEED_FILE)]
    with open(os.path.join(base_folder, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("Writing out llms.txt + %d event files" % len(listed))


def _talk_md(talk, event):
    """The talk page as Markdown, the same content the HTML shows (title, speakers, event, abstract; once released:
    key takeaways and the transcript)."""
    url = SITE + talk["short_url"].replace(".html", "")
    people = []
    for k in (1, 2):
        name = (talk.get("Name%d" % k) or "").strip()
        if name:
            role = " @ ".join(x for x in ((talk.get("JobTitle%d" % k) or "").strip(), (talk.get("Company%d" % k) or "").strip()) if x)
            people.append("[%s](%s%s)%s" % (name, SITE, generate_speaker_url(name), " (%s)" % role if role else ""))
    out = ["# %s" % (talk.get("Title") or "").strip(), "",
           "A talk at [Conf42 %s %s](%s%s) by %s. Page: %s" % (event.get("name"), event.get("year"), SITE,
                                                              event["short_url"].replace(".html", ""), " and ".join(people), url), ""]
    yid = _youtube_id(talk)
    released = event.get("released") and yid
    if released:
        out += ["Video: https://www.youtube.com/watch?v=%s" % yid, ""]
    out += ["## Abstract", "", (talk.get("Abstract") or "").strip(), ""]
    transcript = talk.get("transcript") if isinstance(talk.get("transcript"), dict) else {}
    if released and transcript.get("summary"):
        out += ["## Key takeaways", ""] + ["- %s" % x for x in transcript["summary"]] + [""]
    if released and transcript.get("chunks"):
        out += ["## Transcript", "", re.sub(r"\s+", " ", " ".join((c.get("text") or "") for c in transcript["chunks"])).strip(), ""]
    return "\n".join(out)


def write_markdown(context, posts, base_folder):
    """<page>.md next to every talk page and blog post (linked from the page as rel=alternate type=text/markdown):
    the same text, without the layout, for agents that read Markdown."""
    n = 0
    for event in context.get("events") or []:
        if "external_url" in event or not event.get("short_url"):
            continue
        for talk in event.get("talks_raw") or []:
            if not talk.get("short_url") or not (talk.get("Name1") or "").strip():
                continue
            with open(os.path.join(base_folder, talk["short_url"].replace(".html", "") + ".md"), "w", encoding="utf-8") as f:
                f.write(_talk_md(talk, event))
            n += 1
    for p in posts:
        if p.get("ExternalURL"):
            continue
        out = ["# %s" % p["Title"], "", "Conf42 Blog, %s%s. %s" % (p["date_iso"], ", updated " + p["updated_iso"] if p["updated_iso"] != p["date_iso"] else "", p["canonical"]), ""]
        if p.get("Description"):
            out += ["In short: " + p["Description"], ""]
        out.append(p["Body"])
        talk, event = p["linked"].get("talk"), p["linked"].get("event")
        if talk and event and talk.get("short_url"):
            out += ["", "## Watch the talk", "", "[%s](%s%s) at Conf42 %s %s." % (talk.get("Title"), SITE, talk["short_url"].replace(".html", ""),
                                                                         event.get("name"), event.get("year"))]
        os.makedirs(os.path.dirname(os.path.join(base_folder, p["path"])), exist_ok=True)
        with open(os.path.join(base_folder, p["path"] + ".md"), "w", encoding="utf-8") as f:
            f.write("\n".join(out) + "\n")
        n += 1
    print("Writing out %d Markdown pages" % n)


def write_blog_index(context, posts, base_folder):
    """blog.json + blog.md (Marek 2026-11-10, like the media kit's brandkit.json): every live post with its Markdown
    twin, event, speakers, talk page, video and topics, so scripts and AI agents can filter without scraping. The
    commands on /blog (_blog_agents.html) use it. Companies only when Company1 is set; the video only once released."""
    out = []
    for p in posts:
        if p.get("ExternalURL"):
            continue
        talk, event = p["linked"].get("talk"), p["linked"].get("event")
        item = {"title": p["Title"], "url": p["canonical"], "markdown": p["canonical"] + ".md", "date": p["date_iso"],
                "updated": p["updated_iso"], "type": p.get("Type") or "", "description": p.get("Description") or "",
                "tags": [t.strip() for t in (p.get("Tags") or "").split(",") if t.strip()], "image": p.get("image_abs") or ""}
        if event and event.get("short_url"):
            slug = event["short_url"].replace(".html", "")
            item["event"] = {"slug": slug, "name": "Conf42 %s %s" % (event.get("name"), event.get("year")),
                             "date": event["date"].isoformat() if event.get("date") else "", "url": SITE + slug,
                             "talks": SITE + "llms/" + slug + ".txt"}
        if talk and talk.get("short_url"):
            turl = SITE + talk["short_url"].replace(".html", "")
            item["talk"] = {"title": (talk.get("Title") or "").strip(), "url": turl, "markdown": turl + ".md"}
            yid = _youtube_id(talk)
            if yid and event and event.get("released"):
                item["talk"]["video"] = "https://www.youtube.com/watch?v=" + yid
            item["speakers"] = []
            for k in (1, 2):
                name = (talk.get("Name%d" % k) or "").strip()
                if name:
                    sp = {"name": name, "url": SITE + generate_speaker_url(name)}
                    if (talk.get("Company%d" % k) or "").strip():
                        sp["company"] = talk["Company%d" % k].strip()
                    item["speakers"].append(sp)
            item["topics"] = [h["slug"] for h in talk.get("topics") or []]
        out.append(item)
    hubs = sorted(context.get("topic_hubs") or [], key=lambda h: h["name"].lower())
    data = {"name": "Conf42 blog", "url": SITE + "blog", "count": len(out),
            "about": "Write-ups of talks from Conf42's free online tech conferences, conference roundups, sponsor keynotes "
                     "and webinar recaps. Every post has a Markdown twin (markdown); every talk page too.",
            "topics": [{"slug": h["slug"], "name": h["name"], "url": h["url"], "talks": len(h["talks"])} for h in hubs],
            "posts": out}
    with open(os.path.join(base_folder, "blog.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    lines = ["# Conf42 blog", "", "> %s Machine-readable: %sblog.json" % (data["about"], SITE), ""]
    month = None
    for i in out:
        m = datetime.date.fromisoformat(i["date"]).strftime("%B %Y")
        if m != month:
            lines += ["", "## " + m]
            month = m
        lines.append("- [%s](%s)%s: %s" % (i["title"], i["markdown"], " (%s)" % i["event"]["name"] if i.get("event") else "", i["description"]))
    with open(os.path.join(base_folder, "blog.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("Writing out blog.json + blog.md (%d posts)" % len(out))


def write_indexnow(posts, base_folder, today=None, lastmod=None):
    """docs/<key>.txt + ./_indexnow.json (the URLs dated or updated today, for the workflow's ping step): posts, plus any
    sitemap page whose lastmod is today (talks and events released today, their speakers, topic hubs)."""
    today = (today or datetime.datetime.now(datetime.timezone.utc).date()).isoformat()
    with open(os.path.join(base_folder, INDEXNOW_KEY + ".txt"), "w") as f:
        f.write(INDEXNOW_KEY)
    urls = [p["canonical"] for p in posts if not p.get("ExternalURL") and today in (p["date_iso"], p["updated_iso"])]
    if urls:
        urls += [SITE + "blog", SITE + FEED_FILE]
    urls += sorted(SITE + u for u, d in (lastmod or {}).items() if d == today and SITE + u not in urls)
    with open(INDEXNOW_LIST, "w") as f:
        json.dump({"host": "www.conf42.com", "key": INDEXNOW_KEY, "keyLocation": SITE + INDEXNOW_KEY + ".txt", "urlList": urls}, f)
    print("IndexNow: %d URLs for today" % len(urls))
