# Observability is time to understanding, and OpenTelemetry shortens it

Conf42 Blog, 2023-01-26. https://www.conf42.com/blog/devops2023/opentelemetry-collector-time-to-understanding

In short: Nočnica Mellifera (TelemetryHub) at Conf42 DevOps 2023 on why microservices hide the map, and how OpenTelemetry's collector and tracing bring it back

Restarting a service every 24 hours because it runs out of memory is a fix. It is not understanding. Nočnica Mellifera, Head of Developer Relations at [TelemetryHub](https://ter.li/m8p5qz), opened her Conf42 DevOps 2023 talk with that distinction, then walked through why microservices make understanding harder and how OpenTelemetry, and especially its collector, is the open-source way back.

It is an introductory talk: the three pillars, distributed tracing, the collector and language support, delivered by someone who has clearly answered the beginner questions many times.

## What is observability, if not a buzzword?

Mellifera calls it a design criterion rather than a tool or a standard. Following Charity Majors and the OpenTelemetry project, she defines it as time to understanding, which is usually the first half of time to resolution. That covers the full outage, but also the quieter puzzles: why the app is slow for users in one region, or the bug report nobody can reproduce.

## Why do microservices make it worse?

Her history of the monolith is more generous than usual. Monoliths did not die because they performed badly; they died because it took months for a new engineer to become effective, and with people averaging around two years in a role, that stopped working. Microservices let someone contribute within weeks.

The cost lands on observability. In a monolith, the few people who understood the whole system could get to a full explanation, because all the information sat on one stack. With microservices, someone understands each dot completely. The most common question she gets from teams with deep architectures is not about failures at all: on a normal, successful checkout request, which services does it touch?

"Nobody understands the map that covers all of these microservices," Nočnica Mellifera said at Conf42 DevOps 2023. Her conclusion: for understanding an outage, microservices are almost always a dead weight loss, and the 3am incident is easier in a monolith once the right people are awake.

## Metrics, logs, traces: which one helps when?

- **Metrics** are the speedometer: a number describing a complex system, the best high-level view, and cheap to store even at high volume.
- **Logs** always contain a complete and thorough explanation of the problem, somewhere. Storage and management are their own challenge, and many engineers know they are in a bad place if logs are where an investigation starts.
- **Traces** are, in her description, a hybrid between metrics and logging, aimed at showing every component a request hits as a waterfall of spans, including which steps block which (auth before payment gateway, say).

Her slide on the dirty secret of tracing is worth remembering when someone proposes keeping everything forever: most trace data is never viewed, and by most she means 99.999%.

## Why did tracing need an open standard?

Distributed tracing is simple to describe: add a trace header near the start, pass it along with the request, and have collector-side logic stitch the pieces together. In the closed-source SaaS era, each vendor shipped its own libraries for front end, back end and database, and as microservices multiplied no single company could instrument everything. Traces ended up with black boxes where the context was lost. OpenTelemetry defines an open standard for how components exchange metrics, traces and logs, so the person instrumenting a Laravel or Rails build can produce spans that join up with everyone else's.

## Do you need to run a collector?

The collector is where she says the magic happens, and it is more than a data exporter. Its processors filter, batch and add attributes. Her example: a specific format of health data that must never leave your network, even if it was captured by accident. Instead of waiting for a vendor to build a filter, you add a processor, and because the collector runs in your own cloud, the data is scrubbed before it travels.

But you do not need one on day one. Reporting directly from a service to Prometheus or another OpenTelemetry endpoint is fine for a proof of concept; it just means many more network requests without batching. Switching to a collector later is easy. She also covers baggage, the small piece of context (a client ID is the classic) that travels with a request and can be written onto a trace explicitly.

## Is language support good enough?

Better than the tables suggest, she argues. She once wrote that Ruby looked not quite ready, then learned Shopify uses the Ruby OpenTelemetry project heavily, with metrics marked experimental but widely run in production. For many languages only logs are missing, and you have had a way to ship logs for years. Java and .NET get a lot from automatic instrumentation.

## Who should watch

Engineers new to OpenTelemetry who want the concepts in order before reading the docs, and anyone who has to explain to a team why tracing beats grepping logs across 30 services.

## Related Conf42 talks

- Nicolas Fränkel on [OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing) at Conf42 DevOps 2023.
- Bruno Ferreira on [the OpenTelemetry Collector](https://www.conf42.com/DevOps_2024_Bruno_Ferreira_observability_opentelemetry_collector) at Conf42 DevOps 2024.
- Michael Haberman on [distributed tracing with OpenTelemetry](https://www.conf42.com/JavaScript_2021_Michael_Haberman_distributed_tracing_OpenTelemetry) at Conf42 JavaScript 2021.

[Watch Nočnica Mellifera's talk](https://www.conf42.com/DevOps_2023_Nocnica_Mellifera_open_source_observability_opentelemetry)

## From TelemetryHub

TelemetryHub is an endpoint for OpenTelemetry data: point your services or collector at it and explore the metrics, traces and logs they report.

- [TelemetryHub website](https://ter.li/m8p5qz)

[Watch the talk on YouTube](https://youtu.be/wApKJJVnSIk).

## Watch the talk

[Open Source Observability with OpenTelemetry](https://www.conf42.com/DevOps_2023_Nocnica_Mellifera_open_source_observability_opentelemetry) at Conf42 DevOps 2023.
