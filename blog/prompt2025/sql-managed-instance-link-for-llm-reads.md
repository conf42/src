# Give your LLM a read replica, not your production SQL Server

Conf42 Blog, 2025-10-20, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/sql-managed-instance-link-for-llm-reads

In short: Siva Kumar Raju Bhupathiraju (Paycor) at Conf42 Prompt Engineering 2025 on Azure SQL Managed Instance and MI Link as a low-latency, governed data source for LLMs.

Point a chatbot at the on-prem SQL Server that runs payroll and you've built a load test nobody scheduled. At Conf42 Prompt Engineering 2025, Siva Kumar Raju Bhupathiraju, a principal database administrator at Paycor (now a Paychex company), showed how Azure SQL Managed Instance with Managed Instance Link gives LLM workloads a near-real-time, governed copy of on-prem data without a full migration, and how to tune it for prompt traffic.

It's a focused DBA talk on the Microsoft stack: specific features, a reference architecture, and a tuning checklist, rather than LLM theory.

## Legacy SQL wasn't built for prompt traffic

Siva lists what goes wrong when traditional SQL Server meets LLM applications: high-latency data access, limited scalability under many concurrent AI requests, complex replication across environments, and bottlenecks in real-time scenarios. LLM apps, meanwhile, want sub-second responses per prompt, continuous data sync, elastic scale and enterprise security. The gap between how fast the AI app moves and how fast the database answers is where the user experience dies.

## MI Link: replicate, don't migrate

The core of the talk is Managed Instance Link. It connects an on-prem SQL Server to an Azure SQL Managed Instance using log-based synchronisation, which Siva compares to an Always On availability group configuration, with near-zero latency. The managed instance then holds current, consistent data that LLM workloads can read, while production keeps doing its day job.

The same link doubles as disaster recovery. The managed instance serves AI reads and acts as a DR target, so in a disaster you can fail workloads over from on-prem to Azure. One setup, two jobs.

For global organisations, he shows multiple MI Links from one source database feeding regional managed instances, so LLMs serve users from the nearest copy and cross-region latency drops. His worked example is a global bank building a customer chatbot over mostly on-prem data: regional instances answer the bot, and the on-prem source isn't hammered by every conversation.

## Tune for prompt queries

Siva's tuning list is the most directly useful section for DBAs:

- Enable Query Store to capture query history, spot slow queries and fix plans before they hit LLM response times.
- Configure Resource Governor to classify workloads, so prompt-serving queries get dedicated memory and compute separate from everything else.
- Follow connection pooling best practices and tune parallelism and isolation levels for hundreds of simultaneous requests.
- Size the buffer pool to the workload, and index for read-heavy patterns.
- Monitor MI Link health so replication stays in sync.

For analytical prompt context, he points to Azure Synapse Link: pre-aggregate and index frequently used context in Synapse, keeping analytical preparation separate from transactional workloads and avoiding traditional ETL.

## Governance follows the data

Security travels with replication: automated discovery and labelling of sensitive data used in prompts, row-level and column-level security enforced on each target, comprehensive audit logging of AI-driven data access, and Always Encrypted columns plus TDE for data at rest and in transit.

His phased plan: assess current SQL workloads and AI integration points, optimise with MI replication tuned for low latency, scale to multi-region with integrated analytics, then build new AI applications on the hybrid base.

## Who should watch

SQL Server DBAs and data platform engineers being asked to feed an LLM app from on-prem data, and architects weighing hybrid replication against a full cloud migration. If you're not on Microsoft's stack, the separation-of-workloads idea still applies; the feature names won't.

## Related Conf42 talks

- [Microsoft SQL Server HA/DR on AWS](https://www.conf42.com/Site_Reliability_Engineering_2021_Asif_Mujawar_Microsoft_SQL_server_HADR) by Asif Mujawar at Conf42 Site Reliability Engineering 2021, the same HA/DR concerns on another cloud.
- [RAG in production: challenges, techniques and solutions](https://www.conf42.com/Database_DevOps_2026_Alejandro_Duarte_llm_vectors_semantic) by Alejandro Duarte at Conf42 Database DevOps 2026.
- [AI Assisted Azure Ops with Copilot for Diagnostics and Resource Control](https://www.conf42.com/Database_DevOps_2026_Sampath_Rao_Madarapu_azure_cloud_monitoring) by Sampath Rao Madarapu at Conf42 Database DevOps 2026.

[Watch Siva Kumar Raju Bhupathiraju's talk](https://www.conf42.com/Prompt_Engineering_2025_Siva_Kumar_Raju_Bhupathiraju_sql_infrastructure_hybrid) from [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/8Xk9igDeQuk).

## Watch the talk

[Prompt-Ready Data: Optimizing SQL Infrastructure for LLM Workloads in Hybrid Environments](https://www.conf42.com/Prompt_Engineering_2025_Siva_Kumar_Raju_Bhupathiraju_sql_infrastructure_hybrid) at Conf42 Prompt Engineering 2025.
