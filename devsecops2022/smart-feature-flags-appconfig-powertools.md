# Test the feature flag when it's off, not just when it's on

Conf42 Blog, 2022-12-02. https://www.conf42.com/devsecops2022/smart-feature-flags-appconfig-powertools

In short: Ran Isenberg (CyberArk) at Conf42 DevSecOps 2022 on rule-based feature flags with AWS AppConfig and Lambda Powertools, from dev to retirement

Ran Isenberg, Principal Software Architect at CyberArk and an AWS Community Builder, showed at Conf42 DevSecOps 2022 how his team changes service behaviour without redeploying the service: feature flags stored in AWS AppConfig and evaluated by the feature flags utility he designed and contributed to AWS Lambda Powertools. The most useful part is not the SDK but the lifecycle around it, including a production bug that ran a feature everyone thought was switched off.

## What problem are feature flags solving here?

Three needs. Turn off a broken feature as fast as possible. Roll a feature out gradually, 10%, then 20%, up to 100% of customers, with an automatic rollback on errors. And A/B testing, for example a premium feature set for premium customers. On top of that his requirements included support for both Lambda functions and containers, FedRAMP High certification, and a solution that is fully managed: no backups or high availability to look after.

## Static or dynamic configuration?

A feature flag is configuration, and configuration comes in two kinds. Static configuration (environment variables, JSON files inside the Lambda zip) changes only when the service pipeline runs again, with all its gates and tests. Dynamic configuration is fetched at runtime by API call and deployed by its own, much quicker pipeline. Dynamic means one more pipeline to manage, but it lets you change behaviour quickly, so that's what he picks.

## Why AWS AppConfig?

It's an AWS service, so no third-party integration, no traffic leaving the account and no vendor security review. He says it was one of the few feature flag options, maybe the only one, with FedRAMP High. It's fully managed, it validates configuration against a JSON schema so a malformed upload fails the deployment instead of your service, and it has deployment strategies: a canary such as AppConfig.Canary10Percent20Minutes, watched by CloudWatch alarms that roll the configuration back if they fire. Configurations live under an application (your service) and an environment (dev, test, production).

## What makes a flag smart?

The Powertools utility fetches the configuration from AppConfig, keeps it in an in-memory cache and evaluates flags for you. Lambda Powertools itself is popular, over a million downloads a month, and despite the name the utility also works in containers.

A regular flag is a name with a default. Evaluate it, get a boolean, branch. Always pass a default in code too: if someone deletes the flag from the configuration, the function falls back instead of crashing.

A smart flag adds a rule engine that evaluates against a context you pass in. His example: the event carries a username and a tier; a rule says that when tier equals premium the flag is true, otherwise the default false applies. Same configuration, different behaviour per user, which is the A/B testing requirement. There are more than ten actions (equals, not equals, starts with, key in value, greater than and more), and flags don't have to be boolean: any valid JSON works, such as a list of special actions like removing limits and ads for premium accounts.

The cache is a cost decision. Ran Isenberg said at Conf42 DevSecOps 2022: "Because each call to AWS app config to fetch configuration costs money and we want to save some money." The trade-off is that a longer cache means a slower change in behaviour.

## Best practices from build to retirement

- **Plan and build**: the development team owns the flag end to end, writes the JSON rules and the code that evaluates them, and enables the feature in dev and test accounts while it stays off in production.
- **Test**: mock the configuration, and test both states. With the flag enabled, check the new code runs and its side effects are right. With it disabled, assert the new code does not run. He learned this one the hard way: "We actually had a bug where our feature was marked as false, but due to a bug in the if statement, it was a complicated one." The feature ran in production anyway.
- **Release**: once stable outside production, deploy with a canary strategy and CloudWatch alarms on service errors for automatic revert.
- **Operate**: on errors, disable the flag immediately through the configuration pipeline, add the missing test cases, redeploy, and hold a retro on why the tests missed it.
- **Retire**: flags add branches, mocks and tests. His team meets monthly to pick candidates: features on for all customers for some weeks, stable, with positive feedback, no open issues and no planned changes nearby. Remove the code and redeploy the configuration.

## Who should watch

Serverless teams on AWS who want flags without adding a third-party service, and anyone who has shipped a flag and never removed it. The code examples are Python, but the pattern carries over. Related: [Travis Gosselin on deploy velocity with feature flags](https://www.conf42.com/Site_Reliability_Engineering_2022_Travis_Gosselin_unleashing_deploy_velocity_feature_flags), [Hammad Mushtaq on flagging your canaries](https://www.conf42.com/Cloud_Native_2022_Hammad_Mushtaq_pushing_code_flag_your_canaries) and [Matthew Schillerstrom on feature flags for reliability](https://www.conf42.com/Chaos_Engineering_2024_Matthew_Schillerstrom_feature_flags_reliability_agile_response).

[Watch Ran Isenberg's talk](https://www.conf42.com/DevSecOps_2022_Ran_Isenberg_level_up_cicd_smart_aws_feature_flags)

## From CyberArk

- [CyberArk](https://www.cyberark.com/): identity security, the speaker's employer.

[Watch the talk on YouTube](https://youtu.be/3IT4UzN9Jds).

## Watch the talk

[Level Up Your CI/CD With Smart AWS Feature Flags](https://www.conf42.com/DevSecOps_2022_Ran_Isenberg_level_up_cicd_smart_aws_feature_flags) at Conf42 DevSecOps 2022.
