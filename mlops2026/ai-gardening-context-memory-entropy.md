# AI gardening: agent context drifts, so prune it on purpose

Conf42 Blog, 2026-11-09. https://www.conf42.com/mlops2026/ai-gardening-context-memory-entropy

In short: Ishan Shah (PayPal) at Conf42 MLOps 2026 on AI Gardening: treating context and memory in long-running agent workflows as production state you maintain.

Long-running agent workflows rarely crash. They drift. At Conf42 MLOps 2026 on November 19, Ishan Shah, Staff Software Engineer at PayPal, names the discipline for dealing with that: AI Gardening, the ongoing work of deciding what context gets into an agentic system, what expires, what is kept for audit, and when memory gets reset.

## The failure that doesn't page anyone

The opening line of the abstract sets it up well: most AI demos are short, and production MLOps and agentic workflows are not. Over time, a long-running system accumulates instructions, retrieved documents, tool outputs, partial plans, stale assumptions and memory from earlier work.

None of that looks like a normal service failure. The system keeps responding. Tools keep working. Your dashboards stay green. The workflow just becomes slowly harder to reason about, because its context has wandered away from what anyone intended.

That is a nasty class of problem for an on-call engineer. There is no error to grep for, only behaviour that feels a bit off, and a transcript long enough to make you give up scrolling.

## Gardening, not bulldozing

The metaphor earns its keep. You do not fix a garden once; you prune, weed and decide what stays. Ishan applies that to the operational environment around an LLM workflow once it moves past a single prompt. The questions he puts on the table:

- What context is allowed into a workflow in the first place?
- What should expire, and when?
- What must be preserved for audit?
- When should memory be scoped, and when should it be reset?
- How do you detect contradictory instructions piling up?
- How do you make working state inspectable during real engineering tasks?

He is careful about the goal. The point is not to make probabilistic systems pretend to be deterministic. The point is to make the environment around them maintainable, with bounded context windows, explicit memory ownership, reset boundaries, retrieval evaluation, artifact handoffs, and enough evidence that a human can understand why the system behaved the way it did.

## Context is production input

The takeaway checklist is short and sharp. Treat context as production input, with the same suspicion you give to user data. Separate durable knowledge from temporary working state. Make memory auditable. Design reset paths before drift turns into a failure mode. And give humans a clear way to inspect state, instead of asking them to trust a transcript.

That last point is the one many teams skip. Telling someone to read the conversation log is homework, not an inspection tool. A system that exposes its working state directly is one you can actually operate.

## Who should watch

Engineers running agents that live longer than a single request: coding agents on big tasks, research pipelines, anything with persistent memory. MLOps and platform people who will be asked to own those systems after the demo is over. If your LLM use is single-shot prompts, file this one for later.

## Related Conf42 talks

- [Make Agents Remember the Right Context at the Right Time](https://www.conf42.com/Large_Language_Models_LLMs_2026_Anannya_Roy_Chowdhury_memory_agents_context) by Anannya Roy Chowdhury, the memory-design side of the same coin.
- [Make Agents Remember the Right Context at the Right Time](https://www.conf42.com/Large_Language_Models_LLMs_2026_Anannya_Roy_Chowdhury_memory_agents_context) by Anannya Roy Chowdhury, on choosing what an agent should recall and when.
- [Prompt Drift Kills: How to Make Prompts Stable](https://www.conf42.com/Prompt_Engineering_2026_Sachin_Gupta_drift_prompts_stable) by Sachin Gupta, drift seen from the prompt layer.

Ishan has spoken at Conf42 before, too: his [Feature Flags as Incident Evidence](https://www.conf42.com/Feature_Flags_2026_Ishan_Shah_flags_incident_rca) talk from Conf42 Feature Flags 2026, on governing AI-assisted root cause analysis, is a good companion.

[Watch Ishan Shah's talk](https://www.conf42.com/MLOps_2026_Ishan_Shah_gardening_context_memory) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[AI Gardening for MLOps: Managing Context, Memory, and Entropy in Agentic Systems](https://www.conf42.com/MLOps_2026_Ishan_Shah_gardening_context_memory) at Conf42 MLOps 2026.
