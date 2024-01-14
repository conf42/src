import os
from collections import defaultdict


def process_transcript(path):
    with open(path, "r") as f:
        return f.read()

def find_transcripts(path):
    transcripts = defaultdict(dict)
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith(".txt") and len(filename.split("_")) == 2:
                yt, lang = filename.split("_")
                transcripts[yt][lang] = process_transcript(os.path.join(root, filename))

    return transcripts

def process_transcript(transcript):
    sentences = [
        x.strip() + "." for x in transcript.split(".")
    ]
    output = []
    for sentence in sentences:
        if len(sentence) < 100:
            output.append(sentence)
        else:
            for i, x in enumerate(sentence.split(" so ")):
                output.append(("" if i == 0 else " so ") + x)
    return output
