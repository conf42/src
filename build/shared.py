import textwrap
import csv
import string
import datetime
import re
import os
import string
from urllib.parse import quote, unquote
import requests

BASE_STATIC_URL = "https://conf42.github.io/static"


def read_csv(path):
    """ Read the pre-process the CSV """
    items = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            items.append(dict(item))
    return items

def read_talk_csv(path):
    """ Read the pre-process the CSV """
    items = read_csv(path)
    for item in items:
        # whitespace-only cells (e.g. Company " ") must behave as empty in the templates
        for key, value in list(item.items()):
            if isinstance(value, str):
                item[key] = value.strip()
        if "Abstract" in item:
            item["Abstract_s"] = textwrap.shorten(item.get("Abstract",""), 200-len(item.get("title","")), placeholder="...")
            item["Abstract_m"] = textwrap.shorten(item.get("Abstract",""), 400-len(item.get("title","")), placeholder="...")
            item["Abstract_l"] = textwrap.shorten(item.get("Abstract",""), 700-len(item.get("title","")), placeholder="...")
    return items

def make_remote_address(path, name):
    return BASE_STATIC_URL + "/" + path + "/" + quote(name)

STATIC_REPO_API = "https://api.github.com/repos/conf42/static"


def list_static_slides():
    """ File names in conf42/static's slides/ folder, or None if they can't be listed.

    Two API calls: the default branch's tree, then the slides/ subtree (the
    contents API stops at 1,000 entries). GITHUB_TOKEN, when set, avoids the
    unauthenticated rate limit that CI runners share. """
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = "Bearer " + token
    try:
        root = requests.get(STATIC_REPO_API + "/git/trees/HEAD", headers=headers, timeout=30)
        root.raise_for_status()
        sha = next(e["sha"] for e in root.json()["tree"] if e["path"] == "slides" and e["type"] == "tree")
        tree = requests.get(STATIC_REPO_API + "/git/trees/" + sha, headers=headers, timeout=30)
        tree.raise_for_status()
        return {e["path"] for e in tree.json()["tree"] if e["type"] == "blob"}
    except Exception as e:
        print("Couldn't list conf42/static slides, so only the Slides column is used:", e)
        return None


def conventional_slides_name(event, talk):
    """ The name the factory gives a talk's deck in static/slides:
    `<Name1>[ & <Name2>] - Conf42 <Event> <Year>.pdf` (factory/factory/slides.py). """
    speakers = (talk.get("Name1") or "").strip()
    name2 = (talk.get("Name2") or "").strip()
    if name2:
        speakers += " & " + name2
    return "%s - Conf42 %s %s.pdf" % (speakers, event.get("name"), event.get("year"))


def generate_short_url(event, talk):
    url = "{event}_{year}_{name1}{name2}{keywords}".format(
        event=event.get("name", "").replace(" ", "_"),
        year=event.get("year", "").replace(" ", "_"),
        name1=talk.get("Name1", "").replace(" ", "_"),
        name2=("_" + talk.get("Name2", "").replace(" ", "_")) if talk.get("Name2") else "",
        keywords=("_" + talk.get("Keywords", "").replace(",", "_").replace(" ", "_")) if talk.get("Keywords") else "",
    )
    url = ''.join(filter(lambda x: x in string.printable, url))
    url = re.sub('[\W]+', '', url)
    return url[:100]

def generate_speaker_url(name):
    url = "speaker_{name}".format(
        name=name.replace(" ", "_"),
    )
    url = ''.join(filter(lambda x: x in string.printable, url))
    url = re.sub('[\W]+', '', url)
    return url

def pick_picture_file(base, pic):
    pic_jpeg = pic.replace(".png", ".jpg").replace(".PNG", ".jpg")
    if os.path.isfile(base + pic_jpeg):
        print("Picking jpg: ", base + pic_jpeg)
        return pic_jpeg
    elif not os.path.isfile(base + pic):
        print("Missing picture: %s%s" % (base, pic))
    return pic

def get_canonical_url(page):
    canonical = "https://conf42.com/{}".format(page.replace(".html",""))
    return canonical


WARNINGS = []
def warn_on_missing_file(path, remote=False):
    if remote:
        if not os.environ.get("CHECK_REMOTE"):
            return True
        res = requests.head(path)
        if res.status_code == 404:
            print("Missing remote file: %s (%s)" % (path, unquote(path)))
            WARNINGS.append(unquote(path))
            return False
        return True
    if not os.path.isfile(path):
        print("Missing file: %s" % path)
        return False
    return True

def get_warnings():
    return WARNINGS

# generate times
def start_time(event):
    return datetime.datetime(
        hour=17,
        minute=0,
        year=event.year,
        month=event.month,
        day=event.day,
    )