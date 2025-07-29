# filename: webhook_server.py

from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7613703350:AAGIvRqgsG_yTcOlFADRSYd_FtoLOPwXDKk'
CHAT_ID = '-1002840229810'

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    message = data.get('message', 'No message received.')
    
    # Send Telegram message
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    r = requests.post(url, json=payload)
    
    return {'status': 'ok', 'telegram_response': r.json()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
