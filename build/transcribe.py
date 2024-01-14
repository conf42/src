import yaml
from .yt import download_youtube_audio, check_video_exists, get_yt_id
from .assemblyai import check_transcript_exists, get_transcript, write_transcript, read_transcript

DOWNLOAD_PATH = "./cache_yt"

# find the videos without transcription
# for each,
#       download the audio
#       call the API to get the transcript
#       store the outputs in the cache

video_queue = ["https://youtu.be/kFX9E5PkqLo"]

for video in video_queue:
    print(f"Processing video {video}")

    audio_path = check_video_exists(DOWNLOAD_PATH, video)
    if not audio_path:
        audio_path, _ = download_youtube_audio(video, DOWNLOAD_PATH)
    
    print(f"Got audio: {audio_path}")

    transcript_path = check_transcript_exists(get_yt_id(video))
    
    if transcript_path:
        transcript = read_transcript(yt_id)
    else:
        transcript = get_transcript(audio_path)
        write_transcript(transcript)
    
    print(transcript)

    