# Founding HumanLayer: Dex's Journey

Status: curated from the existing upstream transcript. Claim verification is
transcript only. The transcript source, model, cleanup history, and exact recording
start are not recorded upstream.

Source episode: [`2025-12-23-founding-humanlayer`](../../../2025-12-23-founding-humanlayer)

## Purpose, audience, and message

Purpose: Trace Dex's path from engineering roles through HumanLayer's first product
and into CodeLayer, while extracting lessons about developer tools, pivots, agent
architecture, product discovery, and cofounder selection.

Audience: Technical founders and engineers building agent products, especially
people testing an early market, changing product direction, or introducing coding
agent workflows to a team.

Message: Work directly on the problem you care about, distrust abstractions until
real users validate them, shorten the build and feedback cycle, and use human
judgment where current agent workflows still need context or control.

## Journey and product changes

Dex moved from physics into software through coursework and on-the-job learning. At
Sprout Social he worked on a greenfield internal project. Later roles deepened his
interest in developer productivity and software delivery. He then founded
Metalytics, an agent for SQL data warehouse work, and extracted its human approval
system into HumanLayer.

HumanLayer's original service found the right person through channels such as Slack
and returned approval or feedback to an agent. Customer discovery showed that
reliable production teams had bespoke and more deterministic agent designs. Using
the service often required them to restructure applications around asynchronous
callbacks. That experience led to the 12 Factor Agents material. Experiments with
the Claude Code SDK, RPI, and session management then led the company toward
CodeLayer.

## Tactical practices

- If the desired work is already clear, start doing it instead of designing a long
  sequence of preparatory roles. See 06:29 to 07:26 and 10:19 to 11:14.
- Use onboarding work that crosses the system or exposes many small failures. Both
  approaches can teach a code base when someone designs the learning path. See
  03:11 to 04:35.
- Observe the highest impact internal work. Dex's interest in developer tools came
  from seeing engineers improve sandboxes, deployment, and team velocity. See
  07:30 to 08:55.
- Test product ideas through problem interviews and fast execution. HumanLayer's
  initial pivot followed direct interviews, an MVP, and early revenue rather than a
  settled product thesis. See 11:14 to 14:35.
- Break agent work into controlled steps and use deterministic code where the
  workflow is known. See 17:20 to 21:31.
- Use MCP to extend a product when users choose unknown integrations. If the
  application already knows the tools and workflow, prefer direct code or an SDK.
  See 21:31 to 23:04.
- Rebuild fresh code base context for a task when standing documentation is likely
  stale. Parallel research can produce task-specific inputs for later planning or
  implementation. See 24:59 to 28:16.
- Pair a code base expert with a workflow expert when teaching agent-assisted
  development. Let the code base expert correct context directly. See 32:35 to
  35:28.
- Choose a cofounder through observed work, shared standards, and complementary
  strengths rather than a forced match. See 36:13 to 41:24.
- Watch customers use the product and shorten the build to feedback loop. This both
  exposes defects and confirms which value is real. See 46:39 to 49:15.

## Failure modes and limits

- A standard interface does not create product fit when serious users use different
  architectures or need tighter control than the abstraction provides.
- HumanLayer's callback design required clients to save state and restructure work
  around asynchronous responses. For many prospects, integration cost exceeded the
  value they expected.
- Documentation accumulates errors as code changes. Static agent instructions can
  become another stale source unless they avoid code-specific facts or are rebuilt
  from current source.
- Long prompts can exceed a model's practical instruction following capacity. Dex
  describes splitting planning into smaller workflow steps and using program
  control flow for branching.
- A tool can work for an expert pair yet remain hard to teach across a large
  company. Product support, training, and smaller workflow stages remain separate
  problems.
- Competitive social media can distort a founder's view of progress. Customer use
  provides more direct evidence.
- This is a founder narrative. Revenue, customer counts, product performance, and
  career events are speaker reports and were not independently checked.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2025-12-23-founding-humanlayer/transcript.md),
[episode metadata](../../../2025-12-23-founding-humanlayer/meta.md), and
[source README](../../../2025-12-23-founding-humanlayer/README.md).

No code, diagrams, company records, or product traces are stored in this episode
folder. Several product names are transcribed inconsistently. Future product plans
were statements made on 2025-12-23 and should not be read as current availability.
