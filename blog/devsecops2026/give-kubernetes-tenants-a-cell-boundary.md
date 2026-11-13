# Multi-tenant Kubernetes needs a named boundary, not more rules

Conf42 Blog, 2026-09-10, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/give-kubernetes-tenants-a-cell-boundary

In short: Lahiru De Silva of WSO2 at Conf42 DevSecOps 2026 shows how OpenChoreo turns tenants into cells with four directional gateways instead of hand-written network policies.

In year one, a tenant is one namespace, three services and one network policy. By year three it's four namespaces, cross-namespace calls, a shared platform service and an external SaaS API, multiplied by every tenant you host. At Conf42 DevSecOps 2026, Lahiru De Silva, Associate Technical Lead at WSO2 and a maintainer of the CNCF Sandbox project OpenChoreo, argued that the problem isn't missing rules. The tenant was never modelled in the cluster in the first place, so the fix is to give the boundary a name, a shape and a default: a cell.

The second half uses OpenChoreo, WSO2's open source internal developer platform, as the reference implementation, so expect a product walkthrough.

## "Tenant" means three different things

Lahiru starts by pinning down the word. Internal teams as tenants is the soft form: implicit trust, boundaries by convention, and a conversation if someone crosses one. Business units or partners bring contracts, budgets and compliance, so boundaries start to carry weight. External SaaS customers are mutually untrusted, and one tenant reaching another's data can end the contract or start a lawsuit.

Kubernetes gives you building blocks rather than tenant isolation. On the control plane side that's namespaces, RBAC and resource quotas. On the data plane side it's storage and network isolation, gVisor or Kata Containers sandboxing, and node isolation with taints, tolerations or dedicated pools.

## Why network isolation is the hard one

Most of those knobs are set once by the platform team: a namespace per tenant, a node pool choice, a sandbox technology, a quota number. Network isolation is different, because who talks to whom is a property of the application, decided by the developers. A platform team can't template it in advance.

So teams reach for micro-segmentation with NetworkPolicies, which works fine while a tenant is one namespace. As applications spread out, Lahiru lists what's broken. There are no defaults: deny is something you must remember to write. There's no identity, because policies match labels and IPs, and reachability isn't authentication. Rules multiply with tenants instead of composing. And the result can't be reviewed: when an app times out, you can't point at the policy responsible without working through all of them. The tenant exists in the docs and the billing system, but not in the cluster.

## Cells: self-contained, with a gateway

Cell-based architecture comes from WSO2's reference architecture, co-authored in 2018 by Asanka Abeysinghe and Paul Fremantle. A cell is self-contained: components inside talk freely, and anything from outside comes through the cell gateway. It's one bounded context owned by one team, versioned and immutable, replaced as a unit rather than patched.

Traffic gets four named directions: northbound for public ingress, westbound for ingress from the tenant's other cells, southbound for egress to the outside world, and eastbound for egress to other cells in the organisation. Compared with a pile of rules, Lahiru's scorecard is clear. Scaling is additive (a new tenant is a new cell), the default comes built in, you can tell what a workload can reach by reading the cell config instead of running experiments, and the boundary is an object you can point at.

## Developers declare intent, the platform writes the policy

In OpenChoreo, creating a project creates a cell per environment, so two tenants with three projects across three environments get nine cells, and nobody hand-writes a network policy. The cell is rendered as a standard Kubernetes NetworkPolicy, or a Cilium policy when Cilium is installed. Developers declare endpoints at project, namespace, internal or external scope, and the platform translates that into gateways, listeners, hostnames and certificates.

Observability is scoped to the cell: logs, metrics and traces labelled with namespace, project, environment and component, plus Layer 7 visibility and TCP-level wire logs with Cilium, which the demo shows down to SYN and ACK. Tenancy itself is flexible, from a data plane (cluster) per tenant, through a namespace per tenant, to a project per sub-team.

The abstract also promises egress controls such as credential injection and quotas, the RBAC/ABAC handover and multi-cluster trade-offs; the recorded talk spends its time on the cell model and the walkthrough instead.

## Who should watch

Platform engineers running shared clusters for many teams or customers, especially if your tenant boundary today lives in a spreadsheet of NetworkPolicies. The first half, on why network policies don't compose, is useful whether or not you ever touch OpenChoreo.

## Related Conf42 talks

- [Instant KAI Sandboxes with vCluster: Multi-Tenant, Multi-Scheduler GPU Sharing](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant) by Piotr Zaniewski of vCluster at Conf42 Kube Native 2025.
- [Optimizing Multi-Tenant SaaS: Scalable Architectures for Performance, Security, and Cost Efficiency](https://www.conf42.com/Cloud_Native_2025_Shinu_Pushpan_saas_multitenancy_security) by Shinu Pushpan of Expedia Group at Conf42 Cloud Native 2025.
- [How Kernel Programming Escaped the Kernel](https://www.conf42.com/Observability_2026_Anais_Dotis_ebpf_linux_networking) by Anais Dotis of groundcover at Conf42 Observability 2026.

[Watch Lahiru De Silva's talk](https://www.conf42.com/DevSecOps_2026_Lahiru_De_Silva_kubernetes_multitenancy_isolation) from [Conf42 DevSecOps 2026](https://www.conf42.com/devsecops2026).

[Watch the talk on YouTube](https://youtu.be/anb_J0bEsVg).

## Watch the talk

[Cell-Based Isolation for Multi-Tenant Platforms on Kubernetes](https://www.conf42.com/DevSecOps_2026_Lahiru_De_Silva_kubernetes_multitenancy_isolation) at Conf42 DevSecOps 2026.
