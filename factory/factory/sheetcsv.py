"""The event's Excels_for_WWW tab -> its CSV in the repo (_db/MLOPS_2026.csv ...), minus the speakers' email column.

Marek 2026-11-18: "after each talk link is added to the excel spreadsheet, we push the spreadsheet to the CSV folder
with the right name and the speaker email column deleted. Do not touch the email column in excel, just delete between
download and github upload." So: the sheet is only ever read (the same CSV that File > Download > CSV gives), the email
column goes in memory, and the result is committed + pushed like Marek's own "Add files via upload".

The token is the "Conf42 upload" script's own (gdrive.Drive, UPLOAD_FEED), which has the drive scope - no script change.
The email column has no header in the sheet (MLOPS_2026: column D, blank), so it is found by its content: a column
named e-mail/email, or one whose filled cells are mostly email addresses ("a@x.com ; b@y.com" for duo talks).
Never pushes when an email address would still be in a cell of its own, when Name1/Title/YouTube are missing, or when
the tab has lost more than half the rows the repo CSV has (a cleared tab must not wipe the site).
"""
import csv
import io
import os
import re

from . import events

SHEET_ID = "1_-90A9g5_ACqeZl9bQuIHwfox2_-2gGh3cJMNjBrsHs"   # Excels_for_WWW (as in apps-script/conf42-upload.gs)
EMAIL = re.compile(r"[\w.+'-]+@[\w-]+(?:\.[\w-]+)+")
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
    out = [[c for i, c in enumerate(r) if i not in drop] for r in rows]
    left = sorted({c.strip() for r in out for c in r if EMAILS_ONLY.fullmatch(c)})
    if left:
        raise ValueError("%d email address(es) still in other columns - not pushed" % len(left))
    for need in ("Name1", "Title", "YouTube"):
        if need not in out[0]:
            raise ValueError("no %s column" % need)
    buf = io.StringIO(newline="")
    csv.writer(buf, lineterminator="\r\n" if "\r\n" in text else "\n").writerows(out)
    body = buf.getvalue()
    if not text.endswith(("\n", "\r")):
        body = body.rstrip("\r\n")
    return body, [rows[0][i] or "column %d (no header)" % (i + 1) for i in sorted(drop)]


def download(drive, tab):
    """The tab as File > Download > CSV gives it (formulas as their values)."""
    meta = drive._call("GET", "https://sheets.googleapis.com/v4/spreadsheets/%s" % SHEET_ID,
                       params={"fields": "sheets.properties(sheetId,title)"}).json()
    gid = next((s["properties"]["sheetId"] for s in meta.get("sheets", []) if s["properties"]["title"] == tab), None)
    if gid is None:
        raise LookupError("no tab %s in Excels_for_WWW" % tab)
    r = drive._call("GET", "https://docs.google.com/spreadsheets/d/%s/export" % SHEET_ID,
                    params={"format": "csv", "gid": gid})
    return r.content.decode("utf-8")


def rows_in(text):
    return max(0, len(list(csv.reader(io.StringIO(text, newline="")))) - 1)


def ship(ev, drive=None, git=None):
    """Download the event's tab, leave out the emails, write ev["db_path"], commit + push. Never fails the pass.
    Yields log lines."""
    rel = (ev.get("db_path") or "").lstrip("./").replace("\\", "/")
    tab = os.path.splitext(os.path.basename(rel))[0]
    if not rel.startswith("_db/") or not tab:
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
        if old and rows_in(body) * 2 < rows_in(old):
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
