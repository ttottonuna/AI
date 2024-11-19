from flask import Flask, request, jsonify  # Flask와 관련된 라이브러리 import
from flask_cors import CORS
from gtts import gTTS  # gtts 라이브러리의 gTTS 클래스 import
import pygame  # pygame 모듈 import
import speech_recognition as sr  # SpeechRecognition 라이브러리 import하고 sr이라는 별칭으로 사용
import requests  # requests 라이브러리 import
from datetime import datetime  # datetime 모듈의 datetime 클래스 import
import time  # 일정 시간 대기 기능을 위해 time 모듈 import
import os


app = Flask(__name__)  # Flask 애플리케이션 생성
CORS(app)  # CORS 허용

API_KEY = "5e8a77f0-a667-11ef-b7e6-15a68f653b01b7c1d83b-8f9c-4e88-94cd-a8b10ead7c86"

@app.route('/')
def index():
    return "Flask 서버가 실행 중입니다."

@app.route('/interaction/pet', methods=['POST'])
def handle_interaction():
    r = sr.Recognizer()
    cnt = 1
    is_running = True  # 반복 상태를 관리하는 변수

    while is_running:
        # 음성 녹음 및 인식 시작
        with sr.Microphone() as source:
            print("녹음 시작")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=5)
            print("녹음 끝")

        try:
            text = r.recognize_google(audio, language='ko', show_all=True)
            if isinstance(text, dict):
                text = text['alternative'][0]['transcript']
                print("인식된 텍스트:", text)
            else:
                print("텍스트를 인식하지 못했습니다.")
                continue  # 텍스트를 인식하지 못하면 다음 루프로 이동

            url = f"https://machinelearningforkids.co.uk/api/scratch/{API_KEY}/classify"
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
                is_running = False  # exit 명령이 들어오면 루프 종료

            # 디렉토리 생성 및 파일 경로 설정
            os.makedirs("audio", exist_ok=True)
            speech = f"audio/answer{cnt}.mp3"
            tts = gTTS(answer, lang="ko")
            tts.save(speech)

            # 음성 재생 및 pygame 리소스 해제
            pygame.mixer.init()
            pygame.mixer.music.load(speech)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            pygame.mixer.quit()  # pygame 리소스 해제

            cnt += 1

        except sr.UnknownValueError:
            print("인식 실패")
        except sr.RequestError as e:
            print(f"요청 실패: {e}")

    return jsonify({"message": "음성 인식이 종료되었습니다."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
