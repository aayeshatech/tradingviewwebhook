from flask import Flask, request
import requests

app = Flask(__name__)

# ✅ Ensure this is your actual working bot token
BOT_TOKEN = "7613703350:AAEDKBLlNqjqQPfoe892_t_dSfuPjExppPs"
CHAT_ID = "-1002840229810"  # ✅ Your Telegram group ID

@app.route('/')
def index():
    return "Webhook is live!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received data:", data)  # Optional for debug

    symbol = data.get("symbol", "Unknown")
    price = data.get("price", "N/A")
    alert_type = data.get("alert_type", "Alert")

    message = f"🚨 {alert_type.upper()} Alert\nSymbol: {symbol}\nPrice: {price}"

    # ✅ Telegram message post
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    # Send the Telegram message
    response = requests.post(url, json=payload)

    # Log Telegram response
    print("Telegram response:", response.status_code, response.text)

    return "OK", 200
