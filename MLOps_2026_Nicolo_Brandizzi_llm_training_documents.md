# From 173 Billion Documents to Training Data: A Beginner's Tour of LLM Data Processing

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Nicolo Brandizzi](https://www.conf42.com/speaker_Nicolo_Brandizzi) (Senior Research Scientist @ Fraunhofer IAIS). Page: https://www.conf42.com/MLOps_2026_Nicolo_Brandizzi_llm_training_documents

## Abstract

A model learns everything it knows from its training data. Where does that data come from, and what makes text suitable? This talk answers both questions based on our work at Fraunhofer IAIS  The running example is OpenGPT-X, the project that produced the open Teuken models. I follow its data from a raw Common Crawl dump to a clean, deduplicated corpus: what curated sources and web crawls each give you, why metadata normalization matters, how filtering removes 96.94% of web documents (and why that is the pipeline doing its job), and why deduplication consumes 80% of the compute budget.  Every claim comes with an honest number, from CPU hours to euros per document. By the end you will know how a training corpus is built, and what that tells you about the models trained on it. No data-pipeline experience needed.
