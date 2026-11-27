# Put cost signals in the same engine as your alerts

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/aiops-finops-one-observability-platform

In short: Ganeshkumar Palanisamy of Reltio at Conf42 Observability 2025 on merging AIOps and FinOps into one observability platform for multi-cloud data systems.

Most teams keep the cloud bill in one tool and the pager in another, then wonder why nobody can say which feature made last month expensive. At Conf42 Observability 2025, Ganeshkumar Palanisamy, principal software architect at Reltio, argued for one correlation engine that sees tenant, platform, subsystem, cloud and cost signals together, so AIOps and FinOps stop being separate projects.

## No, you cannot just buy it

Ganeshkumar opens with the multi-cloud bargain: cherry-pick the best of AWS, GCP and Azure, avoid lock-in, and in exchange get fragmented tools, inconsistent metrics and siloed teams. He asks the question every budget holder asks, whether there is a single tool that fixes this, and answers it straight away: no. Observability at this scale is an engine you build, starting with a unified platform that collects metrics, logs and traces consistently across providers and a documented inventory of every cloud resource it covers.

## Smart alerts carry context

The most practical section is on alerting. His example: a latency alert that fires when latency rises 20%. On its own it produces a stream of false positives, because latency also rises while the system is autoscaling, during unusual but legitimate customer load, or while a subsystem hiccups and recovers on its own. Add that context to the rule and the alert fires only when something is going on beyond auto-recovery. Fewer pages, and the ones that remain mean something.

From there the talk stacks three more capabilities:

- **Anomaly detection** that keeps up as new customers bring new usage patterns.
- **Predictive analytics**: at Reltio, data is aggregated every five minutes, and with enough history a model predicts the next five minutes, so you can scale ahead of demand or warn a human when automation cannot fix it.
- **A correlation engine** across multi-tenant signals: per tenant, per platform, per subsystem, per cloud, and then cost.

## FinOps as another signal type

The FinOps half is about joining cost to usage. Once cost data sits next to the operational data, you can see which kind of usage drives which cost, budget from usage and cost trends together, right-size intelligently and attribute spend to the business that caused it. Ganeshkumar reports a 28 to 37% reduction in cloud spend through resource placement and right-sizing, and a 43% drop in underutilised instances. On the operations side he cites incidents detected 67% faster, resolution 51% faster, and teams managing 3.4 times more infrastructure without extra staff.

## Tags are a design decision

The best practices include one worth underlining: standardised tagging across all clouds. His point is that the number of tags matters less than the value each one carries and how consistently it is managed, so everyone can tell what an application is and what it is for. He also wants observability as code, deployed alongside the infrastructure, and part of the design from the first day rather than added after launch.

## Start with the current state, not the ideal one

The action plan is refreshingly unglamorous. Assess what you already have, because most systems already have some observability. Document the tools in use and the baseline you need. Define a target architecture for your own workloads; he explicitly declines to hand out a blueprint because every system differs. Then pick the highest-impact workload first, prove the savings and the scaling gains there, and use that win to fund the next step.

## Who should watch

Platform and data-platform engineers in multi-cloud, multi-tenant setups, and anyone trying to get engineering and finance to read the same dashboard. The talk is strategy with a few concrete examples rather than a tool demo; the alerting and five-minute prediction sections are the parts you can apply next week.

## Related Conf42 talks

- [Manoj Kalakoti on autonomous FinOps and cost governance for financial services](https://www.conf42.com/Kube_Native_2025_Manoj_Kalakoti_finops_costgovernance_autonomous) at Conf42 Kube Native 2025.
- [Prathamesh Sonpatki on the hidden cost of instrumentation](https://www.conf42.com/DevOps_2023_Prathamesh_Sonpatki_cost_instrumentation), the other side of the observability bill, at Conf42 DevOps 2023.
- [Raghu Bhupatiraju on predictive observability for supply chain outages](https://www.conf42.com/DevOps_2026_Raghu_Bhupatiraju_predictive_analytics_outages) at Conf42 DevOps 2026.

[Watch Ganeshkumar Palanisamy's talk](https://www.conf42.com/Observability_2025_Ganeshkumar_Palanisamy_platforms_scale_finops)

[Watch the talk on YouTube](https://youtu.be/y4j1xTwSvNo).

## Watch the talk

[Observability at Scale: Optimizing Multi-Cloud Data Platforms with AI Ops and FinOps](https://www.conf42.com/Observability_2025_Ganeshkumar_Palanisamy_platforms_scale_finops) at Conf42 Observability 2025.
