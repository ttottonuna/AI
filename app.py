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
import logging
import subprocess

app = Flask(__name__)
CORS(app)

# API 키
API_KEY = "378s9d8d8fefefe234-123b-123123adfff-b7e6-158wdbk226-e29d-hhhh-1212-1hfhehdjwjdkekekkdls23kkdjjf"

# FFmpeg 경로
AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin"


# FFmpeg 및 FFprobe 경로 출력 및 실행 확인
print("FFmpeg 경로:", AudioSegment.converter)
print("FFprobe 경로:", AudioSegment.ffprobe)

subprocess.run([AudioSegment.converter, "-version"], check=True)
subprocess.run([AudioSegment.ffprobe, "-version"], check=True)
try:
    subprocess.run([AudioSegment.converter, "-version"], check=True)
    print("FFmpeg 실행 성공")
except Exception as e:
    print(f"FFmpeg 실행 실패: {e}")

try:
    subprocess.run([AudioSegment.ffprobe, "-version"], check=True)
    print("FFprobe 실행 성공")
except Exception as e:
    print(f"FFprobe 실행 실패: {e}")

# 음성 파일 저장 경로 설정
BASE_DIR = "C:\\KDTmooluckproject\\MooluckAI\\AI\\audio"
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

# 테스트 음성 파일 생성
output_path = os.path.join(BASE_DIR, "test_audio.mp3")
try:
    tts = gTTS("테스트 음성 파일입니다.", lang="ko")
    tts.save(output_path)
    print(f"테스트 음성 파일 생성 완료: {output_path}")
except Exception as e:
    print(f"테스트 음성 파일 생성 실패: {e}")

# 음성 변조 테스트
# 음성 변조 테스트
try:
    input_audio_path = os.path.join(BASE_DIR, "test_audio.mp3")
    output_audio_path = os.path.join(BASE_DIR, "modified_test_audio.mp3")

    # 파일 존재 여부 확인
    if not os.path.exists(input_audio_path):
        raise FileNotFoundError(f"입력 파일을 찾을 수 없습니다: {input_audio_path}")

    print(f"입력 파일 존재 확인: {input_audio_path}")
    sound = AudioSegment.from_file(input_audio_path, format="mp3")
    new_sample_rate = int(sound.frame_rate * 1.08)
    modified_sound = sound._spawn(sound.raw_data, overrides={"frame_rate": new_sample_rate})
    modified_sound = modified_sound.set_frame_rate(44100)

    # 변조된 파일 저장
    modified_sound.export(output_audio_path, format="mp3")
    print(f"변조된 파일 저장 완료: {output_audio_path}")

except FileNotFoundError as e:
    print(f"파일 경로 오류: {e}")
except Exception as e:
    print(f"오류 발생: {e}")

# Flask 애플리케이션 경로 설정
APP_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(APP_BASE_DIR, "audio")
if not os.path.exists(AUDIO_DIR):
    os.makedirs(AUDIO_DIR)

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"서버 에러: {e}")
    return jsonify({"error": str(e)}), 500

@app.route('/')
def index():
    return "Flask 서버가 실행 중입니다."

@app.route('/interaction/pet', methods=['POST'])
def handle_interaction():
    r = sr.Recognizer()
    cnt = 1
    try:
        with sr.Microphone() as source:
            print("녹음 시작")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, phrase_time_limit=5)
            print("녹음 끝")

        try:
            text = r.recognize_google(audio, language='ko', show_all=True)
            if isinstance(text, dict) and text.get('alternative'):
                text = text['alternative'][0]['transcript']
            else:
                return jsonify({"message": "음성을 인식할 수 없습니다."}), 400

            print("인식된 텍스트:", text)
        except sr.UnknownValueError:
            return jsonify({"message": "음성을 이해할 수 없습니다."}), 400
        except sr.RequestError as e:
            return jsonify({"message": f"음성 인식 요청 실패: {e}"}), 500

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

        if confidence < 20:
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

        speech_path = os.path.join(AUDIO_DIR, f"answer{cnt}.mp3")
        tts = gTTS(answer, lang="ko")
        tts.save(speech_path)

        sound = AudioSegment.from_file(speech_path)
        new_sample_rate = int(sound.frame_rate * 1.08)
        high_pitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
        high_pitch_sound = high_pitch_sound.set_frame_rate(44100)
        modified_speech_path = os.path.join(AUDIO_DIR, f"modified_answer{cnt}.mp3")
        high_pitch_sound.export(modified_speech_path, format="mp3")

        pygame.mixer.init()
        try:
            pygame.mixer.music.load(modified_speech_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        finally:
            pygame.mixer.quit()

        cnt += 1
        return jsonify({"message": "응답 완료", "answer": answer,"recognized_text": text})

    except Exception as e:
        logging.error(f"예외 발생: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
