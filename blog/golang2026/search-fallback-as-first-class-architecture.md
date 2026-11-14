# A 200 with zero results is still an outage. Design the fallback first

Conf42 Blog, 2026-05-08, updated 2026-11-09. https://www.conf42.com/blog/golang2026/search-fallback-as-first-class-architecture

In short: Hima Bindu Yanala of eBay at Conf42 Golang 2026 on resilient self-service search in Go, with fallback indexes, circuit breakers, bulkheads and user signals.

The most dangerous search failure returns HTTP 200. At Conf42 Golang 2026, Hima Bindu Yanala, software engineer at eBay, argued that self-service search fails quietly, with empty or degraded results that dashboards call healthy, and that the fix is a fallback path designed from day one rather than patched in after each incident.

Self-service search is often the first line of customer support. When it works, people solve their own problem. When it silently returns nothing, the user just concludes the platform did not help, and every degraded query can turn into a support ticket, a lost sale or a frustrated customer. Her shorthand for it: empty does not always mean correct.

## Fallback should be engineered, not improvised

Hima describes the familiar history of fallback logic: an incident, a patch, another incident, another rule, until fallback is a pile of reactive fixes. Distributed systems surface new failure modes faster than patches keep up. Her alternative is to treat fallback as a first-class pattern with its own capacity, routing, freshness, monitoring and user experience. In her words, "fallback should be engineered, not improvised."

## Fan-out turns rare outliers into the common case

Sending one query to many shards buys parallelism and widens the failure surface. If one shard is slow, the whole response waits, which is why tail latency matters more than averages: users experience their own request, not the mean. Goroutines make fan-out easy, and that is the trap. Hima lists what a resilient Go search service needs at every fan-out boundary: context deadlines, timeout budgets, cancellation, worker limits and explicit rules for partial results.

## Four layers, none of them trusted alone

The architecture is defence in depth:

- **Distributed retrieval** sends queries to the primary shards.
- **A circuit breaker** watches latency, errors and timeouts. Closed means normal traffic; past a threshold it opens and routes to the fallback; half-open sends limited probes to check whether the primary has recovered.
- **A fallback index** built for failure, not a shrunken copy of the main one: lightweight, fast, isolated, holding enough high-confidence data (popular queries, common help articles, recent successful results, curated mappings) to keep the user moving.
- **Bulkheads** protect fallback capacity with separate goroutine pools, connection pools, semaphore limits and context cancellation. If the primary path can eat all the CPU, memory and connections, the fallback exists on the diagram and nowhere else.

The bulkhead name comes from ship design: flood one compartment and the ship stays afloat. A good metaphor for a system whose job is to stay above water while one shard is underwater.

## Zero results deserve their own defence

Before falling back, Hima layers query relaxation: loosen strict filters, correct spelling, expand terms, apply synonyms. Query logs drive the synonym work, since a query that often returns nothing, or that users immediately reformulate, is telling you about a vocabulary gap. She warns that broad synonyms cost precision, so tuning has to be careful. AI shows up here in a deliberately practical role: clustering similar queries, detecting intent, suggesting synonym candidates, not as a buzzword bolted on.

## Watch the users, not just the shards

The closing section connects two kinds of metrics. Infrastructure tells you p99 latency, timeouts, shard failures, breaker trips and resource use. Users tell you zero-result frequency, reformulation rate, abandonment, escalations and clicks. Support tickets are lagging indicators; rising tail latency, more breaker trips and spikes in zero-result rates are leading ones, and they can trigger fallback routing and alerts before customers notice. Her goal: users should not notice the incident before the system has already responded safely.

## Who should watch

Engineers who own search, recommendations or any fan-out read path in Go will get a clean checklist. It is pattern-level rather than code-level, so bring your own implementation of the breaker and bulkheads.

## Related Conf42 talks

- [Siddharth Pratap Singh on search privacy and performance](https://www.conf42.com/Golang_2025_Siddharth_Pratap_Singh_search_privacy_performance) at Conf42 Golang 2025
- [Sergey Polyashov on scalable recommendation and search](https://www.conf42.com/Machine_Learning_2025_Sergey_Polyashov_recommendation_search_scalable) at Conf42 Machine Learning 2025
- [Ajitha Buvanachandran on agentic multi-source search](https://www.conf42.com/JavaScript_2025_Ajitha_Buvanachandran_agentic_search_multi) at Conf42 JavaScript 2025

[Watch Hima Bindu Yanala's talk](https://www.conf42.com/Golang_2026_Hima_Bindu_Yanala_designing_resilient_self)

[Watch the talk on YouTube](https://youtu.be/br7vxrK72Dk).

## Watch the talk

[Designing Resilient Self-Service Search in Go: From Failure Modes to Intelligent Fallback Architectures](https://www.conf42.com/Golang_2026_Hima_Bindu_Yanala_designing_resilient_self) at Conf42 Golang 2026.
