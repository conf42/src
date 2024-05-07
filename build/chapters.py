import sys
import os

from .yt import (
    get_yt_id,
)
from .assemblyai import (
    read_transcript,
    get_chapters,
    write_chapters,
)
from .events import (
    get_enriched_metadata,
)

target_yt_id = os.environ.get("YT_ID")
if not target_yt_id:
    print("Specify YT_ID envvar")
    sys.exit(1)

context = get_enriched_metadata("docs")

# find all talk videos
all_talks = dict()
for event in context.get("events"):
    for talk in event.get("talks", []):
        video = talk.get("YouTube")
        if video:
            yt_id = get_yt_id(video)
            all_talks[yt_id] = talk
print(f"Found {len(all_talks)} talks with videos")

if target_yt_id not in all_talks:
    print(f"YT_ID not found: {target_yt_id}")
    sys.exit(1)

talk = all_talks.get(target_yt_id)
print(f"Talk found: {talk['Title']}")
transcript = read_transcript(target_yt_id)
if not transcript:
    print(f"Transcript not found for: {target_yt_id}")
    sys.exit(1)

chapters = get_chapters(talk, transcript)
if not chapters:
    print(f"chapters couldn't be done for: {target_yt_id}")
    sys.exit(1)
print(chapters)
write_chapters(target_yt_id, chapters)
