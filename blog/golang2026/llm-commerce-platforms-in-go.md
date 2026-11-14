# Go as the orchestration layer for LLM-driven grocery commerce

Conf42 Blog, 2026-04-25, updated 2026-11-09. https://www.conf42.com/blog/golang2026/llm-commerce-platforms-in-go

In short: Sanjay Basu of TCS at Conf42 Golang 2026 maps where Go services sit in LLM commerce, from search and catalog enrichment to substitution and agents.

When a shopper types something like "quick high protein for tonight", someone has to turn that into structured filters, a vector lookup, an inventory check and a ranked answer before the shopper gives up. [Sanjay Basu](https://www.conf42.com/Golang_2026_Sanjay_Basu_building_cognitive_commerce), Global Head for AI and GenAI Products at TCS, argued at Conf42 Golang 2026 that this is an architecture problem first and a model problem second, and that Go is a natural fit for the layer that does the coordinating.

It's a compact architecture tour, short on code and long on patterns. Treat it as a map of where Go services sit in an LLM-backed grocery and e-commerce stack, not as a build guide.

## Three layers, and Go owns the outer one

Sanjay's stack has a data layer at the core (vector store, point-of-sale feeds, everything else the models need), an LLM inference layer for model calls and streaming responses, and an orchestration layer of Go services around both. That outer layer does intent routing at the gateway, assembles context from user history and inventory state, and streams tokens straight to the client with no intermediary.

His reasons for Go are the familiar three: goroutines and channels for fanning out many simultaneous LLM calls, predictable low latency, and the operational simplicity of a single static binary. A single commerce request, he notes, may fan out into several model calls (classification, personalisation scoring, inventory-aware checks), and bounded worker pools plus context propagation keep that tractable without an external orchestrator.

## Four places the models earn their keep

The use cases are where the talk is most concrete:

- **Search and personalisation.** Natural-language queries become structured filters; clickstream, basket history and loyalty data are assembled in Go and injected into the prompt to ground it. Embedding generation runs on backend worker pools, and popular query embeddings get cached with a short TTL.
- **Catalog work at scale.** LLMs classify new SKUs into category trees and extract attributes from messy descriptions, images and spec sheets; Go pipelines then validate those attributes against the catalog schema and backfill gaps such as nutrition data and allergen flags.
- **Substitution and demand sensing.** When an item is out of stock, an LLM-backed service ranks alternatives by semantic similarity, dietary compatibility and price or margin delta, with a target of under 200 milliseconds.
- **Fulfilment and agents.** Order, picking, dispatch and last-mile stages pass events over channels with queues and circuit breakers between them. LLM agents interpret pick exceptions and slot conflicts, while Go services execute the approved actions with full audit trails.

## Autonomy needs more guardrails, not fewer

The closing caveats are the part to remember. Design for streaming, fan-out and context assembly before choosing a model. Autonomous agents need stronger observability and stricter circuit breaking, and Go services are the enforcement layer. And govern cost from day one: trace every LLM call end to end with OpenTelemetry, tie token spend to business outcomes, and build token budgets, model tiering and per-intent routing into the gateway before the first production deployment. Every CIO complaining about token bills is the joke, and it isn't really one.

## Who should watch

Architects and Go engineers adding LLM features to retail or marketplace backends who want a vocabulary for the moving parts. If you need benchmarks, code or a case study with numbers, this isn't that talk.

## Related Conf42 talks

- [Golang-Powered Retail Distribution: Transforming Supply Chains Through Cloud-Native Innovation](https://www.conf42.com/Golang_2025_Srinivas_Ankam_retail_distribution_supply) by Srinivas Ankam, the supply-chain end of the same retail stack.
- [The Retry Storm That Ate My Budget](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) by Yamini Rathamsetty and Karthik Akula, on what ungoverned token spend looks like.
- [Cloud-Powered Retail: Serving Future Needs Today](https://www.conf42.com/Cloud_Native_2025_Rustam_Orudzhev_retail_services_optimization) by Rustam Orudzhev, for the cloud side of retail platforms.

[Watch Sanjay Basu's talk](https://www.conf42.com/Golang_2026_Sanjay_Basu_building_cognitive_commerce)

[Watch the talk on YouTube](https://youtu.be/QMoVgGVHkO8).

## Watch the talk

[Building Cognitive Commerce Platforms in Go: Architecting LLM-Driven Intelligence for Grocery Retail and E-Commerce](https://www.conf42.com/Golang_2026_Sanjay_Basu_building_cognitive_commerce) at Conf42 Golang 2026.
