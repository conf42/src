# Treat the Cache as Self-Healing Infrastructure, Not a Tweak

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/roku-self-healing-cache-platform

In short: Roku's Shailin Saraiya at Conf42 Platform Engineering 2025 on layered, ML-tuned caching that heals itself and stays simple for developers.

Caching usually gets filed under small optimisations to tune later. Shailin Saraiya, Senior Software Engineering Manager at Roku, spent his Conf42 Platform Engineering 2025 talk arguing the opposite: treated as a platform, caching becomes a self-healing infrastructure component that cuts latency, protects databases and lets traffic grow without the on-call rota growing with it.

His opening lesson sets the tone: anyone can provision more servers, but real scale comes from systems that are resilient, adaptive and simple for developers to use.

## Static TTLs are where the pain starts

The problem list will be familiar to anyone who has run a busy service. Databases hit connection limits at peak. APIs that were fast at low load start timing out. Teams lose days firefighting instead of shipping. Traditional caching helps a bit, but static TTLs either expire data too soon (wasted recomputation) or keep it too long (stale answers). Scaling is manual and reactive, and observability is poor enough that users notice before engineers do.

## Five principles for a cache that runs itself

Shailin's target state rests on five ideas:

1. **Self-service**: adding caching to an API should be a config change or an annotation, not weeks of distributed-systems work.
2. **Intelligence**: when a launch in Europe sends traffic surging at 3 AM local time, the system rebalances on its own.
3. **Self-healing**: when a node dies or a replica lags, the platform promotes replicas, reroutes and rebuilds state from logs instead of paging someone at 2 AM.
4. **Observability**: automation with dashboards, metrics and recommendations, never blind.
5. **Effortless scaling**: double the traffic should not mean double the operational work.

## Layers, events and a mesh

The architecture stacks four caching tiers: database caches, a distributed key-value tier (Redis is his example), in-memory application caches, and edge caches near users. Four principles hold it together: service-mesh integration for discovery, retries and circuit breaking; event-driven updates from streams rather than polling, which enables async warming and state reconstruction from event logs; directory-based coherency for invalidation across thousands of nodes; and the layering itself, so no single tier becomes the bottleneck.

Implementation follows the same theme. Cache infrastructure is declared and rolled out through GitOps with zero downtime. Developers get annotation-style APIs. Failures are detected in milliseconds and handled by replica promotion and rerouting.

## Let models set the TTL

The ML section is the distinctive part. Predictive warming loads data before the request arrives, based on history, popularity and time of day. Adaptive TTLs adjust expiry to how volatile the data is. Anomaly detection catches odd traffic, potential cache-poisoning attempts and degradations early. He mentions neural networks for access prediction, reinforcement learning to tune eviction for hit ratio, and clustering to group workloads for targeted warming.

At the edge, the hard parts are coherency (eventual consistency, vector clocks, read repair), small nodes (dynamic sizing, smarter eviction, compression) and partitions, where edge caches keep serving and reconcile later.

Observability goes past p50/p95/p99 and hit ratios into insight: flagging that hit rates fell after a deploy, or suggesting an endpoint worth caching. The abstract quotes an 83% latency drop, 6.5x user growth and 97% hit rates; the talk itself stays at the level of patterns, so watch it for the design rather than a benchmark breakdown.

## Who should watch

Backend and platform engineers whose databases sweat at peak, and anyone building caching as a shared service. The culture section (shared ownership, data-driven decisions, incremental migration with legacy support) is short but on point: hot keys are solvable, organisational resistance takes longer.

## Related Conf42 talks

- [Rafal Leszko: Architectural Caching Patterns for Kubernetes](https://www.conf42.com/Cloud_Native_2021_Rafal_Leszko_architectural_caching_patterns_kubernetes).
- [Sylvain Combraque: What's next in the HTTP caching world](https://www.conf42.com/Cloud_Native_2023_Sylvain_Combraque_http_caching_world), for the edge tier.
- [Nick Hodges on self-healing systems](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems).

[Watch Shailin Saraiya's talk](https://www.conf42.com/Platform_Engineering_2025_Shailin_Saraiya_cache_millions_latency)

[Watch the talk on YouTube](https://youtu.be/HgmBVS06BDc).

## Watch the talk

[Building Self-Healing Cache Infrastructure: How Platform Engineering Reduced Latency by 83% While Scaling to Millions](https://www.conf42.com/Platform_Engineering_2025_Shailin_Saraiya_cache_millions_latency) at Conf42 Platform Engineering 2025.
