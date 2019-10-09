- 安装ffmpeg

`apt-get install ffmpeg libavcodec-extra
`
- 安装pybud

`pip install pydub` 

- mp3 转 aac
```python
from pydub import AudioSegment

mp3_file_path = "/tmp/audio.mp3"
aac_file_path = "/tmp/audio.aac"

song = AudioSegment.from_mp3(mp3_file_path)
song.export(aac_file_path, "adts")
```

#### 运行py代码，提示：FileNotFoundError: [Errno 2] No such file or directory: 'xdg-open' 
apt install xdg-utils

