import xml.etree.ElementTree as ET
import json

def parse_jmdict(xml_path, json_path="local_dict.json"):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    dictionary = {}

    for entry in root.findall('entry'):
        word = None
        reading = None
        senses = []

        kebs = [keb.text for keb in entry.findall('k_ele/keb')]
        rebs = [reb.text for reb in entry.findall('r_ele/reb')]

        word = kebs[0] if kebs else (rebs[0] if rebs else None)
        reading = rebs[0] if rebs else None

        for sense in entry.findall('sense'):
            glosses = [gloss.text for gloss in sense.findall('gloss')]
            parts_of_speech = [pos.text for pos in sense.findall('pos')]
            senses.append({
                "glosses": glosses,
                "parts_of_speech": parts_of_speech
            })

        if word:
            dictionary[word] = {
                "reading": reading,
                "senses": senses
            }

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)

    print(f"Converted {len(dictionary)} entries to {json_path}")

if __name__ == "__main__":
    xml_path = "JMdict_e"  # Adjust if your filename differs
    parse_jmdict(xml_path)
