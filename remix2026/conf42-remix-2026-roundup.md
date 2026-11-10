# Conf42 Remix 2026: 52 talks from every corner of the series

Conf42 Blog, 2026-08-21. https://www.conf42.com/remix2026/conf42-remix-2026-roundup

In short: Conf42 Remix 2026 roundup: resilience, AI agents in production, Kubernetes GPUs, Go monoliths, security basics and accessible JavaScript in 52 talks.

Conf42 Remix 2026, on August 20, 2026, is the one event in the series that refuses to pick a topic. It brings together popular talks from across the Conf42 calendar, grouped into tracks named after the series' own conferences, from Rustlang and Golang to Incident Management, DevSecOps and Large Language Models. The 52 talks ranged from Spotify's scaling lessons to monitoring garden plants with IoT sensors, and the whole lineup is on the [event page](https://www.conf42.com/remix2026).

Here are the threads that ran across the tracks.

## Resilience is a separate goal from uptime

Harness opened with a keynote from [Uma Mukkara](https://www.conf42.com/Remix_2026_Uma_Mukkara_resilience_testing_enterprise), Head of Resilience Testing and co-creator of LitmusChaos. His argument: reliability is about staying available, resilience is about how you come back when a provider fails underneath you, and SREs should push for resilience gates in the pipeline the way they already gate on test coverage. He closed with AI-generated resilience risk reports as a way to win permission for chaos testing.

[Stuart Clark](https://www.conf42.com/Remix_2026_Stuart_Clark_scale_fail_spotify) of Spotify told the story of hyper-growth in 2014 creating fragmentation that made onboarding and incident response harder, and the lesson that good abstractions teach complexity rather than hide it. [Sylvain Kalache](https://www.conf42.com/Remix_2026_Sylvain_Kalache_vibes_outages_writes) of Rootly looked at what LLM-assisted coding does to reliability, including AI-generated tests that mirror the bugs they should catch. [Spiros Economakis](https://www.conf42.com/Remix_2026_Spiros_Economakis_sre_experience_ai) of NOFire AI argued the real AI opportunity in SRE is customer-centred prevention rather than faster RCA, and cloud architect [Renato Losio](https://www.conf42.com/Remix_2026_Renato_Losio_mistakes_lessons_scaling) shared five hard lessons from five years of so-called serverless databases.

## AI agents meet production constraints

[Samuel Baruffi](https://www.conf42.com/Remix_2026_Samuel_Baruffi_poc_bedrock_agentcore) of AWS addressed why so many agent projects stall at proof of concept, and how Amazon Bedrock AgentCore covers identity, gateway-based tool access, runtime isolation and memory. [Michael Levan](https://www.conf42.com/Remix_2026_Michael_Levan_agents_telemetry_costs) of Solo.io focused on the two questions every team running MCP gets asked: how do we observe it, and how do we keep costs down?

Two talks went after the context problem. [Roxane Fischer](https://www.conf42.com/Remix_2026_Roxane_Fischer_context_reasoning_infrastructure), co-founder of Anyshift.io, showed infrastructure modelled as a graph so an LLM can follow multi-hop dependencies with Graph RAG and natural-language-to-Cypher queries instead of guessing. Lior Schejter asked what happens when an agent that copes well with one repo meets [a distributed system of 200 microservices](https://www.conf42.com/Remix_2026_Lior_Schejter_context_agents_reasoning), and how to give it a mental model of the whole. And [Leo Visser](https://www.conf42.com/Remix_2026_Leo_Visser_governance_apis_control) of OGD ICT-diensten demonstrated API management as the leash that keeps AI usage, budget and risk under control.

## Kubernetes as a platform for everything

[Piotr Zaniewski](https://www.conf42.com/Remix_2026_Piotr_Zaniewski_sandboxes_gpu_multitenant) of vCluster spun up multi-tenant sandboxes with NVIDIA's open-source KAI Scheduler inside them to share fractional GPUs between teams. [Christophe Gigax](https://www.conf42.com/Remix_2026_Christophe_Gigax_dapr_architectures_cloudnative) of Hager Group made the case for Dapr as an abstraction layer for state, pub/sub and more. [Peng Wang](https://www.conf42.com/Remix_2026_Peng_Wang_workloads_oceanbase_powering) of OceanBase showed one database handling RAG, semantic search and log analytics on Kubernetes, and [Alejandro Mercado](https://www.conf42.com/Remix_2026_Alejandro_Mercado_observability_kubernetes_ebpf) of Michael Page covered eBPF-powered observability for root cause analysis in clusters.

## Go and Rust, from monoliths to leaderboards

The Golang track had two strong engineering stories. [Victor Lyuboslavsky](https://www.conf42.com/Remix_2026_Victor_Lyuboslavsky_modularizing_year_monolith) of Fleet Device Management described modularising a 10-year-old Go monolith whose layers had turned into hidden coupling and unclear ownership, and was candid about the people side as well as the architecture. [Ivan Balashov](https://www.conf42.com/Remix_2026_Ivan_Balashov_engineering_high_performance) of SoftSwiss walked through a leaderboard system that suffered daily outages, and the redesign that took its core operation from O(N²) to O(log N). [Emmanuela Opurum](https://www.conf42.com/Remix_2026_Emmanuela_Opurum_building_secure_pipelines) of SoftNet Technologies used Go to build secure CI/CD automation components. On the Rustlang track, [Tashi Garg](https://www.conf42.com/Remix_2026_Tashi_Garg_cloud_ai_rust) of Juniper Networks built dynamic infrastructure UIs in Rust.

## Security fundamentals, explained well

Several talks were good introductions, and said so. [Peter De Tender](https://www.conf42.com/Remix_2026_Peter_De_Tender_github_dependabot_codeql) of Microsoft gave a lap around GitHub Dependabot, CodeQL and the other built-in security features. [Safeer C M](https://www.conf42.com/Remix_2026_Safeer_C_M_sast_open_source_semgrep) of MoEngage opened the black box of static analysis using open-source Semgrep. Security engineer [Aleksandra Drobnjak](https://www.conf42.com/Remix_2026_Aleksandra_Drobnjak_documentation_artifacts_beginners) set out a minimum viable set of ISO 42001 documents for anyone asked who approved an AI system and on what data, and [Marat Kenzhebulatov](https://www.conf42.com/Remix_2026_Marat_Kenzhebulatov_vision_computer_imaging) of Booking.com showed how to bring AI agents safely into security-critical backend work like code review and threat modelling.

## The web, data and one garden

[Gian Wild](https://www.conf42.com/Remix_2026_Gian_Wild_accessible_easier_than) of AccessibilityOz gave concrete code for accessible forms and JavaScript, reminding everyone that a fifth of the population has a disability. [Daniel Afonso](https://www.conf42.com/Remix_2026_Daniel_Afonso_state_testing_tech) of PagerDuty reviewed a decade of change in JavaScript testing. [Alejandro Duarte](https://www.conf42.com/Remix_2026_Alejandro_Duarte_llm_vectors_semantic) of MariaDB covered RAG in production, glue-on-pizza hallucinations included, and [Maximilian Schattauer](https://www.conf42.com/Remix_2026_Maximilian_Schattauer_retrievers_documents_ranking) of Perelyn showed LLM-driven pairwise ranking beating semantic retrievers on hard document retrieval.

And for the weekend, [Marie Cruz](https://www.conf42.com/Remix_2026_Marie_Cruz_sensors_gardening_analytics) of Grafana Labs showed how to monitor soil moisture with IoT sensors and Grafana Cloud as a project to do with your kids. The only talk of the day where the alert means water the basil.

## Sponsors

Thanks to [Harness](https://www.harness.io/), our diamond sponsor, to gold sponsors [SREday](https://www.sreday.com/) and [LLMday](https://llmday.com/), and to [HockeyStick](https://www.hockeystick.show/) for the podcast partnership.

## What's next

Every talk is linked from the [Conf42 Remix 2026 page](https://www.conf42.com/remix2026). The next edition, [Conf42 Remix 2027](https://www.conf42.com/remix2027), is set for August 19, 2027.
