from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7613703350:AAGIvRqgsG_yTcOlFADRSYd_FtoLOPwXDKk"
CHAT_ID = "-1002840229810"

@app.route('/')
def index():
    return "✅ Webhook is live and ready."

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    symbol = data.get("symbol", "Unknown")
    price = data.get("price", "N/A")
    alert_type = data.get("alert_type", "Alert")

    message = f"🚨 {alert_type.upper()} Alert\nSymbol: {symbol}\nPrice: {price}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, json=payload)
    print("Telegram response:", response.status_code, response.text)

    return "OK", 200
