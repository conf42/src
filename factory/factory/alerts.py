"""The factory's one email (Marek 2026-11-13): "Need more Descript credits", with the top-up link, when Descript
answers 402 (out of AI credits or media minutes). Everything else shows on conf42.com/<event>/factory - no other mail.

Sent by the "Conf42 upload" Apps Script (action "credits", the UPLOAD_FEED key), which mails its owner (or the
NOTIFY_TO script property) and sends at most one such email every 12 hours, however many talks hit the wall.
Without UPLOAD_FEED (a PC that never set it) nothing is sent; the run log says so.
"""
import json
import os
import urllib.parse

TOP_UP = "https://web.descript.com/"   # then Settings (profile photo, top right) > Usage > Top up
HELP = "https://help.descript.com/billing-payments-plans/top-ups"
_sent = set()


def credits_out(event_title, talk=None, log=print):
    if event_title in _sent:
        return False
    _sent.add(event_title)
    feed = os.environ.get("UPLOAD_FEED") or ""
    u = urllib.parse.urlparse(feed)
    token = (urllib.parse.parse_qs(u.query).get("token") or [""])[0]
    if not token:
        log("out of Descript credits - no UPLOAD_FEED here, so no email (top up: %s)" % TOP_UP)
        return False
    body = {"action": "credits", "token": token, "event": event_title, "talk": talk or "", "top_up": TOP_UP, "help": HELP}
    try:
        import requests
        r = requests.post(urllib.parse.urlunparse(u._replace(query="")), data=json.dumps(body), timeout=60)
        ok = r.ok and (r.json() or {}).get("ok")
        log("out of Descript credits - email %s" % ("sent" if ok else "not sent (%s)" % r.text[:120]))
        return bool(ok)
    except Exception as e:                               # noqa: BLE001 - a lost email never fails the run
        log("out of Descript credits - email failed (%s)" % e)
        return False
