# XZ Utils passed CI, so ask what your green checkmarks miss

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/what-green-ci-cannot-catch

In short: Tilda Udufo of Outreachy at Conf42 DevOps 2026 on what CI/CD cannot catch, from the XZ Utils backdoor to rubber-stamp reviews, plus a pre-merge risk checklist.

The XZ Utils backdoor had passing tests, reviewed code and a green pipeline. It was caught because Andres Freund noticed SSH logins taking a few hundred milliseconds too long. At Conf42 DevOps 2026, Tilda Udufo, a software engineer and program organiser at Outreachy who has coordinated code review across open source projects with hundreds of contributors, used that story to argue that CI/CD is necessary but not sufficient, and to show what has to sit next to it.

She is clear that this is not an anti-automation talk. She calls CI/CD one of the best things to happen to software engineering in two decades. The point is to stop treating "it passed" as "it is safe".

## What actually failed in XZ

Tilda's retelling focuses on the human system. A contributor appeared in 2021 with genuinely useful work, earned commit access and became a maintainer over the next two years, and the backdoor surfaced in 2024. The enabling conditions were an overloaded, stretched maintainer, incremental changes that each looked harmless, a long-trusted contributor with real influence, and automation that could not see any of the social dynamics. Automation checks code quality; humans are supposed to check intent.

## The question CI answers, and the one it does not

Her framing is precise. CI/CD answers one question very well: does this code meet the rules we defined? It does not answer whether the change is safe in the real world. Her list of things outside its scope by design:

- social engineering, including a trusted contributor whose motives change while their access does not
- performance regressions that only appear on production-sized data
- integration behaviour across downstream services
- features that work to spec but break users' mental model
- transitive dependencies your scanner does not check
- configuration that is harmless in staging and leaks memory under real load

Why do we over-trust green? It feels like certainty, teams grow faster than reviewer capacity, deadlines turn CI into the only gate that matters, and we confuse necessary with sufficient.

## Trust breaks at predictable sizes

The scaling model is the most memorable slide. At five contributors, personal trust works. At the next step up, people are semi-known and review slows. At five hundred, most pull requests come from strangers and the trust model is broken. That is where XZ was. The paradox: the trust that let a project grow becomes its biggest vulnerability as it succeeds, and pressure (review queues, deadlines, velocity as the only metric, reactive maintenance) makes it worse.

## Three pillars to put beside the pipeline

**Review practices:** a second reviewer for authentication, payments and security-critical paths; avoid the same reviewer approving the same author over and over; a risk checklist before merge; and explicit fast and slow lanes, so docs and tests move quickly while new dependencies and performance work get more scrutiny.

**Culture:** normalise "I don't understand, can you explain?", reward people who catch problems and not only those who ship most, write the reasoning for trade-offs into the PR, and pair-review the genuinely tricky changes.

**Process safeguards:** canary deploys to a small slice of traffic, post-deploy smoke checks, deploy markers in monitoring, alerts on new or upgraded dependencies, and pre-agreed error budget rollback triggers.

## The checklist she likes best

Her favourite slide is a short list to answer before merging: does it touch sensitive areas such as auth or infrastructure, does it add dependencies, are hard-to-test paths changed, is rollback simple, is the reviewer new to this area, does it rely on tribal knowledge, are we merging under time pressure, and what could go wrong if we are wrong? Yes answers do not block the merge; they mean slow down, add a reviewer, add monitoring or stage the rollout. If you cannot answer the last question, you probably do not understand the change well enough to approve it.

## Who should watch

Maintainers, tech leads and anyone who has approved a PR mostly because CI was green. Tooling-focused teams will find few new tools here; what they get is the review and culture layer most pipelines quietly assume exists.

## Related Conf42 talks

- [Supply Chain Security for OpenSource Projects - it's time to prepare!](https://www.conf42.com/Cloud_Native_2023_Sven_Ruppert_supply_chain_security_opensource_projects) by Sven Ruppert covers the dependency side of the same risk.
- [Mastering Efficient Code Reviews: A Path to Superior Codebase](https://www.conf42.com/DevOps_2024_Israel_Heringer_efficient_code_reviews_codebase) by Israel Heringer goes deeper on making review itself work.
- [Rethinking Supply Chain Security in the Age of Agentic AI](https://www.conf42.com/DevSecOps_2026_Roshan_Piyush_supply_chain_security) by Roshan Piyush asks what happens when some contributors are agents.

[Watch Tilda Udufo's talk](https://www.conf42.com/DevOps_2026_Tilda_Udufo_cicd_quality_testing)

[Watch the talk on YouTube](https://youtu.be/1-vUdEJpvvU).

## Watch the talk

[Green Checkmarks, Red Flags: What CI/CD Can't Catch](https://www.conf42.com/DevOps_2026_Tilda_Udufo_cicd_quality_testing) at Conf42 DevOps 2026.
