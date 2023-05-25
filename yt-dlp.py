import os
import subprocess

# 現在のスクリプトのディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# yt-dlpが存在するディレクトリのパスを設定
yt_dlp_dir = "yt-dlp"

# dlurl.txtファイルのパス指定
DLURL_FILE = os.path.join(script_dir, "dlurl.txt")

def main():
    # dlurl.txtファイルを開く
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open(DLURL_FILE, "r") as file:
        lines = file.readlines()

    output_counter = 1

    # 各行を処理する
    for i in range(len(lines)):
        line = lines[i].strip()

        # 空行をスキップ
        if not line:
            continue

        # URLの場合
        if "http" in line:
            current_url = line

            # 次の行が存在し、時間範囲を示している場合を除き、フル動画をダウンロード
            if i == len(lines) - 1 or not "-" in lines[i + 1]:
                output_path = f'scripts/yt-dlp/{output_counter}%(title)s.%(ext)s'
                output_counter += 1

                # yt-dlpコマンドを実行（フル動画）
                cmd = " ".join([
                    "yt-dlp",
                    "-f", "\"bestaudio[ext=m4a]/best[ext=mp4]\"",
                    "-N", "1",
                    "-S", "vcodec:h264",
                    "-o", output_path,
                    "--extract-audio",
                    "--audio-format", "wav",
                    current_url
                ])

                print("Executing command:", cmd)
                subprocess.run(cmd, shell=True)

        # 時間範囲の場合
        elif "-" in line:
            start_time, end_time = line.split("-")
            output_path = f'scripts/yt-dlp/{output_counter}%(title)s.%(ext)s'
            output_counter += 1

            # yt-dlpコマンドを実行（時間範囲指定）
            cmd = " ".join([
                "yt-dlp",
                "-f", "\"bestaudio[ext=m4a]/best[ext=mp4]\"",
                "-N", "1",
                "-S", "vcodec:h264",
                "-o", output_path,
                "--download-sections", f'*{start_time}-{end_time}',
                "--extract-audio",
                "--audio-format", "wav",
                current_url
            ])

            print("Executing command:", cmd)
            subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    main()
