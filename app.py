from flask import Flask, request, jsonify
import json
from datetime import datetime
import threading
import queue

app = Flask(__name__)

# Background logging queue (non-blocking)
log_queue = queue.Queue()

def background_logger():
    while True:
        log_entry = log_queue.get()
        if log_entry is None:
            break
        with open('alerts.log', 'a') as f:
            f.write(json.dumps(log_entry) + '\n')
        log_queue.task_done()

# Start background thread
threading.Thread(target=background_logger, daemon=True).start()

# Health check (for keep-alive)
@app.route('/health')
def health():
    return "OK", 200

# Fast webhook handler
@app.route('/', methods=['POST'])
@app.route('/webhook', methods=['POST'])
def webhook():
    # Quick validation
    if not request.is_json:
        return jsonify({"status": "error"}), 415
    
    data = request.get_json()
    if not data:
        return jsonify({"status": "error"}), 400

    # Queue for background processing (non-blocking)
    log_queue.put({
        "timestamp": datetime.utcnow().isoformat(),
        "alert": data
    })
    
    # Immediate response
    return jsonify({"status": "queued"}), 202  # 202 Accepted

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
