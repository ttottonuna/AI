import sys
import speech_recognition as sr

# UTF-8 강제 설정
sys.stdout.reconfigure(encoding='utf-8')

r = sr.Recognizer()

with sr.Microphone() as source:
    print("녹음 시작...")
    r.adjust_for_ambient_noise(source, duration=2)  # 주변 소음 조정 시간 설정
    audio = r.listen(source)
    print("녹음 종료")

# 음성 인식 시도
try:
    text = r.recognize_google(audio, language="ko")
    print("음성 인식 결과:", text)

    # 보정된 인식 결과 출력
    custom_words = {"우럭이": "무럭이", "꾸러기": "무럭이"}
    corrected_text = custom_words.get(text, text)
    print("보정된 인식 결과:", corrected_text)

except sr.UnknownValueError:
    print("음성을 인식할 수 없습니다.")
except sr.RequestError as e:
    print(f"API 요청 에러: {e}")
