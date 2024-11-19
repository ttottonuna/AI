from gtts import gTTS
from playsound import playsound
from pydub import AudioSegment

text = "안녕하세요"
speech_mp3 = "tts.mp3"
speech_wav = "tts.wav"

# TTS 생성 및 mp3로 저장
tts = gTTS(text, lang="ko")
tts.save(speech_mp3)

# mp3를 wav로 변환 (FFmpeg 없이도 가능)
audio = AudioSegment.from_mp3(speech_mp3)
audio.export(speech_wav, format="wav")

# wav 파일 재생
playsound(speech_wav)
