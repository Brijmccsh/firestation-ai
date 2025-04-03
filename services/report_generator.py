import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_report(transcript, incident_type):
    """Generates a structured incident report using OpenAI."""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": f"Generate a structured incident report for a {incident_type}. Ensure it meets fire department reporting standards."},
            {"role": "user", "content": transcript}
        ]
    )
    return response["choices"][0]["message"]["content"]

