# Small businesses run cloud-native stacks without a security team

Conf42 Blog, 2026-04-15. https://www.conf42.com/blog/cloud2026/security-in-your-pocket-for-small-business

In short: Vaishali Mahavratayajula of Wells Fargo at Conf42 Cloud Native 2026 on Security in Your Pocket, a six-layer AI risk framework for small online businesses.

A one-person online shop today runs a Shopify store, a payment processor, a few SaaS tools, an Instagram DM bot and probably an AI assistant or two. That's a distributed cloud-native estate, and its owner usually doesn't know it. At Conf42 Cloud Native 2026, [Vaishali Mahavratayajula](https://www.conf42.com/Cloud_Native_2026_Vaishali_Mahavratayajula_distributed_systems_performance), AI Security Architect at Wells Fargo, presented Security in Your Pocket, a mobile-first, AI-driven risk assessment framework aimed at exactly those owners.

Honest scope: she introduces it as her product idea. The abstract says it is implemented through the securemystore.ai platform for SKRM Technologies and evaluated in simulated small-business cloud environments, so treat it as a framework with early results rather than a field report.

## Too small for enterprise tools, too big for consumer ones

Her framing is a gap. Enterprise security platforms assume dedicated security teams, DevSecOps pipelines and clear ownership models. Consumer tools protect a person, not a business. A small owner who is also the marketer, the accountant and the support desk fits neither, and often can't say what a vulnerability is, what it would cost the business, or how to fix it.

She names four systemic gaps the framework targets: no visibility into cloud assets (forgotten APIs, unmonitored buckets, shadow AI from tools like ChatGPT and Perplexity), no clear security ownership between owner, web developer and anyone else, uncontrolled third-party and AI tool exposure through plugins and integrations, and security tools that don't match how these businesses actually work.

## Six layers, from discovery to attestation

The architecture runs in six layers:

1. **Asset discovery.** You can't protect what you can't see. Continuously find websites, APIs, SaaS tools, store pages and small AI apps, and track how the footprint changes as integrations get added.
2. **Vulnerability detection.** Known vulnerability patterns, misconfigurations, weak authentication, exposed services and overly permissive IAM roles.
3. **Continuous monitoring.** A one-time scan is a snapshot. Plugins update, permissions drift and new endpoints appear, so the framework baselines, detects deviations and notifies the owner in plain language.
4. **AI correlation.** This is the most interesting layer. A publicly reachable API might be a moderate risk on its own, and so might an over-scoped token. If that token can reach that API, the combination is much more severe than either signal suggests.
5. **Business-aligned risk scoring.** Instead of CVSS numbers, scores reflect revenue exposure, customer trust, regulatory obligations and downtime. For an owner, the useful question is how long the shop would be offline.
6. **Continuous attestation.** Automated evidence that the posture holds, so auditing is built in rather than done on demand.

## Plain language is a security control

A theme across the talk is translation. She wants findings free of CVE and CVSS jargon, phrased around one question: why does this risk matter to me? She also argues it reduces friction between developers and security people, who otherwise argue about whether a finding applies at all. Humans stay in the loop for risk ownership; the AI does the noisy work of scanning, correlating and translating.

## Who should watch

Builders of security products for SMBs, and engineers who look after a friend's or family member's online business and suspect its attack surface is bigger than anyone thinks. If you want implementation detail or detection rates, the talk stays at framework level.

## Related Conf42 talks

- [Beyond the Perimeter: Next-Generation Cloud Security Strategies in an Era of Evolving Threats](https://www.conf42.com/DevOps_2025_Sandeep_Batchu_cloud_security_threats) by Sandeep Batchu at Conf42 DevOps 2025.
- [Hacking Demos, Dirty Secrets, Dangerous Lies, and Asset Intelligence](https://www.conf42.com/DevSecOps_2023_Brian_Contos_hacking_demos_secrets_asset_intelligence) by Brian Contos at Conf42 DevSecOps 2023.
- [Threat Modeling in DevOps: A Practical Guide for Developers](https://www.conf42.com/DevOps_2025_Krishna_Chaitanya_Rudraraju_threat_modeling_developers) by Krishna Chaitanya Rudraraju at Conf42 DevOps 2025.

[Watch Vaishali Mahavratayajula's talk](https://www.conf42.com/Cloud_Native_2026_Vaishali_Mahavratayajula_distributed_systems_performance) or the [YouTube recording](https://youtu.be/J69pPcsK_7E).

## Watch the talk

[Security in Your Pocket: AI Risk Assessment for Cloud-Native SMBs](https://www.conf42.com/Cloud_Native_2026_Vaishali_Mahavratayajula_distributed_systems_performance) at Conf42 Cloud Native 2026.
