# Conf42 Platform Engineering 2025 - paved roads, self-healing and sane thresholds

Conf42 Blog, 2025-09-05. https://www.conf42.com/platform2025/platform-engineering-2025-roundup-paved-roads

In short: Conf42 Platform Engineering 2025 in review, 83 talks on developer platforms, SCM at 50K engineers, ML inference, self-healing infra, zero trust and thresholds.

[Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025) ran on September 4, 2025 with 83 talks, one of the biggest line-ups of the Conf42 year. The common thread: a platform is a product with internal customers, and its job is to remove decisions developers shouldn't have to make, whether that is which Git permissions to request, where an ML model gets served, or what the alert threshold should be. Engineers from Meta, Google, Microsoft, Qualcomm, eBay, Roku, Starbucks, Intuit, Zscaler, Palo Alto Networks, JPMorgan Chase, Fidelity and AWS showed their versions.

## The platform is a product, and DevEx is the metric

[Vasdev Gullapalli](https://www.conf42.com/Platform_Engineering_2025_Vasdev_Gullapalli_scm_git_policies) (Qualcomm) gave the clearest example of platform thinking applied to something most companies treat as plumbing: source control. Managing GitHub, GitLab and Gerrit for more than 50K engineers, his team treats SCM as a platform with governance built in. Licence activation, deactivation and reactivation are all self-serve and automated, because a developer waiting on a licence is a developer not writing code, and an unused licence is opex nobody wants.

[Anil Kumar Veldurthi](https://www.conf42.com/Platform_Engineering_2025_Anil_Kumar_Veldurthi_internal_ops_impact) (US Bank) covered how to build internal developer platforms that move delivery speed, and [Michel Murabito](https://www.conf42.com/Platform_Engineering_2025_Michel_Murabito_practical_elevate_strategies) (Mia-Platform) focused on using AI in platform tooling to cut developer cognitive load. [Mohamed Najaaf](https://www.conf42.com/Platform_Engineering_2025_Mohamed_Najaaf_developer_gitlab_level) (AWS) demoed GitLab with Amazon Q Developer for modernising legacy Java and generating merge requests and reviews. [Rajani Jayantha](https://www.conf42.com/Platform_Engineering_2025_Rajani_Jayantha_monolith_microservices_decision) (Wayfair) offered a decision framework for the eternal microservices versus monolith argument, and [Jayant Tyagi](https://www.conf42.com/Platform_Engineering_2025_Jayant_Tyagi_development_ides_performance) (Salesforce) looked at cloud IDEs as a platform concern, security and performance included.

The most unexpected platform: design. [Pallav Laskar](https://www.conf42.com/Platform_Engineering_2025_Pallav_Laskar_design_tokens_multi) (Zscaler) treats design tokens as infrastructure, run through GitOps workflows, with automated theming across platforms.

## Thresholds are maths, not vibes

[Emmanuel Bakare](https://www.conf42.com/Platform_Engineering_2025_Emmanuel_Bakare_math_exploring_thresholds) (Twilio) gave the most quietly nerdy talk of the day. Static thresholds are easy to estimate and diagnose but noisy, single-variable and blind to organic growth. Dynamic ones adapt and produce fewer false positives, but need more data and a model of the system up front. He walks the numerical process for static thresholds step by step: filter outliers with IQR or z-scores, choose an aggregate, then reduce the error. If your alert thresholds were picked because a round number felt right, this one is for you.

## Self-healing is the new uptime

A whole cluster of talks tried to take humans out of the 3am loop. [Sureshkumar Karuppuchamy](https://www.conf42.com/Platform_Engineering_2025_Sureshkumar_Karuppuchamy_defense_dashboard_large) (eBay) went beyond dashboards to adaptive rate limiting, auto-rollbacks, circuit breakers and closed-loop pipelines for a high-scale listing platform. [Shailin Saraiya](https://www.conf42.com/Platform_Engineering_2025_Shailin_Saraiya_cache_millions_latency) (Roku) described self-healing cache infrastructure built to scale with a fast-growing user base. [Konstantin Berezin](https://www.conf42.com/Platform_Engineering_2025_Konstantin_Berezin_context_agents) (Rapyd) used AI agents to tag anomalies in logs and traces so engineers are paged only for the outliers that matter, and [Lakshmi Srinivasarao Kothamasu](https://www.conf42.com/Platform_Engineering_2025_Lakshmi_Srinivasarao_Kothamasu_firefighting_manual_pipelines) (Fidelity Investments) applied the same thinking to self-healing data pipelines. [Ajay Averineni](https://www.conf42.com/Platform_Engineering_2025_Ajay_Averineni_observability_healing_intelligent) (IBM) tied AI-driven observability to automated remediation.

## Platforms for ML, data and money

ML infrastructure is now a platform team's job. [Gangadharan Venkataraman](https://www.conf42.com/Platform_Engineering_2025_Gangadharan_Venkataraman_inference_orchestration_kubernetes) (Starbucks) shared patterns for Kubernetes-native ML inference platforms that keep data scientists productive, drawing on production systems at Starbucks and eBay. [Bhaskar Goyal](https://www.conf42.com/Platform_Engineering_2025_Bhaskar_Goyal_container_paradise_chaos) (Google) went from container chaos to production-ready AI platforms, and [Peng Wang](https://www.conf42.com/Platform_Engineering_2025_Peng_Wang_workloads_oceanbase_powering) (OceanBase) ran many workloads, AI included, on one database on Kubernetes. [Srinivas Chennupati](https://www.conf42.com/Platform_Engineering_2025_Srinivas_Chennupati_knowledge_rag_strategies) (Fannie Mae) treated production RAG as enterprise knowledge infrastructure.

Financial systems got a strong showing. [Tapan Vijay](https://www.conf42.com/Platform_Engineering_2025_Tapan_Vijay_card_planet_resilience) (Meta) covered the distributed systems and zero-downtime strategies behind planet-scale card processing, [Karthickram Vailraj](https://www.conf42.com/Platform_Engineering_2025_Karthickram_Vailraj_sharding_replication_database) (Charles Schwab) went into database sharding and replication for fintech, and [Tarun Chataraju](https://www.conf42.com/Platform_Engineering_2025_Tarun_Chataraju_modernizing_fixed_index) (JPMorgan Chase) modernised fixed-income index systems cloud-native.

## Security and the network underneath

[Naveen Kumar Birru](https://www.conf42.com/Platform_Engineering_2025_Naveen_Kumar_Birru_perimeters_zero_trust) (Palo Alto Networks) laid out zero trust at enterprise scale, [Naresh Yelkoti](https://www.conf42.com/Platform_Engineering_2025_Naresh_Yelkoti_transforms_code_bulletproof) (U.S. Bank) made the case for security as code in the pipeline, and [Anjan Kaleru](https://www.conf42.com/Platform_Engineering_2025_Anjan_Kaleru_governance_identity_secure) (Sony Interactive Entertainment) used data to drive identity governance.

Then there was the network trivia question you didn't know you had. [Srinivas Shamkura](https://www.conf42.com/Platform_Engineering_2025_Srinivas_Shamkura_ditched_multicast_challenge) (SADA) explained why the big clouds don't offer native multicast: forwarding-state explosion in software-defined networks, a protocol designed for one administrative domain colliding with multi-tenancy, dynamic routing that is hard to automate, and packet processing costs in virtual environments that can eat the bandwidth savings. The radio-station analogy alone is worth the click.

## Where to watch

All 83 talks are on the [event page](https://www.conf42.com/platform2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrBMHyARfX-JY_7WHoF5qmDh). The series returns with [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026).
