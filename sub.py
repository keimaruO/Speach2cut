import os
from subtitle_parser import parse_srt_file
from video_annotator import cut_video_by_subtitles

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

input_video_path = os.path.join(BASE_DIR, "scripts", "concatenated_video.mp4")
srt_file_path = os.path.join(BASE_DIR, "scripts", "temp_1.srt")
output_folder_path = os.path.join(BASE_DIR, "sozai")

subtitles = parse_srt_file(srt_file_path)

cut_video_by_subtitles(input_video_path, subtitles, output_folder_path)
