# AI subscriptions turn model freshness into the product you sell

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/ai-subscription-platforms-need-mlops-and-metering

In short: Chandan Kumar (Adobe) at Conf42 DevOps 2026 on the foundations of AI subscription platforms - metering, MLOps, drift monitoring and compliance.

When customers pay monthly for an AI feature, they expect it to get better every month, and that makes continuous delivery of models a commercial obligation. At Conf42 DevOps 2026, Chandan Kumar, Senior Engineering Manager at Adobe, laid out what an AI subscription platform has to stand on: the infrastructure foundations, the MLOps practices that keep models fresh, and the operational and compliance work that comes with running them at scale.

It is a strategy-level overview rather than an implementation talk, and Kumar says so in effect by moving quickly across architecture, operations, customer success and market trends. Its usefulness is as a map of the moving parts.

## Three forces that reinforce each other

Kumar's starting point is a convergence. DevOps and continuous delivery are the backbone of modern software cycles. The subscription economy raises expectations of ongoing value. And AI only stays good when it is continuously updated and retrained. Each one pushes the others, which is why companies are moving to the model.

## Four foundations, including the one people forget

He names four foundations a platform must rest on: cloud infrastructure for training and inference, model management with versioning, rollbacks, audits and experimentation, robust data pipelines, and service metering. Metering is the one engineers tend to treat as somebody else's job, but in a subscription business it underpins predictable billing and capacity planning. Without all four, he argues, the platform cannot scale sustainably.

## MLOps is DevOps with more things to version

The engineering core is MLOps as an extension of DevOps. CI has to integrate data and model artifacts as well as code. Testing goes deeper, into edge cases and adverse scenarios. Deployment is gradual, with canary rollouts and automated rollbacks.

Kumar separates two kinds of decay worth monitoring: data drift, where inputs change, and concept drift, where the real-world relationship the model learned changes. Either way, continuous observability of AI pipelines is in his words non-negotiable. Continuous learning pipelines then keep models fresh, with retraining schedules that weigh cost (training is expensive) and human feedback loops structured so they don't reinforce bias.

## Data quality, privacy and the right to be forgotten

On data, he stresses validation, anomaly detection, stream processing to catch problems in real time, and provenance tracking for traceability in regulated settings. On security he lists differential privacy, federated learning for training without moving data, and adversarial defences against input manipulation and model extraction.

The compliance section includes an item more teams should plan for: machine unlearning, removing a specific piece of data's influence from a trained model. Combined with GDPR and CCPA and audit trails, it is a reminder that "delete my data" gets harder once the data is in the weights.

## Operations, customers and the money

Operational challenges at scale are cost management, debugging across tightly coupled data, algorithms and infrastructure, capacity planning that balances training against real-time inference, and getting data scientists, ML engineers, DevOps and domain partners to share tools and language. Customer success, in his framing, means translating technical performance into business outcomes, good onboarding and usage analytics that spot friction before churn.

The abstract quotes figures of 37% higher accuracy, 31% cost reduction and 61% faster deployment; the talk itself stays with frameworks and does not walk through a case study behind those numbers.

## Who should watch

Engineering managers and platform leads planning or inheriting an AI feature sold on subscription, who want a checklist of what the platform needs beyond the model. Hands-on MLOps engineers will find most of the techniques familiar. If your team ships models but billing has never heard of your inference costs, the metering section is the one to watch.

## Related Conf42 talks

- [AI-Driven Incident Resilience: Scaling Subscription Systems](https://www.conf42.com/Incident_Management_2025_Venkata_Majeti_subscriptions_scale_uptime) by Venkata Majeti (HashiCorp) looks at keeping subscription systems up.
- [From DevOps to MLOps: Scaling Machine Learning Models](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Chinmay_Naik_devops_mlops_scaling) by Chinmay Naik (One2N) is a hands-on counterpart on serving models at scale.
- [AI Model Monitoring: Building Reliable Alert Systems](https://www.conf42.com/Chaos_Engineering_2025_Muddassar_Sharif_ai_model_systems) by Muddassar Sharif (Virtuans.ai) goes further into drift and alerting.

[Watch Chandan Kumar's talk](https://www.conf42.com/DevOps_2026_Chandan_Kumar_subscriptions_platforms_operations)

[Watch the talk on YouTube](https://youtu.be/XHvSn8rgFSI).

## Watch the talk

[AI Subscription Platforms in DevOps: Transforming Delivery Models & Operations](https://www.conf42.com/DevOps_2026_Chandan_Kumar_subscriptions_platforms_operations) at Conf42 DevOps 2026.
