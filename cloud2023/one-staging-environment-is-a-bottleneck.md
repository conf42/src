# One shared staging environment is a bottleneck with a URL

Conf42 Blog, 2023-03-30. https://www.conf42.com/cloud2023/one-staging-environment-is-a-bottleneck

In short: Lucas da Costa (Ergomake) at Conf42 Cloud Native 2023 on replacing the single staging environment with on-demand, observable, freshly seeded pre-production

When staging goes down, everyone who develops against staging stops working. At Conf42 Cloud Native 2023, [Lucas da Costa](https://www.conf42.com/Cloud_Native_2023_Lucas_da_Costa_staging_environments_blueprint_preproduction), founder of Ergomake and author of *Testing JavaScript Applications*, argues that the single shared staging environment is the real problem, and lays out a blueprint for pre-production: environments on demand, owned by developers, budgeted per team, seeded with fresh fake data and watched like production.

Ergomake builds pre-production environments, and the talk draws on what its users ran into. The product barely appears; the advice works with whatever tooling you have.

## What is staging for, anyway?

He starts by listing why teams use it. Development, because nobody can run a thousand containers and a pile of queues on a laptop, so they run one service locally and point it at staging. Testing, because end-to-end and synthetic tests need somewhere to run that isn't a developer's machine. And validation, because designers and product people need to see the app before it ships. Underneath, pre-production does three jobs: check features match the spec, catch bugs before production, and share context between technical and non-technical people.

"But there are better ways to get all of these benefits than what we currently do," Lucas da Costa said at Conf42 Cloud Native 2023.

## How does a single staging environment fail everyone?

The causes are opaque CI pipelines, complex Helm charts and Terraform that developers don't understand (and sometimes neither does infra), so developers can't create environments themselves and wait on the ops team instead. With only one environment, the failures stack up by role:

- Developers are blocked whenever staging is down or misbehaving.
- Designers see changes only after they are merged and deployed, when feedback is expensive.
- QA tests on top of everyone else's fake data and can't tell a bug from someone else's mess.
- Product managers wait for two developers with conflicting features to sort out who deploys first.

## Environments on demand, with a budget

The fix starts with letting developers spin up an environment whenever they need one. That takes simple infrastructure code and good abstractions from SREs or a platform team, or, if there is no platform team, an infrastructure expert embedded in the dev team as an in-house consultant.

Many environments sound expensive, and they are, so give each team a resource pool and a spending cap instead of an approval queue for every new instance. And not every environment has to be a copy of production. His model has three profiles: functional equivalence for development (the queues and services exist), performance equivalence for validation (designers and QA put little load on the system, so a scaled-down copy behaves the same), and infrastructure equivalence for testing, which still needs nothing like production's instance count to catch most of the bugs.

## Fresh fake data in every environment

Every new environment should get a fresh, representative data set generated from the production schemas as part of its deployment pipeline. A small script that reads the schema and fills it with Faker gives realistic data with no PII. The bonus he hears about most from Ergomake's users: migrations run against that data before production, so you find out whether one destroys something important while it still doesn't matter.

## Put the links where reviewers already are

To move non-technical feedback earlier, give every pull request a link to its own environment, the way Vercel previews work for Next.js apps and Ergomake does for full stacks. Then designers and PMs review functionality by clicking a link instead of guessing what is on staging. Put sensitive previews behind auth so unreleased features don't end up indexed by crawlers.

## Make pre-production observable

Pre-production gets little traffic, so errors hide. Wire up Prometheus and an alert manager posting to Slack, so a backend error during someone's QA session isn't missed even when the page looked fine. Run synthetics and end-to-end tests continuously against each environment, which also keeps them off production. And accept that pre-production won't catch everything: keep production reliable and ship behind feature flags so an escaped bug is a toggle, not a rollback.

## Who should watch

Platform and DevOps engineers who own the staging environment everyone complains about, and team leads deciding whether preview environments are worth the cloud bill. It is a short, dense talk with a summary checklist at the end.

Related Conf42 talks:

- Natalie Lunbeck on [ephemeral environments](https://www.conf42.com/Cloud_Native_2024_Natalie_Lunbeck_ephemeral_environments), Conf42 Cloud Native 2024.
- Mario Garcia on [generating test data for a database project](https://www.conf42.com/Python_2023_Mario_Garcia_generate_test_data_database_project), Conf42 Python 2023.
- Matthew Schillerstrom on [feature flags for reliability](https://www.conf42.com/Chaos_Engineering_2024_Matthew_Schillerstrom_feature_flags_reliability_agile_response), Conf42 Chaos Engineering 2024.

## From Ergomake

Ergomake builds on-demand pre-production environments, the kind of per-pull-request staging the talk recommends.

- [Ergomake](https://ergomake.dev/)

[Watch the talk on YouTube](https://youtu.be/mcsXn-mWvjk).

## Watch the talk

[Designing Staging Environments: A Blueprint for Pre-production](https://www.conf42.com/Cloud_Native_2023_Lucas_da_Costa_staging_environments_blueprint_preproduction) at Conf42 Cloud Native 2023.
