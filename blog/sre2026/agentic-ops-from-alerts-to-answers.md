# From alerts to answers with context-driven observability and agents

Conf42 Blog, 2026-03-08, updated 2026-11-09. https://www.conf42.com/blog/sre2026/agentic-ops-from-alerts-to-answers

In short: Savi Grover (Tekskills) at Conf42 SRE 2026 gives a quick tour of turning alert noise into context, with an agent loop that rolls back a bad canary.

SRE teams don't need more alerts, they need answers, and the gap between the two is context. At Conf42 Site Reliability Engineering (SRE) 2026, Savi Grover, Site Reliability Engineer at Tekskills, gave a brisk tour of context-driven observability and ended with an agent that notices a spike in 500s, traces it to a bad canary and rolls it back before reporting to a human.

It's one of the shortest talks of the event, closer to a lightning talk than a workshop. Watch it as a checklist, not a tutorial.

## Data rich, information poor

Savi's starting point is the paradox most on-call engineers recognize. The move from monoliths to microservices multiplied telemetry volume (she puts it at a hundred times), and SREs are now drowning in high-cardinality noise. Traditional monitoring identifies the symptom and leaves the engineer to hunt for the cause by hand.

She names four reasons the old way fails:

- **Siloed data.** Metrics, logs and traces live in separate tools with no correlation.
- **The dashboard mirage.** Flipping through dozens of dashboards during an outage adds cognitive load instead of removing it.
- **Static thresholds.** She says they lead to 80% flapping, non-actionable alerts.
- **Knowledge leakage.** Resolution depends on tribal knowledge rather than encoded patterns.

## Signal to context

Her framework shifts attention from raw data to meaningful, contextual events. Golden signals (latency, errors, traffic, saturation) are still the base, but read through SLOs rather than as raw thresholds. Distributed tracing is the backbone, with trace IDs stitching the user journey together across the mesh. And AI does dimensionality reduction: a thousand connection-refused log lines become one "database connectivity" cluster event.

The supporting practices are the ones that make all of that possible:

- consistent tags and metadata on all telemetry (application, environment, service tier, owner),
- end-to-end lineage, so you can see which downstream assets an upstream issue affects,
- anomaly detection that learns normal behaviour instead of relying only on static thresholds,
- correlation that links logs, metrics and traces to code changes, infrastructure and business impact,
- automated root cause analysis that goes past detection to triage and suggested fixes.

## The agent loop

The agentic ops part is a four-step loop. **Observe:** watch golden signals through tools like Prometheus and Grafana and notice an anomaly, say a spike in 500 errors. **Analyze:** query traces and find that a downstream API is timing out or down. **Act:** check recent CI/CD logs, identify a bad canary deployment and trigger a rollback. **Report:** tell the team in Slack or email what caused it, what was done and the details of the anomaly.

It's a clean picture of where agents fit in incident response. What the talk doesn't cover is the hard part: guardrails, how much autonomy the agent gets before a human approves, and what happens when it rolls back the wrong thing. Pair it with a longer talk if you're about to build one.

## Who should watch

Engineers new to observability who want the vocabulary in one sitting, or a team lead looking for a short talk to kick off an alert-fatigue discussion. Experienced SREs will know most of it already.

## Related Conf42 talks

- [Tackling Alert Fatigue with SLOs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue) by Mandi Walls (PagerDuty), the SLO half of the argument in depth.
- [From Signal to Insight: Building Queryable Observability with the Model Context Protocol](https://www.conf42.com/DevOps_2026_Pronnoy_Goswami_observability_queries_context) by Pronnoy Goswami (Workday), on giving agents access to telemetry.
- [Securing the Future: How AIOps Drives Operational Resilience on AWS](https://www.conf42.com/DevSecOps_2024_Indika_Wimalasuriya_aiops_resilience_aws) by Indika Wimalasuriya (Virtusa).

[Watch Savi Grover's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Savi_Grover_alerts_answers_modern)

[Watch the talk on YouTube](https://youtu.be/tTUOTjWv3tk).

## Watch the talk

[From Alerts to Answers: Modern SRE with Observability, AI, and Agentic Ops](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Savi_Grover_alerts_answers_modern) at Conf42 Site Reliability Engineering (SRE) 2026.
