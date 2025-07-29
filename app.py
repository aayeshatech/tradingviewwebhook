from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    try:
        data = request.get_json()
        print("Received:", data)

        message = data.get("message")
        token = data.get("token")
        chat_id = data.get("chat_id")

        if not all([message, token, chat_id]):
            return jsonify({"error": "Missing message, token or chat_id"}), 400

        telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "HTML"
        }

        tg_response = requests.post(telegram_url, json=payload)
        print("Telegram response:", tg_response.text)

        return jsonify({"status": "success", "telegram_response": tg_response.json()})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/', methods=['GET'])
def home():
    return "🔔 TradingView Telegram Webhook is Running"

if __name__ == '__main__':
    app.run(debug=True)
