# Design tokens are platform infrastructure, not a style guide

Conf42 Blog, 2025-08-18, updated 2026-11-09. https://www.conf42.com/blog/platform2025/design-tokens-are-platform-infrastructure

In short: Pallav Laskar of Zscaler argues at Conf42 Platform Engineering 2025 that design tokens belong in build pipelines, with schemas, reviews and versioned releases.

Most design systems die the same way: a beautiful Figma file, a PDF style guide, and fifty hand-copied hex codes that drift apart one pull request at a time. At Conf42 Platform Engineering 2025, Pallav Laskar, Principal Software Engineer at Zscaler (and eleven years at Adobe before that, on Adobe Sign, Acrobat and Adobe Experience Manager), makes the case that the fix is to treat design tokens as infrastructure: versioned, validated, built by a pipeline and shipped to every platform from one source.

It is a short talk, closer to a lightning session than a full hour, and it moves fast. That makes it a good one to send to the frontend lead who keeps saying the design system is just CSS.

## One definition, many outputs

The core idea is a token hierarchy run through a build. Raw values sit at the bottom, global and semantic tokens on top of them, and component tokens at the end. Each layer adds meaning, so a button does not know it is `#0057FF`; it knows it is the primary action colour, and the primary action colour knows which blue that is this quarter.

Tokens live in a source format and a pipeline transforms them into whatever each platform eats: CSS variables for the web, Swift for iOS, Android XML for Android. Laskar's summary is one definition, many outputs. Theming falls out of the same structure: multiple brands, light and dark modes and accessibility-driven themes come from composing token sets, not from copying definitions.

If that sounds like infrastructure as code with nicer colours, that is exactly the point.

## The numbers from Zscaler's Nimbus

The concrete part is Zscaler's own design system, Nimbus. Laskar describes consolidating repositories and moving to tokens, which by his account took about 240 kB off the bundle and improved First Contentful Paint by roughly 18%. Those are web-vitals numbers, which is a nice change from the usual feel-good outcomes of design system talks.

He also summarises a Fortune 500 rollout across seven product lines and three acquisitions, quoting around 40% faster feature development and fully automated WCAG compliance checks. Acquisitions are the interesting detail: three companies' worth of buttons is where hand-maintained style guides go to die.

## Governance is what makes it a platform

The section platform engineers will recognise is governance. Token changes go through schema validation, automated contrast testing guarantees accessibility rules hold, peer approval keeps design and engineering in the loop, and documentation updates itself. Tokens get a formal lifecycle: creation, review, distribution, monitoring and a structured deprecation, so old values can be retired without breaking every app that still references them.

For developers, the before-and-after is the familiar one from any good platform: scattered hard-coded values on one side, type-safe tokens with IDE autocomplete on the other.

## Adoption is the hard part, and he says so

Laskar is candid that rollout is never smooth. Teams resist, legacy systems complicate integration, and governance can look like extra risk. His answer is codemods to migrate existing code, a phased rollout (audit and standards, a foundation repo, a pilot, then scale and automate), schema validation and early proof points. His closing line frames tokens as the API contract between design and development, which is the sentence to steal for your next architecture review.

## Who should watch

Frontend platform teams, design system owners, and anyone running a multi-brand or multi-platform product where the blue has five definitions. If you already ship tokens through Style Dictionary or similar, the governance and deprecation parts are the bits worth your time.

## Related Conf42 talks

- [Scalable Design Systems for High-Performance Analytics Platforms](https://www.conf42.com/Golang_2026_Sonali_Priya_scalable_design_systems) by Sonali Priya, Conf42 Golang 2026
- [Building a Design System in Limited Timeframes](https://www.conf42.com/Machine_Learning_2024_Elena_Shabanova_building_design_system) by Elena Shabanova, Conf42 Machine Learning 2024
- [Closing the Developer Experience Gap of Kubernetes Development](https://www.conf42.com/Kube_Native_2023_Edidiong_Asikpo_closing_developer_experience_gap) by Edidiong Asikpo, Conf42 Kube Native 2023

[Watch Pallav Laskar's talk](https://www.conf42.com/Platform_Engineering_2025_Pallav_Laskar_design_tokens_multi)

[Watch the talk on YouTube](https://youtu.be/GoOk5RQk1aA).

## Watch the talk

[Design Tokens as Platform Infrastructure: Architecting Scalable Multi-Platform Design Systems](https://www.conf42.com/Platform_Engineering_2025_Pallav_Laskar_design_tokens_multi) at Conf42 Platform Engineering 2025.
