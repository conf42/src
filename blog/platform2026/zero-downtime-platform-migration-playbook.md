# Replace the system the business runs on without a big-bang weekend

Conf42 Blog, 2026-11-01, updated 2026-11-09. https://www.conf42.com/blog/platform2026/zero-downtime-platform-migration-playbook

In short: Saikrishna Ala (Bath and Body Works) at Conf42 Platform Engineering 2026 on dual-write, bidirectional sync and CDC as reusable migration capability.

A big-bang cutover concentrates every risk of a migration into one weekend and gives you exactly one shot. At Conf42 Platform Engineering 2026, Saikrishna Ala, Senior Applications Developer at Bath and Body Works who leads data integration and platform modernisation, laid out a practitioner playbook for replacing systems the business uses every hour: three patterns, a readiness check before the flip, and an argument for building all of it once as platform capability.

His running example is Bath and Body Works' order management migration from Radial to Manhattan Active Omni, with 100% of order traffic and zero tolerance for downtime.

## Why the rehearsed weekend still fails

Big-bang plans look manageable on paper: one weekend, a runbook, a rollback plan. What they hide, in Saikrishna's list: data drift your test environment never reveals, no validation on real (messy, voluminous) traffic, a rollback that becomes very hard once records have landed in the new system, and a blast radius that hits every user and integration at once.

## Pattern one: dual-write and parallel run

Every write goes to both legacy and new systems; legacy stays the source of truth and serves reads; an automated reconciliation layer compares the two. He breaks it into five phases: shadow (new system takes writes, legacy serves all reads), compare (fix every divergence, which can take weeks, so don't skip it), canary reads (a small slice of reads from the new system), flip (new becomes source of truth, legacy stays as fallback), and retire. The discipline: don't move from compare to canary until divergence is at or near zero. Decide up front your reconciliation latency target, how divergences reach engineers, and how fast you can roll reads back.

## Pattern two: bidirectional sync for long coexistence

When teams will sit on different systems for months while users migrate in waves, a sync layer keeps both alive and consistent. His four non-negotiables:

- **Resolve conflicts deterministically**: per-field ownership, or last-write-wins with timestamps. Figuring it out at runtime is not a strategy.
- **Prevent echo loops**: every change carries an origin tag, and the sync layer never sends a change back where it came from.
- **Make every write idempotent**: replays will happen, so use upserts everywhere.
- **Preserve ordering per entity**: out-of-order applies leave data inconsistent.

## Pattern three: CDC from the transaction log

Change data capture reads the legacy database's transaction log, with no schema changes or application instrumentation and no batch queries against the legacy app. Events go to a durable, replayable stream, and the new platform, search index and analytics consume it independently. The abstract cites Forrester data that event-driven approaches can cut data latency from hours to milliseconds; in the talk he puts most CDC workloads at milliseconds to seconds, versus hours of lag for batch ETL. Three operating rules: take a full snapshot before streaming increments, handle schema changes as versioned events, and monitor consumer lag end to end. Lag, he says, is the migration's heartbeat.

Most real migrations combine them: CDC for the data layer, dual-write or bidirectional sync for the application layer. Dual-write proves the new system on production traffic but needs an application change; sync suits long coexistence at the cost of the sync layer itself; CDC suits high-volume movement when you can't touch the legacy app, with lag and schema drift as the risks.

## Score readiness, then pick a date

Before cutover, score five dimensions: latency (how fresh is data on both sides), reliability (does sync survive failure and replay, chaos-tested before the flip), bidirectionality (changes flow both ways without loops or corruption), scalability (load-tested at peak, not average) and migration safety (verified rollback, no-go checklist, step-by-step plan). If you can't score all five with confidence, you're not ready. Set the date when you can, not before.

The organisational point closes the talk. When every migration team builds its own sync and reconciliation, safety guarantees are inconsistent and every cutover is a heroic weekend. Built once as platform primitives, cutovers become routine engineering, and the investment pays back from the second migration on.

## Who should watch

Platform and data teams facing an OMS, CRM, claims or similar replacement, and anyone who needs to argue internally for funding migration tooling instead of another heroic weekend. It's a patterns-and-checklists talk rather than a detailed account of the Bath and Body Works migration itself.

## Related Conf42 talks

- [Migration from On-Prem Messaging System to The Cloud: What, How and Why](https://www.conf42.com/Cloud_Native_2026_Ran_Tao_data_analytics_insights) by Ran Tao
- [Migrating to Multi Cluster Managed Kafka with 0 Downtime](https://www.conf42.com/Cloud_Native_2022_Natan_Silnitsky_migrating_multi_cluster_managed_kafka_0_downtime) by Natan Silnitsky (Wix)
- [De-Risking a Legacy CRM Migration in Life Sciences: Feature-Flag-Driven Rollout Strategy for a Governed Salesforce Patient Engagement Platform](https://www.conf42.com/Feature_Flags_2026_Jaymin_Sutarwala_crm_migration_salesforce) by Jaymin Sutarwala (United Therapeutics)

[Watch Saikrishna's talk](https://www.conf42.com/Platform_Engineering_2026_Saikrishna_Ala_migrations_downtime_playbook)

[Watch the talk on YouTube](https://youtu.be/H7dZ8BoJdpM).

## Watch the talk

[Platform Migrations Without the Downtime: An Engineering Playbook](https://www.conf42.com/Platform_Engineering_2026_Saikrishna_Ala_migrations_downtime_playbook) at Conf42 Platform Engineering 2026.
