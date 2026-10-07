import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(BASE_DIR, "employee_data.json")

def load_data():
    if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
        with open(FILE_NAME, 'r') as f:
            try:
                return json.load(f)
            except FileNotFoundError:
                return {}
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(data):
    with open(FILE_NAME, 'w') as f:
        json.dump(data, f, indent=4)
