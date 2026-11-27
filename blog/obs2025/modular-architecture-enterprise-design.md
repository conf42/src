# Modular architecture is a boundary problem before a tooling one

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/modular-architecture-enterprise-design

In short: Wayfair engineer Anusha Reddy Guntakandla lays out modular architecture at Conf42 Observability 2025, from encapsulation to modular monoliths and incremental migration.

If your order module also sends customer notifications, you don't have modules, you have folders. At Conf42 Observability 2025, Anusha Reddy Guntakandla, Software Engineer at Wayfair, gave a compact tour of modular architecture for enterprise platforms: how to draw module boundaries, which implementation path fits which team, and why the migration should happen one module at a time. It's a short, survey-style talk, best treated as a checklist rather than a war story.

## A module owns a business capability

Guntakandla's definition is the useful starting point: a large application broken into discrete, self-contained modules, each covering one business capability and talking to others through stable interfaces, APIs or message brokers. Think of each module as a bounded context in domain-driven design terms. It owns its own logic and can evolve, build, deploy and scale independently, which also shrinks the blast radius of any one change in CI/CD.

The four traits she lists are textbook but well illustrated:

- **Encapsulation**: a customer module exposes a profile API and hides how it aggregates loyalty points.
- **High cohesion**: everything in a module serves one purpose (hence the order module that shouldn't send notifications).
- **Loose coupling**: asynchronous messages or stable contracts, which nudges you towards event-driven designs.
- **Interface stability**: REST, GraphQL or gRPC contracts kept backward compatible with OpenAPI or protobuf schemas.

## Fault isolation is the design goal you'll feel

Of the design principles, two stand out. Scalability by design: a payments module can scale three times as far as a mostly static help centre module, so you pay for capacity where the load is. And fault isolation: if the inventory service fails, checkout should still proceed on estimated quantities or cached data. That one sentence is a better argument for modularity than most architecture diagrams.

Maintainability gets a concrete example too: refactoring one module from PHP to Node.js without touching the rest.

## Three ways to get there

The talk compares three implementation paths. Microservices give each service its own codebase, database and pipeline, and suit domains with strong service boundaries. A modular monolith is a single deployable unit organised internally as modules, which she recommends for early-stage teams or when deployment overhead needs to stay low, with the option to split later. Plugin architectures, common in CMS and e-commerce engines, load features at runtime. Her advice is to choose with a decision matrix based on deployment frequency, team size and service criticality.

The illustrative e-commerce case reports a product catalogue moved to a standalone Elasticsearch-backed service with 47% faster queries, a CQRS-based order module with retries and circuit breakers, and a plug-in recommendation engine credited with a 15% lift in product discovery.

## The costs are real, so migrate incrementally

Guntakandla doesn't oversell it. Defining boundaries, contracts and pipelines takes effort up front; too many chatty services add latency (bulkheads, caching, batching and connection pooling help); and without clear ownership, teams re-couple modules by accident, which is where tools like Backstage or Compass come in. Her adoption rules: start with domain modelling (event storming, context maps), govern interfaces with registries and contract testing, and never big-bang. Extract one module, define KPIs, validate, then move on.

## Who should watch

Engineers about to propose breaking up a monolith who want a tidy vocabulary and a list of trade-offs to put in the design doc. It's a 101-to-201 overview without code, so senior architects will recognise most of it. The modular-monolith-first advice is the bit worth repeating in meetings.

## Related Conf42 talks

- Victor Lyuboslavsky on [Modularizing a 10-Year Monolith: The Architecture, The People, and the Pain](https://www.conf42.com/Golang_2026_Victor_Lyuboslavsky_modularizing_year_monolith), the war story this talk doesn't tell.
- Rajani Jayantha on [a decision framework for microservices vs. monolith](https://www.conf42.com/Platform_Engineering_2025_Rajani_Jayantha_monolith_microservices_decision).
- Swetha Lakkaraju on [Decoupling Legacy Banking: Modular Core Strategies for Speed, Scale, and Innovation](https://www.conf42.com/Internet_of_Things_IoT_2025_Swetha_Lakkaraju_banking_modular_modernization).

[Watch Anusha Reddy Guntakandla's talk](https://www.conf42.com/Observability_2025_Anusha_Reddy_Guntakandla_modular_agility_application)

[Watch the talk on YouTube](https://youtu.be/xH5HOI4oSRU).

## Watch the talk

[Modular Architecture: Enhancing Agility and Efficiency in Enterprise Application Design](https://www.conf42.com/Observability_2025_Anusha_Reddy_Guntakandla_modular_agility_application) at Conf42 Observability 2025.
