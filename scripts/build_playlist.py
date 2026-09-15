from pathlib import Path
import re


LANGUAGE_MARKERS = (
    "arabic",
    "spanish",
    "espanol",
    "french",
    "francais",
    "german",
    "deutsch",
    "italian",
    "portuguese",
    "brazilian",
    "turkish",
    "turkiye",
    "arabia",
    "hindi",
    "urdu",
    "bengali",
    "bangla",
    "punjabi",
    "tamil",
    "telugu",
    "malayalam",
    "marathi",
    "gujarati",
    "kannada",
    "mandarin",
    "cantonese",
    "chinese",
    "japanese",
    "korean",
    "polish",
    "polska",
    "romanian",
    "ukrainian",
    "russian",
    "greek",
    "hebrew",
    "persian",
    "farsi",
    "pashto",
    "indonesian",
    "malay",
    "thai",
    "vietnamese",
    "filipino",
    "tagalog",
    "swahili",
)

NSFW_MARKERS = ("nsfw", "xxx", "adult", "porn", "sex")
RELIGIOUS_MARKERS = (
    "allah",
    "bible",
    "buddh",
    "church",
    "christian",
    "christ",
    "evangel",
    "gospel",
    "hindu",
    "islam",
    "jesus",
    "jewish",
    "judaism",
    "koran",
    "mosque",
    "muslim",
    "prayer",
    "quran",
    "religious",
    "temple",
    "torah",
    "worship",
)
ENGLISH_SOURCE_COUNTRIES = {"au", "ca", "gb", "ie", "nz", "uk", "us"}
INTERNATIONAL_ENGLISH_MARKERS = (
    "bbc",
    "bloomberg",
    "cnn",
    "dw english",
    "euronews english",
    "france 24 english",
    "nhk world",
    "sky news",
    "world news",
)


def keep_entry(entry: list[str], source_name: str) -> bool:
    text = entry[0].lower()
    has_language_marker = any(marker in text for marker in LANGUAGE_MARKERS)
    has_religious_marker = any(marker in text for marker in RELIGIOUS_MARKERS)
    is_nsfw = any(
        re.search(rf"(?<![a-z0-9]){re.escape(marker)}(?![a-z0-9])", text)
        for marker in NSFW_MARKERS
    )
    source_country = source_name.split("_", 1)[0]
    is_english_source = source_country in ENGLISH_SOURCE_COUNTRIES
    is_international_english = any(marker in text for marker in INTERNATIONAL_ENGLISH_MARKERS)
    return not has_religious_marker and (is_nsfw or (
        not has_language_marker
        and (is_english_source or is_international_english)
    ))


def build_playlist() -> None:
    playlist = ["#EXTM3U"]
    for source in sorted(Path("streams").glob("*.m3u")):
        lines = source.read_text(encoding="utf-8", errors="replace").splitlines()
        index = 0
        while index < len(lines):
            if not lines[index].startswith("#EXTINF"):
                index += 1
                continue

            end = index + 1
            while end < len(lines) and not lines[end].startswith("#EXTINF"):
                end += 1

            entry = lines[index:end]
            if keep_entry(entry, source.stem):
                playlist.extend(entry)
            index = end

    Path("index.m3u").write_text("\n".join(playlist) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_playlist()
