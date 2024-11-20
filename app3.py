from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
import io

app = Flask(__name__, static_folder='static')
CORS(app)
recognizer = sr.Recognizer()

@app.route('/api/stt', methods=['POST'])
def stt():
    audio_file = request.files['file']
    # 오디오 파일을 AudioSegment로 로드
    audio = AudioSegment.from_file(audio_file)
    # 오디오를 WAV 형식으로 변환
    wav_io = io.BytesIO()
    audio.export(wav_io, format="wav")
    wav_io.seek(0)
    # 변환된 오디오를 speech_recognition에서 처리
    with sr.AudioFile(wav_io) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="ko-KR")
            return jsonify({'text': text})
        except sr.UnknownValueError:
            return jsonify({'error': '음성을 이해할 수 없습니다.'}), 400
        except sr.RequestError:
            return jsonify({'error': 'STT 서비스에 접근할 수 없습니다.'}), 500

@app.route('/api/tts', methods=['GET','POST'])
def generate_tts():
    data = request.json
    text = data.get('text')
    if not text:
        return jsonify({'error': '텍스트가 제공되지 않았습니다.'}), 400
    tts = gTTS(text=text, lang='ko')
    tts_file = "output.mp3"
    tts.save(tts_file)
    return send_file(tts_file, mimetype="audio/mpeg", as_attachment=True, download_name=tts_file)

if __name__ == '__main__':
    app.run(debug=True)
