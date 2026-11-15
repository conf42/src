# Your system recovers only as fast as its slowest workload

Conf42 Blog, 2026-01-18. https://www.conf42.com/blog/devops2026/boring-regional-failover-at-intuit

In short: Akshay Pratinav of Intuit at Conf42 DevOps 2026 on a Kubernetes-native DR platform built on declarative intent, pre-scaling and staged failover.

At Conf42 DevOps 2026, [Akshay Pratinav](https://www.conf42.com/DevOps_2026_Akshay_Pratinav_failover_resilience_workloads), Staff Software Engineer at Intuit, described how his team set out to make regional failover boring. The lesson that shaped the design: your system only recovers as fast as the slowest workload in the stack, so APIs, async workers, databases and routing have to fail over together, as one declared, staged workflow.

He says up front that this isn't a product pitch but patterns learned on the way. Then, helpfully, he shows the system anyway: the YAML teams write, the architecture behind it and the guardrails that keep it safe.

## Recovery is the outage customers remember

Pratinav starts from the premise that outages are normal: regions fail and managed services have bad days. What erodes customer trust is slow, manual, chaotic recovery. In a microservice estate, recovery is lopsided. APIs come back quickly, background workers lag, databases need promotion and async pipelines replay or stall.

Two organisational problems make it worse. Failover evolves team by team, so you end up with dozens or hundreds of DR strategies that are each fine and don't compose. And runbooks get followed by stressed, tired engineers with incomplete information, which is the worst time to work through a multi-page checklist. Nobody, he says, should be manually scaling clusters at 3 AM.

## Declare intent, let the platform own the mechanics

The biggest shift was from imperative procedures to declarative intent. Teams declare capacity, dependencies, data requirements and criticality; the platform executes. A customer-facing API and a nightly batch job can declare very different needs inside the same framework.

Two other principles carry a lot of weight. Fail over the whole stack, because a partial failover can be worse than none: move the API without its async workers and you corrupt state or build huge backlogs. And pre-scale the standby region from live primary traffic, so failover becomes a traffic move rather than a wait for cold capacity.

## A DR plan is a workflow with four stages

The concrete example is a DR procedure in YAML for an active-passive service with a database. Stage one pre-scales Kubernetes pods in the failover region by updating HPA and replica values to match the primary. Stage two promotes the standby database. Stage three dials traffic over. Stage four resets HPA and replicas to their original values, so nobody pays for idle compute afterwards. Each stage starts only when the previous one completes.

Under the hood, a UI calls a backend API that starts a state machine. The state machine publishes each stage to a Kafka topic, where agents pick it up: a database agent for promotion, a capacity agent for scaling, and an in-cluster add-on on every Kubernetes cluster that does the pre-scaling. Each agent takes a lock in a semaphore service and releases it only after an external monitoring tool confirms the action, and the state machine polls that lock before sending the next stage. The frontend is React; the backend is Go and Python. Routing shifts through Route53 or Istio, based on health signals rather than someone's judgement call.

His line on the design deserves a sticky note: toggles don't recover systems, workflows do.

## Safety rails, then practise until it's dull

Speed without safety can be worse than staying down, so moves are gated on health checks, dependency validation and drift detection, and every step is reversible. He wants no DR-only configuration and no special flag flipped once a year: production should always be ready to fail over. Regular game days, low-stress because the process is automated, mean the first failover never happens during a real outage.

The payoff he describes is partly cultural. Once engineers trust the system, they practise more, and failover becomes something they understand rather than fear.

## Who should watch

Platform teams running many microservices across regions, and SREs tired of DR plans that live in a wiki. If you are designing a DR orchestrator, the Kafka-plus-semaphore stage gating is the part to study.

## Related Conf42 talks

- [When Clusters Collide: The Misadventures of Disaster Recovery in Kubernetes](https://www.conf42.com/Platform_Engineering_2024_Lev_Andelman_clusters_disaster_kubernetes) by Lev Andelman at Conf42 Platform Engineering 2024.
- [Recovery Without Reintroducing Risk: A Security-First Approach to RTO/RPO in Event-Driven Systems](https://www.conf42.com/DevSecOps_2026_Sanjay_Iyer_recovery_eventdriven_rto) by Sanjay Iyer at Conf42 DevSecOps 2026.
- [Normalizing Chaos: A Cloud Architecture for Embracing Failover](https://www.conf42.com/Chaos_Engineering_2021_Ryan_Guest_cloud_architecture_embracing_failover) by Ryan Guest at Conf42 Chaos Engineering 2021.

[Watch Akshay Pratinav's talk](https://www.conf42.com/DevOps_2026_Akshay_Pratinav_failover_resilience_workloads) or the [YouTube recording](https://youtu.be/q6jCz-CY6zc).

## Watch the talk

[The Multi‑Workload Challenge: Predictable Failover Across the Stack](https://www.conf42.com/DevOps_2026_Akshay_Pratinav_failover_resilience_workloads) at Conf42 DevOps 2026.
