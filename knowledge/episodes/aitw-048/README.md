# Claude Agent Skills Deep Dive

Status: curated from the existing upstream timestamped transcript. Claims are transcript observations, not independent tests of the demonstrated systems.

Source episode: [2026-03-10-claude-agent-skills-deep-dive](../../../2026-03-10-claude-agent-skills-deep-dive)

## Purpose, audience, and message

Purpose: Explain commands, skills, agents, and subagents as distinct context engineering tools.

Audience: People configuring Claude Code or similar coding agent harnesses.

Message: Use skills to inject reusable instructions and subagents to isolate token heavy work, while keeping global tool descriptions small.

## Tactical practices

- Treat the system prompt, built in tools, repository instructions, and current conversation as parts of one context window. See 00:10:38 to 00:11:55.
- Use a subagent when work needs a fresh context window and only a short result should return to the parent. See 00:11:55 to 00:17:08.
- Fork context for a narrow design question when the subtask needs existing context but its tool work should not pollute the main thread. See 00:17:08 to 00:17:45.
- Use a custom subagent when a stable task prompt must be applied every time the isolated worker runs. See 00:19:27 to 00:21:35.

## Failures, limits, and uncertainty

- Subagent output quality depends on the parent delegation prompt and can omit or invent information like any tool call. See 00:19:27 to 00:20:21.
- Role named subagents can blur execution isolation with reusable instructions and encourage teams to model an organization instead of a task boundary. See 00:21:35 to 00:24:00.

## Sources and uncertainty

Primary evidence: [transcript](../../../2026-03-10-claude-agent-skills-deep-dive/transcript.txt), [metadata](../../../2026-03-10-claude-agent-skills-deep-dive/meta.md), and [source README](../../../2026-03-10-claude-agent-skills-deep-dive/README.md). Supporting files are listed in [source-materials.json](source-materials.json). Speaker claims, demos, and generated artifacts were not independently reproduced. The transcript source model and cleanup history are not recorded upstream.
