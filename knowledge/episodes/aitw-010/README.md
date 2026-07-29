# Entity Resolution: Extraction, Deduping, and Enriching

Status: curated from imported YouTube captions and source code.

Source episode: [`2025-06-17-entity-extraction`](../../../2025-06-17-entity-extraction)

## Purpose, audience, and message

Purpose: Show a production shape for turning verbatim entity mentions into canonical database records.

Audience: Teams extracting people, companies, skills, or other named entities from unstructured data.

Message: Keep extraction separate from resolution, resolve cheap cases first, and send uncertain cases through an asynchronous enrichment and review path.

## Tactical practices

- Preserve the verbatim mention before attempting canonical resolution. See 01:37 to 03:23.
- Treat extraction and resolution as separate typed functions. See 07:56 to 12:17.
- Match legal names and aliases before calling an LLM. See 27:58 to 30:22.
- Queue unresolved entities instead of blocking the main ingestion path. See 05:54 to 07:31 and 43:21 to 48:10.
- Use explicit statuses such as proposed, ready, and committed for human review and later automation. See 48:10 to 56:22.
- Start with a capable expensive model, collect corrections, then optimize against that evidence. See 58:09 to 01:03:41.

## Failure modes and limits

- Mixing extraction with database lookup loses what the source actually said.
- Putting a large canonical list in every prompt stops scaling and increases cost.
- Automatic enrichment can attach the wrong record, so higher risk domains need a human gate.
- The stated heuristic coverage is a speaker estimate, not a measured result in this repository.

## Sources and uncertainty

Primary evidence: [captions](transcripts/stitched.txt), [README](../../../2025-06-17-entity-extraction/README.md), [metadata](../../../2025-06-17-entity-extraction/meta.md), and [resume example](../../../2025-06-17-entity-extraction/baml_src/resume.baml). Speaker labels and caption provenance are unknown.
