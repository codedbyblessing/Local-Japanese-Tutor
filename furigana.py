from typing import List
import html
import re

try:
    from fugashi import Tagger # type: ignore
except Exception as e:
    raise RuntimeError("Please install fugashi[unidic-lite]: pip install 'fugashi[unidic-lite]'") from e

try:
    import pykakasi
except Exception as e:
    raise RuntimeError("Please install pykakasi: pip install pykakasi") from e

_tagger = Tagger()
_kks = pykakasi.kakasi()

_kana_re = re.compile(r'^[\\u3040-\\u309F\\u30A0-\\u30FFー]+$')

def _to_hiragana(s: str) -> str:
    conv = _kks.convert(s)
    if not conv:
        return s
    hira = "".join(item.get("hira", item.get("kana", item.get("orig", ""))) for item in conv)
    return hira

def token_has_only_kana(s: str) -> bool:
    return bool(_kana_re.match(s))

def make_ruby(word: str, reading: str) -> str:
    word_esc = html.escape(word)
    reading_esc = html.escape(reading)
    if token_has_only_kana(word) or word == reading or reading == "":
        return word_esc
    return f"<ruby>{word_esc}<rt>{reading_esc}</rt></ruby>"

def furigana_html(sentence: str) -> str:
    tokens = list(_tagger(sentence))
    parts: List[str] = []
    for tok in tokens:
        surface = tok.surface
        hira = _to_hiragana(surface)
        parts.append(make_ruby(surface, hira))
    html_out = "".join(parts)
    return html_out

if __name__ == "__main__":
    s = "私は毎朝新聞を読みます。"
    print(furigana_html(s))
