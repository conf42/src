# Data science stalls on infrastructure, not algorithms

Conf42 Blog, 2025-08-05, updated 2026-11-09. https://www.conf42.com/blog/platform2025/platform-engineering-data-science-ml-pipelines

In short: Aishwarya Pai of Deloitte at Conf42 Platform Engineering 2025 on the platform principles and patterns that get ML models from notebooks to production.

Your model works in the notebook and dies on the way to production, and the culprit is rarely the model. At Conf42 Platform Engineering 2025, Aishwarya Pai, Senior Consultant at Deloitte, made the case that the bottleneck in enterprise data science is infrastructure, and that platform engineering is the fix: one standard, self-service foundation so data scientists stop firefighting environments.

The abstract leads with numbers: 58% of ML platforms failing to deliver value, and platform engineering bringing 68% faster model delivery and 37% higher AI success rates. The talk itself is a compact, well-ordered overview rather than a single case study, so treat it as a checklist for an ML platform, not a war story.

## Three failure modes before the first model ships

Aishwarya names the usual suspects. Fragmented tooling, where every team picks its own stack and integration becomes the project. Inconsistent environments, the "works on my machine" problem in ML clothing, where a model behaves differently in production than in development. And deployment bottlenecks, where data scientists build models that engineering teams then struggle to operationalise. She adds resource inefficiency (too much compute idling, or not enough when it matters) and patchwork security that makes compliance a scramble.

## Six principles for the platform

Her answer is a short list of platform principles: abstraction, so data scientists never see the messy infrastructure; self-service, so teams provision environments and deploy models without a ticket; standardisation of patterns and tools; observability across models, data and infrastructure; scalability that follows demand; and security by design rather than as an afterthought.

The foundation underneath is containerisation, which gives consistent runtimes and lets several versions of a model run side by side. On top sit microservices for data integration, training and monitoring, each scaled independently, with orchestration and a service mesh tying them together.

## The patterns that make it boring, in a good way

The section on design patterns is the most useful for engineers. Twelve-factor apps for maintainability. Event-driven architecture, so new data arriving can trigger training automatically. Immutable infrastructure, where every change is a new version and rollbacks are cheap. Circuit breakers and bulkheads to keep one failing workload from taking down the rest. Autoscaling to follow demand and save money.

She describes ML pipelines as the assembly line of data science and lists what a good one needs: orchestration of dependencies and schedules, data lineage and versioning for reproducibility, and fault tolerance so a failed step recovers instead of restarting the world.

## Five audiences, one platform

The part that platform teams often skip: a data science platform serves at least five groups with different needs. Data scientists want fast experiments and easy data access. ML engineers want reliable deployment and monitoring. Platform engineers want visibility into cost, performance and compliance. Security wants control without slowing everyone down. Business stakeholders want results they can measure. Monitoring, she argues, has to cover all four layers: infrastructure, application latency and errors, data freshness and schema quality, and model accuracy and drift.

She closes with expected payoffs (tripled productivity, deployment time cut in half, infrastructure costs down 40%) and a five-step roadmap from assessment through foundation, platform development and operational excellence to continuous evolution. Those are her framing figures, not a single measured case, so read them as targets.

## Who should watch

Platform engineers who have inherited the data science team as customers, and data leads arguing for a shared ML platform instead of one more bespoke pipeline. If you already run a mature MLOps stack, most of this will be familiar; it is an orientation talk, and a tidy one.

## Related Conf42 talks

- [Tomas Fernandez on MLOps from Jupyter to production](https://www.conf42.com/Machine_Learning_2024_Tomas_Fernandez_mlops_jupyter_production) at Conf42 Machine Learning 2024.
- [Chinmay Naik on scaling from DevOps to MLOps at 2 million+ requests per day](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Chinmay_Naik_devops_mlops_scaling) at Conf42 SRE 2024.

[Watch Aishwarya Pai's talk](https://www.conf42.com/Platform_Engineering_2025_Aishwarya_Pai_unlocks_agile_science), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/FxYK-WnFGOA).

## Watch the talk

[Platform Engineering for Data Science at Scale: How Agile Infrastructure Unlocks 68% Faster ML Pipeline Delivery](https://www.conf42.com/Platform_Engineering_2025_Aishwarya_Pai_unlocks_agile_science) at Conf42 Platform Engineering 2025.
