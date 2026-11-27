# AI agents on call multiply your speed and your mistakes

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/ai-agents-incident-response-good-bad-ugly

In short: Vladyslav Budichenko of Vocaly AI at Conf42 DevOps 2026 on where AI agents help incident response, where they go wrong, and prompt injection via logs.

Here is an incident nobody budgets for: an attacker writes a prompt into a request, it lands in your logs, and during the next investigation your helpful AI agent reads it and does what it says. At Conf42 DevOps 2026, Vladyslav Budichenko, a senior software engineer at Vocaly AI with a background in platform and observability engineering, sorted AI agents for incident response into the good, the bad and the ugly. His verdict: use them as a force multiplier, and remember that they multiply your mistakes too.

It is a practitioner's talk with no product pitch, from someone who uses Claude Code, Cursor and custom agents day to day.

## The good: gathering and correlating, fast

The slow part of most investigations is not the fix. It is pulling the alert context, checking the playbook, gathering logs and metrics from several systems and correlating them: the service is failing, and CPU is high. That is exactly what an agent does well. Budichenko points to the commercial wave (Datadog, PagerDuty, Honeycomb's MCP, New Relic) and to the open-source route: wire Claude, Cursor, Codex or your own agent into Loki, Tempo or an ELK stack.

The enabler is MCP, the Model Context Protocol, which replaced everyone writing their own API glue. One agent can search Slack for a similar discussion from a year ago, check the Jira ticket behind a deployment, read telemetry in Datadog or Grafana, look up the page in PagerDuty and open the code in GitHub.

## The bad: rabbit holes, garbage in, context limits

Agents can dig without end: fetch, analyse, fetch more, try a change, crash, repeat. You have to bound them. Garbage in, garbage out still applies: without good alerts, decent telemetry and access to it, the agent has nothing useful to reason over. And even million-token windows run out when you pour raw logs into them, so you scope by time (the incident window plus or minus about ten minutes, widened only if needed) and reduce log volume with tooling first.

His structural fix is a swarm rather than one generalist: narrow agents that collect logs, metrics or events, an analytical agent working from a playbook, and an orchestrator on top. Focused agents give better answers.

## The ugly: rubber stamps and prompt injection

The worst failures are human. Engineers approve agent output without reading it, so human-in-the-loop quietly stops being a loop. Senior skills erode, and juniors lose the chance to learn because some companies decided seniors with AI were enough.

Then security. Budichenko compares prompt injection to SQL injection two decades ago, and the log vector above is the scary version: data you investigate becomes instructions. The mitigations are the ones you would expect, applied without exceptions: restrict which tools an agent can call and what it can reach on the internet, run read-only by default, and require approval for everything else.

## Who should watch

SREs and on-call leads deciding how much autonomy to hand an investigation agent, and anyone already running one in YOLO mode. The takeaway is a clear split: trust agents for data gathering, aggregation, pattern recognition and first-pass analysis; verify everything else; never let them take high-risk actions unapproved.

## Related Conf42 talks

- [Deepanshu Kukreja on AI agents for secure infrastructure, delivery and incident response](https://www.conf42.com/DevSecOps_2026_Deepanshu_Kukreja_agents_automation_incidentresponse) at Conf42 DevSecOps 2026.
- [Ralph Bird asks who owns code that AI wrote and shipped](https://www.conf42.com/Observability_2026_Ralph_Bird_sre_agents_incidentresponse) at Conf42 Observability 2026.
- [Anurag Gupta on using generative AI to fix outdated runbooks](https://www.conf42.com/Incident_Management_2023_Anurag_Gupta_generative_ai_fix_runbooks) at Conf42 Incident Management 2023, the playbooks your agents will read.

[Watch Vladyslav Budichenko's talk](https://www.conf42.com/DevOps_2026_Vladyslav_Budichenko_incidents_agents_security)

[Watch the talk on YouTube](https://youtu.be/xMiKK123-Ac).

## Watch the talk

[AI Agents for Incident Response: The Good, the Bad, and the Ugly](https://www.conf42.com/DevOps_2026_Vladyslav_Budichenko_incidents_agents_security) at Conf42 DevOps 2026.
