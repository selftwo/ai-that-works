# Selecting from Thousands of MCP Tools

Status: curated from imported YouTube captions and the tool selection demo.

Source episode: [`2025-05-27-mcp-with-10000-tools`](../../../2025-05-27-mcp-with-10000-tools)

## Purpose, audience, and message

Purpose: Show how to use MCP when the available tool set is too large for one model context.

Audience: Engineers integrating many external APIs or MCP servers into an agent system.

Message: Treat tool choice as retrieval. Keep a small stable control tool, retrieve a bounded candidate set at runtime, then let the model select and call from that set under application control.

## Tactical practices

- Measure the context cost before loading every tool. See 03:44 to 04:30.
- Give the model a small tool that requests or lists relevant tools. See 12:48 to 16:06.
- Retrieve candidate tools with deterministic filters or embeddings. See 15:52 to 16:06.
- Load selected tool definitions dynamically at runtime. See 28:40 to 29:26.
- Improve tool descriptions because those descriptions affect both retrieval and model choice. See 19:21 to 19:32.
- Treat remote tool descriptions as untrusted input. See 21:01 to 21:13.

## Failure modes and limits

- Thousands of schemas consume context and reduce the model's ability to choose.
- Retrieval can omit the needed tool before the model sees it.
- Similar or weak descriptions produce ambiguous selection.
- A remote MCP server can supply malicious descriptions or parameter text.
- Embedding retrieval still needs task based evaluation and access controls.

## Sources and uncertainty

Primary evidence: [caption transcript](transcripts/stitched.txt), [source README](../../../2025-05-27-mcp-with-10000-tools/README.md), [tool loader](../../../2025-05-27-mcp-with-10000-tools/tools.py), and the BAML resume example. The demo does not establish a universal best retrieval method.
