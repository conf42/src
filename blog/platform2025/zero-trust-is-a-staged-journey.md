# Zero trust at enterprise scale is a staged journey, not a product

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/zero-trust-is-a-staged-journey

In short: Naveen Kumar Birru of Palo Alto Networks at Conf42 Platform Engineering 2025 on identity, microsegmentation, service mesh mTLS and API gateways for zero trust.

The castle-and-moat model assumes the attacker is outside the wall. Most traffic now never crosses the wall at all. At Conf42 Platform Engineering 2025, Naveen Kumar Birru, Senior Principal Software Engineer at Palo Alto Networks, walked through what zero trust means once you strip the marketing off: verify every request, base trust on identity instead of network location, and enforce policy at every layer of the stack.

## Why the perimeter stopped working

Birru opens with the numbers he uses to make the case: most enterprises run several cloud providers, the large majority of breaches still come from human error such as phishing and misconfiguration, and average breach costs keep rising. He adds that around 70% of traffic now flows east-west, inside the perimeter, where the moat does nothing. The model he argues for assumes breaches will happen and focuses on limiting the damage.

The three principles are short: continuous verification, identity-based trust and no default trust. His summary of the shift is the most quotable line in the talk: trust becomes something you earn, not something you inherit.

## Identity is the new perimeter

Identity, whether a person, a device or a workload, carries most of the weight. Following the NIST zero trust guidance, authentication and authorisation are dynamic and enforced before every access. The difficulty is that most enterprises run several identity systems, and machine identities now outnumber human ones in a majority of organisations. His recommendations are federated identity across environments, privileged identity management, and continuous authentication that rechecks identity during a session rather than only at login.

Access decisions then become contextual: identity and behaviour patterns, device health, location, time and data sensitivity combined into an adaptive risk decision rather than a static role check.

## Contain the blast radius

Microsegmentation applies controls at the workload level instead of network zones, so only explicitly allowed services can talk. Birru cites a large reduction in breach scope for segmented environments; the mechanism is the useful part: a compromised service cannot wander sideways, so a potential company-wide breach becomes a contained incident.

Encryption follows the same logic. Data in transit, at rest, in API calls and in east-west microservice traffic is encrypted with proper key management, so an intercepted packet is still useless.

## Enforce at three layers

The platform-engineering section maps zero trust onto the stack:

- **Network:** secure gateways, next-generation firewalls and SASE.
- **Service mesh:** Istio, Linkerd or AWS App Mesh providing mTLS on every service-to-service call, explicit policies on which services may talk, telemetry on communication patterns, and cryptographic workload identities that are hard to spoof.
- **Application:** API gateways that authenticate every consumer regardless of network origin, rate-limit, detect anomalies and validate schemas to block malformed payloads.

His warning on APIs is blunt: a zero trust architecture is only as strong as its weakest API. And he stresses that inconsistent enforcement across distributed environments is where attackers look first.

## You cannot secure what you cannot see

Observability gets a full section: security events collected across cloud and on-prem, behavioural baselines to spot deviations, automated responses that contain threats when detected, and feedback loops that tune policies over time. Built in from the start, not bolted on.

## Start with high-value targets

The closing advice is the honest bit. Only a small minority of organisations have fully implemented zero trust; most are partway or still planning. Legacy systems that were never designed for continuous verification are the top obstacle, followed by tool sprawl, skills gaps and culture. Successful programmes start with high-value targets, prove impact, then expand, with leadership, operations and business units aligned. Zero trust is a strategic commitment, not something you buy and tick off.

## Who should watch

Platform and security engineers who need a structured overview to plan a programme or brief leadership. It is a broad survey backed by industry statistics rather than a Kubernetes walkthrough, so do not expect YAML.

## Related Conf42 talks

- Md Azmal on [Ambient Mesh, sidecar-less Istio for zero trust](https://www.conf42.com/Kube_Native_2023_Md_Azmal_ambient_mesh_sidecar_zero_trust) at Kube Native 2023.
- Atif Siddiqui on [cloud network segmentation in pursuit of zero trust](https://www.conf42.com/Platform_Engineering_2023_Atif_Siddiqui_cloud_network_segmentation_in_pursuit_of_zero_trust) at Platform Engineering 2023.
- Cynthia Akiotu on [why observability must start with identity](https://www.conf42.com/Observability_2025_Cynthia_Akiotu_identity_access_breach) at Observability 2025.

[Watch Naveen Kumar Birru's talk](https://www.conf42.com/Platform_Engineering_2025_Naveen_Kumar_Birru_perimeters_zero_trust)

[Watch the talk on YouTube](https://youtu.be/3f62DUCVQCc).

## Watch the talk

[Beyond Perimeters: Implementing Zero Trust at Enterprise Scale](https://www.conf42.com/Platform_Engineering_2025_Naveen_Kumar_Birru_perimeters_zero_trust) at Conf42 Platform Engineering 2025.
