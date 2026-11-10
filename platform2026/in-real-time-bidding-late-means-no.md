# In real-time bidding, a late answer is a no answer

Conf42 Blog, 2026-10-16, updated 2026-11-09. https://www.conf42.com/platform2026/in-real-time-bidding-late-means-no

In short: Sujan Challa (Samsung Electronics America) at Conf42 Platform Engineering 2026 on building an ad auction platform around a 100 ms latency wall.

When the exchange closes the auction at about 100 milliseconds, a slow bid simply doesn't count. At Conf42 Platform Engineering 2026, Sujan Challa, Senior Software Engineer at Samsung Electronics America working on connected-TV advertising, walked through a real-time bidding architecture built one forced move at a time, each move dictated by that deadline.

His framing is the useful part: treat the latency budget as an architectural constraint, not a performance target, and let it decide where state lives, what waits on what, and what gets dropped.

## Every synchronous hop is a purchase

The naive design (request in, database lookup, bid out) dies on contact. A database call per request multiplies load, and one slow dependency sets the floor for the whole system. Sujan's three opening moves:

1. **Feature cache in front of everything.** User context, campaign and model inputs come from memory. The price is staleness, so expiry, invalidation and source-of-truth recovery are designed up front. Strict consistency is reserved for facts that need it, like budget accounting.
2. **Parallelise the independent waits.** The bidder fans out to user, budget and model lookups at once; the slowest bounded call sets the join time, not the sum.
3. **Scale replicas, not state.** Any healthy stateless bidder can serve any request, so capacity is more replicas in more regions, not a redesign.

His one-line generalisation: under a strict budget, every synchronous hop is paid for in milliseconds, and precomputation plus locality is how you stop paying retail.

## The pod is the unit of correctness

Connected TV adds a wrinkle the web never had: ads arrive in pods, several impressions in one commercial break that must be decided together. Two car ads back-to-back, or the same ad twice in a break, is a failure even when every single auction was correct.

The auction core only understands single impressions. Rather than fork it, the platform decomposes each pod into plain impressions, runs them through the core, and reassembles at the edge, where deal tiers, competitive separation and frequency rules live. Frequency state spans requests, so it sits in shared state at that edge layer. The pattern to steal: rules that span requests belong at the layer that can see the whole unit of work. Push them into the core and the core stops being boring and reusable.

## Degradation is a feature with an owner

The live path has a failure table, and it's a real design document rather than an apology. Cache miss: read the source, repopulate. Slow lookup: use a safe default and continue. Repeated failures: open the circuit. Deadline exhausted: return no bid rather than a late one. Timeouts are a design input; a missing signal is cheaper than a missed auction.

Everything not needed to answer moves off the path. Win, loss and impression events go through pub/sub into logging, billing and training data; models retrain offline and refresh the serving layer. The learning loop improves the live path without standing in it. Observability gets the same treatment: P95, P99 and P999 are the product metrics, but measuring costs budget too, so telemetry is sampled, aggregated at the edge and shipped asynchronously. The live path emits; it never waits to report.

## Who should watch

Anyone running payments, search, recommendations or anything else with a hard latency wall; Sujan's point is that they all converge on the same moves. It's an architecture talk with no code, so it suits tech leads and architects more than someone after a Go profiling session. If your services have timeouts but no defaults, the four closing lessons alone are worth the time.

## Related Conf42 talks

- [Building Self-Healing Cache Infrastructure: How Platform Engineering Reduced Latency by 83% While Scaling to Millions](https://www.conf42.com/Platform_Engineering_2025_Shailin_Saraiya_cache_millions_latency) by Shailin Saraiya (Roku)
- [The Failures You Don't See on Dashboards](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhimanyu_Narwal_failures_dashboards_reliability) by Abhimanyu Narwal (Bloomberg LP)
- [Deploying ML solutions with low latency in Python](https://www.conf42.com/Machine_Learning_2021_Aditya_Lohia_Deploying_ML_solutions_low_latency) by Aditya Lohia

[Watch Sujan's talk](https://www.conf42.com/Platform_Engineering_2026_Sujan_Challa_bidding_latency_constraints)

[Watch the talk on YouTube](https://youtu.be/AocAtwN4hqs).

## Watch the talk

[Platform Engineering for Real-Time Bidding Under Strict Latency Constraints](https://www.conf42.com/Platform_Engineering_2026_Sujan_Challa_bidding_latency_constraints) at Conf42 Platform Engineering 2026.
