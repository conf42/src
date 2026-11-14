# Design workflow interoperability in five planes, not adapters

Conf42 Blog, 2026-04-01, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/five-planes-of-workflow-interoperability

In short: Devinder Tokas of Microsoft at Conf42 Cloud Native 2026 on a five-plane framework built on CNCF standards to keep cloud-native workflows portable.

If your team spends more time maintaining glue code between workflow engines than shipping features, interoperability was treated as an integration task instead of an architecture decision. At Conf42 Cloud Native 2026, Devinder Tokas, Software Engineer at Microsoft with more than 20 years on large-scale platform systems, presented a five-plane framework for designing portability into cloud-native workflows using open standards from the CNCF ecosystem.

It is a framework talk: a structured checklist with the standards that fit each layer, plus a migration roadmap. There is no live demo.

## Where the integration debt comes from

Devinder lists three patterns that fragment cloud-native estates. Vendor lock-in, where proprietary APIs or managed services make migration costly and constrain future choices. Incompatible tooling, where different platforms run different workflow engines and data formats, so teams write custom adapters to connect basic pieces. And siloed workflows, isolated per cluster, cloud or team, which blocks unified observability and consistent governance. The net effect is engineering time drifting from features toward integration upkeep.

Standardized contracts are one of the few strategies that systematically reduce that debt, and they buy portability: workflows can move between providers when cost, performance or compliance requirements change, without rewriting the platform.

## The five planes

The model splits a workflow system into five layers, each with a clear contract and deliberately chosen standards:

1. **Workflow definition.** Declare workflows in a portable, versioned format rather than a runtime-specific one: the CNCF Serverless Workflow specification, OpenAPI for service interfaces, JSON Schema for validation. Contract-first, kept in source control, with schema evolution managed on purpose.
2. **Execution and state.** Durable state, checkpointing and recovery, with exactly-once semantics where possible and well-defined idempotency where it is not. CloudEvents helps different engines read state transitions the same way.
3. **Integration.** CloudEvents as the event envelope, AsyncAPI for message-driven interfaces, OpenAPI for request-response, with a service mesh and API gateways for consistent connectivity, security and routing.
4. **Observability and lineage.** OpenTelemetry for traces, metrics and logs, W3C Trace Context to correlate across vendors and runtimes, and data lineage to show what produced, transformed and consumed each piece of data.
5. **Packaging and deployment.** OCI images, Helm charts, Kustomize overlays and GitOps for repeatable, declarative deployments with predictable rollbacks.

His point about the first plane applies to the rest: if the definition is not portable, you pay for it in every plane downstream.

## Outcomes, with an honest caveat

The abstract cites benchmark figures for event-driven throughput and OpenTelemetry Collector performance. In the talk itself Devinder is careful to present performance and reliability gains as representative outcomes that depend on architecture, workload and implementation. The mechanisms are plausible enough on their own: standard contracts cut translation overhead between components, consistent event formats help throughput, shared observability removes duplicate agents and pipelines, and durable state lets workflows resume from the last safe point after a failure. His summary is that ambiguity is often the enemy of reliability, and standard contracts reduce ambiguity.

## A blueprint and a migration path

The reference architecture is an API gateway as the entry point, a service mesh for service-to-service identity and traffic policy, a CloudEvents-compliant messaging backbone, an orchestrator connected through standard APIs, cloud-agnostic state storage, and OpenTelemetry instrumentation throughout. Because the contracts are fixed, implementations can be swapped.

For existing systems: audit definitions against standards, replace bespoke adapters at the integration points, migrate one plane at a time, and instrument observability early so you can measure progress and catch regressions. For greenfield systems: adopt all five planes from day one.

## Who should watch

Platform and architecture teams facing a multi-engine, multi-cloud workflow estate, or planning one. If you already standardize on CloudEvents and OpenTelemetry, the value is the plane-by-plane checklist for spotting the gap you have not covered.

## Related Conf42 talks

- [Nicolas Fränkel's practical introduction to OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing) at Conf42 DevOps 2023.
- [Siri Varma Vegiraju on workflow reliability with Dapr](https://www.conf42.com/Cloud_Native_2025_Siri_Varma_Vegiraju_workflow_dapr_failure) at Conf42 Cloud Native 2025.
- [Gunjan Desai Rajendrakumar on platform engineering for healthcare interoperability with FHIR](https://www.conf42.com/Platform_Engineering_2025_Gunjan_Desai_Rajendrakumar_interoperability_exchange_fhir) at Conf42 Platform Engineering 2025.

[Watch Devinder Tokas's talk](https://www.conf42.com/Cloud_Native_2026_Devinder_Tokas_cloudarchitecture_backend_systems)

[Watch the talk on YouTube](https://youtu.be/C3431IagV_g).

## Watch the talk

[Interoperability by Design for Cloud-Native Workflows](https://www.conf42.com/Cloud_Native_2026_Devinder_Tokas_cloudarchitecture_backend_systems) at Conf42 Cloud Native 2026.
