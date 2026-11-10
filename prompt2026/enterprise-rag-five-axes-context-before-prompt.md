# Better enterprise AI answers start before the prompt reaches the model

Conf42 Blog, 2026-10-27, updated 2026-11-09. https://www.conf42.com/prompt2026/enterprise-rag-five-axes-context-before-prompt

In short: Ravi Ray at Conf42 Prompt Engineering 2026 on a vendor-neutral five-axis framework for enterprise RAG, from ingestion to governance.

Two assistants with the same model and nearly the same prompt answer a question about travel policy. One retrieves last year's policy, the other the current approved version. At Conf42 Prompt Engineering 2026, Ravi Ray, a software engineering PMTS, used that example to argue that in enterprise AI the retrieved context often matters more than the prompt wording, and laid out a vendor-neutral five-axis framework for designing the retrieval layer.

The framework comes from a comparative look at roughly 25 implementations across academic research, open source frameworks and enterprise platforms. The aim wasn't to rank vendors but to find what changes when RAG leaves the prototype.

## RAG is infrastructure now

A prototype is a few PDFs, some embeddings and useful answers, and Ravi calls that a good way to start. Production brings changing content, multiple repositories, permissions and users who expect the same answer every day. So treat RAG like databases, APIs and identity: reliable ingestion, predictable performance, clear ownership, monitoring. The question shifts from "can the model retrieve something relevant?" to whether the whole system retrieves the right evidence consistently, securely and at scale.

## Five axes that affect each other

The axes are ingestion (parsing, normalising, chunking), indexing (dense, sparse or hybrid), retrieval composition (query rewriting, merging, re-ranking), grounding (tying answers to evidence) and governance (permissions, provenance, auditability). They aren't separate boxes: a great re-ranker can't restore a table the parser dropped, and accurate search is still unsafe if access controls are ignored.

## Inspect what the parser actually produced

Ingestion is where many retrieval problems begin. A technical PDF loses a column heading during parsing, and later a search returns text that looks relevant but no longer means what the author wrote. No prompt tweak or vector database setting fixes that. His advice: look at the extracted content, chunk boundaries and metadata (author, last update, access, origin) before tuning retrieval, or you're optimising against damaged evidence.

On indexing, dense retrieval handles paraphrase, sparse retrieval like BM25 handles exact identifiers and product codes, which is why hybrid search plus a re-ranker is common in the systems he studied. Every extra stage costs latency and operational complexity, so measure end to end on real questions. The best pipeline is the simplest one that reliably meets the requirements.

## Grounding and governance are architecture

Grounding means attribution to the specific chunk, faithfulness to that evidence, and visible confidence: if the policy documents don't describe an exception, the assistant says it couldn't verify one. A link to a hundred-page PDF is a decorative citation; a pointer to the right section is a useful one.

Governance is where research demos turn into hard enterprise projects. Enforce access control when candidates are selected, not just when results are displayed. Keep provenance from answer to chunk to source document and version. And evaluate with time in mind: an answer can be semantically correct and based on a pricing policy revised last month, which can do more harm than an obvious failure. Retrofitting any of these later is much harder.

## Seven open problems

He lists the challenges still unsolved: grounding claims across long documents, ranking tables, diagrams, code and prose coherently, freshness through change data capture including deletions, evaluation that doesn't export confidential documents, multi-agent retrieval without duplicated or conflicting evidence, the latency and cost of extra passes, and evaluating under real enterprise conditions that public benchmarks don't capture. The gap between prototype and production, in his reading, is mostly operational, organisational and sometimes regulatory, not algorithmic.

His bigger shift is to design RAG as a knowledge system: source content as governed data with schemas, versions, permissions and change events, and the index as a derived representation, never the source of truth.

## Four things to do on Monday

Audit ingestion by reading the extracted text behind real answers. Enforce access control at retrieval time and test with users who hold different permissions. Instrument provenance back to source and version. Build an evaluation set from real questions that includes outdated documents, exact identifiers, missing evidence and restricted content.

## Who should watch

Architects and platform teams moving a RAG assistant from pilot to production, and prompt engineers who suspect their prompt isn't the problem. It's a framework talk without a demo or benchmark numbers, but the checklist is concrete enough to run against your own system.

## Related Conf42 talks

- [Secure Enterprise RAG: Building Trusted Vectorized Knowledge Systems for DevSecOps](https://www.conf42.com/DevSecOps_2026_Ananda_Kumar_Dey_rag_vectors_trust) by Ananda Kumar Dey (Quadrant Technologies) at Conf42 DevSecOps 2026.
- [RAG in production: challenges, techniques and solutions](https://www.conf42.com/Database_DevOps_2026_Alejandro_Duarte_llm_vectors_semantic) by Alejandro Duarte (MariaDB plc) at Conf42 Database DevOps 2026.
- [Beyond semantic retrievers: leveraging LLMs for question-based document ranking](https://www.conf42.com/Prompt_Engineering_2025_Maximilian_Schattauer_retrievers_documents_ranking) by Maximilian Schattauer (Perelyn) at Conf42 Prompt Engineering 2025.

[Watch Ravi Ray's talk](https://www.conf42.com/Prompt_Engineering_2026_Ravi_Ray_rag_context_enterprise) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/RMJcX3EOFFU).

## Watch the talk

[Beyond Basic RAG: Better Context for More Reliable Enterprise AI](https://www.conf42.com/Prompt_Engineering_2026_Ravi_Ray_rag_context_enterprise) at Conf42 Prompt Engineering 2026.
