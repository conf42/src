# Conf42 Kube Native 2025: GPUs, fewer clusters and regulated AI

Conf42 Blog, 2025-10-17. https://www.conf42.com/blog/kubenative2025/conf42-kube-native-2025-roundup

In short: Conf42 Kube Native 2025 roundup - GPU sharing with vCluster, fewer environments, Dapr and eBPF, defence in depth, and AI in regulated industries on Kubernetes.

Conf42 Kube Native 2025 ran online on October 16, 2025, with 53 talks, which makes it one of the larger events in the series. Two conversations ran side by side. One was about Kubernetes itself: sharing GPUs, cutting environment sprawl, observing clusters with eBPF, and securing them in depth. The other was about what enterprises now run on it, above all AI workloads in banks, insurers, and hospitals, where compliance is part of the architecture.

Every session is on the [Conf42 Kube Native 2025 event page](https://www.conf42.com/kubenative2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrBfaAPyif8OXN3e1XcXeO2A).

## GPUs are the new scarce resource

[Piotr Zaniewski](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant), Head of Engineering Enablement at vCluster, had the most hands-on pitch of the day: in 30 minutes, spin up vCluster sandboxes, drop NVIDIA's open-source KAI Scheduler inside, and use fractional GPUs to share expensive hardware across tenants without deadlocks or a cluster per team. Multi-tenant, multi-scheduler, with the YAML to copy.

[Deepika Annam](https://www.conf42.com/Kube_Native_2025_Deepika_Annam_optimization_reinforcement_performance) of Nike went further up the stack, applying deep reinforcement learning to pod scheduling, autoscaling, and resource management. [Jyotirmoy Sundi](https://www.conf42.com/Kube_Native_2025_Jyotirmoy_Sundi_reinforcement_learning_distributed), co-founder and CTO of Votal.ai, covered scaling reinforcement learning with human feedback across distributed cloud systems.

## How many clusters do you really need?

[Arsh Sharma](https://www.conf42.com/Kube_Native_2025_Arsh_Sharma_kubernetes_environments_scalability), Senior DevRel Engineer at MetalBear, asked the question in the title that every platform team should ask: one environment for production, one for staging, one for CI, one per developer so nobody blocks staging. Do you need them all? The talk shows how to reuse existing environments for development and CI, lowering cloud costs and cluster sprawl.

Platform developers also got two takes on simplifying the code itself. [Christophe Gigax](https://www.conf42.com/Kube_Native_2025_Christophe_Gigax_dapr_architectures_cloudnative), Cloud Solution Architect at Hager Group, showed how Dapr exposes state management, pub/sub, and other building blocks as standard APIs, so microservices stop reimplementing them. [Anupama Pathirage](https://www.conf42.com/Kube_Native_2025_Anupama_Pathirage_ballerina_integration_opensource), Head of Engineering for integration at WSO2, presented Ballerina, an open-source language with cloud deployment constructs built into the code.

## Resilience patterns that hold up

The architecture track was strong on concrete patterns. [Rahul Singh Thakur](https://www.conf42.com/Kube_Native_2025_Rahul_Singh_Thakur_sharding_uptime_architecture) of Salesforce gave a practical guide to multi-zone sharded microservices with intelligent request routing. [Karthik Reddy Beereddy](https://www.conf42.com/Kube_Native_2025_Karthik_Reddy_Beereddy_streaming_redis_selfhealing) of LexisNexis Risk Solutions covered self-healing streaming with Redis Streams and Azure Event Hubs, and [Shalini Katyayani Koney](https://www.conf42.com/Kube_Native_2025_Shalini_Katyayani_Koney_kafka_streaming_scalable) of Walmart scaled Kafka on Kubernetes with StatefulSet tuning, autoscaling, and GitOps. [Ashif Anwar](https://www.conf42.com/Kube_Native_2025_Ashif_Anwar_azure_eventdriven_patterns) of Wolters Kluwer and [Dhruvesh Talati](https://www.conf42.com/Kube_Native_2025_Dhruvesh_Talati_resilience_design_recovery) of Ally added event-driven patterns on AKS and architectures for crisis response.

On the observability side, [Alejandro Mercado](https://www.conf42.com/Kube_Native_2025_Alejandro_Mercado_observability_kubernetes_ebpf), DevOps Lead at Michael Page, made the case for eBPF-powered observability for incident detection and root cause analysis, and [Srinivas Pagadala Sekar](https://www.conf42.com/Kube_Native_2025_Srinivas_Pagadala_Sekar_observability_llms_paas) of Karsun Solutions looked at LLM-assisted diagnostics to cut MTTR and alert noise.

## Defence in depth, and the post-quantum clock

[Karthikeyan Thirumalaisamy](https://www.conf42.com/Kube_Native_2025_Karthikeyan_Thirumalaisamy_security_missioncritical_kubernetes), a Principal Software Engineer at Microsoft, laid out a defence-in-depth blueprint for mission-critical services on AKS, EKS, and GKE, covering insider threats, supply chain attacks, and runtime exploits. [Derek Asir Muthurajan Caleb](https://www.conf42.com/Kube_Native_2025_Derek_Asir_Muthurajan_Caleb_quantum_security_infrastructure) of Broadcom looked further ahead, at moving Kubernetes clusters and service-to-service traffic to quantum-resistant cryptography. [Vivek Koodakkara Shanmughan](https://www.conf42.com/Kube_Native_2025_Vivek_Koodakkara_Shanmughan_identity_keycloak_deployment) of Aryaka Networks described a regional hub model for running Keycloak identity across a global SASE deployment, and [Satya Purella](https://www.conf42.com/Kube_Native_2025_Satya_Purella_integration_fintech_platforms) of Fifth Third Bank covered secure integration platforms for fintech.

## AI in regulated industries

The biggest cluster of talks was about running AI on Kubernetes where regulators are watching. In finance, [Ashish Dibouliya](https://www.conf42.com/Kube_Native_2025_Ashish_Dibouliya_banking_compliance_governance) of Webster Bank presented a Kubernetes-ready AI data governance framework with drift detection, [Jaydeep Taralkar](https://www.conf42.com/Kube_Native_2025_Jaydeep_Taralkar_finance_ml_orchestration) of UBS focused on responsible ML at scale, [Kiran Purushotham](https://www.conf42.com/Kube_Native_2025_Kiran_Purushotham_trading_llm_insight) of JPMorgan Chase showed swarms of LLM agents for market insight, and [Manoj Kalakoti](https://www.conf42.com/Kube_Native_2025_Manoj_Kalakoti_finops_costgovernance_autonomous) of Apple embedded FinOps cost governance into the delivery pipeline. [Manisha Sengupta](https://www.conf42.com/Kube_Native_2025_Manisha_Sengupta_finance_risks_modernization) of Brown Brothers Harriman covered the attack vectors that come with AI in finance.

In healthcare, [Tharun Nallamothu](https://www.conf42.com/Kube_Native_2025_Tharun_Nallamothu_copilot_clinical_workflows) of Microsoft presented Dragon Copilot, an AI clinical assistant built around ambient recording for documentation. [Manikesh Iruku](https://www.conf42.com/Kube_Native_2025_Manikesh_Iruku_ehr_pipelines_accuracy) of Amazon built LLM auditing for EHR pipelines, [Amala Umakanth](https://www.conf42.com/Kube_Native_2025_Amala_Umakanth_genai_healthcare_fraud) of McKinsey applied GenAI to claims processing and fraud, and [Venus Garg](https://www.conf42.com/Kube_Native_2025_Venus_Garg_ethical_ai_trust) of Boston University asked whether Kube-native stacks are ready for the bias, privacy, and trust questions healthcare AI raises.

## The rest of the lineup

Data engineering got its own track, including [Sruthi Erra Hareram](https://www.conf42.com/Kube_Native_2025_Sruthi_Erra_Hareram_etl_airflow_optimization) of TELUS Digital on tuning PySpark and Airflow on Kubernetes and [Vamsi Pulusu](https://www.conf42.com/Kube_Native_2025_Vamsi_Pulusu_datapipeline_streaming_modern) of Ford on moving from legacy ETL to streaming and lakehouses. [Bhavana Reddy Chadagonda](https://www.conf42.com/Kube_Native_2025_Bhavana_Reddy_Chadagonda_abtesting_experimentation_careers) of Intuit offered career advice through A/B testing techniques like CUPED. And for something different, [Chandan Kumar](https://www.conf42.com/Kube_Native_2025_Chandan_Kumar_lighting_immersion_responsive) of Google explained pre-computed surround lighting that reacts in under 100ms, while [Preeti Sali](https://www.conf42.com/Kube_Native_2025_Preeti_Sali_ev_charging_infrastructure) of Ford covered cloud-native EV charging infrastructure.

## Sponsors and what's next

Thanks to gold sponsor [SREday](https://www.sreday.com/), the [StarterAI](https://www.starterai.dev/) newsletter, the [HockeyStick](https://www.hockeystick.show/) podcast, and the media partners on the event page.

For earlier editions, start with [Conf42 Kube Native 2024](https://www.conf42.com/kubenative2024). Then go and count your clusters.
