import sys
from local_dictionary import LocalDictionary
from translate import translate_line
from wiki_downloader import fetch_wiki_extract, save_article
import games

def print_help():
    print("""
List of commands to start learning:
  lookup           - Lookup a word in the local dictionary
  translate        - Translate a Japanese line using Ollama
  grammar          - Read grammar points
  kana-game        - Play kana typing game
  help             - Show this help
  exit             - Exit the program
""")


def main():
    local_dict = LocalDictionary("local_dict.json")

    print("👋 Welcome to Nihongo Agent — your offline Japanese learning assistant!")
    print_help()

    while True:
        cmd = input("📝 What would you like to do? ").strip()

        if cmd == "exit":
            print("👋 Goodbye! Happy learning!")
            break

        elif cmd == "help":
            print_help()

        elif cmd == "lookup":
            word = input("🔍 Enter Japanese word or reading: ").strip()
            entry = local_dict.lookup(word)
            if entry:
                print(f"\n📖 Word: {word}")
                print(f"📝 Reading: {entry.get('reading', 'N/A')}")
                print("💬 Meanings:")
                for sense in entry.get("senses", []):
                    glosses = sense.get("glosses", [])
                    print("  - " + ", ".join(glosses))
            else:
                print("❌ Word not found.")

        elif cmd == "translate":
            text = input("✍️ Enter Japanese text to translate: ").strip()
            if not text:
                print("⚠️  No input provided.")
            else:
                translation = translate_line(text)
                print("\n🗣️ Translation:\n" + translation)

        elif cmd == "grammar":
            try:
                with open("grammar_points.md", "r", encoding="utf-8") as f:
                    print("\n" + f.read())
            except FileNotFoundError:
                print("❌ Grammar file not found.")

        elif cmd == "kana-game":
            games.kana_game()

        else:
            print("❓ Unknown command. Type 'help' to see the menu.")

        # Ask user if they want to continue
        again = input("\n💡 Would you like help with anything else? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("👋 Alright, see you next time!")
            break
        elif cmd == "lookup-en":
            eng_term = input("Enter English word to lookup: ").strip()
            results = local_dict.lookup_english(eng_term)
            if results:
                for word, entry in results:
                    print(f"\nJapanese word: {word}")
                    print(f"Reading: {entry.get('reading', 'N/A')}")
                    print("Meanings:")
                    for sense in entry.get("senses", []):
                        print(" - " + ", ".join(sense.get("glosses", [])))
            else:
                print("No Japanese words found for that English term.")


if __name__ == "__main__":
    main()
