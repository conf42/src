# Rerank documents by asking an LLM which of two is better

Conf42 Blog, 2025-11-03, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/pairwise-llm-reranking-beats-retrievers

In short: Maximilian Schattauer of Perelyn at Conf42 Prompt Engineering 2025 on pairwise LLM document ranking for specialised corpora where embeddings fall short.

When every document in your corpus looks alike to an embedding model, cosine similarity stops being an answer. At Conf42 Prompt Engineering 2025, Maximilian Schattauer, Technical Consultant for Data and AI at Perelyn in Munich, showed how his team improved retrieval for a client by using an LLM as a pairwise judge: show it two documents and a query, ask which answers better, and build the ranking from the votes.

It is a short, focused talk based on one client project, and Maximilian is upfront that the evidence is anecdotal. The method is simple enough to try on your own data.

## Where conventional retrievers break

A classic retriever takes a query and returns documents ranked by semantic relatedness (embeddings) or keyword overlap (BM25). The results might feed an LLM, but Maximilian's case is the one where they do not: they go straight to a user or a downstream data application, so ranking quality is the product.

His list of limits: the retriever always considers the whole query, so you cannot tell it to focus on one aspect; it is a black box you cannot steer; and there is no reasoning in the ordering. In specialised domains where documents are too similar for embeddings or keywords to tell apart, you need something that can reason about small differences. The client project hit exactly that, and the retrieval metrics showed it.

## Retrieve first, then let the LLM reorder

The pipeline keeps a classic retriever for a preliminary candidate set, then uses an LLM to refine the set and its order. The second stage adds a text input you can control: focus on certain aspects of the query, inject metadata, or add rules that a non-LLM retriever cannot capture. You can use a regular model or a reasoning model at this step.

## The LLM as a binary operator

The core idea is how the LLM is used. Rather than pasting all candidates into one prompt and asking for a ranking, Maximilian's team put two documents and the query into each prompt, described the domain, and asked for a single verdict: A or B. Running that over every pair yields a comparison matrix, and counting wins gives an order.

Two refinements matter. Running each comparison several times at non-zero temperature gives statistics to ground the ordering instead of a single coin flip. And pairwise comparison avoids the needle-in-a-haystack problem of one big prompt, where documents get lost when the candidate list is long. In their project, the pairwise setup was quantitatively better than one-shot LLM ranking, and the abstract reports gains in recall@k over traditional retrievers in these specialised scenarios.

## The bill

He does not hide the cost. The number of LLM calls grows with the square of the number of candidates, so this is far slower and more expensive than an embedding lookup, a keyword search or even a single LLM reranking call. Keep the preliminary set small, and save the method for domains where ranking errors are costly. Quadratic is fine for twenty documents and a budget meeting for two thousand.

## Who should watch

Engineers building search or RAG over narrow, look-alike corpora (legal, technical standards, internal policy) who have hit the ceiling of embedding similarity. If your retriever already does well on general web-like text, a cross-encoder reranker is probably the cheaper next step; this talk is for when that is not enough.

## Related Conf42 talks

- [Zain Hasan on chatbots with advanced retrieval-augmented generation techniques](https://www.conf42.com/Large_Language_Models_LLMs_2024_Zain_Hasan_chatbots_retrievalaugmented_building) at Conf42 LLMs 2024.
- [Veliswa Boya's Vector Embeddings and RAG Demystified](https://www.conf42.com/Machine_Learning_2025_Veliswa_Boya_rag_embeddings_vector), the first-stage retrieval this talk builds on.
- [Elizabeth Fuentes Leone on Graph-RAG for reliable retrieval](https://www.conf42.com/MLOps_2026_Elizabeth_Fuentes_Leone_graph_rag_retrieval), another way past plain vector search.

[Watch Maximilian Schattauer's talk](https://www.conf42.com/Prompt_Engineering_2025_Maximilian_Schattauer_retrievers_documents_ranking), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/KqEQGHFoxXI).

## Watch the talk

[Beyond semantic retrievers: leveraging LLMs for question-based document ranking](https://www.conf42.com/Prompt_Engineering_2025_Maximilian_Schattauer_retrievers_documents_ranking) at Conf42 Prompt Engineering 2025.
