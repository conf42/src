# One intent layer instead of a dozen disconnected copilots

Conf42 Blog, 2026-03-26, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/intent-orchestration-ends-the-copilot-sprawl

In short: Dhivya Dhayakar of Zscaler at Conf42 Cloud Native 2026 on intent-based orchestration, smart model routing and trajectory evals for enterprise agents.

Every business unit built its own bot, none of them talk to each other, and the human manager has become the integration layer. At Conf42 Cloud Native 2026, Dhivya Dhayakar, Senior AI Product Manager at Zscaler, presented intent-based orchestration as the architectural answer: a single layer that interprets what the user wants, plans the steps and routes them to specialist agents, with a human gate in front of anything high-stakes.

It is an architecture talk from a product manager's seat, so expect patterns and a phased roadmap rather than code.

## The tangled cables and the intelligence tax

Dhivya names two failure modes of today's copilot sprawl. The first is brittleness: point solutions that break when a process changes slightly or a query gets complicated. The second she calls the intelligence tax, the cost and latency of sending simple, repetitive tasks to a large model when a small one would do. Users, meanwhile, give up on remembering which of many agents does what.

Her running example is employee onboarding. Today the manager stitches together IT, HR and finance automations, some integrated and some not, and any step off the predetermined path breaks the flow. In the orchestrated version, the agent understands the goal (onboard this person) and adapts when individual steps change, while the manager moves from coordinator to overseer.

## Six parts of the middle layer

The architecture is a layer cake: enterprise tools and data at the bottom, channels and UX on top, and a unified orchestration layer in the middle that she calls the brain. Inside it she lists six components:

- intent intelligence that decomposes a complex request and plans steps;
- a multi-agent orchestrator acting as the harness for task-specific agents;
- a specialized agent pool;
- a tools and skills registry, one catalogue for the enterprise;
- adaptive memory so context survives handoffs and pauses;
- a human-in-the-loop policy gate for high-stakes actions.

The orchestrator plans through prompt chaining, then runs a self-reflection loop where the reasoning engine critiques its own plan before any tool is called. Memory has three tiers: session context, an experience store that remembers reasoning paths that worked before, and retrieval for live facts.

## Route by reasoning depth, not by habit

The fix for the intelligence tax is a smart router with a cost logic fork: simple, low-reasoning work goes to cheaper small language models, while ambiguous tasks on critical workflows go to large models with deeper reasoning. Her point is predictability as much as savings: no surprise bills once the system is in production.

## The onboarding flow, with a pause in the middle

The demo scenario is the best part. A supervisor agent issues formal contracts to task-specific agents, and those contracts bound resource use so agents do not fall into expensive infinite loops. At each handoff the harness checks for gaps. If the IT agent requests confidential system access without justification, the harness asks for clarification of intent; because the access is high-stakes, it then triggers a cascading human-in-the-loop pause, persists the distributed state of the whole agent hierarchy, and shows the reviewer an immutable audit trail of what has happened so far. After approval, the supervisor finishes provisioning and payroll on its own.

She also argues for generative UI, treating front-end components as skills in the registry, so a finance risk question renders as a dashboard and an HR checklist renders as a document view.

## Evals that score the path, not just the answer

Accountability rests on trajectory evals: score the route an agent actually took against a predetermined policy graph, so an agent that reached the right answer by an unapproved path still fails. Combined with immutable audit trails, that gives regulators and internal reviewers something to inspect. Her roadmap runs in four phases: intent and retrieval, then orchestration with registries, then high-stakes actions with human accountability, then scale and governance.

## Who should watch

Architects and platform teams inheriting a zoo of departmental bots, and anyone designing human approval into agent workflows. If you already run multi-agent systems with trajectory evaluation, the talk is a tidy reference model rather than new ground.

## Related Conf42 talks

- [Michael Haim on orchestrating AI agents with pattern matching](https://www.conf42.com/AI_Agents_2026_Michael_Haim_orchestration_patterns_determinism) at Conf42 AI Agents 2026.
- [Mazdul Choudhury on LLM agents as co-pilots for decision systems in production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Mazdul_Choudhury_copilots_decision_agents) at Conf42 Large Language Models 2026.
- [Morgan Willis on production-ready architectures for agents you should not trust](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) at Conf42 AI Agents 2026.

[Watch Dhivya Dhayakar's talk](https://www.conf42.com/Cloud_Native_2026_Dhivya_Dhayakar_ai_llm_prompts)

[Watch the talk on YouTube](https://youtu.be/N8GpuF7V_k0).

## Watch the talk

[Cloud-Native Intent Orchestration for Enterprise AI Ecosystems](https://www.conf42.com/Cloud_Native_2026_Dhivya_Dhayakar_ai_llm_prompts) at Conf42 Cloud Native 2026.
