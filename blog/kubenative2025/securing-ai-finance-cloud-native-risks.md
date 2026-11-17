# The quiet attacks on AI in finance hide in cloud-native gaps

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/securing-ai-finance-cloud-native-risks

In short: Manisha Sengupta (Brown Brothers Harriman) at Conf42 Kube Native 2025 on adversarial attacks, data poisoning and Kubernetes misconfigurations in AI-driven finance.

The most dangerous attack on a financial AI system may be the one that looks like normal traffic. At Conf42 Kube Native 2025, Manisha Sengupta, Assistant Vice President for systems in Investor Services Technology at Brown Brothers Harriman, mapped how AI models for fraud, credit scoring and trading pick up new attack surfaces when they move to containers, microservices and public APIs, and what a layered defence looks like.

She opened with a story about a smart home app whose cloud-hosted AI detected unusual activity in the house. One leaked API key later, an attacker was querying the model to learn when the home was empty. Her takeaway: the real threat is often the quiet pattern nobody watches, not the big obvious hack.

## Four ways to break a model without breaking in

Sengupta grouped the AI-specific threats into four. Adversarial attacks craft inputs that look legitimate to humans but fool the model, for example transactions a fraud detector scores as safe, and black-box versions now work with very little insider knowledge. Data poisoning slips malicious records into training data, so a credit model can quietly discriminate against a group while still looking accurate. Model extraction and inversion reverse engineer a model from its outputs, leaking things like customer spending habits or proprietary trading logic, and offering models through APIs widens that surface.

The fourth is the platform itself. Misconfigured RBAC hands out privileges, public container images ship with vulnerabilities, weak network policies allow lateral movement, and short-lived containers are hard to monitor and audit.

## How a fraud system gets walked around

Her attack scenario chains those together: compromise a developer account, use weak network policies to reach the transaction data pipeline, corrupt it, and push real fraudulent transactions past detection without an alarm. For trading systems, adversaries study algorithm outputs to reverse engineer the logic and front-run the institution's own trades. In a distributed system, each step looks like ordinary activity.

## People are part of the attack surface

She gave the human factor equal weight. Data scientists optimise for accuracy and may use unvalidated public datasets or skip sanitisation. Developers grant broad permissions in shared environments and pull vulnerable open source libraries. DevOps teams under deadline pressure cut corners. And there is a global shortage of people who know both AI and security.

## Defence in depth, with explanations

Her resilience model has four pillars: zero trust across the AI pipeline, model governance with versioning and security checks, data security with integrity and lineage tracking, and infrastructure security with defence in depth tailored to AI. Explainable AI helps analysts understand why something was flagged, speeds up investigations and cuts false positives, though she warned it must be balanced against what explanations reveal.

The most practical idea is cross-layer anomaly correlation. A network spike alone is a glitch; a network spike plus model drift plus a data shift is probably an attack. Governance closes the loop with clear ownership across the model lifecycle, continuous audit, incident playbooks that cover AI events, and bias and fairness testing.

## Who should watch

Security engineers and platform teams at banks, asset managers and fintechs who run models in Kubernetes, and ML engineers who have never threat-modelled their own training pipeline. It is a risk-mapping talk without tooling demos, best paired with something hands-on.

## Related Conf42 talks

- [A Beginner's Guide to Adversarial Machine Learning](https://www.conf42.com/Machine_Learning_2024_Anmol_Agarwal_beginners_guide_adversarial) by Anmol Agarwal (Nokia) explains the attacks in more detail.
- [AI-Powered Fraud Detection in Cloud-Native Digital Payments](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security) by Sandeep Katuri shows the defender's side of payments.
- [Transforming Cybersecurity Governance with GenAI](https://www.conf42.com/Platform_Engineering_2024_Akshay_Sekar_Chandrasekaran_cybersecurity_governance_genai) by Akshay Sekar Chandrasekaran (Intuit) covers governance for risk and compliance.

[Watch Manisha Sengupta's talk](https://www.conf42.com/Kube_Native_2025_Manisha_Sengupta_finance_risks_modernization)

[Watch the talk on YouTube](https://youtu.be/QH7uUDXcmyk).

## Watch the talk

[Securing AI-Driven Finance: Navigating Risks in Cloud-Native Modernization](https://www.conf42.com/Kube_Native_2025_Manisha_Sengupta_finance_risks_modernization) at Conf42 Kube Native 2025.
