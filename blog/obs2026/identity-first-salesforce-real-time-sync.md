# Fix identity before speed, or you just sync bad data faster

Conf42 Blog, 2026-08-25. https://www.conf42.com/blog/obs2026/identity-first-salesforce-real-time-sync

In short: Ravichandra Chinta at Conf42 Observability 2026 on moving Salesforce integrations from email matching and nightly batches to SSN/EIN identity and events.

Email addresses make terrible primary keys, and a mortgage lender's CRM will prove it to you one duplicate borrower at a time. At Conf42 Observability 2026, Ravichandra Chinta, a principal Salesforce developer and architect, tells the story of rebuilding the integrations between Salesforce and three downstream lending systems, and his first rule is the title of this post: fix identity first, then make it fast.

The session in the sheet is titled "Closing the Semantic Gap with Feedback-Driven Ontology Learning", but the session as recorded is about real-time data visibility in a financial services integration layer: identity resolution, event-driven sync, document extraction and the human work of getting people to trust the system again.

## The bug that never threw an error

The setup will be familiar to anyone who has owned a CRM integration. Salesforce sat in the middle of the loan lifecycle (sales, draw and rehab, underwriting, servicing, valuations), with Encompass as the loan origination system and BSI and Shellpoint as servicing channels. The connections were periodic jobs, so Salesforce always reflected yesterday.

The worse problem was matching on email. Ravichandra lists three ways it broke in production: shared inboxes where one address covers a household, borrowers who change their email mid-loan, and loan officers who type their own or a placeholder address during origination. None of these fail loudly. They show up a week later as wrong dashboards and a borrower with three loans on the same property address.

The behavioural cost was bigger than the data cost. Teams kept shadow spreadsheets and checked the other system "just to be make sure", and some bypassed Salesforce entirely for urgent loans. That, he argues, was the signal of a foundation problem rather than a performance problem.

## Durable identifiers, hashed

The fix was to match borrowers and brokers on SSN and business entities on EIN, values that are unique by definition. They were not matched in plain text: matching runs on a tokenized or hashed representation, with tighter access control on the raw values. Once that landed, a borrower with three different emails across three loans resolved to one person, and a whole category of duplicates disappeared.

The new records were the easy part. Reconciling years of historical duplicates took matching plus manual review of the ambiguous cases, and he tells you to budget time for it.

## Point-to-point, on purpose

The architecture he landed on runs against the usual hub-and-spoke advice. Each pathway (Salesforce to Encompass, to BSI, to Shellpoint) is its own two-way integration, built and monitored independently, so a Shellpoint outage or rate limit doesn't cascade into the other flows. Underneath sit four pillars: MuleSoft replacing a Jitterbit cloud data loader with event-driven, API-led connectivity; intelligent document processing for the PDFs, scans and Excel draw requests; Salesforce Data Cloud as a harmonisation zone before records land in Salesforce objects; and custom REST and SOAP APIs to bridge legacy interfaces.

The nightly batch was replaced by triggers on real changes: a loan status flips, a draw is approved, a servicing update posts, and the integration fires. One bad record is caught, logged and retried without blocking the good ones. Two-way sync forced explicit conflict rules per object, per field and per direction, instead of ad hoc calls about which system updates first.

## Where observability comes in

This is the bit that earns the talk its slot at an observability conference. Monitoring was built in from day one, with per-pathway health checks and alerts meant to fire before a business user files a ticket. As he puts it, "You can't claim real-time if you can't see what's flowing, what's failing, and what's lagging." His closing line is the one to keep: "Speed without accuracy is noise. Accuracy without trust is shelfware."

## Who should watch

Engineers and architects who own CRM or ERP integrations, especially in regulated, multi-vendor shops where a single enterprise bus isn't realistic. It's a practitioner war story rather than a deep technical walkthrough, and the six principles near the end make a good checklist for your own migration. If you came for ontology learning and semantic layers, this recording doesn't cover them.

## Related Conf42 talks

- [Cloud-Native MDM: Kubernetes Orchestration for Enterprise Data Quality at Scale](https://www.conf42.com/Kube_Native_2025_Rahul_Ameria_mdm_quality_orchestration) by Rahul Ameria at Conf42 Kube Native 2025.
- [API-Led Healthcare Transformation: Enhancing Interoperability, Diagnostics & Personalized Medicine with MuleSoft](https://www.conf42.com/Cloud_Native_2025_Venugopal_Reddy_Depa_api_healthcare_interoperability) by Venugopal Reddy Depa at Conf42 Cloud Native 2025.
- [Transforming Loan Applications with a Mobile-First Borrower Portal](https://www.conf42.com/Python_2025_Ravi_Chandra_Chinta_loan_mobile_portal) by Ravi Chandra Chinta at Conf42 Python 2025.

[Watch Ravichandra Chinta's talk](https://www.conf42.com/Observability_2026_Ravi_Chandra_llms_analytics_semanticlayer) from [Conf42 Observability 2026](https://www.conf42.com/obs2026).

[Watch the talk on YouTube](https://youtu.be/nHfTmcJoWcc).

## Watch the talk

[Closing the Semantic Gap with Feedback-Driven Ontology Learning](https://www.conf42.com/Observability_2026_Ravi_Chandra_llms_analytics_semanticlayer) at Conf42 Observability 2026.
