# Test serverless code locally against the real cloud, then throw the stack away

Conf42 Blog, 2024-03-20. https://www.conf42.com/cloud2024/remocal-testing-ephemeral-environments

In short: Yan Cui (Lumigo) at Conf42 Cloud Native 2024 on remocal tests, plain zip deployments and ephemeral environments for faster serverless work

Mocks tell you whether your code does what you expected, not whether it works. At Conf42 Cloud Native 2024, [Yan Cui](https://www.conf42.com/Cloud_Native_2024_Yan_Cui_patterns_efficient_serverless), Developer Advocate at Lumigo and an AWS user since 2010, laid out three habits for an efficient serverless workflow: test Lambda code locally against real AWS services, keep deployments boringly simple, and give every feature its own short-lived environment.

He also consults, and most of the advice comes from watching client teams hurt themselves. It is framework-agnostic, though the demo uses the Serverless Framework.

## Why are mocks not enough?

Local tests against mocks are fast, debuggable and need no deployment. The catch, in his framing, is that they check your code against your assumptions, and you used the same assumptions to write both the code and the test. He has seen plenty of applications pass every test and fail the first time they run in AWS.

Mocks also skip everything that is not your code: IAM permissions, API Gateway authentication, AppSync resolver templates, EventBridge event patterns, direct service integrations. Yan Cui said at Conf42 Cloud Native 2024: "Customers are not going to care if the problem is with your configuration and not your code."

Testing in the cloud covers all of that, but a full deployment after every small change makes the feedback loop painful.

## What is remocal testing?

His answer is remocal testing: run the code locally, so breakpoints and fast iteration still work, but point it at real AWS resources such as DynamoDB tables, SNS topics and queues. Around it sit unit tests for domain logic and end-to-end tests for what only exists after deployment, such as API Gateway request validation, transforms and Cognito or IAM auth.

The demo makes this concrete. The same test cases switch between modes with a test-mode environment variable. In remocal mode a helper requires the Lambda handler locally and calls it with a stubbed event and context; in end-to-end mode the test creates a Cognito user, gets an ID token and calls the deployed API Gateway endpoint. One schema test, checking that a POST body needs a string `name`, can only run end to end, because that validation lives in API Gateway.

There is a nice unplanned moment, too: he commented out the database write and the test stayed green. A breakpoint showed the bug was in the test, a neat accidental argument for stepping through tests.

## Why avoid Lambda layers?

His deployment advice is to use the simplest option that works. Lambda layers, container images, custom runtimes and provisioned concurrency all have their uses, but in his words, "for 90% of use cases you shouldn't use any of these options."

He saves his strongest words for layers as a way to share code, with a long list of reasons:

- No semantic versioning.
- Security scanners don't know about them, so they can't check them for known vulnerabilities.
- A limit of five layers per function, and they still count towards Lambda's 250 MB unzipped size limit.
- They make local and remocal testing harder, because the dependency only exists in AWS.
- They don't really work for compiled languages like Java or .NET, which need dependencies at compile time.
- Publishing an update is more work than with npm, and you lose bundling and tree shaking.

Instead: shared code within a project goes in a folder and gets bundled with each function, which SAM, the Serverless Framework and CDK all support; shared code across projects goes into a private npm registry. Stick to zip files and managed runtimes so the platform owns the runtime, and use container images only when you outgrow the 250 MB limit.

## How should environments be organised?

At minimum one AWS account per stage (dev, test, staging, production) to contain both throughput problems and breaches. Large organisations should go to one account per team per stage, and business-critical or high-throughput workloads get their own set.

Inside those accounts, ephemeral environments are what he calls easily the most impactful practice to come out of serverless. The loop is four steps: `npx sls deploy -s dev-my-feature`, iterate with remocal tests against it, open a PR so CI runs everything, then `npx sls remove -s dev-my-feature`. CI does the same with an environment per commit SHA. Nobody steps on anyone else's toes and shared stages stay free of test data. With usage-based pricing, idle environments cost nothing; serverful pieces such as RDS or OpenSearch should be shared across ephemeral environments rather than recreated.

Two rules stop the environments colliding: don't name resources explicitly unless you must, so CloudFormation adds a random suffix, and when you must, as with EventBridge buses, put the environment name in it.

## Who should watch?

Teams on AWS Lambda whose tests pass locally and fail in the cloud, or who share a single dev stage and keep tripping over each other. Veterans will know the ideas; the layers list is still handy for design reviews.

## Related Conf42 talks

- Yan Cui's [money-saving tips for the frugal serverless developer](https://www.conf42.com/DevOps_2025_Yan_Cui_serverless_saving_tips) at Conf42 DevOps 2025.
- Gunnar Grosch on [chaos engineering for serverless with AWS Fault Injection Simulator](https://www.conf42.com/Chaos_Engineering_2022_Gunnar_Grosch_serverless_aws_fault_injection_simulator) at Conf42 Chaos Engineering 2022.
- Luciano Mammino on [writing Lambdas in Rust](https://www.conf42.com/Cloud_Native_2023_Luciano_Mammino_lambdas_rust) at Conf42 Cloud Native 2023.

[Watch Yan Cui's talk](https://www.conf42.com/Cloud_Native_2024_Yan_Cui_patterns_efficient_serverless), part of [Conf42 Cloud Native 2024](https://www.conf42.com/cloud2024).

## From Lumigo

Lumigo is an observability and troubleshooting platform built for serverless and cloud-native applications.

- [Lumigo website](https://lumigo.io/?utm_source=conf42)

[Watch the talk on YouTube](https://youtu.be/EB_LvpsbwG4).

## Watch the talk

[Patterns for efficient serverless development](https://www.conf42.com/Cloud_Native_2024_Yan_Cui_patterns_efficient_serverless) at Conf42 Cloud Native 2024.
