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
        'parse_mode': 'Markdown'
    }
    return requests.post(url, data=payload)

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    message = f"📩 *TradingView Alert Received:*\n\n{data.get('ticker', 'N/A')} | {data.get('price', 'N/A')}\n\n{data.get('message', str(data))}"
    send_telegram_message(message)
    return {'status': 'ok'}, 200

@app.route('/', methods=['GET'])
def home():
    return "✅ TradingView Webhook is Live", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
