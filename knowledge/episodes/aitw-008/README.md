# Humans as Tools: Async Agents and Durable Execution

Status: curated from imported YouTube captions and the TypeScript demo.

Source episode: [`2025-06-03-humans-as-tools-async`](../../../2025-06-03-humans-as-tools-async)

## Purpose, audience, and message

Purpose: Show how an agent can request human input without holding a process or HTTP request open.

Audience: Engineers building approval, clarification, or long running workflows around agents.

Message: Persist conversation state, emit a request correlated by an identifier, stop the current worker, and resume from stored state when the human reply arrives.

## Tactical practices

- Design for asynchronous channels rather than assuming a live chat session. See 04:17 to 04:50.
- Serialize the model conversation and store it durably. See 16:15 to 17:18.
- Correlate outbound requests and inbound replies with a thread or state ID. See 25:16 to 25:49.
- Pause by ending the current execution instead of keeping a request open. See 26:31 to 26:44.
- Resume in another worker after appending the human response to stored state. See 25:31 to 26:04.
- Separate scary tools and slow human tools from short synchronous actions. See 24:36 to 24:50.

## Failure modes and limits

- Holding an HTTP request open for human response is fragile and wastes worker capacity.
- A reply without a correlation ID can update the wrong conversation.
- In memory state is lost across process restarts or worker changes.
- Duplicate replies and retries need idempotency rules that the demo only partly covers.
- URLs can carry state for simple examples, but sensitive or large state belongs in durable storage.

## Sources and uncertainty

Primary evidence: [caption transcript](transcripts/stitched.txt), [source README](../../../2025-06-03-humans-as-tools-async/README.md), [agent loop](../../../2025-06-03-humans-as-tools-async/src/agent.ts), and [state implementation](../../../2025-06-03-humans-as-tools-async/src/state.ts). Production retry and security behavior were not independently tested.
