import spacy

# Load Spacy NLP model
nlp = spacy.load("en_core_web_sm")


def extract_details(transcript):
    """Extracts location, time, and responding units from the transcript."""
    doc = nlp(transcript)

    location = ""
    time_of_incident = ""
    responding_units = "Unknown"

    for ent in doc.ents:
        if ent.label_ == "GPE":  # Geopolitical Entity (Location)
            location = ent.text
        elif ent.label_ in ["TIME", "DATE"]:
            time_of_incident = ent.text

    return location, time_of_incident, responding_units
