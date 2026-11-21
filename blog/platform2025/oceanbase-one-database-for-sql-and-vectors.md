# One SQL query instead of four databases for RAG and search

Conf42 Blog, 2025-08-11, updated 2026-11-09. https://www.conf42.com/blog/platform2025/oceanbase-one-database-for-sql-and-vectors

In short: OceanBase's Peng Wang at Conf42 Platform Engineering 2025 on running SQL, full-text and vector search in one Kubernetes-native database for AI apps.

A typical RAG backend asks MySQL for metadata, a vector store for embeddings, Elasticsearch for full text and Redis for the cache, then hopes they all agree. At Conf42 Platform Engineering 2025, Peng Wang, global technical evangelist at OceanBase, argued that platform teams can collapse that stack into one database, and showed how OceanBase does it on Kubernetes.

Honest scope first: this is a vendor talk about OceanBase, and the numbers are OceanBase's customer results. The architectural argument travels further than the product, though.

## AI workloads are now normal workloads

Peng starts with the demand side. Citing IDC, he says over 92% of global data is unstructured, and he points to surveys showing most enterprises already run AI infrastructure platforms and are embedding agents in core applications. His point: RAG and semantic search have left the lab, so platform and database teams inherit their operational problems.

Those problems differ by workload. Q&A chatbots want low-latency semantic search with context. Log analytics wants high write throughput, search and aggregation. Core business systems want ACID transactions and strong consistency. Teams usually answer with one specialised database per need, and then spend their weeks maintaining the ETL between them.

## Count the network round trips

The clearest slide compares two request paths for AI-powered knowledge retrieval. In the conventional design, one user query fans out to MySQL, a vector database and Redis, adding up to at least four network round trips and about 170 milliseconds end to end, plus the job of keeping all of them consistent. In the OceanBase version, the same request is one query against one engine, at about 50 milliseconds, with strong consistency maintained throughout.

His hybrid-query example makes it tangible: a coffee shop within 500 metres, average spend under a set price, a rating above a threshold, and no queues. That mixes GIS, relational and semantic data. In a stitched stack it is several queries and some glue code; in OceanBase it is a single SQL statement.

From the customer case he cites, query latency dropped by over 70%, data that used to take hours to refresh became available in minutes, and the integration code to maintain shrank by over 40%.

## Under the hood

The architecture section covers what platform engineers will ask about. Data is distributed across availability zones for horizontal scale. OceanBase is containerised with operator-based management and elastic scaling of compute and storage. Consistency comes from a Paxos-based consensus protocol with three replicas across zones and automatic failover.

Multi-tenancy is the other half of the pitch: different workloads share a cluster but run in isolated tenants with dedicated resources, so the log-analytics tenant doesn't become the noisy neighbour of the transactional one. A single SQL layer covers structured data, full-text and vector search.

## Who should watch

Platform teams running a vector database next to a relational one and tired of syncing them, and anyone designing RAG infrastructure who wants a counterpoint to the reflex of adding another specialised store. If you need a neutral comparison of databases, look elsewhere; this is one vendor's well-argued case.

## Related Conf42 talks

- [Tim Spann on cloud native open source vector databases](https://www.conf42.com/Kube_Native_2024_Tim_Spann_cloud_native_open_source_vector_databases) surveys the specialised alternative.
- [Alejandro Duarte on RAG in production](https://www.conf42.com/Database_DevOps_2026_Alejandro_Duarte_llm_vectors_semantic) covers the challenges on the retrieval side.
- [Amarachi Iheanacho asks whether a Kubernetes operator can replace a DBA](https://www.conf42.com/Database_DevOps_2026_Amarachi_Iheanacho_postgres_k8s_tuning), a good reality check on operator-managed databases.

[Watch Peng Wang's talk](https://www.conf42.com/Platform_Engineering_2025_Peng_Wang_workloads_oceanbase_powering)

[Watch the talk on YouTube](https://youtu.be/k3tw9GeTgiM).

## Watch the talk

[One Platform, Many Workloads: Powering AI Applications with OceanBase on Kubernetes](https://www.conf42.com/Platform_Engineering_2025_Peng_Wang_workloads_oceanbase_powering) at Conf42 Platform Engineering 2025.
