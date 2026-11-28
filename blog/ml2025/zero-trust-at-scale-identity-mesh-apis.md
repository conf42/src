# Only 8% have finished zero trust; here's what the rest are stuck on

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/zero-trust-at-scale-identity-mesh-apis

In short: Palo Alto Networks' Naveen Kumar Birru covered zero trust at enterprise scale at Conf42 Machine Learning 2025, from identity sprawl to service meshes and APIs.

By the figures Naveen Kumar Birru cited, only 8% of organisations have fully implemented zero trust across the enterprise, while 49% are applying it in key areas and 34% are still planning. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Birru, Senior Principal Software Engineer at Palo Alto Networks, spent his talk on the gap between the pilot and the whole estate, and on the layers where it usually opens.

If you've already heard the never-trust-always-verify pitch, this is the follow-up about doing it across many clouds, many identity systems and a lot of legacy.

## Identity sprawl is the real perimeter problem

Birru's numbers set the scene: multi-cloud estates averaging 3.7 providers, most breaches traced to human error such as phishing and misconfiguration, and 70% of traffic moving east-west inside the network where the old perimeter never looked. His answer is that identity becomes the perimeter, for people, devices and workloads alike, checked continuously during a session rather than once at login.

The hard part is that most enterprises run several identity systems at once, and, per the figures he quoted, machine identities now outnumber human ones in most organisations. Federated identity and privileged identity management stop being nice-to-haves. His summary of the cultural shift: trust becomes something you earn, not something you inherit.

## Enforce at every layer, or attackers find the one you skipped

The architecture section is where the talk earns its title. Policy enforcement has to happen at three layers at once:

- **Network**: secure gateways, next-generation firewalls and SASE.
- **Service mesh**: mTLS between services and fine-grained policies in containerised environments.
- **Application**: API gateways that authenticate and authorise every request.

Any layer without consistent enforcement is where attackers look. Encryption runs through all of it: data in transit and at rest, east-west microservice traffic, API calls, and proper key management, so intercepted data stays useless.

## Service meshes are the connective tissue

Birru gives service meshes such as Istio, Linkerd and AWS App Mesh a central role in cloud-native zero trust. They provide mTLS so every service-to-service call is authenticated and encrypted, explicit policies on which services may talk, cryptographic workload identities that are hard to spoof, and telemetry on communication patterns that exposes anomalies. Without one, he argues, zero trust in microservice environments tends to fall short.

APIs get the same first-class treatment: gateways as central enforcement points, authentication for every consumer regardless of network origin, rate limiting and anomaly detection against abuse, and schema validation to reject malformed or malicious payloads before they reach the backend. Your zero trust strategy is only as strong as your weakest API.

## Legacy is the blocker everyone names

Around 60% of security leaders, he said, cite legacy compatibility as their biggest obstacle: older systems were never built for continuous verification. Add tool sprawl, skills gaps and cultural resistance. The organisations that get further treat it as a staged programme, starting with high-value targets and expanding, with leadership buy-in rather than as a security team side project. Observability ties it together, because you cannot secure what you cannot see.

## Who should watch

Security architects and platform engineers past the zero trust 101 stage who are now facing identity federation, mesh rollout or API gateways. It's a framework talk heavy on survey figures rather than a demo. Birru gave the same talk title at Conf42 Platform Engineering 2025, so pick whichever recording suits you.

## Related Conf42 talks

- [Beyond Perimeters: Implementing Zero Trust at Enterprise Scale](https://www.conf42.com/Platform_Engineering_2025_Naveen_Kumar_Birru_perimeters_zero_trust), Birru's version for Conf42 Platform Engineering 2025.
- [Ambient Mesh: The new sidecar less & faster Istio for zero trust](https://www.conf42.com/Kube_Native_2023_Md_Azmal_ambient_mesh_sidecar_zero_trust) by Md Azmal shows the mesh layer in practice.
- [Zero-Trust Security in DevOps: Automating Trust Verification Across 5G Pipelines](https://www.conf42.com/DevOps_2026_Vijayakumar_Venganti_zerotrust_security_networks) by Vijayakumar Venganti pushes verification into the delivery pipeline.

[Watch Naveen Kumar Birru's talk](https://www.conf42.com/Machine_Learning_2025_Naveen_Kumar_Birru_zero_trust_enterprise)

[Watch the talk on YouTube](https://youtu.be/8nT7zn7CUMw).

## Watch the talk

[Beyond Perimeters: Implementing Zero Trust at Enterprise Scale](https://www.conf42.com/Machine_Learning_2025_Naveen_Kumar_Birru_zero_trust_enterprise) at Conf42 Machine Learning 2025.
