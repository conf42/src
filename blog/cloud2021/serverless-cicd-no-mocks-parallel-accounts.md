# Serverless CI with no mocks, three AWS accounts and no extra bill

Conf42 Blog, 2021-04-30. https://www.conf42.com/blog/cloud2021/serverless-cicd-no-mocks-parallel-accounts

In short: Efi Merdler-Kravitz (Lumigo) at Conf42 Cloud Native 2021 on a 100% serverless CI/CD flow, real-AWS integration tests in parallel, and skipping redeploys

Lumigo's integration tests never touch a mock of an AWS service, and the team made them faster anyway. At Conf42 Cloud Native 2021, Efi Merdler-Kravitz, VP R&D at Lumigo and an AWS Serverless Hero, walked through the CI/CD flow of a company that is 100% serverless in production and in its pipeline: about 20,000 individual test runs a month, around 30 production deploys a week, and the tricks that took the slowest steps down from hours to minutes.

It is a practitioner's tour of one team's setup, with the numbers and the rough edges left in.

## Why is serverless CI/CD different?

A serverless system is distributed across hundreds of components, so standing it up from scratch is an orchestration job. Many components means frequent deploys. And much of it, such as SQS, SNS and Kinesis, can't run on a Linux build box: there are mocks, not containers, so real behaviour needs a real environment.

Lumigo's ground rules follow from that. Every developer has their own AWS account under AWS Organizations; code not tested on a real AWS environment isn't ready. They started with one shared account and name prefixes, and quickly stepped on each other's toes. Serverless first, across the stack, CI included. No dedicated QA or ops: the developer who picks up the ticket takes it all the way to production, so automation is mandatory.

## The stack, briefly

CircleCI drives the pipeline, the Serverless Framework deploys, code is mostly Python with some Node.js. Planning moved from Kanban and Trello to week-long Scrum sprints in Jira as the team grew. GitHub flow: master plus feature branches, and every merge to master deploys to production. They chose a repo per service over a monorepo, partly because it stops developers reading another service's DynamoDB table just because they can import it.

With around 20 services to install into each developer's account, they built an internal Python tool called Uber Deploy (nothing to do with Uber, he notes) that pulls the right branch of each repo, installs requirements and deploys services in parallel in the right order. It is used only for developer and integration environments; production services deploy on their own updates.

## Why not mock AWS?

Tests run in three layers: unit tests locally (Pytest, Mocha, Jest) behind git pre-commit hooks with Black, Flake8, Prettier and ESLint; API-driven integration tests in Node.js and Mocha; and end-to-end flows such as onboarding in Cypress.

Merdler-Kravitz is firm on mocks: some AWS services lack good ones, mocks lag the latest APIs, tools like LocalStack are complicated to run, and the mocks have bugs of their own. More than once, something failed against a mock and then worked perfectly on AWS. "I prefer not to waste my time on debugging mocks," he said at Conf42 Cloud Native 2021.

## Parallel environments for free, almost

The cost of real environments is time. With 20 services, around 200 Lambdas, several DynamoDB tables and Kinesis, a deploy took about an hour and the integration tests about an hour and a half.

The test fix uses the serverless billing model: deploy to three integration environments and split the tests between them so they don't interfere. Idle serverless resources cost nothing, except Kinesis, which needs at least one shard. Test time fell from an hour and a half to around 40 minutes, and scaling further means adding accounts.

The deploy fix: tag each CloudFormation stack with the repo's latest commit hash, and have Uber Deploy skip any service whose code hasn't changed. Redeploys dropped from around 30 minutes to 5. The first deploy into a fresh environment is still slow, and he says so.

## Staging the SDK, measuring the tests

Lumigo's SDK runs inside customers' Lambdas, so a bug there crashes someone else's function. Its release flow publishes an alpha to npm (customers don't see it), deploys it into Lumigo's own environment, and runs a Step Function that releases the final version if nothing goes wrong, with a red button to stop it.

Test results go to Elasticsearch. The useful chart is failures by branch: one branch failing may be a bug in that branch, but the same test failing on many branches is probably a broken test. They also track deployment failures, such as hitting AWS limits when creating several EventBridge resources at once.

Cleaning environments is the unsolved part: a combination of aws-nuke and the open source lumigo-cli, taking a couple of hours per account.

## Who should watch

Teams building on AWS Lambda who are fighting slow pipelines or flaky mocks. The parallel-accounts and commit-hash tricks are directly reusable. The closing demo shows Lumigo monitoring Lumigo; the CI/CD material is the reason to watch.

## Related Conf42 talks

- Zan Markan on [the need for speed in your CI/CD setup](https://www.conf42.com/Cloud_Native_2021_Zan_Markan_need_for_speed_cicd_setup) at Conf42 Cloud Native 2021.
- Aviad Mor on [observability across serverless managed services](https://www.conf42.com/Cloud_Native_2021_Aviad_Mor_observability_serverless_asynchronous_managed_services) at Conf42 Cloud Native 2021.
- Sam Williams on [a serverless-first SaaS startup in 30 days](https://www.conf42.com/Cloud_Native_2023_Sam_Williams_serverless_first_saas_startup_in_30_days) at Conf42 Cloud Native 2023.

[Watch Efi Merdler-Kravitz's talk](https://www.conf42.com/Cloud_Native_2021_Efi_MerdlerKravitz_cicd_serverless)

## From Lumigo

Lumigo is a SaaS platform for AWS monitoring and observability focused on serverless workloads, and the team behind the open source lumigo-cli.

- [lumigo.io](https://lumigo.io/?utm_source=conf42)
- [lumigo-cli on GitHub](https://github.com/lumigo-io/lumigo-CLI)

[Watch the talk on YouTube](https://youtu.be/q1_1N8KCeMM).

## Watch the talk

[CI/CD in the serverless era](https://www.conf42.com/Cloud_Native_2021_Efi_MerdlerKravitz_cicd_serverless) at Conf42 Cloud Native 2021.
