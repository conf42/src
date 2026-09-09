def parse_time_start(time_start):
    """
        Turns something like
        00:00:37,644 --> 00:00:41,286
        into seconds
    """
    seconds = 0
    multiplier = 3600 # hours
    for elem in time_start.split(",")[0].split(":"):
        seconds += multiplier * int(elem)
        multiplier /= 60
    return seconds

def parse_time_precise(time_start):
    """
        Like parse_time_start, but keeps the milliseconds
        (00:00:37,644 -> 37.644). Used only for paragraph breaks.
    """
    seconds = parse_time_start(time_start)
    try:
        seconds += int(time_start.split(",")[1]) / 1000
    except Exception:
        pass
    return seconds

def parse_srt(transcript):
    chunks = []
    for elem in transcript.split("\n\n"):
        # handle extra whitespace
        if not elem.strip():
            continue
        try:
            split_elemts = elem.split("\n")
            time_line = split_elemts[1]
            text = " ".join(split_elemts[2:])
        except Exception as ex:
            print(f"Unexpected format ({ex}): {elem}")
        time_start = time_line.split(" ")[0]
        seconds = parse_time_start(time_start)
        # precise start/end of the cue (used only for paragraph breaks)
        start_precise = parse_time_precise(time_start)
        try:
            end_precise = parse_time_precise(time_line.split(" ")[2])
        except Exception:
            end_precise = start_precise
        chunks.append(dict(
            text=text,
            timestamp=time_start,
            timestamp_s=seconds,
            start_precise_s=start_precise,
            end_precise_s=end_precise,
        ))
    mark_paragraphs(chunks)
    return chunks


PARA_MIN_PAUSE_S = 1.0   # silence before a cue that closes a paragraph
PARA_MAX_SPAN_S = 60.0   # force a break after this long, at the next sentence end
SENTENCE_END = (".", "?", "!")

def mark_paragraphs(chunks):
    """
        Flags cues that should start a new paragraph (chunk["para_break"] = True).
        A break happens when the previous cue ends a sentence AND either the speaker
        paused for a while, or the current paragraph has been running for too long.
        Purely presentational - ids/timestamps of cues are not affected.
    """
    last_break_s = chunks[0]["start_precise_s"] if chunks else 0
    for i, chunk in enumerate(chunks):
        chunk["para_break"] = False
        if i == 0:
            continue
        prev = chunks[i - 1]
        if not prev["text"].rstrip().endswith(SENTENCE_END):
            continue
        pause = chunk["start_precise_s"] - prev["end_precise_s"]
        span = chunk["start_precise_s"] - last_break_s
        if pause >= PARA_MIN_PAUSE_S or span >= PARA_MAX_SPAN_S:
            chunk["para_break"] = True
            last_break_s = chunk["start_precise_s"]
