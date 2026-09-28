"""Everything that differs between machines, in one place, so the factory runs from a plain `git pull` on any
Windows / macOS / Linux computer: where the Desktop really is (OneDrive moves it on Windows), where LibreOffice and
ffmpeg live, where the Descript token is kept, what this machine is called, and the health check (`doctor`).

Per-machine settings go in factory/settings.local.yml (git-ignored), e.g. machine_name, work_root, render_parallel.
The Descript token is never in the repo: an environment variable DESCRIPT_API_TOKEN, or on Windows the user variable
set by setx, or a private file ~/.conf42-factory/descript_token (0600) written by `python -m factory setup`.
"""
import glob
import hashlib
import os
import platform
import shutil
import socket
import subprocess
import sys

TOKEN_FILE = os.path.join(os.path.expanduser("~"), ".conf42-factory", "descript_token")


# ---- places ------------------------------------------------------------------------------------------------------
def desktop():
    """The user's real Desktop folder (on Windows it may live in OneDrive)."""
    if os.name == "nt":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders") as k:
                path = os.path.expandvars(winreg.QueryValueEx(k, "Desktop")[0])
            if os.path.isdir(path):
                return path
        except OSError:
            pass
    elif sys.platform.startswith("linux") and shutil.which("xdg-user-dir"):
        path = subprocess.run(["xdg-user-dir", "DESKTOP"], capture_output=True, text=True).stdout.strip()
        if path and os.path.isdir(path):
            return path
    return os.path.join(os.path.expanduser("~"), "Desktop")


def work_root(cfg):
    """Folder holding one sub-folder per event: settings `work_root` (absolute) or Desktop/<work_folder>."""
    root = cfg.get("work_root")
    return os.path.expanduser(root) if root else os.path.join(desktop(), cfg.get("work_folder") or "talk-factory")


def soffice():
    """LibreOffice's command-line converter, or None."""
    for name in ("soffice", "libreoffice"):
        if shutil.which(name):
            return shutil.which(name)
    for path in (r"C:\Program Files\LibreOffice\program\soffice.exe",
                 r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
                 "/Applications/LibreOffice.app/Contents/MacOS/soffice"):
        if os.path.exists(path):
            return path
    return None


def open_folder(path):
    """Show a folder in Explorer / Finder / the Linux file manager."""
    os.makedirs(path, exist_ok=True)
    if os.name == "nt":
        os.startfile(path)
    else:
        subprocess.Popen(["open" if sys.platform == "darwin" else "xdg-open", path])


def find_tool(name):
    """ffmpeg / ffprobe: PATH, then winget's and Homebrew's usual folders."""
    found = shutil.which(name)
    if found:
        return found
    patterns = [os.path.expanduser(r"~\AppData\Local\Microsoft\WinGet\Packages\*FFmpeg*\*\bin\%s.exe" % name),
                "/opt/homebrew/bin/%s" % name, "/usr/local/bin/%s" % name]
    for pat in patterns:
        hits = glob.glob(pat)
        if hits:
            return hits[0]
    return None


def install_hint(what):
    mac, win = sys.platform == "darwin", os.name == "nt"
    return {"ffmpeg": "winget install Gyan.FFmpeg" if win else "brew install ffmpeg" if mac else "sudo apt install ffmpeg",
            "libreoffice": "winget install TheDocumentFoundation.LibreOffice" if win else
            "brew install --cask libreoffice" if mac else "sudo apt install libreoffice"}.get(what, "")


# ---- who am I ----------------------------------------------------------------------------------------------------
def machine_id():
    """Stable, anonymous id of this computer (the lock and the public status file use it, not the host name)."""
    return hashlib.sha1(socket.gethostname().lower().encode()).hexdigest()[:10]


def machine_name(cfg):
    return str(cfg.get("machine_name") or socket.gethostname())


# ---- the Descript token --------------------------------------------------------------------------------------------
def read_token():
    t = os.environ.get("DESCRIPT_API_TOKEN", "").strip()
    if not t and os.name == "nt":      # a fresh `setx` is not visible to already-open shells: ask the registry
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
                t = str(winreg.QueryValueEx(k, "DESCRIPT_API_TOKEN")[0]).strip()
        except OSError:
            t = ""
    if not t and os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, encoding="utf-8") as f:
            t = f.read().strip()
    return t


def store_token(t):
    """Windows: user environment variable (setx). Elsewhere: a private file only this user can read."""
    t = t.strip()
    if os.name == "nt":
        subprocess.run(["setx", "DESCRIPT_API_TOKEN", t], capture_output=True)
        os.environ["DESCRIPT_API_TOKEN"] = t
        return "Windows user environment variable DESCRIPT_API_TOKEN"
    os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
    with open(TOKEN_FILE, "w", encoding="utf-8") as f:
        f.write(t)
    os.chmod(TOKEN_FILE, 0o600)
    return TOKEN_FILE


# ---- health check -------------------------------------------------------------------------------------------------
def doctor(cfg, repo, check_descript=True):
    """Returns [{name, ok, detail, fix, required}] for the dashboard and `python -m factory doctor`."""
    out = []
    def add(name, ok, detail="", fix="", required=True):
        out.append({"name": name, "ok": bool(ok), "detail": detail, "fix": fix, "required": required})

    add("Python", sys.version_info >= (3, 9), platform.python_version(), "Python 3.9 or newer")
    missing = []
    for mod in ("requests", "yaml", "pypdf", "PIL"):
        try:
            __import__(mod)
        except ImportError:
            missing.append(mod)
    add("Python packages", not missing, "all there" if not missing else "missing: " + ", ".join(missing),
        "pip install -r factory/requirements.txt")
    ff, fp = find_tool("ffmpeg"), find_tool("ffprobe")
    add("ffmpeg / ffprobe", ff and fp, ff or "not found", install_hint("ffmpeg"))
    enc = "CPU (libx264)"
    if ff:
        encs = subprocess.run([ff, "-hide_banner", "-encoders"], capture_output=True, text=True).stdout
        if "h264_nvenc" in encs and shutil.which("nvidia-smi"):
            name = subprocess.run(["nvidia-smi", "--query-gpu=name", "--format=csv,noheader"],
                                  capture_output=True, text=True).stdout.strip()
            enc = "NVIDIA %s (NVENC)" % name.replace("NVIDIA ", "") if name else "NVIDIA (NVENC)"
        elif "h264_videotoolbox" in encs and sys.platform == "darwin":
            enc = "Apple VideoToolbox"
    add("Video encoder", True, enc, required=False)
    so = soffice()
    pptx = so and (os.name != "nt" or os.path.exists(os.path.join(os.path.dirname(so), "ooxlo.dll")))
    add("LibreOffice (PPTX decks only)", pptx,
        so if pptx else ("installed without its PowerPoint import filter (ooxlo.dll) - PPTX decks fail" if so else "not found"),
        ("reinstall the full package: winget uninstall TheDocumentFoundation.LibreOffice, then "
         "winget install TheDocumentFoundation.LibreOffice") if so else install_hint("libreoffice"), required=False)
    root = work_root(cfg)
    try:
        os.makedirs(root, exist_ok=True)
        free = shutil.disk_usage(root).free / 1e9
        add("Work folder", free > 20, "%s (%.0f GB free)" % (root, free), "free some space (a batch needs ~3x its videos)")
    except OSError as ex:
        add("Work folder", False, str(ex), "set work_root in factory/settings.local.yml")
    tok = read_token()
    if not tok:
        add("Descript token", False, "not set", "python -m factory setup")
    elif check_descript:
        try:
            import requests
            r = requests.get("https://descriptapi.com/v1/status", headers={"Authorization": "Bearer " + tok}, timeout=20)
            add("Descript token", r.status_code == 200,
                ("works, drive: %s" % r.json().get("drive_name")) if r.status_code == 200 else "rejected (%s)" % r.status_code,
                "make a new token: Descript > Settings > API tokens, then python -m factory setup")
        except Exception as ex:
            add("Descript token", False, "no answer: %s" % ex, "check the internet connection")
    else:
        add("Descript token", True, "set")
    git = shutil.which("git") or (r"C:\Program Files\Git\cmd\git.exe" if os.name == "nt" else None)
    if git and os.path.isdir(os.path.join(repo, ".git")):
        r = subprocess.run([git, "-C", repo, "push", "--dry-run", "-q"], capture_output=True, text=True, timeout=60)
        add("Git push (status page + machine lock)", r.returncode == 0,
            "can push" if r.returncode == 0 else (r.stderr.strip()[-160:] or "push refused"),
            "sign in to GitHub on this machine (gh auth login) - without it the lock and conf42.com/factory stay local",
            required=False)
    else:
        add("Git push (status page + machine lock)", False, "git not found", "install git", required=False)
    return out
