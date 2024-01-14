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
        if "Abstract" in item:
            item["Abstract_s"] = textwrap.shorten(item.get("Abstract",""), 200-len(item.get("title","")), placeholder="...")
            item["Abstract_m"] = textwrap.shorten(item.get("Abstract",""), 400-len(item.get("title","")), placeholder="...")
    return items

def make_remote_address(path, name):
    return BASE_STATIC_URL + "/" + path + "/" + quote(name)

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