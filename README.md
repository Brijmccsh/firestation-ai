# Fire Station AI – Incident Report Automation  

This project automates the process of generating fire station incident reports. Instead of writing reports manually, firefighters can provide a voice summary, and the system will transcribe, classify, and generate a structured report.  

## How It Works  

1. A firefighter records a spoken summary of the incident.  
2. The system converts the audio into text.  
3. AI classifies the incident as either a "311 Call" (minor) or a "Major Incident" (critical emergency).  
4. A structured report is generated automatically, including key details.  
5. The report is stored for review or integration with other fire department systems.  

## Features  

- Converts firefighter voice summaries into text using speech-to-text models.  
- Classifies incidents to determine report complexity.  
- Automatically generates reports based on structured templates.  
- Stores reports in a database for easy retrieval.  

## Setup  

1. Install dependencies: 
2. Run the server:  

3. Test the API using `curl` or Postman.  

## API Endpoints  

- `POST /transcribe/` → Upload an audio file to convert it into text.  
- `POST /classify/` → Classifies the incident as "311 Call" or "Major Incident."  
- `POST /generate_report/` → Generates a structured incident report.  
- `GET /report/{report_id}` → Retrieves a previously generated report.  

 

