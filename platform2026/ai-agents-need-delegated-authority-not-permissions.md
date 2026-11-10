# A correct diagnosis doesn't give an AI agent the authority to act

Conf42 Blog, 2026-10-09, updated 2026-11-09. https://www.conf42.com/platform2026/ai-agents-need-delegated-authority-not-permissions

In short: Ruby Agarwal, VP of Engineering at Avaya, at Conf42 Platform Engineering 2026 on scoped, expiring authority for agents that remediate production.

An AI agent can be completely right about why production broke and still be wrong to fix it. That's the core of Ruby Agarwal's talk at Conf42 Platform Engineering 2026. Ruby, Vice President of Engineering at Avaya, argues that self-service platforms were built to validate whether an action can run safely, and agents force a new question: should this agent be allowed to decide the action is needed at all?

## 2:14am, 96% confident, still not obviously safe

She opens on an incident bridge. A deployment went out eight minutes ago, p99 latency has jumped and error rates went from 1.8% to 7.4%. A monitoring agent correlates the deploy with metrics, traces and logs and recommends an immediate rollback with 96% confidence.

Then she adds context. The release included a database schema change. The previous version retried more aggressively. The service shares a database with other customer-facing apps. The diagnosis may be correct, but the rollback is suddenly not the obvious move, and that gap is the whole talk.

Later she plays the scenario forward: the rollback works, service A recovers, dashboards go green, and the old retry policy starts hammering the shared database until services B and C degrade. The problem has changed address. Local success isn't system success.

## Decision, authority, execution

Ruby splits the platform contract into three parts. Decision: what the agent believes should happen and why. Authority: whether it has been delegated the right to make that decision under these conditions. Execution: whether the platform can safely perform the authorised action against current state. She doesn't want one agent diagnosing, granting itself authority, executing and declaring success.

Her model for authority is a short-lived lease, not a standing permission. An agent might be allowed to roll back one stateless service to a verified previous version, only with fresh evidence, a compatible state and no conflicting remediation running, and only for a limited time. As she puts it: "We're delegating a decision within boundaries. We're not handing an agent permanent control of production."

## Propose, adjudicate, commit, verify

The architecture has four steps. The agent proposes a structured intent: service, current and target versions, evidence, expected customer impact and stop conditions. An independent authority service checks the agent's scope, evidence freshness, dependency health, blast radius and parallel remediations, then allows, denies or escalates. The executor revalidates right before acting, because time-of-check versus time-of-use bites here too. Then the platform verifies the customer outcome, since a successful rollback API call isn't proof of recovery. Every step lands in a decision record that explains why, not only what.

Her worked ending is a nice touch. The same 96% recommendation is allowed when evidence is fresh and the shared dependency healthy, escalated when the database's health is unknown, and denied when the evidence is 18 minutes old. Authority is evaluated in context, not stapled to an agent's identity.

## Two reasonable agents can make an outage

One scenario every SRE will recognise: a release agent rolls back while a capacity agent scales, the scaling shifts traffic, the release agent reacts again, the capacity agent scales down. Each decision is reasonable; together they oscillate. Ruby's answer is the classic toolkit applied to agents: concurrency controls, resource ownership, fencing, cool-down periods, arbitration, and a way for the incident commander to take control.

## Earn autonomy per decision class

Rollout goes observe, recommend, act within bounds, then act and report. Being great at detecting memory pressure doesn't earn the right to run database failovers, and authority narrows again when performance drops. She's also blunt about rubber-stamp approval buttons: a human clicking yes on dozens of recommendations isn't oversight. Accountability means owning the authority you delegated.

## Who should watch

Platform engineers and SREs designing agent-driven remediation, and leaders deciding who owns those decisions. It's a framework talk without code, and the incident scenario makes every point land.

## Related Conf42 talks

- [Autonomy with Guardrails: Operating Agentic Automation in High-Risk Production Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ajay_Athitya_Ramanathan_autonomy_guardrails_operating) by Ajay Athitya Ramanathan at Conf42 SRE 2026.
- [Your Rollback Is Untested and You Will Find Out at 3am](https://www.conf42.com/MLOps_2026_Artemis_Leonardou_rollback_untested_3am) by Artemis Leonardou at Conf42 MLOps 2026.
- [LLM Copilots for SRE: Transforming Incident Response and Auto-Remediation](https://www.conf42.com/Large_Language_Models_LLMs_2026_Susanta_Kumar_Sahoo_copilots_sre_remediation) by Susanta Kumar Sahoo at Conf42 LLMs 2026.

[Watch Ruby Agarwal's talk](https://www.conf42.com/Platform_Engineering_2026_Ruby_Agarwal_autonomy_service_authority) from [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026).

[Watch the talk on YouTube](https://youtu.be/BEdHOseoPOs).

## Watch the talk

[From Self-Service to Safe Autonomy: The Authority Shift](https://www.conf42.com/Platform_Engineering_2026_Ruby_Agarwal_autonomy_service_authority) at Conf42 Platform Engineering 2026.
