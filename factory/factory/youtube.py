"""YouTube-ready blocks for <event>/chapters.txt: a title of at most 100 characters and the description.

    <short title> | <Speaker(s)> | Conf42 <CODE><YEAR>          e.g. "... | Ananda Kumar Dey | Conf42 DSO2026"

    Read the abstract ➤ https://www.conf42.com/<talk page>
    Other sessions at this event ➤ https://www.conf42.com/<event short_url>
    Apply to speak ➤ https://cfp.ninja/?q=conf42&status=open
    Join Discord ➤ https://discord.gg/yQneDJdJGV

    Chapters
    0:00 ...

The short title is written by Descript's AI editor in the same job as the chapters (or by hand in state.json,
talks.<speakers>.yt_title); shorten_title() is only the fallback. Links, the event code and the limit live in
settings.yml (youtube:).
"""
import csv
import re
import string

NOISE = re.compile(r"\s+(Talk Type or Format:?|Talk type:?|Format:?)\s*$", re.I)


def talk_rows(ev):
    """The event CSV rows with the fields the site uses for the talk page address."""
    with open(ev["db_path"], encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    out = []
    for r in rows:
        n1, n2 = (r.get("Name1") or "").strip(), (r.get("Name2") or "").strip()
        if n1:
            out.append({"speakers": n1 + (" & " + n2 if n2 else ""), "Name1": n1, "Name2": n2,
                        "Keywords": (r.get("Keywords") or "").strip(), "title": clean_title(r.get("Title") or "")})
    return out


def clean_title(t):
    return NOISE.sub("", re.sub(r"\s+", " ", str(t)).strip()).strip()


def talk_page(ev, row):
    """Same as src/build/shared.py generate_short_url (kept in sync by hand: the factory also runs from a slim clone
    without build/)."""
    url = "{event}_{year}_{name1}{name2}{keywords}".format(
        event=ev["name"].replace(" ", "_"), year=str(ev["year"]).replace(" ", "_"),
        name1=row["Name1"].replace(" ", "_"),
        name2=("_" + row["Name2"].replace(" ", "_")) if row.get("Name2") else "",
        keywords=("_" + row["Keywords"].replace(",", "_").replace(" ", "_")) if row.get("Keywords") else "")
    url = "".join(filter(lambda x: x in string.printable, url))
    url = re.sub(r"[\W]+", "", url)
    return url[:100]


def event_code(ev, cfg):
    """DevSecOps -> DSO: settings youtube.event_codes first, else the capitals of a CamelCase name, else initials."""
    codes = ((cfg.get("youtube") or {}).get("event_codes") or {})
    if ev["name"] in codes:
        return str(codes[ev["name"]])
    name = re.sub(r"\(.*?\)", "", ev["name"]).strip()
    caps = re.findall(r"[A-Z]", name)
    words = [w for w in re.split(r"[\s/&-]+", name) if w]
    if len(words) == 1 and len(caps) >= 2:
        return "".join(caps)
    if len(words) >= 2:
        return "".join(w[0].upper() for w in words if w[0].isalnum())
    return name.replace(" ", "")


def suffix(ev, cfg, speakers):
    return " | %s | Conf42 %s%s" % (speakers, event_code(ev, cfg), ev["year"])


def budget(ev, cfg, speakers):
    limit = int((cfg.get("youtube") or {}).get("title_max") or 100)
    return limit - len(suffix(ev, cfg, speakers))


def shorten_title(title, room):
    """Fallback when nobody wrote a short title: drop trailing 'for/in/with ...' phrases, then the subtitle after a
    colon, then cut at a word boundary."""
    t = clean_title(title)
    while len(t) > room:
        m = re.match(r"^(.*\S)\s+(for|in|with|at|on|using|across|through|via)\s+[^:]+$", t, re.I)
        if m and len(m.group(1)) >= 20:
            t = m.group(1).rstrip(",;:-")
            continue
        break
    if len(t) > room and ":" in t and len(t.split(":")[0]) >= 12:
        t = t.split(":")[0].strip()
    if len(t) > room:
        t = t[:room].rsplit(" ", 1)[0].rstrip(",;:-&")
    return t


def title_for(ev, cfg, row, written=None):
    room = budget(ev, cfg, row["speakers"])
    t = clean_title(written or "") if written else ""
    if not t or len(t) > room:
        t = row["title"] if len(row["title"]) <= room else shorten_title(row["title"], room)
    return t + suffix(ev, cfg, row["speakers"])


def block(ev, cfg, row, chapters, written=None):
    yt = cfg.get("youtube") or {}
    base = str(yt.get("site") or "https://www.conf42.com/").rstrip("/") + "/"
    title = title_for(ev, cfg, row, written)
    lines = [title, "",
             "Read the abstract ➤ " + base + talk_page(ev, row),
             "Other sessions at this event ➤ " + base + ev["short_url"],
             "Apply to speak ➤ " + str(yt.get("apply_url") or "https://cfp.ninja/?q=conf42&status=open"),
             "Join Discord ➤ " + str(yt.get("discord_url") or "https://discord.gg/yQneDJdJGV"),
             "", "Chapters"] + ["%s %s" % (c["at"], c["title"]) for c in chapters]
    return title, lines
