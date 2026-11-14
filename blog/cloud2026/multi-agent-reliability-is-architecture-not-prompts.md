# Multi-agent systems fail in the architecture, not the prompt

Conf42 Blog, 2026-03-28, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/multi-agent-reliability-is-architecture-not-prompts

In short: Sandeep Mannapur of ServiceNow at Conf42 Cloud Native 2026 on taking a chatbot to orchestrated agents: circuit breakers, timeout budgets, decision-aware traces.

A four-agent system can turn a two-second request into a twenty-second one, and its dashboards can be all green while it confidently returns the wrong answer. At Conf42 Cloud Native 2026, Sandeep Mannapur, AI and ML Engineer at ServiceNow, walked through how an order-support platform grew from a monolithic chatbot into a centrally orchestrated multi-agent system, and why the fix was architecture rather than a smarter model or a better prompt.

## What the demo hides

Sandeep lists the problems every team hits after the prototype: orchestration logic that spreads across services and becomes the most fragile part of the system, latency that compounds with every agent hop, and failures that propagate when one agent's half-wrong output is passed downstream as if it were valid input.

The monolith failed in a specific order. Conversations that worked at 10 turns broke at 40 because the model was reasoning over tens of thousands of tokens of history. One agent asked to do order lookup, escalation logic, resolution drafting and customer communication became mediocre at all of them. And with no isolation, a single failed tool call took down the whole interaction, with no way to scale escalation separately from status lookups.

## Pick the boring orchestrator

On centralized orchestration versus decentralized swarms, his verdict is clear for operational workflows: centralize. Swarms look good on paper, with more parallelism and no single point of failure, but emergent behaviour is hard to predict, conflicting outputs have no resolution path, and tracing a fault through peer-to-peer chatter is miserable. If agents update real records, you want deterministic control flow and someone clearly accountable.

The resulting design has five layers: an orchestrator that only decomposes, routes and assembles (it never runs domain logic itself); specialist agents that get only the context they need and never read a sibling's state; tools exposed through MCP; agent-to-agent calls over A2A so a LangGraph agent can call a CrewAI agent through the same interface; and a response aggregator that validates everything before it reaches production.

## Four ways to stop one bad agent sinking the rest

- **Circuit breakers** around every agent call, so the orchestrator stops hammering a degraded agent with retries and routes to a fallback.
- **Sandboxing**: no shared in-memory state; inter-agent traffic goes through a durable message bus.
- **Timeout budgets** propagated from the orchestrator, with a degraded mode when an agent overruns.
- **Fallback reasoning paths**: a simpler, lower-capability agent with minimal tooling that keeps critical flows answering when the primary fails.

None of this is new to anyone who has run microservices. That is rather the point: agents are distributed systems with an unusually creative failure mode.

## Trace the decision, not just the call

The sharpest section is on observability. CPU, memory, latency and error rates can all look healthy while outputs are wrong, because correctness depends on the reasoning path. Sandeep wants traces that record which agent was invoked and why, what context it received and what was left out, which tools it called with which parameters, and how the orchestrator resolved conflicting answers. A shared identifier propagates across hops so you can rebuild the full chain. Jaeger and Zipkin will tell you Agent B was called; they will not tell you what Agent B decided. You need both layers.

## Laptop to cloud is a different problem

Locally it is SQLite checkpoints, in-process tools and a local model. In production it becomes Postgres, containerized MCP microservices, A2A servers on cloud functions or Kubernetes pods, stateless orchestrator containers and managed inference behind a gateway such as LiteLLM. He flags three cloud-only traps: token cost compounding (four agents with five tool calls each is 20 or more LLM calls per request, so per-agent token budgets must be hard limits), checkpoint formats that break in-flight workflows during rolling deploys (version them like public APIs), and agent containers that can take 30 to 60 seconds to cold start.

His validated stack is LangGraph, MCP, A2A, LiteLLM, Langfuse and DeepEval, with the caveat that the patterns matter more than the logos. Governance closes it out: schema validation gates on every output, human approval thresholds for high-risk actions, and immutable audit logs.

## Who should watch

Anyone whose agent prototype is about to meet real traffic, and SREs asked to run one. If you have built resilient microservices, much of it will feel familiar, which makes it a fast and useful translation guide.

## Related Conf42 talks

- [Vsevolod Voropaev on why agentic verifiers silently rot in production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) at Conf42 Large Language Models 2026.
- [Artemis Leonardou on checking an agent's action before it runs](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) at Conf42 DevSecOps 2026.
- [Andrew Robinson on fault isolation using shuffle sharding](https://www.conf42.com/Site_Reliability_Engineering_2021_Andrew_Robinson_fault_isolation_shuffle_sharding) at Conf42 Site Reliability Engineering 2021.

[Watch Sandeep Mannapur's talk](https://www.conf42.com/Cloud_Native_2026_Sandeep_Mannapur_ai_agents_workflows)

[Watch the talk on YouTube](https://youtu.be/US93h8Dbh14).

## Watch the talk

[Engineering Production-Grade Multi-Agent Systems in the Cloud](https://www.conf42.com/Cloud_Native_2026_Sandeep_Mannapur_ai_agents_workflows) at Conf42 Cloud Native 2026.
