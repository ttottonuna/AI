import eventlet
eventlet.monkey_patch()
import requests

from flask import Flask, request
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta



app = Flask(__name__)
CORS(app)

#flask 구동 확인
@app.route('/')
def home():
    return 'Hello, World!'

#알림 작동 확인 엔드포인트
@app.route('/trigger-notification', methods=['GET','POST'])
def trigger_notification():
    send_notifications()
    return {'status': 'notification sent'}


# 클라이언트의 알림 수신을 위한 엔드포인트
clients = []

@app.route('/register', methods=['POST'])
def register():
    client_url = request.json.get('url')
    if client_url not in clients:
        clients.append(client_url)
    return {'status': 'registered'}

def send_notifications():
    for client in clients:
        try:
            requests.post(client, json={'message': '할머니, 물주세요'})
        except Exception as e:
            print(f"Failed to send notification to {client}: {e}")

# if __name__ == '__main__':
#     scheduler = BackgroundScheduler(timezone='Asia/Seoul')
#     scheduler.add_job(send_notifications, 'cron', hour=8, minute=0)
#     scheduler.start()
#     app.run(debug=True)

if __name__ == '__main__':
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    # 현재 시간으로부터 1분 후에 작업 실행
    run_time = datetime.now() + timedelta(minutes=1)
    scheduler.add_job(send_notifications, 'date', run_date=run_time)
    scheduler.start()
    app.run(debug=True)
