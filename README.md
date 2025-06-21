# Nihongo Agent 🇯🇵🧠

A terminal-based AI-powered Japanese language learning agent — 100% local, offline-first, extensible, and beginner-friendly.

I made this for personal use. I want to create a learning portal for me where i go full screen, silent notifactions and use my pad and paper with the model to learn japanese without distraction. To incremently inrease my japanse proficinecy. Which will be made as I go back into the code to update and review with new learning methods and resources. Leaping into project ownership.

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
```
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
