# Multi-cloud Terraform security is four stages, not one gate

Conf42 Blog, 2026-09-12, updated 2026-11-09. https://www.conf42.com/devsecops2026/secure-terraform-across-four-stages

In short: Perumalsamy Ravindran at Conf42 DevSecOps 2026 splits Terraform security into author, plan, apply and operate, with federated identity and plan-time policy.

Terraform won't let you write one network block and deploy it to three clouds, and pretending otherwise is how platform teams end up with a lowest-common-denominator module nobody wants. At Conf42 DevSecOps 2026, Perumalsamy Ravindran, a Staff Software Engineer who has run Terraform as the backbone of multi-cloud enterprise platforms, argued that Terraform's real multi-cloud value is one workflow, and that security belongs in four stages of it: author, plan, apply and operate.

It's a dense twenty minutes with a source behind every statistic, and the practical bits outnumber the slides.

## The breaches are boring

Perumalsamy's starting point is that cloud intrusions rarely need anything exotic: an exposed secret, a misconfiguration, an unpatched vulnerability. His examples are familiar. Capital One's over-permissive IAM role behind a misconfigured proxy. A Microsoft AI research storage token with an expiry date in 2051. Location data for 800,000 Volkswagen electric cars in misconfigured storage. Every one, he notes, was a setting that could have been declared, reviewed and enforced in code. Meanwhile, IaC adoption is high but coverage is thin, with Firefly reporting only six percent of organisations fully codified.

## Modules are the security control plane

The architecture has three layers: foundations (accounts, identity federation, network backbone, central logging), a private module registry, and per-application, per-environment workload stacks. The registry holds per-cloud modules that share a contract: the same input names, tag schema and security defaults. Product teams ship on that paved road, and security reviews the road rather than every car.

His six module rules: secure by default (encryption on, public access off, opting out needs an explicit variable that policy can see), small validated interfaces, semantic versioning pinned by consumers, unit tests with mocked providers on every pull request, publishing through the private registry, and flat composition with no provider blocks inside reusable modules.

## State is a secrets database

Because Terraform state is plaintext, Perumalsamy treats it as a secrets store: one state per environment per domain, its own backend and identity to bound blast radius, encryption with your own key, native locking, versioning so corruption is a rollback rather than an incident, and access limited to the pipeline's plan and apply roles plus a break-glass role that pages someone. Log every read, because a state download is a data exfiltration event. CLI workspaces share one backend and credentials, so they are not an isolation boundary.

For secrets themselves, ephemeral resources and write-only arguments keep values out of plan and state entirely. Before those existed, every database password sat in the state bucket in plain text.

## Plan with one identity, apply with another

The pipeline is the same shape on any CI: format, validate, lint and static scanning first; then a plan with a read-only identity, exported as JSON; then policy (OPA, Sentinel or native Terraform policy) evaluated against what will actually change; a cost delta; human approval for production; and finally apply with a separate write-capable identity on the exact saved plan, so what was reviewed is what shipped.

Identity is the first thing he fixes: OIDC federation from CI to cloud, with the trust policy bound to repository and branch so a fork can't assume the production role. Setting the session name to the pipeline run ID makes every cloud audit entry trace back to a commit and an approval.

On policy, his advice is to start with the ten rules you'd be embarrassed to violate (public storage, unencrypted data, wildcard IAM, open management ports, missing ownership tags) and run them in advisory mode for two sprints before making them mandatory.

## The pipeline is now the target

The section that dates fastest, and matters most: attackers now go after the delivery path itself. His examples include a compromised GitHub Action rewritten to dump CI secrets into build logs, malicious releases of a security scanner, and tampered modules and providers on public registries. A provider runs at `init` with your credentials before any plan. The defences are boring and effective: commit the lock file with hashes, pin providers and CI actions to commit hashes, serve from a private mirror with an allowlist, accept only signed providers, and use ephemeral runners.

## Drift needs an owner

The best story is about drift. An engineer opened a security group rule by hand on a Friday; the scheduled drift plan flagged it on Sunday into a shared channel nobody owned; two weeks later the next apply quietly reverted it and broke a vendor integration mid-release. The fix: every drift alert becomes a ticket with a named owner and a one-day SLA, every drift is either codified or reverted, and plan-time policy rejects manual exceptions not in code. Drift is a decision, not a notification.

## Who should watch

Platform and cloud security engineers running Terraform or OpenTofu across more than one provider, especially if your CI still holds static cloud keys. The closing 90-day plan (remote encrypted state and federation first, then modules and split roles, then drift and audit) is a ready-made roadmap.

## Related Conf42 talks

- [How to hack a cloud production environment with external Terraform manipulation](https://www.conf42.com/DevOps_2025_Uri_Aronovici_cloud_terraform_hack) by Uri Aronovici of ZEST Security at Conf42 DevOps 2025.
- [Terraform and Ansible Are Not an Architecture](https://www.conf42.com/Platform_Engineering_2026_Jeleel_Muibi_terraform_ansible_architecture) by Jeleel Muibi of HybridOps at Conf42 Platform Engineering 2026.
- [Your Agent Can Write Terraform. It Can't Feel What It Breaks.](https://www.conf42.com/Prompt_Engineering_2026_Kevin_Brown_agent_terraform_break) by Kevin Brown of Cloud World Model at Conf42 Prompt Engineering 2026.

[Watch Perumalsamy Ravindran's talk](https://www.conf42.com/DevSecOps_2026_Perumalsamy_Ravindran_terraform_multicloud_iac) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/IS2iYa-rsKM).

## Watch the talk

[Terraform for Secure Multi-Cloud DevSecOps: Automating Scalable Infrastructure as Code](https://www.conf42.com/DevSecOps_2026_Perumalsamy_Ravindran_terraform_multicloud_iac) at Conf42 DevSecOps 2026.
