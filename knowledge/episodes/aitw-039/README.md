# Understanding Latency in AI Applications

Status: curated from the existing upstream transcript and supporting demo code.
The code shows the agent and schema used during the episode, but the repository
does not include benchmark output or the visual demonstrations.

Source episode: [`2026-01-06-latency`](../../../2026-01-06-latency)

## Purpose, audience, and message

Purpose: Explain how to find and reduce latency in AI applications, then show how
streaming and interface choices can improve perceived speed.

Audience: Engineers building interactive LLM or agent products where response time
affects user flow.

Message: Measure the real bottleneck, reduce input and reasoning tokens, arrange
shared context for caching, and stream the smallest complete unit that is useful to
the user.

## How the approach works

The episode separates actual runtime from perceived speed. It first covers request
architecture, prefetching, prompt caching, token count, and hidden reasoning tokens.
It then treats semantic streaming as a type and interface design problem. Data can
arrive incrementally, but a field should be exposed only when it forms a useful,
valid unit. The included BAML schema marks some fields with `@stream.done`, and the
Python sample runs a small synchronous coding agent for experimentation.

## Tactical practices

- Profile before optimizing. See 05:21 to 06:18.
- Use an event stream or stored event state when users need cancellation, queued
  input, and progress. See 06:55 to 10:08.
- Prefetch only safe read work. Block writes and discard prefetched work when the
  user changes the request. See 11:53 to 15:30.
- Arrange prompts from stable prefix to changing suffix. For repeated calls, warm
  the shared prefix with one request before starting the rest in parallel. See
  19:20 to 25:47.
- Reduce prompt tokens before applying smaller optimizations. See 26:13 to 27:45
  and 49:13 to 50:27.
- Inspect reasoning token use and lower reasoning effort when the task does not
  need it. See 28:49 to 30:48 and 01:06:14 to 01:07:44.
- Stream complete semantic units. An ingredient needs its amount and unit, while a
  prose instruction can stream token by token. See 39:31 to 44:40.
- Decouple data generation from UI generation so each can run separately and the
  first useful result can render. See 45:53 to 49:13.

## Failure modes and limits

- Optimizing an unmeasured part of the system can add complexity without changing
  user flow.
- Blind parallel requests can miss a shared prompt cache because all requests start
  before the cache is warm.
- Prefetching writes can cause real side effects before the user commits.
- Partial strings, numbers, or tool arguments can be invalid and can force fragile
  special cases into the interface.
- Reasoning summaries may add tokens rather than reduce the wait.
- A faster response can be worse if it is wrong. The right latency target depends
  on whether the user is interacting, waiting, or delegating.
- Cache thresholds and model behavior are provider details reported at recording
  time. They may change and should be measured again.

## Sources and uncertainty

Primary evidence: [source transcript](../../../2026-01-06-latency/transcript.md),
[episode metadata](../../../2026-01-06-latency/meta.md), and
[source README](../../../2026-01-06-latency/README.md).

Supporting evidence: [demo agent](../../../2026-01-06-latency/main.py),
[agent schema](../../../2026-01-06-latency/baml_src/agent.baml), and
[client configuration](../../../2026-01-06-latency/baml_src/clients.baml).

The transcript has clear timestamps but contains transcription errors. Provider
cache rules, model names, and reasoning controls are time bound to January 2026.
Performance numbers are speaker reports and were not reproduced.
