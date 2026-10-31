"""YouTube-ready blocks for <event>/chapters.txt: a title of at most 100 characters and the description.

    <short title> | <Speaker(s)> | Conf42 <Event> <YEAR>        e.g. "... | Ananda Kumar Dey | Conf42 Prompt 2026"

    Read the abstract ➤ https://www.conf42.com/<talk page>
    Other sessions at this event ➤ https://www.conf42.com/<event short_url>
    Apply to speak ➤ https://cfp.ninja/?q=conf42&status=open
    Join Discord ➤ https://discord.gg/yQneDJdJGV

    Chapters
    0:00 ...

The short title is written by Descript's AI editor in the same job as the chapters (or by hand in state.json,
talks.<speakers>.yt_title); shorten_title() is only the fallback. Links, event-name overrides and the limit live in
settings.yml (youtube:).
"""
import collections
import csv
import os
import re
import string

NOISE = re.compile(r"\s+(Talk Type or Format:?|Talk type:?|Format:?)\s*$", re.I)


def talk_rows(ev):
    """The event's talks (banished ones included, see events.talks) with the fields the site uses for the talk page
    address."""
    from . import events
    return [{"speakers": t["speakers"], "Name1": t["name1"], "Name2": t["name2"],
             "Keywords": (t["keywords"] or "").strip(), "title": clean_title(t["title"] or ""),
             "banished": t.get("banished", False)} for t in events.talks(ev)]


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


VIDEO_STATS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_db", "video_stats.csv")
PAST = re.compile(r"\|\s*Conf42\s+(.+?)\s+(20\d\d)\s*$")


def past_names(path=VIDEO_STATS):
    """How our YouTube titles named each event before: {"Prompt": {"2024": 8}, "PE": {"2024": 3}, ...}, from the
    channel's export in src/_db/video_stats.csv (the "Video title" column)."""
    out = collections.defaultdict(collections.Counter)
    try:
        with open(path, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                m = PAST.search(r.get("Video title") or "")
                if m:
                    out[m.group(1)][m.group(2)] += 1
    except OSError:
        pass
    return out


def _words(s):
    return [w for w in re.split(r"[\s/&.-]+", s.lower()) if w]


def _initials(name):
    return "".join(w[0] for w in _words(name) if w[0].isalnum())


def event_code(ev, cfg, history=None):
    """The event's name in the title, the way earlier editions wrote it on YouTube (Marek 2026-10-29: "Conf42 Prompt
    2026", never "Conf42 PE 2026"): settings youtube.event_codes first; else the name past titles used most for this
    event - words over acronyms (Prompt Engineering -> Prompt, Platform Engineering -> Platform Eng.); else the full
    name. An acronym only when the past titles never used words, or the name already is one (SRE, DevSecOps)."""
    codes = ((cfg.get("youtube") or {}).get("event_codes") or {})
    if ev["name"] in codes:
        return str(codes[ev["name"]])
    name = re.sub(r"\(.*?\)", "", ev["name"]).strip()
    short = [x.strip().lower() for x in re.findall(r"\((.*?)\)", ev["name"])]   # "Large Language Models (LLMs)"
    full = _words(name)
    words, acronyms = [], []
    for past, years in (past_names() if history is None else history).items():
        pw, n, last = _words(past), sum(years.values()), max(years)
        # "Prompt", "Platform Eng.", "Chaos Engr": each word starts the event's word in that place
        # (a one-word name only as itself: "ML" is not MLOps; a cut word keeps 3+ letters)
        if past.lower() in short or pw and len(pw) <= len(full) and (len(full) > 1 or pw == full) and \
                all(w == f or (len(w) >= 3 and f.startswith(w)) for w, f in zip(pw, full)):
            words.append((n, last, past))
        elif len(full) > 1 and past.lower() == _initials(name):
            acronyms.append((n, last, past))
    pick = max(words or acronyms or [(0, "", name)])
    return pick[2]


def suffix(ev, cfg, speakers):
    return " | %s | Conf42 %s %s" % (speakers, event_code(ev, cfg), ev["year"])


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
    lines = [title, ""] + ([] if row.get("banished") else ["Read the abstract ➤ " + base + talk_page(ev, row)]) + [
             "Other sessions at this event ➤ " + base + ev["short_url"],
             "Apply to speak ➤ " + str(yt.get("apply_url") or "https://cfp.ninja/?q=conf42&status=open"),
             "Join Discord ➤ " + str(yt.get("discord_url") or "https://discord.gg/yQneDJdJGV"),
             "", "Chapters"] + ["%s %s" % (c["at"], c["title"]) for c in chapters]
    return title, lines
