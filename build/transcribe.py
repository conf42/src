import sys
import os

from .yt import (
    download_youtube_audio,
    get_yt_id,
)
from .assemblyai import (
    check_transcript_exists,
    get_transcript,
    write_transcript,
)
from .events import (
    get_enriched_metadata,
    extract_keywords,
)

DOWNLOAD_PATH = "./cache_yt"


video_queue = []
context = get_enriched_metadata("docs")

# sort from the most recent
context.get("events").sort(key=lambda x: x.get("date"), reverse=True)

# find all talk videos
for event in context.get("events"):
    for talk in event.get("talks_raw", []):
        video = talk.get("YouTube")
        if video:
            video_queue.append((talk, video))
print(f"Found {len(video_queue)} talks with videos")

# find all talks with missing transcriptions
missing_transcriptions = []
for talk, video in video_queue:
    transcript_path = check_transcript_exists(get_yt_id(video))
    if not transcript_path:
        missing_transcriptions.append((talk, video))
print(f"Found {len(missing_transcriptions)} talks without transcripts")

for i, (talk, video) in enumerate(missing_transcriptions):
    print(f"({i}/{len(missing_transcriptions)}) Processing video {video}")

    # get the audio to transcribe
    audio_path = None
    retries = 10
    for _ in range(retries):
        try:
            audio_path, _ = download_youtube_audio(video, DOWNLOAD_PATH)
            print(f"Got audio: {audio_path}")
            break
        except Exception as ex:
            print(f"({i}/{retries}) Error getting audio: {ex}")
            pass
    if not audio_path:
        print("Couldn't get the video after")
        continue
    
    # get the keywords
    keywords = extract_keywords(talk)
    # get the transcript
    transcript = get_transcript(audio_path, keywords)
    if not transcript:
        #sys.exit(1)
        continue
    # write the transcript for later
    write_transcript(get_yt_id(video), transcript)

    # clean up the working dir
    os.remove(audio_path)

    # TODO remove - batch for now
    if i == 99:
        sys.exit(0)

    