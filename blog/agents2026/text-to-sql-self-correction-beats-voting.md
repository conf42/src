# Text-to-SQL on open models: self-correct, don't vote, measure linking

Conf42 Blog, 2026-09-16, updated 2026-11-09. https://www.conf42.com/blog/agents2026/text-to-sql-self-correction-beats-voting

In short: Vladimir Beskorovainyi (Besk Tech) at Conf42 AI Agents 2026 tests text-to-SQL tricks on open models: self-correction pays, voting and schema linking don't.

Everyone has a text-to-SQL demo; few people have to answer for the number it produces at 9 a.m. Vladimir Beskorovainyi, Enterprise AI architect and CTO at Besk Tech, runs one of those systems, with 500 data marts on-prem, open models, and 30 million users who can't read SQL to check it. At Conf42 AI Agents 2026 he tested the popular tricks on the public BIRD benchmark and came back with a short list: pick a recent model family, add a self-correction pass, and measure everything else before you trust it.

## Two kinds of numbers, never mixed

He is unusually careful about sources. Production numbers come from his own system, with closed data and his own definition of correct, so you can't check them. Benchmark numbers come from BIRD dev (all 1,534 questions, execution accuracy), with open code you can rerun. He labels every number with its kind and never compares the two.

The test covered three families on his own servers with identical prompts and settings: Qwen 2.5 Coder at 7B, 14B and 32B, CodeLlama at 7B, 13B and 34B, and Llama 3.1 8B and 3.3 70B. Because every model answers the same questions, he compares pairs with McNemar's test, and his warning is that at this sample size a gap of two and a half points can still be noise. That paragraph alone is worth sending to whoever wrote your last internal benchmark slide.

## The year beats the size

Qwen climbs from 39 to 47 to 50 percent as it grows, and gains flatten quickly after 14B. CodeLlama barely moves, from 21 to 24.5. At 7B the gap between the families is 18 points, larger than any size effect. To check that this wasn't just a 2023 versus 2024 artefact, he added Llama 3.3 70B, which also came out strong. The lesson he draws is not "Qwen wins" but that a recent model beats an old big one: choose the family first, the size second.

## One fix-up pass helps; five votes don't

The cheapest trick was the best: let the model look at its own query and fix it. It helped every family, by about three points on CodeLlama 7B, 3.7 on Llama 8B and 1.2 on Qwen 32B, and it never made results worse. The stronger the model, the smaller the gain, because there is less to fix. The typical repairs were a wrong join key and a dropped filter.

Self-consistency (generate five answers and vote) gained 0.13 points, not significant, for five times the tokens and slow queries stretching from ten seconds to fifty. He measures cost in GPU seconds rather than tokens, because the person paying the bill pays for time. By that measure self-correction on CodeLlama 34B went from 12 to 22 cents per thousand queries for a real gain, a trade he takes every time.

## Schema linking: measure it, don't copy it

The result he didn't believe at first: cutting the schema down to the relevant tables, a step in every tutorial, made things worse on BIRD, by as much as 3.7 points on Llama 70B. A better embedding-based linker with 96.5 percent recall didn't help either. BIRD schemas are small, so the prompt was never the problem, and linking only adds the risk of dropping a table you need.

This is not a contradiction of his own production system, where every query goes through retrieval across 500 marts. There the schema doesn't fit in the context window, so routing is the only way the query works at all. Same name, two different jobs. His complaint is about teams with small schemas copying a trick that only exists because someone else's schema didn't fit. He is also clear that wide-schema routing is his next study, not a claim he makes yet.

## The model may be wrong, just not silently

In production, guardrails are blunt and cheap: read-only access, a whitelist of objects and a row limit on every query. None of that catches a valid query that answers the wrong question, which he calls a meaning problem rather than a security one, so a person still sees the number before it becomes a decision. He is open about limits too: his clean baseline scores 50.4 percent, below strong cloud models and fine-tuned systems.

## Who should watch

Data and platform engineers moving text-to-SQL from demo to something people rely on, especially on-prem with open-weight models. It's a short, dense talk, and the code, settings and per-question answers are published.

## Related talks

- [Automating Database Operations with Cortex Code](https://www.conf42.com/Large_Language_Models_LLMs_2026_Tim_Spann_sql_automation_operations) by Tim Spann
- [Green Evals, Broken Agents: Making Evals a First-Class Deployment Artifact](https://www.conf42.com/MLOps_2026_Dylan_Ler_evals_agents_deployment) by Dylan Ler
- [Your Agent Is Confidently Wrong: Guardrails for Agentic AI in Real Engineering Work](https://www.conf42.com/Feature_Flags_2026_Girish_Konda_agent_guardrails_ai) by Girish Konda

[Watch Vladimir Beskorovainyi's talk](https://www.conf42.com/AI_Agents_2026_Vladimir_Beskorovainyi_sql_orchestration_scale)

[Watch the talk on YouTube](https://youtu.be/t4AZDCjhOnw).

## Watch the talk

[Agentic Text-to-SQL in Production: What 500+ Data Marts and 30M Users Taught Us About LLM Orchestration](https://www.conf42.com/AI_Agents_2026_Vladimir_Beskorovainyi_sql_orchestration_scale) at Conf42 AI Agents 2026.
