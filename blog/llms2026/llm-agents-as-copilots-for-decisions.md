# Put LLM agents in decision systems as copilots, not deciders

Conf42 Blog, 2026-05-25, updated 2026-11-09. https://www.conf42.com/blog/llms2026/llm-agents-as-copilots-for-decisions

In short: Mazdul Choudhury (Walmart) at Conf42 LLMs 2026 lays out a three-layer architecture for LLM copilots in forecasting and planning workflows.

The hard question about LLMs in the enterprise has moved on from whether a model can answer a question. It is whether it can support thousands of business decisions a day within cost, latency, governance and stability limits. At Conf42 Large Language Models (LLMs) 2026, Mazdul Choudhury, Staff Product Manager at Walmart, answers with an architecture: LLM agents as copilots inside decision workflows, with humans keeping the judgment and the accountability.

This is a product manager's framework talk. There's no code and no Walmart-specific numbers; what you get is a clean structure for taking an agent from demo to something an operations team will actually use.

## Copilot is a job description

Mazdul's definition is precise. A copilot gathers information, evaluates options, highlights tasks and surfaces recommendations. It doesn't replace people and doesn't make autonomous decisions. Humans own the call; the agent helps them process complexity faster and more consistently.

He uses forecasting and operational planning as the running example, because it mixes structured data (demand signals, operational metrics) with unstructured inputs (external events, market conditions, human expertise). The same pattern, he says, carries over to supply chain, capacity planning and risk management.

## Three layers that can change independently

The architecture matters more than the model choice, in his view, and it has three layers:

1. **Signal aggregation.** Continuously collect structured data (transactions, forecasts, metrics) and unstructured data (documents, reports, logs, communications) into one queryable context layer. Without good context, model sophistication doesn't help.
2. **Agent reasoning.** The LLM evaluates the context, generates forecasts, detects anomalies and recommends actions, and every output carries its rationale. If users can't see why, they won't act on it.
3. **Human interaction.** Users query the system, explore scenarios, validate assumptions and give feedback. This is the layer that stops the system being a black box, and where trust gets built.

Keeping the layers separate makes the whole thing more resilient and easier to deploy.

## Four production problems that tests won't show

Hallucination, decision consistency, latency and cost show up in production however well the model did in testing. His answers:

- **Grounding** is the most important hallucination fix: RAG, structured queries and authoritative internal sources, treated as an ongoing discipline around freshness and monitoring.
- **Multi-step orchestration**: retrieve context, plan, call tools, synthesise. It mirrors how an analyst works, but runs continuously.
- **Additive integration**: wrap existing systems instead of replacing them, deploy in shadow mode, and keep deterministic fallbacks.
- **Progressive maturity**: focused prototype, shadow deployment, human-in-the-loop validation, then scale with monitoring and governance. Jumping straight from prototype to production is, in his telling, why most AI initiatives fail.

His four takeaways fit on a sticky note: architecture before models, ground everything in enterprise data, integrate additively, and measure accuracy, latency, cost and human trust continuously.

## Who should watch

Product managers and engineering leads scoping their first agent inside an existing planning or operations workflow, especially if stakeholders are nervous about autonomy. Engineers after implementation detail should treat this as the map and look elsewhere for the territory.

## Related Conf42 talks

- [Human-in-the-Loop MLOps: Production Patterns](https://www.conf42.com/MLOps_2025_Tejasvi_Nuthalapati_human_loop_mlops) by Tejasvi Nuthalapati, on the human layer in practice.
- [Transforming Inventory Forecasting with Production ML](https://www.conf42.com/Machine_Learning_2026_Pallab_Haldar_orchestration_workflows_ai) by Pallab Haldar, the forecasting use case with classic ML.
- [AgentCast: Autonomous AI-Driven Time Series Forecasting for DevOps at Scale](https://www.conf42.com/DevOps_2026_Premanand_Tiwari_forecasting_time_autonomy) by Premanand Tiwari, a more autonomous take on agents that forecast.

[Watch Mazdul Choudhury's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Mazdul_Choudhury_copilots_decision_agents)

[Watch the talk on YouTube](https://youtu.be/6nLRZtMYfmw).

## Watch the talk

[LLM Agents as Co Pilots for Scalable Decision Systems in Production Environments](https://www.conf42.com/Large_Language_Models_LLMs_2026_Mazdul_Choudhury_copilots_decision_agents) at Conf42 Large Language Models (LLMs) 2026.
