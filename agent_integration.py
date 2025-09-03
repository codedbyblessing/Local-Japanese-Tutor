from srs import SRS
from tts_fallback import get_tts_audio
from stt_whisper import transcribe_file

srs = SRS()

def review_session_cli():
    due = srs.get_due_cards(20)
    for c in due:
        print("Q:", c.question)
        ans = input("Your answer (type or press ENTER to provide audio path): ")
        if ans.strip() == "":
            p = input("Path to audio file: ")
            try:
                user_answer = transcribe_file(p, language="ja")
                print("Transcribed:", user_answer)
            except Exception as e:
                print("Transcription failed:", e)
                user_answer = ""
        else:
            user_answer = ans
        print("Correct:", c.answer)
        match = user_answer.strip() == c.answer.strip()
        if match:
            quality = 5
        else:
            try:
                quality = int(input("Rate your recall 0-5: "))
            except Exception:
                quality = 3
        srs.record_review(c.id, quality)
  
        audio = get_tts_audio(c.answer)
        print("TTS audio saved to:", audio)
