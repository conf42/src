# Zero Trust compliance can't run on rules refreshed once a quarter

Conf42 Blog, 2026-02-15, updated 2026-11-09. https://www.conf42.com/blog/ml2026/zero-trust-compliance-that-learns

In short: Sudheer Kumar Aluvala (HCL America) at Conf42 Machine Learning 2026 on a closed-loop ML compliance engine that scores risk in real time inside ZTNA.

Plenty of companies have bought Zero Trust network access and then fed it hand-written policies updated on a fixed schedule. At Conf42 Machine Learning 2026, Sudheer Kumar Aluvala, Client Delivery Director for Engineering at HCL America, argued that this pairing leaves gaps between refresh cycles and proposed a machine-learning compliance engine that adjusts access decisions as risk changes.

It is a short, architecture-level talk drawn from his team's ZTNA and AI compliance work for enterprise and SMB customers. Expect a design and reported outcomes, not code.

## Three ways static policy fails

Aluvala groups the problems he keeps meeting into three. Periodic policy refreshes leave windows where threats have moved and the rules have not. Manually defined rules invite misconfigurations and inconsistencies, each a potential hole. And as the footprint spreads across hybrid and multi-cloud environments, maintaining thousands of individual and group rules stops being operationally sustainable.

None of that is surprising, which is the point: the architecture is Zero Trust, but the policy process is still on a calendar.

## A closed loop in four stages

His alternative is a loop with four repeating stages. Data ingestion gathers telemetry across the enterprise. Model training turns that into usable risk signals. Predictive enforcement makes access decisions from projected risk instead of a static rule. Automated feedback feeds every outcome back in, so the system learns from both successful interventions and false positives.

The inputs come from three places: endpoint telemetry (device health, configuration state, patch level), user behaviour analytics (access patterns and authentication history that produce a contextual risk score per person), and threat intelligence feeds with industry-specific vulnerability data. Combined, they replace point-in-time snapshots with a risk assessment that tracks current conditions, and he describes predictive analytics flagging likely compliance violations before they happen.

## What his team reports from production

From their deployments, Aluvala reports around 40% faster incident response through automated enforcement, a 98% reduction in critical policy errors with ML-generated controls, and a 60% decrease in manual effort that freed the team for other work. These are his figures from customer projects; the talk does not break down the baselines, so read them as directional.

## Automation still needs a human with a veto

The enterprise section is where the talk is most grounded. Adoption depends on explainability: clear decision rationale and complete audit trails so automated decisions still satisfy regulators. He lists bias detection to keep access decisions non-discriminatory, human oversight with the ability to review and override, and privacy-preserving analytics through anonymisation and purpose limits.

Deployment is split by size. SMEs get a lightweight setup on managed ML services for quick time to value. Large enterprises get hybrid deployments integrated with existing SIEM and SOAR platforms, which is where most of them will already have their alerts.

## Who should watch

Security architects running ZTNA who suspect their policy refresh cadence is the weak link, and ML engineers asked to build risk scoring for access decisions. If you want implementation details, use this as the map and look elsewhere for the territory.

## Related Conf42 talks

- [Zero Trust MLOps: Securing AI Pipelines from Development to Production](https://www.conf42.com/MLOps_2025_Sudheer_Obbu_zero_trust_mlops) by Sudheer Obbu (JPMorgan Chase) applies Zero Trust to the ML pipeline itself.
- [Zero Trust Security: From Perimeter Defense to Continuous Verification in the Modern Enterprise](https://www.conf42.com/Machine_Learning_2025_Vaibhav_Anil_Vora_zero_trust_security) by Vaibhav Anil Vora (AWS) covers continuous verification from first principles.
- [Automating Continuous Compliance for Scalable and Sustainable SaaS Delivery](https://www.conf42.com/DevOps_2026_Pooja_Ranjan_compliance_saas_governance) by Pooja Ranjan (Oracle America) is the DevOps view of always-on compliance.

[Watch Sudheer Kumar Aluvala's talk](https://www.conf42.com/Machine_Learning_2026_Sudheer_Kumar_Aluvala_optimization_hyperparameters_tuning)

[Watch the talk on YouTube](https://youtu.be/8pQx3Wqj4cs).

## Watch the talk

[Machine Learning–Driven Compliance Engines for Zero Trust Security](https://www.conf42.com/Machine_Learning_2026_Sudheer_Kumar_Aluvala_optimization_hyperparameters_tuning) at Conf42 Machine Learning 2026.
