# Modularizing an 800,000-line Go monolith is mostly a people problem

Conf42 Blog, 2026-05-11, updated 2026-11-09. https://www.conf42.com/blog/golang2026/modular-monolith-fleet-people-first

In short: Victor Lyuboslavsky of Fleet Device Management at Conf42 Golang 2026 on a failed first attempt, a pilot bounded context and the Go tools that enforce it.

It started with a 30-second test recompile on a single Go package. At Conf42 Golang 2026, Victor Lyuboslavsky, Principal Software Engineer at Fleet Device Management, told the story of moving Fleet's ten-year-old, roughly 800,000-line open source Go backend toward a modular monolith, including the first attempt that went sideways and the pilot that worked.

This is the rare architecture talk that spends as much time on pull requests nobody would review as on package diagrams, and it is better for it.

## Thirty seconds is the worst possible wait

Victor's opening diagnosis is precise. The service package was Fleet's biggest compile unit, and while Go compiles fast, linking still runs largely in series, so a huge package with many dependencies made every test recompile crawl. Thirty seconds is too long to ignore and too short to switch tasks, so it just breaks your train of thought. He also points out that AI agents do not fix this: they run the test loop far more often than humans, so slow tests slow them down even more.

## Attempt one: right idea, no buy-in

The first plan was a vertical slice for a new feature, Android MDM, mirroring the legacy structure so engineers would know where things live, with its own API and persistence layers and even a second MySQL schema. The pull request sat unreviewed despite a 24-hour review norm. Engineers felt surprised and unheard. Victor unsplit the database, and when a new ADR process arrived, the API split was approved while the persistence split was rejected as risky, confusing and too big at once.

Then delivery pressure did the rest. With no architectural oversight, the Android code seeped back into the legacy code. Some wins survived (separate Android controllers, some shared code pulled out of the service package), but the lessons are the point:

- Consensus takes real time, and early voices are not everyone's voice; ask in one-on-ones.
- Words matter. He meant architectural modules; half the room heard Go modules.
- Architecture changes slipped into feature PRs moved; standalone architecture PRs stalled. His summary: "If you don't define how your architecture is allowed to change, it changes anyway, and often it changes behind your back."
- Every endpoint needs an owner, even if it is just glue.

## Attempt two: borrow authority, start tiny

Finding no large open source Go project that had done this, Victor pointed to GitLab's documented choice of a modular monolith over microservices for its Rails codebase. That shifted the burden of proof from a crazy idea to a proven pattern. The team agreed on bounded contexts and picked the most self-contained one as a pilot: activity and audit, the record of things that already happened. The ADR stayed open for about four weeks, every related PR was reviewed by the four product-group tech leads, and a central page tracked progress. As he put it, "Surprises are great for birthdays, not for architecture."

The design rules: each context owns its controller, service and persistence layers; other contexts may call its public service API but never touch its tables; auth is injected, not owned; one shared MySQL schema stays, because the pain was ownership, not database load, and splitting a database freezes boundaries you are still learning. Cross-context calls go through small contracts owned by the provider, and legacy access goes through an anti-corruption layer outside the context.

## The glue code was the monolith

A hello-world scaffold for the new context pulled in half the codebase through utility packages and a god package where unplaced types went to live. So before modularizing the domain, they had to build a platform layer for HTTP helpers, database wiring and middleware without domain assumptions.

What made the boundary real in Go:

- An `internal` directory, so the compiler rejects outside imports. No code review rule required.
- A single `bootstrap.New` composition root for production and tests.
- The ACL interface as a coupling meter: fewer methods, less legacy dependency.
- A dedicated CI workflow for the context, which also trimmed the main suite.
- Architecture tests with per-context import allow lists, the fitness functions from Building Evolutionary Architectures, catching humans and AI agents alike.

Extracting the context surfaced old bugs, including an RBAC rule the code violated despite Fleet's public docs, and a cancelled operation that could delete past activity records. Next up are user and certificate management, which sit much closer to the centre.

## Who should watch

Anyone with a large Go codebase arguing about microservices versus just cleaning it up, and tech leads who need to sell structural work to a team shipping features. Victor's closing line is the thesis: "Modularization isn't really about modules. It's about respecting the limits of human attention."

## Related Conf42 talks

- [Rajani Jayantha on the monolith versus microservices decision](https://www.conf42.com/Platform_Engineering_2025_Rajani_Jayantha_monolith_microservices_decision) at Conf42 Platform Engineering 2025
- [Hareesh Iyer on modernizing monoliths](https://www.conf42.com/Cloud_Native_2024_Hareesh_Iyer_modernize_monoliths_microservices) at Conf42 Cloud Native 2024

[Watch Victor Lyuboslavsky's talk](https://www.conf42.com/Golang_2026_Victor_Lyuboslavsky_modularizing_year_monolith)

[Watch the talk on YouTube](https://youtu.be/RHrPkuTbIVw).

## Watch the talk

[Modularizing a 10-Year Monolith: The Architecture, The People, and the Pain](https://www.conf42.com/Golang_2026_Victor_Lyuboslavsky_modularizing_year_monolith) at Conf42 Golang 2026.
