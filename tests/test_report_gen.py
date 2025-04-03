import pytest
from services.report_generator import generate_report

def test_report_generation():
    transcript = "Firefighters controlled a small kitchen fire in 15 minutes."
    incident_type = "Major Incident"
    
    report = generate_report(transcript, incident_type)
    assert "Incident Report" in report
    assert "kitchen fire" in report
