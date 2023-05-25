import pysrt

def parse_srt_file(srt_file_path):
    subs = pysrt.open(srt_file_path)
    return [{'start': sub.start.to_time(), 'end': sub.end.to_time(), 'text': sub.text} for sub in subs]