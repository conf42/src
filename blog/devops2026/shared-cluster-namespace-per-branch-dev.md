# One shared cluster, a namespace per branch, only changed services

Conf42 Blog, 2025-12-27, updated 2026-11-09. https://www.conf42.com/blog/devops2026/shared-cluster-namespace-per-branch-dev

In short: NetApp architect Ravi Babu Dasari at Conf42 DevOps 2026 on a shared-cluster dev platform that deploys only changed services per feature branch.

If your SaaS product has a hundred microservices, a dedicated test cluster per feature branch means a hundred copies of services you did not touch, idling on your cloud bill. At Conf42 DevOps 2026, Ravi Babu Dasari, a senior lead software engineer and architect at NetApp, showed the platform his team uses instead: one shared cluster holds a baseline of every service, and each feature branch gets its own namespace containing only the services it changed.

He calls it SDDP, a scalable development deployment platform, and he ends with a live demo on Rancher Desktop.

## Why canaries are not a dev environment

Dasari dismisses the two usual options quickly. Dedicated clusters are slow to provision and expensive to keep around, especially the ones nobody deleted. Canary builds are designed for production rollouts: you typically get one, not one per developer, and they get awkward fast with stateful services.

## Baseline plus overlays, stitched by ingress

When a developer pushes a branch, the platform creates a namespace, applies Helm or Kustomize overrides and gives the branch its own URL. Only modified services (and anything that must come along) are deployed there; everything else is served from the shared baseline, which CI keeps current from staging or production.

Three things hold it together:

- **Dynamic wildcard ingress rules**, so a request to a branch URL hits the branch's version of a service where one exists and the baseline otherwise.
- **Network policies**, so feature namespaces cannot talk to each other, only to approved baseline services. Without that, branches collide in ways that are miserable to debug.
- **Resource quotas**, so one runaway branch cannot slow the cluster for everyone.

A web portal sits on top for developers, QA and product owners to create sandboxes, pick baselines and share previews. In the demo, one branch deploys a new frontend and API while using the baseline backend; another deploys only the backend; calling the endpoints shows which version answered each hop.

## State is the hard part

Stateless services share easily. Databases, caches and blob storage do not: one branch adding a column another branch does not expect is how a shared environment corrupts itself. His answer is change analysis on the branch diff. A new endpoint with no schema change shares the database; a migration gets a replicated database in the branch namespace. Connection strings are injected per namespace, caches are isolated by key or instance. He suggests an LLM agent reading diffs across repositories is now good enough to make that share-or-replicate call automatically.

## Who should watch

Platform teams fielding a steady stream of own-environment requests for a large microservice estate, and anyone whose preview environments cost more than production. Dasari says he has been running and maintaining the platform at NetApp for years, and that the production version is a lot more complex than the demo. His adoption advice is incremental: start with easy stateless services like the UI, replicate stateful ones until you can share them safely, automate, then scale.

## Related Conf42 talks

- [Natalie Lunbeck's Ephemeral Environments 101](https://www.conf42.com/Cloud_Native_2024_Natalie_Lunbeck_ephemeral_environments) at Conf42 Cloud Native 2024, the clean-slate alternative.
- [Debosmit Ray on a declarative GitOps approach to developer platforms](https://www.conf42.com/DevOps_2024_Debosmit_Ray_gitops_automation_efficient_platforms) at Conf42 DevOps 2024.
- [Yuriy Bezsonov on scaling multi-cluster Kubernetes with GitOps](https://www.conf42.com/Kube_Native_2024_Yuriy_Bezsonov_multicluster_kubernetes_gitops) at Conf42 Kube Native 2024, for when one cluster stops being enough.

[Watch Ravi Babu Dasari's talk](https://www.conf42.com/DevOps_2026_Ravi_Babu_Dasari_microservices_saas_platforms)

[Watch the talk on YouTube](https://youtu.be/jXqPIOcf6Tk).

## Watch the talk

[Scaling Microservices Development: A Shared-Cluster Deployment Platform for Faster, Cost-Efficient SaaS Delivery](https://www.conf42.com/DevOps_2026_Ravi_Babu_Dasari_microservices_saas_platforms) at Conf42 DevOps 2026.
