# Voice Agents and Supervisor Threading

Status: curated from timestamped YouTube automatic captions and local source files. The captions are useful evidence but are not a human checked transcript.

Source episode: [2025-09-02-voice-agent-supervisor-threading](../../../2025-09-02-voice-agent-supervisor-threading)

## Purpose, audience, and message

Purpose: Explain how a supervisor process can monitor and redirect a real time voice agent.

Audience: Engineers building interruptible voice or conversational systems.

Message: Separate the fast speaking loop from slower supervision, define interruption rules, and evaluate the full conversation state rather than one response.

## Tactical practices

- Keep the response path fast and run supervision separately.
- Use voice activity detection and interruption thresholds deliberately.
- Let a supervisor classify whether the conversation remains on track.
- Cancel or ignore obsolete calls after newer user speech arrives.
- Build evals from real conversations and preserved state.

## Failure modes and limits

- Noise or short acknowledgements can cause false interruptions.
- A supervisor that runs too often adds cost and latency.
- Parallel model calls can finish after their result is obsolete.

## Sources and uncertainty

Primary evidence: [timestamped transcript](transcripts/stitched.txt), [source README](../../../2025-09-02-voice-agent-supervisor-threading/README.md), and [episode metadata](../../../2025-09-02-voice-agent-supervisor-threading/meta.md).

The source includes exploratory code and specification notes. The transcript does not prove production reliability. See [source-materials.json](source-materials.json) for the supporting file inventory and [claims.jsonl](claims.jsonl) for timestamped evidence.
