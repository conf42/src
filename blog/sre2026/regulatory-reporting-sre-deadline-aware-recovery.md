# In regulatory reporting, a missed deadline is a compliance failure

Conf42 Blog, 2026-03-10, updated 2026-11-09. https://www.conf42.com/blog/sre2026/regulatory-reporting-sre-deadline-aware-recovery

In short: Bhargavaram Potharaju of Wells Fargo at Conf42 SRE 2026 on high availability, deadline-aware disaster recovery and audit replay for regulatory reporting.

When a regulatory report is late, nobody files it under operations. At Conf42 Site Reliability Engineering 2026, Bhargavaram Potharaju, Senior Infrastructure Engineer at Wells Fargo, argued that on national-scale reporting platforms SRE directly decides compliance outcomes, and that high availability, disaster recovery and audit readiness have to be designed in from day one rather than added after the first audit finding.

It is a short, architecture-level talk with no vendor in it: a reference model, the principles behind it, and a path to adopt it one layer at a time.

## Your SLOs should be written in filing deadlines

The pressure he describes comes from two directions: data volumes grow each reporting cycle while submission windows shrink. In that world a delay is not a service issue and a wrong output is not a data issue; both can turn into penalties. So service level objectives, incident response and error budgets all need to line up with regulatory deadlines, not generic IT targets.

He names five places legacy platforms struggle: high availability, peak-load performance, data accuracy, auditable outcomes and disaster resilience. Most enterprise systems are tuned for an average Tuesday. Reporting platforms live and die in the crunch right before cutoff.

## Recovery time is measured backwards from the cutoff

The most useful idea is deadline-aware disaster recovery. Recovery objectives cannot be picked in isolation; they depend on how much time is left before submission. If an outage hits close to a deadline, the platform still needs time to recover, reprocess, validate and submit, and ideally time to validate the results before sending them. An RTO that looks fine on paper can be useless an hour before the filing window closes.

That is also why he insists failover be tested under realistic load. Availability tested only under daily traffic tells you nothing about burst traffic and peak concurrency, and a DR plan that has never run at peak is, in his framing, a theoretical design exercise.

## Prove how the number was made, not just the number

Audit readiness gets its own section. The platform has to show exactly how a submission was created: immutable logs, full data lineage and deterministic replay, so you can rerun the process and reproduce the same result when asked. The pipeline he sketches runs ingestion, validation, transformation, submission, monitoring and audit replay, with fault isolation between stages so that a problem in one stage cannot silently corrupt the next.

## Business telemetry catches what server metrics miss

Server metrics will tell you a machine is stressed. They will not tell you the deadline is at risk. He wants observability at the business-process level: record counts, validation pass and fail rates, queue depth, per-stage latency, submission timing and acknowledgement status.

The failure mode he flags as most dangerous is the silent one: records dropped, validations skipped, acknowledgements never confirmed, all while the platform looks healthy, and nobody finds out until the audit. His answer is end-to-end validation gates and explicit confirmation that each record reached a correct outcome. He also accepts that many of these platforms cannot go fully cloud native because of security, data residency or legacy integrations, so the controls have to work in hybrid setups too.

## Who should watch

Engineers and architects on finance, insurance or government reporting systems, and anyone whose batch pipeline has a hard external deadline. It is high level and light on tooling; the value is the framing and the checklist: identify current failure modes, define compliance-aligned SLOs, improve telemetry, test DR in realistic scenarios, then harden submission gates step by step.

## Related Conf42 talks

- [Compliance-Aware Platform Engineering: Scaling Hybrid Cloud Automation in Regulated Financial Environments](https://www.conf42.com/Platform_Engineering_2025_Satish_Manchana_aware_regulated_hybrid) by Satish Manchana.
- [Enhancing Resilience with Azure Site Recovery](https://www.conf42.com/Chaos_Engineering_2025_Somaning_Turwale_resilience_recovery_disaster) by Somaning Turwale, for the DR mechanics on one cloud.
- Jaya Krishna Vemuri on [cloud-driven reconciliation for financial accuracy](https://www.conf42.com/Chaos_Engineering_2025_Jaya_Krishna_Vemuri_investment_banking_accuracy) in investment banking.

[Watch Bhargavaram Potharaju's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Bhargavaram_Potharaju_national_scale_regulatory) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/9cs89GFPR5U).

## Watch the talk

[SRE for National-Scale Regulatory Reporting: HA, DR, and Audit-Ready Design](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Bhargavaram_Potharaju_national_scale_regulatory) at Conf42 Site Reliability Engineering (SRE) 2026.
