# RAG support bots should know when they do not know

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/rag-customer-support-beyond-chatbots

In short: Vaibhav Fanindra Mahajan at Conf42 Observability 2025 on RAG for customer support, with confidence thresholds, fresh indexes and clean human handoffs.

A support bot that guesses is worse than no bot at all. At Conf42 Observability 2025, Vaibhav Fanindra Mahajan walked through how retrieval-augmented generation (RAG) improves on classic support chatbots, and the feature that matters most for trust: a RAG system can score its own confidence from retrieval results and escalate or ask a clarifying question instead of making something up.

## Why the old bots break

Vaibhav starts with the problems of traditional chatbots, including the ones with intent classification and basic NLP. They rely on rule-based flows that break on edge cases, they are trained on a snapshot of data that goes stale quickly, and their session state is brittle, so multi-turn context is weak. Every policy change means a manual knowledge update, unusual questions fall through the dialogue tree, and when the model does not know, it tends to guess.

## Retrieval first, generation second

RAG puts retrieval before the answer. The query is embedded with BERT or sentence transformers, matched against a vector store such as FAISS, Pinecone or Weaviate to fetch the top-k passages, and those passages go into the prompt, so the output is grounded in current enterprise knowledge instead of the model's memory.

For multi-part questions, which linear dialogue flows handle badly, the input is split into smaller sub-questions, each is retrieved separately, possibly from different knowledge clusters, and the snippets are fused through concatenation or a fusion-in-decoder layer before one combined answer is generated.

## Confidence is the observable part

The section that fits the conference theme is about knowing when to stop. RAG systems can estimate confidence from retrieval scores and response entropy. Set a threshold, and below it the bot asks a clarifying question or escalates. If no relevant documents come back for, say, an outage question, it returns a fallback or an explicit uncertainty signal rather than a confident invention. Those scores are also exactly what you want on a dashboard.

Session-level memory, using embeddings or key-value stores, tracks intent and previous turns. When a human does take over, the bot hands over a package: conversation history, retrieved documents and generated responses, with the intent chain. The agent does not have to ask the customer to repeat everything, which Vaibhav ties to lower handling time and better first-contact resolution.

## Keep the index fresh, and clean

A RAG bot is only as current as its index, so he describes a continuous update pipeline. When a policy document or support article changes in Confluence or a CMS, it is queued, re-embedded by a background job with a model such as BGE or MiniLM, and the vector index is updated. The next query sees the new content the same day, with no fine-tuning.

He is blunt that this is garbage in, garbage out. Remove duplicates and near-duplicates, reconcile conflicting entries that confuse retrieval, organise the knowledge base with a clear taxonomy and tag everything with metadata for filtering. And keep an access-control and query-filtering layer after retrieval so unauthorised data never reaches a customer.

## Where it goes next

The future section includes per-customer index segments for personalised support, multilingual answers drawn from the same knowledge base, and multimodal RAG with vision encoders such as CLIP and BLIP-2, so a photo of a damaged product or an error screenshot can be matched against visual knowledge. His team is also working on feeding usage logs to the bot to spot anomalies and surface help before an outage hits. He closes with a comparison of first-contact resolution, around 75 to 85% with RAG against 45 to 55% for traditional bots.

## Who should watch

Teams building or buying an AI support assistant who want a clear architecture walkthrough. The observability angle is lighter than the title suggests, centred on confidence scores and knowledge freshness rather than tracing, and the talk is conceptual rather than a demo.

## Related Conf42 talks

- [Ofer Mendelevitch on measuring hallucinations in RAG](https://www.conf42.com/Large_Language_Models_LLMs_2024_Ofer_Mendelevitch_rag_measuring_hallucinations) at Conf42 LLMs 2024.
- [Dmitry Kindrya on whether LLMs will save customer support or kill it](https://www.conf42.com/Large_Language_Models_LLMs_2024_Dmitry_Kindrya_customer_support_revolutionizing) at Conf42 LLMs 2024.
- [Veliswa Boya demystifying vector embeddings and RAG](https://www.conf42.com/Machine_Learning_2025_Veliswa_Boya_rag_embeddings_vector) at Conf42 Machine Learning 2025.

[Watch Vaibhav Fanindra Mahajan's talk](https://www.conf42.com/Observability_2025_Vaibhav_Fanindra_Mahajan_rag_chatbots)

[Watch the talk on YouTube](https://youtu.be/FgzLD1b_n74).

## Watch the talk

[RAG Beyond Chatbots: Transforming Customer Support with Observable Intelligence](https://www.conf42.com/Observability_2025_Vaibhav_Fanindra_Mahajan_rag_chatbots) at Conf42 Observability 2025.
