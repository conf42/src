# Conf42 Platform Engineering 2026: when agents become platform users

Conf42 Blog, 2026-11-06. https://www.conf42.com/platform2026/platform-engineering-2026-roundup-agents-as-users

In short: The Conf42 Platform Engineering 2026 roundup - 26 talks on agents as platform users, delegated authority, GenAI as a platform primitive and real-time data.

[Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026) went out on November 5 with 26 talks, and the question running through most of them was new: what does a platform owe its users when some of those users are AI agents? Speakers from Harness, AWS, PayPal, Coinbase, Walmart, T-Mobile, Electronic Arts and a long list of smaller teams answered from very different angles, but they kept landing on the same ideas. Context has to be explicit, authority has to be scoped, and "done" has to be decided by code you own.

Not everything was about AI. The data, mobile and migration talks were a good reminder that the platform team's day job still includes Kafka, latency budgets and getting a legacy system off life support without downtime.

## Agents are now a class of platform user

The keynote from [Jimmy Caputo](https://www.conf42.com/Platform_Engineering_2026_Jimmy_Caputo_agentic_engineering_platforms) of Harness set the frame: platforms built for humans assume someone knows the tribal knowledge, spots noisy tests and watches deploys. Agents need that made explicit through a single context layer, deterministic pipelines they call instead of improvise, central policy and observability that feeds back into all three.

[Yedidya Schwartz](https://www.conf42.com/Platform_Engineering_2026_Yedidya_Schwartz_orchestrator_sdlc_agent) of Quicklizard brought the field report. His first ticket-to-PR pipeline went green on GitHub after the model quietly skipped three phases; his crash test across six durable engines showed that a thin controller, not the engine, stopped him paying twice for model calls. [Erik Hanchett](https://www.conf42.com/Platform_Engineering_2026_Erik_Hanchett_coding_agent_claw) of AWS toured always-on "Claws", agents with memory, schedules and chat access, along with their rough edges.

Two talks looked at what happens after the code arrives faster. [Lucas Mateus Mazei Sobrinho](https://www.conf42.com/Platform_Engineering_2026_Lucas_Mateus_Mazei_Sobrinho_delivery_bottlenecks_coding) of MEMED S.A. treated AI as a stress test for the delivery system, where environments, reviews and approvals become the new queue. [Shem Magnezi](https://www.conf42.com/Platform_Engineering_2026_Shem_Magnezi_team_one_ai) of Lemonade framed running side projects with AI as platform engineering at a team size of one: the hard part is operating what you built without becoming its permanent support team.

## Authority, not just permissions

If one idea will outlive the event, it's the split between being able to do something and being allowed to decide it. [Ruby Agarwal](https://www.conf42.com/Platform_Engineering_2026_Ruby_Agarwal_autonomy_service_authority) of Avaya walked a 2:14am incident where an agent is 96% sure a deploy caused it, and showed why the rollback still needs scoped, expiring authority, an independent check and verification of the customer outcome. [Cynthia Akiotu](https://www.conf42.com/Platform_Engineering_2026_Cynthia_Akiotu_agent_llms_prompt) of Accenture followed a poisoned refund policy through an agent and showed the system holding even when the model was fooled, because the export needed an authorization check the prompt couldn't grant.

The guardrail talks were refreshingly concrete. [Sumeet L. Ram](https://www.conf42.com/Platform_Engineering_2026_Sumeet_L_Ram_compliance_gate_paved) of PayPal described an MCP server used by more than 150 product teams across 200 markets, where the hard design problem was what the platform refuses to do. [Niharika P Pujari](https://www.conf42.com/Platform_Engineering_2026_Niharika_P_Pujari_guardrails_frontends_generated) of McGraw Hill compared prompting against architecture-level guardrails (Storybook, Playwright, axe-core, CI checks) for AI-generated frontends. [Madhu Chenna](https://www.conf42.com/Platform_Engineering_2026_Madhu_Chenna_healing_rag_telemetry) of Electronic Arts presented a conceptual self-healing ops framework with confidence gates deciding when an agent may act. [Leanid Piliptsevich](https://www.conf42.com/Platform_Engineering_2026_Leanid_Piliptsevich_sandbox_app_make) of EPAM went lower: MazeWall, an experimental toolkit that lets JVM apps sandbox their own components with seccomp and Landlock.

## GenAI as a platform primitive

Several talks treated models as infrastructure with tenants, budgets and SLOs. [Brindal Patel](https://www.conf42.com/Platform_Engineering_2026_Brindal_Patel_idp_generative_apis) of Coinbase, speaking from independent work, designed a GenAI gateway that holds token budgets like card payments, caches only after four safety checks and fails over only to models that passed your evals. [Sergey Pronin](https://www.conf42.com/Platform_Engineering_2026_Sergey_Pronin_kubernetes_llm_engineer) of Solanica covered Model-as-a-Service on Kubernetes with KServe, vLLM and per-model quotas.

[Scarlett Attensil](https://www.conf42.com/Platform_Engineering_2026_Scarlett_Attensil_llm_judgments_fails) of LaunchDarkly ran the event's tidiest experiment: packing five criteria into one LLM judge call cut cost by 46% with no measurable accuracy change, while 40 criteria cost about six points. [Attila Toth](https://www.conf42.com/Platform_Engineering_2026_Attila_Toth_personalization_infra_pages) of ScyllaDB explained the feature stores behind For You feeds, from P99 tail-latency maths to query-first data models.

## Operating models and the metrics that prove them

[Jeleel Muibi](https://www.conf42.com/Platform_Engineering_2026_Jeleel_Muibi_terraform_ansible_architecture) of HybridOps argued that Terraform and Ansible are tools, and the architecture is the layer that decides authority, completion and recovery, demoed as a preflight that refuses a shared network in a dev environment. [Amith Reddy Ravuru](https://www.conf42.com/Platform_Engineering_2026_Amith_Reddy_Ravuru_slos_uptime_journey) of Reltio, an SAP company, proposed journey-based platform SLOs such as time to first environment and self-service completion rate. [Eleftheria Batsou](https://www.conf42.com/Platform_Engineering_2026_Eleftheria_Batsou_monitoring_automated_nobody) of UptimeRobot pointed at the gap in most golden paths: monitoring still gets set up by hand, later, if anyone remembers.

On the reliability side, [Saikrishna Ala](https://www.conf42.com/Platform_Engineering_2026_Saikrishna_Ala_migrations_downtime_playbook) of Bath and Body Works shared a playbook for zero-downtime migrations built on dual writes, bidirectional sync and CDC, and [Mohan Kumar Dalai](https://www.conf42.com/Platform_Engineering_2026_Mohan_Kumar_Dalai_maintenance_power_plant) of GE Vernova took platform thinking into power plants, where AI maintenance lives or dies on context and operator trust.

## Real-time data platforms

The data track was full of hard constraints. [Egor Kolovertnykh](https://www.conf42.com/Platform_Engineering_2026_Egor_Kolovertnykh_telemetry_game_conversion) of BetBoom built an in-house Dota 2 draft feed from Game State Integration and reported conversion rising from 8.4% to 31.2%. [Sujan Challa](https://www.conf42.com/Platform_Engineering_2026_Sujan_Challa_bidding_latency_constraints) of Samsung Electronics America treated latency budgets as architecture in real-time bidding. [Nidhin Jose](https://www.conf42.com/Platform_Engineering_2026_Nidhin_Jose_retail_supply_event) of Walmart covered event-driven retail supply chains with Kafka, CQRS and sagas, and [Vincenzo Santonastaso](https://www.conf42.com/Platform_Engineering_2026_Vincenzo_Santonastaso_pipelines_data_teams) of IBM showed Debezium Platform turning CDC pipelines into self-service for multiple teams.

## Mobile apps are platforms too

Two talks moved platform engineering inside a single binary. [RanjithKumar Ragavan](https://www.conf42.com/Platform_Engineering_2026_RanjithKumar_Ragavan_mobile_teams_app) of T-Mobile explained how five autonomous teams ship into the T-Life app, used by 53 million active users, through versioned contracts and independent build pipelines. [Denis Galkin](https://www.conf42.com/Platform_Engineering_2026_Denis_Galkin_mobile_plugin_framework) of Robofinance turned scattered debug menus into a plugin-based Dev Mode framework owned like an internal product.

## Thanks to the sponsors

[Harness](https://www.harness.io/) was the diamond sponsor, with [SREday](https://www.sreday.com/) as gold sponsor and [HockeyStick](https://www.hockeystick.show/) as podcast partner, alongside media partners including [Manning](https://www.manning.com) and [Packt](https://www.packtpub.com/).

Every talk is on the [Conf42 Platform Engineering 2026 page](https://www.conf42.com/platform2026) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrASkIvm2yEw5xkOVrx3cUOw). Next in the series is [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19, where several of these threads (evals, rollbacks, agents in production) continue from the model side.
