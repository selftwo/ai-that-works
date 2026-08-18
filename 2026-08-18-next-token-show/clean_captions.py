"""Turn YouTube's rolling VTT captions into a readable timestamped transcript."""

from __future__ import annotations

import html
import re
from pathlib import Path


CUE_RE = re.compile(
    r"(?m)^(?P<start>\d{2}:\d{2}:\d{2}\.\d{3}) --> "
    r"(?P<end>\d{2}:\d{2}:\d{2}\.\d{3}).*?\n(?P<body>.*?)(?=\n\n|\Z)",
    re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")
WORD_RE = re.compile(r"[a-z0-9]+(?:['’][a-z0-9]+)?", re.IGNORECASE)

FRIENDLY_NAMES = {
    "7o3wBWltV-s": "ep-00-none-of-my-software-has-gotten-better",
    "AvjACmiik8U": "ep-01-i-want-your-product-to-enable-my-agent",
    "-DKSg1-v1Gg": "ep-02-ive-never-seen-a-model-say-this-file-is-getting-too-big",
    "2bE93tynluk": "ep-03-im-tired-of-the-uncertainty-of-where-this-is-going",
    "nT8CCWN1foc": "ep-04-weve-never-been-wrong-on-the-internet-before",
}


def seconds(timestamp: str) -> float:
    hours, minutes, rest = timestamp.split(":")
    return int(hours) * 3600 + int(minutes) * 60 + float(rest)


def clean_text(body: str) -> str:
    body = TAG_RE.sub("", body)
    body = html.unescape(body).replace("\n", " ")
    return re.sub(r"\s+", " ", body).strip()


def normalized_words(text: str) -> list[str]:
    return [word.lower().replace("’", "'") for word in WORD_RE.findall(text)]


def clean_vtt(source: Path, destination: Path) -> None:
    vtt = source.read_text(encoding="utf-8")
    emitted_words: list[str] = []
    output: list[str] = [
        "# Cleaned transcript",
        "",
        "Generated from YouTube automatic English captions. Timestamps mark the start of each newly emitted caption segment.",
        "",
    ]

    for match in CUE_RE.finditer(vtt):
        start = match.group("start")
        end = match.group("end")
        if seconds(end) - seconds(start) <= 0.05:
            continue

        text = clean_text(match.group("body"))
        if not text:
            continue
        words = text.split()
        normalized = normalized_words(text)
        if not normalized:
            continue

        overlap = 0
        max_overlap = min(len(normalized), len(emitted_words), 80)
        for candidate in range(max_overlap, 0, -1):
            if emitted_words[-candidate:] == normalized[:candidate]:
                overlap = candidate
                break

        new_words = words[overlap:]
        new_normalized = normalized[overlap:]
        if not new_words:
            continue

        emitted_words.extend(new_normalized)
        output.append(f"[{start[:8]}] {' '.join(new_words)}")

    destination.write_text("\n".join(output) + "\n", encoding="utf-8")


def main() -> None:
    root = Path(__file__).parent
    destination_dir = root / "transcripts"
    destination_dir.mkdir(exist_ok=True)
    for source in sorted((root / "raw-captions").glob("*.vtt")):
        video_id = source.stem.split(".")[0]
        name = FRIENDLY_NAMES.get(video_id, video_id)
        clean_vtt(source, destination_dir / f"{name}.transcript.txt")


if __name__ == "__main__":
    main()
