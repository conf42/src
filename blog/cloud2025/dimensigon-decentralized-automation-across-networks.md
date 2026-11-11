# Automating across networks that can't see each other, with Dimensigon

Conf42 Blog, 2025-03-05. https://www.conf42.com/blog/cloud2025/dimensigon-decentralized-automation-across-networks

In short: Daniel Moya of Dimensigon at Conf42 Cloud Native 2025 demos open source, decentralised automation with a REST API on every server and proxied transfers.

Most automation tools assume one control node that can reach every server. At Conf42 Cloud Native 2025, [Daniel Moya](https://www.conf42.com/Cloud_Native_2025_Daniel_Moya_automation_decentralization_orchestration) of Dimensigon demoed the opposite: an open source Python platform that puts a RESTful API on every server, lets any node manage the others, and routes commands and software through bridge nodes when two networks can't talk directly.

The talk is essentially a long hands-on tutorial in Docker, built and narrated live. If you want slides and theory, look elsewhere. If you want to see what using the tool feels like, keystroke by keystroke, this is it.

## A "dimension" is a cluster of servers across subnets

Dimensigon (DM for short) is both the company name and the tool's. It targets a specific, common headache: two or more subnets or data centres connected only through a few specific points, which you still want to manage as one group. That group is called a dimension, and Moya recommends one per lifecycle stage, so production, pre-production and development each get their own, for organisation and security.

The architecture lives in one GitHub repository with three components:

- **dmcore**, a Python Flask service that exposes the RESTful API on each server
- **the elevator**, which detects a new version anywhere in the network and spreads the upgrade
- **dshell**, a command-line client built on prompt_toolkit that turns commands into REST calls, with tab completion everywhere

A web UI is planned. Metadata lives in a distributed database built on SQLAlchemy, with logic to handle split brain during network instability and keep the surviving group consistent.

## The demo network: two subnets and a bridge

The setup is easy to reproduce. Two Docker networks stand in for two data centres, one container is attached to both as a bridge, and the rest live on one side or the other. A new dimension starts with one node, which issues single-use join tokens; every other server joins with its own token, generated from any node that is already a member. From then on, any node can administer the others.

A catalog of actions, orchestrations and software replicates across the dimension with a version watermark. When a node falls behind, `manager catalog refresh` pulls the newest one, and nodes also update automatically in the background.

## Actions, steps and orchestrations

The automation model is layered for reuse. An action is a reusable unit: a shell command, Python, an Ansible playbook, an HTTP request, or one of the built-in internal actions. Steps reference actions, orchestrations are made of steps, and orchestrations can themselves be steps in larger ones. Every step can have an undo, with conditions for when the orchestration counts as failed.

Changing an orchestration creates a new version rather than overwriting the old one, which keeps runs reproducible. Orchestrations export to and import from JSON, and Moya hopes to grow a shared orchestration library. Secrets go in a vault, scoped per environment, and are referenced with double curly braces in the code. The hello-world orchestration runs on three nodes at once and reports success, return code, parameters and elapsed time per server.

## Distributed commands and proxied software transfers

Two features stand out for day-to-day operations. Distributed commands open a shell against a set of target servers so every command you type runs on all of them, handy for pre-flight checks or troubleshooting many hosts. Moya says the idea came from a distributed shell he had used on Oracle Exadata.

The software library is the other. You register a file on any node, and it can be sent to any other node, either one-off or as a step in an orchestration. In the demo, a 200 MB file moves from a server on one network to a server on the other through the bridge, split into chunks and reassembled at the destination. His pitch for it is concrete: no NFS mounts between parts of the company, just a transfer that routes around the network gaps.

Other commands cover log federation (subscribing to a log or directory and replicating it elsewhere), locks for critical orchestrations, server routes and hop costs, and pings that check whether Dimensigon is alive on a node.

## Who should watch

Ops engineers and DBAs managing servers spread across segmented networks, on-prem and cloud, who find SSH jump hosts and a single Ansible control node limiting. It is a tool walkthrough, so watch it with a terminal open.

## Related Conf42 talks

- [Reduce Toil by Improving Your Automation](https://www.conf42.com/DevOps_2024_Mandi_Walls_improve_automation_reduce_toil) by Mandi Walls (PagerDuty) at Conf42 DevOps 2024.
- [Beyond Connectivity: Full Life-Cycle Infrastructure Orchestration and Cost Engineering](https://www.conf42.com/Platform_Engineering_2024_Long_Zhang_Vladimir_Shcherbinin_connectivity_infrastructure_engineering) by Long Zhang and Vladimir Shcherbinin (Electrolux) at Conf42 Platform Engineering 2024.
- [Mastering Cloud Security Automation: A Comprehensive Guide to Terraform and Chef Integration](https://www.conf42.com/Quantum_Computing_2024_Karthik_Jataprole_cloud_security_automation) by Karthik Jataprole (Workday) at Conf42 Quantum Computing 2024.

[Watch Daniel Moya's talk](https://www.conf42.com/Cloud_Native_2025_Daniel_Moya_automation_decentralization_orchestration) or the [YouTube recording](https://youtu.be/WsReAFDsDTk).

## From Dimensigon

Dimensigon was a Silver sponsor of Conf42 Cloud Native 2025. The tool in the talk is Dimensigon DM, open source and written in Python, with its components available from GitHub and PyPI.

- [Dimensigon](https://www.dimensigon.com/): the project and company behind DM
- [All Conf42 Cloud Native 2025 talks](https://www.conf42.com/cloud2025)

## Watch the talk

[Orchestrating the Future: Decentralized Automation & RESTful Integration with Dimensigon DM](https://www.conf42.com/Cloud_Native_2025_Daniel_Moya_automation_decentralization_orchestration) at Conf42 Cloud Native 2025.
