# MCP is Dead?

Status: curated from the existing upstream timestamped transcript. Claim verification is transcript only. The transcript source, model, cleanup history, and exact recording start are not recorded upstream.

Source episode: [2026-03-24-mcp-is-dead](../../../2026-03-24-mcp-is-dead)

## Purpose, audience, and message

Purpose: Separate useful MCP extension points from cases where a direct SDK or first class tool is a better fit.

Audience: Agent builders deciding how to expose integrations and user supplied tools.

Message: Use MCP for user supplied long tail capabilities, build common integrations directly, and account for the context and trust cost of every tool.

## Tactical practices

- Treat MCP as a plugin boundary, not a replacement for every SDK.
- Keep common tools first class and move popular long tail tools into supported integrations.
- Measure tool definition size and remove tools that users do not call.
- Tell users when installed MCPs are inactive so they can disable them.
- Review third party tool descriptions as untrusted instructions.

## Failure modes and limits

- Large tool catalogs consume context even when their tools are never called.
- An untrusted MCP can reduce agent quality through poor or hostile instructions.
- A generic integration will usually perform worse than one designed for the main workflow.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2026-03-24-mcp-is-dead/transcript.txt), [episode metadata](../../../2026-03-24-mcp-is-dead/meta.md), and [source README](../../../2026-03-24-mcp-is-dead/README.md).

Claims describe what the speakers said or demonstrated. Screen only details, reported measurements, exact speaker attribution, and transcript cleanup remain uncertain unless a claim note says otherwise.

