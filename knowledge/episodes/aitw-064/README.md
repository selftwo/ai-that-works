# Agent Observability

Status: curated from verified YouTube captions. Caption cleanup and speaker attribution remain incomplete.

## Purpose, audience, and message

Purpose: Explain why agent-built systems need traces and wide execution events, then show how humans and agents can inspect them.

Audience: Engineers operating agentic or heavily generated software in production.

Message: Instrument the system before failure, preserve rich execution context, and use traces to compare intended behavior with actual behavior.

## Practical lessons

- Capture structured wide events for questions you cannot predict.
- Link spans with trace and parent identifiers so call structure can be reconstructed.
- Use flame graphs to see repeated calls and expensive paths.
- Let agents inspect large trace sets, but keep evidence links for human review.
- Decide sampling, storage, and transport limits as part of the design.
- Add instrumentation at shared runtime boundaries rather than trusting each generated function to do it.

## Failures and uncertainty

Metrics alone answer only predefined questions. Missing trace points make later diagnosis impossible. Full tracing adds overhead and may expose sensitive inputs, while sampling loses request-level coverage. The caption transcript may contain technical name errors.

Sources: [caption transcript](transcripts/stitched.txt) and [metadata](../../../2026-07-07-agent-observability/meta.md).
