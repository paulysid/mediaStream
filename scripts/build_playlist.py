from pathlib import Path


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


def keep_entry(entry: list[str]) -> bool:
    text = " ".join(entry).lower()
    has_language_marker = any(marker in text for marker in LANGUAGE_MARKERS)
    is_nsfw = any(marker in text for marker in NSFW_MARKERS)
    return not has_language_marker or is_nsfw


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
            if keep_entry(entry):
                playlist.extend(entry)
            index = end

    Path("index.m3u").write_text("\n".join(playlist) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build_playlist()
