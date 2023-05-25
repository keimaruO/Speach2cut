import os
import datetime
import subprocess
import re
import shutil

def get_ffmpeg_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "ffmpeg.exe")

def move_files_to_archive(archive_base_dir):
    archive_dir = os.path.join(archive_base_dir, "archive")
    srt_file_path = os.path.join(BASE_DIR, "scripts", "temp_1.srt")
    mp4_file_path = os.path.join(BASE_DIR, "scripts", "concatenated_video.mp4")
    wav_file_path = os.path.join(BASE_DIR, "scripts", "temp_1.wav")
    
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    existing_folders = [int(folder) for folder in os.listdir(archive_dir) if folder.isdigit()]
    next_folder_number = max(existing_folders) + 1 if existing_folders else 1

    files_to_move = [
        os.path.join(BASE_DIR, "scripts", "temp_1.tsv"),
        os.path.join(BASE_DIR, "scripts", "temp_1.txt"),
        os.path.join(BASE_DIR, "scripts", "temp_1.vtt"),
        os.path.join(BASE_DIR, "scripts", "temp_1.json"),
    ]

    if os.path.exists(wav_file_path) or os.path.exists(mp4_file_path) or any(os.path.exists(path) for path in files_to_move):
        new_archive_folder = os.path.join(archive_dir, str(next_folder_number))
        os.makedirs(new_archive_folder)

        # Move files with their original names
        for file_path in [wav_file_path, mp4_file_path, srt_file_path, *files_to_move]:
            if os.path.exists(file_path):
                destination = os.path.join(new_archive_folder, os.path.basename(file_path))
                shutil.move(file_path, destination)

        for file in os.listdir(output_yt_dlp_dir):
            if file != ".gitignore":
                file_path = os.path.join(output_yt_dlp_dir, file)
                shutil.move(file_path, new_archive_folder)

def convert_audio_to_video(input_audio_path, output_video_path):
    ffmpeg_path = get_ffmpeg_path()

    duration_command = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        input_audio_path,
    ]
    duration_output = subprocess.run(duration_command, capture_output=True, text=True)
    duration = duration_output.stdout.strip()

    command = [
        ffmpeg_path,
        "-y",
        "-i",
        input_audio_path,
        "-vf",
        "scale=iw/1:ih/1",
        "-vcodec",
        "mpeg4",
        "-b:v",
        "32k",
        "-r",
        "15",
        "-strict",
        "-2",
        output_video_path
    ]
    os.system(" ".join(command))

# YouTubeからwavだけダウンロード
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
subprocess.run(["python", os.path.join(BASE_DIR, "yt-dlp.py")])

# scripts/yt-dlpフォルダから.wavファイルを見つけてリネームし、scripts/フォルダに移動
output_yt_dlp_dir = os.path.join(BASE_DIR, "scripts", "yt-dlp")
for file_name in os.listdir(output_yt_dlp_dir):
    if file_name.endswith(".wav"):
        source = os.path.join(output_yt_dlp_dir, file_name)
        destination = os.path.join(BASE_DIR, "scripts", "temp_1.wav")
        os.rename(source, destination)
        break

scripts_dir = os.path.join(BASE_DIR, "scripts")
input_wav = os.path.join(BASE_DIR, "scripts", "temp_1.wav")
whisper_command = f'whisper-ctranslate2 "{input_wav}" --model tiny --compute_type auto --language Japanese --temperature_increment_on_fallback None"'
print(whisper_command)
subprocess.run(whisper_command, shell=True, cwd=scripts_dir)

input_audio_path = os.path.join(BASE_DIR, "scripts", "temp_1.wav")
output_video_path = os.path.join(BASE_DIR, "scripts", "concatenated_video.mp4")
convert_audio_to_video(input_audio_path, output_video_path)

subprocess.run(["python", os.path.join(BASE_DIR, "sub.py")])

archive_base_dir = os.path.join(BASE_DIR, "sozai")
move_files_to_archive(archive_base_dir)
archive_video_file_path = os.path.join(archive_base_dir, "archive", "1", "concatenated_video.mp4")

if os.path.exists(archive_video_file_path):
    os.remove(archive_video_file_path)
