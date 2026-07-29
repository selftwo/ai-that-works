# Evals for Classification

Status: curated from timestamped YouTube automatic captions and local source files. The captions are useful evidence but are not a human checked transcript.

Source episode: [2025-09-23-evals-for-classification](../../../2025-09-23-evals-for-classification)

## Purpose, audience, and message

Purpose: Show how to evaluate and improve a large category classification pipeline with a review UI and failure analysis.

Audience: AI engineers building classification systems with many possible labels.

Message: Define what correct means for users, inspect failures in a purpose built UI, and evaluate each pipeline stage before tuning prompts or models.

## Tactical practices

- Narrow a large label set before asking an LLM to select the final class.
- Keep stage level probes for narrowing and final selection.
- Build a UI that makes wrong and borderline cases quick to inspect.
- Record richer correctness classes than a single pass or fail.
- Use real user examples and business impact to choose improvements.

## Failure modes and limits

- Top line accuracy can hide whether the right label was absent from the narrowed set.
- Human reviewers may disagree about labels that are siblings or differ in specificity.
- A test harness built too carefully can slow the first learning loop.

## Sources and uncertainty

Primary evidence: [timestamped transcript](transcripts/stitched.txt), [source README](../../../2025-09-23-evals-for-classification/README.md), and [episode metadata](../../../2025-09-23-evals-for-classification/meta.md).

Reported counts come from the live dataset and UI. They are not independently reproduced in this curation pass. See [source-materials.json](source-materials.json) for the supporting file inventory and [claims.jsonl](claims.jsonl) for timestamped evidence.
