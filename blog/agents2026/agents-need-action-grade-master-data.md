# Your agent did nothing wrong. Your master data lied to it

Conf42 Blog, 2026-09-11, updated 2026-11-09. https://www.conf42.com/blog/agents2026/agents-need-action-grade-master-data

In short: Vishwak Thatikonda (Starbucks) at Conf42 AI Agents 2026: why MDM built for dashboards breaks under agents that act, and the action-grade design that fixes it.

A replenishment agent placed about 9,400 duplicate orders over two days, worth roughly $41,000, and not one line of agent code was at fault. That anonymised incident opens the Conf42 AI Agents 2026 talk by Vishwak Thatikonda, Lead Engineer at Starbucks, and his argument follows from it: master data management built for reporting can't safely feed agents that take actions, so it has to be rebuilt as an action-grade layer.

## Act three has no human in front of the data

He frames the history of enterprise data in three acts. First the data observed (dashboards), then it recommended (churn scores, reorder suggestions), and now it acts: agents place the reorder and issue the retention offer with nobody reviewing each decision. In the first two acts, bad data produced a bad chart that a person could catch. In the third, it produces an action that has already happened by the time anyone looks.

The duplicate-orders story shows how small the trigger can be. An improved address normalisation step, a good change on its own, made one store resolve to two golden records. To the agent, two golden records meant two stores, so it ordered opening inventory twice. Every order looked valid on its own, which is exactly why nothing alerted.

## Four failure modes, four principles

He names the ways the substrate breaks: staleness from batch refreshes, near-match identity errors, duplicate entities, and slow drift that never throws an error. Each maps to a principle:

- **Immutability**: append instead of overwrite, so you can reconstruct what the agent saw when it decided.
- **Versioned contracts**: schema, allowed values and freshness guarantees, explicit and versioned at every point an agent reads.
- **Real-time resolution**: identity resolved in milliseconds when the event arrives, not overnight.
- **Event-driven execution**: state changes flow the moment they happen.

The reference system is a master data platform for a global retailer with about 38,000 locations, with a target of resolving an entity end to end in under 200 milliseconds and executing every agent action exactly once.

## Blocking, confidence bands, and refusing to guess

Comparing every incoming record against every existing one is fine for a thousand records and impossible at that scale. The trick is blocking: cheap keys produce a tiny candidate set before any expensive comparison, which in his telling turns a billion comparisons into about five. Matching then combines weighted, explainable signals (name similarity, address geometry, distance, contact fields) and returns a confidence band instead of a yes or no. High confidence auto-merges, low stays separate, and the middle goes to a human. The agent is always told which band it is in.

The stack is deliberately boring: AWS Lambda for stateless resolution that reruns safely, DynamoDB as the golden record store with change streams for capture, and EventBridge as a schema-registered bus that fans changes out to the inventory agent, the orchestration layer and the rewards engine. Idempotency is enforced in three places: deterministic request IDs, conditional writes in DynamoDB, and deduplication windows on the bus. Failures land in a dead-letter queue you can replay, which is how you reconstruct an agent's view of the world when debugging it.

## The demo makes the case

The live demo runs one event stream into two lanes: a legacy last-write-wins setup and the action-grade design, with the same agent on top. A re-registered store ships opening inventory twice on the left and merges on the right. A retried loyalty event credits a member twice on the left and is rejected as already committed on the right. Late, stale snapshots, look-alike customers and a record missing a required field all go wrong on the left and get refused, routed or dead-lettered on the right. A burst of low-confidence merges trips a circuit breaker and pauses the agent.

He also lists three traps: a cache in front of a batch warehouse (fast access to stale truth, which the agent trusts completely), treating data quality as a one-off clean-up project, and over-merging. For an agent that acts, a false merge is worse than an honest duplicate. As a database person might put it, the duplicate is a bug; the false merge is someone else's loyalty points.

## Who should watch

Data architects, platform teams and anyone whose agents write to systems of record. The roadmap (assess, harden, stream, operate) starts with the entities your agents already touch, which makes it easy to begin without a rewrite.

## Related talks

- [Cloud-Native MDM: Kubernetes Orchestration for Enterprise Data Quality at Scale](https://www.conf42.com/Kube_Native_2025_Rahul_Ameria_mdm_quality_orchestration) by Rahul Ameria
- [Data Quality and Validation in ML Pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) by Sunil Kumar Mudusu
- [Building Resilient Data Platforms: Implementing Blockchain-Based Master Data Management](https://www.conf42.com/Platform_Engineering_2025_Chandra_Adapa_data_master_management) by Chandra Adapa

[Watch Vishwak Thatikonda's talk](https://www.conf42.com/AI_Agents_2026_Vishwak_Thatikonda_mdm_data_retail)

[Watch the talk on YouTube](https://youtu.be/44XjL_ncROc).

## Watch the talk

[From Analytics to Action: Re-Architecting MDM for Agentic Enterprise AI](https://www.conf42.com/AI_Agents_2026_Vishwak_Thatikonda_mdm_data_retail) at Conf42 AI Agents 2026.
