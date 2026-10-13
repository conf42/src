"""conf42.com/headshots (Marek 2026-10-13): the headshot maker of the sister sites (sreday.com/headshots/), for Conf42.

A hidden organizer tool (noindex, never in the sitemap). Keyed (transparent) photos go onto the chosen event's
starfield background, black and white, framed tight like every Conf42 headshot: from the top of the hair to just
below the jaw. Output: the 500x400 PNG static/headshots/ uses, named "<Speaker>_<suffix>.png". One by one with every
setting, or batches of up to 30 with Auto. Everything runs in the browser; nothing is uploaded.

The dropdown lists every current and future event, each with its background: headshot-backgrounds/<event name>.png
(Marek's templates; Chaos Engineering is the background measured from its 2025 headshots, Tokenomics the Cloud Native
template recoloured to #20633E: no Conf42 headshots exist on it yet). They are copied to docs/assets/headshot-bg/.

The file suffix is the one the event's talk sheet already uses for its pictures ("_prompt", "_platform"), else the one
of the latest sheet of the same topic, else the event's short url without the year.
"""
import collections
import datetime
import glob
import os
import re
import shutil

SRC = "headshot-backgrounds"
DEST = os.path.join("assets", "headshot-bg")


def _suffix(event):
    if (event.get("name") or "").strip().lower() == "remix":   # Remix re-runs other events' talks: its sheet holds their pictures
        return "remix"
    db = str(event.get("db_path") or "")
    prefix = re.sub(r"_\d{4}\.csv$", "", os.path.basename(db))
    sheets = sorted(glob.glob(os.path.join("_db", prefix + "_*.csv")), reverse=True) if prefix else []
    for sheet in sheets:
        import csv
        with open(sheet, encoding="utf-8") as f:
            found = collections.Counter(m.group(1).lower() for r in csv.DictReader(f)
                                        for m in [re.search(r"_([A-Za-z0-9]+)\.png$", (r.get("Picture") or "").strip())] if m)
        if found:
            return found.most_common(1)[0][0]
    return re.sub(r"\d+", "", str(event.get("short_url") or "")).replace(".html", "") or "conf42"


def options(events, base_folder, today=None):
    """[{label, bg, suffix, color, date}] for every event from today on that has a background, soonest first."""
    today = today or datetime.date.today()
    os.makedirs(os.path.join(base_folder, DEST), exist_ok=True)
    out = []
    for e in sorted((e for e in events if e.get("date") and e["date"] >= today and "external_url" not in e), key=lambda e: e["date"]):
        name = (e.get("name") or "").strip()
        src = os.path.join(SRC, name + ".png")
        if not os.path.isfile(src):
            print("WARN headshots: no background for %s (%s)" % (name, src))
            continue
        dest = os.path.join(base_folder, DEST, name + ".png")
        if not os.path.exists(dest) or os.path.getmtime(dest) < os.path.getmtime(src):
            shutil.copyfile(src, dest)
        out.append(dict(label="%s %d" % (name, e["date"].year), date="%s %d %d" % (e["date"].strftime("%B"), e["date"].day, e["date"].year),
                        bg="./" + DEST.replace(os.sep, "/") + "/" + name + ".png", suffix=_suffix(e), color=str(e.get("color") or "#1b2a4e")))
    return out


def generate(env, context, base_folder):
    opts = options(context.get("events") or [], base_folder)
    with open(os.path.join(base_folder, "headshots.html"), "w", encoding="utf-8") as f:
        f.write(env.get_template("headshots.html").render(hs_events=opts, **context))
    print("Writing out headshots.html (%d events)" % len(opts))
