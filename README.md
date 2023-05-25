# Speach2cut

Speach2cutはYouTubeでURLを指定して実行するだけで発話部分だけを1.wav...2.wav..のように出力するプログラムです。

# 環境構築

新品のピカピカのPCでも以下の手順で環境構築ができます。

以下のソフトウェアがインストールされていることを確認してください。


Git https://git-scm.com/downloads

Python https://www.python.org/downloads
(バージョンは3.10.7-3.11.3はいけるのはほぼ確定、これ以外は動作確認はしてないけど多分めっちゃ幅広くOKなはず)

CUDA Toolkit 11.7 https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local

cuDNN https://developer.nvidia.com/rdp/cudnn-download

zlib https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-zlib-windows

# インストール手順

エクスプローラーを開き保存したい場所で上にあるファイルパスでcmdと入力してEnterキーを押すとそのパスでコマンドプロンプトが起動します。

そして以下のコマンドを実行して、環境構築を行います。
    
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py && git clone https://github.com/keimaruO/Speach2cut.git && cd Speach2cut && python -m pip install --upgrade pip && pip install -r requirements.txt && curl -L https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip -o ffmpeg.zip && curl -L https://github.com/yt-dlp/yt-dlp/releases/download/2023.03.04/yt-dlp.exe -o yt-dlp.exe && tar -xf ffmpeg.zip && move ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe ffmpeg.exe && move ffmpeg-master-latest-win64-gpl\bin\ffplay.exe ffplay.exe && move ffmpeg-master-latest-win64-gpl\bin\ffprobe.exe ffprobe.exe && del ffmpeg.zip && del ../test/get-pip.py && rd /s /q ffmpeg-master-latest-win64-gpl
```
