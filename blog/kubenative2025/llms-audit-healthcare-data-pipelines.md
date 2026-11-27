# LLMs that audit healthcare data pipelines, not just generate text

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/llms-audit-healthcare-data-pipelines

In short: Manikesh Iruku of Amazon presents at Conf42 Kube Native 2025 an LLM framework that audits EHR pipelines with hierarchical, chain-of-thought prompts.

A broken join in a healthcare ETL job doesn't throw an exception; it quietly drops a medication from a safety alert. At Conf42 Kube Native 2025, Manikesh Iruku, Business Intelligence Engineer at Amazon, presented research on using LLMs to audit electronic health record (EHR) pipelines for exactly those silent, semantic errors, using a layered prompting strategy rather than a bigger model.

It is a research presentation: architecture, method and reported results, with no live demo.

## Manual audits see a third of the logic

Hospitals move EHR records, lab results, imaging, prescriptions and admin data through systems such as Epic and Cerner, and every hop is a transformation someone has to trust. Iruku cites research that manual audits examine only 35% of transformation logic and catch 52% of known pipeline issues in controlled settings. Rule-based checks scale better but mostly validate structure and syntax. Neither reliably catches the expensive kind of bug: logic that runs fine but contradicts a clinical guideline or business rule.

## Three tiers of prompts

The framework's core is a prompt hierarchy:

- **Structural prompts** look at SQL syntax, ETL connectivity and data type consistency.
- **Semantic prompts** check clinical appropriateness: guideline adherence, temporal logic, cross-domain consistency.
- **Comparative prompts** compare components across versions and reconcile between systems.

Chain-of-thought workflows break each audit into steps that mirror how an expert reviewer reasons, while keeping track of dependencies across domains. Compared with standard prompting, he reports a 42% improvement in error detection sensitivity and a 35% cut in false positives.

Around the prompts sit five components: read-only data extraction from existing systems, a prompt generation engine fed with guidelines and organisation rules, an LLM orchestration service, an interpretation module that turns outputs into findings, and an audit management system that tracks remediation.

## The reported results

Iruku's numbers: an 87% detection rate against 52% for manual audits and 63% for rule-based systems; annual audit effort down 70%, from 2,400 to 720 hours; pipeline coverage up from 35% to 92%; and around $340,000 in annual savings. On complex logic specifically, 94% accuracy versus 34% for manual review. The figure that stuck with me is guideline update lag, down from 47 days with rule-based systems to two, which matters when a protocol changes and the pipeline should follow.

The case studies are concrete about the bug types: incomplete medication reconciliation logic feeding patient safety alerts, a sepsis bundle dashboard whose calculations didn't match its specification, and heart failure protocols that hadn't caught up with updated AHA/ACC guidelines.

## Humans still sign off

He closes on governance: human oversight with clear responsibility, transparency about model limits, equity in pipeline coverage, and HIPAA-compliant privacy assessments. The quickest return, in his account, came from running the audits inside CI/CD. Next steps include streaming audits, domain fine-tuning and shift-left checks at design time.

## Who should watch

Data engineers and analytics leads in healthcare or any regulated industry, and anyone who suspects their "data quality" checks are really schema checks. The Kubernetes angle is light, so platform folks hunting for cluster detail can skip it.

## Related talks

- Sunil Kumar Mudusu on the ML side of the same problem: [Data Quality and Validation in ML Pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation).
- Venugopal Reddy Depa on moving healthcare data between systems: [API-Led Healthcare Transformation](https://www.conf42.com/Cloud_Native_2025_Venugopal_Reddy_Depa_api_healthcare_interoperability).
- A finance cousin with the same human-in-the-loop stance: Naveen Gowda's [AI-Driven Financial Reconciliation](https://www.conf42.com/Large_Language_Models_LLMs_2025_Naveen_Gowda_financial_reconciliation_compliance).

[Watch Manikesh Iruku's talk](https://www.conf42.com/Kube_Native_2025_Manikesh_Iruku_ehr_pipelines_accuracy)

[Watch the talk on YouTube](https://youtu.be/iOU9S51BoDQ).

## Watch the talk

[LLM-Audited EHR Pipelines: 87% Accuracy with 70% Fewer Resources](https://www.conf42.com/Kube_Native_2025_Manikesh_Iruku_ehr_pipelines_accuracy) at Conf42 Kube Native 2025.
