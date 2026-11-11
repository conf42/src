# Conf42 DevOps 2026 - agents joined the pipeline, failover got boring

Conf42 Blog, 2026-01-23. https://www.conf42.com/blog/devops2026/devops-2026-roundup-agents-in-the-pipeline

In short: Conf42 DevOps 2026 in review, 47 talks on agents in CI/CD and on-call, infrastructure as a graph, boring failover, CI-gated SLOs and what green CI misses.

[Conf42 DevOps 2026](https://www.conf42.com/devops2026) opened the Conf42 year on January 22, 2026 with 47 talks. The loudest question was what happens when AI agents get commit rights, pipeline access and a seat on the on-call rota. The quieter, equally useful one was how to make the old hard things (region failover, migrations, compliance) dull enough that nobody needs a hero. Speakers came from Intuit, Google, Disney, Meta, Microsoft, Cisco, Splunk, Twilio, Workday, Oracle, ASML, Harness and more.

## Agents in CI/CD and on call, with the brakes attached

Diamond sponsor Harness set the frame. [Chinmay Gaikwad](https://www.conf42.com/DevOps_2026_Chinmay_Gaikwad_cicd_agentic_ai) argued that AI made writing code cheap and moved the bottleneck after the commit, then laid out an enterprise-ready pipeline built by agents: a knowledge graph for context, policies enforced outside the prompt, and RBAC that treats the AI as an extension of the user, so if you can't deploy to production, neither can your agent.

[Neeraj Kumar Singh Beshane](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity) (Meta) proposed GenOps, a governance-first model for letting generative agents act inside CI/CD. [Vladyslav Budichenko](https://www.conf42.com/DevOps_2026_Vladyslav_Budichenko_incidents_agents_security) (Vocaly AI) gave agents in incident response the good, the bad and the ugly treatment, including how to use them safely with MCP. [Neal Iyer](https://www.conf42.com/DevOps_2026_Neal_Iyer_guardrails_ai_accountability) (Splunk) brought the same "guardrails first" stance to agents in the security operations centre, keeping human control in the loop. On the infrastructure side, [Praneeth Patil](https://www.conf42.com/DevOps_2026_Praneeth_Patil_autonomous_infrastructure_cloud) (Equinix) described LLM-driven multi-cloud infrastructure that catches misconfigurations, and [Premanand Tiwari](https://www.conf42.com/DevOps_2026_Premanand_Tiwari_forecasting_time_autonomy) (Amazon) demoed autonomous time-series forecasting for capacity planning.

## Infrastructure is a graph, so give the model the graph

Context engineering got its own cluster. [Roxane Fischer](https://www.conf42.com/DevOps_2026_Roxane_Fischer_context_reasoning_infrastructure) (Anyshift) explained why LLMs fail at infrastructure: they can't see live dependencies or multi-hop relationships. Her answer is to model infrastructure as a graph, query it with Graph RAG and natural-language-to-Cypher, and measure context quality. [Pronnoy Goswami](https://www.conf42.com/DevOps_2026_Pronnoy_Goswami_observability_queries_context) (Workday) used the Model Context Protocol to make telemetry queryable, and [Michael Levan](https://www.conf42.com/DevOps_2026_Michael_Levan_agents_telemetry_costs) (Solo.io) asked the two questions every platform team now hears about agentic and MCP traffic: how do we observe it, and how do we keep the bill sane. [Tina Kanth](https://www.conf42.com/DevOps_2026_Tina_Kanth_finops_streaming_prompts) (Microsoft) showed prompt templates that turn streaming financial events into structured, auditable triage decisions.

## Make failover boring

The most satisfying talks were about removing drama. [Akshay Pratinav](https://www.conf42.com/DevOps_2026_Akshay_Pratinav_failover_resilience_workloads) (Intuit) described a Kubernetes-native platform where services onboard declaratively to region failover: pre-scale from live traffic, promote standby databases, shift routes through Route53 and Istio. The goal, in his words, is to make failover boring, which is the highest compliment in operations.

[Harris Baskaran](https://www.conf42.com/DevOps_2026_Harris_Baskaran_kubernetes_modernization_containers) (Google) walked a high-volume ticketing monolith from VMware and Oracle to GCE, then rebuilt it cloud-native on GKE and PostgreSQL, with dependency mapping, replication and multi-region DR lessons along the way. [Kalyan Inturi](https://www.conf42.com/DevOps_2026_Kalyan_Inturi_availability_migration_gateways) (Oracle Cloud Infrastructure) used shadow traffic and phased rollouts for a zero-downtime gateway migration. [Nikhil Kokal](https://www.conf42.com/DevOps_2026_Nikhil_Kokal_apis_scalability_reliability) (The Walt Disney Company) covered architectures for APIs at billions of requests, and [Srinivas Pagadala Sekar](https://www.conf42.com/DevOps_2026_Srinivas_Pagadala_Sekar_gitops_resilience_automation) (Karsun Solutions) built self-healing pipelines with Tekton and Argo CD.

## Observability as a contract, not a nice-to-have

[Sumit Kaul](https://www.conf42.com/DevOps_2026_Sumit_Kaul_slos_instrumentation_observability) (Payjoy) made observability a platform contract: zero-code instrumentation and SLOs gated in CI/CD, so a service cannot ship without traces and metrics. [Mohit Gupta](https://www.conf42.com/DevOps_2026_Mohit_Gupta_gpu_ci_validation) (Intel) applied the same idea to GPU performance, catching compute and memory bottlenecks in the pipeline instead of in production. [Aravind Sekar](https://www.conf42.com/DevOps_2026_Aravind_Sekar_reliability_prevention_ai) (Twilio) and [Raghu Bhupatiraju](https://www.conf42.com/DevOps_2026_Raghu_Bhupatiraju_predictive_analytics_outages) (Expeditors) both pushed from firefighting towards prediction, the latter for supply chain systems.

## Green checkmarks are not the whole story

[Tilda Udufo](https://www.conf42.com/DevOps_2026_Tilda_Udufo_cicd_quality_testing) (Outreachy) gave one of the event's sharpest reminders: passing tests don't guarantee quality, as the XZ Utils incident showed, and review practice and culture have to cover what automation misses. [Bhaskar Sawant](https://www.conf42.com/DevOps_2026_Bhaskar_Sawant_security_automation_pipelines) mapped how AI-driven development changes the pipeline attack surface. [Gian Wild](https://www.conf42.com/DevOps_2026_Gian_Wild_accessibility_security_inclusion) (AccessibilityOz) took apart the idea that security and accessibility must trade off against each other. Hands-on security tooling came from [Nikolay Milyaev](https://www.conf42.com/DevOps_2026_Nikolay_Milyaev_xdr_security_analytics) (Microsoft) on Defender XDR alert fatigue, [Gareth Emslie](https://www.conf42.com/DevOps_2026_Gareth_Emslie_sentinel_security_automation) (Dynatrace) on extending Microsoft Sentinel, and [Gurdeep Gill](https://www.conf42.com/DevOps_2026_Gurdeep_Gill_firewalls_ai_protection) (Cisco) on NGFWs for AI workloads. [Imran Abdul](https://www.conf42.com/DevOps_2026_Imran_Abdul_sdwan_networking_automation) (Pace University) brought GitOps to the enterprise network, SD-WAN and zero trust included.

## Regulated and physical systems

Compliance and industry talks rounded out the programme: [Pooja Ranjan](https://www.conf42.com/DevOps_2026_Pooja_Ranjan_compliance_saas_governance) (Oracle) on continuous compliance for SaaS, [Vivek Chittireddy](https://www.conf42.com/DevOps_2026_Vivek_Chittireddy_privacy_regulation_security) (Meta) on privacy by design with differential privacy and anonymisation in the pipeline, [Swapna Chimanchodkar](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai) (Cognizant) on deploying real-time sepsis detection, and [Rasmi Ranjan Nayak](https://www.conf42.com/DevOps_2026_Rasmi_Ranjan_Nayak_embedded_robotics_ai) (ASML) on deterministic embedded AI for robotics.

## Sponsors and where to watch

Thanks to [Harness](https://www.harness.io/), the Diamond sponsor, and [SREday](https://www.sreday.com/) at Gold. All 47 talks are on the [event page](https://www.conf42.com/devops2026) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrB6SG3pv3bmTo7NWFlCGiNx).

The series returns with [Conf42 DevOps 2027](https://www.conf42.com/devops2027).
