import sys
import speech_recognition as sr

# UTF-8 강제 설정
sys.stdout.reconfigure(encoding='utf-8')

r = sr.Recognizer()

# 마이크로 음성 입력 받기
with sr.Microphone() as source:
    print("녹음 시작...")
    r.adjust_for_ambient_noise(source)  # 주변 소음에 맞춰 마이크 감도 조정
    audio = r.listen(source)
    print("녹음 종료")

# 음성 인식 시도
try:
    text = r.recognize_google(audio, language="ko")
    print("음성 인식 결과:", text)
except sr.UnknownValueError:
    print("음성을 인식할 수 없습니다.")
except sr.RequestError as e:
    print(f"API 요청 에러: {e}")
