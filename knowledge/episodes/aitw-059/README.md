# No Vibes Allowed: Performance Engineering

Status: curated from verified YouTube captions. Caption cleanup and speaker attribution remain incomplete.

## Purpose, audience, and message

Purpose: Show a measurement-first method for improving runtime performance with agents.

Audience: Engineers optimizing virtual machines, runtimes, and other performance-sensitive systems.

Message: Build stable workloads and measurements first, preserve results, then use traces and source research to make one bounded change at a time.

## Practical lessons

- Measure before changing code.
- Benchmark representative workloads, not one toy function.
- Record variance so noise does not look like progress.
- Save benchmark results for quick comparison and agent review.
- Use profiles to locate allocation and execution costs, then verify the change against the same workload.

## Failures and uncertainty

Long benchmark cycles slow the feedback loop. Profilers add overhead. A local speedup may not carry to another workload. The source is automatic captions, so names and sentence boundaries need review.

Sources: [caption transcript](transcripts/stitched.txt) and [metadata](../../../2026-05-26-no-vibes-allowed-performance-engineering/meta.md).
