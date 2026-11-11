# T-Mobile treats the T-Life app shell as an internal platform

Conf42 Blog, 2026-10-22, updated 2026-11-09. https://www.conf42.com/blog/platform2026/t-mobile-t-life-app-shell-as-platform

In short: RanjithKumar Ragavan (T-Mobile) at Conf42 Platform Engineering 2026 on how five teams ship into one 53-million-user mobile app without breaking each other.

In the backend, giving five teams independence means five repos and five deploys. In a mobile app, Apple and Google take exactly one binary, so everyone compiles, links and ships together. At Conf42 Platform Engineering 2026, RanjithKumar Ragavan, Member of Technical Staff leading mobile architecture for T-Mobile's T-Life app, showed how his team turned that single binary into a self-service internal platform for five engineering pods and 50-plus mobile engineers.

The numbers set the stakes: T-Life serves 53 million active users, millions open it at once on T-Mobile Tuesdays to claim rewards, and the team holds itself to a crash-free session rate above 99.9%.

## One super app, five teams, one junk drawer

T-Life replaced a set of separate apps (bill pay, rewards, home internet) with one. Customers liked it. Engineering inherited one binary, five teams and nothing between them. The loyalty team imported account internals to check login; IoT reached straight into payment code; shared folders became a place where everyone dumped helper classes. A change to one shared file in payments broke compilation for loyalty, and one broken test could block every engineer at the same time.

The organisational fix came first. Four feature pods (account, payments, loyalty, IoT) serve customers. The fifth, the core shell pod, owns navigation, dependency injection, analytics and other infrastructure, and its customers are the other four teams. The shell holds no business logic; its job is to be a stable foundation that features plug into.

## Contracts small enough to compile in a second

The central mechanism is versioned interface contracts. Every team splits its module into a tiny contract module (interfaces and data models only, no UI, no database) and a private implementation. The rule: depend on other teams' contract modules, never on their implementations. Contracts use semantic versioning. A non-breaking addition is a minor bump nobody notices; a breaking change means deprecating the old method, shipping a new contract version and giving consumers time to move. Behind the contract, a team can rewrite internals or redesign screens without telling anyone.

That separation makes isolated builds possible. When a payments PR lands, CI compiles only payments against the prebuilt contracts, runs its unit and UI tests and quality checks, then passes a gate that also verifies the public contract wasn't accidentally broken. Only then is the new version promoted into app integration. If payments fails the gate, the others keep shipping on the last good payments version. Ranjith reports zero cross-team build regressions across all five pods, and feedback in a couple of minutes instead of waiting on a monolith build.

## Plug, don't wire

Features join the app through modular feature injection, which he compares to a wall socket: the electrician doesn't need to know whether you'll plug in a kettle or a TV. Each feature module ships a registration file declaring its screens, deep links and the platform services it needs. At startup the shell scans the registry and connects features at runtime. When a user taps "pay bill" on home, the home screen asks the shell to open a route; it knows nothing about payment code. Teams register, wrap the feature in a remote flag and release on their own schedule, without waiting for the shell team.

## Governance by linter, state by event bus

Two risks remain when teams move fast: someone bypasses the rules under a deadline, or modules corrupt each other at runtime. For the first, no review board. Changes inside your own module need zero outside approvals; changing a shared public contract needs a short RFC; an automated lint rule fails the pull request if loyalty imports payment's private code; and an ADR log in the repo records why each rule exists.

For runtime, each module uses MVI or MVVM with one-directional state flow. Modules never call each other directly: on logout, account publishes an event to a shared bus and every module clears its own data. State is scoped to a module's lifecycle, so closing the IoT screens frees IoT's memory. Ranjith ties that hygiene directly to keeping the crash-free rate.

## Who should watch

Mobile architects on any app with more than two teams in one codebase, and backend platform engineers who want to see contracts, isolated pipelines and self-service land in a world with a single deployable. It's architecture and process rather than code, delivered with plenty of slide metaphors.

## Related Conf42 talks

- [Building Reliable AI-Driven Mobile Platforms for Healthcare and Commerce](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Dipta_Rakshit_building_reliable_driven) by Dipta Rakshit (Walmart Global Tech)
- [Git submodules: we have monorepo at home](https://www.conf42.com/JavaScript_2023_Vadim_Tsaregorodtsev_git_submodules_monorepo) by Vadim Tsaregorodtsev (Emerging Travel Group)
- [Modular Architecture: Enhancing Agility and Efficiency in Enterprise Application Design](https://www.conf42.com/Observability_2025_Anusha_Reddy_Guntakandla_modular_agility_application) by Anusha Reddy Guntakandla (Wayfair)

[Watch RanjithKumar's talk](https://www.conf42.com/Platform_Engineering_2026_RanjithKumar_Ragavan_mobile_teams_app)

[Watch the talk on YouTube](https://youtu.be/aoLaOOL-tys).

## Watch the talk

[Mobile as a Platform: How Five Autonomous Teams Ship into One 53-Million-User App](https://www.conf42.com/Platform_Engineering_2026_RanjithKumar_Ragavan_mobile_teams_app) at Conf42 Platform Engineering 2026.
