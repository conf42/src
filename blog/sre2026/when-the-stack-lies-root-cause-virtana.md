# When every dashboard shows a symptom, map the dependencies

Conf42 Blog, 2026-03-19, updated 2026-11-17. https://www.conf42.com/blog/sre2026/when-the-stack-lies-root-cause-virtana

In short: David McNerney and Daniel Raskin (Virtana) at Conf42 SRE 2026 on finding root cause with a system dependency graph, agents and an MCP server.

A web server alert fires: response time is at three seconds against a normal value of 0.09. About two minutes later the cause is on screen, and it is the database service, two hops away, with disk errors and a certificate expiration warning. That demo is the centre of the Conf42 SRE 2026 session by David McNerney, Director of Product Management at Virtana, and Daniel Raskin, Virtana's Chief Marketing Officer. Their argument is that modern applications fail as systems, so root cause analysis needs a continuously built map of how the layers depend on each other. This is a vendor talk and the product on screen is Virtana's observability platform.

## The application stopped being one thing

Daniel takes the first half and sets up the problem. The classic three-tier application has been decomposed. It runs partly in the cloud and partly on-prem, is broken into microservices, leans on shared services such as identity and access management, and increasingly includes machine learning models and AI workloads.

His examples are airline reservation systems and ATM networks. One may fail because of an upstream service, the other because of database latency. Nothing may be technically down, and the whole system can still stop working because of the relationships between the parts.

He adds a finding from a study Virtana commissioned across Global 2000 businesses: executives believe their organisations are ready for AI, while practitioners look at the same estate and see visibility gaps and fragmented tooling. No figures from the study are given in the talk, but the gap is the point. SREs are the ones who answer for MTTR when the plan meets production.

## Silos show symptoms

Observability grew up in silos: application monitoring, infrastructure monitoring, and now AI factory monitoring, each looking at a slice of the stack. "Every single dashboard across these different silos is gonna show a symptom, but none of it is gonna show the cause," Daniel Raskin said at Conf42 SRE 2026. The APM tool reports that the application is struggling. It cannot see that the reason is an LLM inference delay, because that workload lives in a silo it has no view into.

His alternative is what he calls system-aware observability: one view from the application down through the service layer (API gateways, identity, shared dependencies), the AI factory (GPUs, tokens), and network, storage and infrastructure. Resource contention, infrastructure bottlenecks and noisy neighbours live outside the code, so code-level observability will not find them.

## The dependency graph is the data model

Collecting metrics, events, logs and traces into a data lake is not enough, Daniel argues. The piece that matters is a system dependency graph that continuously analyses that telemetry to discover relationships across the stack, so that when something breaks you can see what it is connected to.

The same graph decides how useful AI will be. Put an agent on top of application monitoring alone and it inherits the same blind spots a human has in that silo, only faster. Put it on top of data with relationships and time series already worked out and it can traverse the graph for automated root cause analysis. Add an MCP server and that data becomes available to general-purpose assistants, so querying it in natural language no longer depends on the one colleague who knows the script.

## From alert to root cause in about two minutes

David's half is the live part. He starts in a global trace topology view of a hybrid estate: workloads in Google Cloud on GKE Autopilot, traditional VMs in Azure and storage that stays in the data center. A checkout application's requests can be followed across all of it, with a vertical topology showing which namespace, node and cluster each hop runs on.

Then he describes the situation the product is aimed at. Logs live in one tool, the data center has its own monitoring, the cloud has another, and the team sets up "a war room with five different teams where we spend two to three hours arguing about who's responsible".

In the demo an alert reports a response time breach on the web server. An agent writes a plain-English summary of what happened, with the threshold and the current value. The baseline is learned automatically, and thresholds can be set by hand. The alert pulls in the Kubernetes metrics underneath the service, such as node disk utilisation, I/O bandwidth, deployment status and replicas, and a related topology shows slowdowns and errors between the cart cache and the cart service, and more errors between the cart service and the DB service.

The troubleshooting tab separates symptoms from the detected cause. The DB service is flagged as the cause: disk errors, a certificate expiration warning, slow queries and timeouts. The cart service and cart cache show elevated error rates as downstream effects. A fishbone diagram lays out the checks per service, which David describes as an SRE in a box, and the correlated logs sit next to the traces, including the DB service timeout. He contrasts this with jumping between three, four or five screens of point tools.

## Fixing it with a human in the loop

For remediation, David is candid that customers differ on how much they want automated. Deleting an unattached EBS volume to save cloud cost can run by itself. Touching production usually means a human approves, through whatever process the team already has: an Ansible playbook, or a Jira ticket that three people must sign.

He shows a copilot turning a plain-English instruction into a YAML alert response policy: when the DB service has a certificate warning, create a high-priority Jira ticket to update the certificate. In the demo the ticket is assigned to Daniel, his co-presenter.

The last few minutes cover the MCP server Virtana has started to roll out. David opens Goose, an open source agent orchestrator, running with a Gemini API key, and asks about the same alert. The agent fetches it through MCP and returns the same summary, then answers a follow-up about other alerts that fired at the same time. The same setup can hook into other MCP servers such as Jira and ServiceNow.

## Who should watch

SREs and platform teams running hybrid estates across cloud and data center who lose incident time to cross-team correlation, and anyone evaluating where agents fit in incident response. The first half is a framing talk from a CMO and the second is a product demo, so expect Virtana's screens throughout. The idea that travels without the product is to build the dependency model first and point the agents at it second.

## Related Conf42 talks

- [Correlation Over Collection: A Layered Observability Framework for SREs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Khushboo_Nigam_correlation_over_collection) by Khushboo Nigam at Conf42 SRE 2026.
- [AI-Assisted Incident Response Using LLMs and MCP in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Makarand_Gujarathi_assisted_incident_response) by Makarand Gujarathi at Conf42 SRE 2026.
- [From Alerts to Answers: Modern SRE with Observability, AI, and Agentic Ops](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Savi_Grover_alerts_answers_modern) by Savi Grover at Conf42 SRE 2026.

[Watch David McNerney and Daniel Raskin's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_David_McNerney_Daniel_Raskin_root_cause_distributed_systems) from [Conf42 SRE 2026](https://www.conf42.com/sre2026).

## From Virtana

- [Virtana](https://www.virtana.com/): full-stack observability from application to infrastructure, the platform shown in this talk.

[Watch the talk on YouTube](https://youtu.be/z9mjbWbV8eo).

## Watch the talk

[When the Stack Lies: Finding Root Cause in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_David_McNerney_Daniel_Raskin_root_cause_distributed_systems) at Conf42 Site Reliability Engineering (SRE) 2026.
