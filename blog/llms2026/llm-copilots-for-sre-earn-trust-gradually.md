# LLM copilots for SRE should earn their trust one risk tier at a time

Conf42 Blog, 2026-06-14, updated 2026-11-09. https://www.conf42.com/blog/llms2026/llm-copilots-for-sre-earn-trust-gradually

In short: Principal SRE Susanta Kumar Sahoo at Conf42 LLMs 2026 on LLM copilots that summarize alerts, correlate deploys and auto-remediate under human guardrails.

An LLM copilot that summarizes a PagerDuty storm into a couple of lines is useful on day one. One that rolls back production on its own has to earn that right. Susanta Kumar Sahoo, a Principal Site Reliability Engineer with two decades in the field (SAP Labs, Yahoo, Goldman Sachs, Apple, Verizon, Autodesk and Zscaler among his stops), made that case at Conf42 Large Language Models 2026: copilots should take over incident work gradually, from low risk to high risk, with humans keeping the strategic calls.

This is an overview from a practitioner, not a deep implementation walkthrough, and it is best taken as a map of where LLMs fit in the incident lifecycle.

## Drowning in telemetry

Sahoo starts with the setup most SREs live in: architectures spread across clouds, regions and Kubernetes clusters for high availability, provisioned with Terraform and friends, each emitting logs, metrics, traces and deploy events. Nobody can hold all of that in their head at 3 a.m. Engineers spend more time filtering alert noise than fixing anything.

His history of incident response has three eras: manual dashboards and escalation chains, AIOps with anomaly detection and event correlation, and now natural language reasoning. Instead of building a query, you ask what changed before the outage, or for rollback options for this incident, and the copilot searches past incidents and recent releases for you.

## What the copilot actually does

The architecture he describes is layered. At the bottom, telemetry: logs, metrics, traces and deployment history, all fed into a knowledge base. On top, dashboards in Grafana, Datadog or Splunk for engineers, leaders and the business. Then the LLM layer, which correlates those signals and can trigger StackStorm or Rundeck jobs and Kubernetes or cloud API calls.

During an incident the copilot checks the usual suspects after a release (API latency spikes, database saturation, slow queries, node instability, upstream and downstream dependencies), builds the incident timeline, lists affected services and business units, and suggests diagnostic commands. Paired with PagerDuty, it summarizes the alert flood and points at the probable area.

The abstract cites a case study where an LLM chatbot integrated with PagerDuty cut mean time to detect by 31 percent, and LLM-assisted remediation brought up to 42 percent fewer repeat incidents.

## Auto-remediation, carefully

The remediation examples are the classic ones: restart unhealthy containers, roll back fast when alerts follow a deploy and investigate afterwards, scale pods and nodes, and fail over to a disaster recovery region. On failover he adds a useful warning: if one of thirty applications fails over to another region, measure the cross-region latency it introduces for everything else. Chaos engineering is how you learn whether one app can move alone or the whole estate has to go together.

That is also his model for trust. Use chaos experiments to learn your strengths, weaknesses and unknowns, then hand the copilot control step by step, from development environments to production, low-risk actions first. High-risk actions keep explicit human approval. Policies restrict which systems the LLM may touch, knowledge comes only from trusted internal sources, and every AI action is logged and reviewed.

## The unsolved parts

Sahoo is open about what still hurts: context windows versus vast telemetry, inference latency during an incident, sensitive telemetry that needs governance or separate models, model drift, and cost. He also argues that one observability platform beats a patchwork of Splunk, Datadog, New Relic and Dynatrace bought team by team, because the copilot is only as good as the data it can reach.

Looking ahead, he expects multimodal analysis across logs, traces and dashboards, predictive remediation, digital twin testing of remediations before production, and anonymized reliability insights shared across companies.

## Who should watch

SRE leads and on-call engineers planning where an LLM should sit in their incident process, and managers who need a sane rollout order for auto-remediation. Engineers wanting prompt designs or code will find it high level.

## Related Conf42 talks

- [AI-Assisted Incident Response Using LLMs and MCP in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Makarand_Gujarathi_assisted_incident_response) from Conf42 SRE 2026 shows a concrete MCP-based take.
- [AI Agents for DevSecOps: Automating Secure Infrastructure, Delivery, and Incident Response](https://www.conf42.com/DevSecOps_2026_Deepanshu_Kukreja_agents_automation_incidentresponse) from Conf42 DevSecOps 2026 adds the security angle.
- [Feature Flags as Incident Evidence: Safer AI-Assisted RCA Workflows](https://www.conf42.com/Feature_Flags_2026_Ishan_Shah_flags_incident_rca) from Conf42 Feature Flags 2026 is about feeding the copilot better evidence.

[Watch Susanta Kumar Sahoo's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Susanta_Kumar_Sahoo_copilots_sre_remediation)

[Watch the talk on YouTube](https://youtu.be/H8kYH2BbJpA).

## Watch the talk

[LLM Copilots for SRE: Transforming Incident Response and Auto-Remediation](https://www.conf42.com/Large_Language_Models_LLMs_2026_Susanta_Kumar_Sahoo_copilots_sre_remediation) at Conf42 Large Language Models (LLMs) 2026.
