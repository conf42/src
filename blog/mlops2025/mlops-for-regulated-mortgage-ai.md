# Mortgage MLOps can't move fast and break things

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/mlops-for-regulated-mortgage-ai

In short: Naganarendar Chitturi (Newrez) at Conf42 MLOps 2025 on MLOps for autonomous mortgage AI, where explainability is legally required and models shadow whole loans.

In mortgage lending, breaking things means someone does not get their home or your company faces fair-lending fines. Naganarendar Chitturi, Senior Automation Architect at Newrez, uses that to explain at Conf42 MLOps 2025 why standard MLOps had to be reworked for autonomous mortgage AI, and how it can still shrink a 30-to-60-day loan process to three to five days.

This is one of the more grounded talks of the event: a regulated domain, legacy systems, and concrete patterns for each.

## 47 steps and a weekend in a queue

Naganarendar starts with the process. A straightforward purchase loan has 47 distinct steps. An application submitted on Friday evening waits in a queue until Monday, employment verification means calling an HR department that may reply on Tuesday, the appraisal is booked for the following week, and bank statements are reviewed line by line. Every step touches different people and systems that do not talk to each other.

The data is just as messy: structured credit bureau feeds, unstructured tax returns and bank statements, real-time property valuations, and loan data in mainframe systems from the 1980s with batch files and formats older than the web. Much of the AI, he says, exists purely to translate between modern pipelines and those systems.

## Explainability is the law here

The regulatory point is what makes mortgage ML different. If you deny a loan, you must give specific, understandable reasons that regulators can audit, so every decision must trace back through the pipeline with full lineage. He recalls an examiner asking about one loan decision from 18 months earlier. With the right architecture he could pull up, in seconds, which models were involved, what data they used, which business rules fired, and the exact versions that were live.

His team's answer is compliance-first feature engineering: every feature pipeline automatically includes bias detection, PII anonymisation and audit trail generation, and the feature code produces documentation compliance officers can use in regulatory submissions.

## Validate across groups, shadow across loan lifecycles

Training is optimised for fairness, explainability and compliance alongside accuracy. He describes regulatory-aware cross-validation, where validation sets are built to test performance across demographic groups, geographic regions and market conditions.

The deployment pattern is the one to remember. Because a loan takes weeks to close, a bad model may not show its damage for weeks. So new models run in extended shadow mode next to production for complete loan lifecycles before any traffic moves. That is a much longer canary than most teams would tolerate, and in this domain it is the right one.

## Documents are the hard part

Document processing is, in his words, one of the most complex parts of the system. PDFs arrive scanned at odd angles, bank statements come in hundreds of formats, pay stubs vary by employer and by year. They use an ensemble of OCR models because no single one handles every document type, plus named entity recognition trained for financial documents that knows gross from net income. Separate model versions handle older and newer document layouts, since applicants submit historical paperwork.

Privacy-by-design pipelines identify and mask PII automatically and log every access. The credit scoring model never sees raw bank statements, only engineered financial-behaviour features from the feature store. Storage is tiered into hot (under 50 ms retrieval for live decisions), warm for training, and cold for long-term regulatory retention. During peaks they make tens of thousands of external API calls an hour to bureaus and verification services, each with its own quirks and outages.

He also mentions results from his work: savings he puts at $8 million, and a generative AI chatbot that handles about 60% of customer service inquiries.

## Who should watch

ML engineers in lending, insurance, banking or any field where a model decision can be challenged in front of a regulator. The shadow-for-a-full-lifecycle pattern and compliance-first features are useful well beyond mortgages.

## Related Conf42 talks

- [Naganarendar Chitturi on building agentic AI platforms for autonomous mortgage processing](https://www.conf42.com/Platform_Engineering_2025_Naganarendar_Chitturi_mortgage_autonomous_lessons) at Conf42 Platform Engineering 2025.
- [Satish Manchana (UBS) on compliance-aware platform engineering in regulated finance](https://www.conf42.com/Platform_Engineering_2025_Satish_Manchana_aware_regulated_hybrid) at the same event.
- [Sandeep Gourneni (Hitachi Digital Services) on LLM-powered legacy banking code transformation](https://www.conf42.com/Machine_Learning_2025_Sandeep_Gourneni_banking_optimization), for the mainframe problem.

[Watch Naganarendar Chitturi's talk](https://www.conf42.com/MLOps_2025_Naganarendar_Chitturi_paperwork_pipeline_building) for the full pipeline design.

[Watch the talk on YouTube](https://youtu.be/g-v-F4k6S5Q).

## Watch the talk

[From Paperwork to Pipeline: Building MLOps for Autonomous Mortgage AI](https://www.conf42.com/MLOps_2025_Naganarendar_Chitturi_paperwork_pipeline_building) at Conf42 MLOps 2025.
