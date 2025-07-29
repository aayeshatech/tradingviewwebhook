# filename: app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json()

    message = data.get("message")
    bot_token = data.get("token")
    chat_id = data.get("chat_id")

    if not all([message, bot_token, chat_id]):
        return jsonify({"error": "Missing fields"}), 400

    send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(send_url, data=payload)

    if response.status_code == 200:
        return jsonify({"status": "sent"}), 200
    else:
        return jsonify({"error": "Telegram API error", "details": response.text}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
