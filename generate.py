#!/usr/bin/env python3

import datetime
import pprint
import csv
import textwrap
import re
import os
import string
import sys
import urllib.parse
import markdown
import requests

import yaml
from jinja2 import Environment, FileSystemLoader
from jinja_markdown import MarkdownExtension
import dateutil.parser
from ics import Calendar, Event
from urllib.parse import quote, unquote

DIVIDER = "#"*80
BASE_FOLDER = "./docs"
BASE_STATIC_URL = "https://conf42.github.io/static"

def make_remote_address(path, name):
    return BASE_STATIC_URL + "/" + path + "/" + quote(name)

def read_csv(path):
    """ Read the pre-process the CSV """
    items = []
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            item = dict(item)
            if "Abstract" in item:
                item["Abstract_s"] = textwrap.shorten(item.get("Abstract",""), 200-len(item.get("title","")), placeholder="...")
                item["Abstract_m"] = textwrap.shorten(item.get("Abstract",""), 400-len(item.get("title","")), placeholder="...")
            items.append(item)
    return items

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

def pick_picture_file(base, pic):
    pic_jpeg = pic.replace(".png", ".jpg").replace(".PNG", ".jpg")
    if os.path.isfile(base + pic_jpeg):
        print("Picking jpg: ", base + pic_jpeg)
        return pic_jpeg
    elif not os.path.isfile(base + pic):
        print("Missing picture: %s%s" % (base, pic))
    return pic

WARNINGS = []
def warn_on_missing_file(path, remote=False):
    if remote:
        if not os.environ.get("CHECK_REMOTE"):
            return True
        res = requests.head(path)
        print(path, res.elapsed, len(res.text))
        if res.status_code == 404:
            print("Missing remote file: %s (%s)" % (path, unquote(path)))
            WARNINGS.append(path)
            return False
        return True
    if not os.path.isfile(path):
        print("Missing file: %s" % path)
        return False
    return True

# init the jinja stuff
file_loader = FileSystemLoader("_templates")
env = Environment(loader=file_loader)
env.add_extension(MarkdownExtension)
def format_sponsors(value, items):
    if items is not None and len(items) == 1:
        # print("format_sponsors", value, items, "SINGLES")
        return value.replace("sponsors", "sponsor").replace("partners", "partner")
    return value
env.filters["format_sponsors"] = format_sponsors
env.filters["markdown"] = lambda x: markdown.markdown(x)

# load the context from the metadata file
context = dict()
with open('metadata.yml') as f:
    context = yaml.load(f, Loader=yaml.FullLoader)
# store urls for the sitemap.xml
urls = []

# EVENTS METADATA
print(DIVIDER)
print("Loading events metadata")

events = context.get("events")
events.sort(key=lambda e: e.get("date"))
print("Loaded %s events" % len(events))
for event in events:
    event["short_url"] = event.get("short_url")

# Validate sponsorship levels
sponsorship_levels = [
    v.get("id") for v in context.get("sponsorships")
]
context["sponsorship_levels"] = sponsorship_levels
print(DIVIDER)
print("Sponsorship levels:", sponsorship_levels)
for event in events:
    for level in event.get("sponsors", dict()).keys():
        if level not in sponsorship_levels:
            print("Event %s has invalid sponsorship level: %s" % (event.get("name"), level))
            sys.exit(1)

future_events = []
past_events = []
years = dict()
featured_sponsors = set()
for event in events:
    # sort sponsors
    for sponsor_type in event.get("sponsors", {}).keys():
        event["sponsors"][sponsor_type].sort()
        if sponsor_type in ["platinum", "diamond"]:
            for sponsor in event["sponsors"][sponsor_type]:
                featured_sponsors.add(sponsor)
    # divide into past and future events
    if datetime.date.today() >= event.get("date"):
        event["cfp_closed"] = True
        past_events.append(event)
        current_event = event
    else:
        future_events.append(event)
    # bucket by year
    year = str(event.get("date").year)
    event["year"] = year
    if year not in years:
        years[year] = []
    years[year].append(event)
    # mark as revealed or not
    event["reveal_videos"] = False
    vrd = event.get("videos_reveal_date")
    if vrd is not None and datetime.date.today() >= vrd:
        event["reveal_videos"] = True
context["years"] = years
context["future_events"] = future_events
context["current_event"] = past_events[-1]
context["past_events"] = past_events[:-1]
context["past_events"].sort(key=lambda e: e.get("date"), reverse=True)
context["featured_sponsors"] = sorted(list(featured_sponsors))

# SPONSORS
print(DIVIDER)
print("Reading sponsor metadata")

try:
    sponsors_list = sorted(read_csv("./_db/sponsors.csv"), key=lambda x: x.get("id"))
    context["sponsors"] = sponsors_list
    context["sponsors_by_id"] = {
        item.get("id"): item for item in sponsors_list
    }
    print("Loaded %d sponsors metadata" % len(context["sponsors"]))
except Exception as e:
    print("Couldn't read sponsors", e)

try:
    sponsor_subpages = sorted(read_csv("./_db/subpages.csv"), key=lambda x: x.get("Sponsor"))
    for subpage in sponsor_subpages:
        subpage["YouTubeId"] = subpage.get("YouTube").split("/")[-1]
    context["sponsor_subpages"] = sponsor_subpages
    context["sponsor_subpages_by_id"] = {
        item.get("Sponsor"): item for item in sponsor_subpages
    }
    print("Loaded %d sponsor subpages" % len(context["sponsor_subpages"]))
except Exception as e:
    print("Couldn't read sponsors", e)

print(DIVIDER)
print("Generating sponsor subpages")
for subpage in context["sponsor_subpages"]:
    with open(BASE_FOLDER + "/" + subpage.get("Sponsor")  + ".html", "w") as f:
        template = env.get_template("sponsor_subpage.html")
        f.write(template.render(sponsor=subpage, secret_mode=True, **context))

# pprint.pprint(context)

# EVENT PAGES
print(DIVIDER)
print("Generating event pages")

for event in events:

    # for external URLs, just use that as url
    if "external_url" in event:
        event["url"] = event["external_url"]
        continue
    event["url"] = context.get("base_path") + event["short_url"]


    # attempt to read the talks CSV
    try:
        talks = read_csv(event.get("db_path"))
    except:
        talks = []
    #talks.sort(key=lambda x: x.get("Title"))

    print("%s %s /%s (%d talks)" % (event.get("date"), event.get("name"), event.get("short_url"), len(talks)))

    # check and pick the picture
    event["thumbnail_path"] = pick_picture_file(BASE_FOLDER + "/", event["thumbnail_path"])

    # split into featured and not
    event["talks_featured"] = [talk for talk in talks if talk.get("Featured","").lower() == "yes"]
    event["talks_panel"] = [talk for talk in talks if talk.get("Panel","").lower() == "yes"]
    context["panels"] = context.get("panels", []) + event["talks_panel"]
    event["talks"] = [
        talk for talk in talks
        if talk.get("Featured","").lower() != "yes" and talk.get("Panel","").lower() != "yes"
    ]

    #counts
    print("%d normal %s keynotes %d panels" % (len(event["talks"]), len(event["talks_featured"]), len(event["talks_panel"])))

    # extract and store the tracks
    tracks = dict()
    for talk in event["talks"]:
        track = talk.get("Track", "other")
        if track not in tracks:
            tracks[track] = []
        tracks[track].append(talk)
    event["tracks"] = tracks

    # render the google calendar link
    name = "Conf42: {}".format(event.get("name"))
    begin = '{} 17:00:00'.format(event.get("date").strftime('%Y-%m-%d'))
    end = '{} 22:00:00'.format(event.get("date").strftime('%Y-%m-%d'))
    url = "https://conf42.com/{}".format(event.get("short_url").replace(".html",""))
    event["google_calendar_url"] = "https://www.google.com/calendar/render?action=TEMPLATE&text={text}&details={details}&location={location}&dates={begin}%2F{end}".format(
        text=urllib.parse.quote_plus(name),
        details=urllib.parse.quote_plus("Online tech conference"),
        location=urllib.parse.quote_plus(url),
        begin='{}T170000Z'.format(event.get("date").strftime('%Y%m%d')),
        end='{}T220000Z'.format(event.get("date").strftime('%Y%m%d')),
    )
    # create an ics file
    event["ics_location"] = event.get("short_url").replace(".html","") + ".ics"
    c = Calendar()
    e = Event(
        name=name,
        begin=begin,
        end=end,
        url=url
    )
    c.events.add(e)
    with open(BASE_FOLDER + "/" + event.get("short_url").replace(".html","") + ".ics", 'w') as f:
        f.write(str(c))
        
    # check that all slide files are there
    print("Checking slides")
    for talk in talks:
        slide_file = talk.get("Slides")
        if slide_file:
            slide_path = make_remote_address("slides", slide_file)
            warn_on_missing_file(slide_path, remote=True)
            talk["Slides"] = slide_path

    # template each talk page for the event
    print("Generating talk pages")
    for talk in talks:
        # check the headshot
        picture_path = make_remote_address("headshots", talk["Picture"])
        warn_on_missing_file(picture_path, remote=True)
        talk["Picture"] = picture_path

        # generate things
        talk["short_url"] = generate_short_url(event, talk)
        talk["YouTubeId"] = talk.get("YouTube").split("/")[-1]

        # template the talk subpage
        with open(BASE_FOLDER + "/" + talk.get("short_url").replace(".html","")  + ".html", "w") as f:
            template = env.get_template("talk.html")
            f.write(template.render(event=event, talk=talk, **context))
            urls.append((talk.get("short_url").replace(".html",""), 0.7))
        # template the secret talk subpage
        if event.get("secret_url"):
            with open(BASE_FOLDER + "/" + event.get("secret_url") + "_" + talk.get("short_url").replace(".html","")  + ".html", "w") as f:
                template = env.get_template("talk.html")
                event_copy = event.copy()
                event_copy["reveal_videos"] = True
                f.write(template.render(event=event_copy, talk=talk, secret_mode=True, **context))

    # template the main event page
    with open(BASE_FOLDER + "/" + event.get("short_url").replace(".html","") + ".html", "w") as f:
        template = env.get_template("event.html")
        f.write(template.render(event=event, **context))
        urls.append((event.get("short_url").replace(".html",""), 0.8))

    # template the secret event page
    if event.get("secret_url"):
        with open(BASE_FOLDER + "/" + event.get("secret_url") + ".html", "w") as f:
            template = env.get_template("event.html")
            event_copy = event.copy()
            event_copy["reveal_videos"] = True
            f.write(template.render(event=event_copy, secret_mode=True, prefix=event.get("secret_url")+"_", **context))



# PODCAST
print(DIVIDER)
print("Generating podcast pages")

podcasts = context.get("podcasts")
# podcasts.sort(key=lambda e: e.get("date"))
for podcast in podcasts:

    picture_path = make_remote_address("podcasts", podcast["picture_path"])
    warn_on_missing_file(picture_path, remote=True)
    podcast["picture_path"] = picture_path

    podcast["YouTubeId"] = podcast.get("url").split("/")[-1]

    transcript_path = podcast.get("transcript")
    if not transcript_path:
        print("No transcript file for: %s" % podcast.get("title"))
        continue

    print("Processing transcript file: %s" % transcript_path)
    with open("./transcripts/" + transcript_path, 'r') as f:
        chapters = f.read().split("\n\n")
    transcript = []
    for chapter in chapters:
        if "Transcribed by" in chapter:
            continue
        if not chapter or not ("\n" in chapter):
            continue
        header, body = chapter.split("\n", 1)
        speaker, timestamp = header.split("  ", 1)
        time_m, time_s = timestamp.split(":")[:2]
        transcript.append(dict(
            speaker=speaker,
            timestamp=timestamp,
            timestamp_s=(int(time_m)*60 + int(time_s)),
            body=body,
        ))
    podcast["transcript"] = transcript

    # write out the template for the podcast episode
    with open(BASE_FOLDER + "/" + podcast.get("short_url").replace(".html","") + ".html", "w") as f:
        template = env.get_template("podcast_episode.html")
        f.write(template.render(podcast=podcast, **context))
        urls.append((podcast.get("short_url").replace(".html",""), 0.81))


print(DIVIDER)
print("Reading sponsor metadata")

try:
    posts = sorted(read_csv("./_db/blog.csv"), key=lambda x: x.get("Date"), reverse=True)
    context["posts"] = posts
    print("Loaded %s posts" % len(posts))
except Exception as e:
    print("Couldn't read blog posts", e)


# BLOG
print(DIVIDER)
print("Generating blog posts")

for post in posts:
    post["Date"] = dateutil.parser.parse(post["Date"])

for post in posts:
    if post.get("ExternalURL"):
        continue
    print("Generating blog post subpage for", post.get("ShortURL"))
    with open(BASE_FOLDER + "/" + post.get("ShortURL") + ".html", "w") as f:
        template = env.get_template("blog_post.html")
        f.write(template.render(post=post, **context))
        urls.append((post.get("ShortURL").replace(".html",""), 0.81))

# MAIN PAGES
print(DIVIDER)
print("Generating main pages")
for page in ["index.html", "podcast.html", "sponsor.html", "sponsorship.html", "code-of-conduct.html", "terms-and-conditions.html", "blog.html", "seradio.html"]:
    with open(BASE_FOLDER + "/" + page, "w") as f:
        print("Writing out", page)
        template = env.get_template(page)
        f.write(template.render(page=page, **context))
        if page != "index.html":
            urls.append((page.replace(".html",""), 0.75))

# SITEMAP
print(DIVIDER)
print("Generating sitemap.xml with %d items" % len(urls))
now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
with open(BASE_FOLDER + "/sitemap.xml", "w") as f:
    template = env.get_template("sitemap.xml")
    f.write(template.render(urls=urls, now=now))

print(DIVIDER)
print("Warnings")
print("Missing %d remote files" % len(WARNINGS))
for w in WARNINGS:
    print(w)