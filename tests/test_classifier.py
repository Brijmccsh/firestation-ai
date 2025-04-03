import pytest
from services.classifier import classify_incident

def test_classifier_major_incident():
    transcript = "Firefighters rescued a trapped individual from a burning house."
    classification = classify_incident(transcript)
    assert classification == "Major Incident"

def test_classifier_311_call():
    transcript = "Firefighters assisted in a minor gas leak."
    classification = classify_incident(transcript)
    assert classification == "311 Call"
