# Auto-healing APIs need feature flags and brakes, not just restarts

Conf42 Blog, 2026-10-01, updated 2026-11-09. https://www.conf42.com/blog/featureflags2026/auto-healing-apis-need-flags-and-brakes

In short: Anil Kumar Chitiprolu at Conf42 Feature Flags 2026 on a control loop that pairs monitoring, circuit breakers and feature flags to recover microservices safely.

Restarting an API does not bring back a failed database, and scaling out just adds more instances hammering the same dead dependency. At Conf42 Feature Flags 2026, Anil Kumar Chitiprolu, a senior lead full-stack developer at Allstate with more than fifteen years in IT, presented a framework for API resilience that treats recovery as a control loop: detect, decide, act, validate, learn, with feature flags as one of the main levers for acting.

It's an architecture overview rather than a code walkthrough, aimed at teams whose recovery plan today is a developer on call restarting services.

## Monitoring tells you, it doesn't fix

His starting problem is the everyday microservices one. A single customer request may touch authentication, profiles, payments, inventory, messaging and external providers, and failures rarely stay put: one slow dependency exhausts threads, grows queues and cascades. So resilience has to be a system property, not something each service owns alone.

Monitoring gives you visibility. The harder questions are operational: restart, redirect, scale or disable? Anil's loop answers them in stages. Observe and detect. Correlate and decide, including whether the service is down on purpose for a deploy, patch or hotfix. Act. Validate, because automation must never assume that running an action means the problem is solved. Then learn from when and why things fail.

Detection leans on the usual four signals (metrics, logs, distributed tracing and synthetic checks for critical workflows when real traffic is low), plus business-level signals. He contrasts static thresholds, simple and fast but blind to gradual drift, with anomaly detection that adapts to baselines that shift with workload and deployments.

## Flags handle the slow problem, breakers the fast one

The feature flag section is the core. For resilience work, flags become runtime operational switches: disable a degraded capability while the rest of the app runs, expand or reverse exposure against health checkpoints, and keep the blast radius small without a full deployment.

He pairs them with circuit breakers deliberately. A breaker reacts immediately to dependency health and stops requests reaching a failing service. A flag works at the application level, switching to an alternate workflow or turning off the dependent feature for as long as needed. One gives you instant containment, the other durable control. His routing examples are concrete: send clients from a failed legacy service to the modern API or the reverse, or shift traffic to another region behind the load balancer.

## Dependency-aware healing and the transactions in between

The talk's most useful part is about what restarts don't fix. Auto-healing logic has to understand relationships between services. Options include a degraded mode serving cached data or queueing work for later, a flag-driven bypass of functionality that depends on the unavailable resource, and controlled rejection that fails gracefully instead of silently. Anil also insists on dealing with transactions that failed or partly failed during the outage: capture them, record their state and get them processed, not just bring the pod back.

Safe automation gets three guard rails: preconditions that confirm the diagnosis before acting, cooldown periods before repeating an action, and bounded automation that escalates to a human when repeated actions don't restore health. A self-healing system without cooldowns is just a very fast way to restart something forty times.

## Governance for operational flags

Recovery has to be observable too: the trigger condition, the signals used, the flag state before and after, routing and infrastructure changes, and the resulting behaviour. That history is how engineers answer why an action happened and whether it worked. Operational flags need strong authorisation and audit logs, policies can be asymmetric (disabling automated, restoring only with stronger evidence or human approval), temporary flags get retired, and the flag service itself is critical infrastructure. Known, reversible failures belong to automation; uncertain or high-impact decisions stay with engineers.

## Who should watch

Developers and SREs running REST or microservice estates who want a checklist for moving from manual restarts toward controlled automatic recovery. It's a conceptual overview, so expect patterns and principles rather than tool configuration.

## Related Conf42 talks

- [Designing Resilient Self-Service Search in Go: From Failure Modes to Intelligent Fallback Architectures](https://www.conf42.com/Golang_2026_Hima_Bindu_Yanala_designing_resilient_self) by Hima Bindu Yanala of eBay at Conf42 Golang 2026.
- [Green Dashboards, Broken Systems: Why Observability Alone Can't Prove Resilience](https://www.conf42.com/Observability_2026_Uma_Mukkara_resilience_testing_enterprise) by Uma Mukkara of Harness at Conf42 Observability 2026.
- [Building Self-Healing CI/CD Pipelines with Tekton and ArgoCD](https://www.conf42.com/DevOps_2026_Srinivas_Pagadala_Sekar_gitops_resilience_automation) by Srinivas Pagadala Sekar of Karsun Solutions at Conf42 DevOps 2026.

[Watch Anil Kumar's talk](https://www.conf42.com/Feature_Flags_2026_Anil_Kumar_api_resilience_monitoring) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/0jp7KlfqCcY).

## Watch the talk

[Feature Flag–Driven API Resilience Through Autonomous Monitoring and Auto-Healing](https://www.conf42.com/Feature_Flags_2026_Anil_Kumar_api_resilience_monitoring) at Conf42 Feature Flags 2026.
