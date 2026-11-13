# Sealed types and pattern matching as the control layer for agents

Conf42 Blog, 2026-08-26, updated 2026-11-09. https://www.conf42.com/blog/agents2026/orchestrate-agents-with-pattern-matching

In short: Michael Haim of Zindell Technologies at Conf42 AI Agents 2026 routes, retries and judges AI agents with Java sealed types and switch patterns.

You can't orchestrate agents with a plain `if` when the thing you're branching on is free text. At Conf42 AI Agents 2026, Michael Haim, founder and CEO of Zindell Technologies and a university lecturer for more than twenty-five years, showed how to turn agent output into a small set of typed results and let pattern matching decide what happens next.

The talk is a code walk-through in Java with LangChain, built as five runnable samples. The idea travels: Michael notes the same approach works in C#, Kotlin, Scala or Python.

## Completeness is the feature you want

The first half is a crisp refresher on modern Java pattern matching, and it is there for a reason. A `switch` expression over a sealed type must cover every permitted subtype, or it doesn't compile. Remove `sealed` from the interface and the compiler rightly complains, because someone could add a type you never handled.

Michael's point for agents: limit the possibilities. An agent result is an `Answer`, a `Clarification` or an `Error`, each a record nested inside a sealed `AgentResult`. Raw model output gets parsed into exactly one of those, and the handler is a switch the compiler checks for you. Guarded patterns (`case X when score > 7`) add conditions, record deconstruction pulls fields straight into local variables, and the unnamed `_` keeps cases tidy when you don't need the binding. Each is a small tool for turning chaos into something closer to deterministic, as he puts it.

## A pipeline is a loop over message types

The second sample is a planner, coder and reviewer chained together. Every message between agents is one of four records under a sealed `AgentMessage`: a plan request, a code request, a review request and a final result. A `step` function switches on the current message, calls the right agent, and returns the next message. The loop runs until the current message is a `FinalResult`.

It is a state machine wearing record syntax, which is the compliment. You can read the whole control flow in one switch, and the agents never decide who goes next.

## Routing, retries and a judge, all in the same shape

The remaining samples reuse the pattern:

- **Router.** A router agent classifies each input into a sealed `TaskClassification` (translate or summarise), and a switch dispatches to the translator or summariser agent.
- **Retry loop.** A coder writes code, a reviewer returns a decision, and the outcome becomes `Approved` or `Rejected`. A guarded case separates "approved with a high score" from plain approval, and a rejection re-invokes the coder with the reviewer's feedback until `maxAttempts` runs out, then returns the last attempt with a warning. No unbounded loops.
- **Fan-out with a judge.** Two agents solve the same task, a judge agent returns a verdict that can only be `PickedA` or `PickedB`, and a switch selects the winner and its reason.

Each demo runs live, and in the retry sample the reviewer approves the first attempt with a score of ten, which is the most cheerful thing an AI code reviewer has ever done.

## Why this matters beyond Java

The abstract frames the bigger claim: treat agents as components in a deterministic system and make pattern matching the control layer, so behaviour is predictable, maintainable and auditable. The model stays probabilistic; the routing doesn't. That makes traces easier to read and the failure paths explicit, because every odd model reply has to land in a named case.

## Who should watch

Backend engineers wiring their first multi-agent flow, especially on the JVM, and anyone whose orchestration currently lives in string checks on model output. If you already know sealed interfaces and records, skip ahead to the agent samples. Michael shares the code and recommends stepping through each sample in a debugger, which is good advice for a talk this hands-on.

## Related Conf42 talks

- [Agents That Check Their Own Work: The Validator Pattern](https://www.conf42.com/MLOps_2026_Shipra_Sonal_Madhu_Gurramkonda_validator_agents_pattern) by Shipra Sonal and Madhu Gurramkonda at Conf42 MLOps 2026.
- [From Agents to Systems: Orchestration, Recovery, and Economics](https://www.conf42.com/MLOps_2026_Rajesh_Gupta_agents_orchestration_economics) by Rajesh Gupta at Conf42 MLOps 2026.
- [Your AI Has Too Much Access: Deterministic Authorization for Coding Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents) by Sohan Maheshwar at Conf42 Large Language Models 2026.

[Watch Michael Haim's talk](https://www.conf42.com/AI_Agents_2026_Michael_Haim_orchestration_patterns_determinism) from [Conf42 AI Agents 2026](https://www.conf42.com/agents2026).

[Watch the talk on YouTube](https://youtu.be/Ef2ee-uObLo).

## Watch the talk

[Orchestrating AI Agents with Pattern Matching](https://www.conf42.com/AI_Agents_2026_Michael_Haim_orchestration_patterns_determinism) at Conf42 AI Agents 2026.
