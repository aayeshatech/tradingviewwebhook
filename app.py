from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Health check endpoint (handles GET and HEAD)
@app.route('/', methods=['GET', 'HEAD'])
def health_check():
    if request.method == 'HEAD':
        # Return headers only (no body) for HEAD requests
        return '', 200
    return "Webhook server is running", 200

# Main webhook endpoint
@app.route('/webhook', methods=['POST'])
def webhook():
    # Only parse JSON for POST requests
    if not request.is_json:
        return jsonify({"status": "error", "message": "Invalid JSON"}), 415
    
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "Empty JSON"}), 400

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

# Also handle POST at root path (for TradingView)
@app.route('/', methods=['POST'])
def root_webhook():
    return webhook()  # Delegate to the main webhook handler

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
