# Implementing Decaying Resolution Memory

Status: curated from imported YouTube captions and implementation files.

Source episode: [`2025-07-15-decaying-resolution-memory`](../../../2025-07-15-decaying-resolution-memory)

## Purpose, audience, and message

Purpose: Turn the prior episode's memory concept into a working data model and summarization flow.

Audience: Agent builders who need bounded long term conversational memory.

Message: Store detailed recent events, roll older events into daily, weekly, and monthly summaries, and preserve links and dates so each summary remains traceable.

## Tactical practices

- Define explicit daily, weekly, and monthly resolution levels. See 03:14 to 12:46.
- Use event time, not processing time, to place information in the right period. See 18:02 to 27:30.
- Summarize with the prior memory context so changes can be recognized. See 31:42 to 41:09.
- Keep source identifiers and date ranges with summaries. See 44:15 to 52:22.
- Redact personal data before sending stored conversations to a model. See 57:04 to 01:04:18.
- Make compaction resumable and inspect intermediate records. See 01:06:11 to 01:16:32.

## Failure modes and limits

- Processing timestamps can put late events in the wrong summary bucket.
- Repeated summarization can erase details or turn mistakes into durable memory.
- PII redaction can miss sensitive text or remove useful context.
- The live implementation is exploratory and does not establish retrieval quality over time.

## Sources and uncertainty

Evidence: [captions](transcripts/stitched.txt), [README](../../../2025-07-15-decaying-resolution-memory/README.md), [main implementation](../../../2025-07-15-decaying-resolution-memory/main.py), and redaction files. Processed sample threads may contain synthetic or demonstration data and were not treated as factual episode claims.
