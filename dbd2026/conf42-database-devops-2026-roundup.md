# Conf42 Database DevOps 2026: migrations, operators and AI on call

Conf42 Blog, 2026-06-05. https://www.conf42.com/dbd2026/conf42-database-devops-2026-roundup

In short: Conf42 Database DevOps 2026 roundup - safe schema migrations, a 30-day Kubernetes operator test, serverless database lessons and AI-assisted tuning.

Conf42 Database DevOps 2026 ran online on June 4, 2026, with 25 talks about the part of the stack that does not roll back cleanly. The schedule was split into AI, automation, delivery, governance, and scale tracks, but one question ran through all of them: now that AI can write your migrations and tune your queries, which parts of database operations can you safely hand over, and which still need a human with a pager?

Every talk is on the [Conf42 Database DevOps 2026 event page](https://www.conf42.com/dbd2026) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrCwmGmMnd2P7QS42DFYdMUU).

## The riskiest deploy you ship

Schema migrations got the most attention, and for good reason. [Ahmed Tariq](https://www.conf42.com/Database_DevOps_2026_Ahmed_Tariq_postgres_mysql_scaling), a Cloud DevOps Engineer, opened his abstract with the line every DBA nods at: application releases can be rolled forward and back, but a migration that locks a 2TB table for an hour, or quietly loses data on rollback, cannot. His field guide covers expand-and-contract, migration tests, approval gates, and post-deploy checks, then adds AI where it earns its keep (drafting forward and rollback DDL, flagging unsafe operations) and is honest about where it breaks, such as hallucinated Postgres flags that are really MySQL flags.

Diamond sponsor Harness showed the pattern end to end. [Stephen Atwell](https://www.conf42.com/Database_DevOps_2026_Stephen_Atwell_cd_stateful_applications), Director of Product at Harness, had AI write a trigger-based Postgres migration that splits a JSON blob column into real columns, then shipped it through blue-green in staging and canary in production with no downtime, with policy checks, production data cloned to staging, and an AI-written test confirming that both app versions saw the same orders.

[Niraj Katkamwar](https://www.conf42.com/Database_DevOps_2026_Niraj_Katkamwar_llm_agents_delivery) of Intuit presented independent research on a prompt-driven framework that turns natural-language requirements into microservice and schema changes.

## Can the operator replace the DBA?

[Amarachi Iheanacho](https://www.conf42.com/Database_DevOps_2026_Amarachi_Iheanacho_postgres_k8s_tuning) of SideroLabs ran the experiment many teams argue about but never run: hand day-to-day operations of a PostgreSQL cluster to the CloudNativePG operator for 30 days, then deliberately inject node failures, pod crashes, storage pressure, replication issues, upgrades, and restores. Some problems were fixed automatically within seconds; others needed a human. The week-by-week walkthrough is the most honest answer to the title you will find.

[Renato Losio](https://www.conf42.com/Database_DevOps_2026_Renato_Losio_mistakes_lessons_scaling) brought five lessons from five years of so-called serverless databases on AWS. He once drew the New York City skyline with Aurora Serverless v2 capacity at re:Invent, and says fifteen years with AWS does not make him an expert, it just makes him old. Among them: serverless is just an adjective, and storage usually matters more than CPU. His key message: serverless databases remove capacity management, but they don't remove database engineering.

## AI as the junior DBA

Several talks put AI into the tuning loop. [Naga Bellamkonda](https://www.conf42.com/Database_DevOps_2026_Naga_Bellamkonda_alerts_incident_platform) of Gartner and [Ellavarasan Asokan](https://www.conf42.com/Database_DevOps_2026_Ellavarasan_Asokan_monitoring_reliability_platform) of Capital One, both long-time Oracle and Postgres administrators, shared lessons from AI-driven optimisation in production, from predictive tuning towards more autonomous operations. [Sampath Rao Madarapu](https://www.conf42.com/Database_DevOps_2026_Sampath_Rao_Madarapu_azure_cloud_monitoring) of Microsoft showed Copilot in Azure for diagnostics and resource control.

On the AI application side, [Alejandro Duarte](https://www.conf42.com/Database_DevOps_2026_Alejandro_Duarte_llm_vectors_semantic) of MariaDB covered RAG in production, starting from the infamous glue-on-pizza answers, and [Ankur Aggarwal](https://www.conf42.com/Database_DevOps_2026_Ankur_Aggarwal_llm_inference_models) of Meta tackled a hard gap: how an LLM running in a trusted execution environment can query databases through MCP without exposing sensitive data.

## Same SQL, different answers

The governance track had the talk most data engineers should watch. [Muthupalaniappan Ramanathan](https://www.conf42.com/Database_DevOps_2026_Muthupalaniappan_Ramanathan_queries_monitoring_sql) of DoorDash showed how identical queries can return different results on Spark, Trino, and Snowflake because of type handling, null semantics, and optimiser behaviour, and proposed a canonical semantic layer with CI-integrated validation to catch the drift.

[Sheena Yap Chan](https://www.conf42.com/Database_DevOps_2026_Sheena_Yap_Chan_incident_reliability_platform) argued that the real risk is often not missing data but database signals that never reach the right people in time. [Muthu Saravanan](https://www.conf42.com/Database_DevOps_2026_Muthu_Saravanan_alerts_telemetry_platform) of Mind-Pros and [Dharmendra Ahuja](https://www.conf42.com/Database_DevOps_2026_Dharmendra_Ahuja_monitoring_analytics_platform) of IBM looked at intentional delivery and ethical validation inside AI-driven data pipelines.

## Always on, at scale

The scale track was heavy on finance. [Priyatham Nagaiya Seenu Naidu](https://www.conf42.com/Database_DevOps_2026_Priyatham_Nagaiya_Seenu_Naidu_kafka_pipelines_clusters) of Mastercard covered real-time payment networks like FedNow, UPI, PIX, and SEPA Instant, where the database must be up around the clock with sub-second processing. [Ritvik Pandya](https://www.conf42.com/Database_DevOps_2026_Ritvik_Pandya_monitoring_telemetry_reliability) of JPMorgan Chase started from a sudden p99 spike at peak hours and traced it to the ingress layer, fixing it with deterministic routing for cache locality. [Srikanth Uddanti](https://www.conf42.com/Database_DevOps_2026_Srikanth_Uddanti_distributed_systems_delivery) of Charles Schwab walked through the trade-offs of distributed databases, and [Surya Lankalapalli](https://www.conf42.com/Database_DevOps_2026_Surya_Lankalapalli_telemetry_analytics_delivery) of Microsoft made the case for active-active, multi-provider DNS, the dependency that quietly delays database failover.

Elsewhere in the lineup: [Jason Lester](https://www.conf42.com/Database_DevOps_2026_Jason_Lester_productivity_teams_efficiency) of Capgemini on loading cloud API output into a database for analysis the console cannot do, [Sulabh Jain](https://www.conf42.com/Database_DevOps_2026_Sulabh_Jain_kafka_streams_k8s) on modernising insurance core systems, [Sirisha Ayyagari](https://www.conf42.com/Database_DevOps_2026_Sirisha_Ayyagari_telemetry_tracing_platform) of IBM on real-time SAP pricing, [Kamini Murugaboopathy](https://www.conf42.com/Database_DevOps_2026_Kamini_Murugaboopathy_agents_pipelines_o11y) on real-time marketing analytics, [Bharat Kumar Reddy Karumuri](https://www.conf42.com/Database_DevOps_2026_Bharat_Kumar_Reddy_Karumuri_models_training_telemetry) of General Motors on operationalising ML and GenAI, [Zeeshan Khan](https://www.conf42.com/Database_DevOps_2026_Zeeshan_Khan_vectors_recruiting_semantic) on hiring as a data infrastructure problem, and [Harsha Vardhani Talluri](https://www.conf42.com/Database_DevOps_2026_Harsha_Vardhani_Talluri_metrics_telemetry_unified) on multi-vendor DOCSIS deployments.

## Sponsors and what's next

Thanks to diamond sponsor [Harness](https://www.harness.io/), gold sponsor [SREday](https://www.sreday.com/), the [HockeyStick](https://www.hockeystick.show/) podcast, and the media partners on the event page.

This was the first Conf42 Database DevOps. The second, [Conf42 Database DevOps 2027](https://www.conf42.com/dbd2027), is set for May 27, 2027. Bring your rollback scripts.
