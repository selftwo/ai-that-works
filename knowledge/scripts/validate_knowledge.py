#!/usr/bin/env python3
"""Validate all episode knowledge packets and catalog transcript timestamps."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STAMP = re.compile(r"[\[(](?:(\d{1,2}):)?(\d{2}):(\d{2})(?:[.,](\d+))?[\])]")


def seconds(match: re.Match[str]) -> float:
    return (int(match.group(1) or 0) * 3600 + int(match.group(2)) * 60 +
            int(match.group(3)) + float(f"0.{match.group(4)}") if match.group(4) else
            int(match.group(1) or 0) * 3600 + int(match.group(2)) * 60 + int(match.group(3)))


def main() -> None:
    packet_count = 0
    claim_count = 0
    for directory in sorted((ROOT / "knowledge" / "episodes").glob("aitw-*")):
        if not (directory / "metadata.json").exists():
            continue
        required = ["README.md", "metadata.json", "claims.jsonl", "source-materials.json", "verification.json"]
        missing = [name for name in required if not (directory / name).exists()]
        if missing:
            raise ValueError(f"{directory.name}: missing {missing}")
        for name in ("metadata.json", "source-materials.json", "verification.json"):
            json.loads((directory / name).read_text())
        claims = [json.loads(line) for line in (directory / "claims.jsonl").read_text().splitlines() if line.strip()]
        if not 5 <= len(claims) <= 9:
            raise ValueError(f"{directory.name}: expected 5 to 9 claims, found {len(claims)}")
        packet_count += 1
        claim_count += len(claims)

    catalog = json.loads((ROOT / "knowledge" / "_catalog" / "episodes.json").read_text())
    transcript_count = 0
    for episode in catalog["episodes"]:
        relative = episode.get("transcript_path")
        if not relative:
            continue
        path = ROOT / relative
        values = [seconds(match) for match in STAMP.finditer(path.read_text(errors="replace"))]
        if not values or any(current < previous for previous, current in zip(values, values[1:])):
            raise ValueError(f"{episode.get('guid')}: invalid transcript timestamps")
        transcript_count += 1
    if packet_count != transcript_count:
        raise ValueError(f"packet count {packet_count} does not match verified transcript count {transcript_count}")
    print(json.dumps({"episode_packets": packet_count, "claims": claim_count,
                      "verified_transcripts": transcript_count}))


if __name__ == "__main__":
    main()
