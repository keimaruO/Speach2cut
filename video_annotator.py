import os
import datetime
from moviepy.editor import AudioFileClip

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def cut_video_by_subtitles(input_video_path, subtitles, output_folder):
    video = AudioFileClip(input_video_path)
    fps = video.fps

    video_duration = video.duration

    for index, subtitle in enumerate(subtitles):
        start_time = datetime.timedelta(hours=subtitle['start'].hour, minutes=subtitle['start'].minute, seconds=subtitle['start'].second, microseconds=subtitle['start'].microsecond).total_seconds()
        end_time = datetime.timedelta(hours=subtitle['end'].hour, minutes=subtitle['end'].minute, seconds=subtitle['end'].second, microseconds=subtitle['end'].microsecond).total_seconds()

        if index > 0:
            prev_end_time = datetime.timedelta(hours=subtitles[index-1]['end'].hour, minutes=subtitles[index-1]['end'].minute, seconds=subtitles[index-1]['end'].second, microseconds=subtitles[index-1]['end'].microsecond).total_seconds()
            if start_time - 1 > prev_end_time:
                start_time = max(0, start_time - 1)

        if index < len(subtitles) - 1:
            next_start_time = datetime.timedelta(hours=subtitles[index+1]['start'].hour, minutes=subtitles[index+1]['start'].minute, seconds=subtitles[index+1]['start'].second, microseconds=subtitles[index+1]['start'].microsecond).total_seconds()
            if end_time + 1 < next_start_time:
                end_time = min(video_duration, end_time + 1)

        clip = video.subclip(start_time, end_time)
        clip.write_audiofile(os.path.join(output_folder, f'{index+1}.wav'))

    video.close()
