# LLM apps are distributed systems now, so trace the decision path

Conf42 Blog, 2026-08-20. https://www.conf42.com/blog/obs2026/llm-apps-are-distributed-systems-trace-them

In short: Princewill Kalio of Dockie at Conf42 Observability 2026 on observing LLM apps in three layers, from system telemetry to AI execution data to quality.

The model is no longer the application. At Conf42 Observability 2026, Princewill Kalio, Senior Software Engineer at Dockie, argued that a modern LLM app (retrieval, vector database, rerankers, semantic cache, tool calls, background workers, evaluation jobs) is a distributed system, and inherits every observability problem distributed systems have, plus one more: a perfectly healthy request can still produce a bad answer.

## From one function call to many boundaries

Kalio starts with the old mental model: prompt goes to model, response comes back, done. That was roughly true for early chatbots. Today a single question may be rewritten, routed through an API service, sent to a model that decides to call a tool or another specialised agent, embedded, matched against a vector store and reranked before anything is generated. Every hop is a boundary, and boundaries are where distributed systems fail: latency, retries, a third party having a bad day.

His point is that the failures he cares about look different at each boundary. The retrieval can succeed and still hand the model the wrong context, which then answers confidently and wrongly. Or retrieval is fine and the model guesses anyway. A database can be healthy while the AI step fails; a tool can work while the request to the model never gets as far as calling it.

## A trace is a decision path

That leads to the talk's most useful reframing. In a classic service, a trace is a request path: which services were hit and how long each took. In an LLM pipeline, Kalio treats the trace as a decision path: what was retrieved, what context the model actually read, which tools it called and what they returned, and how all of that led to the final output. If your telemetry cannot show that an agent pulled the wrong year of birth from the database, he says, your observability is broken, however green the latency panel looks.

## Three layers of signal

His model for an AI observability stack has three layers.

- **System telemetry** at the bottom: latency, errors, throughput, saturation, availability. Keep all of it.
- **AI execution telemetry** in the middle: model and version (did it drift or get deprecated?), tokens, prompts in and outputs out, retrieval results, tool calls and their results, cost.
- **Quality signals** on top: groundedness, relevance, guardrail compliance, including not leaking personal data.

Traditional telemetry asks whether the request executed properly. The top layer asks whether the result was good. He notes that tools such as Langfuse and Arize Phoenix are built around roughly this philosophy, but the principle matters more than the vendor.

## Evaluate continuously, and version your telemetry

Kalio wants evaluation running all the time, not once. In practice that can be a CI job that replays a dataset through the full pipeline (tools, embeddings, vector store) whenever you change a prompt, schema, tool or index, or a scheduled job that checks outputs hourly. If you are just starting out, the CI route is the cheap one.

His closing checklist is short and worth copying: preserve causality by carrying one identity across services, tools, workers and evaluation; instrument the boundaries where retries, state mismatches and third-party failures happen; trace the decision path, not just timing; separate system health from AI quality, since a 200 with a bad answer is both healthy and wrong; and treat telemetry as a production system of its own, with sampling, access control and versioning, so you can tell whether quality is improving or regressing over time.

## Who should watch

Backend and platform engineers inheriting an LLM feature who already know OpenTelemetry and want a mental model for what else to capture. It is a conceptual talk with no live demo, and a good one to hand to a team that still debugs its RAG pipeline like a single script.

[Watch Princewill Kalio's talk](https://www.conf42.com/Observability_2026_Princewill_Kalio_llms_rag_distributedsystems) ([YouTube](https://youtu.be/LrKiXKhgf6c)).

## Related Conf42 talks

- [RAG for Data Engineers: What It Is, Where It Fits, and Why Your Metadata Is the Missing Piece](https://www.conf42.com/Large_Language_Models_LLMs_2026_Varun_Joshi_rag_metadata) by Varun Joshi (AWS), LLMs 2026.
- [Correlation Over Collection: A Layered Observability Framework for SREs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Khushboo_Nigam_correlation_over_collection) by Khushboo Nigam (Oracle), SRE 2026.
- [Vector Embeddings and RAG Demystified](https://www.conf42.com/Machine_Learning_2025_Veliswa_Boya_rag_embeddings_vector) by Veliswa Boya (AWS), Machine Learning 2025.

## Watch the talk

[AI Systems Are Distributed Systems Now](https://www.conf42.com/Observability_2026_Princewill_Kalio_llms_rag_distributedsystems) at Conf42 Observability 2026.
