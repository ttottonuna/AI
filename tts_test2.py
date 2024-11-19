from gtts import gTTS
from playsound import playsound

text = "할머니, 물주세요"
speech = "tts.mp3"
tts = gTTS(text, lang="ko")
tts.save(speech)
playsound(speech)

