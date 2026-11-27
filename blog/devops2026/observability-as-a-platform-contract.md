# Make observability part of the paved road, then fail builds without it

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/observability-as-a-platform-contract

In short: Sumit Kaul of PayJoy at Conf42 DevOps 2026 on zero-code instrumentation, SLOs as version-controlled contracts and CI/CD gates that enforce them.

Observability that depends on each team remembering to add a span is observability with holes in it. At Conf42 DevOps 2026, Sumit Kaul, staff software engineer at PayJoy, argued for turning it into a platform contract: the platform guarantees traces, metrics and logs to every service on the paved road with no instrumentation code, SLOs live next to the manifests as version-controlled agreements, and CI/CD fails a build that breaks the contract, the same way it fails one with low test coverage.

## The problem: coverage only where someone remembered

Sumit's starting point will be familiar to anyone who has bought Datadog, New Relic or a Grafana stack and still had blind spots. Every tool needs manual instrumentation. In a codebase with millions of lines, retrofitting it is a daunting job, so coverage is inconsistent, debugging turns reactive the moment an incident hits an uninstrumented corner, and teams split along an unhelpful line: platform says it does not know the application's context, application teams say observability is platform's job.

The contract model resolves the silo by changing who owns what. The platform owns collection. The service gets observability as an outcome of shipping on the paved road. The contract defines the expectations in between.

## Zero-code instrumentation has three parts

The architecture section is concrete:

- **Automatic instrumentation** with OpenTelemetry agents and framework configuration, across Java, Python, Node, Go, .NET and others, with no code changes from developers.
- **Runtime sidecars** that capture network traffic, database queries and message interactions, so a web request can be correlated with the middleware call and the query behind it.
- **Base container images** shipped by the platform team with the agents, ports and signal configuration already baked in. Merge the PR, the pipeline picks up the base image, and the service is instrumented.

Portable containers and standardised collectors keep it consistent across EKS, AKS and GKE. Sumit says his organisation instrumented more than 200 services across three clouds this way, with service coverage above 99%.

## SLOs as a contract the pipeline can check

The contract has a signal requirement (the few high-signal, low-noise indicators that say whether a service is healthy) and an SLO specification, such as availability targets and p95 latency, stored as a manifest beside the deployment config. That turns "the site feels slow" into a number someone agreed to.

Enforcement sits in CI/CD. On commit, contract validation checks the schema and API contracts, an instrumentation check confirms the hooks and the pre-baked image are present, and a failure stops the pipeline. Sumit's mental model is explicit: treat it like a coverage threshold or a critical vulnerability gate.

## Canaries judged against the SLO

On release, the pattern is to capture the current SLI baseline, send a small slice of traffic (he uses 5% as the example) to the new version, compare its metrics against the baseline and the burn-rate policy, then promote to 50% and 100% or roll back. Degraded SLIs are tied to the deployment's version tag, so tracing a bad release down to the span, the database query and the commit becomes a short walk instead of a war room.

## Results and the adoption path

The before-and-after numbers he shares include mean time to respond dropping from 45 to 12 minutes, failed deployments falling to 12% from 30 to 40%, and 78% fewer manual rollbacks. He also cites examples from financial services, retail Black Friday traffic and logistics, where he says 450-plus microservices were instrumented with zero code changes.

The adoption advice may be the most transferable part. Pilot with two or three services over four to six weeks, expand to 10 to 20, then scale. Run workshops for two or three teams at a time, built on their own metrics and traces rather than generic training, and let early wins spread.

## Who should watch

Platform teams building golden paths, and SREs tired of being the instrumentation police. The numbers are from Sumit's own environments, so treat them as one organisation's results rather than benchmarks; the contract-plus-gate pattern is what travels.

## Related Conf42 talks

- [Zero-instrumentation observability based on eBPF](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Nikolay_Sivko_zeroinstrumentation_observability_ebpf) by Nikolay Sivko gets to "no code changes" by a different route.
- [Techniques for SLOs and Error Budgets at Scale](https://www.conf42.com/Observability_2023_Fred_Moyer_slos_error_budgets_scale) by Fred Moyer goes further into the SLO math the contract depends on.
- [Optimizing Observability with OpenTelemetry Collector for Budget-Friendly Insights](https://www.conf42.com/DevOps_2024_Bruno_Ferreira_observability_opentelemetry_collector) by Bruno Ferreira covers the collector side of a platform-owned pipeline.

[Watch Sumit Kaul's talk](https://www.conf42.com/DevOps_2026_Sumit_Kaul_slos_instrumentation_observability)

[Watch the talk on YouTube](https://youtu.be/pQBoWM78Q5w).

## Watch the talk

[Observability as a Platform Contract: Zero-Code Instrumentation and CI/CD-Enforced SLOs](https://www.conf42.com/DevOps_2026_Sumit_Kaul_slos_instrumentation_observability) at Conf42 DevOps 2026.
