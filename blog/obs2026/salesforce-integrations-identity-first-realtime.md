# Identity first, speed second: real-time Salesforce integrations

Conf42 Blog, 2026-08-25. https://www.conf42.com/blog/obs2026/salesforce-integrations-identity-first-realtime

In short: Ravi Chandra Chinta (Temple View Capital) at Conf42 Observability 2026 on replacing nightly syncs with event-driven integrations, and fixing identity first.

When your sync is nightly, nobody trusts the data in the morning, and they keep a spreadsheet "just in case". At Conf42 Observability 2026, Ravi Chandra Chinta, Principal Salesforce Developer and Architect at Temple View Capital, a real-estate private mortgage lender, explains how his team rebuilt the integrations between Salesforce and Encompass, BSI and Shellpoint, and why the first fix had nothing to do with speed: it was the matching key.

It's a practitioner's case study from financial services. There's no live demo and few hard metrics, but the sequence of decisions (identity, then architecture, then observability, then people) is the useful part, and it carries over to any multi-system integration.

## What went wrong with email as a key?

Loans pass from sales and loan officers through draw and rehab, underwriting, processing and servicing, all working in Salesforce while Encompass (loan origination) and the servicing platforms BSI and Shellpoint hold their own copies. The integrations used email as the primary matching key. In production, Ravi says, that fails three ways: shared inboxes that stand for several borrowers or a household, borrowers who change their email mid-loan so the integration creates a duplicate, and loan officers typing placeholder addresses that silently corrupt matching.

None of this throws an error. It shows up a week later as wrong dashboards and a borrower with three loans at the same property address. The bigger cost was behavioural: teams kept shadow spreadsheets, cross-checked manually, and sometimes bypassed Salesforce for urgent loans, so it stopped being the system of record in practice.

## How did they fix it?

Their decision, in Ravi's words, was "identity first and then speed second". Matching moved to SSN for borrowers and brokers and EIN for business entities, held as tokenised or hashed values with tighter access to the raw ones, because compliance was non-negotiable. A borrower with three different emails across three loans now resolves to one person.

Then the architecture. The team kept point-to-point, two-way integrations (Salesforce to Encompass, to BSI, and to Shellpoint), each independently built and monitored, so a Shellpoint outage or rate limit doesn't cascade into the others. On top sit four pillars:

- **MuleSoft** with event-driven, API-led connectivity, replacing the Jitterbit cloud data loader's overnight queues.
- **Intelligent document processing** for PDFs, scanned draw requests and Excel budgets, feeding the same real-time pipeline, with fallback paths and human review for poor scans.
- **Salesforce Data Cloud** as a harmonisation layer before data lands in accounts, contacts, opportunities and loans.
- **Custom REST and SOAP APIs** to give legacy downstream systems consistent interfaces, working around their payload limits, authentication quirks and rate limits.

Integrations now fire when a loan status changes or a draw is approved, failures are caught, logged and retried without blocking unrelated flows, and monitoring was built in from day one so dashboards and alerts surface problems before a user opens a ticket.

## What got hard?

Ravi lists four frictions: reconciling years of historical duplicates, which took analysis plus manual review of ambiguous cases; conflict resolution for two-way sync, solved with explicit rules per object, per field and per direction; legacy SOAP constraints needing chunking, retries and an adapter layer; and people who had built routines around stale data (checking in the morning after the batch runs), which took communication, training and parallel verification.

## The takeaways

Fix identity before speed, or you will sync bad data faster. Redesign error handling rather than lifting batch retry logic into real time. Treat unstructured data as first-class. Point-to-point is legitimate in regulated multi-vendor setups. Trust moves slower than code, so budget for change management. Build observability first. As Ravi put it at Conf42 Observability 2026: "Speed without accuracy is noise. Accuracy without trust is shelfware."

## Who should watch

Integration and platform engineers on Salesforce or any CRM-to-core-system sync, and anyone whose "real-time" project is about to inherit a bad join key. If you want benchmarks of MuleSoft or Data Cloud, this isn't it: it reports outcomes (three systems integrated bi-directionally, five teams affected, nightly batches replaced) rather than latency figures.

Related Conf42 talks: [How to build your own green observability pipeline](https://www.conf42.com/Observability_2026_Diana_Todea_opensource_observability_sustainability) by Diana Todea of VictoriaMetrics at the same event, and [Your Backup Is Not Your Recovery](https://www.conf42.com/Chaos_Engineering_2026_Praveen_Kumar_Gopalakrishnan_backup_api_recovery) by Praveen Kumar Gopalakrishnan of Salesforce, on rebuilding trust in API-driven systems.

[Watch Ravi Chandra Chinta's talk](https://www.conf42.com/Observability_2026_Ravi_Chandra_Chinta_salesforce_integrations_realtime) from [Conf42 Observability 2026](https://www.conf42.com/obs2026).

[Watch the talk on YouTube](https://youtu.be/nHfTmcJoWcc).

## Watch the talk

[Building Real-Time Data Visibility Across Salesforce Integrations](https://www.conf42.com/Observability_2026_Ravi_Chandra_Chinta_salesforce_integrations_realtime) at Conf42 Observability 2026.
