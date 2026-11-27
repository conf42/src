# Cascading timeouts - every layer gives up before the one above it

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/cascading-timeouts-fail-fast-recover-faster

In short: Madhavi Bhairavabhatla (Mastercard) at Conf42 MLOps 2025 on cascading timeouts, shorter limits inward so failures surface fast and threads stay free.

Most outages that start slow end badly, and a lot of them start with a timeout someone copied from another service. At Conf42 MLOps 2025, Madhavi Bhairavabhatla, Director of Software Engineering at Mastercard, makes the case for cascading timeouts: every upstream call waits longer than its downstream dependency, so the innermost layer fails first, releases its resources, and the error travels up while the client is still listening.

It sounds like a config detail. In a highly transactional system it decides whether one sick database becomes one bad minute or a full outage.

## Three anti-patterns you probably have

Madhavi starts with the timeouts she sees in the wild. Uniform timeouts use the same value at every layer regardless of who calls whom. Inverted timeouts let an outer service give up before the inner one, so the client gets an error while a downstream thread keeps working on a request nobody is waiting for. Excessive timeouts, the 30-seconds-plus kind, hold threads and connection pools hostage during exactly the incident where you need them back.

The symptoms are the familiar ones: thread pool exhaustion, database connection starvation, slow failure detection and, eventually, cascading service degradation. Her advice before changing anything is to go through incident and latency data and work out how many of your major incidents a bad timeout actually contributed to.

## Shorter as you go in, with a buffer at each step

The rule itself is simple. Timeouts get progressively shorter from the outermost edge inward, and Madhavi's implementation gives each downstream layer at least 500 milliseconds less than the layer above to absorb network latency and processing overhead.

Her worked example runs the whole stack. At the edge, the proxy route gets 3,000 ms and the backend proxy 2,500 ms, with circuit breakers and custom response codes for timeouts. The API gateway gets 2,000 ms with one retry and exponential backoff, enough for a second chance without a retry storm, plus caching of known failure responses. The application layer gets 1,500 ms, sized thread pools and a circuit breaker. At the database, she sets statement timeouts at the connection pool level (HikariCP in her example) and separate query timeouts for reads and writes.

The payoff is predictability. When something breaks, the system fails in a controlled way, which, as she puts it, is what engineers want most in the middle of chaos.

## ML inference needs its own budget

This is where the talk earns its MLOps slot. Model serving does not behave like a CRUD endpoint, so Madhavi separates model loading from inference with distinct timeout strategies, gives batch prediction jobs longer limits than real-time inference, and adds a fallback model for when the primary one times out. A cache of recent predictions keeps the service answering in a degraded state, and each model type gets its own circuit breaker tuned to its resource profile. A GPU-heavy model and a tiny classifier should not share one breaker.

## Measure first, then tune iteratively

Her rollout plan is refreshingly unglamorous. Baseline response times, error codes, thread pool and JVM usage under normal load. Assign preliminary values starting from the innermost layers (databases, caches) and work outward, adding buffer at each step. Deploy incrementally, run performance and chaos tests, then keep adjusting from real production data and incident reviews. Setting the numbers lower is not enough; each layer still needs time to do its real work.

## Who should watch

SREs and backend engineers running multi-tier services, especially anyone putting model inference behind an API gateway. If your timeouts were last reviewed when the service was created, this is a good evening's audit checklist.

## Related Conf42 talks

- [Suraj Modi (Uber) on exponential backoff for system resilience](https://www.conf42.com/Rustlang_2024_Suraj_Modi_system_resilience_backoff_computing), the retry half of the same design.
- [Yamini Rathamsetty and Karthik Akula on the retry storm that ate their budget](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens), what happens when retries in agentic AI go unbounded.
- [Nick Hodges (Rollbar) on self-healing systems](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems) at Conf42 Chaos Engineering 2022.

[Watch Madhavi Bhairavabhatla's talk](https://www.conf42.com/MLOps_2025_Madhavi_Bhairavabhatla_fail_fast_recover) and then go and check what your load balancer timeout is.

[Watch the talk on YouTube](https://youtu.be/6_kUviHU6cU).

## Watch the talk

[Fail Fast, Recover Faster: Harnessing Cascading Timeouts for Scalable System Resilience](https://www.conf42.com/MLOps_2025_Madhavi_Bhairavabhatla_fail_fast_recover) at Conf42 MLOps 2025.
