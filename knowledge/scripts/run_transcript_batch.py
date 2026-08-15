#!/usr/bin/env python3
"""Acquire and normalize missing AI That Works episode transcripts.

The default command is a dry run. Pass ``--execute`` to let yt-dlp inspect and
download English captions. Audio and Whisper transcription are deliberately not
started by this runner. Episodes without captions remain resumable with the
``local_whisper_pending`` status.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Iterable


SCHEMA_VERSION = 2
STAGES = ("select", "inspect_captions", "acquire_captions", "normalize", "verify")
YOUTUBE_ID = re.compile(r"^[A-Za-z0-9_-]{11}$")
TIMING = re.compile(
    r"^(?P<start>\d{2}:\d{2}:\d{2}[.,]\d{3})\s+-->\s+"
    r"(?P<end>\d{2}:\d{2}:\d{2}[.,]\d{3})(?:\s+.*)?$"
)
TAG = re.compile(r"<[^>]+>")


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent,
                                     delete=False) as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
        temporary = Path(stream.name)
    temporary.replace(path)


def fingerprint(episode: dict[str, Any]) -> str:
    fields = {
        "schema_version": SCHEMA_VERSION,
        "guid": episode["guid"],
        "youtube_video_id": episode["youtube_video_id"],
        "source_commit": episode.get("source_commit", ""),
    }
    return hashlib.sha256(json.dumps(fields, sort_keys=True).encode()).hexdigest()


def seconds(value: str) -> float:
    hours, minutes, rest = value.replace(",", ".").split(":")
    return int(hours) * 3600 + int(minutes) * 60 + float(rest)


def clock(value: float, decimal: str = ".") -> str:
    milliseconds = max(0, round(value * 1000))
    hours, remainder = divmod(milliseconds, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    whole, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{whole:02d}{decimal}{millis:03d}"


def clean_caption(lines: Iterable[str]) -> str:
    text = " ".join(line.strip() for line in lines if line.strip())
    text = TAG.sub("", html.unescape(text)).replace("\u200b", "")
    return re.sub(r"\s+", " ", text).strip()


def parse_vtt(text: str) -> list[dict[str, Any]]:
    """Parse VTT or SRT cues and remove duplicate rolling caption cues."""
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    raw_cues: list[dict[str, Any]] = []
    index = 0
    while index < len(lines):
        match = TIMING.match(lines[index].strip())
        if not match:
            index += 1
            continue
        start, end = seconds(match["start"]), seconds(match["end"])
        index += 1
        body: list[str] = []
        while index < len(lines) and lines[index].strip():
            body.append(lines[index])
            index += 1
        value = clean_caption(body)
        if value:
            raw_cues.append({"start": start, "end": end, "text": value})

    # YouTube automatic captions are rolling windows. Each cue often repeats all
    # or part of the prior cue before adding a few words. Emit only the new suffix.
    cues: list[dict[str, Any]] = []
    emitted: list[str] = []
    normalized: list[str] = []
    for cue in raw_cues:
        words = cue["text"].split()
        keys = [re.sub(r"\W+", "", word).casefold() for word in words]
        overlap = 0
        limit = min(len(keys), len(normalized), 40)
        for size in range(limit, 0, -1):
            if keys[:size] == normalized[-size:]:
                overlap = size
                break
        new_words = words[overlap:]
        new_keys = keys[overlap:]
        if not new_words:
            if cues:
                cues[-1]["end"] = max(cues[-1]["end"], cue["end"])
            continue
        emitted.extend(new_words)
        normalized.extend(new_keys)
        cues.append({"id": len(cues) + 1, "start": cue["start"],
                     "end": cue["end"], "text": " ".join(new_words)})
    return cues


def verify(cues: list[dict[str, Any]], source_duration: float | None = None) -> dict[str, Any]:
    failures: list[str] = []
    if not cues:
        failures.append("no caption cues")
    for number, cue in enumerate(cues, 1):
        if cue["start"] < 0 or cue["end"] < cue["start"]:
            failures.append(f"invalid cue {number}")
        if number > 1 and cue["start"] < cues[number - 2]["start"]:
            failures.append(f"non-monotonic cue {number}")
    last_seconds = cues[-1]["end"] if cues else None
    duration_delta = abs(source_duration - last_seconds) if source_duration and last_seconds else None
    if duration_delta is not None and duration_delta > max(180.0, source_duration * 0.05):
        failures.append("caption end is too far from source duration")
    return {
        "status": "passed" if not failures else "failed",
        "cue_count": len(cues),
        "first_seconds": cues[0]["start"] if cues else None,
        "last_seconds": last_seconds,
        "source_duration_seconds": source_duration,
        "duration_delta_seconds": duration_delta,
        "monotonic": not any("monotonic" in item for item in failures),
        "failures": failures,
    }


def render(cues: list[dict[str, Any]], episode: dict[str, Any], source: str) -> dict[str, str]:
    payload = {
        "schema_version": SCHEMA_VERSION,
        "episode_guid": episode["guid"],
        "video_id": episode["youtube_video_id"],
        "origin": "youtube_captions",
        "caption_source": source,
        "segments": cues,
    }
    srt = []
    vtt = ["WEBVTT", ""]
    txt = []
    md = [f"# {episode['title']}", "", f"Source: YouTube captions ({source})", ""]
    for cue in cues:
        srt.extend([str(cue["id"]),
                    f"{clock(cue['start'], ',')} --> {clock(cue['end'], ',')}",
                    cue["text"], ""])
        vtt.extend([f"{clock(cue['start'])} --> {clock(cue['end'])}", cue["text"], ""])
        line = f"[{clock(cue['start'])}] {cue['text']}"
        txt.append(line)
        md.append(line)
    return {
        "stitched.json": json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        "stitched.srt": "\n".join(srt),
        "stitched.vtt": "\n".join(vtt),
        "stitched.txt": "\n".join(txt) + "\n",
        "stitched.md": "\n\n".join(md) + "\n",
    }


def write_outputs(directory: Path, outputs: dict[str, str]) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    for name, content in outputs.items():
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=directory,
                                         delete=False) as stream:
            stream.write(content)
            temporary = Path(stream.name)
        temporary.replace(directory / name)


def base_manifest(episode: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "episode_guid": episode["guid"],
        "video_id": episode["youtube_video_id"],
        "source_url": f"https://www.youtube.com/watch?v={episode['youtube_video_id']}",
        "input_fingerprint": fingerprint(episode),
        "status": "pending",
        "stages": {name: {"status": "pending"} for name in STAGES},
        "updated_at": utc_now(),
    }


def choose_caption(info: dict[str, Any]) -> tuple[str, str] | None:
    """Return (language, kind), preferring manual English over automatic English."""
    for kind, key in (("manual", "subtitles"), ("automatic", "automatic_captions")):
        available = info.get(key) or {}
        choices = [lang for lang in available if lang.lower() == "en"]
        choices += sorted(lang for lang in available
                          if lang.lower().startswith("en-") and lang not in choices)
        if choices:
            return choices[0], kind
    return None


def run_command(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, text=True, capture_output=True, check=False)


def process(episode: dict[str, Any], root: Path, execute: bool) -> dict[str, Any]:
    run_dir = root / "knowledge" / "runs" / "transcripts" / episode["guid"]
    transcript_dir = root / "knowledge" / "episodes" / episode["guid"] / "transcripts"
    manifest_path = run_dir / "manifest.json"
    manifest = base_manifest(episode)
    if manifest_path.exists():
        previous = json.loads(manifest_path.read_text())
        if previous.get("input_fingerprint") == manifest["input_fingerprint"]:
            manifest = previous
    manifest["stages"]["select"] = {"status": "done", "completed_at": utc_now()}
    if not execute:
        manifest["status"] = "dry_run"
        manifest["updated_at"] = utc_now()
        return manifest
    expected = [transcript_dir / name for name in
                ("stitched.json", "stitched.srt", "stitched.vtt", "stitched.txt", "stitched.md")]
    if manifest.get("status") == "done" and all(
            path.is_file() and path.stat().st_size > 0 for path in expected):
        manifest["status"] = "done"
        manifest["resume_action"] = "no_op"
        return manifest
    if not shutil.which("yt-dlp"):
        manifest["status"] = "failed"
        manifest["stages"]["inspect_captions"] = {
            "status": "failed", "error": "yt-dlp is not installed"
        }
        atomic_json(manifest_path, manifest)
        return manifest

    url = manifest["source_url"]
    probe = run_command(["yt-dlp", "--skip-download", "--dump-single-json", url])
    if probe.returncode:
        manifest["status"] = "failed"
        manifest["stages"]["inspect_captions"] = {
            "status": "failed", "error": probe.stderr.strip()[-2000:]
        }
        atomic_json(manifest_path, manifest)
        return manifest
    info = json.loads(probe.stdout)
    selected = choose_caption(info)
    source_duration = float(info["duration"]) if info.get("duration") else None
    manifest["stages"]["inspect_captions"] = {
        "status": "done", "selected": selected, "source_duration_seconds": source_duration
    }
    if not selected:
        manifest["status"] = "local_whisper_pending"
        manifest["stages"]["acquire_captions"] = {
            "status": "pending", "reason": "no English YouTube captions"
        }
        manifest["updated_at"] = utc_now()
        atomic_json(manifest_path, manifest)
        return manifest

    language, kind = selected
    run_dir.mkdir(parents=True, exist_ok=True)
    template = str(run_dir / "captions.%(ext)s")
    command = ["yt-dlp", "--skip-download", "--sub-format", "vtt",
               "--sub-langs", language, "--output", template]
    command.append("--write-subs" if kind == "manual" else "--write-auto-subs")
    command.append(url)
    result = run_command(command)
    caption_files = sorted(run_dir.glob("captions*.vtt"))
    if result.returncode or not caption_files:
        manifest["status"] = "failed"
        manifest["stages"]["acquire_captions"] = {
            "status": "failed", "error": result.stderr.strip()[-2000:]
        }
        atomic_json(manifest_path, manifest)
        return manifest
    manifest["stages"]["acquire_captions"] = {
        "status": "done", "path": str(caption_files[0].relative_to(root)),
        "language": language, "kind": kind,
    }
    cues = parse_vtt(caption_files[0].read_text(errors="replace"))
    report = verify(cues, source_duration)
    if report["status"] != "passed":
        manifest["status"] = "failed"
        manifest["stages"]["verify"] = report
        atomic_json(manifest_path, manifest)
        return manifest
    write_outputs(transcript_dir, render(cues, episode, f"{kind}:{language}"))
    manifest["stages"]["normalize"] = {
        "status": "done", "output_dir": str(transcript_dir.relative_to(root))
    }
    manifest["stages"]["verify"] = report
    manifest["status"] = "done"
    manifest["updated_at"] = utc_now()
    atomic_json(manifest_path, manifest)
    return manifest


def eligible(catalog: dict[str, Any], only: set[str]) -> list[dict[str, Any]]:
    items = []
    for episode in catalog.get("episodes", []):
        video_id = episode.get("youtube_video_id", "")
        if episode.get("transcript_path") or not YOUTUBE_ID.fullmatch(video_id):
            continue
        if only and episode.get("guid") not in only:
            continue
        items.append(episode)
    return items


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path,
                        default=Path("knowledge/_catalog/episodes.json"))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--only", action="append", default=[], metavar="GUID")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--execute", action="store_true",
                        help="inspect and download captions with yt-dlp")
    args = parser.parse_args(argv)
    catalog = json.loads(args.catalog.read_text())
    episodes = eligible(catalog, set(args.only))
    if args.limit:
        episodes = episodes[:args.limit]
    results = [process(item, args.root.resolve(), args.execute) for item in episodes]
    summary = {
        "mode": "execute" if args.execute else "dry_run",
        "selected": len(results),
        "by_status": {status: sum(item["status"] == status for item in results)
                      for status in sorted({item["status"] for item in results})},
        "episodes": [{"guid": item["episode_guid"], "video_id": item["video_id"],
                      "status": item["status"]} for item in results],
    }
    print(json.dumps(summary, indent=2))
    return 1 if any(item["status"] == "failed" for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
