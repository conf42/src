# Conf42 Cloud Native 2026: agents become infrastructure

Conf42 Blog, 2026-04-24. https://www.conf42.com/blog/cloud2026/conf42-cloud-native-2026-roundup

In short: Conf42 Cloud Native 2026 roundup: 29 talks on running AI agents like services, securing MCP and cloud automation, migrations and EU compliance on AWS.

Conf42 Cloud Native 2026 ran online on April 23, 2026, with 29 talks under the familiar promise of *everything Cloud Native and Cloud Security*. The thread running through the day: AI agents and MCP servers are turning into ordinary infrastructure, with all the lifecycle, security and cost problems that implies, while the older cloud questions of migration, compliance and observability haven't gone anywhere. The full lineup is on the [event page](https://www.conf42.com/cloud2026) and the recordings are in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrAk91tnHP48BKjDFW9jzf1V).

## Agents need the tooling pods already have

[Andrew Espira](https://www.conf42.com/Cloud_Native_2026_Andrew_Espira_ai_agents_automation) of Kustode asked the question several other speakers circled: you have `kubectl` for pods, `docker` for containers and `helm` for charts, so what do you use for the agents and MCP servers piling up on your machine and in your cluster? His answer is `agentctl`, a zero-dependency Go CLI that registers, health-checks, starts, stops and discovers them like any other managed service, with a live TUI dashboard on top.

[Elizabeth Fuentes Leone](https://www.conf42.com/Cloud_Native_2026_Elizabeth_Fuentes_Leone_ai_llm_applications) of AWS tackled a cost problem that grows with every tool you add: agents serialise every tool description into the context on every call, then pick the wrong tool anyway. Her semantic tool selection uses vector search to filter tools before they reach the model. [Sandeep Mannapur](https://www.conf42.com/Cloud_Native_2026_Sandeep_Mannapur_ai_agents_workflows) of ServiceNow covered what changes when a single chat interface becomes a distributed system of collaborating agents running real workflows, and [Dhivya Dhayakar](https://www.conf42.com/Cloud_Native_2026_Dhivya_Dhayakar_ai_llm_prompts) of Zscaler proposed intent-based orchestration as the fix for enterprises with a dozen isolated copilots and no shared governance.

## The new plumbing is a new attack surface

If agents are infrastructure, so are their connectors. [Aleksandr Pinaev](https://www.conf42.com/Cloud_Native_2026_Aleksandr_Pinaev_security_vulnerabilities_compliance), founder of Swordfish Security, catalogued how cloud MCP servers fail: misplaced trust boundaries, excessive privileges, weak isolation and vulnerable connector logic, plus the defences that work.

Older automation got the same scrutiny. [Leo Visser](https://www.conf42.com/Cloud_Native_2026_Leo_Visser_cloudarchitecture_infra_design) of OGD ICT-diensten asked whether your PowerShell and other cloud automation is quietly creating attack surface of its own. Security engineer [Aleksandra Drobnjak](https://www.conf42.com/Cloud_Native_2026_Aleksandra_Drobnjak_security_zerotrust_encryption) walked through real Azure attack techniques from Microsoft's Digital Defense Report, from hybrid identity abuse to trusted relationships, with demos. And [Rajasingh Gandhi Ramdas](https://www.conf42.com/Cloud_Native_2026_Rajasingh_Gandhi_Ramdas_distributed_systems_architecture) of IBM looked further out, at moving multi-cloud APIs off RSA and elliptic curve cryptography before quantum computers make that urgent.

## Migrations without the big bang

Harness's keynote came from [Ryan Vila](https://www.conf42.com/Cloud_Native_2026_Ryan_Vila_feature_flags_migration), who argued that migrations fail because of how they're released, not how they're coded. Flags route traffic gradually from old service to new, and measuring from the point of change makes regressions visible that fleet-wide dashboards would hide. His case study from Split, the company Harness acquired, moved a batch pipeline to streaming behind a flag and cut processing time from 10 hours to 15 minutes.

[Ran Tao](https://www.conf42.com/Cloud_Native_2026_Ran_Tao_data_analytics_insights) of AWS explained why lift and shift doesn't work for messaging systems moving from on-premises to the cloud. [Devinder Tokas](https://www.conf42.com/Cloud_Native_2026_Devinder_Tokas_cloudarchitecture_backend_systems) of Microsoft made the case for interoperability by design to avoid lock-in across clusters and clouds, and [Purushotham Jinka](https://www.conf42.com/Cloud_Native_2026_Purushotham_Jinka_ai_llm_optimization) of Citi traced how partitioning and indexing strategies change when databases go cloud-native.

## Compliance as an engineering problem

The most opinionated talk of the day was [Dmytro Hlotenko's](https://www.conf42.com/Cloud_Native_2026_Dmytro_Hlotenko_distributed_systems_resilience) "Keep Calm and Run on AWS". Dmytro, a senior cloud operations engineer at Sage in Austria, offered a practitioner's defence of running AWS in regulated European environments: what actually needs solving, what is compliance theatre, where Outposts helps and where it quietly fails, and how to keep a stack your team can still operate at 3am. He opened with a disclaimer that he's an engineer, not a lawyer, which is more than most sovereignty debates manage.

[Manasa Uppula](https://www.conf42.com/Cloud_Native_2026_Manasa_Uppula_data_streaming_realtime) treated digital onboarding in financial services as an architecture problem, where consent boundaries and interaction integrity have to be audit-ready by design. [Karthik Ravva](https://www.conf42.com/Cloud_Native_2026_Karthik_Ravva_ai_agents_reasoning) of Austin Energy argued that data governance has to be embedded in the lifecycle once AI-powered BI depends on it.

## Operations and real systems in production

[Uudit Misra](https://www.conf42.com/Cloud_Native_2026_Uudit_Misra_distributed_systems_reliability) of Salesforce asked why dashboards show green while users see failures, and answered with eBPF-based network observability for Kubernetes, deployed as DaemonSets instead of relying on iptables and sidecars. [Sampath Rao Madarapu](https://www.conf42.com/Cloud_Native_2026_Sampath_Rao_Madarapu_distributed_systems_scaling) of Microsoft showed Copilot in Azure as an assistant for diagnostics and resource management.

Two case studies stood out for being about systems that run today. [Anton Solomonov](https://www.conf42.com/Cloud_Native_2026_Anton_Solomonov_computer_vision_verification) of SIMPLE described a computer vision system that verifies spare parts at warehouse receiving for a manufacturer supplying the mining industry, with confidence thresholds, exception handling and human-in-the-loop checks for parts that look nearly identical. [Gautham Paspala](https://www.conf42.com/Cloud_Native_2026_Gautham_Paspala_data_warehousing_analytics) of ServiceNow tackled friendly fraud, where a legitimate purchase becomes a fraudulent dispute weeks later, using temporal graph attention and transformers.

## Sponsors

Thanks to [Harness](https://www.harness.io/), our diamond sponsor, to gold sponsors [SREday](https://www.sreday.com/) and [Virtana](https://www.virtana.com/), and to [HockeyStick](https://www.hockeystick.show/) for the podcast partnership.

## What's next

All 29 talks are linked from the [Conf42 Cloud Native 2026 page](https://www.conf42.com/cloud2026). The series returns with [Conf42 Cloud Native 2027](https://www.conf42.com/cloud2027) on April 8, 2027, by which point your MCP servers will presumably need their own on-call rotation.
