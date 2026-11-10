# With AI coding, the delivery bottleneck moves to code review

Conf42 Blog, 2026-10-21, updated 2026-11-09. https://www.conf42.com/platform2026/ai-coding-moves-the-bottleneck-to-review

In short: Lucas Mazei (Memed) at Conf42 Platform Engineering 2026 applies the theory of constraints to AI-assisted delivery and shows where platform teams should push.

If your coding stage just doubled its output and your throughput didn't move, Eliyahu Goldratt would like a word. At Conf42 Platform Engineering 2026, Lucas Mateus Mazei Sobrinho, engineering manager at the Brazilian health tech Memed, walked through the theory of constraints applied to AI-assisted software delivery, and why the fastest way to look productive (approve more PRs) is also the fastest way to drown in rework.

## Five boxes and a queue

Lucas starts with a deliberately simple model: five stages (implementation, review, validation, release, production) with illustrative fixed capacities of 4, 3, 4, 4 and 4 changes a day. Review handles three, so the whole system finishes three a day. Speed up release to six or seven and nothing changes, because release only ever receives three. Local optimisation of a non-bottleneck is theatre.

Then he applies AI. Implementation capacity goes up, but so does the size of each pull request: one PR can now hold a whole feature, several times a day. In his model review drops from three to two, and work piles up waiting in the PR list. He says he's hearing exactly this from other managers, tech leads and staff engineers.

## The wrong fix: rubber-stamp it

The tempting move is to review faster by reviewing less. Suppose tired reviewers start approving ten a day. The review queue clears in a flash, and validation becomes the pile. Worse, the poorly reviewed changes start coming back: feature 17 fails validation and returns as a rework ticket; feature 18 breaks in production and does the same. Each repair goes through implementation, review and validation again, consuming the same finite attention as new work.

His accounting rule is worth pinning up: a repair is another attempt at an existing outcome, so link it to the original and never count the outcome twice. Six approvals are not six outcomes.

## The right fix: make review smaller, not sloppier

This is where Lucas gets platform-specific. Before a human or a model looks at a change, run deterministic quality gates against the base revision: same lint rules and test configuration, checks for introduced duplication, coverage drops and broken end-to-end flows. A failed gate feeds a repair agent straight away. Once the gates pass, an AI reviewer looks at behaviour, context and risk, and its findings feed the same repair agent. Every repair is a new revision that restarts the gates.

Two constraints keep it honest. The agent can't lower a threshold or weaken an assertion to get to green. And the loop is bounded (his example: two repair attempts or ten minutes) before it hands the finding and evidence to a person. Tools like CodeRabbit and Linear then help reviewers focus on the parts that need judgment.

He also argues for generators over generated code. If a NestJS resource generator or your own CLI produces the model, controller, service, DTO and test skeleton, and you approved the schema and use case, nobody needs to read the boilerplate. That saves review time and, as a bonus, tokens.

## Then do it again

Fix review and validation becomes the constraint, so Lucas suggests agents that use the product like a user, with repeatable Playwright tests, or engineers owning validation outright. Then release, then production. The constraint isn't always the next column on the board; it can be a shared specialist or a decision nobody is making.

Measurement follows the whole path: completed outcomes with comparable scope, elapsed time, age of unfinished work, escaped defects, change failures, rework and recovery. And count AI cost per useful outcome rather than per line written. The reading list is two books: Goldratt's The Goal and Dominica DeGrandis's Making Work Visible.

## Who should watch

Engineering managers whose dashboards show more PRs and the same releases, and platform teams deciding where to invest in an AI-assisted pipeline. If you already live by value-stream maps, the first act is review; the gates-plus-bounded-repair-loop design is the new part.

## Related Conf42 talks

- [Flow Engineering - Boost velocity, quality and happiness through your entire value stream](https://www.conf42.com/DevSecOps_2022_Steve_Pereira_flow_engineering_boost_velocity_quality_happiness_value_stream) by Steve Pereira
- [From Vibes to Outages: When AI Writes the Code You Debug](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Sylvain_Kalache_vibes_outages_writes) by Sylvain Kalache (Rootly)
- [Beyond Token Counts: Observability for AI Coding-Agent Trajectories](https://www.conf42.com/Observability_2026_Elliot_Gardiner_agents_codegeneration_tracing) by Elliot Gardiner (Code Telemetry)

[Watch Lucas's talk](https://www.conf42.com/Platform_Engineering_2026_Lucas_Mateus_Mazei_Sobrinho_delivery_bottlenecks_coding)

[Watch the talk on YouTube](https://youtu.be/lFWPxq_xt1g).

## Watch the talk

[Beyond AI Coding: The New Bottlenecks of Software Delivery](https://www.conf42.com/Platform_Engineering_2026_Lucas_Mateus_Mazei_Sobrinho_delivery_bottlenecks_coding) at Conf42 Platform Engineering 2026.
