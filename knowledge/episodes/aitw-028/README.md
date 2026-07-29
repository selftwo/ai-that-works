# Agentic RAG + Context Engineering

Status: curated from imported YouTube captions and checked against the source episode files.

Source episode: [`2025-10-21-agentic-rag-context-engineering`](../../../2025-10-21-agentic-rag-context-engineering)

## Purpose, audience, and message

Purpose: Show how an agent assembles context with tools, and identify the implementation details that make that loop useful.

Audience: Teams building retrieval systems, coding agents, or other tool using agents.

Message: Use an open agent loop only when the problem needs flexible retrieval. Most reliability gains come from bounded, observable tool behavior, not elaborate tool descriptions.

## Practical knowledge

- Prefer a deterministic pipeline when the needed steps and context are known. See 04:15 to 07:48.
- Improve the tool implementation before tuning its description. See 13:41 to 14:45.
- Build an interface that exposes each tool call and result during iteration. See 15:00 to 16:07.
- Track the working directory as explicit agent state and tell the model when it changes. See 28:23 to 32:10.
- Put timeouts and result limits around every subprocess and directory search. See 32:50 to 33:29.
- Give truncated reads a line range and a direct way to request the next section. See 33:33 to 34:55.
- Save oversized tool output to a file and let the agent search or read the relevant parts. See 46:18 to 47:40.

## Failure modes and limits

- An open tool loop is slower and less predictable than a fixed retrieval pipeline.
- Hidden working directory changes make later commands fail or waste calls on recovery.
- Unbounded search and read results consume context and may expose files outside the intended scope.
- A truncation notice without a continuation path can leave the model unable to recover missing evidence.
- The episode reports one live build and repeated manual tests, not a controlled model or tool evaluation.

## Sources and uncertainty

Primary evidence is the [timestamped caption transcript](transcripts/stitched.txt). The source README, architecture notes, and implementation files document the demonstrated system. Imported captions have weak speaker labels and transcription errors. Claims about quality and build time are speaker reports.
