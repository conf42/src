# An observability passport for every frontend project

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/observability-passport-for-frontend-apps

In short: Vadim Tsaregorodtsev of ETG at Conf42 Observability 2025 on one page of links per app covering Sentry, SLOs, error budgets, logs and traces.

Vadim Tsaregorodtsev's team once restarted a broken service, found nothing in Sentry, and only later learned the cause was another team's release: their CPU usage jumped and dragged his product down through a shared integration layer. At Conf42 Observability 2025, Vadim, who leads a frontend team at ETG, presented his answer to the question of how you know a product works, and works properly: an observability passport, a single page per project that links every signal you need.

It is a refreshingly practical talk from the frontend side of the house, where observability content is thinner than it should be.

## Works, and works properly, are two questions

The talk splits the question in two. Knowing that the app works is monitoring: requests go through, no errors, an alert fires if load climbs. Knowing that it works properly is observability: being able to explain why the system behaves as it does, such as knowing that load rises after launch time and that is a bad window to release. Monitoring tells you something broke; observability helps you figure out why.

When his team launched a new car rental product for B2B partners and corporate clients, Vadim used it as the chance to build this properly rather than waiting for support to say everything is broken.

## Metrics, sorted by who cares about them

Vadim sorts metrics into technical (CPU, RAM, response time), business (conversion, retention, revenue per user) and hybrid metrics that matter to both, with Google's Web Vitals as the prime example: page load speed is technical, but it shapes user experience and search ranking, which hits the business.

He then gives one of the clearer explanations of SLA, SLO and SLI you will hear in a frontend talk. The SLA formalises business expectations; the SLO is the internal target, such as API response time under 200 ms for 95% of requests; the SLI is the measured share of requests that actually met it. The error budget sits on top: at a 99.9% target, the budget is 0.1%, and when it is nearly gone, feature work freezes and the team fixes reliability. He pitches it as a sprint planning tool and a way to tell the business, in its own language, why a risky feature can wait.

## What goes in the passport

The passport began as a Confluence page of links. Over the talk it fills up:

- **Error tracking** with Sentry (or anything that tells you what went wrong and how to fix it).
- **Vulnerability analysis** with DefectDojo, where the team set an SLO of zero critical vulnerabilities in production and seven days to fix found ones, which he notes is the tool's default.
- **Basic metrics** such as memory and CPU, exported via a Prometheus client package.
- **Logs**, plus **traces** for the cases where one component's logs cannot explain a failure; request IDs tie events together, and OpenTelemetry with Jaeger draws the graph.
- **Profiling** in Sentry to find the slowest endpoints and pages.
- **Product analytics**, which caught real bugs: a currency switcher firing an extra event, and an event meant for the listing page firing on the booking page because of a cache issue.
- **The availability SLA, test coverage and the Swagger docs** for other services.

## A repeatable recipe

Whatever the tool, Vadim reduces each passport entry to the same steps: pick the area to watch, define what counts as deviation, set an error budget, collect the data, visualise it, add alerts where needed, and assign owners with a response protocol. That recipe travels well beyond frontends.

## Who should watch

Frontend leads who own production apps and want a cheap, concrete way to make their reliability visible to the team and the business. Backend SREs will find the SLO material familiar, but the passport idea and the product-analytics examples are worth stealing.

## Related Conf42 talks

- Joe Blubaugh's [Don't get out of bed for anything less than an SLO](https://www.conf42.com/DevOps_2023_Joe_Blubaugh_bed_less_slo) takes the SLO argument into on-call.
- Sumit Kaul's [Observability as a Platform Contract](https://www.conf42.com/DevOps_2026_Sumit_Kaul_slos_instrumentation_observability) enforces SLOs in CI/CD.
- Michael Haberman's [Distributed tracing for Node.js using OpenTelemetry](https://www.conf42.com/JavaScript_2021_Michael_Haberman_distributed_tracing_OpenTelemetry) for the tracing entry in the passport.

[Watch Vadim Tsaregorodtsev's talk](https://www.conf42.com/Observability_2025_Vadim_Tsaregorodtsev_passport_frontend_navigating)

[Watch the talk on YouTube](https://youtu.be/RFLefwDBR4Y).

## Watch the talk

[Observability Passport: Navigating the What, Where, and When of Your Frontend App](https://www.conf42.com/Observability_2025_Vadim_Tsaregorodtsev_passport_frontend_navigating) at Conf42 Observability 2025.
