# Shared Memory for Claude and Codex

This is a design note for a private, model-neutral memory layer. It is based on
the two memory episodes and the private knowledge layer in this repository.

## Evidence

- `aitw-013` 00:08:12–00:11:44: prompts, retrieval, state, history, and
  memory form one context-assembly problem.
- `aitw-013` 00:36:08–00:42:16: inject facts that every task needs.
- `aitw-013` 00:55:18–01:06:42: use prior memory when deciding what is new,
  then compress older history.
- `aitw-014` 00:03:14–00:12:46: keep detailed events, then roll them into
  daily, weekly, and monthly summaries.
- `aitw-014` 00:44:15–00:52:22: retain a source identifier and date range on
  each summary.
- `aitw-014` 00:57:04–01:04:18: remove personal data before model use.

The source transcripts are:

- [Building AI with Memory and Context](../knowledge/episodes/aitw-013/transcripts/stitched.txt)
- [Implementing Decaying Resolution Memory](../knowledge/episodes/aitw-014/transcripts/stitched.txt)

The two caption transcripts have monotonic timestamps. They remain automated
captions, so confirm names and exact wording against the video when it matters.

## Private-repo context

This repository already separates source from derived work:

- dated episode folders are the upstream source corpus;
- `knowledge/` holds transcripts, evidence, claims, and episode packets;
- `analysis/` holds cross-episode design notes;
- `AGENTS.md` gives Codex repository guidance.

Keep personal memory in a new top-level `memory/` folder. Do not put it in an
episode folder or in a model-owned memory store. That makes it portable across
Claude, Codex, machines, and future tools.

## Proposed layout

```text
memory/
  core.md                 # short facts and non-negotiable working rules
  profile.local.md         # private personal preferences; gitignored
  projects/
    ai-that-works/
      overview.md
      decisions.md
      active-work.md
      sources.md
  records/
    2026-07-29-memory-design.md
  events.jsonl            # append-only raw candidate memory events
```

`core.md` and the active project's `overview.md` load for every relevant task.
`active-work.md` carries current state. Retrieve records and older decisions by
task terms, source, and date; do not load the whole archive.

## Write rules

1. Store only durable facts, decisions, preferences, and current work state.
2. Give every entry a date, owner, source link, confidence, and review date.
3. Do not overwrite a changed decision. Mark the old one as superseded.
4. Keep the original record when a summary replaces it.
5. Redact secrets and personal data before any model reads a candidate entry.
6. Require a human review before a candidate fact enters `core.md` or
   `decisions.md`.

## Agent boundary

```text
work notes, commits, chats, source files
                 |
                 v
        events.jsonl (unreviewed)
                 |
                 v
    review, source check, redaction, expiry
                 |
                 v
  core + project facts + dated records
                 |
                 v
        small task-specific context pack
              |                 |
              v                 v
           Claude              Codex
```

Use `CLAUDE.md` to load the shared project rules for Claude. Use `AGENTS.md`
for Codex. Keep both thin: they should name the memory files to read and the
write rules above, rather than contain all the memory themselves.

## Start small

Create only `memory/core.md`, `memory/projects/ai-that-works/overview.md`, and
`memory/projects/ai-that-works/active-work.md` first. Add the event log and
compaction job only after a few weeks show that manual updates no longer keep
up. The episodes support compression, but they do not prove that a full custom
memory service is needed on day one.
