# Shift-left and shift-right testing work better as one loop

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/shift-left-shift-right-one-quality-loop

In short: Jyotheeswara Reddy Gottam of Walmart Global Tech at Conf42 Machine Learning 2025 joins pre-release testing and production signals into one quality loop.

Your unit tests and your Grafana dashboards are probably owned by different people who rarely compare notes. Jyotheeswara Reddy Gottam, Senior Software Engineer at Walmart Global Tech with 13 years in development and quality engineering, argued at [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025) that this split is the real quality problem: shift-left testing and shift-right validation should feed each other as one continuous loop, so production signals shape what gets tested and test results shape what gets watched.

This is a framework talk with a case study and published figures, not a tool demo. It is practical in places, though, and names plenty of real tools.

## The bug you find in UAT costs more than the one you find in a PR

Gottam opens with four symptoms. Development and functional testing happen in one silo, operations in another, so production feedback rarely reaches the developer. Bugs that slip past early testing surface in UAT or production, where they are far more expensive to fix. And the fragmented process slows releases. None of this is new, which is the point: most teams know it and still run four disconnected quality activities.

His continuous quality loop has four stations: preventive shift-left testing during development, continuous monitoring through deployment, reactive shift-right validation in production, and feedback that turns production insight into development priorities. The goal is to shorten the time it takes to go round.

## What each side brings

On the left he lays out a testing pyramid with numbers attached: roughly half the effort in developer-written unit tests, around 30% in automated CI integration checks, 15% functional tests (Cucumber, WebDriver, Playwright), and 5% end-to-end. Pre-commit hooks and CI validation on merge do the gatekeeping.

On the right he lists observability tools (Dynatrace, Splunk, Grafana), chaos engineering (AWS Fault Injection Simulator, Azure Chaos Studio, Chaos Mesh, LitmusChaos), canary deployments that start with 1-2% of users or A/B switches before widening the rollout, and performance monitoring with Prometheus, InfluxDB, CloudWatch or Azure Monitor. A canary that only ever hits 2% of users is also the cheapest apology you will ever issue.

## Treat each tool as an agent, then make them talk

The idea that gives the talk its edge is orchestration. Gottam suggests thinking of each quality activity (unit testing, integration testing, functional testing, Git checks, observability, chaos experiments) as an agent with one targeted job, then wiring them together with agent-to-agent communication. When a fault shows up anywhere in the chain, the signal reaches the developer faster and the fix ships sooner. It is an architecture for feedback, not a single product.

## People are the hard part

He is candid that tooling is the easy bit. Quality has to become everyone's job, from product to SRE. He argues for T-shaped quality professionals: deep in one area such as test automation or CI/CD, and broad enough to understand observability, performance analysis and chaos engineering. Adoption should be phased: baseline current metrics, connect development and production tooling with proofs of concept, add AI-augmented testing, then aim for a self-improving system.

The case study is a financial services team that moved from 12-week release cycles, mostly manual testing and separate QA and SRE groups to two-week releases, a majority of automated coverage and fewer incidents. He also mentions AI-assisted tools such as self-healing tests and test selection from design or requirement documents.

## Who should watch

QA leads and engineering managers trying to justify merging test and operations feedback, and SREs who want developers to care about what production is telling them. Experienced chaos practitioners will find the right-hand side familiar; the value is in the loop.

## Related Conf42 talks

- [Shifting left chaos testing](https://www.conf42.com/Chaos_Engineering_2023_Pablo_Chacin_shifting_left_chaos_testing), Pablo Chacin, Conf42 Chaos Engineering 2023
- [Building resilient test automation: a universal framework for SRE success](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sujeeth_Manchikanti_building_resilient_test), Sujeeth Manchikanti, Conf42 Site Reliability Engineering 2025
- [Resilience: chaos engineering to build robust systems](https://www.conf42.com/Cloud_Native_2025_Sai_Prakash_Narasingu_chaos_engineering_system_resilience), Sai Prakash Narasingu, Conf42 Cloud Native 2025

[Watch Jyotheeswara Reddy Gottam's talk](https://www.conf42.com/Machine_Learning_2025_Jyotheeswara_Reddy_Gottam_shiftright_shiftleft)

[Watch the talk on YouTube](https://youtu.be/dB-3w-n4el4).

## Watch the talk

[Convergent Quality Engineering: Integrating Shift-Left and Shift-Right Testing for Enhanced Software Resilience](https://www.conf42.com/Machine_Learning_2025_Jyotheeswara_Reddy_Gottam_shiftright_shiftleft) at Conf42 Machine Learning 2025.
