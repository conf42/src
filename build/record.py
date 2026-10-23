"""conf42.com/record (Marek 2026-10-22): the in-browser talk recorder that replaces OBS for speakers.

A hidden page (noindex, never in the sitemap), linked from the speaker instructions. The speaker picks the event and
their talk, allows the camera and microphone, loads their PDF (or shares a screen or window for a demo) and records:
the event's New design overlay (docs/assets/js/overlays.js, the one the teasers' Overlays tab draws) with the camera in
the circle and the slides in the window, encoded in the browser (WebCodecs H.264 1080p60 + AAC, docs/assets/js/
record-worker.js) straight into "<Speaker>.mp4" on their disk. Chrome and Edge only. Nothing is uploaded.

The page gets one JSON: every upcoming event with talks, its overlay data (teasers.overlays()) and its lineup.
"""
import os

from .shared import asset_version
from .teasers import cards, overlays, upcoming, _event_name


def events(context):
    out = []
    for event in sorted(upcoming(context.get("events") or []), key=lambda e: e["date"]):
        talks = [dict(names=[n for n, _ in c["people"]], title=c["title"]) for c in cards(event)]
        if not talks:
            continue
        slug = event["short_url"].replace(".html", "")
        ev = dict(name=_event_name(event), slug=slug, date=event["date"])
        out.append(dict(slug=slug, label="Conf42 %s %d" % (ev["name"], event["date"].year),
                        date="%s %d %d" % (event["date"].strftime("%B"), event["date"].day, event["date"].year),
                        ov=overlays(event, ev), talks=sorted(talks, key=lambda t: t["names"][0].lower())))
    return out


def generate(env, context, base_folder):
    evs = events(context)
    v = {k: asset_version(base_folder, "assets/js/%s.js" % k) for k in ("overlays", "record-worker")}
    with open(os.path.join(base_folder, "record.html"), "w", encoding="utf-8") as f:
        f.write(env.get_template("record.html").render(rec_events=evs, rec_v=v, **context))
    print("Writing out record.html (%d events)" % len(evs))
