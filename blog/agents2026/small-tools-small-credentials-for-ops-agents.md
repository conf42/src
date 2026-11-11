# Small tools, small credentials. Don't give the ops agent a shell

Conf42 Blog, 2026-09-19, updated 2026-11-09. https://www.conf42.com/blog/agents2026/small-tools-small-credentials-for-ops-agents

In short: Ahmed Tariq (Simplify9) at Conf42 AI Agents 2026: typed tools, split observer and executor identities, and approvals tied to credentials.

The first prototype of a cloud operations agent usually has one tool called something like RunShell and a credential strong enough to make the demo work. At Conf42 AI Agents 2026, Ahmed Tariq, Cloud DevOps Engineer at Simplify9, took that design apart and replaced it with patterns DevOps teams already use for CI/CD pipelines: typed tools, two identities, short-lived credentials, plan-first changes and policy outside the model.

## The model can't be its own guard

Once an agent can restart a service, trigger a pipeline or change infrastructure, it is operating production, so Tariq treats it like any other privileged production identity. His central point is that a safety rule living only in a prompt is guidance, not enforcement. The model picks its next action from whatever context it was given, and that context can push it off course. Real controls have to live outside it: IAM, tool validation, policy checks and approval gates. The model can request an action; the infrastructure decides whether it's allowed.

He frames the agent's blast radius as two things. Its tools define what it can ask for; its credentials define what the cloud will permit. Shrink either and you shrink the radius. Shrink both and you have a much safer architecture.

## Typed tools with contracts the model can't edit

Instead of a shell, expose narrow tools: get pod logs, describe alerts, get recent changes, and one carefully controlled mutation such as restart deployment. Now the capability list is inspectable, versioned and reviewed in pull requests, and you know which tools are read-only and which mutate state.

A typed tool is more than a wrapper around bash. The restart tool's contract says the namespace must match a valid pattern, the target must be on an allowlist, the effect is declared as a mutation, a plan approval is required, and it carries idempotency, a timeout and an audit record. The model supplies the arguments but can't change the contract. In front of every mutation sits a deny-by-default policy check (OPA, Cedar, a cloud-native policy service or your own small layer) asking whether this is an approved tool, an in-scope environment, a valid approval and the right execution window.

## Observer, executor, and an approval that changes permissions

The identity pattern splits the agent in two. The observer reads logs, metrics, traces, alerts and infrastructure state and can change nothing. The executor holds only the few actions needed and becomes available only after a human approves. Credentials come from workload identity federation (AWS STS, Azure federated credentials, GCP workload identity federation): no static key inside the agent, nothing long-lived waiting to leak. If your agent's role name contains "administrator", he notes, the boundary is probably too wide.

The distinction he draws on approvals is the sharpest idea in the talk. A weak design tells the model to ask a human before doing anything dangerous, which leaves the model deciding what counts as dangerous. A stronger design ties approval to the credential itself: approving one specific plan releases the executor identity or a role assumption, expires quickly and records who approved it. Like a Terraform plan, the agent's output should be a recommendation of changes, never a report that it already made them.

## What permissions can't see

Correct access control still allows wrong targets, duplicate runs, unsafe retries, timeouts after the cloud already accepted a request, and half-finished multi-step changes. His answer is ordinary distributed-systems engineering: validate inputs at the boundary, use idempotency, retry only tools designed to be repeated, set clear timeouts and checkpoint multi-step work. Every tool call, denials included, becomes an audit record with the agent identity, approver, run ID, policy decision and a link back to the plan.

Finally, prompt injection through operational data. Logs, tickets, alerts and commit messages can carry attacker-controlled text, like a log line telling the AI to delete old backups. Treat all of it as untrusted data, return structured values from tools where possible, and assume the model will eventually be fooled. Then the architecture does the work: a missing tool is denied, an out-of-scope target is denied, and a valid-looking plan still stops at a human.

The short demo shows the flow end to end: the observer investigates, the plan waits for approval, a "no" stops it cold, and a "yes" grants a temporary permission and writes the audit entry.

## Who should watch

Platform and DevOps engineers wiring agents into AWS, Azure or GCP. His rollout order is practical: inventory every tool and credential, replace shell access with typed tools, split identities, move to federation, gate mutations on plans, audit everything. You don't have to do it all on day one.

## Related talks

- [Hardening AI Coding Agents with Hooks: Enforcing Least Privilege on Autonomous Developers](https://www.conf42.com/DevSecOps_2026_Karan_Bansal_agents_leastprivilege_hooks) by Karan Bansal
- [Secretless Multi-Cloud Authentication with Workload Identity for DevSecOps Pipelines](https://www.conf42.com/DevSecOps_2026_Venkata_Velavarthipati_workloadidentity_oidc_secretless) by Venkata Velavarthipati
- [Your AI Has Too Much Access: Deterministic Authorization for Coding Agents](https://www.conf42.com/Large_Language_Models_LLMs_2026_Sohan_Maheshwar_deterministic_authorization_agents) by Sohan Maheshwar

[Watch Ahmed Tariq's talk](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud)

[Watch the talk on YouTube](https://youtu.be/bR5xFdRm-HQ).

## Watch the talk

[Don't Give the Agent a Shell: Tool and Identity Boundaries for AI Agents in Cloud Operations](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) at Conf42 AI Agents 2026.
