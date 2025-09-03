import os
import tempfile
import requests
from gtts import gTTS

VOICEVOX_HOST = os.getenv("VOICEVOX_HOST", "http://localhost:50021")

def tts_voicevox(text: str, speaker: int = 1) -> str or None:
    """Try to synthesize speech with a local VoiceVox engine.
    Returns path to WAV file or None if unavailable.
    """
    try:
        q = requests.post(f"{VOICEVOX_HOST}/audio_query", params={"text": text, "speaker": speaker})
        q.raise_for_status()
        query = q.json()
        r = requests.post(f"{VOICEVOX_HOST}/synthesis", params={"speaker": speaker}, json=query, stream=True)
        r.raise_for_status()
        fd, path = tempfile.mkstemp(suffix=".wav")
        os.close(fd)
        with open(path, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
        return path
    except Exception:
        return None

def tts_gtts(text: str, lang: str = "ja") -> str:
    fd, path = tempfile.mkstemp(suffix=".mp3")
    os.close(fd)
    t = gTTS(text=text, lang=lang)
    t.save(path)
    return path

def get_tts_audio(text: str, prefer_voicevox: bool = True) -> str:
    """Return a path to an audio file for the given text.
    Tries VoiceVox first (if prefer_voicevox), then falls back to gTTS.
    Caller is responsible for deleting the temp file when done.
    """
    if prefer_voicevox:
        p = tts_voicevox(text)
        if p:
            return p
    return tts_gtts(text)
