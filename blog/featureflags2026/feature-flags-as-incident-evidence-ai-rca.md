# A flag flip near an incident is a hypothesis, not a verdict

Conf42 Blog, 2026-10-09, updated 2026-11-17. https://www.conf42.com/blog/featureflags2026/feature-flags-as-incident-evidence-ai-rca

In short: Ishan Shah (PayPal) at Conf42 Feature Flags 2026 on treating flag changes as typed incident evidence while policy and the operator keep the authority.

A feature flag changes, checkout latency climbs, and the AI agent recommends a rollback. Do you approve it? Ishan Shah, staff software engineer at PayPal, answers not yet at Conf42 Feature Flags 2026. Timing narrows the search and does not prove the cause. His talk shows how a flag change should enter an AI-assisted incident workflow as one piece of typed evidence, with policy and a human operator holding the authority to act.

The vehicle is Beacon, a prototype he built (and, by his own account, largely vibe coded) for evidence-first incident reasoning. Flags are one slice of it.

## Four explanations, four different kinds of proof

His scenario: checkout latency rises after several nearby changes. A deployment landed. A tax V2 lookup flag reached full rollout. Database pressure shifted. A downstream dependency got noisy. The nearest reversible change is tempting.

Each hypothesis needs its own evidence path. A deployment regression needs repository history, Kubernetes rollout state and pod behaviour. A flag hypothesis needs the provider's audit event, the targeting rule and the evaluated cohort. Database saturation needs connection pool and resource metrics. The tax service needs dependency latency, errors and retries. An agent may rank them, but ranking does not replace the evidence that rules each one in or out.

In his timeline slide, a config change and a scaling event both sit between the flag transition and the first symptom. The flag is not even the nearest change.

## What a flag record cannot tell you

On or off is too weak for root cause analysis. He wants the transition timestamp, environment, actor, targeting rule, cohort, reason and source event preserved, with the observed outcome kept as separate telemetry so the flag record does not carry a conclusion inside it.

Even then there are hard limits. The audit timestamp is not the moment every SDK picked up the change: polling, streaming, caches and client state all add lag. A 10% rollout does not identify the cohort unless targeting and evaluation context are kept. Other flags may have changed in the same window. And a flag can change without the affected code path ever being evaluated.

Rollout stage changes the comparison too. At 10% you can compare flagged against unflagged traffic in the same window. At 100% the control group no longer exists, so you are left with pre versus post and explicit caveats, or a policy-approved partial rollback to recreate a control.

He is candid about the gap between slides and code: the richer audit history fields are the production design target, not something the current adapter does.

## The agent should say what it is missing

Beacon turns metrics, logs, Kubernetes and deployment state, repository history and flags into typed evidence objects. The reasoner produces ranked hypotheses, contradictions, conditions that would disprove a hypothesis, and requests for missing evidence. That last output matters to him because an agent without the data it needs tends to declare a cause anyway, or invent the data.

Service context (runbooks, architecture notes, ownership) is retrieved only within the affected service boundary, shown with a staleness signal, and never outranks live telemetry.

The demo runs on seeded incidents with Datadog monitors and logs, PagerDuty alerts and Gemini as the analysis engine. In one, the hypothesis reaches 84% confidence, the operator approves, and Beacon produces a draft remediation pull request for the team to review. In another, logs are thin and confidence stops at 45%, with the missing signals listed. A third never reaches a model at all: governance rules for sandboxed services, synthetic data or low severity keep the incident gated. Every rule applied and every human decision goes into an audit trail.

The punchline of the first demo is that the system recommended a deployment rollback, not a flag change. In a feature flag talk, he lets the flag be innocent. He also states what the artifact does not show: no production effectiveness, no MTTR improvement, no benchmark.

## Mitigating is allowed. Calling it proof is not

Sometimes turning the flag off is right: customer impact is live, the change is recent, the rollback is reversible and scoped. Before changing exposure, snapshot the audit event, the targeting rule and the telemetry, and record who authorised it and why. Then treat recovery, or its absence, as new evidence.

"A rollback is also an incident action. It is not retroactive proof that the flag caused the incident," Ishan Shah said at Conf42 Feature Flags 2026.

The same chain applies under pressure, though policy can define a faster approval path for pre-authorised actions. His summary of the split is four words: "Policy decides, operator acts."

You do not need Beacon to start. He points to the OpenTelemetry feature flag evaluation vocabulary (flag key, result value, variant, reason, flag set identifier) and OpenFeature hooks before and after evaluation. His practical test: if you cannot answer who received the new path, you cannot compare during the incident. And the design still fails when the provider has no durable audit trail or several changes stay correlated. "Governance does not repair missing evidence."

## Who should watch

SREs and platform engineers wiring AI assistants into incident response, and teams that own a flag system and want its data to hold up in a postmortem. Skip it if you want measured results from a production rollout. This is a design position with a prototype, and he says so more than once.

## Related Conf42 talks

- [AI-Assisted Incident Response Using LLMs and MCP in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Makarand_Gujarathi_assisted_incident_response) by Makarand Gujarathi (Walmart) at Conf42 SRE 2026.
- [Your Agent Is Confidently Wrong: Guardrails for Agentic AI in Real Engineering Work](https://www.conf42.com/Feature_Flags_2026_Girish_Konda_agent_guardrails_ai) by Girish Konda (Microsoft) at Conf42 Feature Flags 2026.
- [AI Gardening for MLOps: Managing Context, Memory, and Entropy in Agentic Systems](https://www.conf42.com/MLOps_2026_Ishan_Shah_gardening_context_memory), Ishan Shah's other talk, at Conf42 MLOps 2026.

[Watch Ishan Shah's talk](https://www.conf42.com/Feature_Flags_2026_Ishan_Shah_flags_incident_rca) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/gkSmIznZs9o).

## Watch the talk

[Feature Flags as Incident Evidence: Safer AI-Assisted RCA Workflows](https://www.conf42.com/Feature_Flags_2026_Ishan_Shah_flags_incident_rca) at Conf42 Feature Flags 2026.
