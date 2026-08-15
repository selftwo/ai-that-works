# Claude for Non-Code Tasks

Status: curated from timestamped YouTube automatic captions and local source files. The captions are useful evidence but are not a human checked transcript.

Source episode: [2025-08-26-claude-for-non-code-workflows](../../../2025-08-26-claude-for-non-code-workflows)

## Purpose, audience, and message

Purpose: Show how markdown, small scripts, and written procedures can support useful agent workflows outside software development.

Audience: Teams that want agent help with operations, reviews, updates, and internal knowledge.

Message: Use plain files as durable state, make procedures explicit, and build deterministic context selection before adding integrations.

## Tactical practices

- Store linked business records as readable markdown when scale permits.
- Use frontmatter and file slicing to pack relevant context deterministically.
- Turn repeatable work into a written SOP that the agent follows.
- Separate a daily read phase from later writing or publishing.
- Let the agent write a narrow API script when a full integration is unnecessary.

## Failure modes and limits

- A growing pile of markdown still needs indexing and pruning.
- Broad MCP integrations can add context and capabilities that the task does not need.
- Generated updates require review because source records can be incomplete.

## Sources and uncertainty

Primary evidence: [timestamped transcript](transcripts/stitched.txt), [source README](../../../2025-08-26-claude-for-non-code-workflows/README.md), and [episode metadata](../../../2025-08-26-claude-for-non-code-workflows/meta.md).

Several examples use private company data that is not included in this repository. See [source-materials.json](source-materials.json) for the supporting file inventory and [claims.jsonl](claims.jsonl) for timestamped evidence.
