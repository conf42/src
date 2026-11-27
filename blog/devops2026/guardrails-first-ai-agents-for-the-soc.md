# Your SOC will ask for AI agents. Ship the guardrails first

Conf42 Blog, 2026-01-22. https://www.conf42.com/blog/devops2026/guardrails-first-ai-agents-for-the-soc

In short: Neal Iyer of Splunk at Conf42 DevOps 2026 on a guardrails-first framework for SOC AI agents, from org context and policy gates to shadow mode.

Neal Iyer, Director of Product Management at Splunk (a Cisco company), opened his Conf42 DevOps 2026 talk with a bet: your security operations colleagues will come to you, the DevOps person, asking for help building and deploying AI agents. His [Guardrails First framework](https://www.conf42.com/DevOps_2026_Neal_Iyer_guardrails_ai_accountability) is what he wants you to have in your pocket when they do: four pillars and a six-phase rollout that keep a non-deterministic model away from your domain controllers.

Iyer is a product manager who says he talks to over 150 SOC teams a year, and the talk reads like it. It's a framework talk, not a product demo, and it applies whether you buy an AI SOC platform or build one in-house.

## Security pays you to be right every time

The tension is stated plainly. SOC teams already had alert fatigue, tool sprawl and a skills shortage; generative AI then made attacks faster, cheaper and easier to launch. Agents look like the only way to keep up. But security is a job where you are paid to be right every single time, and LLMs are variable and sometimes wrong.

His observation about the market is the useful part: the startups and the in-house prototypes all demo very similarly and very well. The hard part is earning enough trust to put one in production. Buy versus build, he argues, is not the fundamental decision.

## Context first: your SOPs are training data

The first pillar is organisational context. The same alert gets triaged differently in two companies, depending on their tools, how their data is laid out and their standard operating procedures. So the agent's curriculum should be your own case notes and the SOPs your lead analysts write.

Two practical warnings come with it. Writing for an agent exposes gaps in existing SOPs, including steps buried in corporate jargon an agent has no way to decode. And every increment needs a back-testing pipeline that runs the agent against alerts your team has already labelled by hand. If you have shipped ML before, that's just an eval set with a security badge.

## Scope the tools, gate the actions

The second pillar is policy constraints. Decide whether an agent enriches, updates tickets or takes response actions, and give it only the tools for that job. An enrichment agent that can't lock accounts can't lock out a domain controller and send the company dark when it reaches the wrong conclusion.

On top of scoping, Iyer wants policy-driven gating: the agent proposes, the proposal is evaluated against policy, and the gate decides whether it executes automatically, escalates to a human, or gets checked after the fact. DevOps engineers will recognise the shape. It's an admission controller for decisions.

## Audit everything, then earn autonomy

Trust comes from a full audit trail: the data the agent used, how it reasoned over it, every action and the final recommendation. He treats complete traceability as a must-have for anything you build or buy.

Autonomy then arrives in stages. Start in shadow mode, visible only to a few SOC leads who judge whether the reasoning holds up. Move to suggestions in the analysts' UI that nobody is obliged to accept. Then grant bounded autonomy for low-risk actions, and keep widening it with feedback. He doesn't see fully autonomous, high-impact actions as sensible with today's technology.

The six-phase blueprint follows the same logic: assess your documentation, pick a narrow low-risk scope (employee-reported phishing emails come up as a common first candidate), design guardrails, build, run in shadow mode, then expose suggestions and grow autonomy. Measure false positives removed, time to analyse, analyst productivity and the accuracy of both recommendations and reasoning.

## Who should watch

Platform and DevOps engineers who will host, wire up or gate a SOC team's agents, and security leads deciding how much autonomy to grant. There's no code here, so if you want implementation detail, pair it with a hands-on agent security talk.

## Related Conf42 talks

- [I Don't Trust AI Agents (And Neither Should You): Building Production-Ready Architectures](https://www.conf42.com/AI_Agents_2026_Morgan_Willis_production_guardrails_trust) by Morgan Willis at Conf42 AI Agents 2026.
- [AI Agents for DevSecOps: Automating Secure Infrastructure, Delivery, and Incident Response](https://www.conf42.com/DevSecOps_2026_Deepanshu_Kukreja_agents_automation_incidentresponse) by Deepanshu Kukreja at Conf42 DevSecOps 2026.
- [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) by Birol Yildiz at Conf42 DevSecOps 2024.

[Watch Neal Iyer's talk](https://www.conf42.com/DevOps_2026_Neal_Iyer_guardrails_ai_accountability) or the [YouTube recording](https://youtu.be/89NFqpH865M).

## Watch the talk

[Guardrails First: Designing Safe, Scalable, and Accountable AI Agents for Security Operations](https://www.conf42.com/DevOps_2026_Neal_Iyer_guardrails_ai_accountability) at Conf42 DevOps 2026.
