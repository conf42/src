# GitOps for the network turns router changes into reviewed pull requests

Conf42 Blog, 2025-12-29, updated 2026-11-09. https://www.conf42.com/blog/devops2026/network-gitops-sdwan-zero-trust-automation

In short: Imran Abdul at Conf42 DevOps 2026 on infrastructure as code for enterprise networks, with SD-WAN templates, canary rollouts and zero trust segmentation.

Push a security patch to 500 network devices the traditional way and you SSH into each one, paste the config, and do it again 499 times, starting over when you make a typo. At Conf42 DevOps 2026, Imran Abdul, a network operations manager, showed how the same Git, CI/CD and canary habits application teams take for granted apply to enterprise networks, drawing on deployments across nuclear, solar and wind sites and enterprise data centres. His reported result: changes that took three to five days now finish in about 15 minutes across 500-plus sites, with a 95% success rate.

## Configuration drift is the silent outage

The problem statement is one every network engineer knows: devices drift from their intended state, troubleshooting gets close to impossible, a one-minute change takes days of coordination and approval windows, and rollback means digging out an old backup. Meanwhile the business wants global changes in minutes, consistent security policy, and connectivity across on-prem and several clouds.

## Templates in Git, pushed through a controller

Abdul uses Cisco Viptela as the worked example: vManage as the central brain for policy and configuration, vSmart as the control plane, vEdge routers as the data plane at every site. Change a policy once in vManage and it reaches every vEdge with no SSH sessions.

The IaC layer replaces hundreds of lines of CLI per device with a YAML template per site type: nuclear sites with strict security requirements, solar sites with isolated SCADA, wind sites with remote monitoring. Templates live in Git, every change has an explanation, and pull requests are reviewed by senior engineers.

## The pipeline, step by step

His GitOps workflow for adding, say, a new VLAN:

1. Branch, edit the YAML, commit with a descriptive message, open a pull request.
2. Automated syntax and policy-compliance checks, plus simulation in a virtual environment that mirrors production, with results posted on the PR.
3. Peer review of the business justification, security and approach, which catches design errors automation misses.
4. Canary deployment to one or two test sites, monitored for 30 to 60 minutes, then 10%, 50% and 100% of sites, with automatic rollback if anything fails.
5. Production rollout with dashboards and continuous health checks.

He credits pre-deployment validation with catching about 80% of errors before they go live.

## Zero trust you can enforce from code

The second half covers zero trust: verify explicitly, least privilege, assume breach. The concrete examples land well. SCADA systems at a wind site talk only to their control server and cannot reach corporate email, HR or other sites. Web tiers reach databases only through approved APIs. Access depends on identity, device posture, location and time, so the same engineer on a managed laptop during business hours gets in, and on public Wi-Fi at night is challenged. QoS keeps SCADA and voice traffic first even under attack.

He also covers routing automation that raises link costs on latency or loss, Cisco ACI's application-centric spine-leaf fabric with VXLAN, and defining one policy (SCADA on port 502 to its control server only) that is translated into AWS Transit Gateway, Azure Virtual WAN and on-prem firewall rules alike.

## Who should watch

Network teams who want to borrow DevOps practice without a big-bang rewrite, and DevOps engineers who keep getting blocked by manual network changes. His starting step costs nothing: put the existing configs of one device type into Git, and make every change go through it.

## Related Conf42 talks

- [Maksim Kupriianov on what to know about network incidents before chaos strikes](https://www.conf42.com/Incident_Management_2024_Maksim_Kupriianov_solving_network_incidents) at Conf42 Incident Management 2024.
- [Jeleel Muibi on why Terraform and Ansible are not an architecture](https://www.conf42.com/Platform_Engineering_2026_Jeleel_Muibi_terraform_ansible_architecture) at Conf42 Platform Engineering 2026.
- [Megha Kadur on GitOps dynamics in the new era of DevOps](https://www.conf42.com/DevSecOps_2024_Megha_Kadur_gitops_devops_navigation) at Conf42 DevSecOps 2024.

[Watch Imran Abdul's talk](https://www.conf42.com/DevOps_2026_Imran_Abdul_sdwan_networking_automation)

[Watch the talk on YouTube](https://youtu.be/OKWke4Hmt74).

## Watch the talk

[Infrastructure as Code for Enterprise Networks: Automating SD-WAN and Zero Trust](https://www.conf42.com/DevOps_2026_Imran_Abdul_sdwan_networking_automation) at Conf42 DevOps 2026.
