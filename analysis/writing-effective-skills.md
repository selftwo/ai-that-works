# Writing Effective Skills

Synthesis of what the corpus says about writing and structuring Claude Code
skills (as distinct from subagents, commands, and MCP tools). Primary source
is `aitw-048` ("Claude Agent Skills Deep Dive"), the one dedicated episode.
Claims cited by episode GUID and timestamp where mined from transcript;
quotes marked "host notes" come from the episode's own source README
(`2026-03-10-claude-agent-skills-deep-dive/README.md`), which is more
specific than the curated claims.jsonl for this episode.

## Core distinction: skills vs. subagents

- `aitw-048` 00:10:38–00:11:55: treat the system prompt, built-in tools,
  repository instructions, and current conversation as parts of one context
  window.
- `aitw-048` 00:11:55–00:17:08: use a subagent when work needs a fresh
  context window and only a short result should return to the parent.
- Host notes: "Skills and subagents solve different problems — don't
  conflate them. A subagent gives you a fresh context window, great for
  long, token-heavy tasks you want to run in isolation. A skill gives you a
  way to inject instructions into any context window, parent or child, on
  demand." Before skills existed, custom subagents were the only way to
  bundle instructions, which is why the two get conflated now.
- Host notes: "Use subagents for context isolation, not for carrying
  instructions." A Playwright agent clicking around a DOM generates a ton of
  tokens — fork it into a subagent so it doesn't pollute the main context.
  For a reusable instruction set like "here's how we write backend code,"
  reach for a skill instead.

**Rule of thumb:** if the problem is *too many tokens in this context*, use
a subagent. If the problem is *this context is missing an instruction I want
available on demand*, use a skill.

## Forking vs. isolating

- `aitw-048` 00:17:08–00:17:45: fork context for a narrow design question
  when the subtask needs existing context but its tool work shouldn't
  pollute the main thread.
- `aitw-048` 00:19:27–00:21:35: use a custom subagent when a stable task
  prompt must be applied every time the isolated worker runs.

## Budget discipline

- Host notes: "Every subagent description, every skill description, and
  every MCP tool gets injected into your context window on every turn." 30
  globally installed skills eat into the token budget the model needs to
  follow your actual instructions. Claude Code mitigates this with a tool
  search feature past a certain threshold, but the simpler fix is installing
  fewer things and being intentional about global vs. per-project scope.

**Inference:** this is a direct, checkable constraint for any skill you
write — before adding a skill globally, ask whether it needs to be global at
all, or whether project-scoped is enough.

## Controlling when a skill fires

- Host notes: use `disable_model_invocation: true` in a skill's frontmatter
  for a skill meant to run only as a user-triggered slash command, not
  auto-invoked mid-task. This removes the skill's description from the
  context window entirely — the model never sees it and can't call it on
  its own.

## Failure modes to write against

- `aitw-048` 00:19:27–00:20:21: subagent output quality depends on the
  parent delegation prompt and can omit or invent information like any tool
  call — a vague delegation prompt produces vague or fabricated subagent
  output.
- `aitw-048` 00:21:35–00:24:00: role-named subagents ("the reviewer," "the
  architect") can blur execution isolation with reusable instructions, and
  push a team toward modeling an organization chart instead of a task
  boundary. A subagent should be scoped to a task, not a persona.

## Applying this to the repos already surveyed

None of the five repos surveyed (agentsmith, defkeys, natural-selection,
portfolio-site, benirl-workshop) currently define Claude Code skills with
`disable_model_invocation` or an explicit token-budget accounting — this is
inference, not a claim in any repo's docs. portfolio-site's
`.agents/skills/impeccable/` is the one existing skill in the corpus; worth
checking it against the budget-discipline and role-naming guidance above
before adding more skills anywhere.
