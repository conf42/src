"""Excels_for_WWW tab -> _db/<TAB>.csv minus the email column (factory/sheetcsv.py), with a fake Drive + git. Offline.
    python factory/tests/test_sheetcsv.py   (from the src repo root)"""
import csv
import io
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from factory import events, sheetcsv  # noqa: E402

REAL = os.path.join(os.path.dirname(__file__), "..", "..", "_db", "MLOPS_2026.csv")


def with_email_column(text, at=3, header=""):
    """What the sheet holds: the repo CSV plus an email column (blank header, like MLOPS_2026 column D)."""
    rows = list(csv.reader(io.StringIO(text, newline="")))
    for n, r in enumerate(rows):
        r.insert(at, header if n == 0 else ("speaker%d@example.com" % n if n % 5 else "a%d@x.org ; b%d@y.org" % (n, n)))
    buf = io.StringIO(newline="")
    csv.writer(buf, lineterminator="\r\n").writerows(rows)      # Drive's CSV: CRLF rows, no final newline
    return buf.getvalue().rstrip("\r\n")


class FakeDrive:
    def __init__(self, text):
        self.text = text

    def _call(self, method, url, **kw):
        class R:
            pass
        r = R()
        if "sheets.googleapis.com" in url:
            r.json = lambda: {"sheets": [{"properties": {"sheetId": 7, "title": "TEST_2027"}}]}
        else:
            assert kw["params"] == {"format": "csv", "gid": 7}
            r.content = self.text.encode("utf-8")
        return r


def main():
    fails = []

    def check(what, ok):
        print("%s  %s" % ("ok  " if ok else "FAIL", what))
        if not ok:
            fails.append(what)

    with open(REAL, encoding="utf-8", newline="") as f:
        real = f.read()
    sheet = with_email_column(real)
    body, dropped = sheetcsv.strip(sheet)
    check("real MLOPS_2026: email column out, the rest byte for byte", body == real)
    check("the blank-header column is the one named", dropped == ["column 4 (no header)"])
    check("a column called Email goes too", sheetcsv.strip(with_email_column(real, 5, "Email1"))[0] == real)
    check("Drive's CRLF row ends kept", "\r\n" in body)
    stray = sheet.replace("Featured", "Featured", 1)
    rows = list(csv.reader(io.StringIO(stray, newline="")))
    rows[2][0] = "someone@example.com"                   # one address in another column: never pushed
    buf = io.StringIO(newline="")
    csv.writer(buf, lineterminator="\r\n").writerows(rows)
    got = sheetcsv.strip(buf.getvalue())[0]
    check("an address typed into another column is taken out", "someone@example.com" not in got)
    bio = sheet.replace("Featured", "Featured", 1)
    rows = list(csv.reader(io.StringIO(bio, newline="")))
    a = rows[0].index("Abstract")
    rows[3][a] += " Chat with me - me@home.net | +44 (0)7887 123456. Uptime 99.9% since 2024."
    buf = io.StringIO(newline="")
    csv.writer(buf, lineterminator="\r\n").writerows(rows)
    got = sheetcsv.strip(buf.getvalue())[0]
    check("a bio's own email + phone are taken out, the rest stays",
          "me@home.net" not in got and "7887" not in got and "99.9% since 2024" in got)
    try:
        sheetcsv.strip("Name1,Title\nAda,Talk")
        check("no YouTube column stops the push", False)
    except ValueError:
        check("no YouTube column stops the push", True)

    # ship(): a throwaway git repo with a bare remote
    root = tempfile.mkdtemp(prefix="sheetcsv-")
    remote, repo = os.path.join(root, "remote.git"), os.path.join(root, "repo")
    run = lambda *a, cwd=root: subprocess.run(list(a), cwd=cwd, capture_output=True, text=True)
    run("git", "init", "-q", "--bare", remote)
    run("git", "clone", "-q", remote, repo)
    os.makedirs(os.path.join(repo, "_db"))
    with open(os.path.join(repo, "_db", "TEST_2027.csv"), "w", encoding="utf-8", newline="") as f:
        f.write(real.replace("https://youtu.be/", "OLD", 1) if "https://youtu.be/" in real else real + "\nx,y")
    for a in (("config", "user.email", "t@t"), ("config", "user.name", "t"), ("add", "-A"), ("commit", "-qm", "init"),
              ("push", "-q", "origin", "HEAD")):
        run("git", *a, cwd=repo)
    git = lambda *a: subprocess.run(["git", "-C", repo] + list(a), capture_output=True, text=True)
    events.REPO = repo
    ev = {"short_url": "test2027", "db_path": os.path.join(repo, "_db", "TEST_2027.csv")}   # absolute, as events.event
    log = list(sheetcsv.ship(ev, FakeDrive(sheet), git))
    with open(os.path.join(repo, "_db", "TEST_2027.csv"), encoding="utf-8", newline="") as f:
        check("ship writes the sheet minus emails", f.read() == real)
    check("ship pushes", "pushed" in " ".join(log) and run("git", "--git-dir", remote, "log", "--oneline").stdout.count("\n") == 2)
    check("no email address reached the repo", "@example.com" not in run("git", "--git-dir", remote, "log", "-p").stdout)
    log = list(sheetcsv.ship(ev, FakeDrive(sheet), git))
    check("same sheet again: nothing to push", "already the same" in " ".join(log))
    log = list(sheetcsv.ship(ev, FakeDrive("\r\n".join(sheet.split("\r\n")[:3])), git))
    check("a tab that lost most rows is not pushed", "not pushed" in " ".join(log))
    os.environ["FACTORY_SHEET_FORCE"] = "test2027"
    log = list(sheetcsv.ship(ev, FakeDrive("\r\n".join(sheet.split("\r\n")[:3])), git))
    os.environ.pop("FACTORY_SHEET_FORCE")
    check("... unless forced for that event (a purge on purpose)", "pushed" in " ".join(log) and "not pushed" not in " ".join(log))
    from factory import events as ev_mod
    t, _ = sheetcsv.strip("Name1,Title,YouTube,Name2\r\nJosé Łukasz Müller,Café talk,,Søren Groß")
    check("accents never reach the website: names in plain letters, other cells untouched",
          t == "Name1,Title,YouTube,Name2\r\nJose Lukasz Muller,Café talk,,Soren Gross")
    check("accents understood: an accented file matches the plain speaker",
          ev_mod._norm("José Łukasz") == ev_mod._norm("Jose Lukasz") == "jose lukasz"
          and ev_mod.match("José Łukasz - Conf42 MLOps 2026.mp4", [{"speakers": "Jose Lukasz", "name1": "Jose Lukasz",
                                                                    "name2": "", "title": "t"}])[0] is not None)
    print("\nALL PASSED" if not fails else "\n%d FAILED" % len(fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
