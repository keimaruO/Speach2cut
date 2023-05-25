# Speach2cut

Speach2cutはYouTubeでURLを指定して実行するだけで発話部分だけを全自動で1.wav...2.wav..のように出力するプログラムです。

簡単にプログラムの説明をするとyt-dlpでwavだけをDLして、Whisperで字幕を生成、生成された.srtの各セクションのタイムコードの範囲だけをwavで出力

Whisperはtinyです、ちなFaster Whisperを採用しているのでVRAM 4GBでもlarge-v2動きます。でも初期はmedium



# 環境構築

新品のピカピカのPCでも以下の手順で環境構築ができます。

以下のソフトウェアがインストールされていることを確認してください。


Git https://git-scm.com/downloads

Python https://www.python.org/downloads
(オススメは3.10.6  ちな3.10.7-3.11.3でもいける、多分めっちゃ古くない限り幅広くOK)

CUDA Toolkit 11.7 https://developer.nvidia.com/cuda-11-7-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exe_local
# 各自の環境に合わせて選択↓
![image](https://github.com/keimaruO/Speach2cut/assets/91080250/ad484c8d-574b-437d-ba58-6616a6bcd2e5)



cuDNN https://developer.nvidia.com/rdp/cudnn-download
# アカウントが必要↓
![image](https://github.com/keimaruO/Speach2cut/assets/91080250/02b74725-50b9-4080-ae25-28f253c02841)
# うまく作れればこうなる↓
![image](https://github.com/keimaruO/Speach2cut/assets/91080250/b246ea34-1c01-41b9-a799-60d11cee1455)

zlib http://www.winimage.com/zLibDll/zlib123dllx64.zip






# インストール手順

gitとpythonのインストール手順はネットにめっちゃ転がっているので各々調べてもらえたら嬉しいです。

で、CUDA Toolkit 11.7、cuDNN、zlibのインストールに関しては、まずCUDAをインストールする。

終えたら

# C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.7\に行き、このフォルダの中に解凍したcuDNNとzlibをドラッグ・アンド・ドロップする。
![image](https://github.com/keimaruO/Speach2cut/assets/91080250/ea18620a-8dcd-442b-879b-3ed39d83db34)
# binフォルダに入れる
![image](https://github.com/keimaruO/Speach2cut/assets/91080250/570a5672-153b-43d6-812f-50223dc73fdb)
# binフォルダに入れる
![image](https://github.com/keimaruO/Speach2cut/assets/91080250/71b9fb7b-48a7-4844-b0ac-17cccf283fc1)


そして次に、エクスプローラーを開き保存したい好きな場所で上にあるファイルパスでcmdと入力してEnterキーを押すとそのパスでコマンドプロンプトが起動します。
# インストールしたい場所↓
![image](https://github.com/keimaruO/Speach2cut/assets/91080250/80d6198d-580e-4a0d-a6af-4e5720d65200)
# cmdと入力してEnter↓
![image](https://github.com/keimaruO/Speach2cut/assets/91080250/1951292f-c61b-483d-9358-7baff44e9343)

# クソ長コマンド実行
そして以下のコマンドを実行して、環境構築を行います。(下記のコマンドはpipのアップデートからクローン、圧縮ファイルの解凍、インストールに使った不要ファイルの削除まで全部してくれるコマンドです)
    
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && python get-pip.py && git clone https://github.com/keimaruO/Speach2cut.git && cd Speach2cut && python -m pip install --upgrade pip && pip install -r requirements.txt && curl -L https://github.com/yt-dlp/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip -o ffmpeg.zip && curl -L https://github.com/yt-dlp/yt-dlp/releases/download/2023.03.04/yt-dlp.exe -o yt-dlp.exe && tar -xf ffmpeg.zip && move ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe ffmpeg.exe && move ffmpeg-master-latest-win64-gpl\bin\ffplay.exe ffplay.exe && move ffmpeg-master-latest-win64-gpl\bin\ffprobe.exe ffprobe.exe && del ffmpeg.zip && rd /s /q ffmpeg-master-latest-win64-gpl
```

![image](https://github.com/keimaruO/Speach2cut/assets/91080250/a0bb7974-56b5-4ff2-aa43-7ee2a9a2fdf3)

# 使い方
dlurl.txtにURLを貼り付けてCtrl + S(ショートカット)で上書き保存

main.pyをpythonで実行する。

Speach2cutのフォルダでさっきみたいにcmd入力して下記のコマンドで実行できる
```
python main.py
```
初回だけWhisperの字幕モデルのダウンロードがあるので少々時間かかります。

全部の処理が終わったらsozaiフォルダの中にwavが配置されてます。(入れ忘れてるpipなどあったら️🙇‍♂️教えて！)

処理に使用した.srtファイルとwavはsozai/archive/フォルダに保存されてます

sozai/archive/には処理に使用したものをずっと保存させれるが
1.wav,2.wav,3.wav...などのファイルはmain.pyを実行するたびに上書きされるので消えてほしくない人は移動させて管理しとくこと！

Whisperのモデルの変え方はmain.pyの95行目にあるmediumを変更してください、モデルの種類は各自調べて欲しいです。(large-v2が最強だけど処理時間遅、tinyは最速だが精度悪。mediumが妥当、、、？)

# うまくいかない場合

もしANACONDAなどいれててデフォルトのpythonがANCONDAのpythonになってるから厄介

ANACONDA入れてるとpythonの環境変数管理がクソになるので、一度ANACONDAの環境変数を外して通常のpythonで実行すればいけるかもです。

下記のコマンドでpythonがどこにあるか見えるようになります。自分が使いたいpythonに先程の呪文みたいなコマンドを入力すればいけるかもです。
```
where python
```
それでもまだ解決しない場合はChatGPTに聞いて欲しいです。

このSpeach2cutは90%ぐらいChatGPTに書いてもらったやつなのでコード汚いままです

# その他 豆知識的な

python yt-dlp.pyってコマンドに入力してエンター押せば音声だけダウンロードしたい時にも単体で機能するから使えたりもする、yt-dlp.py中にあるの画質設定などのコマンド部分を変えれば普通に動画もいけるしめっちゃ細かく設定できるぜい！yt-dlp.py全文をChatGPTに送って何がしたいが細かく正確に言えば書いてくれる。

Whisperに関してもコマンドプロンプトにwhisper-ctanslate2 [字幕作りたいファイル] --model [好きなの]ってやれば使える
