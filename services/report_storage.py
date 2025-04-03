import json
import os

REPORTS_DIR = "db/reports"

def save_report(report_id, report_data):
    """Save report as a JSON file."""
    os.makedirs(REPORTS_DIR, exist_ok=True)
    file_path = os.path.join(REPORTS_DIR, f"{report_id}.json")
    
    with open(file_path, "w") as f:
        json.dump(report_data, f, indent=4)

def load_report(report_id):
    """Load report from JSON file."""
    file_path = os.path.join(REPORTS_DIR, f"{report_id}.json")
    
    if not os.path.exists(file_path):
        return None
    
    with open(file_path, "r") as f:
        return json.load(f)
