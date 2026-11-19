"""The event's Excels_for_WWW tab -> its CSV in the repo (_db/MLOPS_2026.csv ...), minus the speakers' email column.

Marek 2026-11-18: "after each talk link is added to the excel spreadsheet, we push the spreadsheet to the CSV folder
with the right name and the speaker email column deleted. Do not touch the email column in excel, just delete between
download and github upload." So: the sheet is only ever read (the same CSV that File > Download > CSV gives), the email
column goes in memory, and the result is committed + pushed like Marek's own "Add files via upload".

The token is the "Conf42 upload" script's own (gdrive.Drive, UPLOAD_FEED), which has the drive scope - no script change.
The email column has no header in the sheet (MLOPS_2026: column D, blank), so it is found by its content: a column
named e-mail/email, or one whose filled cells are mostly email addresses ("a@x.com ; b@y.com" for duo talks).
Any other address or +country phone number in any cell is taken out as well (a speaker's own, typed into a bio or the
LinkedIn field). Never pushes when Name1/Title/YouTube are missing, or when the tab has lost more than half the rows
the repo CSV has (a cleared tab must not wipe the site).
"""
import csv
import io
import os
import re

from . import events

SHEET_ID = "1_-90A9g5_ACqeZl9bQuIHwfox2_-2gGh3cJMNjBrsHs"   # Excels_for_WWW (as in apps-script/conf42-upload.gs)
EMAIL = re.compile(r"[\w.+'-]+@[\w-]+(?:\.[\w-]+)+")
DOX = re.compile(r"(?:mailto:)?[\w.+'-]+@[\w-]+(?:\.[\w-]+)+|(?<![\w/=.#-])\+\d[\d ()./-]{7,}\d")
EMAILS_ONLY = re.compile(r"\s*%s(?:\s*[;,/]\s*%s)*\s*" % (EMAIL.pattern, EMAIL.pattern))


def email_columns(rows):
    """Indexes of the columns to leave out: named e-mail, or mostly email addresses."""
    out = []
    for i, h in enumerate(rows[0]):
        if re.search(r"e-?mail", h, re.I):
            out.append(i)
            continue
        vals = [r[i].strip() for r in rows[1:] if i < len(r) and r[i].strip()]
        if vals and sum(1 for v in vals if EMAILS_ONLY.fullmatch(v)) * 2 >= len(vals):
            out.append(i)
    return out


def strip(text):
    """The downloaded CSV text -> (CSV text without the email column(s), dropped header names). Keeps Drive's own
    line ends and its missing final newline, so a CSV with no change gives the same bytes."""
    rows = list(csv.reader(io.StringIO(text, newline="")))
    if not rows:
        raise ValueError("the tab is empty")
    drop = set(email_columns(rows))
    # nobody gets doxxed, not even by themselves (Marek 2026-11-18): an address or a +country phone number typed into
    # any other cell (LinkedIn field, "contact me at ..." in a bio) is taken out too
    out = [[DOX.sub("", c) for i, c in enumerate(r) if i not in drop] for r in rows]
    for need in ("Name1", "Title", "YouTube"):
        if need not in out[0]:
            raise ValueError("no %s column" % need)
    buf = io.StringIO(newline="")
    csv.writer(buf, lineterminator="\r\n" if "\r\n" in text else "\n").writerows(out)
    body = buf.getvalue()
    if not text.endswith(("\n", "\r")):
        body = body.rstrip("\r\n")
    return body, [rows[0][i] or "column %d (no header)" % (i + 1) for i in sorted(drop)]


# tab -> gid of Excels_for_WWW (2026-11-19). A new event's tab: add it here (Claude: Sheets connector get_spreadsheet,
# fields sheets.properties.sheetId + title) - or enable the Sheets API in the upload script's Google Cloud project.
GIDS = {"CHAOS_2026": 1004923041, "MLOPS_2026": 791783887, "PLATFORM_2026": 1468852268, "PROMPT_2026": 1603890531,
        "FEATUREFLAGS_2026": 269815288, "DEVSECOPS_2026": 199570246, "AGENTS_2026": 735001650, "OBSER_2026": 1211622988,
        "REMIX_2026": 1723955295, "LLM_2026": 1659298365, "DBD_2026": 365454291, "GOLANG_2026": 1494134528,
        "CLOUD_2026": 569684563, "SRE_2026": 31109235, "ML_2026": 760497841, "DEVOPS_2026": 1305191717}


def download(drive, tab):
    """The tab as File > Download > CSV gives it (formulas as their values)."""
    gid = (getattr(drive, "tabs", None) or {}).get(tab)   # the upload script's own list (v9), no Sheets API needed
    if gid is None:
        try:
            meta = drive._call("GET", "https://sheets.googleapis.com/v4/spreadsheets/%s" % SHEET_ID,
                               params={"fields": "sheets.properties(sheetId,title)"}).json()
            gid = next((s["properties"]["sheetId"] for s in meta.get("sheets", []) if s["properties"]["title"] == tab), None)
        except RuntimeError:                             # the token's project has no Sheets API (403, 2026-11-19):
            gid = GIDS.get(tab)                          # the ids read with the Sheets connector, until script v9 is live
    if gid is None:
        raise LookupError("no tab %s in Excels_for_WWW (or not in sheetcsv.GIDS)" % tab)
    r = drive._call("GET", "https://docs.google.com/spreadsheets/d/%s/export" % SHEET_ID,
                    params={"format": "csv", "gid": gid})
    return r.content.decode("utf-8")


def rows_in(text):
    return max(0, len(list(csv.reader(io.StringIO(text, newline="")))) - 1)


def ship(ev, drive=None, git=None):
    """Download the event's tab, leave out the emails, write ev["db_path"], commit + push. Never fails the pass.
    Yields log lines."""
    rel = ev.get("db_path") or ""
    if os.path.isabs(rel):                               # events.event gives it absolute (fixed 2026-11-19: ship
        rel = os.path.relpath(rel, events.REPO)          # had quietly skipped every real event)
    rel = rel.replace("\\", "/")
    while rel.startswith("./"):
        rel = rel[2:]
    tab = os.path.splitext(os.path.basename(rel))[0]
    if not rel.startswith("_db/") or not tab:
        yield "sheet: not shipped - %s is not a _db/ CSV of this repo" % rel
        return
    path = os.path.join(events.REPO, *rel.split("/"))
    try:
        if drive is None:
            from .gdrive import Drive
            drive = Drive()
        body, dropped = strip(download(drive, tab))
        old = ""
        if os.path.exists(path):
            with open(path, encoding="utf-8", newline="") as f:
                old = f.read()
        if body == old:
            yield "sheet: %s.csv already the same as the sheet" % tab
            return
        force = ev.get("short_url") and ev.get("short_url") in os.environ.get("FACTORY_SHEET_FORCE", "").replace(",", " ").split()
        if old and rows_in(body) * 2 < rows_in(old) and not force:    # force: Marek purged the tab on purpose
            yield "sheet: %s.csv not pushed - the tab has %d rows, the repo %d" % (tab, rows_in(body), rows_in(old))
            return
        if git is None:
            from .app import _git
            git = _git()
        git("pull", "--rebase", "--autostash", "-q")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(body)
        git("add", "--", rel)
        if git("diff", "--cached", "--quiet", "--", rel).returncode == 0:
            yield "sheet: %s.csv already the same as the sheet" % tab
            return
        git("commit", "-q", "-m", "factory: %s.csv from Excels_for_WWW (YouTube links; email column left out)" % tab,
            "--", rel)
        for _ in range(3):
            if git("push", "-q").returncode == 0:
                yield "sheet: %s.csv pushed (left out: %s)" % (tab, ", ".join(dropped) or "nothing")
                return
            git("pull", "--rebase", "--autostash", "-q")
        yield "sheet: %s.csv committed, push failed - the next pass pushes it" % tab
    except Exception as e:                               # noqa: BLE001 - the CSV never fails the pass
        yield "sheet: %s.csv not pushed (%s)" % (tab, str(e)[:200])
