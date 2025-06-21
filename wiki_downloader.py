import requests
import os

WIKI_API = "https://en.wikipedia.org/w/api.php"
SAVE_DIR = "wiki_articles"

ARTICLES = {
    "Tokyo": "Tokyo",
    "History of Toyota": "Toyota Motor Corporation",
    "History of Sony": "Sony",
    "Japanese automobile industry": "Automotive industry in Japan",
    "Japanese technology": "Technology in Japan"
}

def fetch_wiki_extract(title):
    params = {
        "action": "query",
        "prop": "extracts",
        "explaintext": True,
        "format": "json",
        "titles": title,
        "exintro": False
    }
    response = requests.get(WIKI_API, params=params)
    data = response.json()
    pages = data["query"]["pages"]
    page = next(iter(pages.values()))
    return page.get("extract", "")

def save_article(title, content):
    os.makedirs(SAVE_DIR, exist_ok=True)
    safe_title = title.replace(" ", "_") + ".md"
    with open(os.path.join(SAVE_DIR, safe_title), "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write(content)
    print(f"Saved {title}")

if __name__ == "__main__":
    for key, title in ARTICLES.items():
        content = fetch_wiki_extract(title)
        save_article(title, content)
