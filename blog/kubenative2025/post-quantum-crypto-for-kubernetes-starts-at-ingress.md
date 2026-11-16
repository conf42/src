# Post-quantum crypto for Kubernetes should start at the ingress

Conf42 Blog, 2025-10-09, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/post-quantum-crypto-for-kubernetes-starts-at-ingress

In short: Derek Asir Muthurajan Caleb (Broadcom) at Conf42 Kube Native 2025 on where Kubernetes depends on RSA and ECC and how to phase in hybrid PQC.

Every trust relationship in a Kubernetes cluster, from kubectl to the API server to pod-to-pod mTLS, rests on RSA or elliptic-curve keys that a large enough quantum computer could break with Shor's algorithm. At Conf42 Kube Native 2025, Derek Asir Muthurajan Caleb, Principal R&D Engineer at Broadcom, mapped where that exposure sits and laid out a phased migration to post-quantum cryptography (PQC): hybrid handshakes first, external ingress next, then the service mesh, then etcd and the control plane.

It is a planning talk, not a demo, and it is refreshingly specific about the costs.

## Kubernetes is PKI all the way down

Derek's inventory of what breaks is the useful part. API server traffic is protected by TLS. Service mesh mTLS between microservices relies on RSA and ECC key exchange. Ingress terminates external TLS with classical certificates. Registry pulls and pushes are authenticated by classical signatures. If the PKI falls, so does the rest: man-in-the-middle attacks become easy, secrets such as database passwords and API tokens become readable, malicious pods can impersonate services, and backups encrypted today become tomorrow's plaintext.

His summary: without a secure PKI, trust inside the cluster becomes impossible to establish or maintain. Harvest-now, decrypt-later makes that a problem for today's traffic, not just tomorrow's.

## NIST has picked the algorithms

The answer comes from NIST's completed post-quantum project: lattice-based key encapsulation (ML-KEM, the Kyber family) for key exchange, Dilithium-family signatures for authentication, and hybrid modes that combine classical and post-quantum algorithms so upgraded and legacy systems can still talk. With standards final, Derek argues the transition has moved from optional to inevitable.

## Four places to put it, in order

PQC has to land everywhere Kubernetes uses classical crypto, and he gives the order:

1. **Ingress controllers.** The most exposed surface and the easiest win. Clients negotiate a hybrid TLS handshake, the ingress swaps in post-quantum key exchange while staying backward compatible, and pods behind it receive traffic over a quantum-safe hop. Support is emerging in OpenSSL post-quantum branches, Envoy and NGINX.
2. **The service mesh.** Istio and Linkerd depend on mTLS, so PQ-enabled crypto libraries go into the Envoy sidecars, the mesh CA issues hybrid certificates, hybrid mode keeps old and new workloads talking, and latency gets watched closely.
3. **Secrets and etcd.** Post-quantum certificates are much larger, which stresses etcd storage and replication. Use PQ-safe key management such as Vault or a cloud KMS, and rotate long-lived secrets automatically.
4. **Core control plane.** Last, once the rest is proven.

Throughout: keep rollback paths, canary deployments and feature flags.

## The bill comes due in the handshake

Derek doesn't oversell it. His figures put the PQ handshake at about 3.2x the cost of classical algorithms, certificates around 10x larger, and production-grade library maturity at roughly 60%. His comparison has RSA-2048 at a 1x handshake with universal compatibility, and the Kyber-768 option at 3.2x with limited compatibility. Early adopters, he notes, should budget for two to four times the handshake latency and plan capacity accordingly. Polyglot microservices add another snag: PQC support differs across languages and frameworks.

His operational suggestions are very Kubernetes: manage PQ policy with operators and custom resources, ship it via Helm charts, and make cryptographic health an observability signal. Track which algorithms handshakes actually use, the share of connections on PQ, and the latency and error impact.

## Who should watch

Platform security teams, anyone running a service mesh, and compliance-minded orgs in finance where, he notes, early adopters are already experimenting. The call to action is achievable this quarter: inventory your cryptographic dependencies, stand up a PQ-enabled ingress and mesh in staging and measure it, and use hybrid crypto for new deployments.

## Related Conf42 talks

- [Preparing for the Impact of Quantum Computing on Cloud Security](https://www.conf42.com/Quantum_Computing_2025_Pavan_Nutalapati_quantum_cloud_security) takes the same threat to cloud security broadly.
- [Ambient Mesh: The new sidecar less & faster Istio for zero trust](https://www.conf42.com/Kube_Native_2023_Md_Azmal_ambient_mesh_sidecar_zero_trust) explains the mesh layer you would be upgrading.
- [Encrypting Your Way to Safety: Data Security in Kubernetes](https://www.conf42.com/Kube_Native_2024_Victor_Onyenagubom_data_security_encryption_kubernetes) covers encryption at rest and in transit as it stands today.

[Watch Derek Asir Muthurajan Caleb's talk](https://www.conf42.com/Kube_Native_2025_Derek_Asir_Muthurajan_Caleb_quantum_security_infrastructure)

[Watch the talk on YouTube](https://youtu.be/NYO2ROtL_nA).

## Watch the talk

[Quantum-Resistant Kubernetes: Securing Cloud Native Infrastructure for the Post-Quantum Era](https://www.conf42.com/Kube_Native_2025_Derek_Asir_Muthurajan_Caleb_quantum_security_infrastructure) at Conf42 Kube Native 2025.
