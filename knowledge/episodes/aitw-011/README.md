# Building an AI Content Pipeline

Status: curated from imported YouTube captions and repository implementation files.

Source episode: [`2025-06-24-ai-content-pipeline`](../../../2025-06-24-ai-content-pipeline)

## Purpose, audience, and message

Purpose: Build the first working version of a content workflow that connects recordings, generation, storage, and review.

Audience: Teams automating repeated content operations with AI and external services.

Message: Build the data path and review surface first. Use real inputs, typed states, and fast prompt iteration before optimizing individual model calls.

## Tactical practices

- Establish working infrastructure before tuning generation. See 02:40 to 06:42.
- Keep orchestration code simple and controllable. See 07:37 to 12:55.
- Stream typed progress states so the UI can show what the job is doing. See 17:29 to 23:45.
- Test with actual recordings and service responses. See 28:31 to 36:20.
- Split complex generation when one step has several different jobs. See 49:14 to 57:30.
- Keep a human review step for published content. See 01:03:22 to 01:11:40.

## Failure modes and limits

- Prompt work cannot repair missing dates, links, or source data.
- Framework abstractions can hide state transitions that the UI needs.
- Synthetic samples can miss service and transcript failures.
- The repository is a live build artifact, not a proven production deployment.

## Sources and uncertainty

Evidence: [captions](transcripts/stitched.txt), [README](../../../2025-06-24-ai-content-pipeline/README.md), [metadata](../../../2025-06-24-ai-content-pipeline/meta.md), backend code, schema, and specs. Screen actions and service credentials were not reproduced.
