# Put AI data governance inside the CI/CD pipeline

Conf42 Blog, 2025-08-31, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/training-data-declarations-genai-governance

In short: Bhanu Maryala (Informatica) at Conf42 MLOps 2025 on Training Data Declarations, a framework that runs compliance checks inside MLOps pipelines.

Governance that lives in a review meeting will always lose to a deadline. At Conf42 MLOps 2025, Bhanu Maryala, Senior Solution Architect at Informatica, presented Training Data Declarations (TDD), a framework that embeds data governance for generative AI directly into CI/CD so compliance checks run automatically instead of queuing for a human.

The talk is about twenty minutes and aimed at teams shipping generative AI under real regulatory pressure.

## Speed or compliance is a false choice

Bhanu opens with three tensions every enterprise AI team knows: speed versus compliance, provenance tracking that gets harder as datasets grow, and the regulatory burden of operating in several jurisdictions at once. The usual framing is "move fast or stay compliant." His answer is both, and the way to get both is to stop treating governance as a gate outside the pipeline.

(Yes, the acronym collides with test-driven development. Same instinct, though: write the rules down first and let the machine enforce them.)

## What the framework actually contains

TDD has four core pieces:

- A **four-tier classification system** that sorts datasets by risk and provenance, from highly trusted to restricted sources.
- A **standard metadata schema**, so every dataset carries the same governance information, including licensing and transformation history.
- **Real-time risk assessment** that runs continuously from ingestion through training and into runtime.
- **Comprehensive audit trails** that leave regulators a complete record.

The design principle that ties them together: governance travels with the model wherever it is deployed. Bhanu shows it running across AWS (S3, Lambda, SageMaker), Azure (Blob Storage, Functions, Azure Machine Learning), GCP (Cloud Storage, Functions, Vertex AI) and Snowflake through native procedures. Container-native governance tools and Kubernetes-based policy enforcement handle checks before, during and after deployment, with dashboards giving near-instant feedback.

## Licensing is the gap nobody budgets for

The most concrete section is about licensing. Many training datasets include copyrighted or ambiguously licensed material, and in generative AI that turns into legal exposure the moment the model ships. TDD adds automated license detection, risk evaluation and remediation, all before deployment. Bhanu shows a short Python snippet that scans directories, validates policies and flags risky files before they reach training.

There is also jurisdiction-specific automation: different regions have different rules, and the framework adapts checks to regional requirements and cross-border data flows rather than forcing one global policy.

## A case study in review time

The financial services example is a large institution that wanted generative AI in customer service under strict regulation. With TDD and industry-specific rules, Bhanu says the team cut compliance review time by 87% while keeping full regulatory adherence. That is the claim of the talk in one number: governance automation should make releases faster, not slower.

He maps the framework onto the pipeline stage by stage. Metadata collection starts at ingestion, governance checks run during pre-processing, lineage is tracked through training, compliance is verified before validation and deployment, and monitoring continues in production.

## Who should watch

ML platform engineers and data governance leads in regulated industries who are tired of compliance being a manual step at the end. It is a framework overview with one code sample, so bring your own implementation questions.

## Related Conf42 talks

- [Compliance as a Pipeline Stage: Automating AI Governance in MLOps](https://www.conf42.com/MLOps_2026_Arpita_Sheth_compliance_governance_pipeline)
- [GenOps: A Governance-Driven Model for Safe, High-Velocity AI in CI/CD Pipelines](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity)
- [Designing a Scalable Data Governance Framework for Multi-Tenant Cloud Contract Management](https://www.conf42.com/Machine_Learning_2025_Kushal_Shah_governance_framework_cloud)

[Watch Bhanu Maryala's talk](https://www.conf42.com/MLOps_2025_Bhanu_Maryala_automating_ai_ethics)

[Watch the talk on YouTube](https://youtu.be/KBNSRrFcdZs).

## Watch the talk

[Automating AI Ethics: MLOps-Native Data Governance for Production-Ready Generative AI Pipelines](https://www.conf42.com/MLOps_2025_Bhanu_Maryala_automating_ai_ethics) at Conf42 MLOps 2025.
