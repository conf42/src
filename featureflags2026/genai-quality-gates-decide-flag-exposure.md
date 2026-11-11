# Feature flags manage exposure, quality gates decide if AI earns it

Conf42 Blog, 2026-09-29, updated 2026-11-09. https://www.conf42.com/featureflags2026/genai-quality-gates-decide-flag-exposure

In short: Adobe's Rajesh Lingam at Conf42 Feature Flags 2026 on three evaluation gates that decide when a GenAI feature behind a flag gets more traffic.

A GenAI feature can be operationally green, with low errors, fine latency and a perfectly behaved flag, while its answers quietly get worse. At Conf42 Feature Flags 2026, Rajesh Lingam, who works in GenAI evaluation and engineering at Adobe, made the case for pairing flags with automated quality gates, so a rollout step only happens once the AI behaviour has the evidence to justify it. He notes up front that the views are his own, not Adobe's.

His one-line thesis: feature flags manage exposure, quality gates manage confidence.

## The prompt change that passed everything

The story that frames the talk is painfully ordinary. A team edits a prompt to make answers shorter and friendlier. Functional tests pass, the API returns green, latency even improves. But on a small set of retrieval-heavy questions, the model now summarises too aggressively and adds statements the source doesn't support. Rajesh mentions seeing models make up arithmetic, even page numbers, simply because numbers were around.

Normal monitoring misses all of it. The flag will help you roll back once someone notices; a gate is what notices before the exposure grows. The shorter, friendlier, wrong answer is a very polite kind of outage.

## One score hides the failure you care about

In deterministic software, a regression suite passing at a high percentage is a reasonable ship signal. With GenAI, Rajesh argues, a single average can mask exactly the failure that matters. He scores releases on separate dimensions: answer quality (useful and correct for the task), grounding (supported by the provided context), safety, regression against the last stable baseline, and latency and cost, since an accurate system that is too slow or expensive isn't release-ready either. The gate should say which dimension failed and what to fix.

He treats prompts, model versions, retrieval configuration and tools as releasable artifacts. If a change can alter user-facing behaviour, it deserves release evidence, even when no code changed.

## Three gates, three price points

Rather than one giant evaluation run, he describes three:

- **Change-level gate**: cheap and fast, before merge or early in CI. Focused scenarios, deterministic checks and quick judge metrics ask whether the change obviously broke something.
- **Release-level gate**: before broader rollout. Representative scenarios, comparisons against baselines and thresholds, plus human review.
- **Runtime gate**: after exposure starts. Telemetry, sampled evals on live traffic, user feedback, and the rollback decision.

How much evaluation is enough? Depth rises with uncertainty and consequence: how many users or workflows are affected, how bad a failure would be, how big the change is. A one-sentence prompt tweak doesn't need the full suite. He is explicit that this is a decision framework, not a certification formula.

## Exposure grows only as evidence grows

The gates map onto the familiar rollout ladder. At 0% you lean on offline evidence: golden scenarios, regression tests, internal review. At a 1% canary you add runtime evidence from real traffic. At 10% you look for failure categories the offline suite never showed, at 50% for long-tail behaviour, and at 100% you keep monitoring, because models, prompts, retrieval content and user behaviour all drift.

Back to the prompt story: with a gate, targeted evals catch the grounding drop on retrieval-heavy questions, exposure stays where it is, and the team fixes the prompt before widening. The failure still happened. Users just didn't meet it at scale. His last rule is the sharpest: a gate must produce an action (proceed, hold, roll back or review). If it only produces a dashboard, it isn't a gate.

## Who should watch

Teams shipping LLM features behind flags who currently decide rollout steps by gut feel or a demo. It's a concise, framework-level talk without tool specifics, so pair it with something hands-on if you want pipelines and code.

## Related Conf42 talks

- [Green Evals, Broken Agents: Making Evals a First-Class Deployment Artifact](https://www.conf42.com/MLOps_2026_Dylan_Ler_evals_agents_deployment) by Dylan Ler of Adobe at Conf42 MLOps 2026.
- [Harness Engineering for Production LLMs: Eval-as-Code From Day One](https://www.conf42.com/MLOps_2026_Anwar_Khan_eval_llms_harness) by Anwar Khan of John Deere at Conf42 MLOps 2026.
- [How to evaluate your Evals?](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals) by Hilik Paz of Arato.ai at Conf42 Large Language Models 2025.

[Watch Rajesh Lingam's talk](https://www.conf42.com/Feature_Flags_2026_Rajesh_Lingam_quality_gates_genai) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/K88d8qp9zpM).

## Watch the talk

[Beyond On/Off: Using Quality Gates to Safely Release GenAI Features](https://www.conf42.com/Feature_Flags_2026_Rajesh_Lingam_quality_gates_genai) at Conf42 Feature Flags 2026.
