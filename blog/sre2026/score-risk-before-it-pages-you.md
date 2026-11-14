# A risk score that pages you before the SLO breaks, not after

Conf42 Blog, 2026-02-26, updated 2026-11-09. https://www.conf42.com/blog/sre2026/score-risk-before-it-pages-you

In short: Oreoluwa Omoike of JPMorgan Chase at Conf42 SRE 2026 on risk-aware SRE scoring failure x impact / time to impact, with real before-and-after numbers.

Most alerting is very good at screaming after something breaks and bad at noticing that something is about to. At Conf42 Site Reliability Engineering 2026, Oreoluwa Omoike, Site Reliability Engineer at JPMorgan Chase, presented a risk-aware decision framework that scores each risk as probability of failure times business impact, divided by time to impact, and lets a policy engine decide whether to log, scale or page.

In the case study he shares, mean time to detect fell from 14 minutes to 2.3, and false positives dropped from 70% of alerts to 18%.

## The 2am loop you have already lived

Omoike opens with the story every on-call engineer knows: the 2am page, 45 minutes to find the root cause, a hotfix, back to bed, and two weeks later the same class of failure in a slightly different disguise. His three baseline numbers frame the problem: 14 minutes on average just to detect an incident, 70% of alerts that turn out to be noise, and 45 minutes to mitigate once you know. The 70% is what slowly trains engineers to stop caring, which is how the real alerts get buried.

His argument is that the deeper issue is the mental model, not the tooling.

## Observe, score, decide, act

The framework has four steps, and the first is deliberately boring: observe with the stack you already run (metrics, traces, logs, burn rate). Scoring is where AI comes in. Instead of watching for threshold breaches, the system computes a live risk score: failure probability from an ML model, multiplied by business impact (his example is a checkout outage costing a set amount per hour), divided by time to impact. A risk six hours out scores very differently from one ten minutes away.

A policy engine then decides, like a tiered response playbook that runs in milliseconds rather than a human flipping through a runbook at 2am. Then the system acts, consistently, including when nobody is watching.

## Three AI patterns, bolted on the side

The scoring rests on three patterns. Anomaly detection with isolation forests or LSTMs trained on baseline traffic catches behaviour that drifts rather than crossing a line. He likes isolation forests because they are lightweight and engineers can usually tell why one fired; LSTMs earn their keep with richer sequential signals. SLO burn rate prediction forecasts when the error budget runs out, which turns "we're burning" into a deadline you can act on. Change risk scoring gives every deploy, config change and feature flag a blast-radius score before it reaches production, using gradient-boosted models trained on historical incidents.

All three run as sidecars that plug into Prometheus, OpenTelemetry and Grafana. He is emphatic on this: pitch a replacement of the whole observability stack and the project is dead on arrival.

## The numbers, and the pitfalls

The case study is an e-commerce platform handling 50 million events a day, run for six months through the kind of peaks that include Black Friday and flash sales. Mean time to detect went from 14 minutes to 2.3 (84%), false positives from 70% to 18%, mean time to resolve from 45 minutes to 11 (76%), and SLO breaches from 22 a month to four (82%). On-call satisfaction surveys improved too.

The pitfalls section is the part worth taking notes on. Models drift with campaigns, launches and seasons, so retrain weekly on a rolling window and track the population stability index. Don't wire it straight to paging, or you rebuild the alert storm you set out to kill: run log-only for two weeks, then auto-scaling, then paging, with a human override always available. Keep scoring under about five milliseconds with batching, asynchronous evaluation and feature caching for high-cardinality labels. And mind data quality: if 30% of a metric's data is missing, don't score it, because "a bad score is worse than no score." Build data quality monitoring before the scoring model.

## Who should watch

Teams drowning in noisy alerts, and anyone trying to get from SLO dashboards to action, will find a concrete, incremental recipe. His advice for starting is pleasingly small: one isolation forest model and one Prometheus metric. "Perfection is the enemy of shipping."

## Related Conf42 talks

- [Techniques for SLOs and Error Budgets at Scale](https://www.conf42.com/Observability_2023_Fred_Moyer_slos_error_budgets_scale) by Fred Moyer.
- [Guardrails That Outlive the Rollout: Adaptive Statistical Risk Control for Feature Flags](https://www.conf42.com/Feature_Flags_2026_Rakshay_Pawar_guardrails_rollout_risk) by Rakshay Pawar.
- [Predictive Observability: Prevent Supply Chain Outages Before They Break Your Production](https://www.conf42.com/DevOps_2026_Raghu_Bhupatiraju_predictive_analytics_outages) by Raghu Bhupatiraju.

[Watch Oreoluwa Omoike's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Oreoluwa_Omoike_driven_risk_aware) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/4BELqysbNsA).

## Watch the talk

[AI-Driven Risk-Aware Decision-Making for Scalable Reliability Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Oreoluwa_Omoike_driven_risk_aware) at Conf42 Site Reliability Engineering (SRE) 2026.
