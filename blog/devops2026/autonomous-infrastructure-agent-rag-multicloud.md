# Beyond LLM template generators to a RAG-aware infrastructure agent

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/autonomous-infrastructure-agent-rag-multicloud

In short: Equinix's Praneeth Patil at Conf42 DevOps 2026 on an autonomous multi-cloud infrastructure agent built on RAG, staged verification and tight IAM.

Asking an LLM to write Terraform gets you a template. It does not get you the right values, an awareness of what is already deployed, or any idea whether the change will break the network three clouds away. At Conf42 DevOps 2026, Praneeth Patil, a senior staff engineer at Equinix, argued for the next step: an autonomous infrastructure agent that knows your multi-cloud estate through retrieval, checks its own work in stages, and runs under least-privilege identities.

It is a short, opinionated talk. Expect a vision and a build order, not a product demo.

## Multi-cloud is a stitching problem

Patil's starting picture is familiar to anyone at a company of any size: training in Nvidia's cloud, data pipelines in AWS, inference in GCP, sensitive data on-prem, and a constant need to connect them. Every provider names the same thing differently (direct connect, express connect, cloud routers), and the tooling has multiplied: Terraform and Terraform Cloud, Pulumi, Kubernetes operators, Crossplane for reconciliation, CloudFormation.

What all that produces, in his words, is fear of change. State files that disagree with what someone clicked in the console. Opaque state. Cognitive overload from a pile of DSLs and APIs. And tribal knowledge: the one engineer you hope never leaves.

## LLMs as glorified template generators

His critique of today's "AI for IaC" is blunt. LLMs speed you up, but the output is only as good as your prompt, they have no context about your real infrastructure, you still verify correctness, security policy and syntax by hand, and there is no operational intelligence at all. The agent he describes turns a passive code generator into a system that keeps an up-to-date picture of your infrastructure, reasons about changes, acts, and self-corrects.

## RAG in three parts, then a verification pipeline

The architecture centres on a purpose-built retrieval layer, split three ways:

- **Specialised retrieval:** a domain-specific vector store of infrastructure metadata, configuration templates, provider schemas, relationship indices and historical change logs, so the agent can see why a past decision was made.
- **Real-time sync:** cloud feeds, activity logs and drift detection streaming into the agent, so it reasons on today's state rather than last year's provider docs.
- **Guardrail workflows:** mandatory checkpoints, with human-in-the-loop escalation.

Every proposed change then runs through a multi-stage verification pipeline: syntax, semantics (relationships and organisational constraints), security (no stray open ports, no overwritten security groups) and compliance checks from InfoSec.

## The risks get their own slide

Patil does not pretend this is safe by default. He names context-window limits (mitigated by specialised retrieval and summarisation), identity boundary failures (least privilege, service accounts), hallucination (multi-stage verification and dry runs) and the scariest one, a compromised agent manipulating production (immutable audit trails and anomaly detection on agent behaviour). Agents should get time-bound permissions, MFA through their service accounts, segregated execution environments and continuous permission monitoring in case they try to grant themselves more.

## Who should watch

Platform and cloud networking teams drowning in multi-cloud glue, and anyone pitching an agent that runs Terraform to a security team. His build order is sensible: RAG foundation first, then the verification pipeline, then agents on low-risk, high-repetition tasks, scaled up only with governance. If you want benchmarks or a working repo, this talk will not give you one.

## Related Conf42 talks

- [Kevin Brown on why your agent can write Terraform but can't feel what it breaks](https://www.conf42.com/Prompt_Engineering_2026_Kevin_Brown_agent_terraform_break) at Conf42 Prompt Engineering 2026, the sceptic's companion piece.
- [Perumalsamy Ravindran on Terraform for secure multi-cloud DevSecOps](https://www.conf42.com/DevSecOps_2026_Perumalsamy_Ravindran_terraform_multicloud_iac) at Conf42 DevSecOps 2026.
- [Harel Safra's practical guide to creating Terraform providers](https://www.conf42.com/Platform_Engineering_2024_Harel_Safra_terraform_providers_guide) at Conf42 Platform Engineering 2024.

[Watch Praneeth Patil's talk](https://www.conf42.com/DevOps_2026_Praneeth_Patil_autonomous_infrastructure_cloud)

[Watch the talk on YouTube](https://youtu.be/b1x15aQI1U8).

## Watch the talk

[From Reactive IaC to Autonomous Cloud Engineering: LLM-Driven Multi-Cloud Infrastructure for 2026 and Beyond](https://www.conf42.com/DevOps_2026_Praneeth_Patil_autonomous_infrastructure_cloud) at Conf42 DevOps 2026.
