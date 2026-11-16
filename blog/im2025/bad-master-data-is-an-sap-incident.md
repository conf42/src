# Bad master data is an SAP incident waiting for a trigger

Conf42 Blog, 2025-09-29, updated 2026-11-09. https://www.conf42.com/blog/im2025/bad-master-data-is-an-sap-incident

In short: Gobinath Kasimayan (Deloitte Consulting) at Conf42 Incident Management 2025 on AI master data governance in SAP that flags data incidents before they cascade.

A duplicate vendor record looks harmless until the payment run fails, and by then the incident is already in finance. At Conf42 Incident Management 2025, Gobinath Kasimayan, Specialist Master at Deloitte Consulting and a data architect focused on energy and oil and gas, walked through how AI-driven master data governance in SAP can catch that class of problem early, raising incidents from data patterns instead of waiting for a downstream process to break.

## Master data is the DNA, and it replicates

Gobinath's starting point is that customer, supplier, material, asset and employee master data is the bloodline of an SAP estate. When it is inaccurate or stale, it hits operational processes like supply chain, order to cash and finance, and it does not stop there: it replicates into every downstream system that consumes it. Fixing it today usually means someone files an incident, a data steward corrects the record, and the correction is replicated out again.

His asset management example makes the cascade concrete. Enterprise asset management data feeds a performance management system; if the source data is wrong, the performance rules calculate the wrong results, and preventive maintenance in an oil and gas operation goes off course. Globally managed objects such as customer master make it worse, because one bad record spreads to every location at once.

## Why rule-based MDM falls behind

Traditional master data management relies on static validation rules, central manual governance and batch processing. That copes when volume is low. With globalisation and multi-system estates, the rules do not adapt to consolidation or new product lines, and batch jobs find problems after they have landed. He cites research putting the cost of poor data at around $13 million a year for an average enterprise, with 41% of data professionals' time lost to it.

Today's workaround, as he describes it, is a data steward exporting a report to Power BI or Excel and scanning it for anomalies by eye. It is about as fun as it sounds.

## Three pillars: ML, NLP, prediction

The cognitive MDM he proposes rests on three capabilities. Machine learning for anomaly detection and automated classification. Natural language processing to read unstructured data, such as documents and user feedback, and let stewards ask why an error occurred in plain language. Predictive analytics on time-series and historical data to raise incidents before the issue materialises.

He connects this to SAP's own direction: SAP Master Data Governance gaining AI and ML capabilities, HANA's in-memory ML libraries and real-time replication, and Datasphere for semantic models across systems. One practical step he built himself is a small LLM-based tool that reads live or legacy data and generates profiling dashboards, so stewards can see where cleansing is needed during a transformation project.

## Real-time monitoring, faster root cause

On the incident side, two ideas stand out. Real-time monitoring with adaptive thresholds and pattern correlation: a sudden spike in rejected purchase orders can be traced to a faulty vendor master record before it reaches finance. And faster root cause analysis through automated lineage tracing that shows where an error started and how it spread, with multidimensional correlation to prioritise the investigation. Some fixes can be automatic, such as correcting a misclassified material code, with approvers notified and compliance logs updated.

His rollout advice is to avoid boiling the ocean: start with an assessment and data profiling, deploy domain-specific modules for the highest-severity use cases first, keep humans in the loop to train the models, and treat change management as seriously as the tooling.

## The numbers he reports

From his implementations, Gobinath reports cleansing effort down 75% with 95% clean data, around 90% classification accuracy as models mature, 60% less time spent, and 80% of incidents prevented through predictive analysis. His examples include a global retailer with 60% less manual effort and a 15% supply chain efficiency gain, and a bank where faster customer onboarding was worth about $5 million in revenue. These are his project results rather than a published study, so treat them as an experienced practitioner's benchmarks.

## Who should watch

SAP data owners, MDG teams and anyone who keeps getting incidents that turn out to be data rather than code. If your organisation does not run SAP, the cascade patterns still apply to any system of record.

## Related Conf42 talks

- [Building Event-Driven AI Agents for Proactive SAP Incident Management](https://www.conf42.com/AI_Agents_2026_Pon_Murugesh_Devendren_sap_incidents_events) by Pon Murugesh Devendren, the agent-based take on SAP incidents.
- [AI-Driven Data Quality Management: Boosting Accuracy and Speed with Python](https://www.conf42.com/Python_2025_Shashank_Reddy_Beeravelly_data_quality_management) by Shashank Reddy Beeravelly, for building the anomaly checks yourself.

[Watch Gobinath Kasimayan's talk](https://www.conf42.com/Incident_Management_2025_Gobinath_Kasimayan_sap_governance_agility)

[Watch the talk on YouTube](https://youtu.be/_1QTklKZZuk).

## Watch the talk

[AI-Driven Master Data Governance for Agile Incident Management in SAP](https://www.conf42.com/Incident_Management_2025_Gobinath_Kasimayan_sap_governance_agility) at Conf42 Incident Management 2025.
