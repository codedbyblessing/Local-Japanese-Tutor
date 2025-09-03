import gradio as gr
import os
from furigana import furigana_html
from tts_fallback import get_tts_audio
from srs import SRS
import tempfile

srs = SRS("sqlite:///srs.db")

def render_with_tts(text: str):
    html = furigana_html(text)
    audio_path = get_tts_audio(text)
    return html, audio_path


def add_card(question: str, answer: str):
    c = srs.add_card(question, answer)
    return {"status": "ok", "id": c.id}

def get_due(limit: int = 10):
    cards = srs.get_due_cards(limit)
    payload = []
    for c in cards:
        payload.append({"id": c.id, "question": c.question, "answer": c.answer})
    return payload

def review_card(card_id: int, quality: int):
    card = srs.record_review(card_id, quality)
    return {"id": card.id, "due": str(card.due)}

with gr.Blocks(title="Nihongo Agent — Furigana + TTS + Flashcards") as demo:
    gr.Markdown("# Nihongo Agent — Furigana + TTS + Flashcards (local)")
    with gr.Row():
        with gr.Column(scale=2):
            inp = gr.Textbox(label="日本語の文章を入力", placeholder="例: 私は毎朝新聞を読みます。", lines=3)
            render_btn = gr.Button("Render + TTS")
            add_q = gr.Textbox(label="Flashcard question (JP)")
            add_a = gr.Textbox(label="Flashcard answer (EN or JP)")
            add_btn = gr.Button("Add flashcard")
            due_btn = gr.Button("Get due cards")
        with gr.Column(scale=3):
            out_html = gr.HTML()
            out_audio = gr.Audio(label="TTS audio", type="filepath")
            due_list = gr.JSON()

    render_btn.click(fn=render_with_tts, inputs=inp, outputs=[out_html, out_audio])
    add_btn.click(fn=add_card, inputs=[add_q, add_a], outputs=None)
    due_btn.click(fn=get_due, outputs=due_list)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", 7860)))
