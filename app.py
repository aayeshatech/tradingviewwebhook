from flask import Flask, request
import requests

app = Flask(__name__)

# Replace with your bot token and group/chat ID
BOT_TOKEN = '7613703350:AAGIvRqgsG_yTcOlFADRSYd_FtoLOPwXDKk'
CHAT_ID = '-1002840229810'  # Group ID or user ID

# === Telegram Sender ===
def send_telegram(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': text,
        'parse_mode': 'HTML'
    }
    response = requests.post(url, data=payload)
    print(f"Telegram response: {response.status_code} {response.text}")

# === Webhook endpoint ===
@app.route('/', methods=['POST'])
def webhook():
    try:
        data = request.json
        print(f"Received data: {data}")
        message = data.get('message', '🚨 Alert Received, but no "message" field!')
        send_telegram(message)
        return '✅ Alert received and forwarded to Telegram.', 200
    except Exception as e:
        print(f"Error: {e}")
        return '❌ Failed to process webhook.', 500

# === Run Flask App ===
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
