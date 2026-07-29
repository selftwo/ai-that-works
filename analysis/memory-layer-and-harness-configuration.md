# Memory layer and harness configuration plan

Date: 2026-07-29
Status: agreed direction, not yet built
Scope: this repo plus the machine-wide agent setup and 2 to 3 other active repos

## What this note is

A saved assessment of the model-neutral memory design proposed in an earlier session (four layers: always-load rules, project facts, active work state, archive), plus the decisions on how to apply it here. The owner works outcome-led: agents do the coding, the owner sets goals, accepts results, and does not review code line by line.

## Verdict on the proposed design

Usable, with changes:

- A model-neutral memory layer in plain markdown, read by both Claude and Codex, is the correct base. Built-in memories (Claude auto-memory, Codex `AGENTS.md`) do not share state and can be turned off.
- The four layers are the right categories.
- The write rules matter more than the folder shape: dated entries, a source for each fact, decisions marked superseded instead of overwritten.
- Do not build the full pipeline (capture queue, `events.jsonl`, dedupe and expiry machinery) up front. That is the designed-program shape. Start with three files and add machinery only when a specific failure repeats, for example an agent acting on a stale decision twice.

## System level vs project level

| Level | Where it lives | What goes there |
|---|---|---|
| System (machine-wide) | `~/.claude/CLAUDE.md`, Claude auto-memory, plus a global `AGENTS.md` so Codex gets the same rules | Who the owner is, writing style, the work-shaping doctrine, model routing, approval rules |
| Project (per repo) | `memory/` in each repo: `overview.md`, `decisions.md`, `active-work.md` | Repo structure rules, current task and blockers, dated decisions. In this repo that includes the never-rewrite-upstream-folders rule and the private-fork setup |
| Archive | Already exists here: `knowledge/` and `analysis/` | Do not duplicate into a `records/` folder. `knowledge/` already has stricter rules (hashes, provenance, review state). Keep one archive and link to it |

## Rules to encode in the pointer files (`CLAUDE.md`, `AGENTS.md`)

- Before a task: read `memory/overview.md`, `memory/decisions.md`, `memory/active-work.md`.
- When a corrected mistake repeats, the agent proposes a dated one-paragraph entry for `decisions.md` or the system-level rules. The owner accepts or rejects it. This is the write trigger.
- Never overwrite a decision; add a new entry and mark the old one superseded.
- Chat text is not fact without review. Every kept fact gets a date and a source.
- Factual claims about tool limits (context sizes, index limits, doc URLs) are dated claims, not facts. They drift as tools change and need a check date.

## Acceptance check the owner can run without reading code

Once a month or after big shifts: open a fresh agent session, give it only the memory files, and ask it to state the current task, the constraints, and the last three decisions. If it gets those wrong, the memory failed. This is the "test the next change" rule applied to memory, and it works on prose, so no code review is needed.

## Starting shape per repo

```text
memory/
  overview.md      # what this repo is, where things live, the hard rules
  decisions.md     # dated, superseded-not-overwritten
  active-work.md   # current task, next step, blockers
CLAUDE.md          # about 10 lines: read the three files above, write rules
AGENTS.md          # same pointers for Codex
```

Machine-wide, outside any repo: keep `~/.claude/CLAUDE.md` and mirror the durable rules into a global `AGENTS.md` for Codex.

## Next steps

1. Set up `memory/` and the pointer sections in this repo, seeded from what is already true (upstream sync rule, private-repo remotes, July 28 episode pending upstream transcript).
2. Repeat the same minimal shape in the other 2 to 3 active repos.
3. Mirror system-level rules into a global Codex `AGENTS.md`.
4. Only after a repeated failure: consider capture queue, expiry, or event logs.
