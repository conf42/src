# ML is now running the compliance gates in SaaS delivery

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/ml-runs-compliance-gates-in-saas-delivery

In short: Pooja Ranjan of Oracle at Conf42 Machine Learning 2026 on how ML automates compliance checks, monitoring and right-sizing across a cloud delivery pipeline.

Compliance used to be the step where a release waited for someone to tick boxes. At Conf42 Machine Learning 2026, Pooja Ranjan, Engineering Manager at Oracle Cloud, walked through a SaaS delivery pipeline from feature request to production and showed where machine learning now runs those checks automatically, from code coverage gates to latency alarms that fire before an SLA is breached.

It is a broad, experience-led tour rather than a single system deep-dive. Pooja has spent over a decade on SaaS platforms, including early engineering on GoToMeeting, and now leads a mixed team of software and ML engineers building tools for data scientists on Oracle Cloud.

## The boring part of ML engineering is the expensive part

Her opening example is IT support. Access issues and permission problems used to mean waiting for a person, sometimes on site. Internal assistants now find the right document, identify the missing user group, and even set a reminder to renew expiring permissions. Her last three such tickets were resolved by the bot. The point is that ML pays off first on logistics, freeing data scientists to work on data instead of access requests.

## Compliance at every stage of delivery

The core of the talk follows a feature from request to production:

- **Design.** New architecture is checked against standard networking patterns, and release-management tools run compliance and security checks on every new design, including whether it introduces API, UI or infrastructure-as-code changes.
- **Development.** Engineers use code assistants to understand, refactor and test code. Pull requests still need human review before ML-driven compliance checks take over; she was clear it is not fully touchless.
- **CI gates.** Tools integrated into the CI/CD stack enforce code coverage (drop below the bar and the merge is blocked until tests are added) and run dynamic security tests that simulate cross-site scripting and denial-of-service attempts on every PR.
- **Deployment.** The pipeline is touchless from there: artifacts roll out through Terraform to a production-like environment, then a small low-traffic region, then the popular regions.
- **Verification.** Regulatory checks run alongside, from SOX-style acceptance standards to accessibility requirements for users of screen readers.

## Alarm at 300 when the SLA says 500

Her monitoring example is the clearest takeaway. If the SLA says a notebook launch must complete within 500 milliseconds, and the system normally answers in 200 to 250, alarms start at 300, well before the breach. ML then helps triage: hardware fault, scheduling, a data centre down, overload, or a noisy neighbour at the tenancy level.

She closed on sustainability: ML-based tools watch utilisation of every instance and automatically right-size ones that stay underused, after load and performance tests confirm quality does not degrade, cutting both cost and the energy and water bill for cooling.

## Who should watch

Engineering managers and platform teams in regulated SaaS who want a map of where automated compliance fits in the delivery pipeline. Expect breadth over depth; there is no single model or metric to take away.

## Related Conf42 talks

- [Automating Continuous Compliance for Scalable and Sustainable SaaS Delivery](https://www.conf42.com/DevOps_2026_Pooja_Ranjan_compliance_saas_governance), Pooja Ranjan's companion talk from Conf42 DevOps 2026.
- [Compliance As Code with Cloud Custodian](https://www.conf42.com/DevSecOps_2021_Ismael_Hommani_Tanguy_Combe_compliance_as_code_cloud_custodian) by Ismael Hommani and Tanguy Combe, for policy-as-code tooling.
- [Keep Calm and Run on AWS: Engineering Compliance Without Abandoning Your Stack](https://www.conf42.com/Cloud_Native_2026_Dmytro_Hlotenko_distributed_systems_resilience) by Dmytro Hlotenko.

[Watch Pooja Ranjan's talk](https://www.conf42.com/Machine_Learning_2026_Pooja_Ranjan_finetuning_foundation_models) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/fCJIA2VX6P0).

## Watch the talk

[Stop Failures Before They Happen: Gradient Boosting for Perfect Flows](https://www.conf42.com/Machine_Learning_2026_Pooja_Ranjan_finetuning_foundation_models) at Conf42 Machine Learning 2026.
