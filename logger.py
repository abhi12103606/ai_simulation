import json
from datetime import datetime

def log_event(event):
    event["timestamp"] = str(datetime.now())
    print(json.dumps(event, indent=2))
