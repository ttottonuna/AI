import speech_recognition as sr
from playsound import playsound

r = sr.Recognizer()
with sr.Microphone() as source:
    print("녹음시작")
    audio = r.record(source, duration=5)
    print("녹음끝")

file_name = "voice.wav"
with open(file_name, "wb") as f:
    f.write(audio.get_wav_data())

playsound(file_name)


# import speech_recognition as sr
# from pydub import AudioSegment
# from pydub.playback import play

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("녹음시작")
#     audio = r.record(source, duration=5)
#     print("녹음끝")

# # 파일 저장
# file_name = "voice.wav"
# with open(file_name, "wb") as f:
#     f.write(audio.get_wav_data())

# # 오디오 파일 재생
# sound = AudioSegment.from_wav(file_name)
# play(sound)
