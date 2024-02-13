#!/usr/bin/env python3

import datetime
import sys
import urllib.parse
import markdown

from collections import defaultdict
from jinja2 import Environment, FileSystemLoader
from jinja_markdown import MarkdownExtension
import dateutil.parser
from ics import Calendar, Event


from .shared import (
    read_csv,
    generate_speaker_url,
    make_remote_address,
    warn_on_missing_file,
    generate_short_url,
    get_canonical_url,
    get_warnings,
)
from .events import get_enriched_metadata

DIVIDER = "#"*80
BASE_FOLDER = "./docs"
SITEMAP_URLS = []

# store urls for the sitemap.xml
def register_url(url):
    SITEMAP_URLS.append(url)

print(DIVIDER)
print("Loading the context")
context = get_enriched_metadata(BASE_FOLDER)

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
env.filters["speaker_url"] = generate_speaker_url
env.filters["markdown"] = lambda x: markdown.markdown(x)


# SPONSORSHIPS
print(DIVIDER)
print("Validating sponsorship levels")
sponsorship_levels = [
    v.get("id") for v in context.get("sponsorships")
]
context["sponsorship_levels"] = sponsorship_levels
print(DIVIDER)
print("Sponsorship levels:", sponsorship_levels)
for event in context.get("events"):
    for level in event.get("sponsors", dict()).keys():
        if level not in sponsorship_levels:
            print("Event %s has invalid sponsorship level: %s" % (event.get("name"), level))
            sys.exit(1)


# TESTIMONIALS
print(DIVIDER)
print("Reading testimonials metadata")
testimonials = read_csv("./_db/testimonials.csv")
for testimonial in testimonials:
    testimonial["Picture"] = make_remote_address("headshots", testimonial["Headshot"])
context["testimonials"] = testimonials
print("Loaded %d testimonials metadata" % len(context["testimonials"]))


# SPONSORS
print(DIVIDER)
print("Generating sponsor subpages")
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
    print("Couldn't read subpages", e)

for subpage in context["sponsor_subpages"]:
    with open(BASE_FOLDER + "/" + subpage.get("Sponsor")  + ".html", "w") as f:
        template = env.get_template("sponsor_subpage.html")
        f.write(template.render(sponsor=subpage, secret_mode=True, **context))


print(DIVIDER)
print("Writing ics files")
for event in context.get("events"):
    # no need for the external events
    if "external_url" in event:
        continue
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

print(DIVIDER)
print("Checking external assets")
for event in context.get("events"):
    # no need for the external events
    if "external_url" in event:
        continue
    # enrich the talks
    for talk in event["talks_raw"]:
        # check the slide file exists
        slide_file = talk.get("Slides")
        if slide_file:
            slide_path = make_remote_address("slides", slide_file)
            warn_on_missing_file(slide_path, remote=True)
            talk["Slides"] = slide_path

        # check the headshot exists
        picture_path = make_remote_address("headshots", talk.get("Picture", ""))
        warn_on_missing_file(picture_path, remote=True)
        talk["Picture"] = picture_path
        talk["short_url"] = generate_short_url(event, talk)
        talk["YouTubeId"] = talk.get("YouTube", "").split("/")[-1]


print(DIVIDER)
print("Handling speaker stats")
speakers = defaultdict(list)
context["speakers"] = speakers
for event in context.get("events"):
    for talk in event.get("talks_raw", []):
        for field in ["Name1", "Name2"]:
            speaker = talk.get(field)
            if speaker:
                speakers[speaker].append(dict(
                    date=event.get("date"),
                    event=event,
                    talk=talk,
                ))
for speaker, talks in speakers.items():
    talks.sort(key=lambda x: x.get("date"), reverse=True)
#context["speakers_list"] = sorted(speakers.keys(), key=lambda x: str(len(speakers.get(x))) + "_" + x, reverse=True)
context["speakers_list"] = sorted(speakers.keys())
print(f"Found {len(speakers)} speakers")

# stats for videos
print(DIVIDER)
print("Handling video stats")
# read
video_stats = [x for x in read_csv("./_db/video_stats.csv")][:-1]
for stat in video_stats:
    stat["Minutes"] = float(stat["Watch time (hours)"])*60
    stat["Content"] = stat["Content"].strip()
video_stats_totals = video_stats[0]
video_stats = video_stats[1:]
context["video_stats"] = video_stats
context["video_stats_totals"] = video_stats_totals
print(video_stats_totals)
# normalize
video_stats.sort(key=lambda x: int(x.get("Views")), reverse=True)
# generate mappings
video_to_stats = dict()
video_to_position = dict()
context["video_to_stats"] = video_to_stats
context["video_to_position"] = video_to_position
for index, stat in enumerate(video_stats):
    video_id = stat.get("Content")
    video_to_stats[video_id] = stat
    video_to_position[video_id] = index + 1
print(f"Found {len(video_to_stats)} stats")
# match with talks
counter = 0
for event in context.get("events"):
    totals = dict(
        minutes=0,
        views=0,
        impressions=0,
    )
    event["totals"] = totals
    for talk in event.get("talks_raw", []):
        video_id = talk.get("YouTube", "").split("/")[-1]
        stats = video_to_stats.get(video_id)
        talk["stats"] = stats
        position = video_to_position.get(video_id)
        talk["position"] = position
        if stats is not None:
            counter += 1
            stats["talk"] = talk
            talk["event"] = event
            # count up the totals
            totals["minutes"] += int(stats.get("Minutes"))
            totals["views"] += int(stats.get("Views"))
            totals["impressions"] += int(stats.get("Impressions"))
print(f"Matched {counter} talks to stats")
# match with the premieres
premieres = []
context["premieres"] = premieres
for event in context.get("events"):
    video_id = event.get("premiere_url")
    stats = video_to_stats.get(video_id)
    event["stats"] = stats
    position = video_to_position.get(video_id)
    event["position"] = position
    if stats is not None:
        # skip events below 200 views
        if int(stats.get("Views")) < 200:
            continue
        premieres.append(dict(
            stats=stats,
            event=event,
        ))
        stats["event"] = event
premieres.sort(key=lambda x:int(x.get("stats").get("Views")), reverse=True)
print(f"Matched {len(premieres)} premieres to stats")


# EVENT PAGES
print(DIVIDER)
print("Genearing events & talk pages")
for event in context.get("events"):
    # for external events, no need to generate pages
    if "external_url" in event:
        continue
    # just for dev experience - 2s vs 12s
    if "quick" in sys.argv:
        continue

    print(f"Templating out {event.get('name')} {event.get('year')}")

    # template each talk page for the event
    for talk in event.get("talks_raw"):
        # template the talk subpage
        with open(BASE_FOLDER + "/" + talk.get("short_url").replace(".html","")  + ".html", "w") as f:
            template = env.get_template("talk.html")
            f.write(template.render(event=event, canonical=get_canonical_url(talk.get("short_url")), talk=talk, **context))
            register_url(talk.get("short_url").replace(".html",""))
        # template the secret talk subpage
        if event.get("secret_url"):
            with open(BASE_FOLDER + "/" + event.get("secret_url") + "_" + talk.get("short_url").replace(".html","")  + ".html", "w") as f:
                template = env.get_template("talk.html")
                f.write(template.render(event=event, canonical=get_canonical_url(talk.get("short_url")), talk=talk, secret_mode=True, **context))

    # template the main event page
    with open(BASE_FOLDER + "/" + event.get("short_url").replace(".html","") + ".html", "w") as f:
        template = env.get_template("event.html")
        f.write(template.render(event=event, canonical=get_canonical_url(event.get("short_url")), **context))
        register_url(event.get("short_url").replace(".html",""))
    # template the secret event page
    if event.get("secret_url"):
        with open(BASE_FOLDER + "/" + event.get("secret_url") + ".html", "w") as f:
            template = env.get_template("event.html")
            f.write(template.render(event=event, canonical=get_canonical_url(talk.get("short_url")), secret_mode=True, prefix=event.get("secret_url")+"_", **context))

# SPEAKER PAGES
print(DIVIDER)
print("Generating speaker pages")
for speaker, items in speakers.items():
    #print(f"Templating out {speaker}")
    url = generate_speaker_url(speaker)
    with open(BASE_FOLDER + "/" + url  + ".html", "w") as f:
        template = env.get_template("speaker.html")
        f.write(template.render(speaker=speaker, canonical=get_canonical_url(url), items=items, **context))
        register_url(url)


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
        f.write(template.render(podcast=podcast, canonical=get_canonical_url(podcast.get("short_url")), **context))
        register_url(podcast.get("short_url").replace(".html",""))



print(DIVIDER)
print("Generating blog posts")
try:
    posts = sorted(read_csv("./_db/blog.csv"), key=lambda x: x.get("Date"), reverse=True)
    context["posts"] = posts
    print("Loaded %s posts" % len(posts))
except Exception as e:
    print("Couldn't read blog posts", e)
# prepare the posts
for post in posts:
    post["Date"] = dateutil.parser.parse(post["Date"])
# template out the posts
for post in posts:
    # just for dev experience - 2s vs 12s
    if "quick" in sys.argv:
        continue

    if post.get("ExternalURL"):
        continue
    print("Generating blog post subpage for", post.get("ShortURL"))
    with open(BASE_FOLDER + "/" + post.get("ShortURL") + ".html", "w") as f:
        template = env.get_template("blog_post.html")
        f.write(template.render(post=post, canonical=get_canonical_url(post.get("ShortURL")),  **context))
        register_url(post.get("ShortURL").replace(".html",""))

# MAIN PAGES
print(DIVIDER)
print("Generating main pages")
for page in ["index.html", "podcast.html", "sponsor.html", "sponsorship.html", "code-of-conduct.html", "blog.html", "seradio.html", "hall-of-fame.html", "speakers.html", "stats.html", "testimonials.html", "support.html", "about.html"]:
    with open(BASE_FOLDER + "/" + page, "w") as f:
        print("Writing out", page)
        template = env.get_template(page)
        f.write(template.render(page=page, canonical=get_canonical_url(page), **context))
        if page not in ["index.html", "stats.html", "seradio.html", "sponsorship.html"]:
            register_url(page.replace(".html",""))

# SITEMAP
print(DIVIDER)
print("Generating sitemap.xml with %d items" % len(SITEMAP_URLS))
now = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
with open(BASE_FOLDER + "/sitemap.xml", "w") as f:
    template = env.get_template("sitemap.xml")
    f.write(template.render(urls=SITEMAP_URLS, now=now))

print(DIVIDER)
print("Warnings")
for w in get_warnings():
    print(w)
