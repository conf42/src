# Platform engineering is the glue between network and app teams

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/platform-engineering-meets-the-network-stack

In short: Sunil Jorepalli of JPMorgan Chase at Conf42 Platform Engineering 2025 on service meshes, API gateways, zero trust and IaC as one network platform.

Developers want to ship to AWS, Azure and the on-prem data centre without learning how packets get between them. At Conf42 Platform Engineering 2025, Sunil Jorepalli of JPMorgan Chase, who has spent around 16 years in networking, security and automation, argued that the platform team is where that wish gets granted: it hides the network plumbing behind self-service, and it bakes security in so nobody has to remember it.

It is a short, structured talk (he promises 15 minutes and keeps to it), and it works best as a map of the tools a network-aware platform needs rather than a build log.

## Friction is a security problem

Sunil's framing starts with four pressures: hybrid and multi-cloud complexity, zero trust demanding verification at every layer, latency-sensitive apps (payments, gaming) that expect milliseconds, and developer experience. The last one is the sneaky one. When the official path is slow, he says, developers bypass the security controls or build shadow infrastructure just to move faster. A platform that is pleasant to use is also a platform people don't route around.

So his definition of platform engineering is practical: abstract the complexity, automate the repetitive operations, and give teams a secure self-service way in. It is the bridge between developers, operations and security, and it should feel the same whether the workload lands on-prem, in a cloud, or at the edge.

## Four tool sets, one job each

The core of the talk splits the stack into four layers, each with a clear responsibility:

- **Service mesh** (Istio, Linkerd) for east-west traffic: retries, observability, and mTLS between services, so developers don't hand-roll any of it.
- **API gateways** (NGINX, Apigee, Kong and open-source options) for the north-south edge: ingress security, authentication, and a clean front door for consumers. He notes a drift towards open-source gateways that teams can extend themselves.
- **Zero trust** with identity-aware proxies and policy-driven access, citing SPIFFE/SPIRE for service identity and Google's BeyondCorp model for enterprise access. The perimeter firewall as the only line of defence is, in his words, all gone.
- **Programmable infrastructure**: Terraform plus GitOps with Argo CD or Flux, so every change is versioned, reviewed and reproducible.

He is explicit that the names are examples, not endorsements. Pick what fits the business; the layering is the point.

## The forgotten firewall rule

The most relatable part is about repetition. A new app needs an IP address, a DNS name, firewall rules, security config. Done by hand through tickets, someone eventually skips a step, and the missing firewall entry shows up in production. Encoding those steps once, in code that a reviewer approves, turns a checklist into a pipeline. Fewer tickets, fewer 2am "where did I miss it?" moments.

His design rules follow from that: abstract without hiding so much that developers lose visibility when they need it, keep environments consistent, and be secure by design with policies from day one and continuous measurement.

He closes with one anonymised case: a multi-cloud microservices shop that adopted a mesh, a gateway and IaC together, and saw both recovery time and platform adoption improve. Start small, automate incrementally, measure continuously.

## Who should watch

Network and security engineers moving into platform roles, and platform teams who treat networking as somebody else's problem. If you already run Istio behind Kong with SPIRE identities and Argo CD, this is a recap you could have given; if you are deciding where each of those belongs, it is a tidy 15-minute orientation.

## Related Conf42 talks

- [Md Azmal on Istio ambient mesh for zero trust](https://www.conf42.com/Kube_Native_2023_Md_Azmal_ambient_mesh_sidecar_zero_trust) goes deeper on the sidecar-less mesh option.
- [Roman Rastiehaiev compares open-source API gateways](https://www.conf42.com/Cloud_Native_2025_Roman_Rastiehaiev_api_gateways_comparison), handy if you are choosing the front door.
- [Atif Siddiqui on cloud network segmentation in pursuit of zero trust](https://www.conf42.com/Platform_Engineering_2023_Atif_Siddiqui_cloud_network_segmentation_in_pursuit_of_zero_trust) pairs well with the zero trust section.

[Watch Sunil Jorepalli's talk](https://www.conf42.com/Platform_Engineering_2025_Sunil_Jorepalli_stack_layers_bridging)

[Watch the talk on YouTube](https://youtu.be/5j1uKBJ57hw).

## Watch the talk

[Bridging the Layers: Platform Engineering in the Modern Network Stack](https://www.conf42.com/Platform_Engineering_2025_Sunil_Jorepalli_stack_layers_bridging) at Conf42 Platform Engineering 2025.
