# Stream security findings fast, then reconcile them with anti-entropy

Conf42 Blog, 2026-09-11, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/anti-entropy-keeps-security-findings-honest

In short: Rahul Kizhakkepachilamakol of AWS at Conf42 DevSecOps 2026 pairs streaming with Merkle trees, read-repair and hinted handoff so findings don't vanish.

A vulnerability finding that silently disappears in transit can be as dangerous as an outage, and a streaming pipeline is very good at losing things quietly. At Conf42 DevSecOps 2026, Rahul Kizhakkepachilamakol, Principal Software Engineer at Amazon Web Services working on the security data platform behind vulnerability management for AWS and Amazon, explained how his team gets speed and correctness at once: stream every finding, and run an anti-entropy layer beside the stream that compares, detects, repairs and verifies.

It's a compact architecture talk that borrows well-known tricks from distributed databases and points them at security data.

## Late findings are open windows

Rahul's case for latency is straightforward. A finding only has value once it reaches the team that can act on it. Every delay stretches exposure time and slows detection, triage, incident response and containment. It also creates compliance risk, which matters a lot when your customers build their own compliance on top of yours, and it piles up a remediation backlog for security engineers.

The platform has three requirements that pull against each other: fast delivery no matter how distributed the cloud is (AWS runs in 40-plus regions), high availability even when parts of that cloud fail, and strong correctness in the data it hands out.

## Streaming for speed, anti-entropy for truth

The fast path is streaming. Scanner results are emitted as events the moment they're produced, enriched with business logic (severity, asset context, ownership), run through further risk detection and delivered to the people who remediate. Streaming keeps the pipe fast, but unlike a synchronous call it gives you no built-in guarantee that what the producer sent is what the consumer got.

So a second path runs in parallel. Between each producer and consumer, which are often systems owned by different teams, a feed goes to a reconciliation system. It follows the classic anti-entropy loop: compare the data sets, detect what's missing or wrong, repair it, then verify that producer and consumer now agree.

## Hash attributes, not just IDs

Comparing everything at this volume would be ruinously expensive, so the reconciler partitions data into Merkle trees as it collects it. If the hashes match, there's nothing to inspect; only a mismatch sends it deeper.

The detail that makes this security-grade is where the hashing happens. An existence check isn't enough, because a record can be present in both systems and still be wrong. Rahul's example: system A says a vulnerability is critical, system B has the same record at medium. Matching IDs would call that consistent. Hashing at the attribute level catches missing or null fields and changed ownership or context, so the layer finds silent corruption as well as missing findings. If you've ever trusted a dashboard because the row counts matched, this is the paragraph to reread.

## Two repairs, and a receipt for each

Repairs borrow two database techniques. Read-repair re-drives the correct record from the producer to a consumer that holds a wrong version. Hinted handoff covers a consumer that is down: the reconciler waits for it to recover and then replays what it missed, so an infrastructure blip doesn't become a permanent hole in security data.

In a regulated environment the repair itself has to be auditable, because automated corrections without records are their own compliance risk. Every reconciliation action is captured: the restored finding identifier, the source of truth used, the action taken, when it happened and the verification result.

## Who should watch

Platform architects and security engineers who own a findings pipeline, and anyone running event-driven systems where "eventually" needs a bound. The talk stays at architecture level, so don't expect code or benchmark numbers; do expect a pattern you can lift into any producer-consumer pipeline where a lost or mangled record has consequences.

## Related Conf42 talks

- [Modern Database Architectures: From SQL to NoSQL and Distributed SQL](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Andrei_Manakov_tradeoffs_distributed_nosql) by Andrei Manakov of ShareChat at Conf42 SRE 2025.
- [Platform Engineering for FinTech: Database Sharding, Replication & Scale](https://www.conf42.com/Platform_Engineering_2025_Karthickram_Vailraj_sharding_replication_database) by Karthickram Vailraj of Charles Schwab at Conf42 Platform Engineering 2025.
- [Keep Calm and Run on AWS: Engineering Compliance Without Abandoning Your Stack](https://www.conf42.com/Cloud_Native_2026_Dmytro_Hlotenko_distributed_systems_resilience) by Dmytro Hlotenko of Sage Austria at Conf42 Cloud Native 2026.

[Watch Rahul Kizhakkepachilamakol's talk](https://www.conf42.com/DevSecOps_2026_Rahul_Kizhakkepachilamakol_distributedsystems_vulnerabilities_latency) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/faGGNQfMS2g).

## Watch the talk

[Anti-Entropy Mechanisms for Single-Digit Minute Latency in Cloud-Scale Security Platforms](https://www.conf42.com/DevSecOps_2026_Rahul_Kizhakkepachilamakol_distributedsystems_vulnerabilities_latency) at Conf42 DevSecOps 2026.
