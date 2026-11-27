# Your supply chain AI is only as good as the ERP beneath it

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/erp-as-composable-backbone-for-supply-chain-ai

In short: Vinod Nagarahalli (Illumina) at Conf42 Platform Engineering 2025 on rebuilding ERP as a composable, API-first platform for AI-driven supply chains.

Most supply chain AI projects fail before the model is trained, because the data lives in an ERP built for transactions, not intelligence. At Conf42 Platform Engineering 2025, Vinod Nagarahalli, Director of IT at Illumina, made the case for treating ERP as a platform: modular services, API-first interfaces and event-driven flows, so forecasting, predictive maintenance and contract intelligence have a clean, connected foundation to run on.

## Legacy ERP: highways built for cars, asked to carry high-speed trains

Vinod's diagnosis has three parts. Years of customisation and bolt-ons leave planning, logistics, asset management, HR, finance and sourcing fragmented, so data is siloed and decisions lag. The data that does exist is often incomplete and inconsistent, which starves AI of exactly the clean, integrated input it needs. And the architecture is rigid, so every integration with a cloud service, ML framework or digital twin turns into its own expensive project. His image: roads built for cars, now expected to carry high-speed trains.

## Platform engineering applied to the back office

The fix is to apply platform engineering principles to ERP itself. Break functionality into microservices (finance, procurement, planning, logistics) that can scale and change independently. Make it API-first, with versioned, documented interfaces that partners, internal systems and AI services can call. Move from batch to event-driven processing, so inventory updates, demand signals and disruptions are handled as they happen.

On top of that he argues for a unified architecture with a common data model and shared governance. His example of why it matters: maintenance scheduling that automatically accounts for production plans, inventory and transport constraints, because those systems finally share data.

Integration is the other half. Vinod sketches a real-world shape: SAP S/4HANA as the core, with Ariba, extended warehouse management, transportation management, integrated business planning and financial supply chain modules around it, plus Teamcenter for product lifecycle, Camstar for manufacturing execution and LabVantage for lab data. The goal is to turn the ERP from a system of record into what he calls a system of intelligence.

## Three use cases on the same foundation

- **Predictive maintenance.** IoT sensors stream temperature, vibration and pressure; the ERP adds context; ML spots early signs of wear so repairs happen in planned downtime with parts ordered ahead.
- **Demand forecasting.** Models combine sales history, market trends, sentiment, weather and IoT data, keep learning as data arrives, and run what-if scenarios for demand surges or supply disruption.
- **Contract intelligence.** NLP extracts payment terms, delivery obligations and compliance clauses; ML flags risky terms. Wired into the ERP, a supplier missing a critical delivery can trigger a production-plan change or alternative sourcing automatically.

## Governance and people

He closes with the less glamorous parts: data lineage and quality, model lifecycle management with versioning and retraining, privacy techniques such as differential privacy and federated learning, and defences against data poisoning and model extraction. Then people: redesigned processes, upskilling and leaders who can run hybrid human and automated teams. His implementation advice is to start with clean governed data and a few high-impact domains rather than boiling the ocean.

## Who should watch

Engineers and IT leaders in manufacturing or life sciences who are being asked for AI on top of an ERP that barely talks to itself. It's a strategy-level talk with a vendor-heavy reference architecture; there's no code, but the integration map is useful.

## Related Conf42 talks

- [Optimizing Test Orchestration in ERP Systems with Golang, AI, and Cloud-Native Architectures](https://www.conf42.com/Golang_2025_Sridhar_Dachepelly_testing_erp_orchestration) by Sridhar Dachepelly (Dell Technologies), on testing the ERP you're modernising.
- [Leveraging AI for Resilient Supply Chains: Navigating Complexity and Disruptions with DevSecOps](https://www.conf42.com/DevSecOps_2024_Madhusudan_S_Vadigicherla_ai_supply_chains) by Madhusudan S Vadigicherla (Integra LifeSciences).
- [Golang-Powered Retail Distribution: Transforming Supply Chains Through Cloud-Native Innovation](https://www.conf42.com/Golang_2025_Srinivas_Ankam_retail_distribution_supply) by Srinivas Ankam (Cloud5 Solutions).

[Watch Vinod Nagarahalli's talk](https://www.conf42.com/Platform_Engineering_2025_Vinod_Nagarahalli_chains_backbone_supply)

[Watch the talk on YouTube](https://youtu.be/3YKxzKke4YY).

## Watch the talk

[Modern ERP as the Platform Backbone for Scalable, AI-Driven Supply Chains](https://www.conf42.com/Platform_Engineering_2025_Vinod_Nagarahalli_chains_backbone_supply) at Conf42 Platform Engineering 2025.
