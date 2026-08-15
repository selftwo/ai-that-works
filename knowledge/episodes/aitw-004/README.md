# Twelve Factor Agents

Status: curated from imported YouTube captions and the repository walkthrough.

Source episode: [`2025-04-22-twelve-factor-agents`](../../../2025-04-22-twelve-factor-agents)

## Purpose, audience, and message

Purpose: Explain agent systems as ordinary software loops with a model choosing the next structured action.

Audience: Software engineers moving prototypes into controllable production systems.

Message: Own the prompt, context, state, and control flow. Let the model recommend a next action, while deterministic code executes it and decides when to pause, resume, or exit.

## Tactical practices

- Model each turn as prompt in and structured JSON out. See 07:28 to 10:37.
- Dispatch actions with normal switch and loop code. See 10:19 to 11:07.
- Build the context window deliberately from application state. See 09:11 to 09:34.
- Keep tool execution in code rather than treating the model as the executor. See 07:53 to 08:18.
- Own control flow so workflows can pause, resume, branch, or end. See 25:11 to 25:27.
- Use structured outputs to turn human words into typed actions. See 14:16 to 14:38.

## Failure modes and limits

- Framework hidden prompts and state make behavior hard to inspect.
- A growing raw transcript wastes context and can carry irrelevant tool output forward.
- Giving the model direct execution authority weakens validation and access control.
- The twelve factors are design guidance, not a guarantee of correctness.

## Sources and uncertainty

Primary evidence: [caption transcript](transcripts/stitched.txt), [source README](../../../2025-04-22-twelve-factor-agents/README.md), and [step by step walkthrough](../../../2025-04-22-twelve-factor-agents/step-by-step/walkthrough.md). Caption speaker labels are absent.
