"""Slide decks: one PDF per talk, named as the site expects, every one under the size limit.

For each deck in Desktop/<work_folder>/<short_url>/slides/ (unzipped from the Drive download):
  1. match it to its talk (same speaker matching as the videos; never guessed),
  2. keep ONE deck per talk: a PDF beats a PPTX/KEY/ODP, identical duplicates are dropped,
  3. convert anything that isn't a PDF with LibreOffice,
  4. rename to `<Name1>[ & <Name2>] - Conf42 <Event> <Year>.pdf` (the CSV Slides column / static/slides name),
  5. compress every PDF over `slides_max_mb` by re-encoding its images (pypdf + Pillow), page count checked.
Originals of converted / compressed / duplicate files move to "slides originals" next to the folder.
"""
import glob
import hashlib
import io
import logging
import os
import shutil
import subprocess

from . import events

SLIDE_EXT = (".pdf", ".pptx", ".ppt", ".key", ".odp")
logging.getLogger("pypdf").setLevel(logging.ERROR)     # "Ignoring wrong pointing object" noise
STEPS = ((75, 1800), (65, 1600), (55, 1400), (45, 1200), (35, 1000))


def _md5(path):
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()


def _done_name(name, title):
    return (" - %s." % title) in name


def convert(src, out_dir):
    """PPTX/KEY/ODP -> PDF with the first converter this machine has that works: LibreOffice (own throw-away
    profile, so an open LibreOffice window or a locked profile cannot break it), Microsoft PowerPoint (Windows),
    Keynote (macOS). Returns (pdf path, converter name)."""
    from . import machine
    pdf = os.path.join(out_dir, os.path.splitext(os.path.basename(src))[0] + ".pdf")
    errors = []
    for name, fn in machine.pptx_converters():
        try:
            if os.path.exists(pdf):
                os.remove(pdf)
            fn(os.path.abspath(src), os.path.abspath(pdf))
            if os.path.exists(pdf) and os.path.getsize(pdf) > 0:
                return pdf, name
            errors.append("%s: no PDF came out" % name)
        except Exception as ex:
            errors.append("%s: %s" % (name, str(ex)[-160:]))
    raise RuntimeError("could not convert %s to PDF (%s)" % (os.path.basename(src), "; ".join(errors) or
                       "no converter on this machine - install LibreOffice"))


def _shrink(path, quality, max_px):
    from pypdf import PdfReader, PdfWriter
    from PIL import Image
    reader = PdfReader(path)
    writer = PdfWriter(clone_from=reader)
    for page in writer.pages:
        for img in page.images:
            try:
                im = img.image
            except Exception:
                continue
            w, h = im.size
            if max(w, h) > max_px:
                s = max_px / max(w, h)
                im = im.resize((int(w * s), int(h * s)), Image.LANCZOS)
            if im.mode in ("RGBA", "LA", "P"):
                im = im.convert("RGB")
            try:
                img.replace(im, quality=quality)
            except Exception:
                pass
        try:
            page.compress_content_streams()
        except Exception:
            pass
    writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    buf = io.BytesIO()
    writer.write(buf)
    return buf.getvalue()


def compress(path, limit_bytes, originals):
    """Returns (before_mb, after_mb) or None when the file was already small enough."""
    from pypdf import PdfReader
    size = os.path.getsize(path)
    if size <= limit_bytes:
        return None
    best = None
    for q, px in STEPS:
        best = _shrink(path, q, px)
        if len(best) <= limit_bytes:
            break
    if not best or len(best) >= size:
        return (size / 1e6, size / 1e6)
    pages_old = len(PdfReader(path).pages)
    os.makedirs(originals, exist_ok=True)
    shutil.move(path, os.path.join(originals, os.path.basename(path)))
    with open(path, "wb") as f:
        f.write(best)
    if len(PdfReader(path).pages) != pages_old:                 # never ship a deck that lost pages
        shutil.move(os.path.join(originals, os.path.basename(path)), path)
        raise RuntimeError("compressing %s changed the page count - kept the original" % os.path.basename(path))
    return (size / 1e6, len(best) / 1e6)


def prepare(slides_dir, ev, talk_list, max_mb=5):
    """Process every deck in slides_dir; returns a report dict for state.json / the chat."""
    originals = slides_dir + " originals"
    report = {"decks": {}, "unmatched": [], "dropped": [], "converted": [], "compressed": [], "errors": []}
    candidates = {}
    for path in sorted(glob.glob(os.path.join(slides_dir, "*"))):
        name = os.path.basename(path)
        if not name.lower().endswith(SLIDE_EXT):
            continue
        if _done_name(name, ev["title"]):                        # already processed on an earlier run
            report["decks"][name.split(" - Conf42")[0]] = name
            continue
        stem = os.path.splitext(name)[0].replace("(1)", "").replace("(2)", "")
        t, why = events.match(stem, talk_list)
        if not t:
            report["unmatched"].append({"file": name, "why": why})
            continue
        candidates.setdefault(t["speakers"], []).append(path)
    for speakers, paths in candidates.items():
        if speakers in report["decks"]:                          # a finished deck exists: park the new ones
            keep = None
        else:
            pdfs = [p for p in paths if p.lower().endswith(".pdf")]
            keep = max(pdfs, key=os.path.getmtime) if pdfs else max(paths, key=os.path.getmtime)
        for p in paths:
            if p != keep:
                os.makedirs(originals, exist_ok=True)
                shutil.move(p, os.path.join(originals, os.path.basename(p)))
                report["dropped"].append(os.path.basename(p))
        if not keep:
            continue
        try:
            if not keep.lower().endswith(".pdf"):
                pdf, how = convert(keep, slides_dir)
                os.makedirs(originals, exist_ok=True)
                shutil.move(keep, os.path.join(originals, os.path.basename(keep)))
                report["converted"].append(os.path.basename(keep))
                keep = pdf
            target = os.path.join(slides_dir, "%s - %s.pdf" % (speakers, ev["title"]))
            os.replace(keep, target)
            c = compress(target, max_mb * 1024 * 1024, originals)
            if c:
                report["compressed"].append("%s %.1f -> %.1f MB" % (os.path.basename(target), c[0], c[1]))
            report["decks"][speakers] = os.path.basename(target)
        except Exception as ex:
            report["errors"].append("%s: %s" % (speakers, ex))
    # decks that were processed on an earlier run but are still over the limit (e.g. settings changed)
    for speakers, name in report["decks"].items():
        path = os.path.join(slides_dir, name)
        if os.path.exists(path) and os.path.getsize(path) > max_mb * 1024 * 1024:
            try:
                c = compress(path, max_mb * 1024 * 1024, originals)
                if c:
                    report["compressed"].append("%s %.1f -> %.1f MB" % (name, c[0], c[1]))
            except Exception as ex:
                report["errors"].append("%s: %s" % (speakers, ex))
    report["missing"] = [t["speakers"] for t in talk_list if t["speakers"] not in report["decks"]]
    return report
