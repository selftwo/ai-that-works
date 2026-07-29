# Bash vs. MCP: Token Efficient Coding Agent Tooling

Status: curated from timestamped YouTube automatic captions and local source files. The captions are useful evidence but are not a human checked transcript.

Source episode: [2025-09-16-coding-agent-tools-bash-vs-mcp](../../../2025-09-16-coding-agent-tools-bash-vs-mcp)

## Purpose, audience, and message

Purpose: Compare MCP tools with command line tools through context cost, discoverability, and engineering effort.

Audience: Developers choosing tool interfaces for coding agents.

Message: Inspect the actual context cost and task needs. MCP is useful for easy discovery, while a narrow CLI can preserve context and give precise control.

## Tactical practices

- Measure tool schema tokens in the real agent context.
- Expose only the tools needed for the current task.
- Use familiar command names and concise help text.
- Build a narrow CLI when repeated use justifies the engineering cost.
- Cache fetched issue content in local context when it will be reused.

## Failure modes and limits

- Large MCP schemas consume context even when most tools are unused.
- A custom CLI shifts integration work to the developer.
- Poor tool names and descriptions reduce selection accuracy.

## Sources and uncertainty

Primary evidence: [timestamped transcript](transcripts/stitched.txt), [source README](../../../2025-09-16-coding-agent-tools-bash-vs-mcp/README.md), and [episode metadata](../../../2025-09-16-coding-agent-tools-bash-vs-mcp/meta.md).

Token counts are from the demonstrated Claude setup and Linear tools. They will change with clients, schemas, and models. See [source-materials.json](source-materials.json) for the supporting file inventory and [claims.jsonl](claims.jsonl) for timestamped evidence.
