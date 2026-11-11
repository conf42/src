# Release a regulated CRM migration like a feature, not a weekend

Conf42 Blog, 2026-09-25, updated 2026-11-09. https://www.conf42.com/featureflags2026/release-crm-migration-like-a-feature

In short: United Therapeutics' Jaymin Sutarwala at Conf42 Feature Flags 2026 on cohorts, shadow runs and capability rollback for a patient CRM migration.

The riskiest feature most companies ever release is a whole platform, switched on for every user and every record over one weekend. At Conf42 Feature Flags 2026, Jaymin Sutarwala, Associate Director of CRM Strategy and Operations at United Therapeutics, argued that the progressive delivery toolkit (flags, canaries, cohort rollouts) scales up to a regulated CRM migration, and walked through the control plane and state model that make it work.

The talk's abstract sets the context: retiring a legacy patient CRM in favour of a Salesforce ecosystem spanning Marketing Cloud, Data Cloud and Health Cloud, without disrupting live patient engagement or exposing health data. The recording itself stays at the pattern level rather than walking through that project screen by screen.

## The CRM is a hub, and its dependencies are undocumented

Jaymin's first point is that a CRM isn't really an application. Identity rules, web forms, support programmes, contact centres, warehouses, partner feeds, emails, texts and consent all hang off it. Most of those dependencies live in field names, nightly jobs and a workflow someone built years ago that nobody remembers until it stops.

A big-bang cutover moves data, integrations, users and communications across the line at the same moment, which maximises the size of the change and minimises your ability to isolate a problem. Rollback is the real trap. By Wednesday you'd have to unmigrate changed data, work out which emails already went out and repoint integrations that have written records, so rollback quietly turns into fix forward whatever it takes.

## Deploy the platform, then activate it

The way out is the separation this audience already lives by: deployment is not release. He credits Pete Hodgson's feature toggles article on Martin Fowler's site and James Governor's naming of progressive delivery. The new CRM can be fully deployed, integrated and loaded with data while still not being the system anyone depends on.

In between sits a migration control plane that answers one question everywhere: for this request, record or workflow, which path right now? The answer depends on cohort, capability, channel, region, integration and data domain. He's explicit that it needn't be a commercial flag product; gateway routing rules or a config table can do the job, with OpenFeature for the code-level piece. Each cohort or capability moves through explicit states: legacy only, shadow, dual run, pilot, new primary (legacy still fed so rollback stays cheap), legacy disabled. If you can't say what state a cohort is in, since when and who approved it, he says, you don't have a migration plan. You have hope.

## Three patterns that carry the risk

- **Deliberate cohorts.** Random percentages spread odd records evenly so nobody sees a pattern. Pick cohorts by team, segment, data complexity (clean recent records before ones with 15 years of merges), workflow, region or channel, and make assignments sticky by hashing a stable identifier.
- **Integration routing.** Integrations write whether you're watching or not, so a routing decision sits in front of them. That makes it a distributed system, with the usual non-negotiables: correlation IDs, idempotent writes, duplicate detection on business keys, bounded retries into a dead-letter queue someone watches, and a reconciliation store.
- **Shadow and dual run.** Legacy's result is what the person experiences; the new platform processes the same event and sends its output to a comparator. He cites GitHub's Scientist library and Sam Newman's parallel run. Shadow mode must suppress side effects, and not every difference is a bug: sometimes legacy has been quietly wrong for years.

## Flag, telemetry, threshold, rollback

A migration flag without telemetry tagged by flag state, a threshold and a named rollback action is a switch, not a control. Signals go beyond errors and latency to reconciliation mismatches, duplicates, stalled workflows, delivery failures and support tickets. OpenTelemetry's feature flag semantic conventions turn the question of whether things got worse after a flip into a query instead of a meeting.

Regulation makes this more valuable, not less. Audit every flag change, carry consent with the record whichever path is active, keep access control equivalent on both sides, and keep sensitive data out of flag evaluation context and telemetry. He also retells Knight Capital as the cautionary tale for repurposed flags, and closes with capability-level rollback: if one reminder workflow creates duplicates, flip that one route back to the warm legacy path and leave everything else alone.

## Who should watch

Anyone planning an enterprise platform migration, especially with personal or health data involved. The eight-step loop near the end (map, flag, shadow, compare, pilot, observe, expand, retire) is the slide to keep.

## Related Conf42 talks

- [Beyond the Toggle: Feature Flags as Your Cloud-Native Migration Safety Net](https://www.conf42.com/Cloud_Native_2026_Ryan_Vila_feature_flags_migration) by Ryan Vila of Harness at Conf42 Cloud Native 2026.
- [Zero-Downtime by Design: High-Availability Migration Patterns for Modern Gateway & Platform Engineering](https://www.conf42.com/DevOps_2026_Kalyan_Inturi_availability_migration_gateways) by Kalyan Inturi of Oracle Cloud Infrastructure at Conf42 DevOps 2026.
- [DevOps Excellence in Healthcare: Orchestrating a Large-Scale CRM Implementation](https://www.conf42.com/DevOps_2025_Anirudh_Peri_healthcare_crm_devops) by Anirudh Peri of Lookout at Conf42 DevOps 2025.

[Watch Jaymin Sutarwala's talk](https://www.conf42.com/Feature_Flags_2026_Jaymin_Sutarwala_crm_migration_salesforce) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/xfA_Y5pGfM0).

## Watch the talk

[De-Risking a Legacy CRM Migration in Life Sciences: Feature-Flag-Driven Rollout Strategy for a Governed Salesforce Patient Engagement Platform](https://www.conf42.com/Feature_Flags_2026_Jaymin_Sutarwala_crm_migration_salesforce) at Conf42 Feature Flags 2026.
