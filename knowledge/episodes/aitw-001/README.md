# Large Scale Classification

Status: curated from imported YouTube captions. Claims are transcript grounded. Caption text has no speaker labels and may contain recognition errors.

Source episode: [`2025-03-31-large-scale-classification`](../../../2025-03-31-large-scale-classification)

## Purpose, audience, and message

Purpose: Show how to classify an input against thousands of categories without putting every category in one model prompt.

Audience: Engineers building routing, tagging, support, or product classification systems with large label sets.

Message: Treat classification as a pipeline. Narrow candidates with deterministic retrieval, let a model choose among the smaller set, and trace each stage so failures can be located and evaluated.

## Tactical practices

- Keep category descriptions rich enough to embed, not just short identifiers. See 12:56 to 13:41.
- Retrieve the top candidate categories by similarity, then use a model for the final semantic choice. See 22:58 to 23:35.
- Expose the embedding model, candidate count, prompt, and final selector as separate controls. See 13:27 to 13:41 and 32:21 to 32:34.
- Break the pipeline into smaller functions that can be evaluated separately. See 32:21 to 32:34.
- Trace retrieval and selection methods independently. See 66:25 to 66:49.
- Evaluate with real user queries and connect wrong outcomes to the stage that caused them. See 69:23 to 69:35.

## Failure modes and limits

- Embedding retrieval can omit the correct category before the model sees it.
- Similar category names or weak descriptions can make top K retrieval unstable.
- End to end accuracy alone does not show whether retrieval or final selection failed.
- The episode demonstrates an approach, not a measured comparison across models or datasets.

## Sources and uncertainty

Primary evidence: [caption transcript](transcripts/stitched.txt), [source README](../../../2025-03-31-large-scale-classification/README.md), and the source BAML and Python example. Event time comes from source metadata and may not be the exact recording start.
