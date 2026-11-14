# Your AI outage model failed because of governance, not the model

Conf42 Blog, 2026-04-09. https://www.conf42.com/blog/cloud2026/data-governance-is-a-chain-of-custody

In short: Karthik Ravva of Austin Energy at Conf42 Cloud Native 2026 on embedding data governance in every lifecycle stage, from ingestion to auditable deletion.

A utility rolls out an AI model to predict outages, it misses a big one, and the post-mortem finds nothing wrong with the algorithm. At Conf42 Cloud Native 2026, [Karthik Ravva](https://www.conf42.com/Cloud_Native_2026_Karthik_Ravva_ai_agents_reasoning), Senior Product Manager at Austin Energy, used that story to argue that most AI failures are data governance failures, and that governance has to be built into each stage of the data lifecycle rather than bolted on after deployment.

It's a short, framework-level talk from someone who runs emergency data platforms at a utility. Expect a blueprint and a phased plan, not code.

## Teams build first and ask how to govern it later

Ravva's diagnosis is about sequencing. Organisations deploy models across several cloud providers, ship them to production, and only then work backwards to the governance question. The result is fragmented ownership, compliance gaps under GDPR, CCPA, TCPA and HIPAA that need provable lineage, and AI and BI output nobody fully trusts. His summary line: "AI that everybody's talking about is only as good as the data behind it."

## Four layers, one chain of custody

The blueprint has four layers, and the point is that governance lives inside each of them:

1. **Ingestion.** The first and most important control point. Validate, encrypt and record provenance at the gate, enforce structure at the schema and transformation level, and catalog every attribute before bad data spreads. Skip this and you scale bad metadata faster.
2. **Classification and cataloging.** Use ML models to classify data as it lands, because humans can't keep up with the volume. Classification is continuous, not a one-off.
3. **Access control and ownership.** If asking who owns a dataset gets several answers, you don't have ownership. He names the usual roles (data steward, data owner, domain owner, platform team) and pairs them with role-based access control.
4. **Tiered storage.** Archive (long-term, immutable, cryptographic audit trails), cold (rare access with lifecycle policies), warm (operational data for scheduled BI loads) and hot (active AI pipelines, strict RBAC, real-time monitoring). His utility example for hot data is the ADMS platform that utilities lean on to predict the next outage.

## Deletion is where governance gets tested

The sharpest section is about the end of the lifecycle. Data lives in many places at once, so the real audit question is whether you can prove it's gone. Ravva's answer is retention policy by design: when AI classifies data into a tier, attach the compliance flags right there, and make every deletion or retention decision auditable. Automating that is what shortens regulatory response times and takes manual work off the compliance team.

He also wants observability at each of the four layers, so schema drift and behavioural changes in the data get caught by the pipeline instead of by the outage model.

## Stage it, don't boil the ocean

The implementation plan has four phases: foundation (ownership, metadata, classification taxonomy), ingestion and access, the AI intelligence layer, then lifecycle automation. The order matters. AI classification can't work without the rules you defined in the foundation phase, so doing everything at once mostly produces confident mislabels. For multi-cloud and hybrid estates, he wants policies defined as code, one audit platform and one catalog across clouds. As he put it: "Governance maturity is built, not acquired after deployment."

## Who should watch

Product managers and data platform leads who have to convince leadership that a governance programme is worth doing before the next model goes live. Engineers looking for implementation detail will want to pair it with something more hands-on.

## Related Conf42 talks

- [AI-Driven Data Quality Management: Boosting Accuracy and Speed with Python](https://www.conf42.com/Python_2025_Shashank_Reddy_Beeravelly_data_quality_management) by Shashank Reddy Beeravelly at Conf42 Python 2025.
- [Data Quality and Validation in ML Pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) by Sunil Kumar Mudusu at Conf42 Machine Learning 2025.
- [AI-Driven Sensitive Data Discovery for Secure DevSecOps and Privacy Compliance](https://www.conf42.com/DevSecOps_2026_Mary_Sirisha_Duggimpudi_datadiscovery_privacy_compliance) by Mary Sirisha Duggimpudi at Conf42 DevSecOps 2026.

[Watch Karthik Ravva's talk](https://www.conf42.com/Cloud_Native_2026_Karthik_Ravva_ai_agents_reasoning) or the [YouTube recording](https://youtu.be/FisE1JzdClk).

## Watch the talk

[Cloud-Native Data Lifecycle Governance for Trusted AI & BI](https://www.conf42.com/Cloud_Native_2026_Karthik_Ravva_ai_agents_reasoning) at Conf42 Cloud Native 2026.
