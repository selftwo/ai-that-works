#!/usr/bin/env python3
"""Standard-library self-checks for run_transcript_batch.py."""

from __future__ import annotations

import json
import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("run_transcript_batch.py")
SPEC = importlib.util.spec_from_file_location("run_transcript_batch", MODULE_PATH)
assert SPEC and SPEC.loader
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


SAMPLE = """WEBVTT

00:00:01.000 --> 00:00:03.250
<c>Hello &amp; welcome</c>

00:00:03.500 --> 00:00:05.000 align:start position:0%
Second cue

00:00:05.000 --> 00:00:06.000
Second cue
"""


class RunnerTests(unittest.TestCase):
    def test_parse_render_and_verify(self) -> None:
        cues = runner.parse_vtt(SAMPLE)
        self.assertEqual([cue["text"] for cue in cues],
                         ["Hello & welcome", "Second cue"])
        self.assertEqual(cues[-1]["end"], 6.0)
        self.assertEqual(runner.verify(cues)["status"], "passed")
        episode = {"guid": "aitw-test", "youtube_video_id": "abcdefghijk",
                   "title": "Test"}
        outputs = runner.render(cues, episode, "manual:en")
        self.assertEqual(set(outputs), {"stitched.json", "stitched.srt",
                                       "stitched.vtt", "stitched.txt", "stitched.md"})
        self.assertEqual(len(json.loads(outputs["stitched.json"])["segments"]), 2)

    def test_non_monotonic_fails(self) -> None:
        report = runner.verify([
            {"start": 2.0, "end": 3.0}, {"start": 1.0, "end": 2.0}
        ])
        self.assertEqual(report["status"], "failed")

    def test_rolling_caption_overlap_is_removed(self) -> None:
        sample = """WEBVTT

00:00:01.000 --> 00:00:02.000
Hello there

00:00:02.000 --> 00:00:03.000
Hello there friend

00:00:03.000 --> 00:00:04.000
there friend

00:00:04.000 --> 00:00:05.000
there friend today
"""
        cues = runner.parse_vtt(sample)
        self.assertEqual([cue["text"] for cue in cues], ["Hello there", "friend", "today"])

    def test_duration_gap_fails(self) -> None:
        report = runner.verify([{"start": 0.0, "end": 10.0}], source_duration=1000.0)
        self.assertEqual(report["status"], "failed")

    def test_eligible_requires_id_and_missing_transcript(self) -> None:
        catalog = {"episodes": [
            {"guid": "yes", "youtube_video_id": "abcdefghijk", "transcript_path": ""},
            {"guid": "no-id", "youtube_video_id": "", "transcript_path": ""},
            {"guid": "done", "youtube_video_id": "12345678901", "transcript_path": "x"},
        ]}
        self.assertEqual([item["guid"] for item in runner.eligible(catalog, set())], ["yes"])

    def test_dry_run_does_not_write(self) -> None:
        episode = {"guid": "aitw-test", "youtube_video_id": "abcdefghijk",
                   "title": "Test", "source_commit": "abc"}
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result = runner.process(episode, root, execute=False)
            self.assertEqual(result["status"], "dry_run")
            self.assertEqual(list(root.rglob("*")), [])

    def test_caption_preference(self) -> None:
        info = {"subtitles": {"en-GB": [{}]}, "automatic_captions": {"en": [{}]}}
        self.assertEqual(runner.choose_caption(info), ("en-GB", "manual"))


if __name__ == "__main__":
    unittest.main()
