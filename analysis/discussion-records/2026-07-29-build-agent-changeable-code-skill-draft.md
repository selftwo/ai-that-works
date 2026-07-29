# Context: A skill for agent-written code that stays easy to change

## Background

I use AI coding agents to do most of the coding work. I do not expect to write much code myself or review each line. My role is closer to an outcome owner:

- State the user need.
- Set limits and acceptance checks.
- Try the real product result.
- Approve risky or hard-to-undo acts.
- Stop work that has gone in the wrong direction.
- Bring in stronger checks or technical judgment when I cannot judge the code myself.

This changes the main software quality question.

The question is not only:

> Can an agent build this feature and pass the tests?

The more useful question is:

> What can show that the result is good enough for as long as it needs to last?

A system can pass all current tests and still become costly to change. Tests often prove that a known result works now. They may not show whether:

- The code reflects the product in clear terms.
- Each product rule has one clear owner.
- Old user needs still work after later changes.
- A new agent can find the right place to make the next change.
- Complexity and excess code will grow over repeated work.
- The system will remain safe when the original agent and its context are gone.

## Evidence and its limits

The evidence for long-term decline in agent-written code is useful but narrow.

One author based much of the case on a failed team trial and did not claim to have proved it in full. A later study of coding agents found that no agent completed every checkpoint across a full task. Measures of large-function complexity and excess or copied code often rose over repeated changes. Better prompts improved the first result but did not stop later growth.

Those tests dealt with defined Python command-line and API work. They did not test unclear product needs, visual taste, live releases, or work where a user changes the goal after trying the first result.

Reports from teams using agents with high freedom also need care. These teams still rely on people to:

- Set goals.
- Turn user feedback into fixed checks.
- Build safe test copies.
- Set code and system limits.
- Judge product results.
- Improve agent tools and rules.
- Repair repeated faults.

They may stop reading every line of code, but human work remains. It moves toward product judgment, proof, limits, and system upkeep.

## The starting skill

The proposed skill draws some ideas from:

<https://github.com/modem-dev/skills/blob/main/write-discoverable-code/SKILL.md>

That skill helps agents find and understand code through plain-text search. Its main rules include:

- Use clear exported names with product words.
- Avoid broad names such as `create`, `config`, `utils`, or `manager`.
- Use one spelling for each idea.
- Put useful facts near the definition where search lands.
- Use clear types so build errors help the agent correct itself.
- Keep error and event text searchable in the source.
- Give each concept one clear file or part.
- Keep tests close to the code they cover.
- Mark or remove old paths.

This solves a real problem. Most coding agents search files and text, read a small area around each result, and repeat until they understand enough to make a change. Clear names and files cut search time and reduce wrong turns.

However, code can be easy to find and still be poorly designed. Search ease does not prove that:

- Product ideas have clear meanings.
- Product rules live in the right place.
- State changes are valid.
- Outside tools do not control product rules.
- A new feature can be added without a broad rewrite.
- Old user results remain safe.

The new skill should keep the search rules as one part of a wider standard.

## Proposed skill

Suggested name:

`build-agent-changeable-code`

Its purpose:

> Build or change lasting product code so coding agents can find its meaning, preserve accepted user paths, and make later changes safely.

It should trigger for:

- Lasting product features.
- Refactors that change product rules or code ownership.
- Domain model changes.
- Shared interfaces.
- Stored data changes.
- State flows.
- System design.
- Work where agents write most of the code and the human owner judges the result without reading much source.

It should not trigger for:

- Throwaway scripts.
- Small copy edits.
- Clear and local fixes with strong tests.
- Direct code review.
- Requests that only ask how to plan or shape the work.

When the user only wants to decide how to run a task, a separate `shape-ai-work` skill should choose between:

- One-shot work.
- A cheap probe followed by revision.
- A designed program with named stages and pauses.

Once direct coding begins, `build-agent-changeable-code` should guide the work.

## Core principle

The skill should leave code that works now and gives the next agent a clear and safe place to work.

It should join four concerns:

1. Product language.
2. Clear ownership of rules.
3. Search-friendly code.
4. Proof that covers both current behaviour and later change.

## Work process

### 1. Fix the acceptance frame

Before coding, extract:

- The user result.
- What stays out of scope.
- One or two visible checks.
- Old accepted user paths that must still work.
- Risky acts that need approval.
- The undo path.
- Whether the result will be kept and changed.

The agent should infer small gaps from the request, current product, tests, and code. It should ask only when a choice could change product meaning, user harm, or a public contract.

This step is complete when the result, limits, checks, pauses, and undo path are clear or marked as unknown.

### 2. Recover the product language

The agent should read:

- The request.
- Product copy.
- Tests.
- User-facing text.
- Data names.
- Logs and events.
- Nearby code.
- Existing product notes.

It should list the changed:

- User roles.
- User acts.
- Product terms.
- Rules and limits.
- States and allowed state changes.
- Outside systems.

Each product idea should have one plain name across code, tests, logs, events, and user-facing text.

When two terms seem to mean the same thing, the agent should settle that difference before adding another term. It should keep an existing term when that term still matches the product. It should rename stale terms when their meaning has changed.

This step is complete when every changed user act, rule, and state has one clear name and one clear owner.

### 3. Find the full change path

The agent should trace one real user act from its entry point to its visible result.

It should find:

- Where the user act begins.
- Where each product rule lives.
- Which outside systems take part.
- Which tests prove the path.
- Which old paths may break.
- Where rule ownership is unclear or split.
- Which stored data or public contracts may change.

The agent should extend an existing clear owner when possible. It should add a new shared part only when no current part owns the idea and the new part has one clear job.

This step is complete when each changed rule, system edge, test, and visible result has a named place.

### 4. Build one small, complete user path

The agent should build the smallest complete path that can prove the main user result.

It should keep product rules apart from:

- Screens.
- Web routes.
- Database details.
- Queues.
- Vendor tools.
- Framework code.

The agent may choose the local code form, but it should follow hard limits:

- Give each product rule one owner.
- Make invalid product states hard to create.
- Name product acts and state changes.
- Keep coordination code thin.
- Keep outside details away from product rules.
- Use precise types at product and safety bounds.
- Put product words in exported names and file names.
- Use one spelling for each idea.
- Keep full error and event text searchable.
- Mark or remove old paths.
- Place tests next to the code they cover or link them through clear names.

The agent should pause before:

- Weakening an accepted check.
- Changing product meaning.
- Crossing a new system boundary.
- Making a change that is hard to undo.
- Adding work outside the agreed result.
- Changing access, money, private data, or shared stored forms.

This step is complete when the user path works from start to end and each changed rule has one searchable owner.

## Domain design rules

The skill should use domain design as a practical way to keep product meaning clear. It should not force a full set of patterns onto every codebase.

### Use one product language

Use the same term in:

- User stories.
- Product copy.
- Types.
- Functions.
- Events.
- Logs.
- Tests.

Do not switch between near-synonyms for the same idea.

For example, if the product calls something an `invitation`, do not use `invite`, `request`, and `token` for that same idea unless each word has a distinct meaning.

### Give each rule one owner

A product rule should live in one named part. Screens, routes, jobs, and command handlers should call that part rather than copy the rule.

The agent may use these broad parts when they help:

- **Domain part:** product values, rules, decisions, and state changes.
- **Application part:** one user act or system task that joins rules with outside work.
- **Adapter:** code that talks to a screen, web call, database, queue, or vendor.

These are guides, not required layers.

### Make states and limits clear

When valid combinations matter, use named states instead of linked booleans and optional fields.

For example, use clear `Draft`, `Sent`, and `Paid` invoice states instead of mixing `isSent`, `isPaid`, `sentAt`, and `paidAt`.

Use named types for values that agents may swap or misuse, such as:

- User and account IDs.
- Money and units.
- Permissions.
- Dates with set meanings.
- Product limits.
- Validated contact details.

Parse unknown input at the system edge. Pass valid product values into the main rules.

### Avoid empty shared parts

Do not add a new layer, base type, service, manager, or helper only to make the design look complete.

Add a shared part when it:

- Protects a product rule.
- Removes harmful copying.
- Gives a product idea one clear owner.
- Keeps an outside tool from setting product meaning.

A search for the product term should find its rule, main use, and tests.

## Proof model

The skill should keep different claims and proof types apart.

| Claim | Suitable proof |
|---|---|
| The result helps and feels right | The outcome owner tries the real user path |
| Known behaviour still works | Fixed checks and past accepted cases |
| The release works in real use | Error, speed, load, and side-effect checks |
| The code remains workable | A skilled technical check or a later-change test |

A green test suite does not prove product value or ease of future change.

### Proof for kept code

For code that will remain in use, the agent should:

- Run the new user path.
- Rerun old accepted paths touched by the change.
- Check errors and side effects.
- Add upkeep proof.

When harm is high, a skilled technical check should happen before release. High-harm areas include:

- Access control.
- Money.
- Private data.
- Destructive acts.
- Shared stored data.
- Public contracts.
- Hard-to-reverse system edges.

### Later-change test

When risk is lower and the system allows it, give a fresh agent one small nearby change.

Do not tell that agent where the new code lives or explain its design. Give it:

- The normal project rules.
- The user result.
- The fixed checks.
- One small change that uses the same product ideas.

Record:

- Search terms used.
- Files opened before the right one.
- Wrong product terms or owners assumed.
- Files changed.
- Failed checks.
- Human help needed.
- Copying, new layers, or broad rewrites.

The result is healthy when the fresh agent:

- Finds the right rule from product terms.
- Makes a local change.
- Keeps old checks passing.
- Needs no hidden design lesson.
- Does not create a second owner for the rule.

One successful later-change test is a warning check, not proof that all future work will stay easy.

## Role of the outcome owner

The outcome owner should:

- State the need.
- Accept or reject the user result.
- Judge product wording and feel.
- Approve risky acts.
- Stop poor work.
- Decide when a first result changes the goal.

The outcome owner should not have to:

- Review every line.
- Judge type design they do not know.
- Approve code style.
- Pretend to assess system structure.
- Decide whether a complex rule belongs in one module or another.

When code judgment matters, the process should use a fixed check, a skilled technical reviewer, or a later-change test.

## Handoff

At the end of the work, the agent should report:

1. The user result and how to try it.
2. The new and old paths checked.
3. Product terms and rules settled.
4. Live risks and side effects.
5. The upkeep check and its result.
6. Gaps and their owner.
7. The undo step.

The report should let the outcome owner judge the result without reading source. It should also let the next agent locate the changed product rules through the product terms.

## Open design choices

The draft still needs testing on real work. Key open points include:

- Whether the skill should install or call `write-discoverable-code`, or only work beside it.
- Whether its domain rules suit both new systems and old codebases.
- How much domain design it should require for a small feature.
- When a later-change test costs enough to skip.
- What signals best show that an agent struggled with the structure.
- Whether the domain term list should stay in task notes or become a lasting project file.
- How the skill should adapt to languages with weak type systems.
- Whether high-risk work should always require a named technical reviewer.

The first useful test should use a small, lasting product feature with:

- One clear user path.
- At least one product rule.
- One state change.
- An old accepted path.
- An outside system or storage edge.
- A safe nearby change for a fresh agent.

The test should compare the first implementation with the later-change result. The aim is to learn whether the skill changes agent behaviour, keeps product language clear, and makes the next change more local.