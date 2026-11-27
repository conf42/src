# What a card swipe asks of a payment platform in 200 milliseconds

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/card-payments-in-200-milliseconds

In short: Tapan Vijay (Meta) at Conf42 Platform Engineering 2025 on the latency, fraud, settlement and key-management design behind planet-scale card processing.

Buying a coffee with a card gives a dozen systems roughly 100 to 200 milliseconds to agree with each other. At Conf42 Platform Engineering 2025, Tapan Vijay, Head of Payment Engine and Gateway at Meta, took that single swipe apart and showed what a payment platform has to get right inside that window: routing across gateways, a chain of fraud checks, issuer approval and a consistent answer for every party involved.

## A web of parties, each with its own fraud check

The complexity starts with the cast. Cardholder, merchant, acquirer, network, gateway and issuer all sit in the path of one authorisation, across multiple data centres, geographies and dozens of regulatory frameworks. Each party wants to reduce its own liability, so each runs its own fraud checks. Tapan puts numbers on the stakes: in the region he describes, around 150 billion card transactions a year, holiday peaks around 65,000 transactions per second, and roughly $31,000 lost per second of downtime.

## Eventual consistency is not an option at checkout

Most of the architecture advice is classic distributed systems, sharpened by money. Scale horizontally rather than buying bigger machines. Isolate critical components in a service-oriented design so a failure stays local and upgrades don't take the whole system down. Distribute geographically for disasters, but keep transactions from bouncing between continents and blowing the latency budget.

The point he stresses most is consistency. Plenty of systems tolerate eventual consistency; a payment has to complete or not happen at all, within a time bound, with no ambiguity. The nightmare is the bank saying approved while the gateway says failed.

To hit the latency target, authorisation systems use connection pooling and persistent connections to skip TCP handshakes, compact protocols instead of XML, adaptive load balancing that watches server health and queue depth, and circuit breakers. Static reference data is cached, and distributed caches need careful invalidation, because overly aggressive invalidation causes a thundering herd.

## Fraud detection gets 10 to 20 milliseconds

Within the end-to-end budget, fraud scoring gets roughly 10 to 20 milliseconds to analyse hundreds of parameters: device fingerprints, behavioural patterns, velocity checks, geographic anomalies. Models have to be deployed in every region rather than called centrally, which drags in versioning, A/B testing and monitoring problems, plus hot-swapping models without disrupting traffic. New fraud patterns should be expressible as rules in a domain-specific language, so detection can change without a code deploy.

## Settlement, keys and reconciliation run on a different clock

Authorisation is milliseconds; settlement usually runs daily, although real-time payment rails are pushing it toward immediate transfer. That calls for careful state management (authorised, captured, batched, submitted, settled) consistent across every partner. Cross-border payments add FX risk, rate locking and liquidity relationships. Reconciliation at this volume moves from batch to continuous.

On security Tapan covers defence in depth, hardware security modules, zero trust and tokenisation, plus hierarchical key management: a master key in the HSM encrypts data keys stored with the data, so rotation touches only key-encryption keys instead of re-encrypting everything. He also calls out insider controls, because the platform must stop its own staff from pushing through an unauthorised transaction.

## Who should watch

Engineers building anything where correctness and latency both matter, payments or not. It's a dense survey rather than a case study of Meta's own systems, and the closing look at real-time rails, open banking APIs and stablecoins is a good map of what's coming.

## Related Conf42 talks

- [Card Payments Lifecycle Explained](https://www.conf42.com/Machine_Learning_2024_Michael_A_Johnson_card_payments_lifecycle) by Michael A Johnson (Meta), the business flow behind the same swipe.
- [From Milliseconds to Microseconds: How Quantum Computing Could Transform Real-Time Payments](https://www.conf42.com/Quantum_Computing_2025_Nikhil_Kassetty_quantum_payments_latency) by Nikhil Kassetty (Intuit), a speculative look at the latency budget.
- [Feature Flags as a Migration Engine: De-risking Domain-Driven Decomposition of Monolithic Payment Platforms](https://www.conf42.com/Feature_Flags_2026_Jaya_Chand_Bandi_migration_payment_platforms) by Jaya Chand Bandi, on changing a payment platform without stopping it.

[Watch Tapan Vijay's talk](https://www.conf42.com/Platform_Engineering_2025_Tapan_Vijay_card_planet_resilience)

[Watch the talk on YouTube](https://youtu.be/vIxzY2LSj6Q).

## Watch the talk

[Building Planet-Scale Payment Platforms: Engineering Resilience in Global Card Processing Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Tapan_Vijay_card_planet_resilience) at Conf42 Platform Engineering 2025.
