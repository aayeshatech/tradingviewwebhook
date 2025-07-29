from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.get_json()
    message = data.get("message")
    token = data.get("token")
    chat_id = data.get("chat_id")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    response = requests.post(url, json=payload)
    return {"status": "sent", "telegram_response": response.json()}

if __name__ == "__main__":
    app.run(port=8080)
