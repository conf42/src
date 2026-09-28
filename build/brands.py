"""conf42.com/brands: brands.yaml + live numbers from each sister site's published metadata.yml.

For every in-person brand: events = upcoming + past listed on its home page, cities = distinct city slugs of those
events (./2026-san-francisco-q4/ -> san-francisco), since = the earliest year, next = the first upcoming event whose
own metadata.yml has a start in the future (name without "2026 Q4", its date_string, its page). Anything that cannot be
fetched falls back to brands.yaml, so the build never fails on a sister site being down.
"""
import datetime
import re
import urllib.request

import yaml

TIMEOUT = 12


def _yaml(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (conf42 build)"})
    return yaml.safe_load(urllib.request.urlopen(req, timeout=TIMEOUT).read().decode("utf-8", "ignore")) or {}


def _slug(url):
    return str(url or "").strip("./").rstrip("/")


def _city(slug):
    return re.sub(r"^20\d\d-|-q\d$|-20\d\d$", "", slug)


def live(site):
    home = _yaml(site.rstrip("/") + "/metadata.yml")
    up = [e for e in (home.get("events") or []) if isinstance(e, dict)]
    past = [e for e in (home.get("events_past") or []) if isinstance(e, dict)]
    slugs = [s for s in (_slug(e.get("url")) for e in up + past) if re.match(r"^20\d\d-", s)]
    out = {"events": len(up) + len(past), "cities": len({_city(s) for s in slugs}) or None,
           "since": min(int(s[:4]) for s in slugs) if slugs else None, "next": None}
    now = datetime.datetime.now(datetime.timezone.utc)
    for e in up[:6]:
        slug = _slug(e.get("url"))
        if not slug:
            continue
        try:
            em = _yaml("%s/%s/metadata.yml" % (site.rstrip("/"), slug))
        except Exception:
            continue
        start = str(em.get("start_time") or "")
        try:
            if start and datetime.datetime.fromisoformat(start) < now:
                continue
        except ValueError:
            pass
        name = re.sub(r"\s+20\d\d(\s+Q\d)?\s*$", "", str(e.get("name") or slug)).strip()
        out["next"] = {"name": name, "date": str(em.get("date_string") or ""), "url": site.rstrip("/") + "/" + slug + "/"}
        break
    return out


def brands_context(path, events):
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    own = [e for e in events if "external_url" not in e]
    talks = sum(len(e.get("talks_raw") or []) for e in own)
    years = [int(str(e.get("date"))[:4]) for e in own if str(e.get("date") or "")[:4].isdigit()]
    for b in data["brands"]:
        if b.get("key") == "conf42":
            b["stats"] = [("%d" % len(own), "conferences"), ("{:,}+".format(talks // 100 * 100), "talks"),
                          (str(min(years)) if years else "2020", "since")]
            continue
        fb = b.get("fallback") or {}
        try:
            got = live(b["site"])
            print("  brands: %s live - %s events, next %s" % (b["name"], got["events"], (got["next"] or {}).get("name")))
        except Exception as ex:
            print("  brands: %s not reachable (%s) - using brands.yaml" % (b["name"], str(ex)[:60]))
            got = {}
        events_n = got.get("events") or fb.get("events")
        cities = got.get("cities") or fb.get("cities")
        since = got.get("since") or fb.get("since")
        second = (b["home"], "home") if b.get("home") else (str(cities), "city" if cities == 1 else "cities")
        b["stats"] = [(str(events_n), "events" if b["key"] != "pec" else "editions"), second, (str(since), "since")]
        b["next"] = got.get("next")
        if b["next"] and b.get("short"):
            b["next"]["name"] = b["next"]["name"].replace(b["name"], b["short"])
    return data
