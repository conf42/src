# Running AI literature agents over 30 million biomedical citations

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/ai-literature-agents-for-biomedical-research

In short: Nishanth Joseph Paulraj (Thermo Fisher Scientific) at Conf42 MLOps 2025 on the MLOps behind RAG literature agents for biomedical researchers.

Biomedical research publishes more than a million papers a year, and every new project still starts with a literature review. At Conf42 MLOps 2025, Nishanth Joseph Paulraj, a senior data engineer at Thermo Fisher Scientific, shows the MLOps architecture behind AI literature agents that search a corpus of more than 30 million citations, and argues that domain experts have to be part of the pipeline, not just its customers.

The talk is a tour of the full stack, from microservices and model registry to vector database scaling and A/B testing.

## The problem is a tsunami of citations

Nishanth frames it from the researcher's chair. Relevant work can be hidden from search, reading everything is impossible, and by his account researchers spend a large share of their time on the review alone. His solution combines four parts: domain-adapted LLMs, an advanced retrieval-augmented generation system, a precision named entity recognition system for genes, proteins and drug interactions, and robust MLOps to keep it all running.

## General NLP breaks on biomedical language

The domain adaptation section explains why off-the-shelf pipelines struggle. Biomedical text has highly specialised vocabulary that differs across sub-disciplines, entity relationships like gene-protein interactions that need expert understanding, meanings that shift between research areas, and a constant stream of new discoveries. Evaluation therefore needs biomedical accuracy metrics plus domain expert review, not only standard test sets.

## The architecture separates embedding from retrieval

His blueprint for an effective setup is concrete: containerised microservices for modular scaling and versioning, a model registry because the models keep changing, asynchronous processing pipelines for batch citation updates (citation counts change daily), a clean separation of embedding generation from retrieval services, a real-time inference API layer built for sub-second responses, and a dedicated evaluation environment for scientific validation.

Scaling the vector database is its own chapter. The challenges are generating embeddings efficiently for a huge corpus, balancing recall against compute cost, and updating indexes without downtime. His answers are asynchronous batch embedding pipelines, hierarchical indexing, read replicas with staged updates, and query caching. On the RAG side he lists domain-specific embedding models, multi-stage retrieval, citation network enrichment and context window optimisation.

## Speed alone is not a success metric

The KPIs he reports are sub-second query latency, 90% accuracy in entity recognition and citation relevance scores above 85%, with an A/B testing framework reporting an 80% reduction in literature search time. The point he keeps returning to is that faster search is not proof the system is better. Scientific validation pipelines must measure the research outcome too.

Monitoring covers model drift, citation accuracy, system health, query patterns and resource use, on dashboards built for both ML engineers and scientists. Infrastructure has a baseline sized to average load with redundancy, autoscaling inference endpoints, scheduled scaling for predictable peaks like the academic calendar, and dedicated GPU allocation for embedding and inference.

## Who should watch

Engineers building RAG over specialised corpora (legal, patents, clinical, biomedical) where generic embeddings miss the point, and data teams scaling a vector store from a demo to tens of millions of documents. His closing lessons apply well outside biology: bring in domain experts, validate scientifically, keep the corpus updating, and prioritise explainability, because researchers will not trust a citation they cannot trace.

## Related Conf42 talks

- [Nishanth Joseph Paulraj on architecture patterns for AI literature processing platforms](https://www.conf42.com/Platform_Engineering_2025_Nishanth_Joseph_Paulraj_literature_large_rag) at Conf42 Platform Engineering 2025, the platform view of the same system.
- [Ofer Mendelevitch on measuring hallucinations in RAG](https://www.conf42.com/Large_Language_Models_LLMs_2024_Ofer_Mendelevitch_rag_measuring_hallucinations) at Conf42 LLMs 2024.
- [Zain Hasan (Weaviate) with a gentle introduction to vector databases](https://www.conf42.com/Machine_Learning_2023_Zain_Hasan_vector_databases) at Conf42 Machine Learning 2023.

[Watch Nishanth Joseph Paulraj's talk](https://www.conf42.com/MLOps_2025_Nishanth_Joseph_Paulraj_deploying_ai_literature) for the full architecture and scaling patterns.

[Watch the talk on YouTube](https://youtu.be/E86390EpwQ0).

## Watch the talk

[Deploying AI Literature Agents at Scale: MLOps Strategies for Biomedical Research Platforms](https://www.conf42.com/MLOps_2025_Nishanth_Joseph_Paulraj_deploying_ai_literature) at Conf42 MLOps 2025.
