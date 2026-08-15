#!/usr/bin/env python3
"""Aggregate reviewed episode packets into browsable Markdown and JSON catalogs."""

from __future__ import annotations

import csv
import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE = ROOT / "knowledge"
CATALOG = KNOWLEDGE / "_catalog"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def main() -> None:
    source = load_json(CATALOG / "episodes.json")
    source_by_guid = {row["guid"]: row for row in source["episodes"] if row.get("guid")}
    episodes = []
    claims = []
    for directory in sorted((KNOWLEDGE / "episodes").glob("aitw-*")):
        metadata_path = directory / "metadata.json"
        readme = directory / "README.md"
        claim_path = directory / "claims.jsonl"
        if not metadata_path.exists() or not readme.exists() or not claim_path.exists():
            continue
        metadata = load_json(metadata_path)
        guid = metadata.get("guid") or directory.name
        row = source_by_guid.get(guid, {})
        record = {
            "guid": guid,
            "episode": metadata.get("episode", row.get("episode", "")),
            "title": metadata.get("title", row.get("title", "")),
            "event_date": metadata.get("recorded_at", metadata.get("event_date", row.get("event_date", ""))),
            "youtube_video_id": metadata.get("youtube_video_id", row.get("youtube_video_id", "")),
            "source_folder": metadata.get("source_folder", row.get("source_folder", "")),
            "knowledge_readme": str(readme.relative_to(ROOT)),
            "claims_file": str(claim_path.relative_to(ROOT)),
            "transcript_path": row.get("transcript_path", ""),
        }
        episode_claims = []
        for line in claim_path.read_text().splitlines():
            if not line.strip():
                continue
            claim = json.loads(line)
            claim["episode_guid"] = guid
            claim["episode_title"] = record["title"]
            episode_claims.append(claim)
        record["claim_count"] = len(episode_claims)
        episodes.append(record)
        claims.extend(episode_claims)

    episodes.sort(key=lambda row: (row["event_date"], row["guid"]))
    CATALOG.mkdir(parents=True, exist_ok=True)
    (CATALOG / "knowledge-episodes.json").write_text(json.dumps(episodes, indent=2, ensure_ascii=False) + "\n")
    with (CATALOG / "claims.jsonl").open("w") as stream:
        for claim in claims:
            stream.write(json.dumps(claim, ensure_ascii=False) + "\n")
    with (CATALOG / "knowledge-episodes.csv").open("w", newline="") as stream:
        fields = list(episodes[0]) if episodes else []
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(episodes)

    md = ["# AI That Works Knowledge Index", "",
          f"Reviewed episode packets: {len(episodes)}", "",
          f"Timestamped claims: {len(claims)}", ""]
    rows = []
    for item in reversed(episodes):
        relative = Path(item["knowledge_readme"]).relative_to("knowledge")
        md.append(f"- [{item['guid']}: {item['title']}]({relative}) | {item['event_date']} | {item['claim_count']} claims")
        rows.append(
            "<tr>"
            f"<td>{html.escape(item['event_date'])}</td>"
            f"<td>{html.escape(item['guid'])}</td>"
            f"<td><a href=\"{html.escape(str(relative))}\">{html.escape(item['title'])}</a></td>"
            f"<td>{item['claim_count']}</td>"
            "</tr>"
        )
    (KNOWLEDGE / "index.md").write_text("\n".join(md) + "\n")
    page = """<!doctype html><meta charset=\"utf-8\"><title>AI That Works Knowledge</title>
<style>body{font:15px system-ui;max-width:1100px;margin:2rem auto;padding:0 1rem;color:#222}table{border-collapse:collapse;width:100%}th,td{padding:.45rem;border-bottom:1px solid #ddd;text-align:left}th{position:sticky;top:0;background:white}input{width:100%;padding:.6rem;margin:.5rem 0 1rem;box-sizing:border-box}</style>
<h1>AI That Works Knowledge</h1><p>Search reviewed episode packets and timestamped claims.</p>
<input id=\"q\" placeholder=\"Filter episodes\"><table><thead><tr><th>Date</th><th>GUID</th><th>Episode</th><th>Claims</th></tr></thead><tbody>""" + "".join(rows) + """</tbody></table>
<script>q.oninput=()=>document.querySelectorAll('tbody tr').forEach(r=>r.hidden=!r.innerText.toLowerCase().includes(q.value.toLowerCase()))</script>"""
    (KNOWLEDGE / "index.html").write_text(page)
    print(json.dumps({"reviewed_episode_packets": len(episodes), "timestamped_claims": len(claims)}))


if __name__ == "__main__":
    main()
