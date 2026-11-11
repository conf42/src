# Microservices can share code, if the coupling is the point

Conf42 Blog, 2023-01-25. https://www.conf42.com/devops2023/service-chassis-appropriate-coupling-reuse

In short: Travis Gosselin (SPS Commerce) at Conf42 DevOps 2023 on when microservices should share code, the rule of three, and service templates and chassis

Prefer duplication to coupling is the microservices rule everyone quotes, right up to the day a standard header change has to land in dozens of services that copy-pasted the same code. Travis Gosselin, Principal Software Engineer for Developer Experience at [SPS Commerce](https://www.spscommerce.com/about/), argued at Conf42 DevOps 2023 that the no-sharing rule is half myth: some coupling is exactly what you want, and service templates and a service chassis are how SPS Commerce ships it.

## Why is code reuse harder in microservices?

Inside one project, reuse is easy: extract a function, then a module. Distribute it across services and costs pile up: long dependency chains, ownership and administration, roadmap politics, multiple active releases, flaws multiplied across every consumer, and polyglot services that cannot consume a .NET package at all. When friction gets bad enough, a team forks the library and now there are two of them.

He quotes Building Evolutionary Architectures on both sides: microservices prefer duplication to coupling, but code reuse can be an asset as well as a liability, as long as the coupling points don't conflict with other goals of the architecture.

## What happens when you get reuse wrong?

His war story is an S3 multipart upload for .NET. It looked perfect for a shared package: an identified need in two services with more to come, low-level code full of chunking, streams and buffer resets, error prone and hard to test against anything but a local mock. Then it grew. The upload became a cloud package with its own roadmap, which became a proprietary library that required a download service and a download config object just to call S3. It was pinned to one AWS SDK major version, and loading versions 2 and 3 of the same SDK in one .NET app domain is painful. The payoff was about 100 saved lines of code, which he calls a good sign that this wasn't the way to go.

## When should you reuse?

His checklist:

- **Emerging need** is not enough on its own, and depends on the organisation's maturity.
- **High duplication**, by the rule of three: at least three real copies in production, not planned ones, so you can see the actual contract.
- **High complexity, high risk or high change frequency**, where duplicating costs more than sharing.
- **Low coupling on the architectural dimensions you care about**, and **best practices and principles**: authentication and authorisation, logging and monitoring opinions, HTTP client SDKs, error handling and validation, serialisation.

At SPS Commerce that means shared packages for errors, identity, structured logging, serialisation (not just camelCase versus snake_case, but enums and nulls) and an opinionated AWS Secrets Manager format across accounts.

## What is appropriate coupling?

Coupling that buys more than it costs. A consistent log format couples services, and in return operators get reusable dashboards. A shared feature flag library couples flag keys and user context, and in return flag cleanup and targeting work the same everywhere. His analogy is traditional animation in The Lion King: the background is drawn once and reused, the animals in the foreground are redrawn for every frame. Cross-cutting concerns are the background.

What not to share: the grab-bag utility library, which he likens to one book covering both Kraft Dinner in the microwave and building custom furniture. Keep those as snippets.

## Seeds, templates, chassis

Templating groups packages into an opinion for a whole project, in three levels:

- **Project seed**: folder structure, workflow files, CODEOWNERS, a Dependabot config, a README. Cheap, but a copy.
- **Service template**: an opinionated starting point per language with security, external config, logging, health checks, metrics and tracing. Valuable, but its cost grows as copies drift.
- **Service chassis**: the same concerns delivered as referenced packages, so a template only bootstraps and updates flow to every service.

He also names the service mesh gap: Istio-style meshes give you mTLS, tracing, egress and metrics for free, but errors, auth context and logging format still need code, and that is the chassis's job. Distribution relies on Dependabot opening upgrade pull requests (private feeds included), because teams otherwise upgrade only on install, on a vulnerability, or when they need a feature.

The SPS chassis, from what he shows, covers error formats, health checks with Kubernetes probes, identity, structured JSON logs, AWS SSM Parameter Store and Secrets Manager, tracing via AWS X-Ray and OpenTelemetry, Sentry, serialisation and security middleware. Every feature can be switched off: "everything is configurable and ejectable, meaning that you have an escape hatch at every point," Travis Gosselin said at Conf42 DevOps 2023.

His closing advice: if a full chassis is a mile-high order, build one package, reference it from your template and grow from small successes.

## Who should watch

Platform and developer-experience teams deciding what belongs in an internal framework, and architects who need words for why some coupling is fine.

## Related Conf42 talks

- Travis Gosselin on [CI/CD efficiency with templates in Azure](https://www.conf42.com/DevOps_2024_Travis_Gosselin_cicd_efficiency_templates_azure) at Conf42 DevOps 2024.
- Edidiong Asikpo on [closing the developer experience gap](https://www.conf42.com/Kube_Native_2023_Edidiong_Asikpo_closing_developer_experience_gap) at Conf42 Kube Native 2023.
- Vadim Tsaregorodtsev on [git submodules versus a monorepo](https://www.conf42.com/JavaScript_2023_Vadim_Tsaregorodtsev_git_submodules_monorepo) at Conf42 JavaScript 2023.

[Watch Travis Gosselin's talk](https://www.conf42.com/DevOps_2023_Travis_Gosselin_compelling_codecreuse_enterprise)

## From SPS Commerce

SPS Commerce runs a retail network that connects retailers, suppliers and logistics partners for order and supply chain data.

- [About SPS Commerce](https://www.spscommerce.com/about/)

[Watch the talk on YouTube](https://youtu.be/s3SHHKMgRWc).

## Watch the talk

[Compelling Code Reuse in the Enterprise](https://www.conf42.com/DevOps_2023_Travis_Gosselin_compelling_codecreuse_enterprise) at Conf42 DevOps 2023.
