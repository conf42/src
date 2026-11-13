# AI agents across DevSecOps should recommend, not decide

Conf42 Blog, 2026-09-03, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/ai-agents-recommend-humans-approve-devsecops

In short: Deepanshu Kukreja at Conf42 DevSecOps 2026 maps AI agents onto IaC, pipelines, vulnerabilities and incidents, with humans keeping the risky calls.

Most DevSecOps toil isn't hard, it's repetitive: triaging alerts that resolve themselves, eyeballing Terraform for policy violations, sorting scanner output by hand. At Conf42 DevSecOps 2026, Deepanshu Kukreja, a senior DevSecOps engineer with nineteen years in the field, walked through where LLM-powered agents can take that work across the whole lifecycle, and drew a firm line: the agent recommends and escalates, humans keep authority over anything risk-bearing.

It's a short, high-level map rather than a build walkthrough, and that's the right way to watch it: as a checklist of where an agent could sit in your own pipeline.

## Agents as an orchestration layer, wired through MCP

Deepanshu's distinction is between a linear script and an agent that reasons over context and picks which tool to call next. The glue is the Model Context Protocol, and he gives it three jobs: structured tool access through strict schemas instead of free-form execution, scoped permissions for least privilege, and auditability, with every action logged for compliance and forensics.

The abstract lists the systems in scope: Terraform, Kubernetes, GitHub, GitOps pipelines, AWS, Azure, OCI, Splunk, Grafana, CloudWatch, PagerDuty, ServiceNow, security scanners and runbooks. That's a long list of things an agent could break, which is exactly why the talk ends where it does.

## Four places agents earn their keep

**Infrastructure as code.** The agent generates Terraform modules from a plain-language description using your naming conventions, validates them before apply with policy-as-code tools like OPA or Checkov, and keeps running drift detection against the live environment.

**Pipelines and clusters.** On pull requests it looks for exposed secrets and risky dependencies, annotates inline and blocks non-compliant merges. On Kubernetes it audits against CIS benchmarks: namespace isolation, RBAC misconfiguration, privilege escalation, with remediation steps for the developer.

**Vulnerabilities.** Rather than handing engineers thousands of findings, the agent enriches them: CVEs correlated with EPSS scores and public exploit availability, risk weighted by business criticality, findings mapped to frameworks like SOC 2 or FedRAMP, and audit evidence generated along the way.

**Incident response.** The most detailed part is a reusable sixteen-step investigation workflow: pull context from PagerDuty, logs from Splunk, metrics from Grafana, map the blast radius, check historical runbooks for verified mitigations, and look at the history of that exact alert for patterns.

## The alert-tuning loop nobody has time for

The idea worth stealing is small. Engineers stuck firefighting rarely get to look back at an alert's history and tune it so it stops firing. Deepanshu gives that job to the agent: flag short transient spikes and alerts that auto-resolve, separate signal from noise, and propose either a permanent root-cause fix or an alert change. Anyone who has been paged at 3am for a spike that healed before the laptop opened will see the appeal.

## Five guardrail layers, one rule

The guardrails are least-privilege access, a policy-as-code gate on every agent proposal before execution, human-in-the-loop approval for destructive actions, immutable audit trails, and final human authority over risk decisions. In his words, "Automation without control is massive liability." The stated goal is explicitly not full autonomy but governed, auditable assistance.

## Who should watch

Team leads drafting an agent roadmap for a DevSecOps group, and anyone who needs a vocabulary for pitching it to a security review board. If you already run agents in production, the guardrail section is the part to compare against your own setup; the rest will be familiar ground.

## Related Conf42 talks

- [AI Agents for Incident Response: The Good, the Bad, and the Ugly](https://www.conf42.com/DevOps_2026_Vladyslav_Budichenko_incidents_agents_security) by Vladyslav Budichenko at Conf42 DevOps 2026.
- [Tackling Alert Fatigue with SLOs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue) by Mandi Walls at Conf42 SRE 2025.
- [AI Coded It, AI Shipped It, Who Owns It?](https://www.conf42.com/Observability_2026_Ralph_Bird_sre_agents_incidentresponse) by Ralph Bird at Conf42 Observability 2026.

[Watch Deepanshu Kukreja's talk](https://www.conf42.com/DevSecOps_2026_Deepanshu_Kukreja_agents_automation_incidentresponse) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/2JTc8A9jxJw).

## Watch the talk

[AI Agents for DevSecOps: Automating Secure Infrastructure, Delivery, and Incident Response](https://www.conf42.com/DevSecOps_2026_Deepanshu_Kukreja_agents_automation_incidentresponse) at Conf42 DevSecOps 2026.
