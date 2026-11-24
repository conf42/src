# QA for health insurance should watch the claim, not just test it

Conf42 Blog, 2025-05-26, updated 2026-11-09. https://www.conf42.com/blog/obs2025/health-insurance-qa-observability-claims

In short: Subash Lekshmi Velayudhan at Conf42 Observability 2025 on moving health insurance QA from testing to observing claims, portals and compliance.

A parent logs into a member portal to check coverage for their child's surgery, and the portal crashes. At Conf42 Observability 2025, Subash Lekshmi Velayudhan, a quality engineer with 22 years in health plan systems, used that scene to argue that QA in health insurance has to move from testing before release to observing what members and claims go through in production.

His phrase for the goal is a shift "from defect detection to experience protection", and the talk is a roadmap for getting there.

## Why testing alone falls short

Subash's view is that traditional QA does not keep up with fast-moving, heavily regulated healthcare platforms. Test suites catch defects before release; they do not tell you that open enrolment just made the portal crawl or that one microservice in the claims path is failing. He compares mean time to resolve with and without observability tooling, and frames observability as a survival tool rather than a luxury.

## Metrics, logs and traces, in claims language

The best part is how he maps the three signals onto the domain:

- **Metrics:** claims processing by complexity, prior authorisation approval rates, member portal latency during open enrolment.
- **Logs:** the story behind events, including which protected health data was accessed and why a provider lookup failed. They are the audit trail too.
- **Traces:** a claim's journey through 20 or more microservices, checking eligibility, provider validity, pricing, applied benefits, authorisation and status.

That last one is the case for tracing in insurance in one sentence: claims hop across APIs, third-party systems and legacy bridges, and without traces nobody can say which hop stalled.

## Observability as legal armour

Subash pushes the compliance angle further than most talks do. Observability lets you show who accessed protected health information and when, trace every step of a claim, and preserve evidence automatically during a regulatory investigation. It proves you are doing the right things, not only fixing them fast. He points out that QA teams often miss this part.

He also lists domain KPIs worth wiring into dashboards: auto-adjudication rate, first-pass resolution, average processing time and error rate by claim type for claims; portal availability, authentication success and provider search accuracy for members; and query and API response times, resource use and batch completion for the platform.

## A case study and the hard parts

He walks through a case study at a large US health insurer, where portal outages and claim delays were addressed with distributed tracing across more than 200 services and real-time dashboards on the claims pipelines, cutting time to resolution and processing time.

The challenges section is candid: protected health data must stay protected inside the telemetry, storing logs and traces costs money and needs retention policies, legacy systems were not built to be observed, and teams need training. His advice is to pace yourself: pilot one critical service such as claims, eligibility or the member portal, prove value, then scale. QA, operations, security and product all have to own it together.

## Who should watch

QA leads and test architects in healthcare or any regulated domain who want to make the case for observability inside the QA function. It is a strategy talk, light on tooling, heavy on the domain.

## Related Conf42 talks

- [Gurucharann Visagamurthy on real-time insurance underwriting and enrolment on Kubernetes](https://www.conf42.com/Kube_Native_2025_Gurucharann_Visagamurthy_insurance_enrollment_realtime) (Kube Native 2025).
- [Pravesh Nikhare on rule-based AI for dental insurance claims](https://www.conf42.com/Cloud_Native_2025_Pravesh_Nikhare_insurance_rules_processing) (Cloud Native 2025), for the claims logic you would be tracing.
- [Fred Moyer on SLOs and error budgets at scale](https://www.conf42.com/Observability_2023_Fred_Moyer_slos_error_budgets_scale) (Observability 2023), for turning those KPIs into targets.

[Watch Subash Lekshmi Velayudhan's talk](https://www.conf42.com/Observability_2025_Subash_Lekshmi_Velayudhan_insurance_platforms_quality)

[Watch the talk on YouTube](https://youtu.be/Ul6aKdHKwKI).

## Watch the talk

[Observability-Driven Quality Assurance for Health Insurance Platforms](https://www.conf42.com/Observability_2025_Subash_Lekshmi_Velayudhan_insurance_platforms_quality) at Conf42 Observability 2025.
