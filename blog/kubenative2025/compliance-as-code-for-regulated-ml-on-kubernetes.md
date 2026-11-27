# Regulated ML on Kubernetes works when compliance is in the pipeline

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/compliance-as-code-for-regulated-ml-on-kubernetes

In short: Manisha Ponugoti at Conf42 Kube Native 2025 on admission controllers, GitOps audit trails and GPU scheduling for AI in healthcare, banking and insurance.

"Who approved this change?" is a question an auditor will ask, and the right answer takes seconds, not a week of archaeology. Manisha Ponugoti, who designs cloud systems that combine AI with strict regulatory needs in healthcare, banking and insurance, built her Conf42 Kube Native 2025 talk around that idea: let Kubernetes and GitOps enforce the rules, and compliance stops slowing ML down.

She frames the tension simply: AI wants speed, regulators want control. A clinical prediction has to explain itself, a fraud flag has to be explainable to regulators, and every automated insurance claim decision needs a trail of who changed what, when and why.

## Every model is a container, every change is a commit

The architecture is deliberately plain. Each model ships as a container. Kubernetes handles deployment and version upgrades, StatefulSets let models with state roll back safely, and every configuration and model change goes through Git. Manisha's example: a regulator asked for the exact deployment history of a patient-data matching model, and because of GitOps the team could show it in seconds instead of days.

The self-healing basics also count as compliance in this world. One healthcare matching service used to need engineers for hours to redeploy after a failure; on Kubernetes it recovered by itself within minutes.

## Let the cluster say no

The strongest section is about enforcement before anything runs:

- Security rules forcing containers into a safe, read-only mode.
- Network policies blocking any traffic not explicitly allowed.
- Admission controllers rejecting workloads that violate policy.
- Persistent, uneditable audit logs.

Her anecdote: a developer tried to deploy a model that had not been code-reviewed, and the admission controller blocked it automatically. Nobody had to catch it in a meeting.

The GitOps flow wraps around that: every change starts as a pull request, automated checks validate security, fairness and data rules, Kubernetes applies the approved change, and rollback is instant. In one bank, updates that used to take five hours dropped to 12 minutes with no manual steps.

## Watch, explain, and turn GPUs off

Visibility comes from a service mesh for gradual rollouts and instant rollback, model explanation tools so a doctor asking why a patient was flagged high-risk sees the reasons, and Grafana dashboards for performance and cost. On cost, Kubernetes scales GPU nodes on demand, gives critical jobs GPUs first and puts background work on cheaper preemptible servers. In one insurance project that cut compute costs by 40%.

## Three case studies, one set of patterns

The case studies carry the numbers. A global patient-record matching system handled 10 million requests a day after migration, with inference 73% faster and healthcare privacy policies enforced at deploy time. A multinational bank moved from manual, error-prone deployments to pipelines measured in minutes, with fraud detection four times faster. A large insurer used namespaces to isolate clients, autoscaling for claim traffic and built-in explanations for each AI decision.

The repeating patterns: compliance as code, immutable audit trails, safe rollouts starting new models at 5% of traffic, and full separation of training and serving. Next on her list are policy-driven runtime compliance, serverless GPUs priced per prediction, and federated learning so private data stays where it is.

## Who should watch

MLOps and platform engineers in any regulated industry, and the compliance people who keep asking them for evidence. If your audit prep currently involves screenshots, this is the talk.

## Related Conf42 talks

- [When Compliance Meets Crisis: Managing Regulatory Incidents in HIPAA, GDPR, and DMA Environments](https://www.conf42.com/Incident_Management_2025_Nisheedh_Raveendran_compliance_hipaa_gdpr) by Nisheedh Raveendran (LinkedIn), for when a rule does break.
- [Embracing change: Policy-as-code for Kubernetes with OPA and Gatekeeper](https://www.conf42.com/Cloud_Native_2021_Ara_Pulido_poilcyascode_kubernetes_opa_gatekeeper) by Ara Pulido (Datadog), the admission-controller layer up close.
- [Zero Trust MLOps: Securing AI Pipelines from Development to Production](https://www.conf42.com/MLOps_2025_Sudheer_Obbu_zero_trust_mlops) by Sudheer Obbu (JPMorgan Chase), the security side of the same pipeline.

[Watch Manisha Ponugoti's talk](https://www.conf42.com/Kube_Native_2025_Manisha_Ponugoti_microservices_regulated_scalable)

[Watch the talk on YouTube](https://youtu.be/q1sb5n1v_PU).

## Watch the talk

[Kubernetes-Native AI Microservices: Scaling Compliant ML Workloads in Regulated Industries](https://www.conf42.com/Kube_Native_2025_Manisha_Ponugoti_microservices_regulated_scalable) at Conf42 Kube Native 2025.
