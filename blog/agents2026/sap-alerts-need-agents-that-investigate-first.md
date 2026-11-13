# SAP alerts need agents that investigate before a human wakes up

Conf42 Blog, 2026-09-09, updated 2026-11-09. https://www.conf42.com/blog/agents2026/sap-alerts-need-agents-that-investigate-first

In short: Pon Murugesh Devendren (Deloitte) at Conf42 AI Agents 2026: five event-driven agents on SAP BTP that turn a Cloud ALM alert into an approved fix.

SAP Cloud ALM is good at saying something broke and silent on what to do next. At Conf42 AI Agents 2026, Pon Murugesh Devendren, a Manager at Deloitte working as an AI architect on a large US utility engagement, showed a multi-agent design on SAP Business Technology Platform that does the investigation before the operator opens a single log, then stops and waits for a human to approve the fix.

## The alert is where the work starts

His framing of the problem is one every on-call engineer will recognise. When an alert fires, four things still have to happen by hand: figuring out which systems, interfaces, jobs or business processes are actually affected; searching logs, runbooks and old tickets across tools that each want their own login; working out who the right resolver group and approver are; and digging up the fix someone found at 2 a.m. six months ago, which now lives in a ticket comment nobody will read.

The goal, as he put it, is not to replace operators. It is to hand them an incident where the first round of investigation is already done.

## Five agents, one job each

Instead of one large assistant, the architecture splits the work into five specialised agents: triage and classification, context and correlation, knowledge and root cause, resolution and coordination, and remediation and validation. Each one gets a narrow set of permissions and a clean handoff to the next, so it can be tested on its own, and the line between recommending and executing sits exactly where the governance needs it.

The agents are not polling. A qualifying alert created or updated in Cloud ALM triggers the workflow on demand, and the workflow keeps a correlation ID and shared incident state that every agent reads and writes. Without that shared state, in his words, you would have five agents having five separate conversations. The same framework covers integration failures (IDocs, RFCs, proxies), ABAP dumps and failed jobs, and connectivity or authorisation problems. Between those categories only the runbook and the allowlisted actions change, never the architecture.

## Most of an incident is investigation

The worked example is a failed IDoc posting to SAP ERP after retries ran out. The agents pull the IDoc payload, the ERP posting logs, recent GL account changes, known errors and a similar incident from months earlier. They propose a hypothesis with evidence attached: the GL account was locked for month-end close, so release the lock and reprocess the IDoc. An operator checks that in Microsoft Teams, approves, the action runs, and the validation agent confirms the order is now posted with no downstream errors. His point: the fix took five minutes, while finding it used to take an hour.

Grounding is strict. Retrieval runs through SAP AI Core and the Generative AI Hub with a vector engine over a curated corpus of runbooks, known-error articles and incident history, and nothing is answered from the model's memory. The operator gets a decision-ready briefing in Teams (scope, evidence, recommended action, risk level, who must approve) and can ask follow-up questions in the same thread. Tickets and coordination go through ServiceNow.

## Approval is architecture, not a checkbox

The slide he asked the audience to remember is the governance one. Remediation is limited to allowlisted, parameterised workflows; the system never generates and runs arbitrary commands. Anything that could touch production needs an authorised human, and every alert, piece of evidence, approval and outcome lands in an audit trail.

The rollout plan is just as cautious: start with notification only for a few high-value alert categories, then add investigation and recommendations, then a small set of low-risk approved actions, and only then expand. For metrics he adds a third category teams usually forget, governance and adoption, and he treats a rising override rate as the earliest sign that the grounding is going stale.

## Who should watch

SAP Basis and integration teams, SREs running ServiceNow-heavy operations, and anyone designing agents for regulated enterprises will get a reusable pattern here. It is an architecture talk, not a code walkthrough, and it shows how SAP's own tooling fits together rather than introducing a new product.

## Related talks

- [AI-Driven Master Data Governance for Agile Incident Management in SAP](https://www.conf42.com/Incident_Management_2025_Gobinath_Kasimayan_sap_governance_agility) by Gobinath Kasimayan
- [AI Agents for Incident Response: The Good, the Bad, and the Ugly](https://www.conf42.com/DevOps_2026_Vladyslav_Budichenko_incidents_agents_security) by Vladyslav Budichenko
- [Gate the Action, Not the Alert: Checking an Agent Before It Runs](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) by Artemis Leonardou

[Watch Pon Murugesh Devendren's talk](https://www.conf42.com/AI_Agents_2026_Pon_Murugesh_Devendren_sap_incidents_events)

[Watch the talk on YouTube](https://youtu.be/bpD3D8ZEqUU).

## Watch the talk

[Building Event-Driven AI Agents for Proactive SAP Incident Management](https://www.conf42.com/AI_Agents_2026_Pon_Murugesh_Devendren_sap_incidents_events) at Conf42 AI Agents 2026.
