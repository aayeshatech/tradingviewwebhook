from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7613703350:AAEDKBLlNqjqQPfoe892_t_dSfuPjExppPs"
CHAT_ID = "-1002840229810"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    requests.post(url, data=payload)

@app.route("/alert", methods=["POST"])
def receive_alert():
    data = request.json
    message = data.get("message", "🚨 Alert Received")
    send_telegram_message(message)
    return {"status": "sent"}

if __name__ == "__main__":
    app.run(port=8080)
