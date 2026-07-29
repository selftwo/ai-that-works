# SOTA Coding Agent Benchmarks

Status: curated from the existing upstream transcript. Claims capture the speakers'
assessment of benchmarks; this packet does not independently reproduce benchmark
results.

Source episode: [`2026-07-14-sota-coding-agent-benchmarks`](../../../2026-07-14-sota-coding-agent-benchmarks)

## Purpose, audience, and message

Purpose: Explain how coding-agent benchmarks work, what newer designs measure, and
why benchmark scores still miss long-term software quality.

Audience: Engineers who use or evaluate coding agents for production software.

Message: Use benchmarks as narrow evidence about a task class. Pair them with fast
feedback in the real codebase and human judgment about design, change, and upkeep.

## Practical lessons

- A passing task verifier can show that an agent solved one bounded problem; it does
  not show that the resulting code will stay easy to change.
- Prefer behavior-focused checks when many valid implementations exist. A test that
  demands one historical patch can grade implementation matching rather than user
  outcome.
- Longer tasks, regression checks, code-quality rules, and mutation-style checks
  add useful signals, but they still do not model a changing product brief.
- Make back pressure fast and clear: types, linters, tests, and review all help an
  agent converge before a weak pattern spreads.
- Keep people on problem framing and long-horizon design. Those remain hard to turn
  into reliable, general scoring rules.

## Failures and uncertainty

The transcript mixes speaker opinion, examples, and descriptions of outside
benchmarks. Product names and benchmark details may need checking against primary
sources before use as factual comparisons. The speakers argue for a future
sequential benchmark, but it is a proposal, not a reported result.

Sources: [timestamped transcript](../../../2026-07-14-sota-coding-agent-benchmarks/transcript.txt),
[metadata](../../../2026-07-14-sota-coding-agent-benchmarks/meta.md), and
[upstream summary](../../../2026-07-14-sota-coding-agent-benchmarks/README.md).
