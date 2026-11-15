# Banking AI ships at the speed of its data lineage

Conf42 Blog, 2025-11-13, updated 2026-11-09. https://www.conf42.com/blog/robotics2025/ai-data-governance-lineage-banking

In short: Vinaya Nadig of Amazon at Conf42 Robotics 2025 on a unified data governance framework that makes AI in banking traceable from source data to decision.

Banks already run fleets of automated decision-makers, and the thing slowing new ones down is rarely the model; it's proving where the data came from. At Conf42 Robotics 2025, Vinaya Nadig, Principal Engineer in Amazon's Last Mile Transportation organization, made the case for a unified AI data governance framework that bakes lineage, quality and access control into the model lifecycle.

Vinaya calls governance the least exciting word in AI, then spends the talk showing why it decides what reaches production.

## Machines decide in milliseconds, reviews take months

The setup starts with 2008: opaque algorithms on incomplete data, long before generative AI. Today AI approves loans, flags fraud and suggests investments in real time. Vinaya cites survey figures that most financial institutions call governance their main barrier to scaling AI, and puts the typical deployment delay from compliance review at six to nine months. The talk's best line sums up the gap: "AI moves at milliseconds, but our controls move at human speed."

The war stories carry it. When GDPR arrived, banks paused projects to trace how customer data flowed into ML pipelines; one European bank found 30 versions of the same data set across models, with no consistent consent tracking. After the LIBOR scandal, regulators asked for lineage in risk models and most banks couldn't produce it.

## Four pillars, one catalogue

Legacy governance tools came from the 1990s warehouse era: batch, monthly reports, Excel exports, blind to model lineage. The proposed framework embeds governance from feature engineering through deployment and monitoring, on four pillars:

- **Metadata management**, a central catalogue for every data asset and model.
- **Lineage tracking**, every transformation and dependency visible end to end.
- **Quality monitoring**, automated checks for drift, anomalies and bias.
- **Cloud-native oversight**, with targets of sub-200 ms query response while tracking thousands of model updates a day.

Security is the other half: role-based access for tens of thousands of users, a full audit trail for every access, integration with enterprise identity. Vinaya flags data-lineage hijacking, tampered upstream data silently corrupting models, as the AI version of the SolarWinds supply-chain lesson. The frameworks on the checklist are GDPR, CCPA, Basel III and BCBS 239, whose demand for accurate, complete and timely risk data is close to impossible without automated lineage.

Vinaya's analogy for the framework: less a gatekeeper, more an air traffic controller for thousands of models.

## A weeks-long trace became one query

The case study is a tier-one global bank, unnamed, that adopted the framework in 2025. Vinaya reported 30% faster AI deployment, 40% stronger audit readiness and full compliance across GDPR, Basel III and BCBS standards. The anecdote that sticks: a regulator asked to trace a fraud model back to its 2019 training data, a job that used to take weeks, and the answer came from one governance query in 0.3 seconds. We only have the speaker's account of the bank, but the shape of the win, lineage as a query instead of an investigation, is the point.

## Governance first, not governance later

The rollout is foundation (cloud-native with governance built in), integration (wire ML lifecycle tools into governance pipelines), automation (continuous bias, drift and compliance monitoring), then scale. Vinaya's comparison is Netflix building observability into its cloud migration from day one.

## Who should watch

Data platform and ML engineers in financial services, risk and compliance technologists, and anyone who has watched a finished model sit in review for a quarter. Engineers outside banking will still recognise the lineage problem; regulated industries just make it louder.

## Related Conf42 talks

- [Ashish Dibouliya: Kube-Native AI Data Governance in Modern Banking](https://www.conf42.com/Kube_Native_2025_Ashish_Dibouliya_banking_compliance_governance) takes the same problem onto Kubernetes.
- [Bhanu Maryala: Automating AI Ethics](https://www.conf42.com/MLOps_2025_Bhanu_Maryala_automating_ai_ethics) builds MLOps-native data governance for generative AI.
- [Sreenivasulu Gajula: Financial Risk Governance](https://www.conf42.com/Kube_Native_2025_Sreenivasulu_Gajula_fraud_governance_finance) covers cloud-native architecture for risk and compliance.

[Watch Vinaya Nadig's talk](https://www.conf42.com/Robotics_2025_Vinaya_Nadig_governance_banking_robots)

[Watch the talk on YouTube](https://youtu.be/psG_E_D1g5I).

## Watch the talk

[Unified AI Data Governance for Scalable, Compliant Robotics in Modern Banking](https://www.conf42.com/Robotics_2025_Vinaya_Nadig_governance_banking_robots) at Conf42 Robotics 2025.
