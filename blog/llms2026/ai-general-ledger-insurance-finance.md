# Continuous reconciliation for insurance ledgers with Kafka and ML

Conf42 Blog, 2026-05-28, updated 2026-11-09. https://www.conf42.com/blog/llms2026/ai-general-ledger-insurance-finance

In short: Rakesh Jha (DXC Technology) at Conf42 LLMs 2026 on AI general ledgers for life and annuity insurers, from Kafka ingestion to ML anomaly detection.

How long does your month-end close take? At Conf42 Large Language Models (LLMs) 2026, Rakesh Jha of DXC Technology, who works on finance systems for life and annuity insurers, argues that a close measured in days is a system design problem, and walks through an AI-enabled general ledger that reconciles each transaction as it posts instead of saving them all for the weekend.

A note on scope: despite the event, this is mostly a talk about event streaming and classic machine learning (LSTMs, random forests, isolation forests) applied to accounting. Language models appear at the edges, chiefly natural language processing of contracts on his watch list. If you work anywhere near insurance finance, that's a feature.

## The numbers he anchors on

Rakesh opens with three figures he attributes to KPMG-published analysis of AI in insurance: around 30% less time on routine reconciliation, 40% less manual intervention in routine accounting, and a 35% faster month-end close. He is careful about the 40%: it means 40% of the work is automated, not 40% fewer people, and the best organisations he works with use the time to make teams smarter rather than smaller. The close gets faster because validation runs all month, so less is left to investigate at the end.

## Four layers of ingestion before any model

Traditional ledgers batch the day overnight, so morning decisions run on stale numbers. His design processes transactions as they happen: a lapse, a death claim or an annuity payment hits the ledger immediately. Apache Kafka carries every financial transaction as an event. A normalisation layer reconciles formats from policy admin, investment, claims and reinsurance systems. Buffer management absorbs the spike from a typical 200,000 transactions a day to two or three million at quarter end without losing any.

## An ensemble of specialists

The ML pipeline runs feature engineering, models, an inference engine that applies regulatory rules in the same step, and an analytics layer that feeds improvements back.

Feature engineering gets the most attention, with a good analogy: a 3 a.m. call from an unknown number means little until you know it's the third in ten minutes from a country you never deal with. Same with money. A premium on the 1st and the same amount on the 28th are different events.

Then the specialists. An LSTM remembers sequences: a policyholder who paid on the 5th for eight years, 96 payments, suddenly paying on the 28th is a pattern break worth flagging. A random forest classifies which account a transaction belongs to and copes with imperfect data. An isolation forest finds the odd one out, like one suspicious death claim among three million transactions.

## Reconcile continuously, not on Fridays

The reconciliation section will feel familiar to finance teams: thousands of items on a Friday spreadsheet, the oldest the hardest to trace, weekend work, then Monday starts again. His point is that the system was designed to accumulate differences, so fix the design. Check every transaction as it posts and flag mismatches immediately. He cites research suggesting roughly 80% less processing time when moving from manual batch to continuous reconciliation. A sliding window learns recurring patterns, like a reinsurance treaty that always produces a timing difference on the 15th, and stops flagging them.

Anomaly detection has two layers: statistical checks such as z-scores on every transaction, and semi-supervised learning from past fraud cases and reserve errors. Compliance validates each transaction against current rules (NAIC regulations, state requirements, Sarbanes-Oxley) before posting, with immutable logs and versioned rules so auditors can see exactly what applied when.

## Who should watch

Engineers and architects in insurance and fintech, especially anyone who owns a batch ledger. LLM specialists looking for prompt patterns won't find them here. The closing watch list of blockchain for reinsurance, NLP over treaties and edge computing at agencies is speculative and labelled as such.

## Related Conf42 talks

- [AI-Driven Financial Reconciliation: Enhancing Accuracy, Speed, and Compliance Through Human-AI Synergy](https://www.conf42.com/Large_Language_Models_LLMs_2025_Naveen_Gowda_financial_reconciliation_compliance) by Naveen Gowda, reconciliation from the year before, with more of the human side.
- [Optimizing Financial Operations with Large Language Models: A CFO's Perspective](https://www.conf42.com/Large_Language_Models_LLMs_2025_Andriy_Bagryantsev_financial_operations_cfo) by Andriy Bagryantsev, where LLMs take a bigger role in finance.
- [AI-Driven Insurance Operations: MLOps Strategies](https://www.conf42.com/MLOps_2025_Sameer_Joshi_ai_driven_insurance) by Sameer Joshi, for running these models in an insurer.

[Watch Rakesh Jha's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Rakesh_Jha_ledgers_finance_accounting)

[Watch the talk on YouTube](https://youtu.be/UQahnXR6_7Q).

## Watch the talk

[LLM-Driven Financial Ledgers: Building Intelligent, Real-Time Accounting Systems at Scale](https://www.conf42.com/Large_Language_Models_LLMs_2026_Rakesh_Jha_ledgers_finance_accounting) at Conf42 Large Language Models (LLMs) 2026.
