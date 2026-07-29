# Pi Agent Configuration Notes

Working notes for configuring `pi`, the headless coding agent you run inside
project repos (seen so far as `.pi-agent/` in `defkeys`). These notes are
advisory only. You will read them, decide what to change, and hand-apply the
change in pi's own settings — nothing here edits pi directly.

This is a separate track from
[agent-visibility-and-guardrail-tactics.md](../agent-visibility-and-guardrail-tactics.md).
That file is about making agent work legible and safe across your five
product repos in general. This folder is narrower: concrete settings and
structure inside pi itself, one topic per note, built up over time as you
work through your list.

## Context this folder assumes

- You are a design-first PM, not a developer, building small QoL tools,
  research, and agents. The long game is staying in the game: motivation
  comes from craft and fun, not just output. See the values you gave in the
  first request to this folder for the full framing.
- You want subagents in pi to be flexible and task-scoped, not fixed
  personas or roles, so you can freely reassign cheaper or lighter models to
  them from pi's model settings.
- Evidence for these notes comes from `knowledge/episodes/` transcripts
  (cited by GUID and timestamp) and from what your own repos already show
  pi doing, such as `defkeys/orchestration/2026-07-13-product-build.md`.
  Repo-based claims are read from the file at the time of writing and may
  go stale — check the file again before acting on a note that cites it.

## Notes in this folder

1. [Subagents and model routing](01-subagents-and-model-routing.md) — three
   configurable model slots (worker, advisor, designer) with the main agent
   as orchestrator deciding dispatch pattern at call time, not fixed
   subagent roles. Includes the worker + validator pairing pattern and what
   today's failed multi-model run in `defkeys` already tells you.

## How to use this with pi

Bring one note at a time into your pi session. Ask pi to show you its
current subagent or settings config before changing anything, compare it
against the note's recommendation, and only change what the note calls out.
Log what you actually changed and what happened back into the note (or a
dated addendum) so the next note can build on real outcomes instead of
guesses.
