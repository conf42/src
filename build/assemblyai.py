import json
import os
import assemblyai as aai

CACHE_PATH = "./assemblyai"

aai.settings.api_key = os.environ.get("ASSEMBLYAI_KEY")

from .transcript import (
    parse_srt,
)

def get_transcript_path(yt_id, extension=".json"):
    if "https://" in yt_id:
        yt_id = yt_id.split("/")[-1]
    return os.path.join(CACHE_PATH, yt_id + extension)

def check_transcript_exists(yt_id):
    p = get_transcript_path(yt_id)
    if os.path.exists(p):
        return p

def get_transcript(audio_path, keywords):
    print(f"Getting transcript for audio {audio_path} with keywords {keywords}")
    transcriber = aai.Transcriber()
    config = aai.TranscriptionConfig(
        summarization=True,
        summary_model=aai.SummarizationModel.informative,
        summary_type=aai.SummarizationType.bullets_verbose,
        auto_highlights=True,
        word_boost=keywords,
        boost_param="high",
    )
    transcript = transcriber.transcribe(
        audio_path,
        config=config,
    )
    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription failed: {transcript.error}")
        return False

    #print(transcript.text)
    #for result in transcript.auto_highlights.results:
    #    print(f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}")
    return transcript
        
def write_transcript(yt_id, transcript):
    with open(get_transcript_path(yt_id), "w") as f:
        resp = transcript.json_response
        # remove the words portion, as it's super heavy
        resp["words"] = []
        f.write(json.dumps(resp))
    #with open(get_transcript_path(yt_id, extension=".txt"), "w") as f:
    #    f.write(transcript.text)
    #with open(get_transcript_path(yt_id, extension=".vtt"), "w") as f:
    #    f.write(transcript.export_subtitles_vtt())
    with open(get_transcript_path(yt_id, extension=".srt"), "w") as f:
        f.write(transcript.export_subtitles_srt())

def read_transcript(yt_id):
    transcript = dict(chunks=[])
    # read the json
    try:
        with open(get_transcript_path(yt_id), "r") as f:
            transcript["metadata"] = json.loads(f.read())
    except:
        return None

    # preprocess the summary
    transcript["summary"] = [
        li
        for li in transcript["metadata"]["summary"].split("- ")
        if li
    ]

    # read the srt, if present, and parse for easy usage
    path = get_transcript_path(yt_id, extension=".srt")
    try:
        with open(path, "r") as f:
            transcript["srt"] = f.read()
        transcript["chunks"] = parse_srt(transcript["srt"])
        transcript["path"] = path
    except:
        pass
    return transcript

def get_summary(talk, transcript):
    print(f"Getting summary for {talk['Title']}")
    transcript = aai.Transcript.get_by_id(transcript["metadata"]["id"])
    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription failed: {transcript.error}")
        return False
    
    prompt = "Provide a summary. Do not provide a preambule."
    summary = transcript.lemur.task(
        prompt,
        final_model=aai.LemurModel.mistral7b,
    )
    return summary.response

def write_summary(yt_id, summary):
    with open(get_transcript_path(yt_id, extension="-summary.txt"), "w") as f:
        f.write(summary)

def get_chapters(talk, transcript):
    print(f"Getting chapters for {talk['Title']}")
    transcript = aai.Transcript.get_by_id(transcript["metadata"]["id"])
    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription failed: {transcript.error}")
        return False
    
    prompt = "Provide a YouTube description of the transcript. Include chapters with timestamps. Do not provide a preambule."
    req = transcript.lemur.task(
        prompt=prompt,
        #context="this is a talk at a technology conference called Conf42",
        temperature=0.1,
        max_output_size=2000,
    )
    return req.response

def write_chapters(yt_id, summary):
    with open(get_transcript_path(yt_id, extension="-chapters.txt"), "w") as f:
        f.write(summary)

def get_article(talk, transcript):
    print(f"Generating an article for {talk['Title']}")
    transcript = aai.Transcript.get_by_id(transcript["metadata"]["id"])
    if transcript.status == aai.TranscriptStatus.error:
        print(f"Transcription failed: {transcript.error}")
        return False
    
    prompt = "Write an article. Use markdown. Do not provide a preambule."
    summary = transcript.lemur.task(
        prompt,
        final_model=aai.LemurModel.default,
        max_output_size=4000,
    )
    return summary.response

def write_article(yt_id, text):
    with open(get_transcript_path(yt_id, extension=".md"), "w") as f:
        f.write(text)
