# Frontend latency is a reliability problem; Galileo moved work server-side

Conf42 Blog, 2026-02-22, updated 2026-11-09. https://www.conf42.com/blog/sre2026/frontend-latency-is-an-sre-problem

In short: Murali Varma of Galileo Financial Technologies at Conf42 SRE 2026 on server components, streaming SSR and Turbopack as reliability tools for B2B web apps.

Most SRE teams stop caring at the load balancer. At Conf42 Site Reliability Engineering 2026, Murali Varma, Senior Staff Software Engineer at Galileo Financial Technologies (part of SoFi), made the case that the browser belongs in scope too, and showed what happened when Galileo treated frontend latency as an operational reliability problem: a 60% smaller JavaScript bundle, 45% faster initial page loads and server response times cut from 300 ms to 150 ms.

## Users who can't leave still pay for slow pages

The industry statistic he opens with is well known: 53% of users abandon an app that takes more than three seconds to load, rising to 71% beyond four. Galileo's twist is that its users can't abandon anything. Galileo builds B2B operational platforms for more than 200 enterprise clients, used all day by customer service agents and relationship managers.

That makes slowness worse, not better, because the damage is silent and cumulative. Every extra second multiplies across hundreds of agents and thousands of interactions a day: longer handle times, more errors under time pressure, fatigue over eight-hour sessions, and extra API pressure and compute spend across a multi-tenant environment. It just doesn't show up on the dashboard anyone is watching.

## Variance was the real killer

The legacy stack was a classic single-page application: download the full bundle, render everything client-side, call the APIs after hydration, and only then show something meaningful. Bundles ran two to three megabytes, first contentful paint hit three to four seconds on constrained networks, and the cache hit rate sat around 65%.

Varma's sharpest point is about the spread, not the average. On degraded networks, client-heavy rendering collapsed unpredictably, and you cannot set a reliable SLO against that kind of variance. His principle for fixing it is very SRE: move computation off infrastructure you don't control, the user's browser, and onto infrastructure you do.

## Three ways to move the work

**Server components.** Business logic that used to run in the browser now runs on the server, and only minimal serialized UI payloads reach the client. Hydration becomes surgical instead of wholesale, which cuts client CPU and memory and makes behaviour more stable across the mixed corporate hardware agents actually use.

**Streaming SSR.** Instead of waiting for the whole page to be computed, the server sends HTML progressively, decoupling time to first byte from time to interactive. For SREs, he stresses, the win is predictability: lower variance is what makes a meaningful SLO possible. Galileo measured a 42% improvement in time to first meaningful paint and 45% faster initial loads across production routes.

**Hybrid rendering.** Different content gets different modes: static generation where data is stable (cache-friendly and close to failure-proof), server components for dynamic, personalized data, and client JavaScript only for genuinely interactive elements.

## The build system is part of the blast radius

The section people usually skip is build tooling. Legacy tooling was a hidden constraint on evolving the architecture, so Galileo introduced Rust-based Turbopack, with a 10x improvement in cold-start build speed. The SRE link is direct: faster builds mean shorter feedback loops and faster rollbacks, and better tree shaking means smaller payloads, so a bad deploy ships less code.

Across production, cache hit rate went from 65% to 89%. The organisational effects in the abstract are a 35% reduction in time to market and a 47% increase in developer productivity, plus fewer rollbacks. The talk notes that the production metrics came from Galileo's own monitoring and observability systems.

## Who should watch

SREs whose SLOs end at the API gateway, and frontend leads trying to get infrastructure budget for a rendering rewrite, both get ammunition here. It's framework-level rather than a code walkthrough, and the stack is the React Server Components and Next.js ecosystem, so teams on other frameworks will need to translate. His three closing principles: frontend reliability belongs in SRE, server-centric architecture scales, and performance engineering starts at the architecture layer, not with band-aids on top.

## Related Conf42 talks

- [Glorious Monolith: Scaling an application without microfrontends](https://www.conf42.com/JavaScript_2023_Maksim_Zemskov_glorious_monolith_scaling_application_microfrontends) by Maksim Zemskov.
- [JavaScript Micro Frontends: Fast-Track AI Integration for Modern Web Apps](https://www.conf42.com/JavaScript_2025_Linga_Annela_micro_frontends_fast) by Linga Annela.
- [Building Guardrails for AI-Generated Frontends: A Platform Engineering Approach](https://www.conf42.com/Platform_Engineering_2026_Niharika_P_Pujari_guardrails_frontends_generated) by Niharika P Pujari.

[Watch Murali Varma's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Murali_Varma_driven_frontend_architecture) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/zgRrNSVfC0g).

## Watch the talk

[SRE Driven Frontend Architecture for High Performance and Reliable Web Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Murali_Varma_driven_frontend_architecture) at Conf42 Site Reliability Engineering (SRE) 2026.
