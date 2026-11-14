# Airline shopping traffic is mostly repeats, so cache it carefully

Conf42 Blog, 2026-03-11, updated 2026-11-09. https://www.conf42.com/blog/sre2026/airline-ndc-shopping-caching-without-pricing-drift

In short: Mukul Kumar Gaur of Accelya Group at Conf42 SRE 2026 on caching NDC airline offers at scale with freshness rules that stop pricing drift.

Many of the searches hitting an airline's offer engine are the same question asked by different robots a few seconds apart. At Conf42 Site Reliability Engineering 2026, Mukul Kumar Gaur, Senior Principal in Product Management and Product Engineering at Accelya Group, explained how NDC shopping platforms can serve that repeat demand from cache without quoting a price the airline no longer offers.

If NDC is new to you: it is the airline industry's move to offer- and order-based retailing, where offers are built dynamically per request instead of being pulled from static fare filings. That flexibility is exactly what makes every request expensive.

## You are scaling to process repetition

The problem, in his framing, is redundancy. Requests arrive from airline websites, online travel agencies, metasearch sites and automated repricing systems, and a large share are repetitive or near-duplicate searches for the same origin and destination. Meanwhile each one now triggers real-time offer generation: fares, taxes, inventory availability and merchandising rules.

Without caching, the platform recomputes the full offer every time. His phrase for it is that platforms end up scaling infrastructure to process repetition rather than incremental revenue. The bill shows up as latency and cloud cost, and the risk shows up during traffic spikes. The fix is not a bigger engine but recognising repeat demand and reusing work already done.

## Pick the cache by how fast the price moves

The talk lays out three strategies, with the trade-off stated plainly: performance versus flexibility versus pricing freshness.

- **Full offer caching** stores the complete offer as generated and returns it instantly on a matching request. Fastest option, best for markets where prices are fairly stable or the cache window is tightly controlled.
- **Hybrid anchored caching** keeps stable parts (say, the fare structure) and recalculates the volatile parts, such as availability and dynamic price adjustments, per request.
- **Partial component caching** caches individual pipeline pieces independently, such as tax calculations, fare rules or schedule data. Less speed-up, less stale-data risk.

His recommendation is to layer them rather than choose one. Most real platforms have markets in all three categories.

## Governance is what keeps a cache honest

The obvious worry is pricing drift: a cached offer that outlives the inventory or price it was built on. The abstract also names the downstream pain, settlement discrepancies, which is the kind of bug finance finds weeks after engineering shipped it.

The controls he lists are freshness thresholds that cap how long an offer stays valid, real-time invalidation triggers that evict cached data when pricing or availability changes, special handling for high-elasticity markets, and elastic controls that hold consistency under spikes. The abstract adds request quality scoring and partner-level cache controls, so a noisy aggregator does not get the same treatment as a channel that converts.

Monitoring closes the loop: BI dashboards on cache hit rates, system performance and pricing alignment, plus automated alerts when discrepancies appear. Cache invalidation is famously one of the two hard problems; this talk is mostly about making its failures visible fast.

## Peak sales are the real test

His worked scenario is a high-demand promotion, when shopping traffic can jump within minutes. Without caching, every request hits the offer engine and performance degrades exactly when the airline most wants to sell. With layered caching, most of those requests are served from offers already computed, and the engine keeps capacity for the ones that need fresh pricing.

## Who should watch

Engineers on travel, e-commerce or any dynamic pricing system where reads vastly outnumber purchases. It is a conceptual talk with no code or benchmark numbers, so expect a clear mental model and a checklist (layered caching, explicit invalidation policy, observability on pricing accuracy) rather than an implementation.

## Related Conf42 talks

- [Distributed Caching & Queueing in the Cloud](https://www.conf42.com/Cloud_Native_2025_Wisdom_Matthew_distributed_caching_queueing) by Wisdom Matthew.
- [What's next in the HTTP caching world](https://www.conf42.com/Cloud_Native_2023_Sylvain_Combraque_http_caching_world) by Sylvain Combraque.
- [Building Resilient AI Pricing Platforms: Engineering Real-Time Decision Systems at Scale](https://www.conf42.com/Platform_Engineering_2025_Amaresh_Sahoo_pricing_decision_time) by Amaresh Sahoo.

[Watch Mukul Kumar Gaur's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Mukul_Kumar_Gaur_ready_shopping_caching) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/Ozgal9TX72g).

## Watch the talk

[SRE-Ready NDC Shopping: Caching at Scale Without Pricing Drift](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Mukul_Kumar_Gaur_ready_shopping_caching) at Conf42 Site Reliability Engineering (SRE) 2026.
