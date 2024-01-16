import json
import os
import assemblyai as aai

CACHE_PATH = "./assemblyai"


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
    aai.settings.api_key = os.environ.get("ASSEMBLYAI_KEY")
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
    # read the srt, if present, and parse for easy usage
    try:
        with open(get_transcript_path(yt_id, extension=".srt"), "r") as f:
            transcript["srt"] = f.read()
        for elem in transcript["srt"].split("\n\n"):
            _, time_line, text = elem.split("\n")
            time_start = time_line.split(" ")[0]
            transcript["chunks"].append(dict(
                text=text,
                timestamp=time_start,
                timestamp_s=0, # TODO
            ))
    except:
        pass
    # process the srt into an array

    return transcript
