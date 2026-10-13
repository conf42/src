"""Webinars: free one-hour live sessions on Luma, one row each in _db/WEBINARS.csv (Marek 2026-10-12).

The home page shows the next three upcoming ones; with none upcoming it keeps the latest past one up so the
band never disappears. Times are stored once (Date + Time in Timezone) and shown in the viewer's own timezone
by a small script in _webinars_section.html. Until the webinar pages ship, a card links to its Luma event.
"""
import datetime
import os
from zoneinfo import ZoneInfo

from .shared import make_remote_address, pick_picture_file, read_talk_csv

WEBINARS_CSV = "./_db/WEBINARS.csv"
SPLASH_FOLDER = "./assets/splash/"


def load_webinars(base_folder, path=WEBINARS_CSV):
    if not os.path.isfile(path):
        return {"webinars": [], "webinars_past": False}
    now = datetime.datetime.now(datetime.timezone.utc)
    webinars = []
    for w in read_talk_csv(path):
        if not w.get("Title") or not w.get("Date"):
            continue
        tz = ZoneInfo(w.get("Timezone") or "UTC")
        start = datetime.datetime.fromisoformat("%sT%s" % (w["Date"], w.get("Time") or "00:00")).replace(tzinfo=tz)
        end = start + datetime.timedelta(minutes=int(w.get("Duration") or 60))
        w["start"], w["end"] = start, end
        w["start_iso"] = start.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        w["thumbnail_path"] = pick_picture_file(base_folder + "/", SPLASH_FOLDER + w["Splash"]) if w.get("Splash") else ""
        w["picture"] = make_remote_address("headshots", w["Picture1"]) if w.get("Picture1") else ""
        w["is_past"] = end <= now
        if w["is_past"] and w.get("YouTube"):
            w["url"] = w["YouTube"]
        else:
            w["url"] = w.get("LumaURL") or "https://lu.ma/event/%s" % w.get("LumaEvt", "")
        webinars.append(w)
    upcoming = sorted((w for w in webinars if not w["is_past"]), key=lambda w: w["start"])
    past = sorted((w for w in webinars if w["is_past"]), key=lambda w: w["start"], reverse=True)
    print("Webinars: %d upcoming, %d past" % (len(upcoming), len(past)))
    return {"webinars": upcoming[:3] or past[:1], "webinars_past": not upcoming}
