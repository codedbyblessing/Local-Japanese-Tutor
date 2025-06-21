import json
import random

def kana_game():
    try:
        with open("kana_hiragana.json", "r", encoding="utf-8") as f:
            kana_list = json.load(f)
    except FileNotFoundError:
        print("Kana data file not found.")
        return

    print("Kana Typing Game (Hiragana) - Type the romaji for the kana shown")
    score = 0
    for _ in range(10):
        item = random.choice(kana_list)
        kana = item["kana"]
        romaji = item["romaji"]
        answer = input(f"What is the romaji for '{kana}'? ").strip().lower()
        if answer == romaji:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer is {romaji}")
    print(f"Game over! Your score: {score}/10")
