# Identity is the control plane for securing AI systems

Conf42 Blog, 2026-06-15, updated 2026-11-09. https://www.conf42.com/blog/llms2026/identity-is-the-control-plane-for-ai

In short: Arunkumar Muthuramalingam of General Reinsurance at Conf42 LLMs 2026 on least privilege, continuous verification and non-human identities for AI agents.

A summarization agent does not need write access to a production database, yet plenty of them have it. Arunkumar Muthuramalingam, who runs cybersecurity and infrastructure operations at General Reinsurance, used his talk at Conf42 Large Language Models 2026 to argue one point: once LLMs, copilots and agents are in production, identity and access management stops being an admin chore and becomes the primary control plane for AI security.

It is a short, framework-style talk with a checklist at the end, which makes it easy to steal for an internal review.

## Four things broke the perimeter at once

Muthuramalingam names the shifts: every inference boundary is now a trust and authorization decision; autonomous agents act, call APIs, move data and spawn sub-agents with delegated authority; orchestration frameworks and service meshes create dense, mostly implicit machine-to-machine trust; and serverless and workload identities run with credentials almost nobody audits in real time.

What they have in common is that none of them is a human at a laptop behind a firewall. Static firewall rules, periodic audits and log-in-once sessions were built for that human. Identity is the only control that travels with the workload.

## Least privilege, three ways

He breaks least privilege into three properties that apply to human and non-human identities alike:

- **Granular**: scoped to the exact resource and data classification.
- **Context-aware**: roles granted just in time for the job instead of static assignments.
- **Time-bound**: an agent that summarizes documents at 2 p.m. does not need access around the clock. It elevates, does the work and drops the role.

## Every hop is a new trust boundary

Authenticate once at session start and let the agent hop through APIs, vector databases and compute, and you have built a lateral movement path. His alternative is a loop at every boundary: authenticate the identity, authorize the action, monitor the behaviour, then revoke or escalate. Continuous verification targets the two worst post-compromise moves, lateral movement and privilege escalation through stolen tokens or misconfigured trust, and it has to live in every layer of the stack rather than one.

## Most companies cannot count their machine identities

The part he says keeps him up at night is non-human identity. Service accounts, API keys, OAuth tokens and workload identities are the largest and fastest-growing identity population, and historically the least governed. Their failure modes are familiar: long-lived credentials never rotated, scopes granted generously at creation, no MFA, no behavioural baseline, orphaned accounts that outlive their service, and no easy way to correlate them across systems.

The governance answers map one to one: discover and inventory everything, automate rotation with short-lived tokens, baseline behaviour, and tie the credential lifecycle to the service lifecycle. When an application is decommissioned, its identities must die with it, and he points out that this step is a gap in most organizations.

For agents specifically he wants three pillars: a verifiable, non-shared identity per agent instance (shared credentials make incidents impossible to investigate), authorization scoped to the task, and an audit trail of every action.

## A kill switch needs one governance plane

Siloed identity creates blind spots exactly when you need visibility. Centralized telemetry detects anomalies, one governance plane gives you what he calls an AI kill switch to revoke credentials or stop an agent, and pre-staged playbooks reissue and re-scope access without manual coordination. His summary of the outcome is less reach, less movement and faster recovery.

The anti-patterns are worth pinning on a wall: over-privileged service accounts, credential sprawl in code and environment variables, implicit agent trust where a compromised sub-agent inherits its parent's rights, and siloed ownership where IT owns humans, DevOps owns service accounts and nobody owns agents. "So none of these are like zero days, they are governance gaps."

## Who should watch

Security architects, IAM teams and platform leads about to give agents real credentials, and anyone writing the onboarding and decommissioning process for AI agents. It is conceptual rather than tool-specific, so pair it with something hands-on.

## Related Conf42 talks

- [Secretless Multi-Cloud Authentication with Workload Identity for DevSecOps Pipelines](https://www.conf42.com/DevSecOps_2026_Venkata_Velavarthipati_workloadidentity_oidc_secretless) from Conf42 DevSecOps 2026 is the hands-on fix for long-lived credentials.
- [Engineering Secure Cloud Platforms: Data-Driven Identity Governance for Modern Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Anjan_Kaleru_governance_identity_secure) from Conf42 Platform Engineering 2025 goes deeper on identity governance.
- [Don't Give the Agent a Shell: Tool and Identity Boundaries for AI Agents in Cloud Operations](https://www.conf42.com/AI_Agents_2026_Ahmed_Tariq_identity_permissions_cloud) from Conf42 AI Agents 2026 applies the same ideas to operations agents.

[Watch Arunkumar Muthuramalingam's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Arunkumar_Muthuramalingam_identity_security_iam)

[Watch the talk on YouTube](https://youtu.be/OPPqrYdneOU).

## Watch the talk

[Identity-Centric Security for AI Systems: IAM as Cybersecurity Infrastructure](https://www.conf42.com/Large_Language_Models_LLMs_2026_Arunkumar_Muthuramalingam_identity_security_iam) at Conf42 Large Language Models (LLMs) 2026.
