import whisper
import tempfile
import numpy as np
import torch
import soundfile as sf

model = whisper.load_model("base")

async def transcribe_audio(file):
    """Transcribes firefighter voice summary using Whisper AI."""
    try:
        # Read file asynchronously
        audio_data = await file.read()

        # Save to a temporary file
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as temp_audio:
            temp_audio.write(audio_data)  # Save the MP3 data
            temp_audio.flush()  # Ensure file is written

            # Transcribe using Whisper
            result = model.transcribe(temp_audio.name)

        return result["text"]
    except Exception as e:
        return str(e)
