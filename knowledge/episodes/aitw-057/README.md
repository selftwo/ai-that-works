# Code Mode Deep Dive

Status: curated from the existing upstream timestamped transcript. Claim verification is transcript only. The transcript source, model, cleanup history, and exact recording start are not recorded upstream.

Source episode: [2026-05-12-code-mode-deep-dive](../../../2026-05-12-code-mode-deep-dive)

## Purpose, audience, and message

Purpose: Compare inline tools, MCP, shell commands, CLIs, and code mode as ways for agents to call external capabilities.

Audience: Harness and platform builders designing large tool catalogs or multi tenant agent runtimes.

Message: Treat tool definitions as the durable primitive, choose an execution form for the workload, and favor code mode when output shaping and large catalogs outweigh its runtime cost.

## Tactical practices

- Maintain a typed catalog of tool names, inputs, and outputs.
- Use first class tools for common workflows and dynamic mechanisms for the long tail.
- Shape outputs before returning them to model context.
- Generate execution adapters from OpenAPI or another structured interface.
- Isolate credentials and global state for multi tenant execution.

## Failure modes and limits

- CLI authentication stored as machine global state forces stronger sandbox isolation.
- Shell pipelines often return far more text than the agent needs.
- Replacing tools with a JavaScript executor alone does not provide discovery, typing, or schema conversion.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2026-05-12-code-mode-deep-dive/transcript.txt), [episode metadata](../../../2026-05-12-code-mode-deep-dive/meta.md), and [source README](../../../2026-05-12-code-mode-deep-dive/README.md).

Claims describe what the speakers said or demonstrated. Screen only details, reported measurements, exact speaker attribution, and transcript cleanup remain uncertain unless a claim note says otherwise.

