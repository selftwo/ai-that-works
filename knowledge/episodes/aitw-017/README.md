# Context Engineering for Coding Agents

Status: curated from timestamped YouTube automatic captions and local source files. The captions are useful evidence but are not a human checked transcript.

Source episode: [2025-08-05-advanced-context-engineering-for-coding-agents](../../../2025-08-05-advanced-context-engineering-for-coding-agents)

## Purpose, audience, and message

Purpose: Show a research, planning, and implementation workflow that keeps coding agents focused on verified context.

Audience: Developers using coding agents on large or unfamiliar codebases.

Message: Treat research and plans as review gates, compact context on purpose, and fix shared naming before asking an agent to implement.

## Tactical practices

- Use explicit compaction or a fresh context after durable findings have been written to files.
- Send narrow research questions to subagents and keep their results out of the main context until needed.
- Review research before planning, then review the plan before implementation.
- Use consistent domain names across code so the agent can connect related parts.
- Put detailed file paths and test expectations in the implementation plan.

## Failure modes and limits

- Bad research can contaminate every later phase if it is not reviewed.
- More subagents can create more context noise when their scopes overlap.
- A plan can look complete while carrying a false statement from research.

## Sources and uncertainty

Primary evidence: [timestamped transcript](transcripts/stitched.txt), [source README](../../../2025-08-05-advanced-context-engineering-for-coding-agents/README.md), and [episode metadata](../../../2025-08-05-advanced-context-engineering-for-coding-agents/meta.md).

The automatic captions contain transcription errors and do not reliably identify speakers. See [source-materials.json](source-materials.json) for the supporting file inventory and [claims.jsonl](claims.jsonl) for timestamped evidence.
