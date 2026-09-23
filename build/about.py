"""
"About the conference" panel data for every event page (2026-09-23).

Ported from the SREday / LLMday / PLATFORMday sites (their _event_template/_build/generate.py):
a job-title filter that keeps job titles out of "Companies presenting", plus keyword matching of
every talk (title + abstract) into the categories of the event's SERIES in the repo-root about.yaml.
Series key = short_url minus the trailing year, so all editions of e.g. "sre" share one category list.

Conf42 differences from the sister sites:
- Company1 / Company2 are both used; dual affiliations are split on " / " and " | " (NOT on "&",
  because AT&T, S&P Global, McKinsey & Company are single companies here).
- Company names are lightly normalised (legal suffixes, "Title at Company", a few aliases).
- Topic buckets are sorted by talk count (most talks first); "...and more" is always last.
- No `speakers` metadata, so the "more talks soon" line uses talk count + days to the event.
"""
import datetime
import os
import re

import yaml

ABOUT_MIN_TALKS = 3       # below this: blurb only, no companies / topics
ABOUT_FULL_LINEUP = 12    # fewer talks than this on an upcoming event = "more talks soon"
ABOUT_QUIET_DAYS = 14     # more days than this to the event = the lineup is still growing


# ── "Companies presenting" hygiene (ported) ───────────────────────────────────
# Speakers who prefer to stay stealth often put a JOB TITLE in the company column
# ("Principal Software Engineer", "Team Lead, SRE", "ex-Google SRE"). _jt_part_is_title()
# decides, per affiliation part, whether a value is a title rather than a company. Company
# names that merely contain such words survive ("Varnish Software", "Reliability Engineering Lab").

_JT_EXPLICIT = {
    'stealth', 'stealth startup', 'stealth mode', 'sre author', 'independent', 'freelance',
    'freelancer', 'self-employed', 'self employed', 'consultant', 'n/a', 'na', 'none', 'tbd', '-',
    'various', 'multiple', 'private', 'personal', 'confidential', 'undisclosed', 'own company',
}
# a value ENDING in one of these words is a role, not a company
_JT_ROLE_NOUNS = {
    'engineer', 'engineers', 'developer', 'developers', 'architect', 'scientist', 'researcher',
    'consultant', 'advisor', 'adviser', 'lead', 'manager', 'director', 'founder', 'co-founder',
    'cofounder', 'cto', 'ceo', 'cio', 'coo', 'cpo', 'ciso', 'vp', 'head', 'sre', 'devops',
    'evangelist', 'advocate', 'specialist', 'analyst', 'author', 'student', 'professor',
    'contractor', 'principal', 'intern', 'owner', 'strategist', 'practitioner', 'expert', 'coach',
    'trainer', 'programmer', 'administrator', 'technologist', 'executive', 'officer', 'president',
    'speaker', 'blogger', 'investor', 'mentor', 'fellow', 'phd', 'entrepreneur', 'designer',
    'writer', 'hacker', 'tester', 'freelancer', 'supervisor',
}
# words that only ever appear in titles, never as the distinctive part of a company name
_JT_VOCAB = {
    'senior', 'sr', 'junior', 'jr', 'staff', 'principal', 'lead', 'chief', 'head', 'of', 'and',
    'the', 'a', 'ai', 'ml', 'mlops', 'devops', 'devsecops', 'sre', 'data', 'cloud', 'platform',
    'software', 'site', 'reliability', 'security', 'full', 'stack', 'fullstack', 'full-stack',
    'backend', 'back-end', 'frontend', 'front-end', 'web', 'mobile', 'systems', 'system',
    'infrastructure', 'infra', 'engineering', 'science', 'product', 'technical', 'tech', 'it',
    'observability', 'kubernetes', 'network', 'solutions', 'team', 'engineer', 'developer',
    'architect', 'scientist', 'researcher', 'consultant', 'advisor', 'manager', 'director',
    'founder', 'analyst', 'specialist', 'evangelist', 'advocate', 'freelance', 'independent',
    'contractor', 'author', 'expert', 'practitioner', 'strategist', 'programmer', 'ex',
    'applications', 'business',
} | _JT_ROLE_NOUNS
_JT_SENIORITY = re.compile(r'\b(senior|sr\.?|junior|jr\.?|staff|principal|chief|head of|vp of|director of|team lead)\b', re.I)
# generic tech nouns: a short part made only of these next to a title part is a title fragment
_JT_GENERIC = {'cloud', 'software', 'data', 'ai', 'ml', 'platform', 'security', 'systems', 'infrastructure', 'azure', 'aws', 'gcp'}

# dual affiliations in the Conf42 CSVs look like "Grafana Labs / K6" or "Lore | Contagious Health"
_AFFIL_SEP = re.compile(r'\s+[/|]\s+')


def _jt_tokens(part):
    return [t for t in re.split(r"[\s,/|]+", part.lower().strip()) if t]


def _jt_part_is_title(part):
    p = part.strip()
    if not p:
        return True
    low = p.lower()
    if low in _JT_EXPLICIT:
        return True
    toks = _jt_tokens(p)
    if not toks:
        return True
    last = toks[-1].strip('.()')
    if last in _JT_ROLE_NOUNS:
        return True
    if toks[0].startswith('ex-') or ' ex-' in low:
        return True
    if _JT_SENIORITY.search(p) and any(t.strip('.()') in _JT_ROLE_NOUNS for t in toks):
        return True
    if all(t.strip('.()') in _JT_VOCAB for t in toks):
        return True
    return False


def looks_like_job_title(org):
    """True when the whole company value should be dropped (every part is a title)."""
    return all(_jt_part_is_title(p) for p in _AFFIL_SEP.split(org))


def company_parts(org):
    """The parts of a company value that are real companies (titles removed).
    "Principal SDET at Microsoft" becomes "Microsoft" BEFORE the title test, so the company survives."""
    parts = [_strip_title_at(p.strip()) for p in _AFFIL_SEP.split(org or '')]
    flags = [_jt_part_is_title(p) for p in parts]
    if any(flags):
        # sibling rule: "Azure Cloud / AI Architect and Advisor" -> "Azure Cloud" is a title fragment
        for i, p in enumerate(parts):
            toks = _jt_tokens(p)
            if not flags[i] and 0 < len(toks) <= 2 and all(t in _JT_GENERIC for t in toks):
                flags[i] = True
    return [p for p, f in zip(parts, flags) if p and not f]


# ── company name normalisation (Conf42 only) ─────────────────────────────────
# "Principal SDET at Microsoft" -> "Microsoft"; "Amazon Web Services, Inc." -> "AWS";
# "Microsoft Corporation" -> "Microsoft". Distinct brands are NOT merged (Google Cloud stays).
_TITLE_AT_RX = re.compile(r'^(?P<title>.+?)\s+at\s+(?P<org>.+)$', re.I)
_ORG_SUFFIX = re.compile(
    r'[\s,]*(?:&\s*co\.?|\b(?:inc|llc|ltd|limited|corp|corporation|gmbh|plc|pvt\.?\s*ltd|s\.?a\.?|b\.?v\.?)\b\.?)\s*$',
    re.I)
_ORG_ALIASES = {
    'amazon web services': 'AWS',
    'amazon web services (aws)': 'AWS',
    'aws (amazon web services)': 'AWS',
    'amazon.com': 'Amazon',
    'jpmorganchase': 'JPMorgan Chase',
    'jp morgan chase': 'JPMorgan Chase',
    'jpmorgan chase & co': 'JPMorgan Chase',
    'jpmorgan': 'JPMorgan Chase',
    'google llc': 'Google',
    'meta platforms': 'Meta',
    'ibm corporation': 'IBM',
    'international business machines': 'IBM',
    'tata consultancy services': 'TCS',
    'tata consultancy services (tcs)': 'TCS',
    'tata consultancy services(tcs)': 'TCS',
    'wells fargo bank': 'Wells Fargo',
    'wells fargo bank n.a': 'Wells Fargo',
    'microsoft corp': 'Microsoft',
}
_ACADEMIC = ('university', 'universit', 'institute of technology', 'college', 'polytechnic')


def _title_side_is_role(text):
    toks = _jt_tokens(text)
    if not toks:
        return False
    if _JT_SENIORITY.search(text):
        return True
    return any(t.strip('.()') in _JT_ROLE_NOUNS for t in toks)


def _strip_title_at(name):
    """"Title at Org" -> "Org", only when the left side really reads like a role
    (so "The University of Texas at Austin" is left alone)."""
    m = _TITLE_AT_RX.match(name or '')
    if m and _title_side_is_role(m.group('title')):
        return m.group('org').strip()
    return name


def normalise_company(name):
    name = _strip_title_at((name or '').strip())
    if not name:
        return ''
    # strip legal suffixes (twice: "Pvt. Ltd." / "Corp Inc")
    for _ in range(2):
        stripped = _ORG_SUFFIX.sub('', name).strip()
        if not stripped or stripped == name:
            break
        name = stripped
    name = name.strip(' .,;')
    alias = _ORG_ALIASES.get(name.lower())
    return alias or name


def is_academic(name):
    low = (name or '').lower()
    return any(a in low for a in _ACADEMIC)


# ── config ───────────────────────────────────────────────────────────────────
_CONFIG_CACHE = {}
_CATEGORY_CACHE = {}
_WARNED_SERIES = set()


def series_key(event):
    return re.sub(r'\d{4}$', '', str(event.get('short_url') or ''))


def load_about_config(path='about.yaml'):
    """The repo-root about.yaml (the build runs from the repo root). Cached; {} when missing."""
    if path in _CONFIG_CACHE:
        return _CONFIG_CACHE[path]
    config = {}
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            config = yaml.load(f, Loader=yaml.FullLoader) or {}
    else:
        print("WARN: %s not found, the About panel will show no topics" % path)
    _CONFIG_CACHE[path] = config
    return config


def _kw_rx(kw):
    # keywords of <=3 chars match whole words only (plus optional plural "s");
    # longer keywords are prefix matches anchored at a word boundary
    kw = str(kw).strip().lower()
    if len(kw) <= 3:
        return re.compile(r'\b' + re.escape(kw) + r's?\b')
    return re.compile(r'\b' + re.escape(kw))


def compiled_categories(key, config):
    """[{name, rules: [(regex, weight)]}] for a series, compiled once."""
    if key in _CATEGORY_CACHE:
        return _CATEGORY_CACHE[key]
    series = (config.get('series') or {}).get(key) or {}
    cats = []
    for cat in series.get('categories') or []:
        rules = []
        for kw in cat.get('keywords') or []:
            # phrases count double
            weight = 2 if ' ' in str(kw).strip() else 1
            rules.append((_kw_rx(kw), weight))
        cats.append({'name': cat.get('name', ''), 'rules': rules})
    if not cats and key not in _WARNED_SERIES:
        _WARNED_SERIES.add(key)
        print("WARN: about.yaml has no categories for series '%s'" % key)
    _CATEGORY_CACHE[key] = cats
    return cats


def _blurb_for(event, key, config):
    series = (config.get('series') or {}).get(key) or {}
    blurb = series.get('blurb') or config.get('default_blurb') or ''
    return (str(blurb)
            .replace('{name}', str(event.get('name') or ''))
            .replace('{year}', str(event.get('year') or ''))
            .strip())


# ── per-event computation ────────────────────────────────────────────────────
def build_about(event, config, today=None):
    """Sets event["about_*"] from event["talks_raw"] (needs talk["short_url"], so call it after
    the talk enrichment loop in events.py)."""
    today = today or datetime.date.today()
    key = series_key(event)
    event['about_series'] = key
    event['about_blurb'] = _blurb_for(event, key, config)

    talks, seen = [], set()
    for t in event.get('talks_raw') or []:
        title = (t.get('Title') or '').strip()
        if title and title.lower() not in seen:
            seen.add(title.lower())
            talks.append(t)
    n = len(talks)
    event['about_talks_count'] = n

    companies, dropped = [], []
    if n >= ABOUT_MIN_TALKS:
        seen_orgs = set()
        for t in talks:
            for col in ('Company1', 'Company2'):
                raw = (t.get(col) or '').strip()
                if not raw:
                    continue
                kept = company_parts(raw)
                for p in (p.strip() for p in _AFFIL_SEP.split(raw)):
                    if p and p not in kept and p not in dropped:
                        dropped.append(p)
                for org in kept:
                    org = normalise_company(org)
                    if not org or is_academic(org):
                        continue
                    low = org.lower()
                    if low in seen_orgs:
                        continue
                    seen_orgs.add(low)
                    companies.append(org)
        companies.sort(key=lambda s: s.lower())
    event['about_companies'] = companies

    topics = []
    cats = compiled_categories(key, config) if n >= ABOUT_MIN_TALKS else []
    if cats:
        buckets = [[] for _ in cats]
        misc = []
        for t in talks:
            hay_title = t['Title'].strip().lower()
            hay_abs = (t.get('Abstract') or '').lower()
            entry = {'title': t['Title'].strip(), 'url': t.get('short_url') or ''}
            best_i, best_score = None, 0
            for ci, cat in enumerate(cats):
                score = 0
                for rx, weight in cat['rules']:
                    # title hit = 3 pts, abstract hit = 1 pt (phrases already weigh double)
                    if rx.search(hay_title):
                        score += 3 * weight
                    elif rx.search(hay_abs):
                        score += weight
                if score > best_score:
                    best_i, best_score = ci, score
            if best_i is None:
                misc.append(entry)
            else:
                buckets[best_i].append(entry)
        topics = [{'category': cat['name'], 'talks': buckets[ci]}
                  for ci, cat in enumerate(cats) if buckets[ci]]
        # most talks first; sort is stable so ties keep the about.yaml order
        topics.sort(key=lambda b: -len(b['talks']))
        if misc:
            topics.append({'category': '...and more', 'talks': misc})
    event['about_topics'] = topics

    # "more talks soon": upcoming events whose lineup is still thin or still has time to grow
    is_past = bool(event.get('is_past'))
    date = event.get('date')
    days_left = (date - today).days if isinstance(date, datetime.date) else 0
    event['about_more_soon'] = (not is_past) and (n < ABOUT_FULL_LINEUP or days_left > ABOUT_QUIET_DAYS)
    event['about_is_past'] = is_past

    if dropped:
        print("About panel %s: dropped job-title companies: %s" % (event.get('short_url'), '; '.join(dropped)))
    misc_n = len(topics[-1]['talks']) if topics and topics[-1]['category'] == '...and more' else 0
    print("About panel %s: talks=%d companies=%d topics=%d misc=%d more_soon=%s" % (
        event.get('short_url'), n, len(companies), len(topics) - (1 if misc_n else 0), misc_n, event['about_more_soon']))
