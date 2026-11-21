# When the legacy system has no API, an RPA bot can click for you

Conf42 Blog, 2025-08-08, updated 2026-11-09. https://www.conf42.com/blog/platform2025/rpa-salesforce-legacy-integration

In short: Uday Bheemarpu of Clean Earth at Conf42 Platform Engineering 2025 on pairing RPA with Salesforce to automate workflows across systems that lack APIs.

Every enterprise has at least one system that only speaks through a screen. At Conf42 Platform Engineering 2025, Uday Bheemarpu, Information Technology Lead at Clean Earth, explained how robotic process automation fills the gaps that Salesforce's own automation tools cannot reach, and where the combination pays off: order entry into SAP, invoice processing and compliance checks against licensing websites.

His framing is fair to Salesforce. The limits, he says, reflect how enterprises are built: not every system has a modern API, some processes still run on paper or offline, and some need a human to click through an old interface.

## What native tools cover, and where they stop

Uday walks through the Salesforce toolkit first: Flows as a visual workflow builder, Apex for custom logic, REST and SOAP APIs, the Bulk API for large data volumes, and Platform Events for event-driven integration. Powerful, but they depend on what the other side offers.

The gaps cluster in four places: legacy systems with no API or a terminal interface, file-based processes on Excel, CSV and scanned PDFs, external web portals where someone copies data by hand, and cross-system orchestration where each system has different integration capabilities. Middleware can help, but adds cost and complexity of its own.

## RPA works at the UI layer

RPA's trick is that it operates where a human would: in browsers, desktop apps, terminal emulators and even Citrix sessions, only faster and without fatigue. Combined with OCR and natural language processing it can pull data from documents, emails and images. Every bot action is logged, which helps audits and troubleshooting, and bots scale up and down with workload.

## Three scenarios

- **Order processing.** A bot watches Salesforce for new orders, logs into SAP, navigates the screens, types in the order, captures the confirmation number and writes it back to Salesforce. Exceptions go to a human and are reported in Salesforce.
- **Invoice processing.** OCR reads scanned invoices, the bot validates them against purchase orders in Salesforce, enters approved ones into the accounting system, and opens Salesforce cases for discrepancies.
- **Compliance data collection.** On a schedule, bots visit licensing websites, look up the providers listed in Salesforce, capture license status and expiry dates, and update the records.

## Architecture and patterns

The technical design has four pillars: monitoring and governance (dashboards, alerting, SLA management), integration patterns, a security framework (least privilege, credential vaulting, auditability) and a proper development environment with version control and dev, test and prod pipelines.

The integration patterns run both ways. Bot-initiated: bots call Salesforce REST APIs, publish Platform Events, or drive the Salesforce UI when needed. Salesforce-initiated: outbound messages notify an RPA orchestrator, RPA listeners consume Platform Events, or Apex callouts invoke bot endpoints. Which one you pick depends on the system of record, volume, latency needs and operational controls.

## The maintenance tax

His best-practice list is where the practical wisdom sits. Start with process discovery: document the manual steps, find the systems without APIs and calculate ROI to choose use cases. Start small. Design for resilience with error handling, fallbacks for downtime and planned maintenance windows. Keep humans in the loop for exceptions. And the one that bites everyone: when the target website or screen changes, the bot has to be updated too, or its clicks land in the wrong place. He cites typical results of an 80% reduction in processing time, a 95% improvement in error rates and three times the volume handled.

## Who should watch

Salesforce admins and architects with a stubborn legacy system on the other end, and platform engineers deciding whether to build an API wrapper or let a bot click. It is an overview with scenarios rather than a build walkthrough.

## Related Conf42 talks

- [Pradeep Reddy Guttha on the Salesforce Platform and Agentforce as a cloud-native app](https://www.conf42.com/Cloud_Native_2025_Pradeep_Reddy_Guttha_salesforce_ecosystem_development) at Conf42 Cloud Native 2025.
- [Vijay Kumar Kola on AI-powered testing to prevent SAP and Salesforce incidents](https://www.conf42.com/Incident_Management_2025_Vijay_Kumar_Kola_sap_salesforce_testing) at Conf42 Incident Management 2025.
- [Jaymin Sutarwala on a feature-flag rollout for a legacy CRM migration to Salesforce](https://www.conf42.com/Feature_Flags_2026_Jaymin_Sutarwala_crm_migration_salesforce) at Conf42 Feature Flags 2026.

[Watch Uday Bheemarpu's talk](https://www.conf42.com/Platform_Engineering_2025_Uday_Bheemarpu_salesforce_rpa_ecosystems), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/8j58lEQoRLM).

## Watch the talk

[Bridging Legacy and Modern Systems: RPA-Driven Automation in Salesforce Ecosystems](https://www.conf42.com/Platform_Engineering_2025_Uday_Bheemarpu_salesforce_rpa_ecosystems) at Conf42 Platform Engineering 2025.
