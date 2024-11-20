from flask import Flask, request, jsonify
from flask_cors import CORS
from gtts import gTTS
import pygame
import speech_recognition as sr
import requests
from datetime import datetime
import time
import os
from pydub import AudioSegment
from pydub.playback import play

app = Flask(__name__)
CORS(app)

API_KEY = "313d7170-a68b-11ef-b7e6-15a68f653b01b0694326-e29d-493f-8384-9d06d4feabd9"

@app.route('/')
def index():
    return "Flask 서버가 실행 중입니다."

@app.route('/interaction/pet', methods=['POST'])
def handle_interaction():
    r = sr.Recognizer()
    cnt = 1
    is_running = True

    while is_running:
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
                continue

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
                answer = "안녕하세요, 저는 무럭이에요."
            elif label == "time":
                answer = f"지금은 {datetime.now().strftime('%H시 %M분')}이에요."
            elif label == "weather":
                answer = "날씨가 화창해요."
            elif label == "meal":
                answer = "점심으로 제육볶음을 추천해요."
            elif label == "exit":
                answer = "네, 종료할게요."
                is_running = False

            os.makedirs("audio", exist_ok=True)
            speech_path = f"audio/answer{cnt}.mp3"
            tts = gTTS(answer, lang="ko")
            tts.save(speech_path)

            # pydub을 사용하여 음성 파일 로드
            sound = AudioSegment.from_file(speech_path)

            # 피치 조절: 8% 빠르게 재생하여 어린이 목소리 효과
            new_sample_rate = int(sound.frame_rate * 1.08)
            high_pitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
            high_pitch_sound = high_pitch_sound.set_frame_rate(44100)

            # 조절된 음성 파일 저장
            modified_speech_path = f"audio/modified_answer{cnt}.mp3"
            high_pitch_sound.export(modified_speech_path, format="mp3")

            # pygame을 사용하여 음성 재생
            pygame.mixer.init()
            pygame.mixer.music.load(modified_speech_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            pygame.mixer.quit()

            cnt += 1

        except sr.UnknownValueError:
            print("인식 실패")
        except sr.RequestError as e:
            print(f"요청 실패: {e}")

    return jsonify({"message": "무럭이와 함께라 행복해요💚"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
