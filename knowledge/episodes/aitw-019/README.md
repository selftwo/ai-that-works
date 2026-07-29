# Interruptible Agents

Status: curated from timestamped YouTube automatic captions and local source files. The captions are useful evidence but are not a human checked transcript.

Source episode: [2025-08-19-interruptible-agents](../../../2025-08-19-interruptible-agents)

## Purpose, audience, and message

Purpose: Build an agent loop that can accept new user input, cancel work, and resume with changed instructions.

Audience: Product engineers designing interactive agent experiences.

Message: Interruption is an application state problem. Own the queue, task identity, cancellation behavior, and resume rules instead of hiding them in a framework.

## Tactical practices

- Give each running task an identity and keep new messages in an explicit queue.
- Race agent completion against incoming user input when low latency matters.
- Represent proposed changes as exact diffs that can be accepted or replaced.
- Separate cancellation from state reset and define both explicitly.
- Keep human approval points visible in the workflow.

## Failure modes and limits

- A blocking request loop cannot observe input until the model call ends.
- Parallel listeners add thread safety and lifecycle complexity.
- An interrupted task may keep stale state unless resume semantics are explicit.

## Sources and uncertainty

Primary evidence: [timestamped transcript](transcripts/stitched.txt), [source README](../../../2025-08-19-interruptible-agents/README.md), and [episode metadata](../../../2025-08-19-interruptible-agents/meta.md).

The episode is a live implementation. Some code paths are exploratory and not presented as production tested. See [source-materials.json](source-materials.json) for the supporting file inventory and [claims.jsonl](claims.jsonl) for timestamped evidence.
