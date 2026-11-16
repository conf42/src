# What the pandemic taught Zensar about automating partner supply chains

Conf42 Blog, 2025-10-12, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/supply-chain-automation-pandemic-lessons

In short: Kunal Dixit (Zensar Technologies) at Conf42 Prompt Engineering 2025 on order automation, direct shipping and remote field operations built during COVID.

"Plan A always worked" is a fine strategy until a lockdown closes the office, the warehouse and the customer site in the same week. At Conf42 Prompt Engineering 2025, Kunal Dixit, a delivery manager at Zensar Technologies, told the story of how partner and field automation kept a supply chain running through COVID, and why the remote-first changes outlived the crisis.

This is a case-study talk from the delivery side, light on code and heavy on what was changed, in what order, and what it bought.

## What broke first

Kunal's list of pandemic failure points is a useful audit for any operations team. Paper-based order processing, email coordination and spreadsheet tracking all became bottlenecks the moment people worked remotely. Field operations, equipment installation and partner training needed physical presence that lockdowns made impossible. Inventory visibility was limited, so information arrived late and decisions arrived later. And a centralised, inflexible network meant one failing node could take the environment down. In his words, there was no plan B because plan A always worked.

## Automate the order, end to end

The first fix was splitting order handling into three automated stages. Capture: partners submit orders through API integration, removing manual data entry. Processing: a new middleware layer validates the order, checks inventory and routing options, without a human in the loop. Fulfilment: shipping is triggered, systems are updated on delivery status, and notifications go out in real time. He described orders that used to take days now taking hours, with remote teams keeping full operational capability.

## Ship direct, track everything

Next came distribution. Rather than routing equipment through a central warehouse, Zensar shipped directly to partner locations, using GPS and IoT sensors for real-time shipment visibility and automated notifications at every milestone (dispatch, transit, delivery). Exceptions could be handled proactively instead of discovered by an angry phone call. Internal teams stopped babysitting shipments and went back to strategic work.

## Field work without the field

The third piece is the one that stuck: technicians configured equipment remotely using automated configuration templates, digital audits kept compliance documentation paperless, and a virtual training platform gave partners on-demand modules with automated assessment of knowledge gaps. Expensive site visits disappeared from many workflows, and Kunal says the shift to remote operations became permanent, with cost savings lasting beyond the crisis.

## Resilience is a design choice

The architectural lesson is explicit. Zensar's resilient design framework rests on modular, component-based architecture that can be reconfigured or replaced quickly, automated health monitoring, simulation testing of crisis scenarios, and comprehensive documentation so knowledge survives staffing disruption. Kunal cited a chart showing organisations with mature automation recovering 15 times faster than traditional peers, and real-time inventory visibility cutting stockouts by 60%. His takeaway: recovery speed correlates directly with digital maturity, and that maturity came from deliberate choices, not luck.

His practical sequence: start with the most painful high-friction process, make the architecture modular, integrate the partner ecosystem, invest in training, then test and iterate regularly. The next disruption, he closes, is inevitable; the question is whether you're ready.

## Who should watch

Delivery and operations leaders in hardware or partner-driven businesses, and architects who need a concrete before-and-after story to justify modularity and automated monitoring. Engineers looking for implementation detail on the middleware itself won't find it here.

## Related Conf42 talks

- [Power BI & Prompt Engineering: Driving $30M in Supply Chain Savings at Kellogg's](https://www.conf42.com/Prompt_Engineering_2025_Victor_Gabriel_supplychain_savings_bi) by Victor Gabriel at Conf42 Prompt Engineering 2025.
- [Leveraging AI for Resilient Supply Chains: Navigating Complexity and Disruptions with DevSecOps](https://www.conf42.com/DevSecOps_2024_Madhusudan_S_Vadigicherla_ai_supply_chains) by Madhusudan S Vadigicherla at Conf42 DevSecOps 2024.
- [SRE for Supply Chain: Building Reliable Human-AI Warehouse Operations at Scale](https://www.conf42.com/DevOps_2026_Vishnu_Prasad_supplychain_reliability_warehouses) by Vishnu Prasad at Conf42 DevOps 2026.

[Watch Kunal Dixit's talk](https://www.conf42.com/Prompt_Engineering_2025_Kunal_Dixit_supplychain_automation_resilience) from [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/GW0xKU6NUwk).

## Watch the talk

[Supply Chain Resilience with Partner & Field Automation: Post-COVID Lessons](https://www.conf42.com/Prompt_Engineering_2025_Kunal_Dixit_supplychain_automation_resilience) at Conf42 Prompt Engineering 2025.
