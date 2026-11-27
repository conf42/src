# Shard your AI service, but keep the conversation state central

Conf42 Blog, 2025-11-06, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/shard-ai-services-session-affinity

In short: Rahul Thakur of Salesforce at Conf42 Prompt Engineering 2025 on sharding AI services across zones, with routing, session affinity and migration.

A single deployment serving all your LLM traffic is one bad node away from an outage. At Conf42 Prompt Engineering 2025, Rahul Thakur, Lead Member of Technical Staff at Salesforce, made the case for running AI services as many independent shards behind a metadata-aware router, with compute sharded and conversation state kept in a central store.

It is a short, design-level talk: no benchmarks or code, but a clear component list you can hold your own architecture against.

## Why AI traffic is awkward

Rahul starts with what makes AI services different from a typical stateless API. Traffic is extremely variable. Conversations are stateful, so you carry context and customer settings between requests. Some requests need far more resources than others. And failures arrive unannounced. Put all of that on one deployment and you get bottlenecks, resource contention and a single point of failure.

## The pieces of a sharded AI service

His proposal splits traffic across shards that each serve a share of requests, with smart routing and failover on top. The components:

- **AI service shards**, each working independently.
- **A metadata service** that knows every shard and its dependencies. This is the brain of the setup.
- **A routing layer** that sends each request to the right shard.
- **Multi-zone placement**, so losing one availability zone does not take the service down.
- **State management**, because conversations carry context.
- **Observability**, which matters more once you are debugging across many shards instead of one.

## Affinity, then load, then priority

Routing gets the most detail. The first rule is session affinity: the same user should land on the same shard every time, and the metadata service tracks which shard already serves them. Next, if some shards are overloaded, the router steers new traffic to quieter ones. Priority routing can sit on top, keyed on subscription tier or workload type, and geographic routing sends users to nearby shards.

## Shard the compute, not the context

The design choice to remember is about state. Rahul keeps conversation context in a centralised database while the compute is sharded. When a shard misbehaves and a conversation has to move, the migration is a short sequence: retrieve the state, pick a new shard, update the routing, and optionally pre-warm. Because the context never lived on the failed shard, there is nothing to rescue from it.

That is the part of the talk most likely to save you a postmortem. Sticky sessions without a plan for moving them are a pager waiting to go off.

## Scaling signals

For scaling he lists horizontal (more shards), vertical (bigger shards where one shard naturally carries more load), capacity reservation, and cost optimisation through reserved capacity. Autoscaling triggers include request queue depth, latency thresholds, predictive models trained on past usage, and cost-aware triggers that retire underused shards. Health checks per shard, disaster recovery and automatic failover round it out.

The abstract sets the goal at 99.99% uptime; in the talk Rahul describes the payoff as getting close to full availability, independent scaling and lower cost from right-sizing each shard. His rollout advice is to build a few shards first, confirm that scale-up, scale-down and the metadata service all work, and only then expand.

## Who should watch

Backend and platform engineers who own an LLM-backed service that has outgrown one deployment, or who are designing one and want the failure modes on the table early. If you already run cell-based architecture, this will feel familiar, applied to stateful AI chat.

## Related Conf42 talks

- [Andrew Robinson on fault isolation with shuffle sharding](https://www.conf42.com/Site_Reliability_Engineering_2021_Andrew_Robinson_fault_isolation_shuffle_sharding) at Conf42 SRE 2021, the classic way to limit blast radius.
- [Trista Pan on sharding and scaling out traditional databases on Kubernetes](https://www.conf42.com/Cloud_Native_2023_Trista_Pan_automatically_shard_scaleout_databases_kubernetes), for the state side of the story.
- [Aleksander Iskhakov on sharded synchronization in write-heavy systems](https://www.conf42.com/DevOps_2025_Aleksander_Iskhakov_sharded_synchronization) at Conf42 DevOps 2025.

[Watch Rahul Thakur's talk](https://www.conf42.com/Prompt_Engineering_2025_Rahul_Thakur_infrastructure_resilience_scale), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/jIqiojcliTQ).

## Watch the talk

[Prompt-Driven Infrastructure: Sharding AI Services for Scale & Resilience](https://www.conf42.com/Prompt_Engineering_2025_Rahul_Thakur_infrastructure_resilience_scale) at Conf42 Prompt Engineering 2025.
