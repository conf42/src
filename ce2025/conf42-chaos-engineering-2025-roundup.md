# Conf42 Chaos Engineering 2025: break it on purpose, everywhere

Conf42 Blog, 2025-02-21. https://www.conf42.com/ce2025/conf42-chaos-engineering-2025-roundup

In short: Conf42 Chaos Engineering 2025 roundup - socio-technical experiments, network faults on Fargate, chaos in platforms, mobile apps, AI monitoring and security.

Conf42 Chaos Engineering 2025 ran online on February 20, 2025, with 28 talks, and the theme was scope creep in the best sense. Chaos engineering started with killing instances; in this lineup it reached on-call rotations, internal developer platforms, mobile apps, AI model monitoring, and security controls. The common thread: if you have not watched it fail on purpose, you do not know how it fails.

The talks are all on the [Conf42 Chaos Engineering 2025 event page](https://www.conf42.com/ce2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrDA4LX-Xal04LBJN52V6C1C).

## The system includes the people

[Benjamin Wilms](https://www.conf42.com/Chaos_Engineering_2025_Benjamin_Wilms_reliable_system_unpredictable), co-founder and CEO of gold sponsor Steadybit, gave the keynote-style talk of the day. His definition of a system includes the infrastructure, pipelines, people, and processes around the software, and his best demo tested all of it at once: inject latency into one backend service and take down the gateway, then check that Datadog alerts within 90 seconds, PagerDuty opens an incident, someone acknowledges it, the system recovers, and the incident is resolved. Before any experiment, he also found an availability-zone risk just by colouring Kubernetes deployments by zone. He is clear that the point is the organisation, not blaming whoever was on call.

[Pierluigi Meloni](https://www.conf42.com/Chaos_Engineering_2025_Pierluigi_Meloni_success_people_tech), co-founder and CEO of Utterskills, pushed the human angle further: coding alone no longer makes you stand out, and most project failures come from human factors rather than technology. [Mihaela-Roxana Ghidersa](https://www.conf42.com/Chaos_Engineering_2025_MihaelaRoxana_Ghidersa_mindset_software_build) of Signant Health looked at how reasoning patterns shape design decisions, and [Vitali Shchur](https://www.conf42.com/Chaos_Engineering_2025_Vitali_Shchur_qa_mindset_startup) of Check Point Software argued that QA engineers at startups need to think like business analysts and usability experts too.

## Fault injection, hands on

[Sunil Govindankutty](https://www.conf42.com/Chaos_Engineering_2025_Sunil_Govindankutty_network_resilience_experiments), an Enterprise Support Lead at AWS, opened with Werner Vogels's line that everything fails all the time, then demoed AWS Fault Injection Service experiments on Amazon ECS with Fargate: latency, packet loss, and blackhole conditions against a sample containerised application, so you can see the behaviour before your users do.

[Sayan Mondal](https://www.conf42.com/Chaos_Engineering_2025_Sayan_Mondal_cultural_mindset_platform), a Senior Software Engineer at Harness and a LitmusChaos maintainer, argued for a chaos-first mindset in platform engineering: make resilience testing part of the internal developer platform and the CI/CD path, with a demo deliberately built to break. [Muhammad Ahmad Saeed](https://www.conf42.com/Chaos_Engineering_2025_Muhammad_Ahmad_Saeed_chaos_microservices_engineering) covered designing microservices that hold up under failure, and [Muhammad Rizwan](https://www.conf42.com/Chaos_Engineering_2025_Muhammad_Rizwan_architecture_systems_event) of Procode showed failure isolation and self-healing with event-driven architecture on Azure Event Grid. [Somaning Turwale](https://www.conf42.com/Chaos_Engineering_2025_Somaning_Turwale_resilience_recovery_disaster) of Microsoft took the bigger blast radius, disaster recovery with Azure Site Recovery.

## Chaos beyond the backend

Two talks took controlled failure to places it rarely goes. [Jaspreet Kumar](https://www.conf42.com/Chaos_Engineering_2025_Jaspreet_Kumar_mobile_apps), Lead Software Engineer at Microsoft, asked the obvious question in his abstract: why not break your mobile app before your users do? [Muddassar Sharif](https://www.conf42.com/Chaos_Engineering_2025_Muddassar_Sharif_ai_model_systems), co-founder and CTO of Virtuans.ai, applied failure simulation to AI model monitoring, starting from the questions executives and engineering managers ask about LLMs in production and the monitoring concepts the industry already uses.

[Prashanth Reddy Kora](https://www.conf42.com/Chaos_Engineering_2025_Prashanth_Reddy_Kora_chaos_cloud_systems) of Centene stress-tested cloud database systems, and [Shashank Reddy Beeravelly](https://www.conf42.com/Chaos_Engineering_2025_Shashank_Reddy_Beeravelly_ai_data_quality) of Walmart looked at keeping data quality intact when the data itself is chaotic.

## Security as a failure mode

The security track treated breaches as just another failure to rehearse. [Sandeep Batchu](https://www.conf42.com/Chaos_Engineering_2025_Sandeep_Batchu_security_cloud_defense), a Principal Software Engineer at Microsoft, made the case for chaos principles in cloud security testing. [Chirag Gajiwala](https://www.conf42.com/Chaos_Engineering_2025_Chirag_Gajiwala_resilience_models_security) of Nutanix explored reinforcement learning for adaptive resilience and generative models to simulate vulnerabilities, and [Vamsi Anumolu](https://www.conf42.com/Chaos_Engineering_2025_Vamsi_Anumolu_security_devsecops_operations) of iCrossing covered DevSecOps across multiple clouds. [Rinku Mohan](https://www.conf42.com/Chaos_Engineering_2025_Rinku_Mohan_signon_design_implementation) of bettercoach went deep on single sign-on design and its integration traps.

## The quiet case for fewer moving parts

A few talks argued that resilience starts with less. [Denis Ermakov](https://www.conf42.com/Chaos_Engineering_2025_Denis_Ermakov_library_fundamentals_need), front-end lead at Techflow (which builds portfolio management software for banks), greeted his "lovely chaotic people" and then made the case against reaching for a shiny auth library in Next.js when the fundamentals already do the job. [Vivek Kumar](https://www.conf42.com/Chaos_Engineering_2025_Vivek_Kumar_apps_vps_docker) compared VPS hosting with Docker, and [Hari Yerramsetty](https://www.conf42.com/Chaos_Engineering_2025_Hari_Yerramsetty_cost_optimization_success) of Flexport covered right-sizing, autoscaling, and FinOps.

The rest of the lineup ran from enterprise systems to networks: [Gopikrishna Yeturi](https://www.conf42.com/Chaos_Engineering_2025_Gopikrishna_Yeturi_performance_migration_framework) of LTIMindtree and [Lurduma Reddy Thirumala Reddy](https://www.conf42.com/Chaos_Engineering_2025_Lurduma_Reddy_Thirumala_Reddy_operations_workloads_scalability) on SAP migrations and SAP on Azure, [Jaya Krishna Vemuri](https://www.conf42.com/Chaos_Engineering_2025_Jaya_Krishna_Vemuri_investment_banking_accuracy) of State Street on reconciliation, [Naveen Gowda](https://www.conf42.com/Chaos_Engineering_2025_Naveen_Gowda_financial_automation_ecosystems) of Couchbase on financial workflow automation, [Rao Marapatla](https://www.conf42.com/Chaos_Engineering_2025_Rao_Marapatla_analytics_marketing_insights) of BreakthroughT1D on nonprofit marketing APIs, [Vedant Agarwal](https://www.conf42.com/Chaos_Engineering_2025_Vedant_Agarwal_personalization_ranking_systems) of Walmart Global Tech on neural ranking, [Sai Charan Madugula](https://www.conf42.com/Chaos_Engineering_2025_Sai_Charan_Madugula_iot_networking_agility) on SDN for IoT and 5G, and [Dmitrii Nikitin](https://www.conf42.com/Chaos_Engineering_2025_Dmitrii_Nikitin_development_maintenance_applications) of Quadcode on white-label Android apps.

## Sponsors and what's next

Thanks to gold sponsors [Steadybit](https://steadybit.com/), [Rapydo](https://www.rapydo.io/), and [SREday](https://www.sreday.com/), the [StarterAI](https://www.starterai.dev/) newsletter, the [HockeyStick](https://www.hockeystick.show/) podcast, and the media partners on the event page.

The series continues with [Conf42 Chaos Engineering 2026](https://www.conf42.com/ce2026) on December 3, 2026. Schedule your next game day accordingly.
