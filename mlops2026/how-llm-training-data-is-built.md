# Filtering throws away 96.94% of the web, and that's the point

Conf42 Blog, 2026-11-10. https://www.conf42.com/mlops2026/how-llm-training-data-is-built

In short: Nicolo Brandizzi (Fraunhofer IAIS) at Conf42 MLOps 2026 gives a beginner's tour of LLM training data, from Common Crawl to the OpenGPT-X corpus.

Most of the web is not fit to train a language model, and a good data pipeline proves it by throwing almost everything away. At Conf42 MLOps 2026 on November 19, Nicolo Brandizzi, Senior Research Scientist at Fraunhofer IAIS, follows real training data from a raw Common Crawl dump to a clean, deduplicated corpus, and explains why filtering removes 96.94% of web documents.

The running example is OpenGPT-X, the project that produced the open Teuken models. The title's number is the starting scale: 173 billion documents on one end, training data on the other.

## A model is what it ate

The talk starts from a simple premise: a model learns everything it knows from its training data. So two questions follow. Where does that data come from, and what makes a piece of text suitable?

Nicolo answers both from the work at Fraunhofer IAIS. Curated sources and web crawls each give you different things, and the trade-offs between them shape the model you end up with. This is the bit that turns the usual line about models being trained on the internet from a shrug into something you can reason about.

## Metadata normalisation, the unglamorous hero

Before filtering and deduplication can do their jobs, the data has to agree with itself. The abstract singles out metadata normalisation as something that matters, and anyone who has merged two datasets with different ideas about what a language code or a date looks like will nod along. Pipelines at this scale amplify small inconsistencies into large ones.

## The pipeline doing its job

Then comes filtering, and the headline number. Removing 96.94% of web documents sounds like a pipeline gone rogue. Nicolo's framing is the opposite: that is the pipeline doing its job. The web is full of boilerplate, spam, near-empty pages and text that would teach a model bad habits, and a filter that keeps a few percent is a filter that works.

It is a healthy reframe for anyone who measures data work by volume. Here the valuable output is mostly the stuff you decided not to keep.

## Deduplication eats the compute

The second surprise: deduplication consumes 80% of the compute budget. Finding repeated text across a corpus of this size is expensive work. If you ever planned a data pipeline by assuming the clever model-based steps would dominate the bill, this is a useful correction.

Nicolo promises an honest number behind every claim, from CPU hours to euros per document. That level of cost accounting is rare in public talks about LLM data, and it is the reason to watch even if you never plan to pre-train anything yourself.

## Who should watch

This is explicitly a beginner's tour; no data-pipeline experience needed. That makes it a good fit for MLOps and platform engineers who serve or fine-tune models and want to understand what went into them, and for data engineers curious how their skills map onto LLM pre-training. Researchers who already run deduplication at scale will find the numbers interesting but the concepts familiar.

You should leave knowing how a training corpus is built, and what that tells you about the models trained on it.

## Related Conf42 talks

- [Beyond Pre-training: Scaling Cloud-Native LLMs with Contextual Data for Real-Time AI](https://www.conf42.com/Cloud_Native_2025_Ankit_Awasthi_llm_data_performance) by Ankit Awasthi, what happens to data after pre-training.
- [Fine-tuning LLMs: A Cost-Benefit Analysis for Businesses](https://www.conf42.com/Large_Language_Models_LLMs_2025_Muddassar_Sharif_fine_tuning_business) by Muddassar Sharif, another talk that puts money next to model work.
- [Building Efficient and Frugal Image Data Processing Pipelines](https://www.conf42.com/Platform_Engineering_2024_Anna_Heng_Chi_image_data_processing) by Anna Heng Chi, frugal data pipelines in a different modality.

[Watch Nicolo Brandizzi's talk](https://www.conf42.com/MLOps_2026_Nicolo_Brandizzi_llm_training_documents) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[From 173 Billion Documents to Training Data: A Beginner's Tour of LLM Data Processing](https://www.conf42.com/MLOps_2026_Nicolo_Brandizzi_llm_training_documents) at Conf42 MLOps 2026.
