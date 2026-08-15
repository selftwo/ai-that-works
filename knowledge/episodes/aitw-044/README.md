# Agentic Backpressure Deep Dive

Status: curated from the existing upstream timestamped transcript. Claims are transcript observations, not independent tests of the demonstrated systems.

Source episode: [2026-02-10-agentic-backpressure-deep-dive](../../../2026-02-10-agentic-backpressure-deep-dive)

## Purpose, audience, and message

Purpose: Teach learning tests as a way to replace agent assumptions about external systems with executable evidence.

Audience: Developers and coding agent users integrating SDKs, APIs, and other systems whose documented behavior may be incomplete.

Message: Research gives descriptions. A small executable test gives evidence that can correct the plan before implementation.

## Tactical practices

- Write a learning test to check how an external field or behavior works before building on it. See 00:13:30 to 00:15:42.
- Treat learning tests as proof work during research, not as feature implementation. See 00:16:30 to 00:17:59.
- Use eval runs as learning tests for model behavior before connecting the prompt to the rest of the system. See 00:18:28 to 00:18:57.
- Keep learning tests for the large class of problems where runtime behavior can cheaply confirm or reject an assumption. See 00:18:57 to 00:20:30.

## Failures, limits, and uncertainty

- Reading complete API documentation can still leave subtle misunderstandings that enter a plan as assumptions. See 00:12:36 to 00:14:13.
- Learning tests help with observable integrations but do not replace design work for every complex problem. See 00:17:59 to 00:18:38.

## Sources and uncertainty

Primary evidence: [transcript](../../../2026-02-10-agentic-backpressure-deep-dive/transcript.txt), [metadata](../../../2026-02-10-agentic-backpressure-deep-dive/meta.md), and [source README](../../../2026-02-10-agentic-backpressure-deep-dive/README.md). Supporting files are listed in [source-materials.json](source-materials.json). Speaker claims, demos, and generated artifacts were not independently reproduced. The transcript source model and cleanup history are not recorded upstream.
