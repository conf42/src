# Network and security teams belong on the same stack

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/network-and-security-teams-should-share-one-stack

In short: Cisco product manager Sharanya Prasad argued at Conf42 Machine Learning 2025 for converging networking and security with SDN, SASE and zero trust.

When the network team and the security team run separate tools, separate policies and separate on-call rotations, the attacker gets to work in the gap between them. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Sharanya Prasad, Senior Product Manager at Cisco, argued that the two functions should converge into one framework, so visibility, detection and response all come from the same place.

It's a strategy talk from a product manager, about 15 minutes long, and best read as a briefing for the people who set the roadmap rather than the people who write the firewall rules.

## Silos are a security vulnerability

Prasad's starting point is organisational. Isolated networking and security teams produce fragmented systems, inconsistent policies and slow incident detection, which adds up to business risk. Building security into the network infrastructure itself gives unified visibility, faster detection and automated response. Her examples of what that buys are drawn from organisations that did it: a Fortune 500 bank cutting security incidents by 35% with integrated software-defined networking, a hospital taking breach containment from over 48 hours to under 60 minutes after rolling out SASE, and a manufacturer reaching 99.8% uptime on its OT systems with zero trust principles.

## Four technologies carry the convergence

She names four pillars:

- **Software-defined networking**, which routes traffic dynamically based on real-time security needs.
- **Secure Access Service Edge (SASE)**, her favourite topic, which unifies networking and security at the edge so the same policy follows the user wherever they connect.
- **Zero trust architecture**, verifying every user and device to cut lateral movement.
- **AI-powered security**, using machine learning to spot anomalies and automate responses, which is how this talk earns its slot at an ML conference.

## The pyramid is about people, not boxes

The most useful slide is an organisational pyramid. Consolidated infrastructure sits at the base, integrated toolsets that bridge networking and security workflows come next, then cross-functional teams with shared accountability and success metrics, and strategic alignment between business and security goals at the top. The point is that buying a converged product does nothing if the two teams still don't talk.

Prasad is straightforward about why this is hard. The biggest gap is skills: few people understand both domains deeply. Then come teams clinging to old roles, legacy infrastructure that was never designed for converged architectures, and budgets that lose to other priorities even when the ROI looks good on paper.

## Assess, pilot, then expand

Her roadmap is phased: assess the current infrastructure and vulnerabilities, align goals with business outcomes, break down silos with unified platforms and cross-training, then deploy in phases with analytics and feedback loops. For cloud, it starts with visibility into the full footprint, then multi-layer access policies across hybrid and multi-cloud, converged control systems, and continuous monitoring. Start small, think big, review regularly.

## Who should watch

Security and network leads making the case for SASE or a platform consolidation, and engineers who want to understand the vocabulary their leadership is using. It's high-level and vendor-neutral in tone, with no product demo. If you need configuration detail, the related talks below go lower down the stack.

## Related Conf42 talks

- [Cloud Network Segmentation in pursuit of Zero Trust](https://www.conf42.com/Platform_Engineering_2023_Atif_Siddiqui_cloud_network_segmentation_in_pursuit_of_zero_trust) by Atif Siddiqui gets concrete about segmenting cloud networks.
- [Invisible Highways: Observability in the Evolution of AI-Era Networking Infrastructure](https://www.conf42.com/Observability_2025_Bhaskararao_Vakamullu_networking_era_highways) by Bhaskararao Vakamullu covers the visibility half of the argument.
- [Enhancing IoT Cybersecurity](https://www.conf42.com/Internet_of_Things_IoT_2024_Amod_Darshane_cybersecurity_network) by Amod Darshane applies segmentation and zero trust to devices.

[Watch Sharanya Prasad's talk](https://www.conf42.com/Machine_Learning_2025_Sharanya_Prasad_networking_security_digital)

[Watch the talk on YouTube](https://youtu.be/HmB-YwEjcsE).

## Watch the talk

[Converging Networking and Security: A Comprehensive Approach for a Resilient Digital Future](https://www.conf42.com/Machine_Learning_2025_Sharanya_Prasad_networking_security_digital) at Conf42 Machine Learning 2025.
