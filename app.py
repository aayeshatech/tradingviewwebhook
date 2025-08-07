# requirements.txt additions
redis==5.0.1
celery==5.3.4

# app.py
from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def process_alert(data):
    # Heavy processing here
    with open('alerts.log', 'a') as f:
        f.write(json.dumps(data) + '\n')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    process_alert.delay(data)  # Async processing
    return jsonify({"status": "queued"}), 202
