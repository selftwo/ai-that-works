# Theme capture rules

These rules govern The Next Token and future podcast processing. The central
rule is: do not collapse every claim into a generic “AI impact” theme. Capture
the claim at the layer where it actually lives.

## The five lenses

| Code | Lens | Capture when the claim is about | Do not use it for |
|---|---|---|---|
| `MI` | Model intelligence | What a model can or cannot understand, reason about, plan, generalize, remember, route, or do with tools; also observed model behavior and capability limits | A product becoming better or worse just because it contains a model |
| `PQ` | Product quality | The user-visible outcome: usefulness, correctness, reliability, UX, performance, maintainability, or whether the shipped product solves the problem | Claims about why the product team made the tradeoff |
| `OC` | Organizational competence | How people and organizations execute: architecture, workflow, staffing, review, governance, operations, coordination, accountability, and proof | A model limitation or a price point by itself |
| `EI` | Economic incentives | Price, cost, revenue, market power, access, regulation, provider policy, resource allocation, and what behavior those incentives encourage | Human fatigue or attention unless the claim explicitly connects it to an incentive |
| `ATTN` | Speaker attention and agency | What the individual must notice, decide, remember, steer, or sustain; cognitive load, distraction, burnout, joy, and the changing shape of personal work | Aggregate organizational process or a general product-quality claim |

“His own attention” means the speaker’s first-person operating experience. Keep
that distinct from what the organization does and from what the model can do.

## Atomic-claim rules

1. Write one claim per theme. A theme may have one primary lens and one
   explicitly linked secondary lens, but it must not hide two different claims.
2. Split mixed claims. For example, “autonomous agents are expensive,
   unreliable, and exhausting” becomes three notes: `EI` cost, `MI`/`PQ`
   reliability, and `ATTN` operator load.
3. Use `MI` for capability evidence, `PQ` for the resulting product outcome,
   and `OC` for the human or organizational practice that connects them. Do
   not treat one as proof of another.
4. Use `EI` when money, access, policy, or power explains why a system behaves
   as it does. State the incentive or constraint explicitly.
5. Use `ATTN` only when the transcript describes a person’s own attention,
   agency, cognitive load, or emotional sustainability. Do not infer it from
   a generic mention of “humans.”
6. Preserve disagreement as evidence. If hosts disagree, capture the claim
   and the counterclaim instead of averaging them into a single conclusion.
7. Separate observation from interpretation. Record what happened, what the
   speaker inferred, and what remains uncertain.
8. Do not promote a vendor prediction to a model-intelligence fact. Mark it as
   a claim under review until the transcript supplies observed behavior or an
   external source is independently checked.

## Required shape for each captured theme

```md
### [MI] Short atomic claim

- Evidence: `HH:MM:SS–HH:MM:SS`
- Observation: what the speakers actually describe
- Interpretation: what the claim means at this lens
- Counterevidence or uncertainty: disagreement, missing context, or source risk
- Related lenses: links to separate `PQ`, `OC`, `EI`, or `ATTN` notes when needed
```

## Review and promotion rules

- Produce four to six high-value themes per episode by default, but allow a
  mixed claim to split into more than six atomic notes when that prevents
  category collapse.
- Keep per-episode themes separate from cross-episode themes.
- Keep the source timestamp on every theme.
- Mark inferred sections and unverified proper names.
- Treat every theme as a candidate until Ben keeps, renames, merges, splits,
  or drops it.
- A cross-episode theme is allowed only when the same lens and claim recur in
  at least two episodes. If the lens changes, keep separate linked themes.

