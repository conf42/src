# Put the API gateway at the edge and keep the data near the database

Conf42 Blog, 2025-03-06. https://www.conf42.com/blog/cloud2025/api-gateway-at-the-edge-data-stays-home

In short: Adrian Machado of Zuplo at Conf42 Cloud Native 2025 on which parts of an API belong at the edge, the data trade-offs, and a slow D1 demo debugged live.

Rejecting a missing API key should not require a round trip from Japan to Texas. At Conf42 Cloud Native 2025, [Adrian Machado](https://www.conf42.com/Cloud_Native_2025_Adrian_Machado_api_network_distribution), staff engineer at Zuplo, made the case for running the compute-heavy, data-light parts of an API (auth, validation, rate limiting, caching) on the worldwide edge, while the services that touch your database stay close to it.

It is an honest talk. Machado spends as much time on why the edge is not a silver bullet as on why APIs suit it, and his own demo comes out slower than the API it was copying, which he then debugs on stage.

## What "the edge" buys you, and what it costs

A typical API lives in one region, so a user far away pays for every undersea hop, sometimes adding up to seconds. CDNs fixed this for static files. Edge functions, pushed by Cloudflare, Vercel and others through the WinterCG working group, do the same for code: lightweight function-as-a-service runtimes deployed at the CDN's points of presence, typically with a zero millisecond cold start.

The trade-offs are real. Cloudflare's runtime is JavaScript plus some WebAssembly, so Python or Rust services need a Wasm build. Node.js compatibility is partial, and anything that needs raw TCP probably won't work. Bundle sizes are capped. Libraries built for the browser usually run, because the edge is essentially V8.

## Your data is the catch

The bigger problem is that compute is global and data usually isn't. A CRUD call from an edge function pays the edge-to-database round trip, which can be slower than co-locating function and database in one region. Thousands of edge invocations can also exhaust your database connections.

Machado lays out three answers in order of effort:

- **A database proxy** such as Prisma Accelerate or RDS Proxy, which pools connections and can cache, without changing the database.
- **A globally distributed data store** like Cassandra or CockroachDB, or read replicas near the edge, at the price of consistency: async writes give stale reads, sync writes give slow ones.
- **Data that lives at the edge**, such as Cloudflare R2 for blobs, D1 or Upstash for per-region SQLite (handy for GDPR locality), or edge key-value stores for configuration that rarely changes.

## Why APIs are a good fit

Public API users can be anywhere, because you have no control over where your customers deploy. And a lot of API work is compute, not data: authentication and authorisation (especially API keys you validate yourself), logging, request validation with libraries like Ajv or Zod, bot and bad-actor filtering, rate limiting and caching.

Rate limiting at the edge has a bonus effect he points out: rejected requests never reach your central services, which frees them up for legitimate traffic and soaks up some DDoS along the way. His recommended architecture follows from that. Run an edge API gateway for those concerns, and host the actual microservices near the data, ideally replicated across a few regions. The gateway layer is JavaScript or Wasm; your services can be Django or anything else.

## The demo that came out slow

The demo is an ATM locator, a good edge use case because ATM locations are regional, rarely written, and very cacheable. As a baseline he calls Capital One's Nessie hackathon API, which answers in roughly 100 milliseconds. His version uses a Next.js site on Vercel, a Zuplo edge function and route, an edge cache, and Cloudflare D1 holding ATM data he gathered from Capital One's dataset.

The first call took about 1.3 seconds. Rather than hide it, he walks the debugging checklist: is the D1 query itself slow (a latitude/longitude index would help), is the database placed too far away, or is gateway latency to blame. His most likely suspect is placement, since D1 won't necessarily put a low-traffic hobby database close to you, and the practical fix is to cache at the edge so the round trip happens as rarely as possible. It is a better lesson than a perfect demo would have been.

## Who should watch

API engineers modernising a public API, CTOs thinking about API developer experience, and anyone whose global users are paying latency for work that never needed the database. It is a high-level talk, not an introduction to serverless and not a deep tuning session.

## Related Conf42 talks

- [Hono: Multi-Runtime Web Framework for the Edges](https://www.conf42.com/Cloud_Native_2024_Nikolay_Pryanishnikov_hono_multiruntime_framework) by Nikolay Pryanishnikov (Station Labs) at Conf42 Cloud Native 2024.
- [K8s Gateway API 101](https://www.conf42.com/DevOps_2024_Gregorio_Palama_k8s_gateway_api) by Gregorio Palama (Lutech) at Conf42 DevOps 2024, the in-cluster view of the gateway layer.
- [Advanced API Design for Scalable and Fault-Tolerant Data-Intensive Distributed Systems](https://www.conf42.com/Python_2024_Santosh_Nikhil_Kumar_api_design_scalable_distributed_systems) by Santosh Nikhil Kumar (ByteDance) at Conf42 Python 2024.

[Watch Adrian Machado's talk](https://www.conf42.com/Cloud_Native_2025_Adrian_Machado_api_network_distribution) or the [YouTube recording](https://youtu.be/HBomddyvQps).

## From Zuplo

Zuplo was a Silver sponsor of Conf42 Cloud Native 2025. The talk uses Zuplo's API gateway, which runs at the edge, for the demo's API route. Machado also maintains RateMyOpenAPI, an open source API governance and scoring tool.

- [Zuplo](https://zuplo.com/): the edge API management platform used in the demo
- [All Conf42 Cloud Native 2025 talks](https://www.conf42.com/cloud2025)

## Watch the talk

[Your API needs to operate on the worldwide edge](https://www.conf42.com/Cloud_Native_2025_Adrian_Machado_api_network_distribution) at Conf42 Cloud Native 2025.
