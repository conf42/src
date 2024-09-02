CACHE_PATH = "./srt"

from .transcript import (
    parse_srt,
)

def read_srt_transcript(name, event):
    transcript = dict(metadata={}, summary="")

    # read the srt, if present, and parse for easy usage
    key = f"{event}_{name}"
    path = (CACHE_PATH + "/" + key + ".srt").replace(" ", "_")
    try:
        with open(path, "r") as f:
            print(f"found transcript at {path}")
            transcript["srt"] = f.read()
    except:
        print(f"nothing at {path}")
        return None
    try:
        transcript["chunks"] = parse_srt(transcript["srt"])
        return transcript
    except Exception as ex:
        print(ex)
        return None
