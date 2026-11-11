# Six readiness checklists don't add up to one go-live decision

Conf42 Blog, 2026-09-15, updated 2026-11-09. https://www.conf42.com/blog/agents2026/agent-readiness-needs-one-scorecard

In short: Shubham Sharma (Microsoft) at Conf42 AI Agents 2026 presents MCRF, one readiness framework with evidence gates for mission-critical AI agents.

When the security team, the platform team and the AI team each sign off on an agent separately, the go-live decision ends up reflecting a negotiation rather than evidence. At Conf42 AI Agents 2026, Shubham Sharma, Senior Technical Program Manager at Microsoft, presented the Mission-Critical Readiness Framework (MCRF): one governance model that scores an agent platform across six domains and blocks deployment until the evidence is in.

## The problem is the seams

An enterprise agent is not one system. Sharma walks the stack: foundation models as the reasoning core, retrieval systems (vector stores, knowledge bases, RAG pipelines) for grounding, orchestration frameworks that run agent loops and route tools, security and compliance services, human-in-the-loop checkpoints with escalation paths and approval gates, and the cloud infrastructure under all of it. Each layer usually has an owner and a checklist. His point is that when those checklists are evaluated independently, governance fragments, deployment decisions become inconsistent, and the risk compounds in exactly the settings where a failure carries real downstream consequences.

Anyone who has watched a launch stall because three teams each assumed another had tested the retry path will recognise the shape.

## Six domains, measured before production

MCRF groups readiness into six domains: technical, operational, infrastructure, security, organisational and AI-specific. Before any production deployment it sets measurable gates on:

- **Agent reliability**: task completion rates and failure recovery, including adversarial and edge-case conditions.
- **Model governance**: evaluation, alignment testing, drift detection and version control for foundation models.
- **Tool connectivity**: validated integration contracts, API stability and latency SLAs for external tools.
- **Workflow resilience**: graceful degradation, retry logic and failure isolation across orchestration layers.
- **Observability**: end-to-end tracing, structured logging, alerting coverage and explainability for decision traces.
- **Compliance and operational preparedness**: regulatory alignment, audit readiness and verified on-call staffing.

The last item deserves attention: whether anyone is actually on call for the agent is a readiness question that rarely appears on an AI checklist.

## A lifecycle, not a gate

Sharma is explicit that MCRF is not a single sign-off. It runs as a loop: scope and classify (what the agent is, its risk tier, its stakeholders), assess the six domains, collect evidence (tests, artefacts, audit trails), then decide, either governance sign-off or remediation. Every phase leaves a structured record: assessment reports, evidence packages and decision records that stay with the agent.

Three mechanisms keep it honest. Readiness scorecards score each domain against predefined thresholds instead of judgement calls. Mandatory evidence gates block deployment until test results, audit logs and runbooks are submitted and reviewed. Cross-functional sign-off requires acknowledgement from engineering and operations leads, so approval no longer rests on one team that becomes the bottleneck.

## Who should watch

This is a governance and program-management talk, not an engineering walkthrough: there's no demo, no code and no case-study numbers. It suits TPMs, platform leads and architects who need a shared vocabulary for go/no-go reviews of agent platforms, or who are building the readiness template their organisation doesn't have yet. Engineers looking for implementation detail on any single domain will get more from talks focused on evals, tracing or identity, and the related picks below cover some of those.

## Related talks

- [Building AI-Native DevSecOps Platforms with Governed Platform Engineering](https://www.conf42.com/DevSecOps_2026_Sonu_Kumar_platformengineering_governance_ai) by Sonu Kumar
- [From Benchmarks to Business Impact: Evaluating Generative AI in Production](https://www.conf42.com/Observability_2026_Srikanth_Devarakonda_llms_evals_benchmarks) by Srikanth Devarakonda
- [From Acceleration to Assurance: Governing AI Code Assistants in SOX and ICFR Audit Analytics](https://www.conf42.com/Large_Language_Models_LLMs_2026_Karishma_Velisetty_governance_audit_assistants) by Karishma Velisetty

[Watch Shubham Sharma's talk](https://www.conf42.com/AI_Agents_2026_Shubham_Sharma_readiness_platform_enterprise)

[Watch the talk on YouTube](https://youtu.be/7tiVZtzSOoI).

## Watch the talk

[A Unified Readiness Framework for Mission-Critical AI Agents and Autonomous Platforms](https://www.conf42.com/AI_Agents_2026_Shubham_Sharma_readiness_platform_enterprise) at Conf42 AI Agents 2026.
