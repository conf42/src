# Gcore moved managed Kubernetes off Magnum and ran control planes as pods

Conf42 Blog, 2023-03-29. https://www.conf42.com/blog/cloud2023/cluster-api-control-plane-as-pods

In short: Andrei Novoselov (Gcore) at Conf42 Cloud Native 2023 on replacing OpenStack Magnum with Cluster API and control planes as pods in a service cluster

Running a managed Kubernetes service on OpenStack Magnum meant fixing failed clusters by hand-editing rows in the production MariaDB. At Conf42 Cloud Native 2023, Andrei Novoselov, who leads the team behind Gcore's cloud platform services, explained why Gcore moved its managed Kubernetes to Cluster API, and how the team went further than upstream: no control plane VMs at all, just pods in a Gcore-run service cluster, with OpenVPN and Argo CD filling the gaps that created.

It is a migration story from an operator's chair, with architecture diagrams and kubectl output rather than a product pitch.

## What was wrong with Magnum?

Magnum orchestrates container clusters (Docker Swarm and Kubernetes) and leans on OpenStack Heat to write cloud-init configs and update node software. Both follow the usual OpenStack shape: an HTTP API, RabbitMQ, and a conductor or engine doing the work, plus a Heat agent on every VM.

In Gcore's Magnum design, each cluster had three control plane VMs running etcd, kube-apiserver, controller manager, scheduler and DNS as Podman containers under systemd, hidden behind cloud load balancers and a firewall. The problems he lists:

- **No control plane isolation.** Magnum gives the user full admin access to the control plane components. "And that's not how you do the managed Kubernetes service," Andrei Novoselov said at Conf42 Cloud Native 2023.
- **Extra API load.** Magnum and Heat had to sit behind the Gcore Cloud API, so every request went through it twice.
- **Fragility.** If Octavia or RabbitMQ hiccuped during a create or update, the cluster went into an error state with no CLI way back. Recovery meant fixing the root cause, then updating Magnum's row and Heat's stacks directly in the database.
- **Observability.** Checking every kube-apiserver meant SSH to the control plane nodes or writing your own exporter.
- **No bare metal workers.**
- **Version lag.** On OpenStack Yoga, about a year old at the time, Magnum topped out at Kubernetes 1.23 while upstream supported 1.24 to 1.26. He reckons OpenStack runs about two Kubernetes versions behind.

On the database surgery: "And it's a lot of update operations on the production database, which is not what you want to do on daily basis."

## What does Cluster API give you?

Cluster API manages the full lifecycle (create, scale, upgrade, destroy) of Kubernetes clusters through a declarative API, on premises or in any cloud, with swappable implementations. It is four controllers running inside Kubernetes: the core controller manager, a bootstrap provider, a control plane provider and an infrastructure provider. Out of the box you get kubeadm, MicroK8s and Talos for bootstrap and control plane, and infrastructure providers from AWS and Azure to Hetzner and OpenStack. A Cluster object points at a control plane and an infrastructure reference; machine deployments describe worker pools; only the infrastructure objects change between clouds.

Upstream still had gaps for Gcore: no Gcore provider, no control plane isolation, three VMs per control plane with kubeadm, and the bootstrapping problem that you need a Kubernetes cluster to create one.

## How did Gcore build it?

They leaned into that last point. Gcore already ran a service cluster for Cluster API, so the client control planes moved into it: one namespace per client cluster holding the Cluster API custom resources and the control plane pods side by side. That required a Gcore bootstrap controller, a Gcore control plane controller and an infrastructure provider called CAPGC, built with help from colleagues at Wargaming. Client networks now contain only worker nodes.

Two pieces close the gaps:

- **OpenVPN for reverse connectivity.** Workers reach kube-apiserver through a load balancer, but kubectl logs, port-forward and admission webhooks need the API server to reach into the client network. Each kube-apiserver pod gets a second container, an OpenVPN client, which connects to an OpenVPN server pod in the client cluster and receives routes to node, pod and service networks.
- **Argo CD for self-repair.** The service cluster runs Argo CD apps for kube-proxy, kube-dns, Calico and the OpenVPN server in each client cluster. Delete one with kubectl and Argo CD puts it back.

## What did they get?

Speed, because spinning up pods beats creating VMs. Kubernetes 1.24, 1.25 and 1.26 out of the box, with easy upgrades of in-cluster infrastructure through Argo CD. A reconciliation loop: when a load balancer create fails, Cluster API simply retries until it works, so fixing Octavia or RabbitMQ no longer means repairing every cluster in the region. Bare metal worker nodes, which customers had asked for. Plain kubectl visibility across all clusters, control planes, machine deployments and machines. And no control plane nodes to pay for.

## Who should watch

Platform teams running Kubernetes for others, especially on OpenStack, and anyone weighing hosted control planes against per-cluster VMs. Pair it with [Stephen Levine on scaling multi-cluster Kubernetes](https://www.conf42.com/Kube_Native_2023_Stephen_Levine_scaling_multi_cluster), [Yuriy Bezsonov on multi-cluster GitOps](https://www.conf42.com/Kube_Native_2024_Yuriy_Bezsonov_multicluster_kubernetes_gitops) and [Utibeabasi Umanah on GitOps with Argo CD](https://www.conf42.com/Kube_Native_2022_Utibeabasi_Umanah_gitops_argocd).

[Watch Andrei Novoselov's talk](https://www.conf42.com/Cloud_Native_2023_Andrei_Novoselov_managing_k8s_openstack_magnum_cluster_api)

## From G-Core Labs

- [Gcore](https://gcore.com/): edge cloud provider with 20+ locations, including the managed Kubernetes service this talk describes.

[Watch the talk on YouTube](https://youtu.be/HpdBZhmVuqQ).

## Watch the talk

[Managing k8s: moving from the Openstack Magnum to the Cluster API](https://www.conf42.com/Cloud_Native_2023_Andrei_Novoselov_managing_k8s_openstack_magnum_cluster_api) at Conf42 Cloud Native 2023.
