# Enterprise RAG needs authorization inside retrieval, not at the UI

Conf42 Blog, 2026-09-08, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/enterprise-rag-authorization-inside-retrieval

In short: Ananda Kumar Dey of Quadrant Technologies at Conf42 DevSecOps 2026 treats enterprise RAG as a knowledge security problem, with access filters before ranking.

When production goes down, the answer is usually spread across Jira, ServiceNow, GitHub, Confluence and a security platform, plus whatever lives in one senior engineer's head. At Conf42 DevSecOps 2026, Ananda Kumar Dey, who leads AI strategy and solution architecture at Quadrant Technologies, argued that pointing an LLM at all of that is a knowledge security and trust problem first, and that the single most important control is filtering what a user may see before retrieval ranks anything.

It's an architecture overview of a production RAG system, aimed at teams moving past the demo, and it's refreshingly firm about measuring before tuning.

## The LLM is the small box

Ananda's diagram is familiar: query processing, retrieval, prompt augmentation, generation. His point is where the effort goes. The model is one component; ingestion, retrieval, access control, observability and grounding are the enterprise work. A wrong, stale or unauthorized retrieval produces an answer that is convincing and still wrong.

Governance starts at ingestion, well before anyone types a question. Pull from GitHub, Jira, Confluence and ServiceNow through governed pipelines, attach metadata on owner, sensitivity and source while chunking, and detect PII and secrets before creating embeddings. Bad data in the knowledge layer doesn't stay put; retrieval amplifies it.

## Index hygiene and hybrid search

Retrieval quality comes down to three choices: the embedding model, a vector store that supports filtering and enterprise controls, and index hygiene. Documents change, permissions change, content goes stale, so you need versioning, deletion propagation and lifecycle management, the same discipline as any other data platform.

On the vector database question (Pinecone, pgvector, Weaviate, Azure AI Search and friends) he refuses to pick a benchmark winner. Choose on hybrid search, metadata filtering, security integration and what you already operate. It's an architectural decision, not a speed contest.

The technical-content point every DevSecOps team will recognise: semantic search is good at concepts and paraphrase, and weak on exact identifiers like a CVE number, incident ID or config key. Combine dense retrieval with sparse BM25 and merge the rankings. Then re-rank: retrieve broadly (say the top fifty), score with a cross-encoder, and send only the best few chunks to the model. Retrieve broadly, re-rank intelligently, generate narrowly.

## Don't retrieve it and then hide it

The core security principle is that authorization can't live in the UI. The user's identity and policies have to shape retrieval itself: a policy engine evaluates the request and chunk metadata, and filters drop unauthorized chunks before they enter ranking. The system never fetches sensitive content and then tries to hide it afterwards.

Around that sit corpus protection (encryption, secret scanning, classification, retention and deletion) and an audit trail of who asked what, what was retrieved, what was generated and which sources backed it. Trust needs evidence that the controls ran, not just the controls.

## Measure retrieval separately from generation

On hallucinations, Ananda reframes the goal: rather than eliminating them, design controls that make unsupported answers hard to produce and easy to detect. That means authoritative sources, answers tied to retrieved evidence, and human review when confidence is low or the stakes are high.

Then evaluate in two layers. First ask whether retrieval found the right evidence (precision, recall, MRR), then whether generation used it well (RAGAS faithfulness and answer relevance), against a baseline of representative questions. His line: don't tune RAG by intuition, measure it.

## Graphs and agents come later

Some questions aren't answered by the three most similar paragraphs: which apps depend on this service, who owns it, are there related incidents or vulnerabilities. That's where graph retrieval, agentic RAG that splits a question into retrieval steps, and tool-augmented RAG pulling live API data come in. His production lessons put them in order: fix the data before tuning the model, enforce authorization inside retrieval, measure before changing models, chunking or prompts, and operate RAG as versioned, monitored, tested software. Twice, for emphasis: "RAG is not a prompt engineering project, it's a production system."

## Who should watch

Architects and platform teams building an internal knowledge assistant for engineering or security, especially where documents carry different access levels. If you've already shipped hybrid search with permission-aware filtering and a golden dataset, this will confirm your choices rather than surprise you.

## Related Conf42 talks

- [Beyond Basic RAG: Better Context for More Reliable Enterprise AI](https://www.conf42.com/Prompt_Engineering_2026_Ravi_Ray_rag_context_enterprise) by Ravi Ray at Conf42 Prompt Engineering 2026.
- [RAG for Data Engineers: What It Is, Where It Fits, and Why Your Metadata Is the Missing Piece](https://www.conf42.com/Large_Language_Models_LLMs_2026_Varun_Joshi_rag_metadata) by Varun Joshi of AWS at Conf42 Large Language Models 2026.
- [Vector Embeddings and RAG Demystified](https://www.conf42.com/Machine_Learning_2025_Veliswa_Boya_rag_embeddings_vector) by Veliswa Boya of AWS at Conf42 Machine Learning 2025.

[Watch Ananda Kumar Dey's talk](https://www.conf42.com/DevSecOps_2026_Ananda_Kumar_Dey_rag_vectors_trust) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/WFpTX__ugsM).

## Watch the talk

[Secure Enterprise RAG: Building Trusted Vectorized Knowledge Systems for DevSecOps](https://www.conf42.com/DevSecOps_2026_Ananda_Kumar_Dey_rag_vectors_trust) at Conf42 DevSecOps 2026.
