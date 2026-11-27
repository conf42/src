# Four layers of defense for mission-critical managed Kubernetes

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/four-cs-defense-in-depth-for-managed-kubernetes

In short: Karthikeyan Thirumalaisamy of Microsoft lays out at Conf42 Kube Native 2025 a cloud, cluster, container and code defense-in-depth model for AKS, EKS and GKE.

Managed Kubernetes takes the control plane off your hands; it doesn't take the cluster admin with stolen credentials off your threat model. At Conf42 Kube Native 2025, Karthikeyan Thirumalaisamy, Principal Software Engineer at Microsoft, presented a defense-in-depth model for mission-critical services on AKS, EKS and GKE, built on the four Cs of cloud-native security: cloud, cluster, container and code.

The structure is the selling point. After each layer he asks the same question, what gap is still open, and the next layer answers it.

## What counts as mission-critical

He defines mission-critical services as systems whose failure has serious financial, safety or reputational consequences: payment processing and fraud detection in finance, EHR platforms and medical monitoring in healthcare, secure communications in defence, and code signing, security scanning and package verification in the software supply chain. All handle sensitive or regulated data.

The threats in managed Kubernetes are a familiar list taken seriously: insider risk at cloud, cluster and tenant admin level; misconfigurations such as permissive rules, public control-plane endpoints or missing encryption; malware injected through base images, registries or CI/CD; runtime exploits and container escapes; and supply-chain attacks on build systems and dependencies. His point is that the default protections from your cloud provider cover only part of that list.

## Cloud and cluster: shrink the surface

At the cloud layer the tools are network design: a hub-and-spoke topology with the hub handling routing, inspection and policy while spokes isolate workloads; strict firewall rules on both inbound and outbound traffic; and private clusters and endpoints so the control plane and container registry talk only over internal IPs.

That only protects the perimeter, so the cluster layer goes inside. A private API server with RBAC and least privilege. etcd encrypted at rest with a key management service, so a stolen disk doesn't hand over your secrets. Kubelet anonymous access disabled and ports restricted. Network policies to limit pod-to-pod and namespace traffic, cutting lateral movement. And OPA Gatekeeper as an admission controller to block privileged pods, require signed images and enforce configuration standards before anything runs.

## Container: trust the hardware, not the host

Even a well-secured cluster can lose a container to a kernel exploit or a breakout. Thirumalaisamy's answer is confidential computing. Confidential VMs use hardware-backed trusted execution environments to encrypt memory and isolate the VM from the hypervisor and host. Confidential containers extend that to individual workloads, running them in secure enclaves so code and data in use stay protected even if the kernel, container runtime or host is compromised. This is also the layer that answers the insider question: a privileged cloud operator can't read what the hardware won't decrypt for them.

## Code: lock down what actually runs

The last gap is the application itself: code that downloads packages, spawns processes or runs unverified scripts at runtime. The controls here are signed images from trusted registries, distroless images with no shell or package manager for attackers to use, immutable containers that are rebuilt rather than patched in place, seccomp profiles restricting system calls, and Falco for real-time detection of privilege escalation, unexpected file access and unknown processes.

He presents the four layers together as closing the known gaps, so that a breach of one layer still leaves three standing. That is the model's promise rather than a guarantee, but the layered argument holds up.

## Who should watch

Platform and security engineers running regulated workloads on managed Kubernetes, and anyone who needs a clear structure to audit a cluster against. If you already run confidential containers in production, the earlier sections will be review.

## Related talks

- Aleksandra Drobnjak gets hands-on with the runtime layer in [Runtime Kubernetes Security: Hands-On Threat Detection with Falcosidekick](https://www.conf42.com/Kube_Native_2024_Aleksandra_Drobnjak_kubernetes_security_falcosidekick_threat_detection).
- Srinivas Vallabhaneni on enclaves at scale: [Scaling Secure Enclaves: Confidential Computing in Go-Powered Distributed Systems](https://www.conf42.com/Golang_2025_Srinivas_Vallabhaneni_enclaves_security_confidential).
- Gresshma Atluri on the supply chain threats behind the code layer: [DevSecOps Supply Chain Defense](https://www.conf42.com/DevSecOps_2025_Gresshma_Atluri_supply_chain_threats).

[Watch Karthikeyan Thirumalaisamy's talk](https://www.conf42.com/Kube_Native_2025_Karthikeyan_Thirumalaisamy_security_missioncritical_kubernetes)

[Watch the talk on YouTube](https://youtu.be/X1mOrm9x-6Y).

## Watch the talk

[Cloud-Native Defense-in-Depth Security for Mission-Critical Services in Managed Kubernetes](https://www.conf42.com/Kube_Native_2025_Karthikeyan_Thirumalaisamy_security_missioncritical_kubernetes) at Conf42 Kube Native 2025.
