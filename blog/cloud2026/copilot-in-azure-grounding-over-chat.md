# Copilot in Azure is only useful because it's grounded in your telemetry

Conf42 Blog, 2026-04-11. https://www.conf42.com/blog/cloud2026/copilot-in-azure-grounding-over-chat

In short: Sampath Rao Madarapu of Microsoft at Conf42 Cloud Native 2026 on Copilot in Azure: grounding in live telemetry, read-first safeguards and a staged rollout.

The interesting part of an ops copilot isn't the chat box, it's what the answers are grounded in. At Conf42 Cloud Native 2026, [Sampath Rao Madarapu](https://www.conf42.com/Cloud_Native_2026_Sampath_Rao_Madarapu_distributed_systems_scaling), Senior Technical Advisor at Microsoft working in Azure infrastructure support, walked through how Copilot in Azure combines an LLM with live resource data, and why he insists on "augmented", not automated or autonomous.

This is a Microsoft engineer talking about a Microsoft product, from the support side rather than the marketing side. There's no live demo; it's architecture, scenarios and adoption advice.

## You are the integration layer

He starts with the toil. Diagnosing one VM issue can mean ten or more portal blades: the VM config, attached disks, network security groups, Azure Monitor metrics, Log Analytics queries, then dependencies across resource groups, all before root-cause analysis begins. Metrics, logs and configuration live in different tools that don't talk to each other in context, so the engineer stitches them together by hand. At scale, he argues, operational toil costs more than the infrastructure.

## Three layers, and the outer one matters most

He describes Copilot as three concentric layers. The core is the LLM engine that interprets intent and reasons. Around it sits the natural-language interface that captures context, like which resource you are looking at. The outer layer is the Azure control plane itself: live telemetry, Resource Manager APIs and resource data.

That outer ring is the point of the talk. His line: "Grounding is what makes AI operationally useful." A generic model can list what might cause high CPU. A grounded one can tell you this VM is hitting its uncached throughput limit because these specific disks are at their IOPS ceiling. The sources he lists are Azure Resource Graph for inventory and relationships, Azure Monitor and Log Analytics for metrics and logs, Resource Manager APIs for configuration and policy state, and diagnostic telemetry for edge and cloud health.

## What it looks like on a normal day

The scenarios are concrete. Ask why an App Service shows elevated latency and get metrics, recent config changes and dependency health in one reply. List every storage account without private endpoints across subscriptions without writing KQL. Find dev VMs that have been underutilised for three days and get right-sizing suggestions. The same model extends to Arc-enabled infrastructure at the edge.

## The safeguards are the product

He is direct that engineers stay in the loop. Humans validate that the telemetry Copilot cites reflects real behaviour, judge whether a design suggestion fits the customer's SLAs, and write the runbooks that steer it. Three safeguards make it enterprise-ready in his view: explainable responses that show data sources, a read-first design where Copilot queries and explains but every change is started and confirmed by a human, and Azure RBAC, so it can't surface data you aren't allowed to see.

## Start where the risk is low

His rollout advice is four steps. First, fix your telemetry baseline (Azure Monitor, Log Analytics, Resource Graph), because Copilot is only as good as that data. Then use it for diagnostics, config queries and policy reviews. Then build internal prompt patterns and playbooks. Only then move to cost optimisation and capacity planning, with human review at each step.

## Who should watch

Azure operators and SRE teams weighing AI-assisted tooling, and anyone building an internal ops assistant on another cloud: the grounding and read-first lessons transfer directly.

## Related Conf42 talks

- [Exploring Copilot Capabilities](https://www.conf42.com/Prompt_Engineering_2024_Peter_De_Tender_copilot_capabilities_microsoft) by Peter De Tender at Conf42 Prompt Engineering 2024.
- [LLM Copilots for SRE: Transforming Incident Response and Auto-Remediation](https://www.conf42.com/Large_Language_Models_LLMs_2026_Susanta_Kumar_Sahoo_copilots_sre_remediation) by Susanta Kumar Sahoo at Conf42 Large Language Models (LLMs) 2026.
- [AI Assisted Azure Ops with Copilot for Diagnostics and Resource Control](https://www.conf42.com/Database_DevOps_2026_Sampath_Rao_Madarapu_azure_cloud_monitoring), Madarapu's companion session at Conf42 Database DevOps 2026.

[Watch Sampath Rao Madarapu's talk](https://www.conf42.com/Cloud_Native_2026_Sampath_Rao_Madarapu_distributed_systems_scaling) or the [YouTube recording](https://youtu.be/W8wLlbx7LMA).

## Watch the talk

[AI-Augmented Azure Ops: Copilot for Intelligent Cloud Resource Management](https://www.conf42.com/Cloud_Native_2026_Sampath_Rao_Madarapu_distributed_systems_scaling) at Conf42 Cloud Native 2026.
