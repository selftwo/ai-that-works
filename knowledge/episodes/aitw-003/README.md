# Code Generation with Small Models

Status: curated from imported YouTube captions. Claim verification is transcript only unless a repository file is named.

Source episode: [`2025-04-15-code-generation-small-models`](../../../2025-04-15-code-generation-small-models)

## Purpose, audience, and message

Purpose: Build a code editing pipeline where models produce structured diffs and deterministic code checks constrain their output.

Audience: Engineers who want cheaper or smaller models to perform bounded code generation tasks reliably.

Message: Decompose editing into explicit stages, validate every result with normal programming tools, and improve one narrow stage at a time before considering a smaller or fine tuned model.

## Tactical practices

- Separate instruction quality, file selection, diff generation, diff application, and validation. See 01:52 to 05:03.
- Ask for structured diffs rather than an unconstrained rewritten repository. See 09:45 to 12:05.
- Apply diffs in deterministic code, then run validation. See 04:41 to 05:03.
- Parse generated Python with the AST library to catch syntax errors and identify the bad line. See 34:19 to 34:48.
- Feed validation errors back into another repair step rather than accepting invalid output. See 35:45 to 36:36.
- Optimize or fine tune a small model for one stable stage after the surrounding pipeline works. See 53:15 to 53:27.

## Failure modes and limits

- Weak user instructions and wrong file selection fail before generation begins.
- Models may wrap output in Markdown or produce malformed diff syntax.
- Syntax validity does not prove behavioral correctness.
- Applying several diffs at once can create conflicts or hide which change failed.
- The discussion suggests a path to small models but does not report a completed small model benchmark.

## Sources and uncertainty

Primary evidence: [caption transcript](transcripts/stitched.txt), [agent code](../../../2025-04-15-code-generation-small-models/agent), and [sample project](../../../2025-04-15-code-generation-small-models/project). Captions can mishear technical terms.
