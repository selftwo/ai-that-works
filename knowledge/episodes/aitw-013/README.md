# Building AI with Memory and Context

Status: curated from imported YouTube captions and source notes.

Source episode: [`2025-07-08-context-engineering`](../../../2025-07-08-context-engineering)

## Purpose, audience, and message

Purpose: Define memory as part of the wider problem of assembling useful model context.

Audience: Teams building stateful, personalized, or proactive agents.

Message: Design memory for a clear user behavior. Fetch required facts deterministically, expose bounded domain tools, and compress history according to what the task needs.

## Tactical practices

- Treat prompts, RAG, history, and memory as parts of one context assembly step. See 08:12 to 11:44.
- Define the desired user experience before choosing a memory architecture. See 17:42 to 24:50.
- Inject facts that are always needed instead of hoping the agent retrieves them. See 36:08 to 42:16.
- Give agents meaningful tools such as calendar and inbox operations, scoped to the user. See 44:20 to 52:31.
- Summarize older history at lower resolution and include existing memory when deciding what is notable. See 55:18 to 01:06:42.
- Keep deterministic work such as timezone conversion in application code. See 01:09:20 to 01:15:38.

## Failure modes and limits

- Remembering everything grows cost and hides relevant facts.
- A generic memory search tool makes the agent infer too much and can widen access.
- Summaries made without prior memory can repeat facts or miss change.
- Memory quality depends on the product goal, so the proposed architecture is not universal.

## Sources and uncertainty

Evidence: [captions](transcripts/stitched.txt), [README](../../../2025-07-08-context-engineering/README.md), [metadata](../../../2025-07-08-context-engineering/meta.md), and code examples. Linked external articles were not used as episode evidence.
