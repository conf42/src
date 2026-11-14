# Asking Azure why it returns 503s, in plain English

Conf42 Blog, 2026-05-15, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/azure-copilot-diagnostics-database-teams

In short: Sampath Rao Madarapu of Microsoft at Conf42 Database DevOps 2026 on Copilot in Azure for diagnostics, governance and database operations, with humans in the loop.

Diagnosing an Azure incident usually means five portal blades, a Log Analytics query and some manual timestamp matching. At Conf42 Database DevOps 2026, Sampath Rao Madarapu, Senior Technical Advisor in Azure infrastructure support at Microsoft, presented Copilot in Azure, the AI assistant built into the Azure management experience, and focused on what it does for database and DevOps teams.

This is a Microsoft product talk from someone on the support front line, so it is an overview of capabilities rather than a hands-on demo. The most interesting part is how the human side of the system works.

## The problem is context switching

Azure has hundreds of services and thousands of resource types. A team running Azure SQL, Cosmos DB or PostgreSQL deals with interconnected configurations where a small change can cascade, and under incident pressure it bounces between portal, CLI, dashboards and docs. Sampath's sharpest point is about knowledge: the know-how that says "this error pattern means check the connection pool" lives in a few heads and does not scale across teams and regions.

## Three layers behind the chat box

Copilot combines large language models that interpret the question, Azure control plane data (live resource metadata, ARM configurations, subscription topology), and real-time telemetry such as metrics, diagnostic logs and health signals. The point of the last two is grounding: answers about your resources in their current state, not generic documentation.

The examples he gives are the kind of thing you would actually type: which VMs in a subscription are not patched, which SQL databases are above 80% DTU utilization, or why an App Service is returning 503 errors. For the last one Copilot correlates Azure Monitor, Application Insights and resource diagnostics into one summary with a root cause hypothesis and suggested next steps such as scaling or configuration changes. Sampath's claim is that what used to take an hour of investigation can now take minutes.

## Database teams get the most specific help

For data platforms the integration covers Azure SQL, Cosmos DB, Synapse Analytics, PostgreSQL and MySQL. He lists four uses: query performance analysis (slow queries, missing indexes, DTU versus vCore utilization without parsing Query Store or DMV output by hand), security posture review of firewall rules, encryption and audit settings, capacity guidance for tiers, elastic pools and read replicas based on actual telemetry, and validation of backup policies, retention windows and geo-redundancy across all databases at once.

On the governance side, the same interface summarizes resources for incident triage or onboarding, finds untagged or misconfigured resources, checks RBAC role assignments at scale, and flags violations against Azure Policy and Defender for Cloud baselines.

## The AI is trained by support engineers

The section worth the watch is how Copilot's diagnostic intelligence is kept honest. Sampath describes four human stages: engineers validate that metrics map to the right diagnostic scenarios; technical advisors like him review outputs for accuracy and find edge cases; trusted troubleshooting runbooks are written into the knowledge base; and feedback from real use flows back into grounding and prompt tuning as services change.

The trust rules follow from that. Responses cite the telemetry and configuration behind them, the reasoning is shown so you can check it, and Copilot does not autonomously execute destructive or irreversible actions. The engineer stays the decision-maker, which is the right default for anything that can resize a production database.

## Who should watch

Azure database and DevOps teams evaluating Copilot in Azure, and anyone designing an internal ops assistant who wants a template for grounding and human review. If you are not on Azure, the four-stage human-in-the-loop model is the transferable part.

## Related Conf42 talks

- [Susanta Kumar Sahoo on copilots for SRE remediation](https://www.conf42.com/Large_Language_Models_LLMs_2026_Susanta_Kumar_Sahoo_copilots_sre_remediation) at Conf42 Large Language Models 2026.
- [Carlos Solis Salazar on Azure management and security](https://www.conf42.com/DevSecOps_2024_Carlos_Solis_Salazar_azure_management_security) at Conf42 DevSecOps 2024.
- [Peter De Tender on Microsoft Copilot capabilities](https://www.conf42.com/Prompt_Engineering_2024_Peter_De_Tender_copilot_capabilities_microsoft) at Conf42 Prompt Engineering 2024.

[Watch Sampath Rao Madarapu's talk](https://www.conf42.com/Database_DevOps_2026_Sampath_Rao_Madarapu_azure_cloud_monitoring)

[Watch the talk on YouTube](https://youtu.be/BlRzRJs1SEc).

## Watch the talk

[AI Assisted Azure Ops with Copilot for Diagnostics and Resource Control](https://www.conf42.com/Database_DevOps_2026_Sampath_Rao_Madarapu_azure_cloud_monitoring) at Conf42 Database DevOps 2026.
