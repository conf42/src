# Terraform and Ansible are tools; the operating model is the architecture

Conf42 Blog, 2026-11-03, updated 2026-11-09. https://www.conf42.com/platform2026/terraform-ansible-not-an-architecture

In short: Jeleel Muibi of HybridOps at Conf42 Platform Engineering 2026 on authority, preflight checks and run records that sit above Terraform and Ansible.

Every step in the pipeline went green, and the traffic still didn't move. That is the scene Jeleel Muibi, infrastructure and automation engineer and maintainer of the open-source HybridOps project, opens with at Conf42 Platform Engineering 2026. His claim: Terraform provisions, Ansible configures and a pipeline sequences, but none of them decides whether a change should run or what "done" means. That decision layer is the architecture.

## Three passes and a no

The opening slide is worth pausing on. Infrastructure is provisioned, configuration is applied, the health check passes, and the requested outcome still fails because something outside the pipeline wasn't ready. Each tool did its job. What was missing was a model of how the tools' outputs connect to the result anyone actually asked for.

Jeleel frames the gap with six boundaries, which he ties to the CNCF platform engineering maturity model: intent, authority, permission, readiness, completion and continuity. Tools live inside those boundaries. The operating model draws them.

## Authority comes from outside the tool

The most practical idea is "authority is a scoped fact". In his example, a blueprint deploys a platform VM that must get its IP address from an IPAM, NetBox in the demo. Before any step runs, a preflight checks that the authoritative source is reachable and can answer. If it can't, the whole run stops with a clear failure instead of half-provisioning a VM that will later fight another one for an address.

Notice that the tool underneath doesn't matter. The VM could be built by Terraform, Pulumi, Ansible or a PowerShell script. The decision about whether it may be built belongs to the layer above.

## Fail fast at the boundary that owns the decision

The demo, run in VS Code against the HybridOps repository, walks through validate, plan and preflight for an on-prem foundation on Proxmox SDN. The fun moment is a refusal. Jeleel runs preflight for a shared network foundation in a dev environment, and the policy rejects it: shared foundations belong in the shared environment, and dev should consume them, not create its own copy. Run the same Terraform module on its own and it would have happily deployed to dev, setting up a VLAN or IP conflict for later.

Because the network step was blocked, the inventory and platform steps were deferred and nothing external changed. Terraform's own plan stage catches conflicts within Terraform; this check catches conflicts between tools and environments, which is where multi-tool platforms tend to bleed.

## A refusal should tell you what to do next

The last section is about evidence. A run should leave a reviewable chain, not a folder of terraform.log, ansible.log and Packer output that someone has to correlate at 2am. A good refusal names the blueprint, the policy that blocked it, the selected environment, the deferred steps, the owner of the decision and the path to fix it.

His starting advice for teams with a pile of hand-triggered pipelines is pleasantly unglamorous: pick one risky end-to-end workflow, name its outcome, assign authority, move the checks before execution, define completion with a signal the service owns, keep the record, then repeat. Keep the tools, design the architecture around them, and swapping a tool later stops being a migration project.

## Who should watch

Platform and infrastructure engineers who own Terraform and Ansible estates across on-prem and cloud, especially anyone who has explained a green pipeline in a post-incident review. Be aware that the demo uses HybridOps, Jeleel's own MIT-licensed project, as the worked example; the pattern applies without it. The talk runs long and the delivery is conversational, so the slides on boundaries and refusals carry most of the value.

## Related Conf42 talks

- [Your Agent Can Write Terraform. It Can't Feel What It Breaks.](https://www.conf42.com/Prompt_Engineering_2026_Kevin_Brown_agent_terraform_break) by Kevin Brown at Conf42 Prompt Engineering 2026.
- [Terraform for Secure Multi-Cloud DevSecOps](https://www.conf42.com/DevSecOps_2026_Perumalsamy_Ravindran_terraform_multicloud_iac) by Perumalsamy Ravindran at Conf42 DevSecOps 2026.
- [When Infrastructure as Code Ends: The Practical Guide to Creating Terraform Providers](https://www.conf42.com/Platform_Engineering_2024_Harel_Safra_terraform_providers_guide) by Harel Safra at Conf42 Platform Engineering 2024.

[Watch Jeleel Muibi's talk](https://www.conf42.com/Platform_Engineering_2026_Jeleel_Muibi_terraform_ansible_architecture) from [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026).

[Watch the talk on YouTube](https://youtu.be/4n6_9qk0ud8).

## Watch the talk

[Terraform and Ansible Are Not an Architecture](https://www.conf42.com/Platform_Engineering_2026_Jeleel_Muibi_terraform_ansible_architecture) at Conf42 Platform Engineering 2026.
