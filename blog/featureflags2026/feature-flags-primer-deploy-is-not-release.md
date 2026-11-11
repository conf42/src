# A first talk on feature flags: deploy is not release

Conf42 Blog, 2026-10-11, updated 2026-11-09. https://www.conf42.com/blog/featureflags2026/feature-flags-primer-deploy-is-not-release

In short: SoftNet Technologies' Emmanuela Opurum at Conf42 Feature Flags 2026 gives a beginner-friendly tour of flags, rollouts, canaries, blue-green, A/B tests and flag hygiene.

The new button that appears in your banking app overnight was probably sitting in production for a while before anyone could see it. At Conf42 Feature Flags 2026, Emmanuela Opurum, Solutions Architect at SoftNet Technologies, gave a beginner-friendly introduction to feature flags built on that one distinction: deploying code and releasing it to users are different events, and flags are what let you control the second one.

This is a 101 and says so in its framing; she opens by addressing people who've never heard of a feature flag. If you run a flag platform already, skip ahead to the hygiene checklist at the end. If you're new to the idea, or need to explain it to a manager, it's a clear place to start.

## The supermarket warehouse

Emmanuela's analogy for deploy versus release is a supermarket. Products can be in the store's warehouse without being on the shelf, where customers can see the price and buy. Deployment is code that passed CI and CD and now sits in production. Release is putting it on the shelf.

The case for flags follows from a bank example. Ship a new transfer feature to every customer at once and, if it fails, every one of them is affected. Release it to a hundred users or to employees first, and the same bug becomes a small, cheap fix. Testing before production still matters, she notes, but real users exercising a feature is a different kind of test.

## Four ways to widen the door

She walks through the main release strategies with everyday examples:

- **Progressive rollout**: 1%, then 10%, then 50%, then everyone, watching bugs, complaints, performance and security at each step before widening.
- **Canary release**: a small group first, with error and performance monitoring, then gradual expansion or withdrawal.
- **Blue-green**: a complete new environment beside the old one, with traffic switched over at once rather than gradually. Her example is a new Buy Now button running in its own environment next to the old one.
- **A/B testing**: two user groups, half on the old button and half on the new, compared on the outcome you actually care about, such as payments, before deciding which to keep.

She also shows an AWS reference diagram of rolling, blue-green and canary strategies side by side, and explains rollback in plain terms: disable the new release and return users to the last stable experience once monitoring shows something wrong, like a button that sends people to a shopping page instead of payments.

## Flags are temporary, and someone owns them

The most useful part for experienced listeners is the hygiene section. Flags shouldn't live forever: once a feature is fully released, remove the flag, or it turns into technical debt. Too many flags make testing hard, because a checkout, a payment and a discount that each depend on separate toggles multiply the combinations you have to check. Access should be least privilege: not every developer should be able to flip a production flag, or someone may switch on a feature a colleague turned off on purpose.

Her closing checklist is short enough to adopt today: a clear name, an owner, a safe default, a planned removal date, and monitoring in place before the flag is turned on. Her starter exercise is equally small: put a new image editor behind a flag called enable image editor, flip it, and watch the old and new experiences swap. It is the hello world of progressive delivery.

## Who should watch

Developers, testers and product people meeting feature flags for the first time, and team leads looking for a gentle explainer to share. Engineers already running percentage rollouts in production will find it familiar, though the checklist is still a decent audit of your own flag inventory.

## Related Conf42 talks

- [From Blue to Green Without Seeing Red: Mastering Deployments on AWS](https://www.conf42.com/DevSecOps_2025_Rayenn_Hamrouni_deployments_aws) by Rayenn Hamrouni of Lenstra at Conf42 DevSecOps 2025.
- [System-Level Experimentation at Scale: Pricing, Supply, A/B and Switchback Testing in FoodTech](https://www.conf42.com/Machine_Learning_2026_Sergei_Nasibian_knowledge_graphs_reasoning) by Sergei Nasibian of Rothesay at Conf42 Machine Learning 2026.

[Watch Emmanuela Opurum's talk](https://www.conf42.com/Feature_Flags_2026_Emmanuela_Opurum_flags_cloud_deployments) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/iAmEsR7l0q8).

## Watch the talk

[Beyond On and Off: Using Feature Flags for Safer Cloud Deployments](https://www.conf42.com/Feature_Flags_2026_Emmanuela_Opurum_flags_cloud_deployments) at Conf42 Feature Flags 2026.
