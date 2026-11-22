# Pick monolith or microservices by team maturity, not hype

Conf42 Blog, 2025-08-06, updated 2026-11-09. https://www.conf42.com/blog/platform2025/microservices-vs-monolith-decision-framework

In short: Rajani Jayantha of Wayfair at Conf42 Platform Engineering 2025 gives a decision framework for monolith vs microservices, plus a real routing migration.

The monolith versus microservices argument usually starts with a conference talk from a company ten times your size. At Conf42 Platform Engineering 2025, Rajani Jayantha, Senior Engineer at Wayfair with over 15 years in the industry, offered a decision framework that starts somewhere less glamorous: your team's maturity, your culture and your cloud platform. Her headline advice is that context matters more than trends.

## Both sides, fairly

The talk earns its framework by treating both architectures honestly. Microservices give independent scaling, deployment flexibility, contained failures and freedom to pick a tech stack per service, and she cites studies claiming 30 to 40% cost savings from scaling efficiency and deployment frequency five to ten times higher. The bill: every service call adds network latency, you need service discovery, API versioning, circuit breakers and retries, distributed transactions need eventual consistency and sagas, and the observability burden grows with every service. Without Kubernetes, independent CI/CD pipelines and distributed tracing in place, she argues, the promised benefits never arrive.

The monolith gets a better hearing than it usually does. A single codebase means faster onboarding, simpler debugging and testing, and in-process calls that are far faster than network hops. It shines for MVPs and prototypes, small teams with unclear domain boundaries, predictable workloads, and strong consistency needs like financial transactions. It struggles as it grows: over-provisioning, and development speed that slows year on year in a large codebase.

## The framework: people first

The decision starts with organisational readiness. A monolith fits teams under about 20 developers with basic CI/CD and limited cloud experience; microservices tend to need 50 or more developers with advanced automation and distributed systems skills. Cultural signals matter as much as headcount: is ownership centralised or distributed, is communication synchronous or async, is the organisation conservative or experimental, does it actually learn?

Then come the technical requirements: number of business domains, integration points, consistency needs, realistic growth and traffic projections (she warns against optimistic forecasts built on thin data), and cloud platform capabilities from container orchestration and service meshes to managed databases. If the platform cannot support microservices at scale, the architecture will struggle however nice the diagram looks.

## Architecture as a journey

Rajani's recommended path avoids the big-bang rewrite: start with a modular monolith, use domain-driven design to find service boundaries, extract services gradually with the strangler fig pattern, and build observability, automation and CI/CD alongside. Her rough timelines: 18 to 24 months for a full microservices migration, six to 12 months to optimise a monolith while keeping options open.

## The routing service that earned its split

The real-world example is a monolithic routing application that made scaling hard and turned deployments into a bottleneck, with a team mature enough to take on microservices. They decoupled routing into modular services, built reusable libraries and plugins, recorded decisions in architecture decision records, and added service auto-wiring and shared utilities such as feature toggles, caching and logging. The reported results: deployments three times faster, code-to-production speed up 21 times, uptime up 8.5%, mean time to recovery halved, and a system handling tens of millions of contacts per month.

She closes by noting the choice is no longer binary: serverless, modular monoliths and ML-assisted decomposition all sit between the poles, and hybrids often win. Business value, in her view, decides the architecture, and the most elegant design is worthless if it serves no business goal.

## Who should watch

Tech leads facing a decomposition decision, and anyone who needs a structured way to push back when a planning meeting decides microservices are the answer before asking the question. Teams already deep into service meshes will find the first half familiar; stay for the readiness criteria and the migration numbers.

## Related Conf42 talks

- [Hareesh Iyer on moving monoliths to microservices in a phased approach](https://www.conf42.com/Cloud_Native_2024_Hareesh_Iyer_modernize_monoliths_microservices) at Conf42 Cloud Native 2024.
- [Victor Lyuboslavsky on modularizing a 10-year monolith](https://www.conf42.com/Golang_2026_Victor_Lyuboslavsky_modularizing_year_monolith) at Conf42 Golang 2026.
- [Daniil Koshelev on transitions from monolith to microservices](https://www.conf42.com/DevSecOps_2024_Daniil_Koshelev_monolith_microservices_transitions) at Conf42 DevSecOps 2024.

[Watch Rajani Jayantha's talk](https://www.conf42.com/Platform_Engineering_2025_Rajani_Jayantha_monolith_microservices_decision), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/dx0kQ4c8dp8).

## Watch the talk

[Platform Engineering Decision Framework: Microservices vs. Monolith for Scalable Cloud Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Rajani_Jayantha_monolith_microservices_decision) at Conf42 Platform Engineering 2025.
