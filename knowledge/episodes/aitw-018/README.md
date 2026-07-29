# Decoding Context Engineering Lessons from Manus

Status: curated from timestamped YouTube automatic captions and local source files. The captions are useful evidence but are not a human checked transcript.

Source episode: [2025-08-12-manus-context-engineering](../../../2025-08-12-manus-context-engineering)

## Purpose, audience, and message

Purpose: Explain context engineering through inference mechanics, especially prompt caching, tool definitions, and selective context.

Audience: Agent builders who need lower latency, lower cost, and steadier behavior in long runs.

Message: Keep stable prompt prefixes stable, avoid changing tool definitions midstream, and give each step only the context it needs.

## Tactical practices

- Place stable instructions and tool definitions before dynamic content.
- Measure cache hits instead of assuming a provider caches the prompt.
- Use few shot examples only when they help the specific action.
- Pass narrow context to specialized agents rather than the whole history.
- Reinforce goals through explicit state or task files.

## Failure modes and limits

- Adding or removing tools can invalidate a cached prefix.
- Few shot examples can bias outputs toward an accidental pattern.
- Cache advice depends on the model provider and serving stack.

## Sources and uncertainty

Primary evidence: [timestamped transcript](transcripts/stitched.txt), [source README](../../../2025-08-12-manus-context-engineering/README.md), and [episode metadata](../../../2025-08-12-manus-context-engineering/meta.md).

The discussion interprets an external Manus article. Local files do not include the article text or provider measurements. See [source-materials.json](source-materials.json) for the supporting file inventory and [claims.jsonl](claims.jsonl) for timestamped evidence.
