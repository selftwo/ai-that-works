# How to Build AI Agents that Work in Any Language

Status: curated from the upstream transcript. Transcript evidence only.

## Purpose, audience, and message

Purpose: Present a maintainable architecture for multilingual AI applications.

Audience: Teams whose agent prompts and tools are mainly English but whose users are not.

Message: Keep one well-tested core pipeline and normalize language at the input and output edges, while evaluating translation risks separately.

## Practical lessons

- Translate or normalize before the core agent and localize after it.
- Preserve the original message and source language for tone recovery.
- Test the edge nodes independently from the core pipeline.
- Add an English fast path only after measuring its classification errors.
- Review schema and tool names because they also steer language.

## Failures and uncertainty

Parallel language pipelines drift and multiply eval work. Edge translation can lose meaning, especially in high-stakes domains. The live demo is not a broad quality study across languages.

Sources: [transcript](../../../2026-06-02-multilingual-ai-apps/transcript.txt), [metadata](../../../2026-06-02-multilingual-ai-apps/meta.md), and [upstream README](../../../2026-06-02-multilingual-ai-apps/README.md).
