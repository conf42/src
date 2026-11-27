# Shipping AI models is solved; operating them safely is the hard part

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/ai-trust-triad-rl-federated-explainable

In short: Saideepak Kandibanda (DISH Network) at Conf42 DevOps 2026 presents the AI Trust Triad, RL plus federated learning and explainable AI with DevOps guardrails.

Kubernetes, CI/CD and infrastructure as code already get models into production; the trouble starts the day after. At Conf42 DevOps 2026, Saideepak Kandibanda of DISH Network, who leads AI and automation engineers, presented what he calls the AI Trust Triad: a framework for running reinforcement learning, federated learning and explainable AI in regulated systems with the same traceability and rollback you expect from any critical software.

The examples lean towards finance and supply chains, but the pipeline advice is domain-neutral. Think of it as a checklist for what your MLOps platform should track once models start making decisions that auditors care about.

## Treat the learning process as something you deploy

Reinforcement learning gets the most operational attention. Kandibanda's examples are portfolio optimisation that reallocates assets within risk constraints, automated circuit breakers that react to volatility, and supply chain routing driven by live demand signals. In every case the policy changes as it learns, which means a static model-approval process does not fit.

His four operational requirements:

- **Policy versioning**: every reward function, exploration policy and constraint is version-controlled.
- **Safe exploration**: new policies run in shadow mode before they touch real users or assets.
- **Reward monitoring**: check continuously that learned behaviour matches business goals instead of exploiting loopholes.
- **Meta-risk detection**: watch for second-order failures such as reward hacking and emergent behaviour.

The underlying idea is that the learning process itself must be observable, governable and reversible.

## Federated learning needs a DevOps-grade pipeline too

For industries where data cannot leave its boundary (banking, telecom, healthcare, e-commerce), federated learning trains locally and shares only encrypted updates, combined through secure aggregation. Kandibanda's production requirements are model versioning with cryptographic verification of every update, secure aggregation via homomorphic encryption or secure multi-party computation, drift detection to catch local models diverging or malicious updates arriving, and performance validation so the global model behaves fairly across participants. Private is necessary; he also wants it auditable and reproducible.

## Explanations can drift, and that is a signal

The third pillar, explainable AI, serves three audiences: regulators who need transparency, engineers who need fast debugging, and customers who expect fairness. In the pipeline he wants three checks: pre-deployment checks that each model version keeps stable, interpretable feature attributions; runtime explanations stored for every live prediction; and explanation monitoring over time.

That last one is the sharpest idea in the talk. If feature importance suddenly shifts, it is an early warning of drift or data problems, often before accuracy metrics move. Your model can keep its score and quietly change its reasoning, which is exactly what an auditor will ask about.

## Governance as code, lineage as default

The wrap-up is familiar DevOps applied to models: policy as code for approval workflows and explainability thresholds, drift dashboards with automated alerts and rollbacks, and progressive rollouts (canaries, A/B tests) that validate fairness and interpretability as well as accuracy. Reproducibility means versioning every dataset, hyperparameter and code dependency, containerised deterministic training, and end-to-end lineage from data ingestion to deployment.

He closes with three hidden risks to monitor in production (reward hacking, data poisoning through federated nodes, explanation drift) and a four-step blueprint: start with pipelines, layer in drift and explainability checks, monitor meta-risks proactively, release progressively.

## Who should watch

MLOps and platform engineers in regulated industries who already have a deployment pipeline and now need to prove that a model still behaves. It is a framework talk with no code, so it pairs well with something hands-on. If explainability in your shop is a SHAP plot someone made once for a slide, the explanation-monitoring section alone is worth your time.

## Related Conf42 talks

- [Building Trust in Conversational AI: The Role of Explainable AI](https://www.conf42.com/DevSecOps_2024_Shradha_Kohli_conversational_ai_trust) by Shradha Kohli (Salesforce) applies explainability to chatbots.
- [Scaling Reinforcement Learning with Human Feedback in Distributed Cloud Systems](https://www.conf42.com/Kube_Native_2025_Jyotirmoy_Sundi_reinforcement_learning_distributed) by Jyotirmoy Sundi (Votal.ai) covers the infrastructure for RL at scale.
- [Enhancing IoT Security and Privacy with Blockchain and Federated Learning](https://www.conf42.com/Internet_of_Things_IoT_2024_Neetu_Gangwani_security_blockchain) by Neetu Gangwani (UBS) takes federated learning across clouds.

[Watch Saideepak Kandibanda's talk](https://www.conf42.com/DevOps_2026_Saideepak_Kandibanda_trust_explainability_regulation)

[Watch the talk on YouTube](https://youtu.be/PdSYFwGj2t4).

## Watch the talk

[The AI Trust Triad for DevOps: Shipping Reinforcement Learning, Federated Learning, and Explainable AI Safely in Regulated Systems](https://www.conf42.com/DevOps_2026_Saideepak_Kandibanda_trust_explainability_regulation) at Conf42 DevOps 2026.
