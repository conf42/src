# Give the on-call LLM read-only MCP access and a very good schema doc

Conf42 Blog, 2026-02-25, updated 2026-11-09. https://www.conf42.com/blog/sre2026/mcp-turns-incident-sql-into-a-conversation

In short: Makarand Gujarathi of Walmart at Conf42 SRE 2026 on AI-assisted incident response, where LLMs query telemetry over MCP, grounded by context engineering.

The slow part of most incidents is not the fix, it's the two to four hours of finding where the problem actually is. At Conf42 Site Reliability Engineering 2026, Makarand Gujarathi, Senior Software Engineer at Walmart, presented an incident response pattern where an LLM, connected to telemetry through the Model Context Protocol (MCP), turns a plain-language description of the incident into investigative SQL, refines it in a loop and proposes a hypothesis while the on-call engineer steers.

His claim about what makes it work is the useful part: AI assistance is only as good as the context you provide.

## The human is the only integration layer

Gujarathi's diagnosis will be familiar to anyone who has been on call for microservices. A single request can touch five to 10 services, each with its own database, cache, queue and pipeline. During an incident the engineer jumps between a data warehouse, Kibana or Splunk, Grafana or Datadog dashboards, a tracing UI, deploy logs and feature flag dashboards. None of these share a mental model; the person on the bridge is the only thing joining them.

Expertise is the other bottleneck. Senior engineers know which dashboards to trust and which service really sits behind an API. Juniors wait for them to join the call. And the problem is never a lack of telemetry, it's making sense of too much of it under time pressure. The abstract puts numbers on the manual version: 15 to 30 SQL queries for a moderate incident, with timestamp skew from hundreds of milliseconds to several seconds.

## MCP is what makes the chatbot safe to point at production

The LLM brings natural language and structured-data skills. MCP gives it a standard, controlled way to reach telemetry, which Gujarathi breaks into three jobs. Schema introspection lets the agent ask which tables, columns and metrics exist, so it works from the real schema, not a guessed one. Controlled execution exposes only safe, read-only operations, enforces query patterns and filters or masks personal data, which gives you guardrails and an audit log. And a standard protocol means the same agent can query BigQuery, Snowflake, a lakehouse, Prometheus or a log store without a custom integration per system.

His walkthrough uses a checkout service throwing HTTP 500s in one region shortly after a deployment. The agent extracts the service, region, time window and the deploy, then queries error rates by endpoint, latency before and after, and traffic by version. It narrows the spike to one region, one version and the payment endpoint, notices payment provider timeouts rising after the rollout, and suggests the payment integration change as the cause. The engineer can interrupt or redirect at any point; the AI does the query-writing grunt work.

## Context engineering is the actual project

Connect an LLM to a production database with no documentation and, he warns, expect poor results and possibly unsafe behaviour. Three ingredients fix that:

- **Schema documentation** that explains meaning, not just names: what a column represents, whether timestamps are seconds or milliseconds, how logs and metrics join for one request.
- **Curated query libraries** of pre-tested investigations (error rate by endpoint, P95 latency before and after a deploy, top services by error volume) that the agent adapts instead of reinventing.
- **Architecture diagrams** in machine-readable form, so knowing that checkout depends on payments, inventory and user profile becomes a suggested next query.

Telemetry quality still sets the ceiling: inconsistent metric names, mixed tracing libraries, one-minute versus five-minute buckets and sampled traces all hurt the AI as much as the human.

## What changes, and what stays human

He is careful about results. The exact percentage gains depend on telemetry maturity, context work and how comfortable engineers are with the assistant, so he describes the qualitative pattern instead: plausible root causes sooner, far more queries run in the first 10 to 15 minutes, and junior engineers driving investigations without waiting for an expert. Critical actions such as rollbacks, traffic shifts, declaring a major incident and external comms stay under human control. The rule of thumb is to have AI recommend and explain, not silently act, starting with read-only automations like pre-running standard diagnostics when an alert fires.

His adoption path is refreshingly unglamorous: assess telemetry maturity first (if it's poor, fix that before any AI), then build the context materials, then pilot read-only on one or two services during real incidents and iterate.

## Who should watch

SRE and observability teams thinking about an LLM in their incident tooling will get a sober, buildable pattern here, along with the reasons a weekend demo tends to disappoint. It's an architecture talk with a worked scenario, not a product pitch.

## Related Conf42 talks

- [Leveraging SRE and Observability Techniques for the Wild World of Building on LLMs](https://www.conf42.com/Incident_Management_2023_Christine_Yen_sre_observability_building_llms) by Christine Yen.
- [AI Agents for Incident Response: The Good, the Bad, and the Ugly](https://www.conf42.com/DevOps_2026_Vladyslav_Budichenko_incidents_agents_security) by Vladyslav Budichenko.
- [How to use generative AI to finally fix out-dated runbooks](https://www.conf42.com/Incident_Management_2023_Anurag_Gupta_generative_ai_fix_runbooks) by Anurag Gupta.

[Watch Makarand Gujarathi's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Makarand_Gujarathi_assisted_incident_response) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/xZ1pT6BQKu0).

## Watch the talk

[AI-Assisted Incident Response Using LLMs and MCP in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Makarand_Gujarathi_assisted_incident_response) at Conf42 Site Reliability Engineering (SRE) 2026.
