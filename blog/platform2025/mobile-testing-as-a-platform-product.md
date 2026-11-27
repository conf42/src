# Mobile Test Infrastructure Should Be a Product, Not a Service

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/mobile-testing-as-a-platform-product

In short: Cognizant's Charanpreet Singh Hora at Conf42 Platform Engineering 2025 on device clouds, GitOps, feature flags and AI test selection for mobile.

Every month brings new iOS and Android releases and new devices, and no QA team can buy all of them. At Conf42 Platform Engineering 2025, Charanpreet Singh Hora, a Senior Manager at Cognizant with over ten years in mobile automation on device clouds such as Perfecto and BrowserStack, argued that mobile testing should be run as an internal platform product: self-service, API-driven, multi-tenant and governed.

It's an overview talk that maps platform engineering practice onto mobile QA. The abstract promises live demos and data from hundreds of enterprises; the recording is a slide walkthrough, so come for the structure rather than a demo.

## Why siloed QA can't keep up

The problem is combinatorial. Diverse OS versions, native and web apps, a wide spread of screen sizes, varying network conditions, and continuous delivery on top. Siloed QA teams with manually managed devices can't keep pace. The platform answer is devices on demand and testing as a capability teams consume through an API.

## The foundations look like any other platform

Charanpreet's architecture will be familiar to cloud teams:

- **Infrastructure as code** with Terraform across AWS, Azure and Google Cloud, with Kubernetes running isolated test containers, so test environments stop drifting.
- **GitOps** for test configuration, automation scripts and infrastructure definitions, with peer review, staging first and progressive rollout of new testing capabilities.
- **Multi-tenancy** with a namespace, resource quota and access controls per team, network segmentation for sensitive test data, and role-based access tied to the enterprise directory, denied by default.

## Run fewer tests, smarter

The AI section focuses on two practical ideas. Predictive models use historical test patterns, release schedules and seasonal traffic to provision device capacity before a crunch and release it in quiet periods. Intelligent test selection picks the minimum suite needed to validate a specific change, so critical flows get tested without running everything on every device.

Compatibility testing goes past functional checks into performance, accessibility and visual regression across device sizes. Device clouds let you pick real devices by region: if your customers are in Australia, test from Australian devices and see their latency.

## Testing doesn't stop at release

The progressive delivery section ties testing to production. Feature flags roll a change to a small percentage of Android or iOS users and widen over weeks. Canary analysis compares control and experiment groups for performance regressions, crash rates and UX degradation. Automated rollback triggers revert a bad change when metrics slip. In other words, the release is the last test stage, and it should have a kill switch.

Industry examples cover financial services (PCI DSS and SOX checks automated as policy as code, generating audit evidence) and e-commerce (traffic simulation of browse, search, cart and checkout journeys, performance budgets that block regressions, and test environments scaled to production load ahead of peaks like Thanksgiving).

## Observability and governance for the test platform itself

The platform needs its own SLOs and error budgets, distributed tracing through test workflows to find bottlenecks, and governance that balances developer autonomy with control: admission policies, resource quotas, budget alerts and regular policy reviews. Developer experience gets REST and GraphQL APIs, SDKs and interactive docs. Future directions include 5G and edge testing and carbon-aware scheduling of heavy test runs.

## Who should watch

QA leads and mobile platform teams planning a move from a device drawer and a shared spreadsheet to a self-service test platform. Experienced platform engineers will know the patterns; the value is seeing them applied to mobile.

## Related Conf42 talks

- [Jaspreet Kumar on chaos engineering in mobile apps](https://www.conf42.com/Chaos_Engineering_2025_Jaspreet_Kumar_mobile_apps).
- [Pranjal Deo: Engineering Reliable Mobile Applications](https://www.conf42.com/Site_Reliability_Engineering_2021_Pranjal_Deo_reliable_mobile_applications).

[Watch Charanpreet Singh Hora's talk](https://www.conf42.com/Platform_Engineering_2025_Charanpreet_Singh_Hora_testing_ecosystems_mobile)

[Watch the talk on YouTube](https://youtu.be/TxmU2ElaWK4).

## Watch the talk

[Platform-First Mobile Automation: Engineering Resilient Testing Infrastructure Across Enterprise Ecosystems](https://www.conf42.com/Platform_Engineering_2025_Charanpreet_Singh_Hora_testing_ecosystems_mobile) at Conf42 Platform Engineering 2025.
