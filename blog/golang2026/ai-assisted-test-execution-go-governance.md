# AI test agents on top of go test, with confidence thresholds

Conf42 Blog, 2026-04-30, updated 2026-11-09. https://www.conf42.com/blog/golang2026/ai-assisted-test-execution-go-governance

In short: Rejenish Kiran of Citizens Property Insurance at Conf42 Golang 2026 on adding AI test agents to Go suites under escalation and audit rules.

A deterministic test either passes or fails. An AI test agent gives you an answer with a confidence level, and in an insurance company that difference has consequences. [Rejenish Kiran](https://www.conf42.com/Golang_2026_Rejenish_Kiran_assisted_test_execution), QA engineering manager at Citizens Property Insurance Corporation in Florida, used his Conf42 Golang 2026 talk to argue that AI belongs as an augmentation layer above existing Go test suites, and only with explicit thresholds, escalation paths and fallbacks.

It's a short talk, roughly ten minutes, and it's a governance framework more than a tooling demo. That brevity suits the message: the hard part isn't the agent, it's deciding what you let it decide.

## Augment, don't replace

The agents he describes interpret plain-language requirements, turn business intent into executable validation steps, and navigate interfaces adaptively, which makes them more resilient when DOM structures, identifiers or content change. Rejenish cites research showing context-aware locator techniques hold up better under that drift, moving maintenance away from fixing broken locators and towards checking genuine behaviour changes.

He is equally clear about the limits: large-scale enterprise validation of these approaches remains thin, especially in regulated industries like insurance and banking. So the Go side stays in charge. Table-driven tests, benchmark suites and integration harnesses remain the core execution layer, and go test remains the source of truth. AI adds orchestration, telemetry, confidence scoring and escalation, mostly in system and acceptance testing, integrated into GitHub Actions, GitLab or Jenkins.

## Confidence decides what happens next

The most reusable idea is confidence-based escalation. A mature setup shouldn't emit only pass or fail:

- high-confidence outcomes proceed automatically;
- medium-confidence results go to an engineer for review;
- low-confidence cases escalate to humans or block the release;
- if classification itself fails, deterministic execution is the fallback.

Thresholds and escalation policies have to be defined before anything probabilistic runs in a regulated pipeline. Think of it as a circuit breaker for judgement.

## Test artifacts are compliance evidence

In regulated environments, Rejenish notes, test execution records double as compliance evidence. So every AI action has to be explainable, attributable and reproducible: decision logs, traceability from requirement through execution, replayable sessions for audit. Failure has to be safe too. When confidence drops, the system moves along defined fallback paths (pause for human input, fall back to deterministic Go scripts, open an escalation ticket) instead of landing in an undefined state.

He also points to learning-based defect prediction: models trained on historical execution data to rank which tests are most likely to fail, so the riskiest run first and time to first failure shrinks.

## Adopt in phases

The rollout advice is incremental: start in observation mode, add augmentation where it pays, then scale across the portfolio, with governance and evidence collection maturing alongside.

## Who should watch

QA leads and Go teams in finance, insurance or healthcare evaluating AI test agents, and anyone who has to explain a probabilistic test result to an auditor. If you want a hands-on framework walkthrough, this isn't it; take the escalation model and build your own.

## Related Conf42 talks

- [Practical guide to testing Go services](https://www.conf42.com/Golang_2025_Nikolay_Kuznetsov_testing_go_services) by Nikolay Kuznetsov, the deterministic base layer this talk builds on.
- [Tackling Flaky Tests: Strategies for Reliability in Continuous Testing](https://www.conf42.com/DevOps_2025_Mike_Morgan_testing_flaky_strategies) by Mike Morgan, because a probabilistic test can look a lot like a flaky one.
- [How Visual AI Makes Testing a Breeze](https://www.conf42.com/Machine_Learning_2022_Andrew_Knight_visual_ai_testing) by Andrew Knight, an earlier look at AI-driven UI validation.

[Watch Rejenish Kiran's talk](https://www.conf42.com/Golang_2026_Rejenish_Kiran_assisted_test_execution)

[Watch the talk on YouTube](https://youtu.be/c2aDCAePVvE).

## Watch the talk

[AI-Assisted Test Execution for Scalable Go Quality Engineering](https://www.conf42.com/Golang_2026_Rejenish_Kiran_assisted_test_execution) at Conf42 Golang 2026.
