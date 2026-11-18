# Swap the AI monolith for a team of specialised agents

Conf42 Blog, 2025-09-01, updated 2026-11-09. https://www.conf42.com/blog/platform2025/multi-agent-ai-platforms-replace-monoliths

In short: Okta's Sidhanta Panigrahy at Conf42 Platform Engineering 2025 lays out a four-layer multi-agent architecture for AI platforms that fail in pieces, not all at once.

Monolithic AI platforms fail the way monolithic apps always have: one bad change, one exhausted resource, and everything goes down together. At Conf42 Platform Engineering 2025, Sidhanta Panigrahy, Director of Business Technology at Okta, argued for breaking the "one big AI system" into many small, specialised agents he calls microminds, coordinated by a dedicated layer so that a failure stays local.

It is an architecture talk at the level of patterns, not a framework demo. If you lived through the microservices migration, a lot of it will rhyme, and that is rather the point.

## Why the monolith stops scaling

Sidhanta's description of the bottleneck will be painfully familiar. As the codebase grows, an update that took a week stretches into a month because everyone competes for the same architecture and resources. A minor feature triggers regression testing across unrelated parts of the system. Tightly coupled systems fail completely. And there is an organisational cost: different business units have different AI needs, and one centralised system turns into a queue they all wait in.

## Four layers of agents

The core idea is that complex intelligence does not require one complex system. Instead you build many focused agents, each tuned for a specific problem, and connect them with a standard communication protocol (he points at MCP for agent communication), an intelligent coordination layer, and natural fault tolerance. He structures it as four layers:

- **Perception:** data ingestion, processing and first interpretation.
- **Cognition:** analysis, reasoning, decision making and domain-specific insight.
- **Action:** turning those decisions into concrete operations on external systems and business processes.
- **Coordination:** orchestrating the agents across all layers and adapting collaboration patterns to current conditions.

That split is the useful takeaway even if you never adopt the vocabulary. It gives you a place to put each responsibility and a boundary to fail at.

## Fail in pieces, recover in pieces

On performance, agents run in parallel on different resources, scale with actual demand, and idle when not needed, connected through message queues with compression so communication does not eat the gains. On reliability, the familiar patterns come back: graceful degradation, circuit breakers, continuous health monitoring and self-healing. The difference from a monolith is granular recovery. You restart one agent rather than the whole platform, and restore functionality incrementally while keeping downtime small.

Operating it is harder, and he says so. You need distributed tracing to follow one request across many agents, and correlation-based alerting that can tell a problem the system can absorb from one that needs a human. Security moves to zero trust between agents: each one has its own identity and dynamic permissions, there are distributed audit trails, and behavioural baselines flag anomalies.

## Getting there from here

Nobody rewrites a production AI platform over a weekend, so the legacy integration section matters. Sidhanta lists four strategies: adapter layers so agents and legacy systems can talk, data synchronisation between old and new components, an API gateway to centralise security and protocol translation, and event-driven messaging so the two worlds coordinate asynchronously. He is just as firm that the change is about people: skills programmes for running distributed systems, development processes adapted for interdependence, and pilots that prove value while keeping risk small.

## Who should watch

Architects and platform leads sketching how an AI platform should be decomposed, especially those already fighting a shared model service that every team depends on. The abstract promises live demos and Fortune 500 data; the recording is mostly the architecture and the patterns, which is where its value is.

## Related Conf42 talks

- [Jimmy Caputo (Harness) on agentic engineering platforms](https://www.conf42.com/Platform_Engineering_2026_Jimmy_Caputo_agentic_engineering_platforms), the platform team's view of agents a year later.
- [Rajesh Gupta (Skan AI) on going from agents to systems](https://www.conf42.com/MLOps_2026_Rajesh_Gupta_agents_orchestration_economics), with more on orchestration, recovery and cost.

[Watch Sidhanta Panigrahy's talk](https://www.conf42.com/Platform_Engineering_2025_Sidhanta_Panigrahy_microminds_monoliths_multi)

[Watch the talk on YouTube](https://youtu.be/NZvl0xFQBJg).

## Watch the talk

[From Monoliths to Microminds: Building Resilient AI Platforms with Multi-Agentic Architecture](https://www.conf42.com/Platform_Engineering_2025_Sidhanta_Panigrahy_microminds_monoliths_multi) at Conf42 Platform Engineering 2025.
