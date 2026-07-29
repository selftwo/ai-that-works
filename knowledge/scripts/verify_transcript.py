#!/usr/bin/env python3
"""Verify speaker timestamp order and basic coverage in an episode transcript."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


STAMP = re.compile(r"[\[(](?:(\d{1,2}):)?(\d{2}):(\d{2})(?:[.,](\d+))?[\])]")


def seconds(match: re.Match[str]) -> float:
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2))
    whole_seconds = int(match.group(3))
    fraction = float(f"0.{match.group(4)}") if match.group(4) else 0.0
    return hours * 3600 + minutes * 60 + whole_seconds + fraction


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_transcript.py TRANSCRIPT", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    values = [seconds(match) for match in STAMP.finditer(path.read_text(errors="replace"))]
    failures = []
    if not values:
        failures.append("no timestamps found")
    if any(current < previous for previous, current in zip(values, values[1:])):
        failures.append("timestamps are not monotonic")
    report = {
        "path": str(path),
        "timestamp_count": len(values),
        "first_timestamp_seconds": values[0] if values else None,
        "last_timestamp_seconds": values[-1] if values else None,
        "nonempty": path.stat().st_size > 0,
        "monotonic": "timestamps are not monotonic" not in failures,
        "status": "passed" if not failures and path.stat().st_size > 0 else "failed",
        "failures": failures,
    }
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
