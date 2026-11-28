# From coffee and tea vectors to RAG on Amazon Bedrock

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/vector-embeddings-rag-from-coffee-to-bedrock

In short: Veliswa Boya of AWS gave a beginner-friendly tour of vector embeddings and RAG at Conf42 Machine Learning 2025, ending in Bedrock Knowledge Bases.

Models only understand numbers, so before an LLM can finish *the capital of France is*, your text has to become vectors. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Veliswa Boya, Senior Developer Advocate at AWS, used under 30 minutes to explain vector embeddings, retrieval augmented generation, and how the two fit together, with a short Boto3 demo on Amazon Bedrock.

She says up front it's a high-level introduction, and that's exactly what it is: a clean first talk on the topic, not a tuning session.

## Coffee sits near tea, cappuccino sits nearer coffee

The embedding explanation is built from a café menu. Put *coffee* and *tea* into a toy vector space and they land close together because both are hot drinks. Add *cappuccino* and it lands closer to coffee, since there's coffee in it. Where words end up comes from training and from how the words are used in the training text.

Boya then shrinks the idea to a sheet of paper: words as arrows from one corner, their direction carrying meaning, their coordinates turning words into numbers. Two dimensions are nowhere near enough for a real vocabulary, so real embeddings use hundreds or thousands of them. It's the clearest mental model you'll find for why *similar* becomes *close* in a vector database, and why music and shopping apps can recommend things that match your taste.

## RAG answers the questions your model was never trained on

Her RAG example is a PDF of internal staff training courses. A foundation model knows nothing about it, so it can't tell you which course is most popular or how long people take to finish one. RAG fixes that by pulling from an authoritative knowledge base outside the training data before generating the answer, and it does so without retraining the model. She frames it as a cost-effective way to keep output relevant and accurate for a specific organisation.

She's also honest about the plumbing that makes people hesitate: multiple data sources, embedding large volumes of data, incremental updates to the vector store, scaling retrieval, and orchestrating it all.

## The AWS part, clearly labelled

This is an AWS talk and it says so. The demo initialises a Boto3 session, creates a Bedrock Runtime client and defines a `get_embedding` function that calls the Amazon Titan Embeddings model and returns the vector. The managed answer to the plumbing problem is Amazon Bedrock Knowledge Bases, which connects foundation models and agents to private data sources, augments prompts via the Retrieve API, and offers RetrieveAndGenerate for the full loop with source attribution.

## Who should watch

Watch it if RAG is on your roadmap and you want the concepts straight before you pick a vector store, or if you need a short explainer to share with a team that's new to it. If you already run hybrid search with rerankers in production, this one will feel like a refresher; skip to the related talks.

## Related Conf42 talks

- [Vector Ops: How to run vector embedding-powered apps in production](https://www.conf42.com/Machine_Learning_2023_Daniel_Svonava_vector_ops_embeddingpowered_apps) by Daniel Svonava picks up where this intro stops.
- [Measuring hallucinations in RAG](https://www.conf42.com/Large_Language_Models_LLMs_2024_Ofer_Mendelevitch_rag_measuring_hallucinations) by Ofer Mendelevitch asks whether retrieval actually kept the model honest.
- [Building Production-Ready RAG Systems](https://www.conf42.com/Platform_Engineering_2025_Srinivas_Chennupati_knowledge_rag_strategies) by Srinivas Chennupati looks at RAG as platform infrastructure.

[Watch Veliswa Boya's talk](https://www.conf42.com/Machine_Learning_2025_Veliswa_Boya_rag_embeddings_vector)

[Watch the talk on YouTube](https://youtu.be/QxwQTa6vWGE).

## Watch the talk

[Vector Embeddings and RAG Demystified](https://www.conf42.com/Machine_Learning_2025_Veliswa_Boya_rag_embeddings_vector) at Conf42 Machine Learning 2025.
