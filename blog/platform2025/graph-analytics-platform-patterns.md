# When friend-of-a-friend breaks SQL, build a graph platform

Conf42 Blog, 2025-08-11, updated 2026-11-09. https://www.conf42.com/blog/platform2025/graph-analytics-platform-patterns

In short: Muthuselvam Chandramohan of Intuit Mailchimp at Conf42 Platform Engineering 2025 on real-time graph platforms, partitioning, query tuning and backups.

Find every friend of a friend who shares at least three interests with a user, and your relational database starts guessing how many joins you meant. At Conf42 Platform Engineering 2025, Muthuselvam Chandramohan, senior software engineer at Intuit Mailchimp with more than 20 years in data engineering, walked through the architectural decisions behind a graph platform that serves both real-time and analytical queries.

It is the most thorough talk of its kind at the event: partitioning, replication, storage tiers, query tuning, memory, integrations, monitoring and backup, each with the trade-off spelled out.

## Relationships as first-class citizens

The case for graph is multi-hop analysis when you don't know the number of hops in advance. Relational databases force you to assume a depth and write the joins; a graph database stores the relationship itself, so traversals follow edges whose next step depends on the previous result. Social networks, supply chains, fraud and knowledge graphs all look like this.

The platform challenges are threefold: sub-second responses for fraud and cybersecurity, integration with very different producers (microservices, batch pipelines, packaged apps), and scale. Vertical scaling hits a ceiling, so horizontal it is.

## Event-driven in, partitioned underneath

Muthuselvam favours an event-driven architecture with Kafka or another streaming platform feeding the graph. Many graph databases ship Kafka connectors, updates route to the right partition, and you get replay after an outage plus multiple consumers. One stream can feed a fraud graph and a marketing graph, each tuned for its own audience.

For horizontal scale he splits the decision in two. Partitioning (vertex-cut or edge-cut) should follow your query patterns, not your data shape, and not every graph database supports both. Replication ranges from quorum-based eventual consistency, which he considers reasonable because a graph is usually a system of reference rather than the system of record, to leader-follower and Raft-style consensus.

## Storage tiers and query tricks

Storage depends on latency needs: in-memory options such as RedisGraph for sub-second lookups, persistent stores such as Neo4j or Amazon Neptune when durability and recovery matter more, or a graph layer on a NoSQL store you already run.

The query optimisation section is where the graph-specific ideas shine:

- **Early termination**: stop traversing once you have the answer.
- **Bidirectional search**: start from two anchors (a country and an age group) and meet in the middle.
- **Cost-based starting points**: check vertex degree and avoid starting a traversal at a supernode.

Memory tuning follows: vertex and edge pooling to calm the Java garbage collector, compressed representations such as CSR adjacency lists, and splitting hot partitions onto more compute.

## Integration, monitoring, backup

Integrations come in three flavours: change data capture from existing databases, GraphQL as the schema layer in front of the graph (the graph does the heavy traversal, GraphQL presents it), and Spark or Trino connectors for analytics. Monitoring watches query complexity, hot vertex heat maps, and graph-shape metrics such as degree distribution and clustering coefficients. For backup he recommends full graph backups over incremental ones, because interconnected data doesn't split cleanly into change logs.

His closing caution is worth framing: not every use case needs a graph. Know the use case and the target users first.

## Who should watch

Data and platform engineers evaluating graph databases for fraud, identity, recommendations or knowledge graphs. It is long and dense, so it rewards a second screen with notes open.

## Related Conf42 talks

- [Siva Prakash on graph-based monitoring for financial systems](https://www.conf42.com/Observability_2025_Siva_Prakash_financial_anomaly_graph) applies graphs to anomaly detection.
- [Prateek Mittal on knowledge graphs as the backbone of AI-first software delivery](https://www.conf42.com/Large_Language_Models_LLMs_2026_Prateek_Mittal_knowledge_graphs_delivery) shows the knowledge-graph angle.
- [Sasidhar Reddy Somula on real-time fraud prevention at scale](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sasidhar_Reddy_Somula_real_time_fraud) covers the sub-second fraud requirement from the SRE side.

[Watch Muthuselvam Chandramohan's talk](https://www.conf42.com/Platform_Engineering_2025_Muthuselvam_Chandramohan_relationship_architectural_graph)

[Watch the talk on YouTube](https://youtu.be/9I5KzzaShZ4).

## Watch the talk

[Building Real-Time Graph Analytics Platforms: Architectural Patterns for High-Performance Relationship Processing](https://www.conf42.com/Platform_Engineering_2025_Muthuselvam_Chandramohan_relationship_architectural_graph) at Conf42 Platform Engineering 2025.
