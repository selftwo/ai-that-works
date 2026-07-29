# Subagent First Principles: External Research Compared Against the Corpus

Compares an external research document (pasted into conversation, no episode
GUIDs or timestamps, source/authorship unknown) against
`analysis/using-subagents-effectively.md` (corpus-derived, transcript-cited)
and `analysis/pi-agent-configuration/01-subagents-and-model-routing.md`
(settings-advisory, downstream of the corpus doc).

**Provenance warning:** unlike every other file in `analysis/`, the external
document has no citable source, and it isn't drawn from the podcast corpus
at all. It was checked against current Anthropic and OpenAI documentation
and general web search (2026-07-14) rather than transcript evidence — see
"External verification" below for what that turned up and what it's worth.

## What the two existing docs already cover

`using-subagents-effectively.md`: subagents are for context isolation, not
personas (confirmed independently by transcript in `aitw-017`); parallel
dispatch works on partitionable work and fails on greedy sequential
research or shared build-tool locks; delegation prompt quality matters
("task" not "subagent"); subagents can be pinned to cheaper models; prior
subagent use biases the model toward more subagent use.

`pi-agent-configuration/01-...md`: three model-capability slots
(worker/advisor/designer); orchestrator decides dispatch at call time, not
baked in ahead of time; warns against role-named subagents.

Both are solid on **mechanism** (what a subagent is, how dispatch behaves).
Neither has a theory of **when the orchestrator should commit to a plan**,
**what makes a task a good delegation candidate in general form**, or
**how the system should decide it's done**. That's where the external
document is actually useful.

## What's genuinely new

### 1. The control-system framing

"One accountable controller, many disposable contexts, one external truth
surface." Neither existing doc names this. It reframes the corpus's
scattered observations (context resets between phases, subagents returning
tight summaries, the parent re-checking subagent work in `aitw-033`) as
instances of a single design: a feedback-control loop, not a task queue.
The corpus supports this framing without ever stating it directly — this
is a useful naming, not a new fact.

### 2. Model owns judgment, harness owns physics

A clean division: the model decides what to do; the harness decides what
it's allowed to do, what must persist, and what counts as evidence. This
matches the corpus's implicit pattern (e.g. `aitw-028`'s hardcoded
no-recursion rule, `aitw-027`'s Cargo lock as an environment constraint the
model can't reason its way around) but the corpus never states it as a
general principle. Worth adopting as a design lens: before adding any new
constraint to a subagent setup, ask which side of this line it belongs on.

### 3. Probe / Builder / Verifier as a task-nature taxonomy

This is the most concrete new idea. The pi-agent-configuration doc's
worker/advisor/designer slots classify subagents by **which model** runs
them (capability tier). This external framing classifies subagents by
**what kind of work they do** (probe = reduce uncertainty, read-only;
builder = change the world, narrow write scope, returns proof; verifier =
try to falsify a claim, separate from the builder by default).

These are orthogonal axes, not competing ones. A probe can run on the
worker-tier model; a verifier plausibly wants the advisor-tier model. The
pi note currently has a "worker + validator" pattern (citing `aitw-021`)
that is really a probe-tier or verifier-tier task riding on an advisor-tier
model — the two docs are describing compatible things without a shared
vocabulary. **Concrete action:** the next revision of the pi note should
cross the two axes explicitly (task type × model tier) instead of treating
model tier as the only classification.

#### Expansion: this maps onto a real product pattern, not a hypothetical

Cursor shipped exactly this shape as a product in 2026. [Cursor 3
"Glass"](https://dev.to/gabrielanhaia/cursor-3-glass-replaced-composer-with-an-agents-window-1pcg)
(April 2026) replaced the old single-pane Composer with an Agents Window:
spin up several agents in parallel, point each at a different task, and pick
a model per agent from a pool (Sonnet, Opus, GPT-5.5, Grok 4.5, plus Cursor's
own Composer 2.5 — a cheap, fast, high-volume specialist tuned for
long-running agentic coding at roughly a tenth the cost of Opus/GPT-5.5,
according to vendor benchmarks). Subagents, added to Cursor separately in
January 2026, let a single session fan out into several parallel Claude
instances each with independent context and task scope.

What Cursor's UI actually optimizes for is **picking a model per task by
hand, per launch** — the user looks at what a task needs and reaches for a
different model button. That's a manual version of exactly the two-axis
problem above: the human is doing, by eye, the task-type × model-tier
crossing that a preset system would do by name.

**The preset idea, made concrete.** Instead of the pi orchestrator (or you)
choosing a model tier and a task shape separately every time, define named
presets that bind both axes together — closer to Cursor's per-agent model
picker, but named and reusable rather than re-chosen from scratch each
launch:

| Preset name | Task type | Model tier | When to reach for it |
|---|---|---|---|
| `quick-probe` | Probe | worker | Cheap fact-finding, single question, read-only — most subagent dispatch should default here |
| `deep-probe` | Probe | advisor | Ambiguous or high-stakes uncertainty where a cheap model's research would be unreliable — e.g. architecture feasibility, security implications |
| `build` | Builder | worker | Bounded implementation work inside an already-committed plan, narrow write scope |
| `critical-build` | Builder | advisor | Implementation work touching a irreversible or shared surface, where the builder's own judgment quality matters more than speed |
| `verify` | Verifier | advisor | Falsification pass on a builder's claim — deliberately a different model from whatever built the thing, so it isn't just reviewing its own reasoning |
| `design-review` | Verifier (or Probe, for exploration) | designer | Taste/UI/feel judgments — the one place model choice is about aesthetic judgment, not correctness |

This is a proposal, not a settled design — you said you'll bring back your
own brainstorm on the pi extension system and want to hold it against these
notes, so treat the table as a starting shape to argue with, not a spec.
Two things worth deciding when you do:

1. **Whether presets are fixed pairs or just defaults.** Cursor's model
   picker is fully manual per agent — no named presets, just a raw model
   list. A pi preset system is more opinionated than that (a named shortcut
   for a task-type/model-tier pair) but should probably still let the
   orchestrator override the tier for a given dispatch, the way the
   existing pi note already insists model tier isn't baked into a fixed
   subagent persona (see `aitw-048`'s role-naming warning, already cited in
   both docs). A preset should be a default, not a lock.
2. **Whether `verify` should ever default to the same model tier as the
   task it's checking.** Anthropic's trust-escalation concern (§7 above)
   argues for structural separation — a verifier checking a builder's own
   model's output is weaker evidence than an independent model checking it.
   Worth building that constraint into the preset system itself (verify
   preset never silently matches the build preset's model) rather than
   relying on remembering to vary it by hand each time, the way Cursor's
   manual picker requires.

### 4. Before-commitment / after-commitment sequencing

"Before commitment, maximize diversity. After commitment, minimize
divergence." This is sharper than anything in the corpus docs. The corpus
has the pieces — `aitw-027`'s research → plan → implement phases,
`aitw-017`'s point that subagents are "mostly read-only" during research —
but never states the general rule that parallel exploration and parallel
execution are different regimes with different risk profiles. The
external doc's evidence for this (the C-compiler experiment: 16 agents
made progress on independently-failing tests, but collapsed on one
indivisible kernel failure until the environment was redesigned to expose
independently testable subsets) is not verifiable from here, but the
*logic* matches the corpus's own Cargo-lock failure in `aitw-027`
(00:56:07–00:56:44) almost exactly: parallel execution failed not because
of agent count, but because the environment made the work indivisible.
**This is corroboration from two independent failure stories, not just one
document's claim.**

### 5. The spawn-decision inequality

"Context saved + parallel time + independent search value + risk
containment, must exceed briefing cost + coordination cost + integration
cost + verification cost." No existing doc formalizes this. It's a
restatement, as a general rule, of what `aitw-027`'s failure mode
demonstrated empirically (greedy research subagents exhausting context
without proportionate value). Useful as a checklist before delegating, not
as literal math — none of the terms are measurable in practice.

### 6. Two-layer stopping conditions

Neither existing subagent doc discusses when to stop. The external
document's split — hard terminal conditions (explicit DONE criteria) plus a
marginal-value check (`P(material error) × consequence > cost of next
check`) — is a real gap-filler. It also states a distinction worth keeping:
a budget running out is not the same as being done; the honest states are
"blocked," "inconclusive," or "ready for human review." This lines up with
`analysis/agent-visibility-and-guardrail-tactics.md` cluster A (evidence
over narration, `aitw-064`) — both argue against a system claiming
completion it can't back with evidence.

### 7. Multi-agent trust escalation

The claim that subagent output must remain untrusted evidence and not be
elevated just because another model produced it is attributed to
Anthropic in the external doc but not independently checked here. It's
worth taking seriously regardless of source, because it directly extends
`analysis/agent-visibility-and-guardrail-tactics.md` cluster C (guardrail
modeling for untrusted content, `aitw-049`) into a case that cluster
didn't cover: the untrusted content can come from your *own* subagent, not
just external retrieval. Neither subagent doc currently addresses this.
**Concrete action:** the delegation contract template below (§8) already
has an answer — a verifier stage that treats the builder's own output as
a claim to check, not a result to accept.

### 8. The delegation contract and receipt template

The external doc's worked example (a `Task T-014` file with Objective /
Scope and authority / Questions to resolve / Required return / Evidence
standard / Do not / Stop when / Escalate when, paired with a structured
receipt) is more disciplined than the corpus's informal guidance ("say
task not subagent," "tell the parent how to prompt the subagent"). It's
also strikingly close to patterns already live in the user's own repos —
`defkeys/learning/AGENT_REVIEW.md`'s may/may-not contract, benirl-
workshop's issue lease system, agentsmith's `Reported<T>` evidence
contract. **This isn't a new idea for this project — it's a generalized,
reusable template of a pattern already independently invented three times
across the five repos surveyed in the earlier cross-repo map.** The main
value of the external template is as a shared shape, not as new content.

## Where it overlaps and confirms

- Fresh context per subagent, tight return contract: matches `aitw-017`
  directly.
- Recursion/depth limits for legibility: matches `aitw-028`'s no-recursion
  architecture and its lower iteration cap for subagents.
- "Ten agents with clever job titles is the wrong abstraction": matches the
  corpus's role-naming warning (`aitw-048` 00:21:35–00:24:00) and the pi
  note's existing rejection of task-named custom subagents.
- Parallel work needing disjoint ownership / single-writer for shared
  surfaces: matches `aitw-027`'s Cargo lock failure and portfolio-site's
  lease-based single-writer agent workflow (from the earlier cross-repo
  survey).

## External verification (web search, 2026-07-14)

Checked the external document's structural claims against current published
sources rather than taking them on faith:

- **Anthropic's multi-agent research system is real and matches the
  compression/isolation framing closely.** [Anthropic's engineering
  writeup](https://www.anthropic.com/engineering/multi-agent-research-system)
  confirms an orchestrator-worker pattern: a lead agent develops strategy
  and spawns subagents that explore in parallel, each with its own context
  window, returning condensed findings rather than raw search transcripts.
  Anthropic reports a lead-Opus-4 + subagent-Sonnet-4 configuration beat a
  single Opus 4 agent by 90.2% on their internal research evals, with the
  advantage concentrated in breadth-first, independently-parallelizable
  queries — the same "parallelism is a property of the problem, not the
  agent count" point the corpus's Cargo-lock failure (`aitw-027`)
  demonstrates from the failure side. Anthropic also notes a real fragility
  the external doc doesn't mention: **small changes to the lead agent's
  prompt unpredictably change subagent behavior** — worth adding as a risk
  when tuning an orchestrator prompt, not just the subagent prompts.
- **Multi-agent trust escalation is a real, named Anthropic security
  concern**, not an invented framing. Anthropic's ["How we contain Claude
  across products"](https://www.anthropic.com/engineering/how-we-contain-claude)
  describes exactly the mechanism cited: a subagent's output getting
  treated as higher-trust because it "came from us," creating a trust chain
  analogous to a software supply chain — a compromised subagent can promote
  attacker-controlled content into the parent's trusted context. Anthropic's
  documentation adds a point the external doc left out: **subagents can
  inherit the same permission level as the parent by default** unless
  explicitly scoped down — a privilege-escalation risk on top of the
  content-trust risk. This is a second, concrete extension to
  `analysis/agent-visibility-and-guardrail-tactics.md` cluster C, alongside
  the point already logged there.
- **Codex's depth-of-one subagent default is real, current, documented
  behavior**, not corpus anecdote or external-doc invention. [OpenAI's Codex
  subagent docs](https://developers.openai.com/codex/subagents) confirm
  `agents.max_depth` defaults to 1 (root can spawn direct children, children
  can't spawn further descendants) and `agents.max_threads` defaults to 6
  concurrent — close to, not identical to, the "~5" the corpus speaker
  estimated informally in `aitw-029`. Worth correcting: that corpus claim
  was an approximation, not a documented number.
- **OpenAI's Symphony spec is real and open source**, and does define
  handoff states exactly as described: a run can succeed by reaching a
  workflow-defined non-terminal state like "Human Review," not only by
  reaching "Done." Confirmed at
  [github.com/openai/symphony](https://github.com/openai/symphony/blob/main/SPEC.md).
  This directly supports point 6 above (stopping conditions) with a real
  citation instead of an unsourced one.
- **The model names and positioning are current and real, not fabricated
  marketing.** GPT-5.6 (Sol/Terra/Luna tiers) went GA July 9, 2026; Grok 4.5
  shipped the day before; Fable 5 and Sonnet 5 released June 9, 2026.
  Fable 5 leads on SWE-Bench Pro (80.4% vs. Grok 4.5's 64.7% and GPT-5.5's
  58.6%); GPT-5.6's Sol tier reports 91.9% on Terminal-Bench 2.1 using what
  vendors describe as an "ultra mode" that splits work across parallel
  subagents — i.e., parallel subagent orchestration is now a marketed,
  model-native capability, not just a harness-level pattern. Source:
  [gaodalie.substack.com model comparison](https://gaodalie.substack.com/p/i-tested-gpt-56-vs-fable-5-vs-opus),
  [axios.com](https://www.axios.com/2026/07/08/gpt-sol-ultra-openai-anthropic-grok).
  Treat the comparative benchmark numbers as vendor/reviewer-reported, not
  independently reproduced here — but the release timeline and tier
  structure are corroborated across multiple independent sources, so the
  external doc's premise ("the current frontier has moved beyond agents
  that need every step prescribed") holds up better than expected for an
  uncited claim.

## Where to be skeptical

- The `DONE = ...` and `P(material error) × consequence > cost` formulas
  are only pseudocode; treating them as literally computable would be a
  mistake the external doc itself doesn't quite avoid — it presents them
  with more precision than the underlying judgment calls actually have.
- The file-based state protocol (`.agents/current.md`, `tasks/`,
  `receipts/`, `decisions.md`, `final-proof.md`) is presented as if novel;
  it's a relabeling of conventions the user's own repos already run
  (benirl-workshop's `agent-notes/` + `issues/`, agentsmith's
  `docs/orchestration/*.md`, portfolio-site's `tickets/`). Adopting the
  external doc's exact folder names is optional — the pattern is already
  in place under different names.

## Recommendation

Fold two things into the pi-agent-configuration note specifically, since
that's the file this doc was asked to inform:

1. Add the probe/builder/verifier task-type axis alongside the existing
   worker/advisor/designer model-tier axis — they compose, they don't
   compete. The existing "worker + validator" pattern in that note is
   already halfway to this; it just doesn't name the general taxonomy.
2. Add an explicit stop condition to the "concrete checks before changing
   pi's subagent settings" list: define what "done" or "blocked" looks
   like for the worker+validator test run, rather than leaving it as "log
   whether the review call caught something."

Everything else in the external doc either restates what
`using-subagents-effectively.md` already has transcript evidence for, or
restates a pattern already live in the five surveyed repos under a
different name. Worth keeping as a reference document for vocabulary, not
as a new source of fact.
