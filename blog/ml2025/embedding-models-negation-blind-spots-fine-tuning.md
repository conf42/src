# Your embedding model thinks "effective" and "ineffective" match

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/embedding-models-negation-blind-spots-fine-tuning

In short: Ritesh Modi (Microsoft) at Conf42 Machine Learning 2025 on the 38 ways off-the-shelf embedding models misread language, and how fine-tuning fixes most of them.

"The treatment was completely ineffective" and "the treatment was absolutely effective" scored 96% cosine similarity with an off-the-shelf embedding model. At Conf42 Machine Learning 2025, Ritesh Modi, Principal AI Engineer at Microsoft, used that result to open a systematic look at how embedding models misunderstand language, tested across 38 failure scenarios, and showed how domain models, preprocessing and fine-tuning with Sentence Transformers bring the scores back in line with meaning.

If your RAG system retrieves by embeddings, and most do, this is the talk that will make you go and test yours.

## A quick, practical primer

Ritesh starts with the basics, done well. Embeddings turn text into vectors that carry meaning, so dog sits near puppy. He covers dimensionality (from 32 to 4,096; more captures nuance, fewer is faster and cheaper to store), max sequence length (tokens past the limit are silently dropped, so know your model's), vocabulary size (out-of-vocabulary words have no meaning to preserve), and the comparison metrics, with cosine similarity as the default. A live demo with an MPNet model scores "What's the weather like in New York today?" against "Can you tell me the current weather in New York?" at 88%: different words, same intent, which is the whole point of embeddings.

## The quiz that breaks your trust

Then the quiz. Effective versus ineffective treatment: 96% similar. Hypertension versus hypotension, two opposite conditions, are next to each other too. His wider test set covers 38 scenarios, including capitalisation, whitespace, negation, word order, temporal order (finishing a degree before starting a job, or the other way round), hypotheticals versus facts, units (a procedure taking five minutes versus five hours), numeric ranges, and dates written 10/12 versus 12/10, which came out 99% similar despite two months between them. The lowest similarity across the whole set was around 80%, for spelling and typos. Every pair should have scored much lower.

He explains the causes plainly. Models weight words they consider important, reward word overlap regardless of order, and lean on sentiment words, so a sentence saying something was not enjoyed still looks like one saying it was. Picture that in a retrieval system serving medical guidance, where the opposite instruction comes back as the best match.

## Three fixes, in the right order

His remedies, to combine as needed:

- **Choose a domain model.** A medical or legal embedding model trained on that vocabulary, many of which are on Hugging Face.
- **Preprocess on ingestion.** Expand numbers and dates into words, spell out abbreviations, add metadata to disambiguate entities like Apple the fruit and Apple the brand.
- **Fine-tune.** Build sentence pairs labelled with target similarity (generated with an LLM and curated, or your own data), split into train, validation and test, then fit with Sentence Transformers using a loss function and an embedding similarity evaluator.

After fine-tuning, the same 38 scenarios drop sharply, some into negative cosine scores; the negation case falls to 46%. A few stay high, which he treats honestly: more data, different epochs, or maybe it doesn't matter for your use case (capitalisation might not).

## Fine-tuning is the last step, not the first

His closing advice is the senior-engineer part. Know your data, evaluate the base model on your own examples before trusting it, prefer a model someone has already tuned, and fine-tune only if needed. Keep a baseline, evaluate systematically and keep iterating. The demo code is on GitHub.

## Who should watch

Anyone building RAG, semantic search or recommendations, especially in medical, legal or financial domains where a negation is the whole meaning.

## Related Conf42 talks

- [Ofer Mendelevitch (Vectara) on measuring hallucinations in RAG](https://www.conf42.com/Large_Language_Models_LLMs_2024_Ofer_Mendelevitch_rag_measuring_hallucinations), the generation-side counterpart.
- [Daniel Svonava (Superlinked) on running embedding-powered apps in production](https://www.conf42.com/Machine_Learning_2023_Daniel_Svonava_vector_ops_embeddingpowered_apps), vector ops beyond the model choice.
- [Alejandro Duarte on RAG in production: challenges, techniques and solutions](https://www.conf42.com/Database_DevOps_2026_Alejandro_Duarte_llm_vectors_semantic), for the rest of the pipeline.

[Watch Ritesh Modi's talk](https://www.conf42.com/Machine_Learning_2025_Ritesh_Modi_embedding_models_language)

[Watch the talk on YouTube](https://youtu.be/tzk4sQD-l3U).

## Watch the talk

[Hallucination by Design: How Embedding Models Misunderstand Language](https://www.conf42.com/Machine_Learning_2025_Ritesh_Modi_embedding_models_language) at Conf42 Machine Learning 2025.
