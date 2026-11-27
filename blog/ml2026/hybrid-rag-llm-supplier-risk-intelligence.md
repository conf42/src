# Supplier risk starts outside the ERP, so the model has to look there

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/hybrid-rag-llm-supplier-risk-intelligence

In short: Oracle's Sujith Vadakkepati at Conf42 Machine Learning 2026 on an explainable hybrid RAG-LLM pattern for continuous, auditable supplier risk intelligence.

A supplier can be green on every internal metric, on-time and freshly audited, while a regulator is already investigating it. At [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026), Sujith Vadakkepati, senior principal product manager at Oracle working on supplier qualification and risk, presented an explainable hybrid RAG-LLM framework that pulls external signals in next to ERP data and produces risk narratives an auditor can trace back to evidence.

He is explicit that this is "a pattern, not a product." No chatbot, no Oracle feature tour: an architecture for putting generative AI to work inside the constraints of a procurement and compliance organisation.

## The system of record is always late

Traditional supplier risk runs on scorecards, thresholds and quarterly or annual reviews over structured ERP data. That suits slow, stable environments. Modern supply risk is neither. It is triggered by pandemics, sanctions, geopolitical tension, litigation and ESG violations that surface first in news, filings and enforcement actions, long before they show up as a missed delivery. His core insight: "the system of record is never where risk first appears."

He names three gaps that reinforce each other: static rules that assume we already know what risk looks like, limited sources that ignore unstructured external data, and threshold-based detection that fires only once the risk is already big.

## Retrieve first, then reason

The framework is a pipeline with separated responsibilities, which is why he thinks it survives regulated, high-stakes use:

1. **A RAG grounding layer** gathers evidence from internal systems (performance history, compliance data) and external intelligence (regulatory actions, news, ESG disclosures). It defines what the system actually knows.
2. **An LLM reasoning layer** connects signals across domains and explains why a risk profile may be shifting, anchored to the retrieved evidence. If the data isn't there, it doesn't invent an answer.
3. **Risk narratives** replace a bare score: which evidence was used, how the signals combined, and where uncertainty remains.

The data layer pairs ERP context with four external streams: geopolitical indicators, financial stability signals such as credit stress and rating changes, regulatory signals such as warning letters and litigation, and ESG performance, treated as a primary input. Sources are normalised and tagged with metadata like recency and source credibility so the retriever can weigh them.

## Weak signals add up

The detection argument is the interesting part. A small financial concern, some regulatory scrutiny and an ESG flag may each look minor, and none crosses a threshold. Together they can mark a supplier heading for trouble. Because retrieval runs continuously and in parallel, a new filing or enforcement action is evaluated almost as soon as it appears, instead of at the next review cycle.

He reports evaluations across manufacturing and technology supplier networks showing better detection precision, faster response and broader risk coverage than rule-based systems. The talk gives the direction of those results, not the figures.

## Governance is in the architecture

Every step leaves a record. Retrieval logs which documents were pulled, from where, when and why. Extraction ties each fact to its source. Synthesis produces the structured narrative. Human review, including approvals, overrides and escalations, joins the audit trail. On top sit three controls: bias monitoring across data, weighting and outputs; interpretability for every assessment; and structured human oversight, because this is decision support, not an autonomous decision maker.

## Who should watch

Procurement, compliance and risk engineering teams evaluating LLMs, and anyone building RAG over mixed internal and external sources where every answer must be defensible. It is architecture-level; if you want retrieval tuning or prompt details, bring your own.

## Related Conf42 talks

- [SRE for supply chain: building reliable human-AI warehouse operations](https://www.conf42.com/DevOps_2026_Vishnu_Prasad_supplychain_reliability_warehouses), Vishnu Prasad (ERP Initiatives Group), Conf42 DevOps 2026
- [Predictive observability: prevent supply chain outages before they break production](https://www.conf42.com/DevOps_2026_Raghu_Bhupatiraju_predictive_analytics_outages), Raghu Bhupatiraju (Expeditors), Conf42 DevOps 2026
- [AI-powered anomaly detection and self-healing systems for resilient supply chains](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Venkata_Anil_Kumar_Nilisetty_ai_powered_anomaly), Venkata Anil Kumar Nilisetty (Cognizant), Conf42 SRE 2025

[Watch Sujith Vadakkepati's talk](https://www.conf42.com/Machine_Learning_2026_Sujith_Vadakkepati_deployment_containers_kubernetes)

[Watch the talk on YouTube](https://youtu.be/5tzUA38kNN8).

## Watch the talk

[Explainable Hybrid RAG–LLM Framework for Dynamic Supplier Risk Intelligence](https://www.conf42.com/Machine_Learning_2026_Sujith_Vadakkepati_deployment_containers_kubernetes) at Conf42 Machine Learning 2026.
