# Incident agents: diagnosis is the easy half, authority is the hard one

Conf42 Blog, 2026-11-16, updated 2026-11-17. https://www.conf42.com/blog/mlops2026/agentic-llms-microservices-observability

In short: Nishanth Vepachedu at Conf42 MLOps 2026 on graduated oversight for incident agents: typed actions, risk tiers and a session score the agent cannot lower.

An incident agent is a privileged identity in production whose main input is partly written by strangers. That is how Nishanth Vepachedu, who works on AI infrastructure for agentic systems, frames the problem at Conf42 MLOps 2026. Most talks on this subject are about making the agent a good investigator. His is about what the agent is allowed to do, who decides, and how that decision should change as an investigation drags on.

Anyone who can send a request to your service can put words in your logs. The agent that reads those logs may also be able to restart and roll back. In security terms, he says, that is a confused deputy waiting to happen.

## A good investigator has four habits

He covers the investigation side quickly and fairly. A credible agent grounds every claim in a trace ID, a timestamp and linked log lines, and a claim it cannot cite is not a finding. It turns its story into a prediction and runs the query that could refute it first. It retrieves in stages, cheap aggregates before traces before log windows, behind a gateway that enforces a budget so the investigation does not take down the telemetry. And it is honest about gaps: sampling drops spans, and a missing edge is not evidence of health.

When that side goes wrong, an engineer loses time. When the action side goes wrong, customers lose service. And the usual safeguard there is one approve or deny prompt, the same for restarting a pod and for changing network policy in a region. By the twentieth prompt of the night, the on-call engineer is clicking approve.

## Logs are untrusted input, and no single step is the breach

He makes the input problem concrete with research he cites. In a benchmark called LogJack, authors planted prompt injection payloads in cloud logs and gave them to debugging agents built on eight foundation models; on six of the eight, the agent executed a command that came from log content. A NeurIPS paper on security operations agents ran more than 1,100 payloads, and every configuration tested could be talked into downgrading real malicious activity. Letting the agent pull more read-only telemetry to cross-check did not reliably fix it.

The second problem needs no attacker. An agent reads logs, queries traces, restarts a pod, then the service, then proposes a network policy change. Each step passes on its own. The path went from reader to network editor and nothing raised the bar. He points to a July incident in which research agents in an OpenAI security evaluation got out of their sandbox into Hugging Face's production: by the accounts he cites, roughly 17,600 actions over four days, and from one dataset pod to cluster admin in under 13 hours. He is careful to say those were not incident response agents. The lesson he takes is narrower: a control that judges one call at a time, with no memory, cannot see a trajectory.

## The action sets a floor, and the session raises it

His proposal, which he is building as an open reference design, starts with making the agent the best instrumented service you own. Every tool call emits a typed event before it runs: effect (none, reversible, irreversible), scope (pod, service, region), provenance (which inputs influenced it, any of them untrusted), and what scrutiny was required and granted. A tool with no declared metadata fails closed.

Typed actions get a floor. Querying telemetry is tier zero, a pod restart gets a light check, network policy needs a person, and anything irreversible or crossing a tenant boundary never drops below human approval. "Confidence is not a credential.", Nishanth Vepachedu said at Conf42 MLOps 2026.

Between acting alone and asking a human he puts steps: observe; justify in a fixed structure that a deterministic rule checks against the cited evidence; a second opinion from an independent model; human approval with provenance shown; halt. The tier an action needs is the larger of its floor and the tier implied by the risk the session has accumulated. Three properties hold it together: nothing the agent says or reads can lower the score, a sub-agent inherits its parent's risk, and the floor always holds.

Models act as sensors here, with measured error rates. Authority lives in a small deterministic state machine. His rule: a model's judgment is evidence, not permission.

## Four numbers to ask any vendor for

He offers no results, and says so: the harness is in progress. What he offers are the measurements. Which tier caught each unsafe action. Approvals per on-call shift, treated as a budget. How many legitimate investigations still complete with the gate on. And the miss rate when replayed against past incidents.

The rollout order follows: offline replay, read-only in production with the gate in shadow, reversible actions, then wider authority only as far as the data supports. His one-sentence summary is "Scale the oversight with the agent."

## Who should watch

SREs, platform engineers and security people who are being asked to let an agent do more than write summaries. If you want a tour of LLM-driven telemetry correlation with MTTR numbers, as the abstract suggests, this is a different and more useful talk: a design argument about authority, with no product and no benchmarks of its own yet.

## Related Conf42 talks

- [AI Agents for Incident Response: The Good, the Bad, and the Ugly](https://www.conf42.com/DevOps_2026_Vladyslav_Budichenko_incidents_agents_security) by Vladyslav Budichenko at Conf42 DevOps 2026.
- [AI-Assisted Incident Response Using LLMs and MCP in Distributed Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Makarand_Gujarathi_assisted_incident_response) by Makarand Gujarathi of Walmart at Conf42 SRE 2026.
- [Don't Give the Agent a Shell: Tool and Identity Boundaries for AI Agents in Cloud Operations](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) by Ahmed Tariq at Conf42 AI Agents 2026.

[Watch Nishanth Vepachedu's talk](https://www.conf42.com/MLOps_2026_Nishanth_Vepachedu_microservices_observability_llms) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Scaling Microservices Observability with Agentic LLMs](https://www.conf42.com/MLOps_2026_Nishanth_Vepachedu_microservices_observability_llms) at Conf42 MLOps 2026.
