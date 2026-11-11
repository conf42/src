# Keeping 100k reverse tunnels alive across six EKS regions

Conf42 Blog, 2023-09-28. https://www.conf42.com/blog/kubenative2023/teleport-cloud-100k-reverse-tunnels-six-regions

In short: Stephen Levine (Teleport) at Conf42 Kube Native 2023 on the ingress, rollout and networking choices behind Teleport Cloud's multi-cluster Kubernetes.

Most Kubernetes ingress advice assumes connections are short and a dropped one gets retried. Teleport Cloud has the opposite problem: more than 100,000 reverse tunnels that are meant to stay open indefinitely, and every disconnect cuts someone off from their infrastructure. At Conf42 Kube Native 2023, Stephen Levine, Software Engineer at Teleport, walked through how the Teleport Cloud team runs that on EKS clusters in six regions, including the two approaches they threw away for each of the three hard parts.

It's a vendor talk in the sense that the system is Teleport's own SaaS. It's also one of the more honest multi-cluster architecture talks around, because it spends as much time on what failed as on what shipped.

## What makes this workload awkward?

Teleport is an open source infrastructure access platform: agents inside your Kubernetes clusters, SSH hosts, databases, web apps and Windows desktops open reverse tunnels out through the firewall to a Teleport proxy, and users connect to the proxy instead of the resource. The auth server handles authentication, authorisation and roles, and the proxies cache what they need from it.

Teleport Cloud runs a dedicated Teleport instance per customer: over 10,000 pods and over 100,000 reverse tunnels across six regions, with proxies in different regions peering over gRPC so a client in one region can reach a resource tunnelled into another. "It's really, really important that we provide a very stable network stack for this platform," Stephen Levine said at Conf42 Kube Native 2023. The platform moved to EKS from Gravity, and the requirements split into ingress, coordinated deployment and container networking.

## Why not anycast, and why not NGINX?

Anycast via AWS Global Accelerator was the first attempt, and it was attractive: one stable IP address for everyone, DNS never changes. Routing wasn't stable enough for tunnels that live for days, even with logic to resume dropped tunnels quickly. "It really just wasn't stable enough to provide really consistent, really highly available connectivity," Stephen said.

Open source NGINX came next. It supports ALPN routing, which lets the ingress separate client connections from agent connections on port 443 without terminating TLS. But it had no in-process configuration reloading, so every route change meant a new NGINX instance, and memory usage climbed with how often the routes changed.

What shipped: Route 53 latency records published by the ExternalDNS operator, pointing at stateless Network Load Balancers in each region (they don't drop connections when things change underneath), and Envoy Proxy configured through Gateway API with Teleport's own fork of Envoy Gateway that adds ALPN routing on TLS routes via annotations.

## The minReadySeconds trick

The neatest idea in the talk is the zero-downtime proxy upgrade. A Kubernetes Deployment's minReadySeconds keeps the old and new pod generations both serving for a set period after the new pods are ready. Teleport uses that window to let existing agents open fresh tunnels to the new proxies while the old ones still carry traffic. Once the new tunnels are established, a custom controller flips the Service labels from the old generation to the new, old connections drain, and only then do the old pods shut down.

## How do you roll out across six regions without a single point of failure?

Upgrades need ordering: auth servers before proxies (because of how auth caches proxy heartbeats), and sometimes not every region's proxies at once. GitOps with Flux was ruled out for two reasons: customer data belongs in Postgres, not a Git repo, and Flux only pushes one way, while the rollout needs status from each region to decide the next step. Cross-cluster reconcilers sharing one custom resource in a management cluster created a single point of failure and multiple writers fighting over one status field. KubeFed had the right model but is no longer active.

So the team built Sync Controller, open sourced under Apache 2 days before the talk. A tenant resource in the management cluster creates one Teleport deployment resource per region; Sync Controller in each region copies the spec down and the status back up. Lose the management cluster and every regional cluster keeps reconciling on its own. Tenant data lives as JSONB in Postgres, and the portal validates edits against the CRD's own OpenAPI schema, so nothing gets stored that the cluster would reject.

## And the cross-region networking?

Cilium Global Services, with a dedicated etcd, which handled the pod churn of mass tenant updates and Cilium upgrades best. Auth servers run in several availability zones of one region only; proxies elsewhere reach them through a global service of the same name, and custom controllers can redirect proxy traffic to the nearest region where a region has no proxies.

## Who should watch

Anyone running stateful, long-lived connections through Kubernetes ingress, or designing a multi-cluster control plane and wondering whether GitOps fits. Pair it with [Shane Utt on Gateway API beyond Ingress](https://www.conf42.com/Cloud_Native_2023_Shane_Utt_beyondkubernetes_ingress_gateway_api), [Natan Silnitsky on migrating multi-cluster Kafka with zero downtime](https://www.conf42.com/Cloud_Native_2022_Natan_Silnitsky_migrating_multi_cluster_managed_kafka_0_downtime), and [Yuriy Bezsonov on multi-cluster Kubernetes with GitOps](https://www.conf42.com/Kube_Native_2024_Yuriy_Bezsonov_multicluster_kubernetes_gitops) for the approach Teleport decided against.

[Watch Stephen Levine's talk](https://www.conf42.com/Kube_Native_2023_Stephen_Levine_scaling_multi_cluster) from [Conf42 Kube Native 2023](https://www.conf42.com/kubenative2023).

## From Teleport

The open source pieces Stephen pointed to: Sync Controller at [github.com/gravitational/sync-controller](https://github.com/gravitational/sync-controller), the Teleport Cloud fork of Envoy Gateway at [github.com/gravitational/gateway](https://github.com/gravitational/gateway), and Teleport itself at [github.com/gravitational/teleport](https://github.com/gravitational/teleport), all Apache 2.

- Teleport: [goteleport.com](https://goteleport.com/)
- [About Teleport](https://goteleport.com/about)
- The [Teleport blog](https://goteleport.com/blog)
- Teleport on [YouTube](https://www.youtube.com/channel/UC1O9RGv3FGJau091DD09ooQ)
- Teleport on Conf42: [conf42.com/teleport](https://www.conf42.com/teleport)

[Watch the talk on YouTube](https://youtu.be/f4qxdG79QrI).

## Watch the talk

[Scaling Multi-cluster Kubernetes at Teleport Cloud](https://www.conf42.com/Kube_Native_2023_Stephen_Levine_scaling_multi_cluster) at Conf42 Kube Native 2023.
