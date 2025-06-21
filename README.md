# Nihongo Agent 🇯🇵🧠

Japanese Language Learning Agent – Personal Project (Python, LLMs, CLI), 100% local, offline-first, extensible, and beginner-friendly.
- Built a terminal-based Japanese language tutor using local LLaMA-based models with Ollama
- Integrated dictionary lookup (JMdict), translation via local LLM inference, and Kana quiz games
- Designed modular Python code handling grammar references, cultural context, and CLI interaction
- Applied prompt engineering, caching strategies, and model streaming output handling


In addition to personal use, I aim to incorporate scientific learning methods behind updates to test them out on myself.


## 🌟 Features
- 🎴 Hiragana & Katakana typing games
- 🈳 Vocabulary flashcards (JLPT levels)
- 📖 Traditional Japanese short stories
- 🖌️ Kanji stroke order explanations
- 🧠 Grammar & culture review (markdown powered)
- 🧩 Interactive trivia games (Tokyo culture, tech history)
- 💬 LLM chat support using Ollama (LLaMA3)

## Commands

- `lookup` — Lookup words in local dictionary  
- `translate` — Translate Japanese text via local Ollama LLM  
- `grammar` — Show grammar points 
- `kana-game` — Play kana typing quiz  
- `help` — Show commands  
- `exit` — Quit  

## 🚀 Getting Started
1. Install Python 3.8+
2. [Install Ollama](https://ollama.com)
3. Clone this repo
4. Run the agent:

```bash
python agent.py
or on some terminals like mine, python3 works instead

## 🌐 3. **Future improvements**

| Step | Goal                                | Tool Suggestions                   |
|------|-------------------------------------|------------------------------------|
| 1    | Update files weekly                 | Flask / FastAPI                    |
| 2    | Wrap CLI logic in a REST API        | Flask / FastAPI                    |
| 3    | Build a UI for games & stories      | React (with Tailwind)              |
| 4    | Connect Ollama to backend           | Use local API (already done)       |
| 5    | Host static frontend                | GitHub Pages / Vercel              |
| 6    | Bundle as a PWA for offline use     | Service Workers + Webpack          |

---

## License

MIT License  
Powered by Ollama
Stories from Aozora Bunko
Stroke data adapted from KanjiVG
