# LLM agents in incident response should shorten understanding, not act

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/llm-agents-incident-response-production-safe

In short: Payjoy staff engineer Sumit Kaul at Conf42 Machine Learning 2026 on a production-safe LLM architecture for incident response, with humans deciding.

Incidents rarely go badly because the data is missing. They go badly because no human can read all of it under pressure. At [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026), Sumit Kaul, staff software engineer at Payjoy, laid out an architecture where LLM agents correlate signals, summarise and propose hypotheses during an incident, while nothing executes in production without a human. His target metric is not MTTR but MTTU, mean time to understanding.

For scale, he gave his own numbers: around 4 million messages a day on a single endpoint, and more than 200 endpoints like it. That's the alert fatigue that pushes teams from proactive to reactive operations.

## Accuracy is not the blocker; trust is

Kaul's point on why LLMs aren't already everywhere in SRE: the risks are operational. Confident but wrong suggestions. Privileged tools that can mutate production. And trust erosion, because once engineers stop trusting the system, adoption dies. The blocker is safety and trust, not whether the model can spot 99% of patterns.

## Analyse and propose; humans decide and act

The pipeline is data ingestion, context building, LLM analysis, human review and decision logging, with a strict separation of concerns. In his words, "AI suggestions are inputs, not commands." That maps onto SRE habits teams already have: change control, auditability and postmortems.

The context matters more than the model. Traces for request flow and latency, metrics for health, logs for detail, recent deployments, and SLOs and error budgets to frame impact. A better context beats a bigger model, in his telling, and a narrower one beats a firehose. The outputs are three: situational summaries so responders across application, infrastructure and data teams share one picture; ranked, explainable root-cause hypotheses, explicitly guesses and not facts; and runbook-style mitigations that a human reviews and that are never auto-executed.

## Guardrails are architecture, not prompt tricks

Three layers keep it production-safe:

- **Data hygiene:** automated PII redaction (emails, phone numbers, auth keys, customer IDs) before anything reaches the model, and a bounded context window: the last couple of hours, key metrics, recent deploys.
- **Privilege boundaries:** read-only by default, an allowlist of tools with explicit scope, and an audit trail on every call. If an action isn't auditable, it doesn't belong in production.
- **Verification gates:** shadow execution of recommendations in isolation, counterfactual validation ("would this have helped last time?"), and an immutable decision ledger of AI suggestions and human responses that feeds back into improvement.

## From reactive to proactive

The lowest-risk, highest-return uses he suggests: the LLM as first-line responder that filters low-threshold noise and escalates only real issues; cross-service correlation that spots systemic problems across dependencies early; and evidence assembly that pre-builds incident context before anyone formally declares an incident. Knowing about an incident before it is declared is the safest win available.

His pilot blueprint is pure SRE: start on non-critical services, measure trust and not just accuracy, tune guardrails from real behaviour, and expand as confidence grows. Production AI maturity grows the way reliability does, incrementally.

## Who should watch

SREs and platform teams being asked to "add AI" to on-call, and anyone evaluating vendor incident copilots who wants a checklist of what safe looks like. Pair it with Kaul's DevOps 2026 talk on observability contracts below.

## Related Conf42 talks

- [Observability as a platform contract: zero-code instrumentation and SLOs in CI/CD](https://www.conf42.com/DevOps_2026_Sumit_Kaul_slos_instrumentation_observability), Sumit Kaul (Payjoy), Conf42 DevOps 2026
- [AI-assisted incident response using LLMs and MCP in distributed systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Makarand_Gujarathi_assisted_incident_response), Makarand Gujarathi (Walmart), Conf42 SRE 2026
- [LLM copilots for SRE: incident response and auto-remediation](https://www.conf42.com/Large_Language_Models_LLMs_2026_Susanta_Kumar_Sahoo_copilots_sre_remediation), Susanta Kumar Sahoo, Conf42 LLMs 2026

[Watch Sumit Kaul's talk](https://www.conf42.com/Machine_Learning_2026_Sumit_Kaul_architecture_design_patterns)

[Watch the talk on YouTube](https://youtu.be/0GkcO1pauJc).

## Watch the talk

[LLM Agents for Site Reliability: Production-Safe Architectures for AI-Powered Incident Response](https://www.conf42.com/Machine_Learning_2026_Sumit_Kaul_architecture_design_patterns) at Conf42 Machine Learning 2026.
