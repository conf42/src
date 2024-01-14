import json
import os
import assemblyai as aai

CACHE_PATH = "./assemblyai"


def get_transcript_path(yt_id):
    return os.path.join(CACHE_PATH, yt_id + ".json")

def check_transcript_exists(yt_id):
    p = get_transcript_path(yt_id)
    if os.path.exists(p):
        return p

def get_transcript(audio_path):
    print(f"Getting transcript for audio {audio_path}")
    aai.settings.api_key = os.environ.get("ASSEMBLYAI_KEY")
    transcriber = aai.Transcriber()
    config = aai.TranscriptionConfig(
        summarization=True,
        summary_model=aai.SummarizationModel.informative,
        summary_type=aai.SummarizationType.bullets_verbose,
        auto_highlights=True,
    )
    transcript = transcriber.transcribe(
        audio_path,
        config=config,
    )
    print(transcript.text)

    for result in transcript.auto_highlights.results:
        print(f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}")
    return transcript
        
def write_transcript(yt_id, transcript):
    with open(get_transcript_path(yt_id), "w") as f:
        f.write(json.dumps(transcript.json_response))
    
def read_transcript(yt_id):
    with open(get_transcript_path(yt_id), "r") as f:
        return json.loads(f.read())
