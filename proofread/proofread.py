#!/usr/bin/env python3
"""Abstract proofreading bookkeeping for the conference sites (SREday, LLMday, PLATFORMday, Conf42).

The Google Sheets are the source of truth: a fix goes into the sheet cell first (the agent does that with
the Google Sheets connector), then this script copies it into the repo CSV (abstract field only, every other
byte kept). The script only READS the sheets (xlsx export; they are link-readable). Rules: PROOFREAD.md.

  scan [--limit N] [EVENT ...]   abstract cells never proofread (hash not in state.json) -> pending.json
  show [EVENT]                   print the pending abstracts for reading (EVENT = e.g. sreday/2026-nyc-q4)
  finish [FIXES.json]            re-read the sheet: record clean cells, refuse rewrites, patch the CSVs
                                 (connector mode, sheets not downloadable: FIXES.json says what was written)
  baseline [EVENT ...]           record pending cells as seen WITHOUT proofreading

In scope: tabs of events that have a CSV in the repo - top-level <year>-<city>-q<n>/_db/talks.csv in the
three site repos (never past/), _db/<EVENT>_<year>.csv from MIN_YEAR on in conf42.
State = proofread/state.json: per brand, sha256[:16] of every abstract text already dealt with. A cell is
only looked at again when its text changes. stdlib only.
"""
import argparse, csv, difflib, hashlib, io, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STATE = os.path.join(HERE, 'state.json')
JOB = os.environ.get('PROOFREAD_JOB', '')      # parallel passes: each job gets its own pending/restore/cache
_J = f'-{JOB}' if JOB else ''
PENDING = os.path.join(HERE, f'pending{_J}.json')
RESTORE = os.path.join(HERE, f'restore{_J}.json')
CACHE = os.path.join(HERE, f'.cache{_J}')
MIN_YEAR = 2026          # Conf42 CSVs older than this are never scanned

BRANDS = {
    'sreday':      {'sheet': '1Qqe_1rvt9H81uNkMrWiHyKord3FYFZTrzw70cscp4Qc', 'dirs': ['website', 'sreday'], 'kind': 'site'},
    'llmday':      {'sheet': '1RQVIKjHm2dVFZ7HJl6BW_z0RzMk_4ofmkQsUV4-Y9H8', 'dirs': ['llmday'], 'kind': 'site'},
    'platformday': {'sheet': '1w1OJKyNjqOYr76-JdCaQrucpAmtf1mseyt57bzqM6Gg', 'dirs': ['platformday'], 'kind': 'site'},
    'conf42':      {'sheet': '1_-90A9g5_ACqeZl9bQuIHwfox2_-2gGh3cJMNjBrsHs', 'dirs': ['conf42', 'src'], 'kind': 'conf42'},
}
CITY = {'nyc': 'NYC', 'san-francisco': 'SF', 'tel-aviv': 'Tel Aviv'}
PLACEHOLDER = re.compile(r'^\W*(tba|tbd|tbc|n/?a|coming soon|to be announced)\W*$', re.I)


def norm(text):
    return (text or '').replace('\r\n', '\n').replace('\r', '\n').strip()


def h(text):
    return hashlib.sha256(norm(text).encode('utf-8')).hexdigest()[:16]


def load_state():
    if os.path.exists(STATE):
        with open(STATE, encoding='utf-8') as f:
            st = json.load(f)
    else:
        st = {'version': 1, 'seen': {}}
    for b in BRANDS:
        st['seen'].setdefault(b, [])
    return st


def save_state(st):
    import fcntl
    with open(STATE + '.lock', 'w') as lock:     # merge with whatever a parallel job saved meanwhile
        fcntl.flock(lock, fcntl.LOCK_EX)
        if os.path.exists(STATE):
            disk = json.load(open(STATE, encoding='utf-8'))
            for b, hs in disk.get('seen', {}).items():
                st['seen'].setdefault(b, []).extend(hs)
        _write_state(st)


def _write_state(st):
    for b in st['seen']:
        st['seen'][b] = sorted(set(st['seen'][b]))
    with open(STATE, 'w', encoding='utf-8') as f:
        json.dump(st, f, indent=0, sort_keys=True)
        f.write('\n')


def repo_dir(root, brand):
    for d in BRANDS[brand]['dirs']:
        p = os.path.join(root, d)
        if os.path.isdir(os.path.join(p, '.git')) or os.path.isdir(p):
            return p
    return None


# ---------------------------------------------------------------- CSV, byte-safe

class Csv:
    """A CSV kept re-writable byte for byte (Google's export: minimal quoting, CRLF, no trailing newline)."""

    def __init__(self, path):
        self.path = path
        raw = open(path, 'rb').read()
        self.raw = raw
        self.bom = raw.startswith(b'\xef\xbb\xbf')
        text = raw.decode('utf-8-sig' if self.bom else 'utf-8')
        first = text.split('\n', 1)[0]
        self.delim = '\t' if first.count('\t') > first.count(',') else ','
        self.lt = '\r\n' if first.endswith('\r') else '\n'
        self.endnl = text.endswith('\n')
        self.rows = list(csv.reader(io.StringIO(text, newline=''), delimiter=self.delim))
        self.header = self.rows[0] if self.rows else []
        low = [c.strip().lower() for c in self.header]

        def col(*names):
            for n in names:
                if n in low:
                    return low.index(n)
            return None
        self.c_abs, self.c_name, self.c_title = col('abstract'), col('name', 'name1'), col('title')
        self.roundtrip = self.dump() == raw

    def dump(self):
        out = io.StringIO(newline='')
        w = csv.writer(out, delimiter=self.delim, lineterminator=self.lt, quoting=csv.QUOTE_MINIMAL)
        w.writerows(self.rows)
        text = out.getvalue()
        if not self.endnl and text.endswith(self.lt):
            text = text[:-len(self.lt)]
        return (b'\xef\xbb\xbf' if self.bom else b'') + text.encode('utf-8')

    def get(self, row, c):
        return row[c] if c is not None and c < len(row) else ''

    def save(self):
        with open(self.path, 'wb') as f:
            f.write(self.dump())


def event_files(root):
    """-> [(brand, event key, tab hint, csv path)] for everything in scope."""
    out = []
    for brand, cfg in BRANDS.items():
        repo = repo_dir(root, brand)
        if not repo:
            print(f'! repo for {brand} not found under {root} (tried {cfg["dirs"]})', file=sys.stderr)
            continue
        if cfg['kind'] == 'site':
            for d in sorted(os.listdir(repo)):                      # top-level events only: past/ is left alone
                m = re.match(r'^(20\d\d)-(.+)-q(\d)$', d)
                p = os.path.join(repo, d, '_db', 'talks.csv')
                if m and os.path.isfile(p):
                    city = CITY.get(m.group(2), m.group(2).replace('-', ' ').title())
                    out.append((brand, f'{brand}/{d}', f'{city} {m.group(1)} Q{m.group(3)}', p))
        else:
            db = os.path.join(repo, '_db')
            for f in sorted(os.listdir(db)):
                m = re.match(r'^([A-Z][A-Z_]*)_(20\d\d)\.csv$', f)
                if m and int(m.group(2)) >= MIN_YEAR:
                    out.append((brand, f'conf42/{f[:-4]}', f[:-4], os.path.join(db, f)))
    return out


class SheetUnreachable(Exception):
    pass


def fetch_xlsx(brand, fresh=False):
    """The brand's whole sheet as an xlsx export (the sheets are link-readable, so no login)."""
    import time, urllib.request
    os.makedirs(CACHE, exist_ok=True)
    dest = os.path.join(CACHE, f'{brand}.xlsx')
    if os.path.exists(dest) and not fresh:
        return dest
    url = f'https://docs.google.com/spreadsheets/d/{BRANDS[brand]["sheet"]}/export?format=xlsx'
    last = None
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (proofread)'})
            data = urllib.request.urlopen(req, timeout=60).read()
            if data[:2] != b'PK':
                raise RuntimeError('not an xlsx (the sheet is no longer link-readable?)')
            with open(dest, 'wb') as f:
                f.write(data)
            return dest
        except Exception as ex:          # noqa
            last = ex
            time.sleep(5 * (attempt + 1))
    raise SheetUnreachable(f'cannot download the {brand} sheet: {last}')


def scan(root, st, fresh=True, only=None):
    """Pending = abstract cells of the in-scope tabs (events that have a CSV in the repo) never proofread."""
    pending, tabs_of = [], {}
    for brand, key, hint, path in event_files(root):
        if only and key not in only:
            continue
        if brand not in tabs_of:
            tabs_of[brand] = xlsx_tabs(fetch_xlsx(brand, fresh))
        tab, rows, letter = sheet_rows(tabs_of[brand], hint)
        if not tab or not letter:
            print(f'! {key}: no tab like "{hint}" (or no abstract column) in the sheet - skipped', file=sys.stderr)
            continue
        seen = set(st['seen'][brand])
        for n, name, title, a in rows:
            if not norm(a) or PLACEHOLDER.match(norm(a)) or h(a) in seen:
                continue
            pending.append({'id': f'{key}#{letter}{n}', 'brand': brand, 'event': key, 'sheet_id': BRANDS[brand]['sheet'],
                            'tab': tab, 'cell': f'{letter}{n}', 'range': f"'{tab}'!{letter}{n}",
                            'csv': os.path.relpath(path, root), 'name': name, 'title': title, 'abstract': a})
    return pending


def scan_csv(root, st, only=None):
    """Connector mode (the sheets cannot be downloaded from here): pending = CSV abstracts never proofread.
    The agent finds the cells and reads the sheet text with the Google Sheets connector."""
    pending = []
    for brand, key, hint, path in event_files(root):
        if only and key not in only:
            continue
        c = Csv(path)
        if c.c_abs is None:
            continue
        seen, got = set(st['seen'][brand]), set()
        for row in c.rows[1:]:
            a = c.get(row, c.c_abs)
            if not norm(a) or PLACEHOLDER.match(norm(a)) or h(a) in seen or h(a) in got:
                continue
            got.add(h(a))
            pending.append({'id': f'{key}#{h(a)}', 'mode': 'csv', 'brand': brand, 'event': key,
                            'sheet_id': BRANDS[brand]['sheet'], 'tab': hint, 'csv': os.path.relpath(path, root),
                            'name': c.get(row, c.c_name), 'title': c.get(row, c.c_title), 'abstract': a})
    return pending


def cmd_scan(args):
    try:
        pending = scan(args.root, load_state(), only=args.events)
    except SheetUnreachable as ex:
        print(f'CONNECTOR MODE: {ex}. Follow "Connector mode" in PROOFREAD.md.')
        pending = scan_csv(args.root, load_state(), only=args.events)
    total = len(pending)
    if args.limit and total > args.limit:                # whole events, oldest tab order, until the cap
        keep, n = [], 0
        for ev in dict.fromkeys(p['event'] for p in pending):
            items = [p for p in pending if p['event'] == ev]
            if keep and n + len(items) > args.limit:
                break
            keep += items[:args.limit]
            n = len(keep)
        pending = keep
    with open(PENDING, 'w', encoding='utf-8') as f:
        json.dump(pending, f, indent=1, ensure_ascii=False)
    by = {}
    for p in pending:
        by.setdefault((p['event'], p['tab'], p['sheet_id']), []).append(p)
    print(f'{total} abstract(s) never proofread; {len(pending)} in this batch -> {PENDING}')
    for (ev, tab, sid), ps in by.items():
        print(f'  {len(ps):3d}  {ev}   tab "{tab}"   spreadsheet {sid}')


def cmd_show(args):
    pending = json.load(open(PENDING, encoding='utf-8'))
    for p in pending:
        if args.event and p['event'] != args.event:
            continue
        print(f'=== {p.get("range") or p["id"]} | {p["name"]} | {p["title"]}')
        print(p['abstract'])
        print()


# ---------------------------------------------------------------- guard: a proofread is not a rewrite

def words(t):
    return re.findall(r"[^\W_]+", norm(t).lower())


def guard(orig, new):
    """None if `new` is a plausible proofread of `orig`, else the reason it is refused."""
    a, b = words(orig), words(new)
    if not b:
        return 'empty result'
    if not (0.85 <= len(b) / max(1, len(a)) <= 1.15):
        return f'word count {len(a)} -> {len(b)}'
    r = difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
    if r < 0.8:
        return f'only {r:.0%} of the words kept'
    return None


def finish_csv(args, pending):
    """Connector mode: the agent says what it wrote (fixes file), the script guards it and patches the CSVs."""
    if not args.fixes:
        raise SystemExit('connector mode: finish needs the fixes file (see "Connector mode" in PROOFREAD.md)')
    st = load_state()
    fixes = json.load(open(args.fixes, encoding='utf-8'))
    byid = {p['id']: p for p in pending}
    files, log, restore = {}, [], []
    for fx in fixes:
        p = byid.get(fx.get('id'))
        if not p:
            log.append(f'?  {fx.get("id")}: not in this batch - ignored')
            continue
        who = f'{p["event"]} {fx.get("cell", "")} | {p["name"]}'
        seen = st['seen'][p['brand']]
        old, new, so = p['abstract'], fx.get('corrected'), fx.get('sheet_original')
        if fx.get('missing'):
            seen.append(h(old))
            log.append(f'-  {who}: not in the sheet, recorded untouched')
            continue
        if new is None or norm(new) == norm(so if so is not None else old):
            seen.append(h(old))
            if so is None or norm(so) == norm(old):
                log.append(f'=  {who}: clean')
                continue
            seen.append(h(so))
            if guard(old, so):       # the sheet text is a different abstract, not a proofread of the CSV one
                log.append(f'=  {who}: clean (sheet differs from the CSV; CSV left for the next export)')
                continue
            new = so                 # proofread in the sheet on an earlier run whose push was lost: catch up
        base = so if so is not None else old
        why = guard(base, new)
        if why:
            restore.append({'spreadsheet': p['sheet_id'], 'tab': p['tab'], 'cell': fx.get('cell'), 'value': base, 'why': why})
            log.append(f'X  {who}: REFUSED ({why}) - restore the cell from the restore file')
            continue
        seen += [h(old), h(new)] + ([h(so)] if so is not None else [])
        if so is not None and norm(so) != norm(old) and guard(old, new):
            # the sheet was really edited since the export (not just proofread earlier): the export brings it
            log.append(f'~  {who}: fixed in the sheet; the CSV holds an older text, left for the next export')
            continue
        path = os.path.join(args.root, p['csv'])
        c = files.get(path) or Csv(path)
        files[path] = c
        if not c.roundtrip:
            log.append(f'~  {who}: fixed in the sheet; {p["csv"]} cannot be rewritten byte-safely, left for the next export')
            continue
        for r in c.rows[1:]:
            if norm(c.get(r, c.c_abs)) == norm(old):
                r[c.c_abs] = norm(new)
        c.changed = True
        log.append(f'+  {who}: fixed')
    for path, c in files.items():
        if getattr(c, 'changed', False):
            c.save()
    save_state(st)
    json.dump(restore, open(RESTORE, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('\n'.join(log))
    count = lambda k: sum(l[0] == k for l in log)
    left = len(pending) - len({fx.get('id') for fx in fixes} & set(byid))
    print(f'\nSUMMARY: {count("+")} fixed (sheet + CSV), {count("~")} fixed in the sheet only, {count("=")} clean, '
          f'{count("X")} refused, {left} not reported (stay pending)')
    if restore:
        print(f'{len(restore)} cell(s) to restore: see {RESTORE}')


def cmd_finish(args):
    """After the agent edited cells in the sheet: re-read the sheet, keep the good fixes, patch the CSVs."""
    pending = json.load(open(PENDING, encoding='utf-8'))
    if pending and pending[0].get('mode') == 'csv':
        return finish_csv(args, pending)
    st = load_state()
    tabs_of, files, log, restore = {}, {}, [], []
    for p in pending:
        brand = p['brand']
        if brand not in tabs_of:
            tabs_of[brand] = xlsx_tabs(fetch_xlsx(brand, fresh=True))
        _, rows, letter = sheet_rows(tabs_of[brand], p['tab'])
        now = {f'{letter}{n}': (name, a) for n, name, _, a in rows}.get(p['cell'])
        who = f'{p["event"]} {p["cell"]} | {p["name"]}'
        if not now or norm(now[0]) != norm(p['name']):
            log.append(f'?  {who}: the row moved or went away meanwhile - left for the next run')
            continue
        old, new = p['abstract'], now[1]
        seen = st['seen'][brand]
        if norm(new) == norm(old):
            seen.append(h(old))
            log.append(f'=  {who}: clean')
            continue
        why = guard(old, new)
        if why:
            restore.append({'spreadsheet': p['sheet_id'], 'range': p['range'], 'value': old, 'why': why})
            log.append(f'X  {who}: REFUSED ({why}) - restore the cell from the restore file')
            continue
        seen += [h(old), h(new)]
        path = os.path.join(args.root, p['csv'])
        c = files.get(path) or Csv(path)
        files[path] = c
        hit = [r for r in c.rows[1:] if c.c_abs is not None and norm(c.get(r, c.c_abs)) == norm(old)]
        if not hit:
            log.append(f'~  {who}: fixed in the sheet; the CSV has no row with that text, left for the next export')
        elif not c.roundtrip:
            log.append(f'~  {who}: fixed in the sheet; {p["csv"]} cannot be rewritten byte-safely, left for the next export')
        else:
            for r in hit:
                r[c.c_abs] = norm(new)
            c.changed = True
            log.append(f'+  {who}: fixed')
    for path, c in files.items():
        if getattr(c, 'changed', False):
            c.save()
    save_state(st)
    json.dump(restore, open(RESTORE, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('\n'.join(log))
    count = lambda k: sum(l[0] == k for l in log)
    print(f'\nSUMMARY: {count("+")} fixed (sheet + CSV), {count("~")} fixed in the sheet only, {count("=")} clean, '
          f'{count("X")} refused, {count("?")} postponed')
    if restore:
        print(f'{len(restore)} cell(s) to restore: see {RESTORE}, then run finish again')


def cmd_baseline(args):
    st = load_state()
    n = 0
    for p in scan(args.root, st, only=args.events or None):
        st['seen'][p['brand']].append(h(p['abstract']))
        n += 1
    save_state(st)
    print(f'{n} abstract(s) recorded as seen without proofreading')


# ---------------------------------------------------------------- local helper: xlsx export of a sheet

def xlsx_tabs(path):
    """{tab title: rows of strings} from an xlsx export (stdlib; keeps in-cell CR/LF, decodes _xHHHH_)."""
    import zipfile
    import xml.etree.ElementTree as ET
    ns = {'m': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
    rel = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
    z = zipfile.ZipFile(path)

    def parse(name):
        data = z.read(name).decode('utf-8')
        head, _, body = data.partition('?>')
        return ET.fromstring((head + '?>' + body.lstrip().replace('\r', '&#13;')).encode('utf-8'))

    def unesc(s):
        return re.sub(r'_x([0-9A-Fa-f]{4})_', lambda m: chr(int(m.group(1), 16)), s)

    def si_text(si):
        return unesc(''.join(t.text or '' for t in si.iter('{%s}t' % ns['m'])))
    shared = [si_text(si) for si in parse('xl/sharedStrings.xml').findall('m:si', ns)] if 'xl/sharedStrings.xml' in z.namelist() else []
    rels = {r.get('Id'): r.get('Target') for r in parse('xl/_rels/workbook.xml.rels')}
    tabs = {}
    for s in parse('xl/workbook.xml').find('m:sheets', ns):
        target = rels[s.get(rel)]
        root = parse('xl/' + target.lstrip('/').replace('xl/', '', 1))
        rows = []
        for r in root.iter('{%s}row' % ns['m']):
            row = {}
            for c in r.findall('m:c', ns):
                ref = re.match(r'[A-Z]+', c.get('r')).group(0)
                idx = 0
                for ch in ref:
                    idx = idx * 26 + ord(ch) - 64
                t, v = c.get('t'), c.find('m:v', ns)
                if t == 's' and v is not None:
                    val = shared[int(v.text)]
                elif t == 'inlineStr':
                    val = si_text(c.find('m:is', ns))
                else:
                    val = unesc(v.text) if v is not None and v.text else ''
                row[idx - 1] = val
            n = int(r.get('r'))
            while len(rows) < n:
                rows.append([])
            rows[n - 1] = [row.get(i, '') for i in range(max(row) + 1)] if row else []
        tabs[s.get('name')] = rows
    return tabs


def find_tab(tabs, hint):
    k = lambda s: re.sub(r'[^a-z0-9]', '', s.lower().replace('san francisco', 'sf'))
    for name in tabs:
        if k(name) == k(hint):
            return name
    return None


def sheet_rows(tabs, hint):
    """-> (tab, [(row number, name, title, abstract)], abstract column letter) by header names."""
    tab = find_tab(tabs, hint)
    if not tab or not tabs[tab]:
        return None, [], None
    head = [c.strip().lower() for c in tabs[tab][0]]

    def col(*names):
        for n in names:
            if n in head:
                return head.index(n)
    ca, cn, ct = col('abstract'), col('name', 'name1'), col('title')
    g = lambda r, c: r[c] if c is not None and c < len(r) else ''
    letter = ''
    n = ca + 1
    while n:
        n, rem = divmod(n - 1, 26)
        letter = chr(65 + rem) + letter
    return tab, [(i, g(r, cn), g(r, ct), g(r, ca)) for i, r in enumerate(tabs[tab][1:], start=2)], letter


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--root', default=os.path.dirname(os.path.dirname(HERE)),
                    help='folder holding the repo checkouts side by side (default: next to this repo)')
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('scan'); s.add_argument('--limit', type=int, default=0); s.add_argument('events', nargs='*'); s.set_defaults(fn=cmd_scan)
    s = sub.add_parser('show'); s.add_argument('event', nargs='?'); s.set_defaults(fn=cmd_show)
    s = sub.add_parser('finish'); s.add_argument('fixes', nargs='?'); s.set_defaults(fn=cmd_finish)
    s = sub.add_parser('baseline'); s.add_argument('events', nargs='*'); s.set_defaults(fn=cmd_baseline)
    args = ap.parse_args()
    args.fn(args)


if __name__ == '__main__':
    main()
