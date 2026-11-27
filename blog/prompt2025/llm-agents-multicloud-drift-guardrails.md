# An LLM agent for multi-cloud should act like a guarded junior SRE

Conf42 Blog, 2025-11-06, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/llm-agents-multicloud-drift-guardrails

In short: Praneeth Patil of Equinix at Conf42 Prompt Engineering 2025 on moving LLMs from one-off Terraform snippets to RAG-grounded agents that fix multi-cloud drift.

Asking a chatbot for a Terraform module is fast, and sometimes fast in the wrong direction. At Conf42 Prompt Engineering 2025, Praneeth Patil, Senior Staff Engineer at Equinix, sketched how LLMs can move from reactive snippet generators to agents that watch multi-cloud state, detect drift and propose fixes, and what verification has to surround them before anyone lets them touch production.

## The VPC module that opened everything

Praneeth's cautionary tale is worth the price of admission. A chat assistant wrote a clean VPC module in minutes. It also opened up all traffic, because nobody had mentioned the bastion host restriction. Nice code, wrong outcome. His lesson: without context and checks, you speed up right and wrong changes equally.

The wider problem is familiar to anyone running AWS, Azure, GCP and colocation side by side. Each has its own IAM, network model, APIs and billing knobs. The result is config sprawl, policy divergence and drift, and the glue (Terraform, Crossplane, scripts) becomes a second platform to maintain, or worse, tribal knowledge.

## RAG is the difference between fiction and grounded action

The agent he describes behaves like a junior SRE with excellent recall of the docs, wrapped in strict guardrails. It keeps continuous awareness (snapshots of state, drift and quotas across clouds), detects misconfigurations, vulnerabilities and cost anomalies, and proposes or executes fixes with approvals and rollbacks.

Retrieval is the core. Before changing a security group, the agent pulls the desired state from infrastructure as code, the actual rules from the cloud API, the change history from logs and PRs, your own security and FinOps policies, and provider best practices such as the AWS Well-Architected material. The output is a proposed diff plus the reasoning behind it.

## Four checks before anything applies

The verification pipeline is the part to steal:

1. Syntax validation, linting and formatting for YAML, JSON and Terraform.
2. Semantic analysis: does this change do what was intended? Reasoning models help here.
3. Policy guardrails: compliance, budgets, tagging, encryption, data residency.
4. Dry runs: `terraform plan`, `kubectl diff`, smoke tests in staging.

He also recommends dual-model verification, where a second model or a rules engine critiques the plan and asks why it is needed and what could go wrong. Red teaming, built into the pipeline.

## The real value is between deployments

Praneeth argues that the agent earns its keep after the deploy, watching for IAM changes, route table edits, load balancer health, quotas and pricing. His anecdote: a teammate with account access modified a security group, and the whole team went looking for what broke. An agent holding the desired state could have spotted the change, explained it and proposed the rollback.

He is candid about risks: hallucinated configurations, over-privileged agents and runaway cost, including the cost of the agent's own inference. The mitigations are least privilege granted on demand, tests that confirm the agent behaves as expected, logging every decision and its reasoning, tiered human approvals with time-boxed change windows (not at 2 AM), and a versioned artifact behind every action so rollback is instant.

## Start small

His adoption path has four steps: keep your current flow and add retrieval and validation around LLM-generated artifacts; add RAG over your docs, IaC and runbooks; let agents detect and report drift; only then allow autonomous actions, with humans in the loop.

## Who should watch

Platform and SRE teams who already use Terraform or Crossplane across more than one provider and are being asked what agentic AI means for them. It is architecture and practice, not a product demo.

## Related Conf42 talks

- [Stephane Jourdan on why infrastructure drift deserves attention](https://www.conf42.com/Cloud_Native_2021_Stephane_Jourdan_infrastructure_drift) at Conf42 Cloud Native 2021, the problem before agents.
- [Peter O'Neill on securing terraform apply with Open Policy Agent](https://www.conf42.com/Site_Reliability_Engineering_2022_Peter_ONeill_terraform_apply_secured_open_policy_agent), one way to build the guardrail stage.
- [Perumalsamy Ravindran on Terraform for secure multi-cloud DevSecOps](https://www.conf42.com/DevSecOps_2026_Perumalsamy_Ravindran_terraform_multicloud_iac) at Conf42 DevSecOps 2026.

[Watch Praneeth Patil's talk](https://www.conf42.com/Prompt_Engineering_2025_Praneeth_Patil_agents_infrastructure_multicloud), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/Y_8vRkJsbZA).

## Watch the talk

[From Reactive Prompts to Autonomous Agents: LLMs for Multi-Cloud Infrastructure](https://www.conf42.com/Prompt_Engineering_2025_Praneeth_Patil_agents_infrastructure_multicloud) at Conf42 Prompt Engineering 2025.
