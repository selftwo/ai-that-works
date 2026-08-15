# Building an Animation Pipeline

Status: curated from the existing upstream speaker transcript.

Source episode: [`2025-11-18-building-an-animation-pipeline`](../../../2025-11-18-building-an-animation-pipeline)

## Purpose, audience, and message

Purpose: Show an AI assisted pipeline that turns an Excalidraw file into a reviewed WebM and then uploads it to YouTube.

Audience: Engineers automating creative production workflows with coding agents and existing tools.

Message: Use agents for adaptable glue work, but preserve review points, build a good human testing loop, and keep human design judgment in charge.

## Practical knowledge

- Reuse object timestamps in an Excalidraw file to replay and record the drawing. See 05:55 to 08:13.
- Wrap browser automation and CLI tools in a slash command that asks for review before upload. See 09:04 to 12:39.
- Keep an agent in the loop when natural language changes such as “make it slower” are valuable. See 12:39 to 15:05.
- Stop a visibly wrong run instead of spending more tokens. See the later implementation discussion.
- Design the human testing workflow before optimizing the agent workflow. See 52:16 to 53:39.

## Failure modes and limits

- A linear stable flow may be cheaper and clearer as a script.
- Browser recording and font loading are fragile integration points.
- Parallel agent work raises review and attention costs.
- Fast code generation does not replace system design or testing judgment.

## Sources and uncertainty

Primary evidence is the [upstream speaker transcript](../../../2025-11-18-building-an-animation-pipeline/transcript.md). The source README summarizes the workflow. Screen state and private tools were not independently verified.
