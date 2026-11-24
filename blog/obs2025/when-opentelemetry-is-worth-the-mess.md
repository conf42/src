# When OpenTelemetry is worth the mess it brings

Conf42 Blog, 2025-06-01, updated 2026-11-09. https://www.conf42.com/blog/obs2025/when-opentelemetry-is-worth-the-mess

In short: NVIDIA's Narendra Reddy Sanikommu at Conf42 Observability 2025 on what OpenTelemetry fixes, the new problems it creates, and when it pays off.

OpenTelemetry fixes vendor lock-in and fragmented instrumentation, and in exchange hands you a stack of SDKs, exporters and YAML. Narendra Reddy Sanikommu, a senior software engineer at NVIDIA, made that trade explicit at Conf42 Observability 2025 in a short, balanced talk: what OTel solves, which problems it creates, and how to decide whether your organisation is on the right side of the ledger.

The title asks "OpenTelemetry or OpenTeleMessy?" and the answer is honest: both, depending on what you run.

## What it genuinely fixed

Narendra starts with the wins, and they are real. Before OpenTelemetry, every vendor shipped its own agent and SDK; now you instrument once and send the data to whichever backend you like. OTel merged OpenTracing and OpenCensus into one standard across languages, covers metrics, traces and logs, and lets you correlate them. The collector decouples collection from analysis, and auto-instrumentation removes a lot of boilerplate. He also pointed to its community: one of the most active CNCF projects, with a busy roadmap.

## And what it broke

Then the bill. The documentation throws a newcomer straight into APIs, SDKs and layers of abstraction. Each component has its own configuration. Language implementations are inconsistent, which undercuts the polyglot promise: the standard is shared, the quirks are not. Signals sit at different maturity levels, with tracing the most mature, metrics next, and logging the recent arrival. Debugging is hard when a problem could live in instrumentation, collection or export. And collector configurations grow into large YAML files with mismatched component names, authentication you wire up yourself, and connectivity issues. Filing an issue can mean bouncing between repositories.

Anyone who has chased a missing span through three config files will recognise every slide.

## The test for whether it pays off

The most useful section is his decision rule. OpenTelemetry makes sense when:

- your organisation has a large, diverse technology stack you want to standardise;
- the value exceeds the implementation complexity, which you have to judge honestly;
- you want vendor-neutral collection and export as a long-term investment;
- you run cloud-native, distributed, containerised workloads such as Kubernetes;
- you need control over data routing and filtering to cut noise and cost.

If none of those apply, the mess may outweigh the benefits.

## How to tame it

His strategies are incremental. Begin with language-specific auto-instrumentation, and use what your platform already ships (he mentioned Amazon EKS offering OpenTelemetry collectors). Start with tracing, the most mature signal, and add metrics and logs later. Follow semantic conventions and keep attributes and labels tidy. Use local exporters to speed up troubleshooting. Roll out to critical user flows first instead of a big-bang migration, lean on community blogs and talks beyond the official docs, and consider vendor distributions such as Grafana Alloy that smooth adoption.

The outlook section notes semantic conventions reaching stability, the collector approaching version 1, profiling arriving as a signal, and generative AI observability joining the ecosystem. His conclusion: still the first choice if you want a vendor-neutral, comprehensive solution.

## Who should watch

Architects deciding whether to adopt OpenTelemetry, and teams halfway through an adoption who want a sanity check. It is a compact overview rather than a hands-on lab, so it suits a lunch break.

## Related Conf42 talks

- Prathamesh Sonpatki's [The Complete Handbook to OpenTelemetry Metrics](https://www.conf42.com/DevOps_2024_Prathamesh_Sonpatki_handbook_opentelemetry_metrics) for the signal this talk calls less mature than tracing.
- Nicolas Fränkel's [Practical introduction to OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing), a good first step for the "start with tracing" advice.
- Pranay Prateek's [Scaling Opentelemetry Collectors using Kafka](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Pranay_Prateek_scaling_opentelemetry_kafka) for when collectors become the bottleneck.

[Watch Narendra Reddy Sanikommu's talk](https://www.conf42.com/Observability_2025_Narendra_Reddy_Sanikommu_opentelemetry_messy_problems)

[Watch the talk on YouTube](https://youtu.be/EMHkJQLDuwk).

## Watch the talk

[OpenTelemetry or OpenTeleMessy? Solving Observability Problems While Creating New Ones](https://www.conf42.com/Observability_2025_Narendra_Reddy_Sanikommu_opentelemetry_messy_problems) at Conf42 Observability 2025.
