import whisper
import tempfile
import os

# Choose model size based on available hardware; 'small' is a reasonable default.
MODEL = whisper.load_model(os.getenv("WHISPER_MODEL", "small"))

def transcribe_file(filepath: str, language: str = "ja") -> str:
    result = MODEL.transcribe(filepath, language=language)
    return result.get("text", "").strip()

def transcribe_bytes(audio_bytes: bytes, ext: str = "wav") -> str:
    fd, path = tempfile.mkstemp(suffix=f".{ext}")
    os.close(fd)
    with open(path, "wb") as f:
        f.write(audio_bytes)
    t = transcribe_file(path)
    try:
        os.remove(path)
    except Exception:
        pass
    return t
