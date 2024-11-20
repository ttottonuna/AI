from gtts import gTTS  # gtts 라이브러리의 gTTS 클래스 import
import pygame  # pygame 모듈 import
import speech_recognition as sr  # SpeechRecognition 라이브러리 import하고 sr이라는 별칭으로 사용
import requests  # requests 라이브러리 import
from datetime import datetime  # datetime 모듈의 datetime 클래스 import
import time  # 일정 시간 대기 기능을 위해 time 모듈 import

API_KEY = "5e8a77f0-a667-11ef-b7e6-15a68f653b01b7c1d83b-8f9c-4e88-94cd-a8b10ead7c86"

r = sr.Recognizer()
end = False  # 종료 조건 변수 수정
cnt = 1

while not end:
    with sr.Microphone() as source:
        print("녹음 시작")
        r.adjust_for_ambient_noise(source)  # 주변 소음 조절
        audio = r.listen(source, phrase_time_limit=5)  # 녹음 시간 설정 (5초)
        print("녹음 끝")

    try:
        text = r.recognize_google(audio, language='ko', show_all=True)

        if isinstance(text, dict):  # 텍스트 인식 성공
            text = text['alternative'][0]['transcript']  # 텍스트 추출
            print("인식된 텍스트:", text)
        else:
            print("텍스트를 인식하지 못했습니다.")
            continue  # 텍스트 인식 실패 시 다음 루프로 이동

        url = "https://machinelearningforkids.co.uk/api/scratch/" + API_KEY + "/classify"
        
        response = requests.get(url, params={"data": text})

        if response.ok:
            responseData = response.json()
            topMatch = responseData[0]
        else:
            response.raise_for_status()

        label = topMatch["class_name"]
        confidence = topMatch["confidence"]

        print(f"[인공지능 인식 결과]: {label} {confidence}%")

        if confidence < 60:
            answer = "잘 모르겠어요"
        elif label == "hello":
            answer = "안녕하세요, 반가워요."
        elif label == "time":
            answer = f"지금은 {datetime.now().strftime('%H시 %M분')}입니다."
        elif label == "weather":
            answer = "날씨가 화창해요."
        elif label == "meal":
            answer = "점심으로 제육볶음을 추천해요."
        elif label == "exit":
            answer = "네, 종료할게요."
            end = True

        speech = f"answer{cnt}.mp3"
        tts = gTTS(answer, lang="ko")
        tts.save(speech)

        # pygame을 사용하여 MP3 파일 재생
        pygame.mixer.init()  # pygame 믹서 초기화
        pygame.mixer.music.load(speech)  # 음성 파일 로드
        pygame.mixer.music.play()  # 음성 파일 재생
        while pygame.mixer.music.get_busy():  # 재생이 끝날 때까지 대기
            time.sleep(0.1)

        cnt += 1

    except sr.UnknownValueError:  # 음성 인식 실패
        print("인식 실패")
    except sr.RequestError as e:  # 요청 실패 
        print(f"요청 실패: {e}")
