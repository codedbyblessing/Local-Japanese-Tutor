import json
import os

class LocalDictionary:
    def __init__(self, dict_path="local_dict.json"):
        if not os.path.exists(dict_path):
            raise FileNotFoundError(f"{dict_path} not found. Please add your local dictionary JSON.")
        with open(dict_path, "r", encoding="utf-8") as f:
            self.dictionary = json.load(f)

    def lookup(self, word):
        entry = self.dictionary.get(word)
        if entry:
            return entry

        for k, v in self.dictionary.items():
            if word.lower() in k.lower() or word.lower() in v.get("reading", "").lower():
                return v
        return None
    def lookup_english(self, english_term):
        results = []
        term_lower = english_term.lower()
        for word, entry in self.dictionary.items():
            for sense in entry.get("senses", []):
                glosses = [g.lower() for g in sense.get("glosses", [])]
                if any(term_lower in gloss for gloss in glosses):
                    results.append((word, entry))
                    break
        return results

