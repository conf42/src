# When a hurricane hits, the claims portal is the incident

Conf42 Blog, 2025-10-02, updated 2026-11-09. https://www.conf42.com/blog/im2025/insurance-incident-response-ai-edge-serverless

In short: Chandra Prakash Kathroju (Citizens Property Insurance) at Conf42 Incident Management 2025 on AI, edge computing and serverless for insurance incident response.

For an insurer, the worst day for the systems is the worst day for the customers: a hurricane makes landfall, thousands of policyholders file claims at once, and the portal falls over. At Conf42 Incident Management 2025, Chandra Prakash Kathroju, Software Engineer at Citizens Property Insurance Corporation, gave a short overview of how AI, edge computing and serverless architecture change incident response in insurance, where the incident is often a physical event and the system's job is to keep up with it.

It is a compact, high-level talk that maps technologies onto insurance problems rather than walking through one implementation.

## Four ways insurers fall behind

Kathroju starts with the pain points. Incidents can go unnoticed for hours or days, delaying recovery and adding cost. Claims processing is manual, so adjusters are overloaded and policyholders wait in backlogs. Without real-time data, insurers react to losses instead of preventing them. And during disasters, systems built for normal demand collapse under the surge. All four hit customer trust and operating cost directly.

## Process at the source, scale in the cloud

The three technologies each cover a different gap.

**AI** is already in underwriting (IoT sensor data, driving behaviour and property data for risk assessment), claims (chatbots gather information, models triage severity, human adjusters handle exceptions) and fraud detection, catching patterns before payout. For incidents it adds real-time monitoring of underwriting and claims data, early detection of unusual patterns and alerts routed to the right team with a severity level and suggested action. It also supports root cause analysis, pulling data from several systems to tell weather damage from equipment failure from human error.

**Edge computing** processes data where it is created. A flood sensor in a home can raise an alert immediately even if the connection to the cloud is slow; accident data from a car's telematics can be analysed locally so the insurer can act right away. Less latency, less bandwidth, faster response.

**Serverless** he compares to electricity: you use what you need and don't worry about the power plant. For insurers that means claim portals that scale with a disaster surge instead of crashing, and new tools like claim apps shipped in days.

The layered model joins them: sensors capture data, edge processing gives instant local insight, cloud analytics finds patterns across sources, and the result feeds decisions from claim approvals to fraud prevention.

## Disaster mode and the compliance line

For large disruptions he lists the standard toolkit: autoscaling, dynamic allocation that moves workloads across regions, failover with backups, and load balancing to smooth spikes. Two insurance-specific points follow. Blockchain fits reinsurance, where smart contracts can automate settlements and an immutable trail builds trust between insurers and reinsurers. And hybrid cloud is how insurers square scale with regulation: sensitive regulated data stays in private or on-premises systems, while analytics and other elastic workloads run in public cloud, with logging, monitoring and automated governance keeping GDPR and HIPAA obligations covered.

The roadmap is assess, design, pilot in a small controlled environment, then scale and optimise.

## Who should watch

Engineers and architects at insurers, or anyone building systems whose load follows the weather. It is an overview, not a deep technical session, so treat it as a map of where each technology fits in an insurance incident.

## Related Conf42 talks

- [Transforming Insurance Through AI](https://www.conf42.com/Cloud_Native_2025_Bhaskara_Beeraka_insurance_innovation_insights) by Bhaskara Beeraka covers the AI applications in more depth.
- [From Manual to Magical: How Rule-Based AI is Transforming Dental Insurance Claims](https://www.conf42.com/Cloud_Native_2025_Pravesh_Nikhare_insurance_rules_processing) by Pravesh Nikhare zooms in on claims automation.
- [Leveraging AI and ML with JavaScript: Transforming Claims Processing](https://www.conf42.com/JavaScript_2024_Praveen_Kumar_50_ai_claimsprocessing) by Praveen Kumar looks at claims in life and annuities.

[Watch Chandra Prakash Kathroju's talk](https://www.conf42.com/Incident_Management_2025_Chandra_Prakash_Kathroju_edge_serverless_insurance)

[Watch the talk on YouTube](https://youtu.be/GnMB8RUR640).

## Watch the talk

[AI, Edge & Serverless: Reshaping Insurance Incident Response in the Cloud Era](https://www.conf42.com/Incident_Management_2025_Chandra_Prakash_Kathroju_edge_serverless_insurance) at Conf42 Incident Management 2025.
