# Hands-on with Fable 5

Status: curated from the upstream transcript. The repository calls the model “Fable 5”; that name has not been corrected without stronger source evidence.

## Purpose, audience, and message

Purpose: Show how the hosts test a new model on hard, known engineering problems.

Audience: Engineers comparing coding models for complex repository work.

Message: Use repeatable hard cases, check comprehension and constraint handling, and measure reduced correction work instead of relying on launch claims.

## Practical lessons

- Test the hardest problem you understand well.
- Save repository states and prompts for known failures.
- Ask for an architecture explanation before code.
- Check whether the model holds subtle constraints, not only whether it produces a plausible patch.
- Record partial wins and exact failure points.

## Failures and uncertainty

The model missed both a thread-ID constraint and the unique correlation key in a race condition. These are two live examples, not a full model evaluation. The source folder does not contain the benchmark commits or generated patches.

Sources: [transcript](../../../2026-06-09-fable-5/transcript.txt), [metadata](../../../2026-06-09-fable-5/meta.md), and [upstream README](../../../2026-06-09-fable-5/README.md).
