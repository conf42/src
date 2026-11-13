# Performance signatures that gate every LLM and RAG commit

Conf42 Blog, 2026-06-10, updated 2026-11-09. https://www.conf42.com/blog/llms2026/performance-signatures-gate-every-llm-commit

In short: Kandasamy Selvaraj of ADP at Conf42 LLMs 2026 on statistical CI/CD gates that catch LLM latency, token and tool-call regressions before production.

Most LLM teams write the prompt, commit, build and run inference, then find out about the latency regression from users. Kandasamy Selvaraj, Principal Architect who leads performance engineering at ADP, argued at Conf42 Large Language Models 2026 that the missing step is a gate: a statistical performance signature evaluated on every commit, with a verdict back to the developer in about 15 to 20 minutes.

## Why LLM performance bugs hide

Selvaraj lists what makes these defects different. Latency varies with every model update, so you cannot tell whether time to first token got worse because of your code or your provider. RAG pipeline failures show up first in production. Token throughput and time to first token need different instrumentation from ordinary API metrics. Agents are probabilistic, so failures cascade silently along a chain. And developers get no feedback when they commit.

He cites research suggesting that agent failures in complex workflows mostly come from orchestration and tool-call sequencing rather than the model itself, which is exactly where his framework looks.

## Normal beats acceptable

The core idea is a deviation score: the observed metric minus the learned baseline, divided by the baseline's standard deviation. A static threshold tells you whether a number is acceptable. The deviation score tells you whether it is normal for this system. A 50 ms jump in p90 with a 20 ms standard deviation gets flagged at the two-sigma gate because it is 2.5 deviations out, even though 50 ms sounds harmless.

The baseline is not fixed. It is recalibrated as models, prompts and data change across commits, so the gate keeps up with the system it guards.

## Five dimensions, all must pass

For agents, time to first token is not enough. The signature tracks five dimensions:

- total trace latency across every LLM call and tool invocation
- per-tool response time, each tool with its own baseline
- LLM calls per trace, which catches looping and context loss (with a baseline of two calls, three is flagged and four is blocked)
- tokens per trace, where small changes compound: 200 extra output tokens per call, three calls per trace and 60,000 requests an hour adds up to 36 million extra tokens an hour
- tool error and retry rate, because a silent retry still costs latency and tokens

In his worked trace, the LLM calls pass but a code-executor tool lands 4.3 sigma out and the whole build is blocked. "One slow tool blocks the entire build."

## Tag every request with its build

The integration trick that makes root cause automatic is simple: inject build ID, commit ID, model version and prompt hash into every LLM request. Tools such as Langfuse, LangSmith or Arize can then tie a slow trace to the exact prompt change that caused it. The reference stack in the talk uses JMeter-style load generation, Jenkins for orchestration, Prometheus and Grafana for visibility, LangChain behind an AI gateway, and PostgreSQL and Redis on Kubernetes.

The demo shows a `/perf gate` chatbot running the same checks: one commit passes at 218 tokens per request against a 500 limit, then with the limit dropped to 100 the same pipeline blocks the build and explains why.

## Results and the honest caveats

Over an eight-week rollout he reports 30 to 40 percent fewer production performance issues per month, around 200 percent more defects found in development, mean time to detect down from most of a day to under an hour, and automated root cause for 91 percent of failures. The lessons are useful too: LLM non-determinism needs a wider sigma band than deterministic services, the gate needs 10 to 20 runs of baseline before it is trustworthy, and every team still needed a two-to-three-hour onboarding session.

He is explicit that the commit gate is an add-on to full-scale load and soak testing, not a replacement. The pipeline catches the change; the big test validates the system.

## Who should watch

Performance engineers, platform teams owning CI/CD for AI services, and anyone whose token bill has surprised the finance team. If you already run load tests and want them to say something useful per commit, this is the playbook.

## Related Conf42 talks

- [Building Robust GPU Performance Validation into CI/CD Pipelines for AI Infrastructure](https://www.conf42.com/DevOps_2026_Mohit_Gupta_gpu_ci_validation) from Conf42 DevOps 2026 applies the same gating idea one layer down.
- [The Retry Storm That Ate My Budget: Debugging the Hidden Cost Loops in Agentic AI](https://www.conf42.com/AI_Agents_2026_Yamini_Rathamsetty_Karthik_Akula_cost_loops_tokens) from Conf42 AI Agents 2026 is the horror story behind the retry dimension.
- [Automating peak readiness: turning observability signals into workload engineering insights](https://www.conf42.com/Observability_2026_Vasuki_Uday_Kiran_Vudathala_loadtesting_performance_capacityplanning) from Conf42 Observability 2026 covers the full-scale side he says you still need.

[Watch Kandasamy Selvaraj's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Kandasamy_Selvaraj_performance_lag_signatures)

[Watch the talk on YouTube](https://youtu.be/VUCevl9qYd8).

## Watch the talk

[Shift-Left Performance Engineering for RAG and LLM Platforms with CI/CD Performance Signatures](https://www.conf42.com/Large_Language_Models_LLMs_2026_Kandasamy_Selvaraj_performance_lag_signatures) at Conf42 Large Language Models (LLMs) 2026.
