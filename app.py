from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Health check endpoint
@app.route('/health')
def health():
    return "OK", 200

# Main webhook endpoint (handles both root and /webhook)
@app.route('/', methods=['GET', 'POST'])
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'GET':
        return "Webhook server is running", 200
        
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "Invalid JSON"}), 400

    # Process alert
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "alert": data
    }
    
    # Save to file
    with open('alerts.log', 'a') as f:
        f.write(json.dumps(log_entry) + '\n')
    
    print(f"Processed alert: {data}")
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
