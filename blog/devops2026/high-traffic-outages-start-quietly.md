# Outages start quietly, so build systems that fail fast

Conf42 Blog, 2026-01-19. https://www.conf42.com/blog/devops2026/high-traffic-outages-start-quietly

In short: Justice Eziefule of Metastable Labs at Conf42 DevOps 2026 on retry storms, pool exhaustion, timeouts that cancel work and failing fast under load.

Most outages don't announce themselves with a wall of 500s. They start with a dependency that gets a little slower while every dashboard still looks fine. At Conf42 DevOps 2026, [Justice Eziefule](https://www.conf42.com/DevOps_2026_Justice_Eziefule_availability_resilience_operations), co-founder and CTO of Metastable Labs and formerly a senior software engineer at Paystack, walked through how that quiet start turns into a full outage, and the habits that keep a system standing while it is failing.

Eziefule spent years at Paystack, the African payments company later acquired by Stripe, running systems that processed hundreds of millions of dollars a month. He promised not to make the talk a shopping list, and kept the promise: it's about failure mechanisms that behave the same on any cloud.

## The incident that looks like a normal Tuesday

His example starts with a traffic bump from a launch or a campaign. Twenty minutes in, one dependency slows down: Postgres under heavier reads, a hot Redis, a third-party provider rate-limiting you. Average query time climbs from about 15 ms to about 150 ms. Nothing is down yet.

Then the maths arrives. One dashboard load fans out to six internal services, each hitting the database, so 100 ms per call becomes 600 ms per request. And averages lie at scale: if p50 is 100 ms but p99 is five seconds, someone is always living in that p99.

## Retries multiply load at the worst moment

Things slow down, so everyone adds retries: the client, the service, the SDK. One request becomes two or three. His point is blunt: retries don't reduce load, they multiply it, at exactly the wrong time. That's the retry storm, and it turns a slow dependency into a death spiral.

Next comes connection pool exhaustion. Slower queries hold connections longer, the pool of 50 fills, and new requests queue for a connection that never frees up. CPU and memory look fine. The service is up but frozen, which he calls a zombie. Then timeouts fire, and many are badly designed: no timeout at all, a 30-second timeout that blocks everything, or a timeout that doesn't cancel the work underneath. That last one means the database keeps grinding on queries for requests the client has already given up on. Systems, as he puts it, die politely.

## Stabilise first, investigate later

During an incident, his first goal is not root cause. It's to stabilise the system and protect users, and the toolkit is ordered:

- **Limit concurrency.** Cap concurrent requests per endpoint and concurrent DB queries. Returning a 429 beats accepting everything and collapsing.
- **Layered timeouts that cancel.** Short and consistent: two to three seconds for a user request, roughly 500 ms to 1.5 s between services, and when a request times out, cancel its pending queries and downstream calls.
- **Circuit breakers.** Stop calling a sick dependency for a while, giving it room to recover and keeping your service from being dragged down.
- **Graceful degradation.** In payments, auth and placing an order are critical; a recommendations widget is not. Serve cached data, return partial results, and never block a payment because analytics is slow.
- **Load shedding.** Reject early, drop non-critical background tasks, sample logs. Fail fast, because slow failure is what kills you.

## Alert on burn rates, not CPU

For detection he uses the four golden signals (latency, traffic, errors, saturation), with latency as percentiles. Quiet incidents show up as a stable p50, a creeping p95 and a spiking p99, with queue depth and pool usage rising before any errors. So alert on p99 burn rate, queue growth, error budget burn and pool exhaustion, not on whether CPU is high. Add correlation IDs and structured logs even without full tracing, so you can follow one request through the stack.

His controversial claim is that many outages are prolonged by a messy response rather than bad code: five engineers deploying fixes with nobody in charge. His playbook names an incident lead, freezes non-essential changes, stabilises, restores via rollback, and only then investigates. Before the next outage, design for idempotency so retries can't double-charge, move heavy work to queues, add bulkheads and rate limits.

## Who should watch

Backend engineers and SREs running anything with fan-out and a shared database. If you have ever watched a healthy-looking service stop answering, this half hour explains why, in plain language.

## Related Conf42 talks

- [Designing for Failure: Strategies to Build Resilient, Always-On Services](https://www.conf42.com/DevSecOps_2024_Abhishek_Vajarekar_resilient_alwayson_services) by Abhishek Vajarekar at Conf42 DevSecOps 2024.
- [AI-Driven Rate Limiting for Resilient and Cost-Efficient Cloud API Protection](https://www.conf42.com/Incident_Management_2025_Rehana_Sultana_Khan_ratelimiting_api_protection) by Rehana Sultana Khan at Conf42 Incident Management 2025.
- [Building Self-Healing Cache Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Shailin_Saraiya_cache_millions_latency) by Shailin Saraiya at Conf42 Platform Engineering 2025.

[Watch Justice Eziefule's talk](https://www.conf42.com/DevOps_2026_Justice_Eziefule_availability_resilience_operations) or the [YouTube recording](https://youtu.be/726LRiAHQmM).

## Watch the talk

[Keeping High-Traffic Systems Running When Things Go Wrong](https://www.conf42.com/DevOps_2026_Justice_Eziefule_availability_resilience_operations) at Conf42 DevOps 2026.
