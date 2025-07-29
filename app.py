from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7613703350:AAGIvRqgsG_yTcOlFADRSYd_FtoLOPwXDKk'
CHAT_ID = '-1002840229810'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, json=payload)
    print("Telegram response:", response.status_code, response.text)
    return response

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json()
    print("Received TradingView alert:", data)
    message = data.get('message', 'No message received')
    send_telegram_message(message)
    return {'status': 'success'}, 200

if __name__ == '__main__':
    app.run(port=8080)
