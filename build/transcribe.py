import sys
from .yt import (
    download_youtube_audio,
    check_video_exists,
    get_yt_id,
)
from .assemblyai import (
    check_transcript_exists,
    get_transcript,
    write_transcript,
    read_transcript,
)
from .events import (
    get_enriched_metadata,
    extract_keywords,
)

DOWNLOAD_PATH = "./cache_yt"


video_queue = []
context = get_enriched_metadata("docs")

# sort from the most recent
context.get("events").sort(key=lambda x: x.get("date"), reversed=True)

# find all talk videos
for event in context.get("events"):
    for talk in event.get("talks", []):
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

# TODO remove
missing_transcriptions = missing_transcriptions[:1]

for talk, video in missing_transcriptions:
    print(f"Processing video {video}")

    # get the audio to transcribe
    audio_path, _ = download_youtube_audio(video, DOWNLOAD_PATH)
    print(f"Got audio: {audio_path}")
    
    # get the keywords
    keywords = extract_keywords(talk)
    # get the transcript
    transcript = get_transcript(audio_path, keywords)
    if not transcript:
        #sys.exit(1)
        continue
    # write the transcript for later
    write_transcript(get_yt_id(video), transcript)

    