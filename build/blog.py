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

from .shared import make_remote_address, pick_picture_file, read_csv

SITE = "https://www.conf42.com/"
BLOG_CSV = "./_db/blog.csv"
WEBINARS_CSV = "./_db/WEBINARS.csv"
SISTER_JSON = "./_db/sister_events.json"
SPLASH_FOLDER = "./assets/splash/"
FEED_FILE = "blog.xml"
FEED_SIZE = 50
VISIBLE_STATUSES = {"", "published"}
# IndexNow (Bing, Yandex, Seznam, Naver; Bing feeds ChatGPT/Copilot search): the key is public by design - it is served
# at /<key>.txt to prove the site owns the pings. The morning cron run pings the posts that went live / changed today.
INDEXNOW_KEY = "fcd04983393834bd2826cd6a2f8503d1"
INDEXNOW_LIST = "./_indexnow.json"


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
        event = self.events.get(short_url)
        if not event:
            return None, None
        for talk in event.get("talks_raw") or []:
            if _norm(talk.get("Name1")) == _norm(name1):
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


def _image(post, linked, base_folder):
    """ThumbnailPath as given (local splash -> its 500px JPEG, or an absolute URL); empty -> from what the post is about."""
    path = (post.get("ThumbnailPath") or "").strip()
    if path:
        return path if re.match(r"^https?://", path) else pick_picture_file(base_folder + "/", path)
    talk, event = linked.get("talk"), linked.get("event")
    if talk and talk.get("Picture"):
        return make_remote_address("headshots", talk["Picture"])
    if event and event.get("thumbnail_path"):
        return event["thumbnail_path"]
    webinar = linked.get("webinar")
    if webinar and webinar.get("Splash"):
        return pick_picture_file(base_folder + "/", SPLASH_FOLDER + webinar["Splash"])
    sister = linked.get("sister")
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
    yid = (talk or {}).get("YouTubeId")
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
        "publisher": {"@type": "Organization", "name": "Conf42", "url": SITE},
    }
    if event and event.get("date"):
        data["uploadDate"] = event["date"].isoformat() + "T17:00:00Z"
    duration = _iso_duration(talk.get("Duration"))
    if duration:
        data["duration"] = duration
    if speakers:
        data["actor"] = [{"@type": "Person", "name": n} for n in speakers]
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
        "author": {"@type": "Person", "name": author} if author and author != "Conf42"
                  else {"@type": "Organization", "name": "Conf42", "url": SITE},
        "publisher": {"@type": "Organization", "name": "Conf42", "url": SITE,
                      "logo": {"@type": "ImageObject", "url": SITE + "assets/conf42/CONF42.QR.png"}},
        "isAccessibleForFree": True,
    }
    if post.get("image_abs"):
        data["image"] = [post["image_abs"]]
    if post.get("Tags"):
        data["keywords"] = [t.strip() for t in post["Tags"].split(",") if t.strip()]
    event = post["linked"].get("event")
    if event:
        data["about"] = {"@type": "Event", "name": "Conf42 %s %s" % (event.get("name"), event.get("year")),
                         "url": SITE + event.get("short_url", "")}
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
    talk = post["linked"].get("talk")
    video = video_jsonld(talk, event, post["canonical"]) if talk and (event or {}).get("released") else None
    if video:
        out.append(video)
    return out


def _date(value):
    return dateutil.parser.parse(value).date() if (value or "").strip() else None


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
    for row in rows:
        post = {k: (v.strip() if isinstance(v, str) and k != "Body" else v) for k, v in row.items() if k}
        slug = post.get("ShortURL") or post.get("ExternalURL") or post.get("Title")
        status = (post.get("Status") or "").lower()
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
        try:
            updated = max(_date(post.get("Updated")) or date, date)
        except (ValueError, OverflowError):
            updated = date
        post["linked"] = linked
        post["Date"] = datetime.datetime.combine(date, datetime.time())
        post["date_iso"] = date.isoformat()
        post["updated_iso"] = updated.isoformat()
        post["Body"] = _body(post.get("Body"))
        post["ThumbnailPath"] = _image(post, linked, base_folder)
        post["image_abs"] = absolute(post["ThumbnailPath"])
        if not post.get("ExternalURL"):
            post["canonical"] = SITE + post["ShortURL"]
            post["description"] = post.get("Description") or re.sub(r"\s+", " ", re.sub(r"[#*_>\[\]`]|\(http[^)]*\)", "", post["Body"]))[:200].strip()
            post["jsonld"] = _post_jsonld(post)
        visible.append(post)
    visible.sort(key=lambda p: (p["Date"], p.get("ShortURL") or ""), reverse=True)
    return visible, dropped


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


def write_robots(base_folder):
    """robots.txt: everyone welcome, AI *search* crawlers named. Cloudflare prepends its managed block (content signals,
    ai-train=no: ClaudeBot, GPTBot, Google-Extended... disallowed) - training bots are left to it, never re-allowed here."""
    lines = ["User-agent: *", "Allow: /", ""]
    for bot in ("OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Perplexity-User", "Claude-SearchBot", "Claude-User", "Bingbot"):
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
    lines += ["", "## Blog", "- [All posts](%sblog): talk previews, conference roundups, sponsor keynotes, webinars" % SITE]
    lines += ["- [%s](%s): %s" % (p["Title"], p["canonical"], p["description"]) for p in posts if not p.get("ExternalURL")][:60]
    lines += ["", "## Optional", "- [Speakers](%sspeakers)" % SITE, "- [Podcast](%spodcast)" % SITE, "- [Atom feed](%s%s)" % (SITE, FEED_FILE)]
    with open(os.path.join(base_folder, "llms.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("Writing out llms.txt")


def write_indexnow(posts, base_folder, today=None):
    """docs/<key>.txt + ./_indexnow.json (the URLs dated or updated today, for the workflow's ping step)."""
    today = (today or datetime.datetime.now(datetime.timezone.utc).date()).isoformat()
    with open(os.path.join(base_folder, INDEXNOW_KEY + ".txt"), "w") as f:
        f.write(INDEXNOW_KEY)
    urls = [p["canonical"] for p in posts if not p.get("ExternalURL") and today in (p["date_iso"], p["updated_iso"])]
    if urls:
        urls += [SITE + "blog", SITE + FEED_FILE]
    with open(INDEXNOW_LIST, "w") as f:
        json.dump({"host": "www.conf42.com", "key": INDEXNOW_KEY, "keyLocation": SITE + INDEXNOW_KEY + ".txt", "urlList": urls}, f)
    print("IndexNow: %d URLs for today" % len(urls))
