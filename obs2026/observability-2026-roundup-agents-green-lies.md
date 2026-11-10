# Conf42 Observability 2026 - when green stopped meaning healthy

Conf42 Blog, 2026-09-11. https://www.conf42.com/obs2026/observability-2026-roundup-agents-green-lies

In short: Conf42 Observability 2026 in review, 20 talks on tracing AI agents, dashboards that lie, eBPF, telemetry pipelines and using signals to test.

[Conf42 Observability 2026](https://www.conf42.com/obs2026) went out on September 10, 2026 with 20 talks, and a single complaint kept surfacing in different accents: the dashboard said everything was fine. Sometimes the culprit was an AI agent reporting 200 OK while answering wrong, sometimes a payment provider, sometimes a fallback path nobody had ever exercised. Speakers from PagerDuty, Adobe, Google, Snowflake, ServiceNow, General Motors, Harness and a crowd of observability vendors showed what to measure instead.

## Green is a claim, not a proof

Diamond sponsor Harness opened with [Uma Mukkara](https://www.conf42.com/Observability_2026_Uma_Mukkara_resilience_testing_enterprise), head of resilience testing and LitmusChaos co-founder, on why dashboards can only show paths that have already run. His case study is a third-party API failing over to a redundant path that never carried traffic, a retry storm turning a partial outage into a full one, and a team debugging an hour nobody instrumented. The cure is an inventory of untested paths and controlled experiments to fill it.

[Eleftheria Batsou](https://www.conf42.com/Observability_2026_Eleftheria_Batsou_healthchecks_outages_dependencies) (UptimeRobot) took the outside-in version: your app returns a healthy 200 while customers can't pay because Stripe is degraded. The thing that broke is the payment provider, the identity provider, the CDN or the LLM API you added last quarter. [Victoria Nduka](https://www.conf42.com/Observability_2026_Victoria_Nduka_accessibility_slos_goldensignals) (VictoriaMetrics) proposed accessibility as a fifth golden signal, so regressions show up in SLOs instead of in an audit weeks later. And [Sylvain Kalache](https://www.conf42.com/Observability_2026_Sylvain_Kalache_burnout_oncall_sre) (Rootly) pointed the same discipline at people: we have liveness probes for every service, but the engineer holding the pager gets "How are you doing?" and always answers "Fine."

## Agents need traces of their own

The busiest track was agent observability. [Sabith K Soopy](https://www.conf42.com/Observability_2026_Sabith_K_Soopy_agents_debugging_tracing) (Stackgen) put it best in one line of his abstract: traditional APM won't tell you an agent burned 40k tokens narrating a wrong answer. He showed the spans Stackgen uses to follow an agent through plan, gather and present, with per-tool cost and latency. [Emerson Braun](https://www.conf42.com/Observability_2026_Emerson_Braun_agents_llms_observability) (Plan A Technologies) followed one agent run from request to outcome and instrumented the context it received, the decisions it made and where it started to drift.

[Elliot Gardiner](https://www.conf42.com/Observability_2026_Elliot_Gardiner_agents_codegeneration_tracing) (Code Telemetry) treated coding agents as long-running processes that search, edit, test, retry and delegate to subagents, and argued that token counts and adoption are the wrong metrics for them. [Princewill Kalio](https://www.conf42.com/Observability_2026_Princewill_Kalio_llms_rag_distributedsystems) (Dockie) said the quiet part out loud in his title: AI systems are distributed systems now, with retrieval pipelines, vector stores and background workers, and they deserve distributed-systems tracing rather than print statements.

## The 3am page for code no human wrote

Two talks dealt with the operational aftermath. [Ralph Bird](https://www.conf42.com/Observability_2026_Ralph_Bird_sre_agents_incidentresponse) (PagerDuty) opens at 03:47 with a pager firing over code written by one agent, shipped by another, never seen by a human, after the SRE agent has already failed. [Artemis Leonardou](https://www.conf42.com/Observability_2026_Artemis_Leonardou_debugging_agents_codegeneration) (NOFire AI) lived it: an agent-written change passed review and CI, then took a production path down for about three hours. Nothing in the diff was wrong on its own; the failure lived in the combination, and the dashboards could say what and where but not why.

## Measuring whether the AI was right

[Srikanth Devarakonda](https://www.conf42.com/Observability_2026_Srikanth_Devarakonda_llms_evals_benchmarks) (Adobe) connected generative AI evaluation (factual accuracy, grounding, safety, task completion) to observable system performance and business outcomes instead of static benchmarks. [Arjun D Sureshbabu](https://www.conf42.com/Observability_2026_Arjun_D_Sureshbabu_llms_hallucinations_nlp) (Snowflake) shared lessons from a human-in-the-loop architecture for legal, compliance and privacy NLP, where a hallucination has a regulatory cost. [Ravi Chandra](https://www.conf42.com/Observability_2026_Ravi_Chandra_llms_analytics_semanticlayer) (Google) went after the semantic layer behind analytics agents, using feedback to keep a static, expert-curated ontology from missing the long tail of what users actually ask.

## Pipelines, kernels and the bill

On the plumbing side, [Anais Dotis](https://www.conf42.com/Observability_2026_Anais_Dotis_ebpf_linux_networking) (groundcover) gave a hype-free explanation of eBPF and how kernel programming escaped the kernel into monitoring and security. [Rita Lopes](https://www.conf42.com/Observability_2026_Rita_Lopes_metrics_logging_tracing) (Gigapipe) started from the familiar four-backend stack of Prometheus, Loki, Tempo and Pyroscope, and the trade-off between observing everything and paying for it. [Diana Todea](https://www.conf42.com/Observability_2026_Diana_Todea_opensource_observability_sustainability) (VictoriaMetrics) built a green observability pipeline entirely from open source and described how she got there by contributing upstream. [Emmanuela Opurum](https://www.conf42.com/Observability_2026_Emmanuela_Opurum_cloudnative_architecture_tracing) (SoftNet Technologies) argued for designing observability into cloud architectures rather than bolting it on, and [Joshua Fox](https://www.conf42.com/Observability_2026_Joshua_Fox_kubernetes_autoscaling_reliability) (DoiT International) went beyond HPA and VPA for Kubernetes autoscaling that cuts waste without hurting reliability.

## Telemetry as test input

Two talks turned signals into tests. [Vasuki Uday Kiran Vudathala](https://www.conf42.com/Observability_2026_Vasuki_Uday_Kiran_Vudathala_loadtesting_performance_capacityplanning) (ServiceNow) replaced interviews and spreadsheet guesses about peak traffic with workload models built from observability data. [Sumaiyya Fatima](https://www.conf42.com/Observability_2026_Sumaiyya_Fatima_automotive_embedded_simulation) (General Motors) applied observability-driven validation to hardware-in-the-loop testing for software-defined vehicles, where functionality emerges from many domains talking to each other.

## Sponsors and where to watch

Thanks to [Harness](https://www.harness.io/), the Diamond sponsor, and [SREday](https://www.sreday.com/) at Gold. Every talk is on the [event page](https://www.conf42.com/obs2026) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrBA6AiE2f0hmsnFk5oGfFjb).

The series continues with [Conf42 Observability 2027](https://www.conf42.com/obs2027). Bring the dashboards you trust least.
