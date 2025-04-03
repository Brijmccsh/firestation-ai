from fastapi import FastAPI, UploadFile, File
import uuid
from models import IncidentReport
from services.transcriber import transcribe_audio
from services.classifier import classify_incident
from services.report_generator import generate_report as generate_ai_report
from utils.extract_details import extract_details

app = FastAPI()
incident_reports = {}  # Temporary in-memory storage

from pydantic import BaseModel

class TranscriptInput(BaseModel):
    transcript: str

@app.post("/classify/")
async def classify(input_data: TranscriptInput):
    """Classifies incident as '311 Call' or 'Major Incident'."""
    category = classify_incident(input_data.transcript)
    return {"incident_type": category}


@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    transcript = await transcribe_audio(file)  # Correctly await the function
    return {"transcript": transcript}



class ReportRequest(BaseModel):
    transcript: str
    incident_type: str

@app.post("/generate_report/")
async def generate_report(input_data: ReportRequest):
    """Generates a structured incident report."""
    report = generate_ai_report(input_data.transcript, input_data.incident_type)
    return {"generated_report": report}


@app.get("/report/{report_id}")
async def get_report(report_id: str):
    """Retrieves a generated report."""
    return incident_reports.get(report_id, {"error": "Report not found"})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
