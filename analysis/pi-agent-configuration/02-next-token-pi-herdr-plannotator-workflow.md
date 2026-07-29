# Pi, Herdr, and Plannotator: workflow reference

Source: [Next Token, Episode 02](https://www.youtube.com/watch?v=-DKSg1-v1Gg),
recorded 2026-07-17 and published 2026-07-23. This note covers the workflow
section, 00:34:18–01:10:12. It is a timestamped, cleaned reference from the
video's automatic English captions, checked against the video chapter list.
Names corrected from caption errors: **Pi**, **Herdr**, **Plannotator**, and
**Wayfinder**. Treat claims about current tool behaviour as dated to the
recording.

## The workflow in one pass

Dillon Mulroy's loop is deliberately human-led:

1. Ask Pi questions about the current code before asking it to change code.
2. Read and mark up the answer in Plannotator; send grouped feedback back to
   Pi.
3. Ask Pi for a code-oriented spec: types, changed call paths, side effects,
   errors, tests, and a first vertical slice.
4. Review and revise that spec in Plannotator until the system shape is clear.
5. Let Pi implement it.
6. Run two first-pass reviews: one against the spec and one against the
   coding standards.
7. Review the local diff in Plannotator, comment file by file, send the
   comments back to the agent, and repeat until satisfied.

Herdr runs and shows several agent sessions while this loop is under way.
Pi's `/tree` lets him branch and revisit the same conversation without asking
an autonomous subagent to decide what research to do.

## Pi: small harness, added only when needed

### 00:37:50–00:43:58

Pi is the terminal agent harness he uses every day. His reason for choosing it
is not that it has the most built-in machinery. He wants a small, stable base:
a short fixed system prompt and a small set of tools. He says this makes the
agent feel more focused and makes its behaviour easier to learn while models
themselves remain variable.

Pi can extend itself. It can read its own extension docs and code, then help
make a tool or extension suited to the user's work. His advice is to start
with stock Pi and add an extension only after a real pain appears. Public
extensions can be used as examples, not as a default bundle to install.

The small set he showed included:

- a gateway for work use;
- a secret-masking extension;
- a skill toggle;
- `/md` to save an agent reply as Markdown;
- web search and fetch tools;
- a continuation aid after compaction;
- a Git command guard that rejects `--no-verify` and makes the agent fix the
  hook failure or ask for help.

The useful rule is: keep the harness plain, then add a narrow control or tool
for a known recurring need. The Git guard is a good example: it protects a
check that the agent should not bypass.

### 00:48:36–00:50:16 — `/tree`

Pi's built-in `/tree` lets him jump to any earlier point in a conversation. He
can follow one line of inquiry, then return to the root or another point with
no summary, a normal summary, or a custom summary. He calls it close to
manual subagents: the human, rather than an agent, chooses the branches and
the context each branch gets.

For a code change, he begins with questions such as: where does the current
user action start, what is its code path, what owns a setting, and how does a
value move through that path? This creates an evidence base before the agent
writes a plan or code.

## Herdr: the surface for concurrent agent work

### 00:44:13–00:46:34

Herdr wraps the Pi sessions. Dillon describes it as a terminal multiplexer
for agent work. Its sidebar shows workspaces and agent sessions, including
whether an agent is running or blocked. That replaces the sound alerts he used
to notice when a tmux-based agent session finished.

He moved his old tmux key bindings into Herdr in one pass with an agent. The
point is not that everyone should replace tmux. It is that a tool which makes
parallel agent state visible can lower the cost of working across two or three
features or repos at once.

## Plannotator: make the artifact reviewable

### 00:46:42–00:47:22 — what it does

Plannotator opens a local web view for a file, a code diff, or the last agent
message. The reviewer can highlight a part, leave several comments, then send
the collected feedback back to the coding agent. It supports both plan review
and local code review.

### 00:50:28–00:54:18 — research and plan feedback

He uses `plannotator last` when Pi has produced a long code-path explanation.
The web view makes the explanation easier to read than a terminal scrollback.
He marks unclear or doubtful parts, saves the comments, then sends them back
as one feedback set.

He treats this as a human-controlled alternative to handing research to an
autonomous subagent. Pi investigates; he reads the result, asks the next
question, and decides when the model has enough context to plan. He then asks
for a detailed implementation spec and opens that spec in Plannotator for the
same comment-and-revise loop.

### 01:00:36–01:02:13 — why the interaction matters

The important part is not merely comments. Plannotator lets the reviewer mark
large parts of a whole plan or diff in their original place. That is easier
than quoting fragments into a small terminal chat box, and it keeps feedback
tied to the relevant text.

### 01:05:06–01:07:31 — local code review

After implementation, he opens `plannotator review` against `origin/main`.
He reads the local diff, adds comments on the lines or files he dislikes, sends
them to the agent, and repeats. This avoids pushing unfinished code only to
get a usable review screen. His first-pass review experiment has two tracks:
one agent checks the implementation against the spec; another checks it
against his coding standards. The human then reviews the resulting diff.

## The plan format: types and call paths first

### 00:54:18–01:00:43

His specs look closer to pseudocode than product requirement documents. For
each changed call path, he asks the agent to state:

- the current path and the proposed path;
- the types that will be added or changed;
- input and output types at each level;
- side effects and possible errors;
- validation, verification, and tests;
- the narrowest end-to-end slice that proves the feature before expansion.

He uses this because he does not trust current agents to choose good system
boundaries by themselves. The spec review lets him settle data flow and the
shape of the system before a large amount of code appears.

He also adds friction before a new abstraction. The agent should first check
whether a current interface can be extended, adapted, or repaired. He sees
agents too readily create many small, thin abstractions. His own design habit
is to centre a module on one core type; moving between several core types is a
signal that a new module may be needed.

## Wayfinder: split large work before writing one spec

### 01:08:11–01:10:12

He had started trying Matt Pocock's skills. `grill me` and `grill me with docs`
interview the user and keep testing what they are trying to build. Wayfinder is
for work too large for one planning session or one technical spec. It makes a
map of the open work: research, further interview or "grilling" sessions,
prototypes, and tasks. Throwaway prototypes can answer a specific question.
Only after those questions are resolved does it build toward a fuller text
spec and implementation issues.

This is a way to turn one vague large request into a small sequence of
questions with proof, rather than making a single broad plan look certain.

## Fit for this harness

The video describes an engineer who says he still reads every code diff. That
does not match your outcome-owner role, so do not copy that part as a duty.
Keep the structure and change the human checks:

- Use Pi or Codex to map the current path and write a reviewable plan.
- Use Plannotator to mark the plan, user copy, acceptance checks, and diff
  summary. Focus your comments on product meaning, risks, and missed paths.
- Require an agent-side check against the agreed spec and code standards.
- For lasting or high-harm work, add an independent technical review before
  release; do not treat an agent's own code review as enough proof.
- Use a Wayfinder-style map only when a request has several linked unknowns.
  For a clear small change, use the smaller plan → build → check loop.

This fits the existing [memory layer and harness configuration plan](../memory-layer-and-harness-configuration.md): human judgment stays with the
outcome owner, while durable instructions, checks, and decisions live in the
repo rather than in chat memory.

## Source markers

- 00:34:18 — workflow segment begins.
- 00:37:50 — Pi.
- 00:44:13 — Herdr.
- 00:46:42 and 00:50:28 — Plannotator and plan review.
- 00:54:18 — type-driven specs and call stacks.
- 00:59:46 — limits of agent-led abstraction.
- 01:05:06 — local code review.
- 01:08:11 — Wayfinder.
