# Feature flags turn a migration into a ramp you can walk back down

Conf42 Blog, 2026-10-15, updated 2026-11-09. https://www.conf42.com/blog/featureflags2026/feature-flags-make-migrations-reversible

In short: Ryan Vila of Harness at Conf42 Feature Flags 2026 on gradual, measurable, reversible cloud-native migrations, and the flag hygiene that keeps them safe.

A migration that can only move forward is a bet, not a plan. At Conf42 Feature Flags 2026, [Ryan Vila](https://www.conf42.com/Feature_Flags_2026_Ryan_Vila_feature_flags_migration), Americas Advisory Director at Harness, showed how feature flags turn a cloud-native migration into a series of small, measured steps, each of which you can pause or undo, and why the flags themselves need the same discipline as the code they guard.

Ryan works with teams adopting feature management and experimentation, and he came to Harness through Split, the feature management company Harness acquired. The talk is a vendor keynote, but most of it is practice you can apply with any flagging tool.

## Three ways a migration goes wrong

Ryan opens with the failure modes he sees most often. The first is the big bang cutover: deployment and release are the same event, and teams often bundle a UI change, a pipeline change and a new service into one switch. If any one of them breaks, all of them roll back together, assuming they can.

The second is a forward-only path. If you can't pause halfway or step back a stage, nobody wants to start, and the migration stalls in planning. The third is an uncontrolled blast radius: when deploy equals release, 100% of users meet the bug at the same moment.

His answer is the strangler fig pattern, which he openly calls a refresher. Run the new service next to the old one, route a controlled slice of traffic to it with a flag, compare the two streams, and retire the old path once the evidence says so. Nothing new in the idea; the hard part is doing it on purpose.

## Back up a stage instead of pulling the plug

The most useful part of the talk is the ramp. Ryan describes it as a ladder: internal users first, then test accounts with synthetic traffic or trusted customer QA teams, then a small release, then a measured ramp to general availability. What counts as small is up to you: 1% of traffic, one zip code, one region. The rule is the smallest blast radius that still lets you see a negative effect.

He asks you to treat the whole ramp like a load test. Something can be fine at 5% and break at 6%, so you keep measuring at every step, with the same metrics you used at the start.

The point people skip: when a metric goes wrong, the right move often isn't the kill switch. You can drop from the measured ramp back to the small release, or from the small release back to test accounts, learn what scale exposed, and climb again. Killing everything is sometimes more disruptive than stepping down one rung.

## The flag is code, so test every state

Ryan closes with a cautionary section that deserves its own poster. Stale flags need a lifecycle and governance, because a forgotten flag is a landmine for whoever toggles it next while trying to work out what it does. Flags have more than on and off: there is a default state for when evaluation fails, and teams must test that fallback path too.

He also warns about configuration drift. Flag definitions in staging should match production, and if you keep flags in a disaster recovery environment, they should match production at the moment you fail over, or be off. And ownership has to be explicit, because whoever owns the flag owns the decision to flip it during an incident.

His summary line is the one to keep: the flag itself is a change. "It is its own code and therefore should be tested as code in all of its states." Then it gets deleted when nothing calls it any more, like any other dead code.

## Three questions to take back to your team

The talk ends with homework for whatever migration you have in flight. How are you gating the new path, and is every element that changes actually behind a control? If it goes wrong, which flag reverts or scales back, and could that be automated instead of waiting for whoever is awake at 3am? And what is your rollback SLA, the time between "we have a problem" and solid ground again?

## Who should watch

Platform and release engineers planning a re-platforming, and SREs who get asked to approve one. If your migration plan has a single cutover weekend on it, this one is worth your evening. If your team already runs progressive delivery with per-cohort metrics, the hygiene section is the part to send to everyone else.

An earlier cut of the same material ran at Conf42 Cloud Native 2026 with more time on the Split pipeline case study; this version leans into the ramp and the flag lifecycle.

## Related Conf42 talks

- [Unleashing Deploy Velocity with Feature Flags](https://www.conf42.com/Site_Reliability_Engineering_2022_Travis_Gosselin_unleashing_deploy_velocity_feature_flags) by Travis Gosselin (SPS Commerce), on decoupling deploy from release at scale.
- [Migration from On-Prem Messaging System to The Cloud: What, How and Why](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Ran_Tao_migration_prem_messaging) by Ran Tao (AWS), on why lift and shift fails for messaging.
- [Integrating Chaos Engineering and Feature Flags for Enhanced Reliability](https://www.conf42.com/Chaos_Engineering_2024_Matthew_Schillerstrom_feature_flags_reliability_agile_response) by Matthew Schillerstrom, pairing flags with failure injection.

[Watch Ryan Vila's talk](https://www.conf42.com/Feature_Flags_2026_Ryan_Vila_feature_flags_migration).

## From Harness

Harness sponsored Conf42 Feature Flags 2026. The flag practices in this talk map to its feature management and experimentation module, which grew out of Split.

- [Harness](https://www.harness.io/)
- [Harness Feature Management & Experimentation](https://www.harness.io/products/feature-management-experimentation)
- [Feature Management & Experimentation docs](https://developer.harness.io/docs/feature-management-experimentation)

[Watch the talk on YouTube](https://youtu.be/Q1nDdka4AiU).

## Watch the talk

[Making Cloud-Native Migrations Gradual, Measurable, and Reversible](https://www.conf42.com/Feature_Flags_2026_Ryan_Vila_feature_flags_migration) at Conf42 Feature Flags 2026.
