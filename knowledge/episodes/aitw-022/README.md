# Generative UIs and Structured Streaming

Status: curated from timestamped YouTube automatic captions and local source files. The captions are useful evidence but are not a human checked transcript.

Source episode: [2025-09-09-generative-uis](../../../2025-09-09-generative-uis)

## Purpose, audience, and message

Purpose: Show how partial structured model output can drive usable interfaces before generation finishes.

Audience: Frontend and AI engineers building streaming applications.

Message: Stream semantic partial objects instead of broken JSON, and declare which fields or objects must be complete before the UI uses them.

## Tactical practices

- Parse partial output into typed optional fields.
- Delay fields or objects whose partial form has no useful meaning.
- Render stable components from semantic state, not raw token text.
- Let downstream work start when a complete subobject arrives.
- Treat error and incomplete states as part of the UI contract.

## Failure modes and limits

- Raw JSON is invalid for much of a token stream.
- Numbers and identifiers can pass through misleading partial values.
- A generic renderer can produce unstable or poor interfaces without product constraints.

## Sources and uncertainty

Primary evidence: [timestamped transcript](transcripts/stitched.txt), [source README](../../../2025-09-09-generative-uis/README.md), and [episode metadata](../../../2025-09-09-generative-uis/meta.md).

The claims describe the demonstrated BAML behavior. They are not a comparison against every structured streaming library. See [source-materials.json](source-materials.json) for the supporting file inventory and [claims.jsonl](claims.jsonl) for timestamped evidence.
