from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7613703350:AAGIvRqgsG_yTcOlFADRSYd_FtoLOPwXDKk'
CHAT_ID = '-1002840229810'

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    message = data.get('message', 'No message received')
    send_telegram(message)
    return 'OK', 200

def send_telegram(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': text}
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
