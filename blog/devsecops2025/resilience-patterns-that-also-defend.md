# Circuit breakers, backoff and chaos tests are security controls too

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/resilience-patterns-that-also-defend

In short: Raghavendra Reddy Kapu of Akshaya Inc at Conf42 DevSecOps 2025 on fault-tolerance patterns, chaos engineering and queueing maths for secure enterprise systems.

A retry storm and a DDoS look a lot alike from the database's point of view. At Conf42 DevSecOps 2025, [Raghavendra Reddy Kapu](https://www.conf42.com/DevSecOps_2025_Raghavendra_Reddy_Kapu_resilient_system_secure), quality performance engineer at Akshaya Inc, walked through the classic fault-tolerance toolkit (circuit breakers, exponential backoff, redundancy, chaos engineering) and argued that it has to be designed together with security, because a resilience mechanism nobody watches can be turned into an attack.

This is a broad, practical survey rather than one deep idea. If you already run a service mesh with circuit breaking and a chaos programme, much of it will be a refresher. If you are building that muscle, it's a well-organised map with worked numbers.

## Three pressures, one design rule

Kapu names three pressures on distributed systems. Security threats aimed at microservice boundaries, where controls are inconsistent and one vulnerable service can expose the mesh. Cascading failures, where a pool exhaustion or a memory leak in one service turns into timeouts and aggressive retries everywhere. And performance demands, with Black Friday traffic far above baseline and security incidents creating their own spikes.

His design rule is to assume the service will fail and ask how the system handles it, what stops the cascade, and whether recovery is automatic.

## The patterns, with the numbers attached

The circuit breaker gets the most attention. Closed means normal flow. After five consecutive failures, in his example, it opens and callers get a fast "temporarily unavailable" instead of hanging on a dead database. After 30 seconds it goes half-open and lets one or two test requests through; success closes it, failure keeps it open. His before-and-after: without a breaker, a five-minute outage plus a long recovery; with one, the failure is recognised in seconds and recovery happens automatically.

Retries use exponential backoff with jitter. His example doubles the wait from 100 milliseconds upwards, so by the fifth attempt a client has backed off 1.6 seconds, and jitter stops every client retrying at the same instant, the thundering herd. Redundancy comes in active-passive form (primary and standby) and active-active (three payment processors each taking a third, so losing one means slower service, not an outage), plus multi-region deployment for near-zero recovery time.

He also covers the CAP theorem in enterprise terms: partition tolerance isn't optional, so you choose per domain. Money stays consistent even if that means refusing requests; social feeds stay available and tolerate slightly stale data.

## Break it on purpose, one radius at a time

The chaos engineering section is hypothesis-driven. State an expectation, for example that the API keeps serving from the database, more slowly, if the cache cluster goes down; then kill the cache, observe, fix the gap and rerun. His schedule widens the blast radius week by week: a single node, then a network partition between regions, then multiple critical services, and finally a simulated security incident to check that malicious traffic gets detected and blocked. Netflix gets the expected credit for pioneering the practice.

## Observability and maths make the arguments objective

Kapu wants security and performance signals in one place: metrics, centralised logs with security correlation (multiple failed logins from one IP), distributed traces across a checkout that touches seven services, and anomaly-based alerts rather than static thresholds, so a jump in error rate or traffic from an unusual geography gets flagged as a possible attack.

He then brings in Markov chains to model service state transitions and queueing theory to size capacity, so teams can say how many servers a traffic pattern needs instead of guessing. His worked cost example right-sizes an over-provisioned platform while checking availability, p99 latency and error rate after each step.

## Security and resilience have to be designed together

The closing point is the one worth remembering. Fault tolerance has to work in harmony with security controls: an attacker can exploit retry behaviour to amplify a DDoS, so watch your circuit breakers and treat unusual trip patterns as a security signal. His defence-in-depth stack layers network controls, rate limiting, circuit breakers, retries with backoff, health checks with automatic failover, and chaos tests that validate the lot. Blameless post-mortems close the loop: ask why it failed, not who.

## Who should watch

Engineers and SREs moving a monolith-shaped team into microservices, and security engineers who want to understand how reliability patterns change the attack surface.

## Related Conf42 talks

- [Boosting System Resilience with Exponential Backoff](https://www.conf42.com/Rustlang_2024_Suraj_Modi_system_resilience_backoff_computing) goes deeper on the retry maths.
- [Graceful Degradation: Keeping The Lights On When Everything Goes Wrong](https://www.conf42.com/Chaos_Engineering_2023_Tanveer_Gill_graceful_degradation_everything_goes_wrong) covers load shedding when the patterns aren't enough.
- [Self Healing Systems](https://www.conf42.com/Chaos_Engineering_2022_Nick_Hodges_self_healing_systems) extends the automated recovery idea.

[Watch Raghavendra Reddy Kapu's talk](https://www.conf42.com/DevSecOps_2025_Raghavendra_Reddy_Kapu_resilient_system_secure)

[Watch the talk on YouTube](https://youtu.be/sG_nE1W5nA0).

## Watch the talk

[Resilience Engineering for Secure and Fault-Tolerant Enterprise Systems](https://www.conf42.com/DevSecOps_2025_Raghavendra_Reddy_Kapu_resilient_system_secure) at Conf42 DevSecOps 2025.
