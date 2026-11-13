# Four layers for turning LLM experiments into real-time decisions

Conf42 Blog, 2026-05-27, updated 2026-11-09. https://www.conf42.com/blog/llms2026/real-time-llm-decision-systems-architecture

In short: Mohanraj Varatharaj at Conf42 LLMs 2026 on streaming data, RAG, decision engines and observability for real-time LLM decision systems.

Most enterprises already run AI somewhere. The hard part is getting a model's output into a decision that happens in seconds instead of after a weekly report. At Conf42 Large Language Models (LLMs) 2026, Mohanraj Varatharaj, a lead software engineer with more than fourteen years on Spring Boot, Kafka and Flink backends, lays out a reference architecture for real-time decision systems built on LLMs, and the places it tends to break.

It's a broad overview with no single case study, which makes it a useful checklist for teams moving from pilots to production.

## From dashboards to decisions

Mohanraj traces the familiar path: static reporting (dashboards a human reads), batch ML (scheduled predictions), streaming analytics (near-real-time alerts, still handed to a human), and finally LLMs in the loop, building context from live streams and recommending decisions directly. Each step removes a manual handoff that turned a minutes-long decision into a days-long one.

## Four layers

His architecture has four components:

1. **Data ingestion.** Streaming pipelines such as Kafka, Kinesis or Flink normalise events from fragmented enterprise sources in real time.
2. **LLM reasoning.** Models with retrieval-based context generate structured recommendations from live operational signals.
3. **Decision engine.** Orchestration logic checks LLM output against business rules, confidence thresholds and governance constraints before anything acts.
4. **Observability.** Every decision is logged and traced, with drift, latency and decision quality tracked over time.

The decision engine is the layer worth copying first: the model recommends, and something deterministic decides whether that recommendation is allowed to act.

## Bad data, bad outcome

The data problems he lists will be familiar to anyone in a large organisation. The same customer transaction or product SKU lives under different schemas in different systems, and an LLM fed both gets confused. Real-time events joined to batch reference data create temporary inconsistencies: yesterday's inventory against today's demand. And when data comes from many teams, nobody is clearly accountable for its freshness or quality.

Governance comes in three tiers. Assisted means the AI suggests and a human decides (slow but safe). Supervised means the AI acts and humans review exceptions. Autonomous means the AI acts alone, with an audit trail so you can find and fix what went wrong.

## Where it breaks at scale

Four bottlenecks get named: provider rate limits that collapse under enterprise volumes, context window management, cold-start latency from serverless deployments that rules out tight SLAs, and the scaling pain of keeping session state across distributed services.

His design principles are concrete. Decouple inference from orchestration. Cache deterministic LLM outputs aggressively. Use async patterns for non-critical decisions. Set hard latency budgets per decision type. Add circuit breakers so a model call can't run forever.

On retrieval, he warns against over-fetching (noise) and under-fetching (missing context), recommends hybrid retrieval with re-ranking, and ties index updates to data changes. Semantic caching and hybrid routing, with local models for common cases and large ones for edge cases, keep cost and latency in check.

For failure, he wants deterministic fallbacks and graceful degradation to simpler models, because silent failure is the bigger risk. Input guardrails block prompt injection and out-of-scope requests; output checks use schema or regex validation plus quality scoring.

## Who should watch

Backend and platform engineers being asked to put an LLM on top of an existing event stream. The talk stays at architecture level, so pair it with something hands-on, but the closing advice holds: audit the data foundations first, define decision tiers before you build, and build observability from day one.

## Related Conf42 talks

- [Adding Generative AI to Real-Time Streaming Pipelines](https://www.conf42.com/Large_Language_Models_LLMs_2024_Tim_Spann_generative_ai_streaming) by Tim Spann, the ingestion and LLM layers wired together in practice.
- [Real-Time FinOps Intelligence: Template-Driven Prompt Engineering for Streaming Financial Events](https://www.conf42.com/DevOps_2026_Tina_Kanth_finops_streaming_prompts) by Tina Kanth, prompts over a live event stream.
- [Edge-Ready GenAI: Engineering Low-Latency Solutions for Resource-Constrained Environments](https://www.conf42.com/Machine_Learning_2025_Sai_KR_Pentaparthi_latency_solutions_genai) by Sai KR Pentaparthi, for the latency budget and local-model side.

[Watch Mohanraj Varatharaj's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Mohanraj_Varatharaj_realtime_decisions_llms)

[Watch the talk on YouTube](https://youtu.be/aNsdP7F6XAY).

## Watch the talk

[Building Real-Time AI Decision Systems with Large Language Models](https://www.conf42.com/Large_Language_Models_LLMs_2026_Mohanraj_Varatharaj_realtime_decisions_llms) at Conf42 Large Language Models (LLMs) 2026.
