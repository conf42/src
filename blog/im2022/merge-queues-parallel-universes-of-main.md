# Merge queues, from 50 hours to under one: treat main as parallel universes

Conf42 Blog, 2022-09-30. https://www.conf42.com/blog/im2022/merge-queues-parallel-universes-of-main

In short: Ankit Jain (Aviator Technologies) at Conf42 Incident Management 2022 on merge queue strategies that keep a busy monorepo's main branch green.

Two pull requests, both green, merged an hour apart, and main is red. At Conf42 Incident Management 2022, Ankit Jain, co-founder and CEO of Aviator Technologies and formerly an engineer at Google and Adobe, walks through the merge strategies that stop this from happening in a busy monorepo, and does the arithmetic on each so you can see what it costs in hours and CI runs.

It's a sponsor talk; Aviator builds merge automation and Ankit spends the last few minutes on its features. The rest is a tidy tour of ideas published by Uber, Airbnb and LinkedIn, and the open source Bors, all of which he cites at the end.

## Why does main break when every PR passed?

Ankit lists the usual suspects for mainline failures (infrastructure, timeouts, third-party dependencies, race conditions, shared state) and then narrows to two: stale dependencies and implicit conflicts. Each PR was tested against the main it branched from, not the main it lands on. Two changes touching related code can each pass and still be incompatible together.

As the team grows, he says, these failures grow exponentially, and you get build police, rollbacks, delayed releases and chain reactions where people branch off a broken main. Everyone waits for green.

## Why isn't a simple merge queue enough?

The basic fix is merge automation: instead of pressing the button, you mark a PR ready, the system merges the latest main into it, runs CI and merges only if it passes. The next PR waits its turn. Every change is validated against the real future main.

The catch is serial throughput. With 30-minute CI, a team merging 10 PRs a day spends 5 hours in the queue. At 100 PRs a day it's 50 hours, which no system can absorb in a day.

## Batching, then optimism

Ankit's numbers, all for 100 PRs a day with 30-minute CI:

| Strategy | Best case | 10% failure rate |
|---|---|---|
| Simple queue | 50 hours | - |
| Batches of 4 | 12.5 hours, 25 CI runs | about 24 hours |
| Optimistic queue | under 1 hour, 100 CI runs | about 6 hours, ~150 runs |
| Optimistic + batches | under 1 hour, 25 CI runs | about 4 hours, ~48 runs |

Batching waits for a few PRs and tests them together, bisecting the batch on failure to find the culprit. It cuts CI runs but failures hurt a lot.

The optimistic queue is the conceptual jump. Stop thinking of main as a line and think of it as several possible futures, Ankit's parallel universes. When PR 2 arrives while PR 1's CI is still running, assume PR 1 will pass and start testing PR 2 on an alternate main that already includes PR 1. If PR 1 fails, throw that alternate main away and rebuild the rest without it. Combining that with batching gets you both the speed and the lower CI bill.

## Predict which futures are worth testing

Taken to the extreme, you could test every combination of queued PRs and never wait on a failure, at the cost of an absurd amount of CI. Ankit's middle ground is predictive modelling: score each path by lines of code changed, types of files modified, tests added or removed and the number of dependencies, then run CI only on paths above a cutoff (0.5 in his example).

## Multi-queues: one queue per affected target

If your build system can tell you which targets a change affects (Bazel can), you don't need a single queue at all. Put PRs into disjoint queues per target, backend and frontend for instance. A PR that touches two targets sits in both. A failure then only blocks PRs behind it in the same queue, not the whole repository.

"This definitely increases the velocity at which you're merging the changes, because it's in some ways localizing failures to a particular affected target," Ankit Jain said at Conf42 Incident Management 2022.

His closing list of further tweaks is worth stealing whatever tool you use: reorder the queue so high-priority or low-risk changes go first, run the tests that fail most often first so a bad PR fails fast, and split tests into pre-merge (fast, critical, flaky-prone) and post-merge (slow, stable smoke tests) with automatic rollback for the rare post-merge failure.

## Who should watch

Anyone whose monorepo has a build cop rota, or who has turned on GitHub's merge queue and wondered what's next. It's a clear explanation, not a benchmark: the figures are worked examples with assumed CI times and failure rates, not measurements from a production repository. For neighbouring topics, see [Mike Morgan on tackling flaky tests](https://www.conf42.com/DevOps_2025_Mike_Morgan_testing_flaky_strategies) at Conf42 DevOps 2025, [Eugene Khabarov's introduction to Bazel](https://www.conf42.com/Golang_2024_Eugene_Khabarov_build_enough_bazel) at Conf42 Golang 2024, and [Vadim Tsaregorodtsev on Git submodules as a home-made monorepo](https://www.conf42.com/JavaScript_2023_Vadim_Tsaregorodtsev_git_submodules_monorepo) at Conf42 JavaScript 2023.

[Watch Ankit Jain's talk](https://www.conf42.com/Incident_Management_2022_Ankit_Jain_automate_merging_keep_builds_healthy) from [Conf42 Incident Management 2022](https://www.conf42.com/im2022).

## From Aviator Technologies

At the end of the talk Ankit shows what Aviator adds on top of the queue: ChangeSets that merge related PRs across several repositories (an API change plus its web, iOS and Android clients) as one atomic unit, a flaky test check that suppresses failures unrelated to the PR so it can still merge, and a CLI for syncing and queuing stacked PRs together.

- Aviator: [aviator.co](https://www.aviator.co/)

[Watch the talk on YouTube](https://youtu.be/9YfpNc7dv2w).

## Watch the talk

[Automate merging to keep builds healthy at scale](https://www.conf42.com/Incident_Management_2022_Ankit_Jain_automate_merging_keep_builds_healthy) at Conf42 Incident Management 2022.
