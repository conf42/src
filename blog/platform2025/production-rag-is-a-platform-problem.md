# Production RAG at enterprise scale is a platform engineering job

Conf42 Blog, 2025-08-14, updated 2026-11-09. https://www.conf42.com/blog/platform2025/production-rag-is-a-platform-problem

In short: Srinivas Chennupati of Fannie Mae at Conf42 Platform Engineering 2025 on scaling enterprise RAG: vector stores, caching, model routing, cost per query.

Getting a retrieval-augmented generation demo to answer one question is an afternoon. Getting it to answer ten thousand people in under two seconds without leaking a document is a platform. At Conf42 Platform Engineering 2025, Srinivas Chennupati, a platform architect at Fannie Mae with over 14 years in the industry, laid out the infrastructure strategies that take RAG from notebook to enterprise knowledge service.

## Why RAG, and why it is hard at scale

Chennupati starts with a short primer: retrieve relevant snippets from internal documents, PDFs and emails, pass them to the LLM as context, and the answer is grounded in your facts instead of stale training data. He cites hallucination rates as high as 27% as the reason enterprises reach for it.

Then the hard part. A production system has to cover terabytes of repositories, keep queries under a second or two, stay up, and serve 10,000-plus concurrent users. None of that is solved by a better prompt.

## Four pillars under the vector store

The infrastructure section builds on four ideas:

1. **Distributed vector databases.** Shard embeddings across nodes for horizontal scale; Weaviate, Pinecone and similar systems trade off scalability, latency and cost differently.
2. **Load balancing** that routes queries across database clusters, pipelines and LLM instances so no single tier becomes the bottleneck.
3. **Hybrid storage.** Hot embeddings on SSD, the rest on cheaper cold storage.
4. **Elastic scaling.** On Kubernetes, the vector store, retrievers, rerankers and LLMs scale independently, because they never get busy at the same time.

## From 12 seconds to under two

The performance section is the one to steal from. Chennupati describes cutting query times from eight to twelve seconds down to under two with layered tricks:

- **Caching at two levels:** query-level caching (hashed) for repeated questions, embedding-level caching for frequently retrieved documents.
- **Hierarchical retrieval:** a cheap coarse filter first, fine-grained ranking second, so you compare far fewer vectors.
- **Dynamic model routing:** small LLMs for lightweight queries, large ones only for the complex ones.
- **Placement:** retrieval and inference closer to the data, via edge or regional clusters.

Model routing doubles as the main cost lever. Together with autoscaled inference endpoints, open-source models for routine queries, volume discounts from vector database and cloud vendors, and careful placement across on-prem GPUs and cloud, he puts the achievable saving at up to 60%.

## Treat it like any other tier-one service

The reliability advice will sound familiar to SREs, which is the point. Metrics on embedding throughput, vector search latency and inference time in Prometheus and Grafana. Replicated clusters with automatic failover. Checkpointing embeddings so an outage does not mean re-indexing everything. Chaos testing of the retrieval pipeline with simulated node failures and network partitions. Version-controlled pipelines deployed through CI/CD and Terraform.

Security gets the same treatment: zero trust between RAG components, encryption of embeddings at rest and in transit, role-based access that respects existing enterprise data governance, audit logs for SOC 2 and ISO 27001, and masking sensitive data in logs. An embedding of a confidential memo is still a confidential memo.

## Benchmark five things before you ship

His closing framework is a short list worth pinning to a wall. Measure end-to-end query latency under different loads, retrieval accuracy against ground truth, throughput at peak concurrency, resource utilisation across compute, memory and storage, and cost per query at different scales. Then set SLAs before launch.

From more than 50 enterprise implementations he reported adoption around 85% when RAG lives inside existing tools (Slack bots, CRM plugins, knowledge portals) and ROI of 200 to 400% within 18 months. Those are aggregate claims rather than a single walked-through case, so treat them as direction, not a benchmark.

## Who should watch

Platform and infrastructure engineers who just inherited "the AI knowledge base" from a data science team will get a sane checklist. If you want code, retrieval evaluation methods or a specific vendor comparison, this is the wrong talk: it is an architecture overview, delivered quickly.

## Related Conf42 talks

- Ofer Mendelevitch on [measuring hallucinations in RAG](https://www.conf42.com/Large_Language_Models_LLMs_2024_Ofer_Mendelevitch_rag_measuring_hallucinations) at LLMs 2024.
- Stephen Batifol's [Vector Databases 101](https://www.conf42.com/Machine_Learning_2024_Stephen_Batifol_vector_databases_work) at Machine Learning 2024, if the vector tier is new to you.
- Vaibhav Fanindra Mahajan on [observable RAG for customer support](https://www.conf42.com/Observability_2025_Vaibhav_Fanindra_Mahajan_rag_chatbots) at Observability 2025.

[Watch Srinivas Chennupati's talk](https://www.conf42.com/Platform_Engineering_2025_Srinivas_Chennupati_knowledge_rag_strategies)

[Watch the talk on YouTube](https://youtu.be/ASBY-UrPFv8).

## Watch the talk

[Building Production-Ready RAG Systems: Platform Engineering Strategies for Enterprise Knowledge Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Srinivas_Chennupati_knowledge_rag_strategies) at Conf42 Platform Engineering 2025.
