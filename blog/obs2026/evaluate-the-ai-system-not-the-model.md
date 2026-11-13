# Benchmarks grade the model. Production needs to grade the system

Conf42 Blog, 2026-08-18. https://www.conf42.com/blog/obs2026/evaluate-the-ai-system-not-the-model

In short: Srikanth Devarakonda of Adobe at Conf42 Observability 2026 on continuous GenAI evaluation tied to observable signals and business outcomes.

A model can top a leaderboard and still give your users wrong answers, because users do not talk to the model, they talk to the whole system around it. At Conf42 Observability 2026, Srikanth Devarakonda, Software Development Engineer 5 at Adobe, where he leads GenAI capabilities for Acrobat Assistant, argued for moving from one-off model benchmarks to continuous evaluation of the complete AI system, measured with observable signals and tied to business outcomes.

## Why the benchmark score lies by omission

Devarakonda is clear that benchmarks are useful for comparing models under controlled conditions. The problem is what they leave out. A benchmark is a static, curated dataset; production is unpredictable input. A benchmark scores single transactions; production is multi-turn conversations where context piles up. A benchmark isolates the model; production adds retrieval, prompt templates, orchestration, APIs, databases, permissions, safety layers, latency budgets, and users doing things you never anticipated. A failure can come from any of those, and sometimes the model is not the problem at all.

So the question changes from how capable the model is to how the whole system behaves when real users depend on it. He breaks that into four activities: measure (define quality for your application as signals), validate (automate, with human judgment where automation falls short), monitor (catch drift and new failure modes after launch) and govern (traceability and controls).

## Four dimensions, defined by your domain

The evaluation dimensions are factual accuracy, grounding (is the answer supported by authoritative, retrieved content), safety within policy, and task completion. The last one is the easiest to forget: a factually correct answer that does not help the user finish their task is still a failure.

Which dimension matters most depends on the application. Customer support cares about resolution without escalation. Decision support cares more about evidence, traceability and confidence calibration. A generic benchmark applied to both will give you a great score for the wrong thing. Define what failure looks like and what it costs first, then pick metrics.

## Automate for breadth, send the hard cases to humans

Nobody can hand-review every production interaction, and fully automated evaluation has blind spots. Devarakonda's answer is LLM-as-judge, embedding similarity, classifiers and rule-based checks for scale, plus intelligent sampling that routes low-confidence, high-risk and policy-sensitive interactions to human reviewers. What the reviewers find feeds back into the rubric, the ground-truth dataset, the judge prompts and the system itself. A production failure is information about your evaluation method as much as about the model.

For hallucinations he describes a layered stack: entailment checks against retrieved context, self-consistency sampling across multiple generations, retrieval faithfulness, and inference-time controls such as confidence thresholds and human escalation. The aim is to intercept unreliable answers before users see them, which turns hallucination handling from an analytics job into an engineering control. Robustness gets the same treatment: perturbed and adversarial inputs, fairness checks, red teaming for jailbreaks and prompt injection, and re-evaluation when the traffic distribution shifts.

## Segment the dashboard, version everything

The observability stack he describes has three parts: real-time dashboards (hallucination rate, latency, refusals, satisfaction, task success), segmentation by model version, prompt template, user segment and environment, and full interaction tracing from input to retrieved context to output to evaluation score. Segmentation is what turns a vague five percent quality drop into one bad prompt template you can roll back. Governance belongs in the engineering process too: model versioning, evaluation snapshots, automated rollback triggers, audit logs. Added afterwards, he warns, it becomes paperwork.

The slide he calls the most important connects technical metrics to business ones. Higher task success should mean higher resolution, fewer escalations and lower support cost. That is how you tell leadership something better than a three-point bump in an evaluation score.

## Who should watch

Engineers and product owners moving a GenAI feature from pilot to production, especially if your current evaluation is a benchmark run before launch. It is a framework talk without a demo or Adobe-specific numbers, so treat it as a checklist for designing your own evaluation pipeline.

[Watch Srikanth Devarakonda's talk](https://www.conf42.com/Observability_2026_Srikanth_Devarakonda_llms_evals_benchmarks) ([YouTube](https://youtu.be/chDuQddtZyo)).

## Related Conf42 talks

- [How to evaluate your Evals?](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals) by Hilik Paz (Arato.ai), LLMs 2025.
- [The Judge Problem: Why Your Agentic Verifier is Silently Rotting in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) by Vsevolod Voropaev, LLMs 2026.
- [An Advanced Validation Pipeline for Summary Evaluation in High-Stakes Environments](https://www.conf42.com/Large_Language_Models_LLMs_2026_Liliya_Imasheva_Michael_Banf_validation_summaries_evaluation) by Liliya Imasheva and Michael Banf (Perelyn), LLMs 2026.

## Watch the talk

[From Benchmarks to Business Impact: Evaluating Generative AI in Production](https://www.conf42.com/Observability_2026_Srikanth_Devarakonda_llms_evals_benchmarks) at Conf42 Observability 2026.
