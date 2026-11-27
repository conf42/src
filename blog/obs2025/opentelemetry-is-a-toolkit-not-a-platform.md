# OpenTelemetry is a toolkit, so budget for the rest of the build

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/opentelemetry-is-a-toolkit-not-a-platform

In short: Meletius Mgbeodichimma Igbokwe at Conf42 Observability 2025 on field lessons from OpenTelemetry: collector sizing, version drift, docs and training.

OpenTelemetry gives you the plumbing for traces, metrics and logs; it does not give you a finished observability system. That is the thread through Meletius Mgbeodichimma Igbokwe's talk at Conf42 Observability 2025, a practitioner's list of what goes wrong once a team moves from the OpenTelemetry pitch to running collectors in production, and what he would do differently.

The talk starts with the promise: a single standard across clouds and on-premises, freedom from vendor-specific agents, and broad adoption across the big cloud providers and established tools like Datadog and LogicMonitor. Then it spends most of its time on the gap between that promise and a Tuesday afternoon with a full disk.

## The pain starts before the first span

Meletius groups the early problems into three. Documentation that drifts out of date, so teams follow instructions for a version they are not running. SDK and library burden across languages, where outdated libraries quietly break instrumentation. And version conflicts between components, which he described as a constant source of friction when teams try to ingest or trace anything. None of these is exotic. All of them eat weeks.

His fix for the documentation problem is cultural rather than technical: treat internal docs as a regular activity owned by everyone, not something one person updates once in a while.

## Collectors need real hardware and someone watching them

The most memorable part is a story from his own environment. A cluster used for support servers and data warehousing filled its storage, nobody had a collector watching it, the server disks filled too, and the environment crashed, at real cost to the business. The lesson is the obvious one that teams still skip: monitor the thing that stores your telemetry.

He also warned against putting collectors on undersized, burstable servers meant for dev and test. Processing pipelines that cannot keep up with data volume, and single points of failure in the telemetry path, turn into dropped or delayed data exactly when the environment is busiest. Observability that goes dark under load is a smoke alarm that only works when nothing is burning.

## Set it up, then test that it works

A recurring complaint in the talk is the "configure and walk away" pattern: monitoring gets installed, the ticket closes, and nobody checks the dashboards, the schemas or whether the alerts fire. Meletius calls these monitoring blind spots and pairs them with collector crashes under peak load and version drift, where weeks go into triaging library updates that did not match the codebase.

His advice: verify monitoring end to end before handing it off, and schedule regular reviews of schemas, resources and integration points rather than waiting for an incident to do the review for you.

## What he says actually works

The closing recommendations are pragmatic:

- Start small, on critical systems, and limit the initial scope.
- Write documentation and training tailored to your own stack.
- Expand gradually as the team gets comfortable.
- Treat OpenTelemetry as a foundation and build alerting and visualisation layers on top of it.
- Accept that observability needs ongoing investment in people and infrastructure, not a one-time setup.

## Who should watch

Teams early in an OpenTelemetry rollout, and managers who need a plain-language case for why "we adopted OTel" is the start of the budget conversation, not the end. Engineers looking for collector configuration snippets or benchmark numbers will not find them here; this is an experience talk about process and ownership.

## Related Conf42 talks

- Bruno Ferreira's [Optimizing Observability with OpenTelemetry Collector for Budget-Friendly Insights](https://www.conf42.com/DevOps_2024_Bruno_Ferreira_observability_opentelemetry_collector) gets into the collector configuration this talk leaves out.
- Siddhartha Khare's [The Road Ahead: OpenTelemetry's Path to Observability's Future](https://www.conf42.com/DevSecOps_2023_Siddhartha_Khare_opentelemetry_path_observability) for the project's direction.
- Nočnica Mellifera's [Open Source Observability with OpenTelemetry](https://www.conf42.com/DevOps_2023_Nocnica_Mellifera_open_source_observability_opentelemetry) as a friendly starting point.

[Watch Meletius Mgbeodichimma Igbokwe's talk](https://www.conf42.com/Observability_2025_Meletius_Mgbeodichimma_Igbokwe_lessons_field_bullet)

[Watch the talk on YouTube](https://youtu.be/fAuhNeJA1zE).

## Watch the talk

[OpenTelemetry Is Not a Silver Bullet: Lessons from the Field](https://www.conf42.com/Observability_2025_Meletius_Mgbeodichimma_Igbokwe_lessons_field_bullet) at Conf42 Observability 2025.
