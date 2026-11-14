# Vector RAG can't count, so let the graph database do it

Conf42 Blog, 2026-03-27. https://www.conf42.com/blog/cloud2026/graph-rag-stops-agents-fabricating-counts

In short: Elizabeth Fuentes Leone of AWS at Conf42 Cloud Native 2026 shows graph RAG with Neo4j and Strands Agents answering counts that vector RAG makes up.

Ask a vector-RAG agent how many hotels have swimming pools and it will read three chunks, count what it sees and tell you "approximately four or five" with a straight face. At Conf42 Cloud Native 2026, Elizabeth Fuentes Leone, Developer Advocate at AWS, shows why that happens and how graph RAG fixes it: turn the documents into a knowledge graph, have the model write a Cypher query, and let the database do the counting.

The session is listed under the title "Reduce AI Agents Costs and Mistakes with Semantic tool Selection". The session as recorded is about graph RAG: she introduces a five-part series on stopping agent failures, mentions semantic tool selection as the second technique, and spends the talk on the first one.

## Similarity search answers from a sample

Her framing is blunt. Vector search returns the most similar documents, not all of them, so on an aggregate question "your agent answered from 1% of the data". The real answer to the pool question on her slide is 133. The model never had the data to get there, so it estimated, and an estimate delivered with full confidence is a fabricated number.

She groups the failure modes into three: fabricated statistics, incomplete retrieval, and out-of-domain fabrication, where the agent cheerfully answers about things the knowledge base has never heard of.

## Build the graph, then let the LLM write queries

The demo uses a hotel dataset of 300 documents (with a lighter 10% version she recommends for trying it yourself). Neo4j's knowledge-graph pipeline has an LLM read each document and discover the entity types on its own (hotels, rooms, amenities, policies, services) along with the relationships between them, so there is no hand-written schema. Entity resolution then merges near-duplicates such as outdoor pools and swimming pools into one node, which is exactly what makes a count query come out right.

At question time the agent doesn't search by similarity. The tool's docstring carries the graph schema, the model reads it and generates a Cypher query, and the database executes it across every node. The model only writes the query and phrases the result. A useful side effect: instead of paying tokens for a pile of retrieved chunks the model has to aggregate in its head, it receives just the rows it asked for. And, in her words, "when the data does not exist, graph RAG returns empty".

## Four questions, two agents

The agents are built with Strands Agents, the open-source SDK that AWS maintains, here running on OpenAI as the model provider to show the provider is swappable. The baseline agent gets a FAISS vector store with an open-source sentence-transformers embedding model; the second gets the Cypher tool. Same prompt, four tests:

- **Aggregation:** the average guest rating across hotels in Paris. Vector RAG found two hotels and did the arithmetic itself.
- **Counting:** hotels with swimming pools in Paris. One short, grounded answer from the graph.
- **Multi-hop:** room types and prices of the highest-rated hotel. The dataset has no prices; the graph agent traverses to room data and says price is not available.
- **Out of domain:** hotels in Antarctica. Vector RAG offers a general overview it invented; the graph agent says there are none in the database.

She is fair to plain RAG at the end. Keep it for semantic search over unstructured text and fuzzy matching; reach for graph RAG for counts, aggregations and multi-hop reasoning; in production you probably want both.

## Who should watch

Anyone whose RAG agent gets asked "how many" or "which is the highest" questions by real users. It's a short, demo-led session with a notebook rather than a production case study, and the repository she shares covers the rest of the series, including deployment to production on AgentCore. If you wanted the semantic tool selection material, it gets a brief mention here and its own session elsewhere.

## Related Conf42 talks

- [Stop AI Agents from Making Up Facts: Graph-RAG for Reliable Data Retrieval](https://www.conf42.com/MLOps_2026_Elizabeth_Fuentes_Leone_graph_rag_retrieval) by Elizabeth Fuentes Leone at Conf42 MLOps 2026.
- [Reduce AI Agents Costs and Mistakes with Semantic tool Selection](https://www.conf42.com/AI_Agents_2026_Elizabeth_Fuentes_Leone_tools_semantic_cost) by Elizabeth Fuentes Leone at Conf42 AI Agents 2026.
- [Hallucination by Design: How Embedding Models Misunderstand Language](https://www.conf42.com/Machine_Learning_2025_Ritesh_Modi_embedding_models_language) by Ritesh Modi at Conf42 Machine Learning 2025.

[Watch Elizabeth Fuentes Leone's talk](https://www.conf42.com/Cloud_Native_2026_Elizabeth_Fuentes_Leone_ai_llm_applications) from [Conf42 Cloud Native 2026](https://www.conf42.com/cloud2026).

[Watch the talk on YouTube](https://youtu.be/PvWSg2Rz-gE).

## Watch the talk

[Reduce AI Agents Costs and Mistakes with Semantic tool Selection](https://www.conf42.com/Cloud_Native_2026_Elizabeth_Fuentes_Leone_ai_llm_applications) at Conf42 Cloud Native 2026.
