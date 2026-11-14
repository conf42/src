# Your recommendation model should never be able to slow checkout

Conf42 Blog, 2026-02-21, updated 2026-11-09. https://www.conf42.com/blog/sre2026/keep-ai-workloads-away-from-checkout

In short: Ajay Srinivas Kiran Gemidi of Valuguard Solutions at Conf42 SRE 2026 on isolation, execution limits and lineage for AI analytics in critical platforms.

In one production environment, a recommendation service took 40% of the shared compute during peak traffic and checkout got slower. The model was accurate; the architecture had no resource limits. That story sits at the centre of Ajay Srinivas Kiran Gemidi's talk at Conf42 Site Reliability Engineering 2026, where the Sr Systems Engineer at Valuguard Solutions argues that AI analytics inside production platforms is a reliability problem first and a modelling problem second.

Gemidi brings 20 years across systems engineering, DevOps and enterprise data platforms, and the talk reads like it: four architectural guardrails, each with the mechanisms that enforce it.

## Why AI workloads show up in postmortems

Analytics used to run overnight, safely away from the transactional path. Now models power fraud detection, recommendations and real-time analytics inside the platform. Three things make that awkward. Inference compute demand is bursty, with feature extraction, pre-processing and model execution all competing for the same resources. Execution is opaque, so you cannot simply read the code path when the output looks wrong. And data dependencies sprawl across feature pipelines and upstream services.

In incident reviews this surfaces as three recurring patterns: latency amplification when inference competes for compute, cascading failures when a slow inference service pushes delay and load upstream, and observability gaps because CPU, memory and request latency say nothing about prediction confidence or feature drift.

## Guardrail one: isolation

Analytical workloads should not compete with transactional ones for compute. The fixes are familiar container-platform tools used on purpose: dedicated compute pools for inference, namespace resource quotas, separate execution queues, network segmentation to shrink the blast radius, and priority-aware scheduling so mission-critical services win during contention. In the checkout story, the remedy was dedicated pools, CPU limits and circuit breakers. Nothing exotic, which is rather the point.

## Guardrail two: deterministic execution

Inference pipelines get treated as system components with hard edges: validate inputs and reject malformed ones early, put execution timeouts on long-running requests, validate output schemas, and define performance budgets at design time. Those budgets include maximum inference latency, capacity headroom and rate limits on inference APIs.

## Guardrail three: lineage you can replay

When an automated decision triggers an incident, the investigator needs to know what input data the model saw, which model version answered and which feature values drove the result. Gemidi's operational lineage is input snapshots, version-pinned model artifacts and distributed trace IDs, which together allow replaying a prediction during the investigation. Replay is where he puts the gain in time to resolution. He also folds security into reliability: access controls limit blast radius, so they belong in the same design conversation.

## Guardrail four: operating it for years

Models drift because users and data change. His toolkit is continuous monitoring on AI-specific signals such as confidence distributions, feature distributions and inference latency percentiles, plus shadow deployments, canary releases and champion-challenger testing before full rollout, with automated rollback triggers. Human oversight stays in: confidence thresholds route uncertain predictions to human review, and feature flags let engineers switch a model off quickly during an incident.

## Who should watch

SREs and platform engineers who have just been told a model is moving into the request path will get a clear checklist. Data scientists will find it a useful preview of the questions operations will ask. It is a principles talk with one worked example, delivered clearly but without code. His four takeaways fit on a sticky note: isolate AI workloads early, enforce execution constraints, build lineage from day one, and engineer for drift.

## Related Conf42 talks

- [Cell-Based Isolation for Multi-Tenant Platforms on Kubernetes](https://www.conf42.com/DevSecOps_2026_Lahiru_De_Silva_kubernetes_multitenancy_isolation) by Lahiru De Silva.
- [Challenges and takeaways of managing AI workloads on cloud environments](https://www.conf42.com/Large_Language_Models_LLMs_2025_Graziano_Casto_workloads_cloud_environments) by Graziano Casto.
- [The machine learning pipeline is a myth - build production ML systems with feature/training/inference pipelines](https://www.conf42.com/Python_2023_Jim_Dowling_pipeline_myth_production_ml_systems_feature_training_inference_pipelines) by Jim Dowling.

[Watch Ajay Srinivas Kiran Gemidi's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ajay_Srinivas_Kiran_Gemidi_reliability_first_architectures) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/vm92JbUOJ1U).

## Watch the talk

[Reliability-First Architectures for AI Analytics in Mission-Critical Platforms](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ajay_Srinivas_Kiran_Gemidi_reliability_first_architectures) at Conf42 Site Reliability Engineering (SRE) 2026.
