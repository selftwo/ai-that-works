# PII Redaction and Sensitive Data Scrubbing

Status: curated from the existing upstream timestamped transcript. Claims are transcript observations, not independent tests of the demonstrated systems.

Source episode: [2026-03-03-pii-redaction-and-sensitive-data-scrubbing](../../../2026-03-03-pii-redaction-and-sensitive-data-scrubbing)

## Purpose, audience, and message

Purpose: Present a layered architecture for redacting legally restricted and contextually sensitive data.

Audience: Teams shipping AI systems that handle personal, health, account, or other sensitive information.

Message: Set risk tolerance first, keep zero tolerance controls in deterministic software, and combine static, dynamic, and generative rules for contextual cases.

## Tactical practices

- Separate zero tolerance data from contextually sensitive data before designing the redaction system. See 00:01:47 to 00:02:17.
- Handle data with legal liability through a software control plane and security analysis, not an LLM prompt. See 00:02:17 to 00:06:46.
- Use regex for fast known patterns, while recognizing that it grows reactively from known misses. See 00:09:11 to 00:09:25.
- Model redaction as three rule types: static rules, dynamic rules from current data, and generative rules for ambiguous content. See 00:18:53 to 00:20:30.

## Failures, limits, and uncertainty

- The episode focuses on lower tolerance contextual leaks and does not present its demo as a solution for zero tolerance data. See 00:06:09 to 00:06:46.
- Replacing regex with an LLM changes the leak versus degradation tradeoff but does not remove it. See 00:09:25 to 00:14:00.

## Sources and uncertainty

Primary evidence: [transcript](../../../2026-03-03-pii-redaction-and-sensitive-data-scrubbing/transcript.txt), [metadata](../../../2026-03-03-pii-redaction-and-sensitive-data-scrubbing/meta.md), and [source README](../../../2026-03-03-pii-redaction-and-sensitive-data-scrubbing/README.md). Supporting files are listed in [source-materials.json](source-materials.json). Speaker claims, demos, and generated artifacts were not independently reproduced. The transcript source model and cleanup history are not recorded upstream.
