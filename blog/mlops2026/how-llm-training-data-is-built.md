# Filtering throws away 96.94% of the web, and that's the point

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/how-llm-training-data-is-built

In short: Nicolo Brandizzi (Fraunhofer IAIS) at Conf42 MLOps 2026 on turning 173 billion Common Crawl documents into LLM training data, with the CPU and euro bills.

Run deduplication before filtering and the job costs 750 CPU years instead of 25. That single reordering is the most memorable number in the talk Nicolo Brandizzi, senior research scientist at Fraunhofer IAIS, gave at Conf42 MLOps 2026. He co-leads the data team there, and he walks through how the OpenGPT-X project, which produced the open Teuken models, turned 173 billion web documents into a training corpus. It is pitched as a beginner's tour and it is one, with real bills attached.

## Two sources, one record format

Training data comes in two kinds. Curated sources such as books, encyclopedias and parliament transcripts have been through an editorial process. Web data, meaning Common Crawl, is enormous and mostly low value: an article body surrounded by ads, footers and navigation.

The curated pipeline is light: format conversion, content normalization, language detection, metadata normalization, some filtering. His example of why normalization matters is the word café. The accented e can be one character or a plain e plus a combining accent. They look identical to you and the tokenizer sees two different words.

The web pipeline starts from Common Crawl's WET files, chosen over WARC because some HTML noise is already removed, and adds quality scoring, harmful content detection, a cheap pre-filter, heavier filtering and finally deduplication. Both paths end in the same JSONL record: the text plus metadata about source, language and scores. His first takeaway is to keep that lineage, so that when an evaluation result moves you can trace it back to the config change that caused it.

## 1.2 million years of reading

The raw input was 173 billion documents, about 700 terabytes from 60 Common Crawl dumps. The abstract gives the share removed as 96.94%. About five billion documents remain.

To show that this is the pipeline working, he converts it to reading time. A person reading at average speed would need around 1.2 million years for the full set, which he notes is four times longer than our species has existed. The five billion survivors still take 35,000 years, roughly the age of the oldest cave paintings. Plenty left.

The cheap filters that do much of the removal do not understand text at all. Count words per line and keep lines above four. Count symbols and keep documents under 30%. That is enough to keep an article and drop a navigation menu and a log dump.

## Order is a cost decision

Add up every step and the pipeline took 31 years of single-core CPU time. Deduplication, done locally with MinHash and LSH, accounts for 80% of it, about 25 of the 31 years. That is why it sits last, after filtering has shrunk the input. Swap the order and deduplication alone needs 750 CPU years, more than thirty times as much.

"the order is a cost decision and it matters," Nicolo Brandizzi said at Conf42 MLOps 2026.

Then he complicates it. CPU time and wall-clock time are different budgets. Measured in terabytes processed per day, the slowest steps were downloading and filtering, and since the steps run in series the slowest one sets the calendar. Add euros and you have three variables, compute, money and calendar days, that influence each other and that a project has to plan for from the start.

## Form is cheap to check, value is not

The cheap filters have a blind spot. A paragraph on photosynthesis and a line of cheap-flight spam both pass, because both are well formed. Meanwhile code or translator-style notes with many symbols can be dropped despite being valuable. Filters see form. Value needs a reader.

The current answer is an LLM as judge, rating each document from zero to five. He prices it: about 300 euros per million documents at mid-2026 rates, which comes to around 1.5 million euros for the five billion. Too much.

So the last part is about proxies. His framing: "bad text and bad quality data is easy to spot and good is not". Good depends on what the model is for. He describes a trust ladder with human reviewers on top (most trusted, most expensive), LLM judges in the middle and heuristics at the bottom (nearly free, blind to value). The work is passing trust downward: humans calibrate the judge, the judge labels a sample, and cheaper filters are learned from those labels. He cites FineWeb's educational-value score as one such proxy. There is no magic formula, he says, and any quality score is only confirmed after training, at evaluation.

## Who should watch

Engineers and researchers who use pretrained models or Hugging Face datasets and have never seen how the text got there. People who already run web-scale data pipelines will find it introductory, though the CPU-year and euro figures are worth having as reference points. The delivery is unhurried and the slides carry references for the deduplication comparison.

## Related Conf42 talks

- [Beyond Pre-training: Scaling Cloud-Native LLMs with Contextual Data for Real-Time AI](https://www.conf42.com/Cloud_Native_2025_Ankit_Awasthi_llm_data_performance) by Ankit Awasthi, what happens to data after pre-training.
- [Fine-tuning LLMs: A Cost-Benefit Analysis for Businesses](https://www.conf42.com/Large_Language_Models_LLMs_2025_Muddassar_Sharif_fine_tuning_business) by Muddassar Sharif, another talk that puts money next to model work.
- [Building Efficient and Frugal Image Data Processing Pipelines](https://www.conf42.com/Platform_Engineering_2024_Anna_Heng_Chi_image_data_processing) by Anna Heng Chi, frugal data pipelines in a different modality.

[Watch Nicolo Brandizzi's talk](https://www.conf42.com/MLOps_2026_Nicolo_Brandizzi_llm_training_documents) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[From 173 Billion Documents to Training Data: A Beginner's Tour of LLM Data Processing](https://www.conf42.com/MLOps_2026_Nicolo_Brandizzi_llm_training_documents) at Conf42 MLOps 2026.
