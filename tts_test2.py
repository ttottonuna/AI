from gtts import gTTS
from pydub import AudioSegment
from playsound import playsound

# 음성 생성
text = "할머니, 물주세요"
speech = "tts.mp3"
tts = gTTS(text, lang="ko")
tts.save(speech)

# 피치 조정
audio = AudioSegment.from_file(speech)
# 피치를 높여 초등학생 목소리 느낌으로
higher_pitch_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * 1.2)})
higher_pitch_audio = higher_pitch_audio.set_frame_rate(audio.frame_rate)  # 원래 프레임 레이트로 설정
higher_pitch_audio.export("higher_pitch_tts.mp3", format="mp3")

# 재생
playsound("higher_pitch_tts.mp3")
