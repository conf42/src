# Your LLM judge is failing silently, and it should be the strongest model

Conf42 Blog, 2026-05-26, updated 2026-11-09. https://www.conf42.com/blog/llms2026/llm-judge-verifier-rots-silently

In short: Vsevolod Voropaev at Conf42 LLMs 2026 argues the verifier is an agent system's hardest part and routes cross-family judges with bandits.

When your agent is wrong, you lose a task. When your judge is wrong, you lose the ability to know anything is wrong at all. At Conf42 Large Language Models (LLMs) 2026, Vsevolod Voropaev, a founding engineer at an early-stage multi-agent startup with two years of production LLM work across three companies behind him, argues that the verifier is the hardest component in an agentic system, not the easiest, and that most teams have their intuition about it exactly backwards.

## Silence is the failure mode we can't see

The story is familiar. The agent works in the demo, someone asks how you know the output is correct, and you bolt on a second model call that rates the answer. For a while the judge and your own eyes agree, so you stop reading outputs. That's when the rot starts: a broken judge and a working judge emit the same artifact, a number.

No exception fires when a judge approves a bad answer. Logs, alerts and dashboards surface events, and a silently wrong verdict is the absence of one. The verifier, in his phrase, is the one component whose failures are invisible by construction.

## The biases are measured, and they compound

Vsevolod walks through findings from the LLM-as-judge literature. Position bias and verbosity bias appear in the original LLM-as-judge paper from Zheng and colleagues in 2023 and have survived every model generation since. Self-preference is worse: work by Wataoka and colleagues found it tracks perplexity, meaning judges favour text that reads like their own. On Arena Hard, he cites a self-preference effect ranging from -38% to +90% across judges. If agent and judge share a model family, you're getting a model nodding at its reflection.

Putting a human on top doesn't close the gap. Dietz and colleagues documented a rubber-stamp effect: people asked to check an LLM's verdict tend to agree with it, even when it's demonstrably wrong. That stacks two correlated verifiers and calls it defence in depth. None of this shows in a ten-example demo; the biases are statistical and appear at scale, exactly where you stopped looking.

## The judge should usually be smarter than the agent

The common setup puts the big model on the agent and a cheap one on the judge, because checking feels easier than doing. Vsevolod takes the verification-asymmetry argument seriously, then shows where it breaks. Checking is cheap only when there is a certificate: multiply the factors, run the code, execute the query. Most agentic tasks have none. Was the summary faithful to the contract? Will this plan reach the goal? Verifying means redoing the reasoning, and a judge can't reliably catch a mistake on a problem it couldn't solve.

His conditional rule: with a cheap certificate, a cheaper judge plus the tool can verify a stronger generator, so lean on the tool. Without one, the judge must be at least as strong as the agent.

Self-verification doesn't rescue you. He cites research showing generation and self-verification don't improve together, and that much apparent self-checking is fake verification: the model writes the words of checking with almost no effect on the answer. Real verification needs independent purchase on the problem: a different model, a tool, a ground-truth outcome.

## Route judges, don't average them

Three judges from one family averaged together give you sharper confidence, not better accuracy. Judges from genuinely different families (Claude, GPT, Gemini) disagree in systematic, measurable ways, and the cases where they split are a live map of where your risk is. Never let a model be the only judge of itself.

Since running a full panel on every output is unaffordable, he frames judge selection as a multi-armed bandit. Each judge or combination is an arm; downstream signals (spot checks, tests, escalations) are rewards. Thompson sampling, dating to 1933, explores early and concentrates on judges that keep being right per task type, and keeps relearning as models and traffic drift. The economics follow: verification at full strength can be the largest line in your inference bill, so you pay for strong judges only on the fraction of tasks near a decision boundary.

## Who should watch

Anyone running LLM-as-judge in production, or about to. The talk is dense with citations and he shares a reading list at the end, so keep the slides handy.

## Related Conf42 talks

- [Who Judges the AI Agent? LLM-as-Judge for Testing Non-Deterministic Code Generation](https://www.conf42.com/AI_Agents_2026_Liran_Yushinsky_testing_judge_codegen) by Liran Yushinsky, for judges in a code generation setting, where certificates exist.
- [Self-Signed Evidence: Why Your LLM Agent's Green Checks Prove Nothing](https://www.conf42.com/MLOps_2026_Danila_Redikultsev_evidence_agent_checks) by Danila Redikultsev, a close cousin of the fake-verification argument.
- [How to evaluate your Evals?](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals) by Hilik Paz, on verifying the verifier.

[Watch Vsevolod Voropaev's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production)

[Watch the talk on YouTube](https://youtu.be/Haa1DCigr_o).

## Watch the talk

[The Judge Problem: Why Your Agentic Verifier is Silently Rotting in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) at Conf42 Large Language Models (LLMs) 2026.
