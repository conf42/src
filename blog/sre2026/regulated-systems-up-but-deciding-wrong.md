# Regulated systems can be up and still make the wrong decisions

Conf42 Blog, 2026-03-14, updated 2026-11-09. https://www.conf42.com/blog/sre2026/regulated-systems-up-but-deciding-wrong

In short: Shruthi Sepuri of TCS at Conf42 SRE 2026 on workflow-level reliability for insurance and finance - decision accuracy SLIs and testing that continues in production.

A rule configuration change can quietly move an approval threshold and leave every dashboard green. At Conf42 Site Reliability Engineering 2026, Shruthi Sepuri, Software Developer Engineer at TATA Consultancy Services, showed how that kind of silent workflow failure slips past infrastructure monitoring in regulated systems, and how to extend testing into production so you catch wrong decisions, not just slow ones.

Her one-line summary is the talk in miniature: "A system can be up and still be wrong."

## The factory machine that hums while making bad parts

She opens with an analogy: a factory machine that runs perfectly, nothing overheating, panel all normal, while the parts coming out are wrong. Her first slide puts that into software. On the left, the view on-call engineers are used to: four nines of uptime, tiny error rate, low latency, CPU and memory comfortable. On the right, the business workflow: ingestion passes, the rule engine errors, the decision output is wrong, compliance validation is skipped and the audit log has a gap. The footnote says it all: a rule misconfiguration, and no infrastructure alert triggered.

Uptime, error rates and latency measure technical health. None of them measure decision correctness, and in insurance or financial services, a wrong approval at scale is a compliance event, not a minor defect.

## There is a missing layer in most monitoring stacks

She breaks systems into layers. Infrastructure and application services (servers, databases, APIs, queues, caches) are usually monitored well. The business workflow layer (claims processing, underwriting, policy adjustments, compliance validation, audit logging) is under-monitored. The compliance outcomes layer (correct decisions, audit trails, risk controls) is often not measured at all.

Her worked example is a claims system where a config change silently alters approval thresholds. Infrastructure stays green throughout, decisions drift, incorrect approvals or rejections go through at scale, and the audit trail may be incomplete. The listed causes are all mundane: rule misconfigurations, data mapping issues, threshold drift, missing compliance attributes. None of them crash anything.

## Four indicators for decision correctness

Reliability has to be defined at the workflow level, with a check at each step: is the input validated, are the right rules in use, is the outcome in the expected range, are required fields complete, is the audit record immutable and complete. From those come four indicators:

- **Decision accuracy rate**: share of automated decisions within the expected outcome range.
- **Approval and rejection deviation**: statistical drift from the historical baseline, so a sudden spike or drop becomes a signal.
- **Compliance field completion**: required audit attributes populated per transaction.
- **Rule execution correctness**: rules behaving as configured, checked against known test cases.

## Testing does not stop at the release

The bridge to QA is the part testers will appreciate. Testing feeds deployment, deployment feeds monitoring, incidents feed learning, and learning feeds better tests. Her four methods: synthetic business transactions replayed continuously against live rule engines, real-time monitoring of decision outcomes and rule execution, comparing rule engine output against expected baselines after every deployment, and alerting on statistical anomalies in outcomes rather than only on technical errors. Production decision distributions then flow back to update test cases and thresholds before the next rule change ships.

Her formula for it is testing plus observability equals workflow reliability. Neither half is enough alone.

## Who should watch

QA engineers moving toward reliability work, and SREs on rule-heavy platforms in insurance, banking or anywhere a config file can change an outcome. It is an accessible, framework-level talk with illustrative dashboards; bring your own rule engine and you will leave with a short list of SLIs to add.

## Related Conf42 talks

- [Building ML-Based Compliance Monitoring for Automated Risk Detection](https://www.conf42.com/DevSecOps_2026_Vinay_Puri_ml_compliance_monitoring) by Vinay Puri.
- [Turning Synthetic Traces into Gold: Scalable Monitoring for Critical User Journeys](https://www.conf42.com/Observability_2025_Sudeep_Kumar_traces_user_synthetic) by Sudeep Kumar, a close cousin of synthetic business transactions.
- [Kubernetes-Native AI Microservices: Scaling Compliant ML Workloads in Regulated Industries](https://www.conf42.com/Kube_Native_2025_Manisha_Ponugoti_microservices_regulated_scalable) by Manisha Ponugoti.

[Watch Shruthi Sepuri's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Shruthi_Sepuri_testing_reliability_strengthening) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/AlsOfI1yxzQ).

## Watch the talk

[From Testing to Reliability: Strengthening Regulated Production Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Shruthi_Sepuri_testing_reliability_strengthening) at Conf42 Site Reliability Engineering (SRE) 2026.
