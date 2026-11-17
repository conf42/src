# Spanner Graph turns scattered security alerts into one attack story

Conf42 Blog, 2025-09-17, updated 2026-11-09. https://www.conf42.com/blog/im2025/spanner-graph-turns-alerts-into-attack-stories

In short: Pushap Goyal (Google) at Conf42 Incident Management 2025 on modelling security incidents as a graph in Spanner Graph, with TrueTime keeping the timeline honest.

A security incident is a graph whether your tooling admits it or not: a user touched a machine, the machine talked to an IP, a process spawned another process. At Conf42 Incident Management 2025, Pushap Goyal, a software engineer at Google, argued that investigators should store it that way, in Spanner Graph, so the questions responders ask first (how far did this spread, and in what order) become queries rather than an afternoon of dashboard archaeology.

It is a short, architecture-level talk, and Pushap opens with a disclaimer that it reflects his own experience and public information rather than an official Google position. Treat it as a well-organised map of the idea, not a product walkthrough.

## Four ways traditional incident tooling lets you down

Pushap sorts the pain into four buckets. Data is fragmented across systems that were never meant to be joined. Every system stamps events with its own clock, so reconstructing the forensic timeline is guesswork. Relational and log-centric models miss the relationships between entities. And the gap gets filled by people: he describes SRE engineers correlating dashboards by hand, which is slow and leaks detail.

The outcome is the familiar one. Detection takes longer, investigations end incomplete, and the operational bill grows.

## Nodes, edges, properties: the incident as a data model

The graph model is simple to state. Nodes are users, machines, IP addresses and processes. Edges are the relationships between them: accessed, created, communicated with. Properties carry the context, such as timestamps, severity and classification. Put network, application, endpoint, cloud and identity data into one model and you get a single semantic layer you can query across, instead of five consoles you alt-tab between.

From there the investigation patterns fall out naturally. Traverse outward from the breach point and you have the blast radius. Follow edges through systems and you have the lateral movement path. Look for links between events that looked unrelated and you find the connections traditional tools miss.

## Why Spanner specifically: the clock

The interesting part of the pitch is time. Spanner's TrueTime gives globally consistent timestamps with bounded uncertainty, so there is a known maximum skew between events in different regions and their order can be trusted. For incident forensics that is the whole game: an attack timeline where step three appears before step two is worse than no timeline at all.

Pushap also points out that Spanner Graph sits on the same database you might already use for transactional workloads, with Spanner's horizontal scaling and automatic sharding and replication, so the security graph does not have to be a separate island.

The query side covers what responders reach for: path analysis between compromised assets, pattern matching, centrality measures to find critical assets and choke points, and community detection to group related events into one campaign.

## The boring parts that decide whether it works

The implementation slide is the most practical one: collect from every source, normalise, fit the data into the graph model, store it, then investigate. He flags three design challenges up front. Schema design is a trade-off between how many entity and relationship types you model and how fast queries run. Ingestion means choosing real-time or batch and handling out-of-order events. And query performance needs tuning, planning or caching to keep responses inside your threshold. Anyone who has watched a graph query fan out across a supernode will nod at that last one.

## Who should watch

Security engineers and incident responders who spend investigations stitching logs together, and platform teams deciding where security telemetry should live. If you want benchmarks or a live demo, this is not that talk; it is the case for the model and the checklist for building it.

## Related Conf42 talks

- [Advancing Financial Fraud Detection with Graph Databases](https://www.conf42.com/Machine_Learning_2025_Venkateswarlu_Boggavarapu_fraud_detection_db_graph) by Venkateswarlu Boggavarapu, the same graph thinking pointed at fraud rings.
- [How AI can enhance digital forensic analysis and evidence collection](https://www.conf42.com/DevSecOps_2025_Victor_Agboola_forensic_ai_analysis) by Victor Agboola, on the evidence side of the investigation.

[Watch Pushap Goyal's talk](https://www.conf42.com/Incident_Management_2025_Pushap_Goyal_graph_spanner_security)

[Watch the talk on YouTube](https://youtu.be/A43DG52tAvQ).

## Watch the talk

[Accelerating Incident Response with Distributed Graph Technology: Leveraging Google Spanner Graph for Complex Security Incident Investigation](https://www.conf42.com/Incident_Management_2025_Pushap_Goyal_graph_spanner_security) at Conf42 Incident Management 2025.
