# In anti-money laundering work, a prompt is a compliance control

Conf42 Blog, 2026-10-07, updated 2026-11-09. https://www.conf42.com/blog/prompt2026/aml-prompt-is-a-compliance-control

In short: Pratik Patel of Hexaware at Conf42 Prompt Engineering 2026 on grounded, schema-checked prompts for AML investigations that never infer intent.

"Explain why this transaction is suspicious" looks like a harmless prompt until you notice it has already decided the answer. At Conf42 Prompt Engineering 2026, Pratik Patel, Principal Consultant at Hexaware Technologies, argued that in a bank a prompt is a control, and should be designed, tested and governed like any other control in an anti-money laundering (AML) workflow.

Pratik has spent more than 14 years on financial services transformation, with AML, fraud and cloud modernisation work for banks including TD Bank, Royal Bank of Canada and Santander. The talk reads like it: fewer clever tricks, more audit questions.

## The leading prompt problem

The opening contrast is the best part. The basic prompt assumes suspicion and invites the model to build a story, and models are very good at building stories when evidence is thin. The governed version reads: "Summarize the supplied transaction evidence, identify documented alert indicators, cite supporting record IDs, and flag information gaps. Do not infer criminal intent."

The model summarises instead of concluding, cites record IDs, says what's missing and stays away from intent. Pratik distils it into five principles: context grounding, structured instructions, evidence traceability, controlled reasoning (facts separate from hypotheses) and safe failure.

## Where AI sits in the pipeline

His workflow runs ingest, enrich, alert, summarise, investigate. The model helps in the last two steps only. It doesn't replace transaction monitoring and doesn't make the call. For Currency Transaction Reporting, which is rule-driven (in the US, cash over ten thousand dollars in a business day triggers a report), AI gathers related transactions and checks fields, and the analyst validates the aggregation.

The architecture is five layers: enterprise data sources, a governed cloud-native data platform, prompt orchestration, compliance applications, and governance drawn over all of them. His warning about layer two is worth repeating: if the data underneath is messy, the AI produces messy answers, only faster and more fluently.

## Facts, indicators, assessments

The pyramid slide separates three kinds of statement that must never blur. Verified facts come straight from source systems. Observed indicators are patterns that warrant review against monitoring criteria. Investigative assessments are interpretations, reviewed and owned by an analyst, never determined by the model.

His contrast example: a weak output says the customer is structuring deposits to avoid reporting. A governed one lists five cash deposits between $9,000 and $9,900 across four days, with transaction references, and says the pattern warrants analyst review. Same facts, very different liability.

## Valid JSON is not a true answer

Outputs follow a schema: case ID, transaction summary, indicators each with evidence IDs, missing information, and a review status that starts as pending analyst review, never approved. Four gates sit behind it: schema enforcement, evidence verification (if the model cites a transaction that was never retrieved, the output is rejected), completeness checks, and escalation to a correction workflow or an analyst.

The caution he underlines is the one most teams skip. A well-formed response tells you nothing about whether it's correct, which is why evidence checks and human review sit on top of schema validation.

## Fail safe, and treat documents as data

Pratik lists failure scenarios with a control for each: request more evidence when it's missing, flag conflicting customer records, reject unsupported claims, block unauthorised access, retry bad formats within limits, and require human review when confidence is low. "In regulated operations, a safe refusal or escalation is always better than a confident, unsupported answer."

He also covers prompt injection in a case file (hidden text telling the model to mark the case low risk is data, never a command) and a flat ban on autonomous regulatory submissions. Governance means versioned prompts with approval gates, least-privilege access, and audit trails good enough to answer who approved this prompt, what data it saw and who reviewed the output.

## Who should watch

Engineers and architects building LLM features in banking, insurance or any regulated review workflow. It's a framework talk without a live demo, and the rollout plan (start with bounded summarisation tasks, measure from day one) makes it a good brief to hand a compliance stakeholder.

## Related Conf42 talks

- [Designing Compliant Digital Onboarding: Cloud-Native Architectures for Trustworthy, Audit-Ready Financial Services](https://www.conf42.com/Cloud_Native_2026_Manasa_Uppula_data_streaming_realtime) by Manasa Uppula at Conf42 Cloud Native 2026.
- [Real-Time FinOps Intelligence: Template-Driven Prompt Engineering for Streaming Financial Events](https://www.conf42.com/DevOps_2026_Tina_Kanth_finops_streaming_prompts) by Tina Kanth of Microsoft at Conf42 DevOps 2026.
- [Automating the 'Governance': Building a Rules Engine for AI Use Case Governance at Scale](https://www.conf42.com/MLOps_2026_Ankur_Gupta_rules_engine_governance) by Ankur Gupta of Roblox at Conf42 MLOps 2026.

[Watch Pratik Patel's talk](https://www.conf42.com/Prompt_Engineering_2026_Pratik_Patel_aml_compliance_workflows) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/mxdV5RpwfrE).

## Watch the talk

[Prompt Engineering for AML: Building Reliable Compliance Workflows at Scale](https://www.conf42.com/Prompt_Engineering_2026_Pratik_Patel_aml_compliance_workflows) at Conf42 Prompt Engineering 2026.
