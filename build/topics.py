"""Topic hubs (conf42.com/topics/<slug>, Marek 2026-11-10): every Conf42 talk on one subject across all events and
years, newest first, with the blog posts about them. The page AI answers cite for "best talks on X".

_db/topics.yaml is the list: slug, name, a regex matched against the talk's Title + Keywords (case-insensitive),
optional `events` (event names whose every talk belongs, e.g. Golang for Go), and a short intro written from what those
talks actually cover. A topic without an intro, or with fewer than MIN_TALKS talks, gets no page - no thin doorways.
"""
import os
import re

import yaml

from .blog import ORG_REF, SITE, released_on

TOPICS_YAML = "./_db/topics.yaml"
MIN_TALKS = 15
TALK_TOPICS_SHOWN = 3


def _key(s):
    return re.sub(r"\W+", "", (s or "").casefold())


def load_topics(path=TOPICS_YAML):
    with open(path, encoding="utf-8") as f:
        topics = yaml.safe_load(f) or []
    for t in topics:
        t["re"] = re.compile(t["match"], re.I)
        t["events"] = set(t.get("events") or [])
    return topics


def assign(context, path=TOPICS_YAML):
    """-> the hubs that get a page; also sets talk["topics"] (up to TALK_TOPICS_SHOWN hubs, the smallest first - the most
    specific link) for the talk page."""
    try:
        topics = load_topics(path)
    except Exception as e:
        print("Couldn't read topics", e)
        return []
    for t in topics:
        t["talks"] = []
    for event in context.get("events") or []:
        if "external_url" in event or not event.get("short_url"):
            continue
        for talk in event.get("talks_raw") or []:
            if not (talk.get("Name1") or "").strip() or not talk.get("short_url"):
                continue
            text = "%s | %s" % (talk.get("Title") or "", talk.get("Keywords") or "")
            for t in topics:
                if event.get("name") in t["events"] or t["re"].search(text):
                    t["talks"].append(dict(event=event, talk=talk))
    for t in topics:
        # a talk re-aired (Remix) is listed once, at its first airing; its re-air page still links the hub
        t["all"] = t["talks"]
        t["talks"].sort(key=lambda i: (i["event"].get("date"), i["talk"].get("Title") or ""))
        seen, items = set(), []
        for i in t["talks"]:
            key = (_key(i["talk"].get("Title")), _key(i["talk"].get("Name1")))
            if key not in seen:
                seen.add(key)
                items.append(i)
        t["talks"] = items[::-1]
    hubs = [t for t in topics if (t.get("intro") or "").strip() and len(t["talks"]) >= MIN_TALKS]
    for t in topics:
        if t not in hubs and len(t["talks"]) >= MIN_TALKS:
            print("WARN topics: %s has %d talks but no intro - no page" % (t["slug"], len(t["talks"])))
    for hub in hubs:
        hub["lastmod"] = max((d for d in (released_on(i["event"]) for i in hub["talks"]) if d), default=None)
        hub["url"] = SITE + "topics/" + hub["slug"]
        hub["n"] = len(hub["talks"])
        for item in hub.pop("all"):
            item["talk"].setdefault("topics", []).append(hub)
    for event in context.get("events") or []:
        for talk in event.get("talks_raw") or []:
            if talk.get("topics"):
                talk["topics"] = sorted(talk["topics"], key=lambda h: len(h["talks"]))[:TALK_TOPICS_SHOWN]
    print("Topic hubs: %d pages (%s)" % (len(hubs), ", ".join("%s %d" % (h["slug"], len(h["talks"])) for h in hubs)))
    return hubs


def _jsonld(hub, posts):
    items = [{"@type": "ListItem", "position": i + 1, "name": it["talk"].get("Title") or "",
              "url": SITE + it["talk"]["short_url"].replace(".html", "")} for i, it in enumerate(hub["talks"])]
    return [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Conf42 talks on %s" % hub["name"],
             "url": hub["url"], "description": hub["intro"].strip(), "publisher": ORG_REF,
             "isPartOf": {"@id": SITE + "#website"}, **({"dateModified": hub["lastmod"]} if hub["lastmod"] else {}),
             "mainEntity": {"@type": "ItemList", "numberOfItems": len(items), "itemListElement": items}},
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Conf42", "item": SITE},
                {"@type": "ListItem", "position": 2, "name": "Topics", "item": SITE + "topics"},
                {"@type": "ListItem", "position": 3, "name": hub["name"], "item": hub["url"]}]}]


def generate(env, context, hubs, base_folder, register_url):
    """docs/topics/<slug>.html per hub + docs/topics.html (the list)."""
    if not hubs:
        return
    os.makedirs(os.path.join(base_folder, "topics"), exist_ok=True)
    posts = [p for p in context.get("posts") or [] if not p.get("ExternalURL")]
    template = env.get_template("topic.html")
    for hub in hubs:
        urls = {i["talk"]["short_url"] for i in hub["talks"]}
        hub_posts = [p for p in posts if ((p.get("linked") or {}).get("talk") or {}).get("short_url") in urls][:12]
        speakers = {}
        for i in hub["talks"]:
            for n in (i["talk"].get("Name1"), i["talk"].get("Name2")):
                if (n or "").strip():
                    speakers[n.strip()] = speakers.get(n.strip(), 0) + 1
        hub["n_events"] = len({id(i["event"]) for i in hub["talks"]})
        hub["n_speakers"] = len(speakers)
        with open(os.path.join(base_folder, "topics", hub["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(template.render(hub=hub, hub_posts=hub_posts, base_root=True, canonical=hub["url"],
                                    topic_ld=_jsonld(hub, hub_posts), **context))
        register_url("topics/" + hub["slug"], lastmod=hub["lastmod"])
    with open(os.path.join(base_folder, "topics.html"), "w", encoding="utf-8") as f:
        f.write(template.render(hub=None, hubs=sorted(hubs, key=lambda h: h["name"].lower()), canonical=SITE + "topics",
                                topic_ld=[{"@context": "https://schema.org", "@type": "CollectionPage",
                                           "name": "Conf42 talks by topic", "url": SITE + "topics", "publisher": ORG_REF,
                                           "hasPart": [{"@type": "CollectionPage", "name": h["name"], "url": h["url"]}
                                                       for h in hubs]}], **context))
    register_url("topics", lastmod=max((h["lastmod"] for h in hubs if h["lastmod"]), default=None))
    print("Writing out topics.html + %d topic hubs" % len(hubs))
