# Four layers and a few algorithms keep APIs up at billions of requests

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/scaling-apis-billions-four-layer-framework

In short: Disney's Nikhil Kokal at Conf42 DevOps 2026 on edge caching, request coalescing, distributed rate limiting, sharding and tail-based tracing.

Ten thousand requests for the same uncached item arrive in the same instant. Without help, that is ten thousand database queries and a database that will not be answering the ten thousand and first. At Conf42 DevOps 2026, Nikhil Kokal, a software engineering manager at The Walt Disney Company (previously Google and Salesforce), walked through the architectures and algorithms that keep APIs fast past the billion-request mark, drawing on ad platforms that handle over 200 billion annual impressions.

It is a dense, well-organised survey, closer to a reference card than a war story.

## Scaling hits a coordination wall

His starting point: vertical scaling has physical limits, and horizontal scaling done naively adds coordination overhead. Past some node count, service discovery, health checks and state sync start costing more than the work. He nods to Netflix's edge caching and adaptive streaming, Uber's geo-sharding to keep one city's surge from becoming everyone's noisy neighbour, and RevenueCat's request coalescing.

## The edge: the fastest request never reaches you

Layer one is the edge, and the main lever is cache key design. Too specific and your hit rate collapses; too broad and you serve stale data. Segment keys by user class, geography or device type. Use stale-while-revalidate so an expired entry is served immediately while a background fetch refreshes it, and adaptive TTLs that stretch when the backend is under load. Kokal says the combination can cut origin traffic by 95%.

## Coalescing and rate limiting are reliability tools

Back to that thundering herd: the single-flight pattern marks the first miss as in flight, queues every later request for the same key, and broadcasts the one database result to all of them. One query instead of ten thousand. He calls it a reliability insurance policy, and it is the cheapest one in the talk.

At the gateway layer, the token bucket allows bursts (handy when a web app loads 20 resources at once) while the leaky bucket enforces a smooth rate for fragile legacy downstreams. The hard part is global: a 1,000-requests-per-minute limit across 50 data centres. His answer is local-first counting with periodic sync to a central Redis-style cluster, trading a little accuracy for local speed.

## Data and services: shard well, break circuits early

Multi-region active-active beats active-passive: geo-DNS sends users to the nearest healthy region, each region keeps enough data to serve requests if the cross-region link is cut, and CRDTs merge concurrent profile updates without human help. Consistent hashing with virtual nodes lets you add or remove database nodes without remapping everything, and geographic sharding often doubles as data-residency compliance. A service mesh such as Envoy or Istio handles mTLS, retries with exponential backoff and circuit breakers that stop the death spiral of retries hammering a failing service.

## Observe failures, not everything

At this volume, logging everything would cost more than compute. Tail-based tracing buffers each trace and keeps it only if the request failed or ran slow (he uses 200 ms as the example), giving full visibility into failures while storing a fraction of the data. Predictive autoscaling then pre-provisions capacity from historical traffic, because reactive scaling at 70% CPU arrives after the spike.

## Who should watch

Backend and platform engineers whose traffic is growing faster than their architecture, and anyone preparing for a live event or a viral moment. If you already run all of this, the closing look ahead (energy-aware elasticity, chasing P99.99 rather than P99) is still worth the last few minutes.

## Related Conf42 talks

- [Rehana Sultana Khan on AI-driven rate limiting for scalable, secure, cost-efficient APIs](https://www.conf42.com/JavaScript_2025_Rehana_Sultana_Khan_rate_limiting_cost) at Conf42 JavaScript 2025.
- [Shailin Saraiya on building self-healing cache infrastructure](https://www.conf42.com/Platform_Engineering_2025_Shailin_Saraiya_cache_millions_latency) at Conf42 Platform Engineering 2025.
- [Santosh Nikhil Kumar on API design for fault-tolerant, data-intensive distributed systems](https://www.conf42.com/Python_2024_Santosh_Nikhil_Kumar_api_design_scalable_distributed_systems) at Conf42 Python 2024.

[Watch Nikhil Kokal's talk](https://www.conf42.com/DevOps_2026_Nikhil_Kokal_apis_scalability_reliability)

[Watch the talk on YouTube](https://youtu.be/8HFX9l0T3_c).

## Watch the talk

[Scaling APIs to Billions: Architectures and Algorithms for Extreme-Scale Reliability](https://www.conf42.com/DevOps_2026_Nikhil_Kokal_apis_scalability_reliability) at Conf42 DevOps 2026.
