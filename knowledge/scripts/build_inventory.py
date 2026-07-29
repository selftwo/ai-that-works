#!/usr/bin/env python3
"""Build a deterministic transcript coverage catalog from the source clone."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "knowledge" / "_catalog"
EPISODE_DIR = re.compile(r"^\d{4}-\d{2}-\d{2}-.+")
YOUTUBE_ID = re.compile(r"(?:youtu\.be/|youtube\.com/watch\?v=)([A-Za-z0-9_-]{11})")


def git_head() -> str:
    return subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()


def git_head_time() -> str:
    return subprocess.run(
        ["git", "show", "-s", "--format=%cI", "HEAD"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def registry() -> dict[str, dict]:
    data = json.loads((ROOT / "data.json").read_text())
    return {item["folder"]: item for item in data.get("episodes", [])}


def video_overrides() -> dict[str, dict]:
    path = ROOT / "knowledge" / "_catalog" / "video-overrides.json"
    return json.loads(path.read_text()) if path.exists() else {}


def first_video_id(paths: list[Path]) -> str:
    for path in paths:
        if not path.exists():
            continue
        match = YOUTUBE_ID.search(path.read_text(errors="replace"))
        if match:
            return match.group(1)
    return ""


def registry_video_id(item: dict) -> str:
    candidates = [item.get("links", {}).get("youtube", ""), item.get("media", {}).get("url", "")]
    for value in candidates:
        if not value:
            continue
        match = YOUTUBE_ID.search(value)
        if match:
            return match.group(1)
    return ""


def verified_knowledge_transcript(guid: str) -> Path | None:
    transcript = ROOT / "knowledge" / "episodes" / guid / "transcripts" / "stitched.txt"
    manifest = ROOT / "knowledge" / "runs" / "transcripts" / guid / "manifest.json"
    if not transcript.exists() or not manifest.exists():
        return None
    state = json.loads(manifest.read_text())
    if state.get("status") != "done" or state.get("stages", {}).get("verify", {}).get("status") != "passed":
        return None
    return transcript


def main() -> None:
    entries = registry()
    overrides = video_overrides()
    head = git_head()
    source_updated_at = git_head_time()
    rows = []
    for folder in sorted(p for p in ROOT.iterdir() if p.is_dir() and EPISODE_DIR.match(p.name)):
        item = entries.get(folder.name, {})
        source_transcripts = [p for p in (folder / "transcript.txt", folder / "transcript.md", folder / "trasncript.txt") if p.exists()]
        knowledge_transcript = verified_knowledge_transcript(item.get("guid", ""))
        transcripts = source_transcripts or ([knowledge_transcript] if knowledge_transcript else [])
        transcript = transcripts[0] if transcripts else None
        text = transcript.read_text(errors="replace") if transcript else ""
        guid = item.get("guid", "")
        video_id = (overrides.get(guid, {}).get("youtube_video_id", "") or
                    registry_video_id(item) or
                    first_video_id([folder / "meta.md", folder / "README.md"]))
        rows.append({
            "guid": item.get("guid", ""),
            "episode": item.get("episode", ""),
            "title": item.get("title", folder.name[11:].replace("-", " ")),
            "source_folder": folder.name,
            "event_date": item.get("eventDate", ""),
            "youtube_video_id": video_id,
            "transcript_path": str(transcript.relative_to(ROOT)) if transcript else "",
            "transcript_origin": "upstream" if source_transcripts else ("youtube_captions" if transcript else ""),
            "transcript_sha256": sha256(transcript) if transcript else "",
            "has_timestamps": bool(re.search(r"[\[(]\d{2}:\d{2}(?::\d{2})?[.,]\d+[\])]", text)),
            "transcript_bytes": transcript.stat().st_size if transcript else 0,
            "source_commit": head,
            "source_updated_at": source_updated_at,
        })

    CATALOG.mkdir(parents=True, exist_ok=True)
    payload = {"schema_version": 1, "source_commit": head, "source_updated_at": source_updated_at, "episodes": rows}
    (CATALOG / "episodes.json").write_text(json.dumps(payload, indent=2) + "\n")
    fields = list(rows[0]) if rows else []
    with (CATALOG / "coverage.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "episode_directories": len(rows),
        "with_transcript": sum(bool(row["transcript_path"]) for row in rows),
        "with_timestamped_transcript": sum(row["has_timestamps"] for row in rows),
        "with_direct_youtube_id": sum(bool(row["youtube_video_id"]) for row in rows),
    }
    (CATALOG / "coverage-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
