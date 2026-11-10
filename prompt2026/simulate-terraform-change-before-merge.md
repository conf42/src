# Give an agent's Terraform change consequences before merge

Conf42 Blog, 2026-10-02, updated 2026-11-09. https://www.conf42.com/prompt2026/simulate-terraform-change-before-merge

In short: Kevin Brown of Cloud World Model at Conf42 Prompt Engineering 2026 shows simulated cost, CPU and latency for an infrastructure PR, gaps labelled.

An agent can write a perfectly valid Terraform change and still have no idea what it costs or how it behaves under load. At Conf42 Prompt Engineering 2026, Kevin Brown, founder and CEO of Cloud World Model, argued that the missing layer between an agent's plan and the real cloud is a model of what the change will do, and showed his company's GitHub app putting simulated results straight into a pull request.

Fair warning on scope: this is a short founder talk about his own product. The idea it carries is worth the few minutes even if you never install anything.

## Prompting decides intent, not consequences

Kevin's abstract frames it neatly: "Prompt engineering decides what an agent intends. Something else decides what happens when it acts." An agent that can write and apply an infrastructure change can't feel its cost, latency or failure behaviour until it's live. The usual guardrail, a sandbox, covers code. It says nothing about what a workload does at 300 requests per second or what a node failure does to a queue.

`terraform plan` doesn't fill that gap either. In the talk he points out that plan tells you the change is syntactically correct and what resources move, not what the change will cost, how latency shifts or how often it fails. Reviewers end up approving infrastructure PRs with less information than they'd demand for an application change.

## The demo: one machine type, one report

The worked example is deliberately boring, which is the point. Kevin took the public HashiCorp GKE tutorial for Terraform and committed one small change: the node shape moved from n1-standard-1 to e2-standard-2 on two nodes. Opening the pull request triggers a report that simulates the base and the head of the PR and shows the before and after for cost, CPU, P99 latency and error rate, modelled at 300 RPS.

The reviewer, or the agent that made the change, can then decide whether to adjust or merge. Kevin's pitch is that these are numbers you'd normally only see after the deploy.

## Read the labels

The part of the talk that earns trust is the time spent on what the model gets wrong or doesn't cover. Every number in the report carries a label: modelled, estimated, or a known gap.

He lists the gaps out loud. IAM policies aren't modelled. Network paths such as route tables and security groups aren't modelled; the report detects the change and marks it "not modeled yet". Memory scope is covered for Cloud Run and GKE only. Spot interruptions are modelled for EKS only, with a two-minute notice.

Cost is modelled from public list prices, so a reported saving doesn't include your discounts and isn't your bill. Cloud World Model also doesn't connect to your cloud account; Kevin presents that as a feature, with the trade-off that you still have to check your own environment. A simulation that tells you where it's blind is far more useful than one that's confidently precise about everything.

## Why this belongs at a prompt engineering conference

The broader argument matches a thread that ran through the event: reliable agents need checks outside the prompt. You can tell an agent in capital letters to avoid expensive changes, and it still won't know what expensive means for a node pool change. A modelled consequence, attached to the PR where both the agent and the human reviewer can see it, turns that sentence into evidence. It gives the agent consequences before it gets access.

## Who should watch

Platform and infrastructure teams letting agents (or juniors, or tired seniors) open Terraform PRs, and anyone designing review gates for infrastructure as code. It's a vendor demo, so go in expecting a product walkthrough. Kevin closed by asking teams who ship infrastructure as code weekly to send one real PR for blunt feedback, with no contract.

## Related Conf42 talks

- [How to hack a cloud production environment with external Terraform manipulation](https://www.conf42.com/DevOps_2025_Uri_Aronovici_cloud_terraform_hack) by Uri Aronovici of ZEST Security at Conf42 DevOps 2025.
- [Gate the Action, Not the Alert: Checking an Agent Before It Runs](https://www.conf42.com/DevSecOps_2026_Artemis_Leonardou_agents_guardrails_policy) by Artemis Leonardou of NOFire AI at Conf42 DevSecOps 2026.
- [From Reactive IaC to Autonomous Cloud Engineering: LLM-Driven Multi-Cloud Infrastructure for 2026 and Beyond](https://www.conf42.com/DevOps_2026_Praneeth_Patil_autonomous_infrastructure_cloud) by Praneeth Patil at Conf42 DevOps 2026.

[Watch Kevin Brown's talk](https://www.conf42.com/Prompt_Engineering_2026_Kevin_Brown_agent_terraform_break) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/QbHUdS0xTDk).

## Watch the talk

[Your Agent Can Write Terraform. It Can't Feel What It Breaks.](https://www.conf42.com/Prompt_Engineering_2026_Kevin_Brown_agent_terraform_break) at Conf42 Prompt Engineering 2026.
