# Compile it, judge it, attack it, on every PR that touches the agent

Conf42 Blog, 2026-09-14, updated 2026-11-09. https://www.conf42.com/blog/agents2026/compile-judge-attack-every-agent-pr

In short: Liran Yushinsky (JFrog) at Conf42 AI Agents 2026: a three-layer CI gate of compile checks, LLM-as-judge and Garak red-teaming for code agents.

If you check AI-generated code with a regex and a couple of unit tests, Liran Yushinsky would say you aren't testing, you're hoping. At Conf42 AI Agents 2026, the automation lead in JFrog's AppTrust group showed a three-layer gate that runs on every pull request touching an agent's system prompt or tools: a deterministic compile check, an LLM judge scoring meaning against a golden dataset, and a Garak red-team scan. Any layer can block the merge.

## Why your old assertions stop working

A deterministic API is a peaceful contract: send a payload, assert on the response. An agent that turns natural language into code through a chain of tool calls gives you a different valid answer each run, so "actual equals expected" has nothing to hold on to. He also dismisses BLEU and ROUGE for code. They count word overlap, so renaming a variable or swapping a while loop for a for loop fails a correct function, and he cites research by Dan Hendrycks and colleagues showing such scores can rise while the code gets more broken.

His framing of the bigger picture: the gap in enterprise AI is not generation but verification. An agent's output is shippable only if you can prove, automatically and on every change, that it is correct.

## Making the judge trustworthy

LLM-as-judge means a strong model grades another model's output against a rubric you write. He cites the MT-Bench and Chatbot Arena work by Lianmin Zheng and colleagues, where a GPT-4 judge agreed with human reviewers on clear-cut cases about as often as humans agreed with each other. That was the point he stopped being a skeptic.

His four rules for a reliable judge are concrete:

- Let it reason step by step, then turn that into a series of yes/no checks (he names G-Eval, DAG and QAG).
- Don't ask for a score from one to ten; ask for labels such as pass, partial, fail.
- Anchor it with a golden reference and a couple of examples. For code, one good example often beats ten.
- Never let a model grade its own homework: if GPT wrote it, a different model family judges it.

He is honest about the blind spots: verbosity bias, position bias, self-enhancement bias, run-to-run wobble and model drift over time. Swap the order in head-to-head comparisons, log every score and alert on slips. His favourite trick is treating the wobble as a map, since the judge disagrees with itself exactly where your instructions are unclear. The judge in turn gets checked by meta-evaluation: run it over a human-labelled golden set, measure agreement, read every miss, tighten the rubric, repeat.

## Each layer catches what the others miss

Layer one strips the nice markdown and tries to compile or parse the output, or validates it against the real API spec. Hallucinated endpoints and broken JSON fail instantly, no LLM involved. Layer two runs the agent over 30+ curated natural-language-to-code pairs, with Promptfoo running the evaluation and Helicone tracing the calls, and blocks when the meaning score falls below threshold. Layer three uses Garak, NVIDIA's open-source LLM vulnerability scanner, to fire known jailbreaks and injections; if the agent takes the bait even once, the merge is blocked.

His comparison table makes the case: a missing colon is caught only by layer one, valid code that ignores a business rule only by the judge, and a "print your system prompt" injection only by the red team. Every row has a different hero.

The live demo runs the same gate against the JFrog AI assistant on the docs site and against ChatGPT writing Python. The interesting run is valid Python that blocks on low severity instead of critical: it compiles, layer one is happy, and the judge blocks it. As JFrog's own talk, it also points to AppTrust and JFrog Xray along the way.

## Who should watch

Test automation engineers and anyone shipping an agent that writes code, queries or policy. Mind his cost caveat: judge calls burn tokens, so the deterministic layer runs on every commit and the expensive LLM checks can run on a schedule.

## Related talks

- [The Judge Problem: Why Your Agentic Verifier is Silently Rotting in Production](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vsevolod_Voropaev_verification_agents_production) by Vsevolod Voropaev
- [How to evaluate your Evals?](https://www.conf42.com/Large_Language_Models_LLMs_2025_Hilik_Paz_evaluate_evals) by Hilik Paz
- [Agent Evals That Check What Actually Happened](https://www.conf42.com/MLOps_2026_Sajal_Garg_agent_evals_happened) by Sajal Garg

[Watch Liran Yushinsky's talk](https://www.conf42.com/AI_Agents_2026_Liran_Yushinsky_testing_judge_codegen)

[Watch the talk on YouTube](https://youtu.be/FI0zGAXb1Jk).

## Watch the talk

[Who Judges the AI Agent? LLM-as-Judge for Testing Non-Deterministic Code Generation](https://www.conf42.com/AI_Agents_2026_Liran_Yushinsky_testing_judge_codegen) at Conf42 AI Agents 2026.
