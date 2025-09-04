import gradio as gr
import os
import random
from furigana import furigana_html
from tts_fallback import get_tts_audio
from srs import SRS

# ---------- Initialize database ----------
srs = SRS("sqlite:///srs.db")

# ---------- YouTube videos (tested embeddable) ----------
youtube_videos = [
    # "https://www.youtube.com/embed/WOJkfMCtyNc",
    # "https://www.youtube.com/embed/1HgdtHkiZwg",
    # "https://www.youtube.com/embed/18mIwPU2BFs",
    # "https://www.youtube.com/embed/7bmngRoiMRg",
    # "https://www.youtube.com/embed/8VUXKBycFc0"
   "https://www.youtube.com/embed/sXrPeHS-WZE",
    "https://www.youtube.com/embed/3tDrX8CDcaI",
    "https://www.youtube.com/embed/9MUzBZVUtS4",
    "https://www.youtube.com/embed/jcftjN3XXJA",
    "https://www.youtube.com/embed/sdpeVDTPzEc",
    "https://www.youtube.com/embed/qKJDWD_l4PQ",
    "https://www.youtube.com/embed/4EqljICUnGg",
    "https://www.youtube.com/embed/Hl6nBH6Gwtg",
    "https://www.youtube.com/embed/WcT_6FbwQco",
    "https://www.youtube.com/embed/uLT9TtgGwdI"


]


# ---------- Helper Functions ----------

def get_random_cartoon():
    """Return a responsive iframe HTML for a random cartoon video."""
    video_url = random.choice(youtube_videos)
    embed_html = f"""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
        <iframe src="{video_url}" 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                allowfullscreen>
        </iframe>
    </div>
    """
    return embed_html

# ---------- Core Functions ----------
def render_with_tts_and_cartoon(text: str):
    try:
        html = furigana_html(text)
        audio_path = get_tts_audio(text)
        cartoon = get_random_cartoon()
        return html, audio_path, cartoon
    except Exception as e:
        error_msg = f"<p style='color:red;'>Error: {e}</p>"
        return error_msg, None, None

def add_card(question: str, answer: str):
    try:
        c = srs.add_card(question, answer)
        return f"✅ Card added! ID: {c.id}"
    except Exception as e:
        return f"❌ Error adding card: {e}"

def get_due(limit: int = 10):
    try:
        cards = srs.get_due_cards(limit)
        return [[c.id, c.question, c.answer] for c in cards]
    except Exception:
        return []

def review_card(card_id: int, quality: int):
    try:
        card = srs.record_review(card_id, quality)
        return f"Card ID {card.id} reviewed. Next due: {card.due}"
    except Exception as e:
        return f"❌ Error reviewing card: {e}"

# ---------- Gradio UI ----------
with gr.Blocks(title="Nihongo Agent — Furigana + TTS + Flashcards + Cartoons") as demo:
    gr.Markdown("# Nihongo Agent — Furigana + TTS + Flashcards + Cute Cartoons")

    with gr.Row():
        # ---------- Left Column: Input & Flashcards ----------
        with gr.Column(scale=2):
            gr.Markdown("### Enter Japanese text to see Furigana + listen to TTS")
            inp = gr.Textbox(label="日本語の文章を入力", placeholder="例: 私は毎朝新聞を読みます。", lines=3)
            render_btn = gr.Button("Render + TTS")

            gr.Markdown("### Flashcard Manager")
            add_q = gr.Textbox(label="Flashcard question (JP)")
            add_a = gr.Textbox(label="Flashcard answer (EN or JP)")
            add_btn = gr.Button("Add flashcard")
            status_add = gr.Textbox(label="Status", interactive=False)
            add_btn.click(fn=add_card, inputs=[add_q, add_a], outputs=status_add)
            
            due_btn = gr.Button("Get due cards")
            due_list = gr.Dataframe(headers=["ID", "Question", "Answer"], datatype=["number", "str", "str"])
            due_btn.click(fn=get_due, outputs=due_list)
            
            with gr.Row():
                review_id = gr.Number(label="Card ID to review")
                easy_btn = gr.Button("Easy")
                medium_btn = gr.Button("Medium")
                hard_btn = gr.Button("Hard")
                review_status = gr.Textbox(label="Review Status", interactive=False)
                easy_btn.click(fn=lambda cid: review_card(cid, 5), inputs=review_id, outputs=review_status)
                medium_btn.click(fn=lambda cid: review_card(cid, 3), inputs=review_id, outputs=review_status)
                hard_btn.click(fn=lambda cid: review_card(cid, 1), inputs=review_id, outputs=review_status)

        # ---------- Right Column: Output ----------
        with gr.Column(scale=3):
            out_html = gr.HTML()
            out_audio = gr.Audio(label="TTS audio", type="filepath", interactive=False, autoplay=True)
            
            # Cute Cartoons
            cartoon_html = gr.HTML()
            random_cartoon_btn = gr.Button("Show Random Cartoon")
            random_cartoon_btn.click(fn=get_random_cartoon, inputs=None, outputs=cartoon_html)

    # Render TTS + Cartoon together
    render_btn.click(fn=render_with_tts_and_cartoon, inputs=inp, outputs=[out_html, out_audio, cartoon_html])

# ---------- Launch ----------
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")  # picks an available port automatically
