# Replay production traffic to migrate a gateway with zero downtime

Conf42 Blog, 2025-12-26, updated 2026-11-09. https://www.conf42.com/blog/devops2026/zero-downtime-gateway-migration-shadow-traffic

In short: Oracle Cloud Infrastructure's Kalyan Inturi at Conf42 DevOps 2026 on moving a Ruby monolith gateway to Kong using sampled shadow-traffic parity checks.

Synthetic tests only check the behaviour you remembered to write down. A legacy gateway is mostly behaviour nobody wrote down. At Conf42 DevOps 2026, Kalyan Inturi, a principal member of technical staff at Oracle Cloud Infrastructure, walked through how his team replaced a monolithic Ruby gateway with Kong without a customer-facing incident, by replaying sampled production requests against the new gateway and diffing everything.

This is a case study with a reusable trick at its centre, and it is the trick that makes it worth the watch.

## The monolith in question

The old gateway was Ruby and Sinatra, with session management, authentication, authorisation and routing all in one service. A routing change could break the auth stack. It could not make good use of multi-core machines, scaling one concern meant scaling all of them, Ruby expertise was getting scarce, and security vulnerabilities kept piling up. The obvious plan (write unit and integration tests against the old system, run them on the new one, cut over when green) fails exactly because of the undocumented behaviour and tribal knowledge baked into years of changes.

## Shadow traffic without double writes

The core of the talk is a five-step replay mechanism, and it solves the problem that makes most shadow-traffic schemes scary: executing a write twice.

1. The legacy gateway handles the request normally and answers the client.
2. Asynchronously, a processor on the legacy side assigns a parity ID and stores the downstream request, downstream response and client response in a NoSQL store.
3. It fires the same request at Kong with the parity ID added as a query parameter.
4. Kong does what the legacy gateway should do and forwards downstream. There, an interceptor spots the parity ID and, instead of executing the call again, returns the stored downstream response from the cache.
5. The processor compares both sides and records every difference.

Two comparisons come out of it: what each gateway sent to the backend, and what each sent back to the client. Inturi calls this a store-and-forward pattern that decouples validation from real backend state. Reads would have been safe anyway; the interceptor is what makes writes safe.

## Sample, then roll out in phases

Replaying everything would double load on downstream systems, so they sampled roughly one fifth of requests with a random function over the request ID, on the assumption that over time every route and function would be covered. The full plan had eight phases, from Terraform-provisioned infrastructure with routes captured as YAML for Kong, through load testing, shadow validation and offloading authentication into its own microservice, to incremental traffic shifting, final cutover and retiring the old gateway.

## What it bought

Inturi reports zero customer-facing incidents across millions of requests and around a 20% reduction in compute cost, mostly from independent scaling: no more scaling the whole Ruby stack to serve lightweight auth checks. A vendor-supported gateway took over security patches, and mean time to recovery dropped with automated deployments and rollbacks.

## Who should watch

Anyone facing a project to replace the thing everything goes through: gateways, auth services, API layers. His closing point is that the pattern is not gateway-specific; it applies to any backend REST migration where the old system's behaviour is the only real spec.

## Related Conf42 talks

- [Ryan Vila on feature flags as a cloud-native migration safety net](https://www.conf42.com/Cloud_Native_2026_Ryan_Vila_feature_flags_migration) at Conf42 Cloud Native 2026, another way to make a cutover reversible.
- [Wenchao Xiang on Kong Gateway performance and best practices](https://www.conf42.com/DevOps_2024_Wenchao_Xiang_kong_gateway_performance_enhancement) at Conf42 DevOps 2024, for life after the cutover.
- [Victor Lyuboslavsky on modularising a 10-year monolith](https://www.conf42.com/Golang_2026_Victor_Lyuboslavsky_modularizing_year_monolith) at Conf42 Golang 2026.

[Watch Kalyan Inturi's talk](https://www.conf42.com/DevOps_2026_Kalyan_Inturi_availability_migration_gateways)

[Watch the talk on YouTube](https://youtu.be/SPLlxgP1wYQ).

## Watch the talk

[Zero-Downtime by Design: High-Availability Migration Patterns for Modern Gateway & Platform Engineering](https://www.conf42.com/DevOps_2026_Kalyan_Inturi_availability_migration_gateways) at Conf42 DevOps 2026.
