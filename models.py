from pydantic import BaseModel


class IncidentReport(BaseModel):
    id: str
    incident_type: str
    severity: str  # "311 Call" or "Major Incident"
    location: str
    responding_units: str
    time_of_incident: str
    summary: str
    generated_report: str
