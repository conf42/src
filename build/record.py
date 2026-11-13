"""conf42.com/record (Marek 2026-10-22): the in-browser talk recorder that replaces OBS for speakers.

A hidden page (noindex, never in the sitemap), linked from the speaker instructions. The speaker picks the event and
their talk, allows the camera and microphone, loads their PDF (or shares a screen or window for a demo) and records:
the event's New design overlay (docs/assets/js/overlays.js, the one the teasers' Overlays tab draws) with the camera in
the circle and the slides in the window, encoded in the browser (WebCodecs H.264 1080p60 + AAC, docs/assets/js/
record-worker.js) straight into "<Speaker>.mp4" on their disk. Chrome and Edge only. At Stop the recording and the slides go up to the
Conf42 Speaker Workspace on Drive (apps-script/conf42-upload.gs, metadata.yml record_upload_url) for the cloud factory.

The page gets one JSON: every upcoming event with talks, its overlay data (teasers.overlays()) and its lineup.
"""
import os

from .shared import asset_version
from .teasers import cards, overlays, past, upcoming, _event_name


def events(context):
    out = []
    for event in sorted(upcoming(context.get("events") or []), key=lambda e: e["date"]):
        # k = the talk page key (talk short_url): uploads name it so the factory never has to guess who it is
        talks = [dict(names=[n for n, _ in c["people"]], title=c["title"], k=c["key"], min=c["duration"]) for c in cards(event)]
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


def generate_factory(env, context, base_folder, gate):
    """conf42.com/<event>/factory (Marek 2026-11-13): every talk's upload state, live (_templates/factory_event.html),
    for each upcoming event and each past one since 2026 with a lineup. Unlisted: noindex, never in the sitemap."""
    evs = upcoming(context.get("events") or []) + past(context.get("events") or [])
    out = []
    for event in evs:
        talks = [dict(names=[nm for nm, _ in c["people"]], title=c["title"], k=c["key"], keynote=c["keynote"]) for c in cards(event)]
        if not talks:
            continue
        slug = event["short_url"].replace(".html", "")
        fe = dict(slug=slug, label="Conf42 %s %d" % (_event_name(event), event["date"].year), color=event.get("color") or "",
                  date="%s %d %d" % (event["date"].strftime("%B"), event["date"].day, event["date"].year),
                  status_url=context.get("record_upload_url") or "", talks=talks)
        os.makedirs(os.path.join(base_folder, slug), exist_ok=True)
        with open(os.path.join(base_folder, slug, "factory.html"), "w", encoding="utf-8") as f:
            f.write(env.get_template("factory_event.html").render(fe=fe, gate=gate))
        out.append(dict(slug=slug, label=fe["label"], date=fe["date"], upcoming=event in evs[:len(upcoming(context.get("events") or []))]))
    print("Writing out <event>/factory.html for %d events (unlisted)" % len(out))
    return out
