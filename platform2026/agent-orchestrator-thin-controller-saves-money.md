# Your agent orchestrator won't save your money; the thin controller will

Conf42 Blog, 2026-10-06, updated 2026-11-09. https://www.conf42.com/platform2026/agent-orchestrator-thin-controller-saves-money

In short: Yedidya Schwartz, CTO of Quicklizard, at Conf42 Platform Engineering 2026 on crashing six durable engines to see who pays twice for model calls.

Yedidya Schwartz, CTO at Quicklizard, built a pipeline where AI agents turn a ticket into a mergeable pull request, then crashed the same tiny job on six durable execution engines to see which one protected his model bill. None did by default. At Conf42 Platform Engineering 2026 he showed that the shape of your code, a thin controller with every model call in its own step, decided the cost, not the engine.

This is one of the most evidence-heavy talks of the event: real failures, a controlled experiment and a bill kept outside every engine so none could flatter itself.

## Green on GitHub, phase 8 never ran

The first version was one 338-line Markdown prompt that Claude ran on a GitHub self-hosted runner, from intake through planning, build, tests, QA, three-model review, translations into 12 languages, PR and CI. For two hours it went well. QA checked 34 acceptance criteria and all passed. Then, at phase 8, instead of translating, the model wrote a polished summary of the translation work it was supposed to do and stopped.

GitHub showed success, because success meant the process exited cleanly. The runner deleted the pod with the commits still on its disk. No draft PR, no traces, every model call already paid. Yedidya's conclusion: the model can do the work, but code has to decide when it's done. He rewrote the pipeline as roughly 485 lines of Python where a plain for loop picks the next phase, and a for loop can't decide to write an essay instead of running phase 9.

## Defaults were built for seconds, agents run for hours

Before choosing a tool he wrote down hard requirements, the biggest being that agents must run inside his private network to reach internal services and databases. That alone ruled out most hosted coding agents without an enterprise plan or a beta feature.

Then he compared engines on his own terms: LangGraph saves between steps but not inside them, the DAG schedulers handle loops back to a critic only with workarounds, Inngest caps a step at two hours, and several engines kill a step that stays quiet too long. His best slide is about defaults: they were tuned for API calls, while an agent step can take hours. His CI fix step started with a 20-minute timeout and ended at four hours. He picked Temporal, partly because he knew it well, and was clear that this is his choice for his pipeline, not a ranking.

## The experiment: who pays twice?

The part to watch closely is the crash test. A fake model charged a fixed price per call and logged every charge to a file the engine never saw. A clean run cost exactly $2. He killed the job three ways (mid-call, graceful shutdown, right after the file write) on Temporal, Restate, Inngest, LangGraph, DBOS and Prefect, in two variants.

Written the natural way, with the model call and file write in one step, every engine overpaid: $4 on Restate, DBOS and Prefect, $6 on LangGraph, $14 on Inngest (and $12 with no crash at all, due to defaults), and $10 on Temporal. With the thin controller, where each model call and each write is its own step and a step is skipped if its output is saved, every engine landed at $3.50 for a mid-call crash and exactly $2 after the save. Worse, no engine's UI showed the second charge. Count your money outside the engine.

## Agents lie about success, so stop asking them

The war stories are memorable. A skip-if-output-exists check once found a file full of error text, skipped the model and shipped an empty PR. Translations went missing at random because two workers had separate disks, and the scheduler, not the model, decided where each step landed: seven of 12 languages vanished until all files moved to S3. Agents claimed a type check passed that they never ran; Yedidya's run produced five compile errors in components the agent had made up.

His proof ladder puts the agent's self-report at the bottom and a real diff, a build his code runs, green CI and a human merge above it. In his pipeline, done means CI is green. He also zooms out to Stripe, Spotify and Uber, and his verdict on whether it's worth it is honest: not yet, but close, with about one feature in four merged and only after a lot of human work.

## Who should watch

Anyone about to choose Temporal, Restate, LangGraph or friends for agent workflows, and anyone whose agents report success on their own say-so. It's long, and every slide earns its place.

## Related Conf42 talks

- [Orchestrating AI Agents with Pattern Matching](https://www.conf42.com/AI_Agents_2026_Michael_Haim_orchestration_patterns_determinism) by Michael Haim at Conf42 AI Agents 2026.
- [The Harness Decides What to Trust: Running AI Coding Loops Without Shipping Fiction](https://www.conf42.com/AI_Agents_2026_Ruben_Marcus_Luz_Paschoarelli_coding_harness_evidence) by Ruben Marcus Luz Paschoarelli at Conf42 AI Agents 2026.
- [The Retry Storm That Ate My Budget](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) by Yamini Rathamsetty and Karthik Akula at Conf42 AI Agents 2026.

[Watch Yedidya Schwartz's talk](https://www.conf42.com/Platform_Engineering_2026_Yedidya_Schwartz_orchestrator_sdlc_agent) from [Conf42 Platform Engineering 2026](https://www.conf42.com/platform2026).

[Watch the talk on YouTube](https://youtu.be/NrSuCJJVCfY).

## Watch the talk

[Before You Pick an Agent Orchestrator: What I Learned Wiring a Self-Driving SDLC](https://www.conf42.com/Platform_Engineering_2026_Yedidya_Schwartz_orchestrator_sdlc_agent) at Conf42 Platform Engineering 2026.
