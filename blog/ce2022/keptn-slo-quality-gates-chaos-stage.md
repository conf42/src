# Chaos experiments become a release gate when SLOs decide the result

Conf42 Blog, 2022-03-11. https://www.conf42.com/blog/ce2022/keptn-slo-quality-gates-chaos-stage

In short: Ana Margarita Medina (Gremlin) at Conf42 Chaos Engineering 2022 on continuous reliability with Keptn, SLO quality gates and a chaos stage before production

Run a chaos experiment in a pipeline and someone has to decide whether the result is good enough to ship. At Conf42 Chaos Engineering 2022, Ana Margarita Medina, Senior Chaos Engineer at Gremlin and a Keptn advisory board member, argued that nobody should have to: define SLOs as code, let the CNCF project Keptn evaluate them as quality gates at every stage, and the experiment's verdict becomes a pass or a fail.

Her recipe for continuous reliability is three words: automation, standardisation and experimentation.

## What problem is this solving?

Complexity outran the tooling. Ana traces the path from one on-premises service and an annual release to hundreds or thousands of microservices, cloud regions you cannot name, and daily (sometimes Friday) deploys. Failures got more complex with them, and SREs still spend nights hunting dashboards and running runbooks and shell scripts by hand. The talk shows a this-is-fine stick figure for a reason.

## What does Keptn do here?

Keptn, a CNCF sandbox project, is a control plane for DevOps automation of cloud-native applications, declarative and GitOps-based, and not limited to Kubernetes. Out of the box it brings observability, dashboards and SLO-based alerting per service, multi-stage delivery, and operations and remediation under one roof.

The anchor is SLOs. Ana's slide example: the SLI is web request latency under 500 ms; the SLO is 95% of requests under 500 ms over a rolling month; the SLA is 90% under 500 ms for the month, or the customer gets money back. Keptn standardises SLOs across tools and stages, and they live in YAML files (an sli.yaml and an slo.yaml) with pass and warning criteria and an overall score. She calls the result test-driven operations: developers see how their change moves the reliability metric before it reaches customers. She credits Keptn contributor Andreas Grabner for much of the SLO material.

## What did the demo show?

Following the Keptn full tour tutorial with Dynatrace (Prometheus also works), she installs Keptn for the continuous delivery use case, onboards a sock shop project with three stages (development, staging, production), and deploys a carts service with its database. Version one goes green all the way to production.

Version two fails the gate in staging: the 95th percentile response time comes in at 1,052 ms, the evaluation fails, and the release is not promoted, so production stays on version one. Version three fixes the response time and rolls through dev, staging and production. When a production SLO is breached, Keptn can also run a declared remediation action, such as toggling a feature flag, re-evaluate the SLO, and close the issue if it passes.

## Where do chaos experiments fit?

Ana offers three placements:

- **Every stage**: run experiments in dev and staging before anything reaches production.
- **A dedicated chaos stage**: development, staging, then chaos as the last quality gate before production.
- **Alongside performance testing**: she describes doing load tests and chaos engineering together at Uber to prepare for peak days such as Halloween and New Year's, when a trip depends on about 50 microservices.

The decision logic is simple. SLO met: promote. SLO not met: did we find a weakness? Fix, release again, repeat. Nobody needs to argue in a meeting about whether the experiment result is acceptable for customers, because the SLO already says so.

## The part that is not about a tool

Her closing is the most quotable bit. Ana said at Conf42 Chaos Engineering 2022: "You can't bring in just a new tool that's going to promise you more nines of reliability. Those don't exist." Reliability comes from processes you automate and keep running: experiments, SLOs, game days, failovers, and runbooks exercised often enough not to rot.

## Who should watch

SREs and platform teams who already run some chaos experiments and want them wired into delivery with an objective pass/fail, and anyone who needs a crisp SLI/SLO/SLA explainer for their team.

## Related Conf42 talks

- Uma Mukkara on [continuous SLO validation using chaos engineering](https://www.conf42.com/Site_Reliability_Engineering_2021_Uma_Mukkara_continuous_SLO_validation_using_chaos_engineering) at Conf42 SRE 2021.
- Akram Riahi on [chaos engineering with Litmus and Jenkins](https://www.conf42.com/Chaos_Engineering_2022_Akram_Riahi_chaos_engineering_alongside_litmus_and_jenkins) at Conf42 Chaos Engineering 2022.
- Fred Moyer on [SLOs and error budgets at scale](https://www.conf42.com/Observability_2023_Fred_Moyer_slos_error_budgets_scale) at Conf42 Observability 2023.

[Watch Ana Margarita Medina's talk](https://www.conf42.com/Chaos_Engineering_2022_Ana_Margarita_Medina_continuous_reliability)

## From Gremlin

Ana closes by pointing to Gremlin's chaos engineering certification, offered at two levels: Practitioner, covering chaos engineering fundamentals, and Professional, for advanced chaos engineering.

- Gremlin: [gremlin.com](https://www.gremlin.com)
- Gremlin certification: [gremlin.com/certification](https://www.gremlin.com/certification)

[Watch the talk on YouTube](https://youtu.be/5NJk7wc5WII).

## Watch the talk

[Continuous Reliability. How?](https://www.conf42.com/Chaos_Engineering_2022_Ana_Margarita_Medina_continuous_reliability) at Conf42 Chaos Engineering 2022.
