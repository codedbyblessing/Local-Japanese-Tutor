import requests
import json

def translate_line(text, target_lang="en"):
    text = text.strip().replace('\n', ' ')
    prompt = (
    f"You are a Japanese language tutor. Translate the following sentence into English "
    f"and explain the tone or context of usage if appropriate.\n\n"
    f"Japanese: {text}"
    )

    try:
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": "llama3",
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "stream": True
            },
            stream=True
        )
        response.raise_for_status()

        output = ""
        for line in response.iter_lines():
            if not line:
                continue
            try:
                data = json.loads(line.decode("utf-8"))
                delta = data.get("message", {}).get("content", "")
                output += delta
            except json.JSONDecodeError:
                continue

        return output.strip()

    except Exception as e:
        return f"Error during translation: {e}"

