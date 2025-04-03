import pytest
from services.transcriber import transcribe_audio

def test_transcriber_basic():
    transcript = transcribe_audio(open("tests/sample_audio.mp3", "rb"))
    assert isinstance(transcript, str)
    assert len(transcript) > 10
