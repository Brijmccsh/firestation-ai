import openai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def classify_incident(transcript):
    """Classifies an incident as '311 Call' or 'Major Incident' using OpenAI."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are an AI fire department assistant. Classify the fire incident strictly as either '311 Call' (minor) or 'Major Incident' (critical emergency). ONLY return one of these two words, nothing else."},
                {"role": "user", "content": transcript}
            ]
        )
        
        # Ensure we only return the classification (strip extra text)
        category = response["choices"][0]["message"]["content"].strip()

        # Validate output, enforce expected values
        if "311 Call" in category:
            return "311 Call"
        elif "Major Incident" in category:
            return "Major Incident"
        else:
            return "Unknown"

    except Exception as e:
        return str(e)
