# Zero trust for ML pipelines, stage by stage

Conf42 Blog, 2025-09-17, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/zero-trust-mlops-four-pipeline-stages

In short: Sudheer Obbu of JPMorgan Chase at Conf42 MLOps 2025 on applying never-trust-always-verify to data, training, serving and monitoring in MLOps.

An ML pipeline has more ways in than a web app: the training data, the model artifact, the training infrastructure and the live inference endpoint are all targets. At Conf42 MLOps 2025, Sudheer Obbu, Senior Lead Software Engineer at JPMorgan Chase and a DevSecOps and multi-cloud architect with 19 years in the field, argued that traditional DevSecOps misses those threats and showed how to apply zero trust at each of four stages of the ML lifecycle.

The talk is a framework with a practical tool list at the end. The 73% reduction in security incidents he cites is his headline result for organisations adopting the approach; the reusable part is the stage-by-stage control set.

## The threats that DevSecOps doesn't cover

Sudheer singled out three ML-specific threats and ranked them by risk. Data poisoning sits highest: feed a fraud model bad data and it becomes a fraud enabler. Inference attacks come next, manipulating a live model for desired outputs or extracting confidential training data. Model theft goes straight at the proprietary asset. None of these is fixed by scanning your code, which is why the attack surface needs its own strategy.

## Data and training: lineage, sandboxes, signatures

Zero trust here means never trusting by default, even inside your network, and verifying every request to read data or deploy a model. For data ingestion he described a security pyramid: strict identity and access management for data sources at the base, encryption in transit and at rest in the middle, and data lineage with checksums at the top so you can prove nothing was tampered with on the way in. Garbage in, garbage out turns into something nastier when the garbage was planted.

Training jobs run in isolated sandbox containers with locked-down network access and scanned dependencies. Training scripts get least privilege: read access to the data they need, write access to one artifact location. Every trained model is digitally signed, versioned and stored in an audited registry with its own access controls.

## Serving and monitoring: hardened endpoints, assumed breach

At serving time, models run on hardened minimal container images behind network policies, every inference request is authenticated and authorised, and rate limiting and input validation are standard. Secrets go into a dedicated manager such as HashiCorp Vault or AWS Secrets Manager, never into code. Monitoring then assumes breach: log every request, response and access event, watch for anomalies such as performance drift and data skew that may signal a subtle attack, and trigger automated responses like revoking access and alerting the security team.

His two case studies make it concrete. A fintech that enforced strict IAM and signed all model artifacts cleared its major audit findings on data access and spent 40% less time on manual compliance reporting. A healthcare platform used isolated model environments with token-based API authentication to reach HIPAA compliance on diagnostic models.

## The pitfalls are mostly human

The closing advice is sharp. Too much friction and data scientists will build insecure shadow IT, so automate security into CI/CD and ship secure-by-default project templates. Zero trust is continuous: review logs, rotate credentials, run security drills. And treat models differently from code: a signed container doesn't stop a model being stolen or poisoned, so sign the artifact itself and monitor for drift.

The toolbox he listed: Okta, Azure Active Directory and cloud secret managers for identity; Snyk, Trivy and Dependabot for code and containers; Istio or Linkerd for service-mesh encryption and policy, with Falco for runtime threats; and DVC, MLflow or ClearML for data lineage and model registries. The four-step start: map your pipeline and its access controls, give every user and service a unique identity with MFA, enforce least privilege with just-in-time access, and monitor continuously.

## Who should watch

Platform and security engineers responsible for ML infrastructure in regulated industries, and MLOps teams whose security review consists of a container scan. If you already run a service mesh and signed artifacts, the threat model section is the new part.

## Related Conf42 talks

- Anmol Agarwal (Nokia) with [A Beginner's Guide to Adversarial Machine Learning](https://www.conf42.com/Machine_Learning_2024_Anmol_Agarwal_beginners_guide_adversarial).
- Roshan Piyush (Harness) on [Rethinking Supply Chain Security in the Age of Agentic AI](https://www.conf42.com/DevSecOps_2026_Roshan_Piyush_supply_chain_security).
- Vaibhav Anil Vora (AWS) on [Zero Trust Security: From Perimeter Defense to Continuous Verification](https://www.conf42.com/Machine_Learning_2025_Vaibhav_Anil_Vora_zero_trust_security).

[Watch Sudheer Obbu's talk](https://www.conf42.com/MLOps_2025_Sudheer_Obbu_zero_trust_mlops)

[Watch the talk on YouTube](https://youtu.be/Ss3CcoULpgQ).

## Watch the talk

[Zero Trust MLOps: Securing AI Pipelines from Development to Production](https://www.conf42.com/MLOps_2025_Sudheer_Obbu_zero_trust_mlops) at Conf42 MLOps 2025.
