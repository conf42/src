# RAG is easy until the second PDF arrives

Conf42 Blog, 2026-05-05, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/rag-in-production-modular-pipeline-mariadb

In short: Alejandro Duarte of MariaDB at Conf42 Database DevOps 2026 on what breaks when RAG leaves the demo, and a modular pipeline that handles it.

A retrieval-augmented generation demo fits on one slide; a RAG system that survives real documents needs about five modules. At Conf42 Database DevOps 2026, Alejandro Duarte, Developer Relations Engineer at MariaDB plc, walked every stage of the RAG pipeline, named what goes wrong at each one, and then showed MariaDB AI RAG, the company's own packaged answer to the problem.

So, honest scope: the first two thirds are a vendor-neutral tour of RAG engineering, and the last third is a product demo. Both halves are useful, and Alejandro is clear about which one you are in.

## Context is all you need

The talk opens with the familiar exhibits: an AI model recommending non-toxic glue on pizza, and another suggesting one small rock a day for your digestion. RAG is the standard defence. Alejandro frames it as building context specific to each query, which at its core is prompt stuffing, with his own warning that this is an oversimplification.

The Hello World version is a product recommendation chatbot (the Java code is on GitHub, deliberately framework-free). Concatenate each product's title, description and price, send it to an embedder, store the vector in a new column of the same MariaDB table. At query time, embed "I want running shoes", order the table by vector distance, take the top three, and hand them to the LLM. To track how hard each step is, Alejandro brings in the Doom Guy face from the old game HUD. At this point Doom Guy is laughing.

## Every stage of phase one costs you a hit

Then real data shows up: PDFs, DOCX, XML, JSON. You cannot embed a 300-page PDF as one vector, so you chunk it, and naive chunking bites. His example is a document that opens "I left my wife a note", split right after "wife". Overlap fixes some of that. Recursive chunking cuts by page, then paragraph, then sentence until the size fits. Semantic chunking lets an LLM pick the cut points: precise, but an extra call per chunk.

Ingestion has its own list. Sources can be SQL, the file system, HTTP or S3; multiple users may need their own directories; messy multi-column PDFs need layout-aware extraction or the text comes out in the wrong order, just like copy-pasting from a PDF reader. Calls to the embedder need retries and error handling you do not want to reimplement in every microservice, and documents and chunks need CRUD and versioning. Doom Guy is bleeding by now.

## The second database is the biggest hit

Phase two, retrieval and generation, starts with one question: does your database store vectors natively, or are you adding a vector database or extension? Adding one means a new system to license, operate, connect to and keep compatible. Alejandro's sharpest aside is about risk: he points out that pgvector, the Postgres vector extension, is maintained by one person, so its bus factor is one. He is careful to say that does not mean the project is in danger; it is one metric to weigh. MariaDB ships vector types and a vector index in the server, which is his pitch for skipping that hit.

Retrieval itself is a design choice. Vector search handles meaning; keyword search over a full-text index is better for identifiers that carry no semantics, like product codes. Hybrid search runs both and merges them with reciprocal rank fusion. A cross-encoder re-ranking step (FlashRank locally, or Cohere as a service) reorders the chunks so you send the LLM less, which is cheaper and gives it fewer chances to hallucinate.

## A modular RAG architecture you can copy

The useful takeaway, product or not, is the architecture: separate modules for ingestion (with Docling or LlamaParse for extraction), chunking with configurable strategies, retrieval with hybrid search and re-ranking, generation with swappable LLM providers (or Ollama for data that must stay in-house), citations and streaming, plus an orchestration layer for async processing, retries, health checks, auth and multiple users. Package it as one horizontally scalable service behind a REST API.

That is what MariaDB AI RAG is, with an MCP server added for agents. The demo runs it from Swagger UI against MariaDB Enterprise Server: ingest his own book, Practical Vaadin, as a PDF, chunk it recursively into roughly four hundred chunks, and ask which dog breed appears in an example. ChatGPT and Gemini both missed earlier in the talk; with hybrid retrieval, Gemini answers correctly: an English bulldog named Draco. The product was in beta at recording time.

## Who should watch

Engineers moving a RAG prototype towards production, especially those deciding whether vectors belong in their existing database. The checklist of failure points is worth it even if you never touch MariaDB. If you already run a mature retrieval stack with re-ranking and versioned chunks, the first half will be review.

## Related Conf42 talks

- [Ofer Mendelevitch on measuring hallucinations in RAG](https://www.conf42.com/Large_Language_Models_LLMs_2024_Ofer_Mendelevitch_rag_measuring_hallucinations) at Conf42 Large Language Models 2024.
- [Stephen Batifol on how vector databases work](https://www.conf42.com/Machine_Learning_2024_Stephen_Batifol_vector_databases_work) at Conf42 Machine Learning 2024.
- [Lei Xu on LanceDB, an open-source serverless vector database](https://www.conf42.com/Rustlang_2023_Lei_Xu_lancedb_oss_serverless_vector_db) at Conf42 Rustlang 2023.

[Watch Alejandro Duarte's talk](https://www.conf42.com/Database_DevOps_2026_Alejandro_Duarte_llm_vectors_semantic)

[Watch the talk on YouTube](https://youtu.be/CBn_Cqno8BA).

## Watch the talk

[RAG in production: challenges, techniques and solutions](https://www.conf42.com/Database_DevOps_2026_Alejandro_Duarte_llm_vectors_semantic) at Conf42 Database DevOps 2026.
