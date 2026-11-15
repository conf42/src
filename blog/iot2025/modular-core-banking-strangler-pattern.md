# Strangle the banking mainframe one domain at a time

Conf42 Blog, 2025-11-27, updated 2026-11-09. https://www.conf42.com/blog/iot2025/modular-core-banking-strangler-pattern

In short: Swetha Lakkaraju at Conf42 IoT 2025 on modernizing legacy core banking with the strangler pattern, domain-driven design, API-first and microservices.

Most banks are not short of ideas; they are short of budget left over after keeping the core running. At Conf42 Internet of Things (IoT) 2025, independent researcher Swetha Lakkaraju, who has spent over 18 years in mainframe core banking with Systematics and Vision Plus, argued that modular core architectures are how incumbents get their release cycles from months back down to weeks or days.

A heads-up on scope: despite the event, this one has nothing to do with sensors or devices. It is a strategy talk about core banking modernization, aimed at the people who have to fund and sequence it.

## Where innovation goes to die

Swetha opens with the money. In her account a large share of bank IT budgets, sometimes 60 to 80%, goes to simply keeping legacy systems alive, leaving little for anything new. Every change drags through long testing cycles and carries high risk, so traditional banks ship in months or years while fintechs launch something every few weeks. Her point is that the legacy core stops being a technical burden and becomes a strategic one.

The underlying cause is coupling. Core banking, payments, customer accounts and card systems are so interdependent that touching one means retesting all of them. Breaking the monolith into modules that each own a business capability lets teams update one piece without risking the rest, and keeps a failure in one area from taking down the whole core.

She grounds the case in her research comparing institutions across several countries over multiple years: speed, cost efficiency, innovation output, digital adoption and customer experience. The pattern she reports is that banks that went modular outperformed those that did not.

## Four pillars, and the order matters

The strategy section is the most reusable part of the talk:

- **Strangler pattern.** Replace legacy components in small increments while the business keeps running, instead of betting the bank on a big bang migration.
- **Domain-driven design.** Make the technical boundaries match the business ones, so teams own and evolve their domains independently.
- **API-first.** APIs become the standard layer between internal systems, partners and fintechs.
- **Microservices.** Fine-grained scaling, flexible deployment and better fault isolation.

Operationally, she ties decoupling to fewer cascading failures, fewer integration defects thanks to explicit API contracts, and smaller audit scopes that make compliance quicker. Less firefighting, more building.

## The roadmap starts somewhere boring

Her modernization roadmap has four stages. Assess the current architecture, name the pain points and get leadership aligned early. Validate on a small, non-critical domain to build skills and test assumptions. Then scale into the core domains such as lending, payments and customer systems, with governance, automated testing and refined deployment. Finally, expand into an ecosystem of partner integrations, where APIs let a bank add things like digital KYC or loyalty programs without modifying the core.

She is candid about what gets in the way: people resisting change, regulators who need early engagement and detailed documentation, legacy code with little documentation and tangled logic, and budgets. Her answer to the budget problem is phased execution that reinvests the savings from each step into the next.

## Who should watch

Architects and engineering leaders in banks or insurers sitting on a mainframe core, and anyone writing the business case for a modernization program. If you are here for IoT, skip to the next talk; if you have ever tried to change one field on a COBOL copybook, stay.

## Related talks from Conf42

- [Srinivas Allam on Go-powered banking and modernizing iSeries systems](https://www.conf42.com/Golang_2025_Srinivas_Allam_banking_modernization_fintech) at Conf42 Golang 2025.
- [Rajkumar Chindanuru on strategies for modernizing legacy applications](https://www.conf42.com/Golang_2025_Rajkumar_Chindanuru_legacy_modernization_strategies) at Conf42 Golang 2025.
- [Dmitry Vinnik on fixing broken windows in legacy systems](https://www.conf42.com/Site_Reliability_Engineering_2021_Dmitry_Vinnik_broken_windows_legacy_systems__poor_quality_gaps) at Conf42 SRE 2021.

[Watch Swetha Lakkaraju's talk](https://www.conf42.com/Internet_of_Things_IoT_2025_Swetha_Lakkaraju_banking_modular_modernization) from [Conf42 IoT 2025](https://www.conf42.com/iot2025).

[Watch the talk on YouTube](https://youtu.be/8VP8lZ5pX4I).

## Watch the talk

[Decoupling Legacy Banking: Modular Core Strategies for Speed, Scale, and Innovation](https://www.conf42.com/Internet_of_Things_IoT_2025_Swetha_Lakkaraju_banking_modular_modernization) at Conf42 Internet of Things (IoT) 2025.
