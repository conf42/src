#!/usr/bin/env python3

import datetime
import pprint
import csv
import textwrap
import re
import os
import string

import yaml
from jinja2 import Environment, FileSystemLoader

BASE_FOLDER = "./docs"
POSTFIX = ""
if os.environ.get("LOCAL") == "true":
    POSTFIX = ".html"

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
    return url[:100] + POSTFIX

def pick_picture_file(base, pic):
    pic_jpeg = pic.replace(".png", ".jpg")
    if os.path.isfile(base + pic_jpeg):
        return pic_jpeg
    elif not os.path.isfile(base + pic):
        print("Missing picture: %s%s" % (base, pic))
    return pic

def warn_on_missing_file(path):
    if not os.path.isfile(path):
        print("Missing file: %s" % path)
    # else:
    #     print("OK: %s" % path)

# init the jinja stuff
file_loader = FileSystemLoader("_templates")
env = Environment(loader=file_loader)

# load the context from the metadata file
context = dict()
with open('metadata.yml') as f:
    context = yaml.load(f, Loader=yaml.FullLoader)

# preprocess the events
events = context.get("events")
# sort events by date
events.sort(key=lambda e: e.get("date"))
print("Loaded %s events" % len(events))
for event in events:
    event["short_url"] = event.get("short_url") + POSTFIX

future_events = []
past_events = []
years = dict()
for event in events:
    # sort sponsors
    for sponsor_type in event.get("sponsors", {}).keys():
        event["sponsors"][sponsor_type].sort()
    # divide into past and future events
    if datetime.date.today() >= event.get("date"):
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
    if datetime.date.today() >= event.get("videos_reveal_date"):
        event["reveal_videos"] = True
context["years"] = years
context["future_events"] = future_events
context["current_event"] = past_events[-1]
context["past_events"] = past_events[:-1]
context["past_events"].sort(key=lambda e: e.get("date"), reverse=True)

# read the sponsors metadata
try:
    sponsors_list = sorted(read_csv("./_db/sponsors.csv"), key=lambda x: x.get("id"))
    context["sponsors"] = sponsors_list
    context["sponsors_by_id"] = {
        item.get("id"): item for item in sponsors_list
    }
    print("Loaded %d sponsors metadata" % len(context["sponsors"]))
except Exception as e:
    print("Couldn't read sponsors", e)

# pprint.pprint(context)

# generate the subpages
for event in events:
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
    event["talks"] = [talk for talk in talks if talk.get("Featured","").lower() != "yes"]

    # extract and store the tracks
    tracks = dict()
    for talk in event["talks"]:
        track = talk.get("Track", "other")
        if track not in tracks:
            tracks[track] = []
        tracks[track].append(talk)
    event["tracks"] = tracks

    # check that all slide files are there
    for talk in talks:
        slide_file = talk.get("Slides")
        if slide_file:
            warn_on_missing_file(BASE_FOLDER + "/assets/slides/" + slide_file)

    # # template each talk page for the event
    # for talk in talks:        # check the headshot
        talk["Picture"] = pick_picture_file(BASE_FOLDER + "/assets/headshots/", talk["Picture"])

        # generate things
        talk["short_url"] = generate_short_url(event, talk)
        talk["YouTubeId"] = talk.get("YouTube").split("/")[-1]

        # template the talk subpage
        with open(BASE_FOLDER + "/" + talk.get("short_url").replace(".html","")  + ".html", "w") as f:
            template = env.get_template("talk.html")
            f.write(template.render(event=event, talk=talk, **context))
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

    # template the secret event page
    if event.get("secret_url"):
        with open(BASE_FOLDER + "/" + event.get("secret_url") + ".html", "w") as f:
            template = env.get_template("event.html")
            event_copy = event.copy()
            event_copy["reveal_videos"] = True
            f.write(template.render(event=event_copy, secret_mode=True, prefix=event.get("secret_url")+"_", **context))

# preprocess the podcasts
podcasts = context.get("podcasts")
# sort podcasts by date
# podcasts.sort(key=lambda e: e.get("date"))
for podcast in podcasts:

    transcript_path = podcast.get("transcript")
    if not transcript_path:
        continue

    podcast["YouTubeId"] = podcast.get("url").split("/")[-1]

    with open("./transcripts/" + transcript_path, 'r') as f:
        chapters = f.read().split("\n\n")
    transcript = []
    for chapter in chapters:
        if "Transcribed by" in chapter:
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

# generate the static bits
for page in ["index.html", "podcast.html", "sponsor.html", "code-of-conduct.html"]:
    with open(BASE_FOLDER + "/" + page, "w") as f:
        template = env.get_template(page)
        f.write(template.render(page=page, **context))
