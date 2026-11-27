# Catch errors in the middleware, before customers call you

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/middleware-first-error-detection-mttr

In short: Sreelatha Pasuparthi of Liberty Mutual at Conf42 Platform Engineering 2025 on moving error detection into application middleware with ML-ranked alerts.

If your first alert is an angry phone call from your biggest client, your monitoring is watching the wrong layer. At Conf42 Platform Engineering 2025, Sreelatha Pasuparthi, Principal Software Engineer at Liberty Mutual Insurance, explained how moving error detection into application middleware, and ranking alerts with machine learning, cut detection from hours to minutes. Her abstract puts the result at an 88.5% drop in MTTR, from 162-minute detection delays, across 230K users.

## The Tuesday that started it

The talk opens with an incident story. A flagship e-commerce platform had been failing quietly for over two hours, mis-processing orders and corrupting customer data. Nothing in the extensive monitoring estate noticed; support tickets and a call from the largest enterprise client did. Another catalyst: a database corruption issue that went undetected for nearly three hours.

Meanwhile the alerting that did fire was mostly noise. The average developer got more than 40 alerts a day, and more than three quarters needed no action or duplicated known issues. Engineers became desensitised, on-call turnover grew, and the team had dozens of tools and hundreds of dashboards but still could not tell when things were actually broken for users.

## Detect where the error happens

The central insight is a single sentence worth putting on a sticky note: "Real errors happen in code, not in infrastructure metrics." CPU, memory, network and database graphs are lagging indicators. By placing error capture in the request pipeline, alongside authentication, validation, business logic and persistence middleware, the system records each failure at the moment it occurs, with the user session, the operation, the input and the execution path attached.

The middleware works in phases: immediate capture with minimal processing, enrichment with more context, ML classification, then routing. Each phase is built to fail safely, so if the error reporter itself breaks, the original request carries on. Monitoring that can take production down is not monitoring.

## Not every timeout is an incident

Classification replaces static thresholds. The models look at temporal patterns, correlations between error types, how errors hit different user cohorts, and learn from past incidents and engineer feedback. Priority is dynamic: one user hitting a database timeout is minor, hundreds hitting it at once is an infrastructure problem. The inputs she lists are error frequency and correlation, business context of the affected users, similar past errors and their fixes, and current system state including load and scheduled maintenance.

Routing then respects how people work: developers get Slack, GitHub issues and IDE plugins; operations get runbooks, incident management and PagerDuty escalation; management gets dashboards and summaries. The system learns which channel produces the fastest response for each alert type.

## One root cause, one alert

Cascade handling is the other big win. A connection pool exhaustion produces service timeouts and then frontend exceptions, and traditional monitoring pages for each symptom separately. Because the middleware captures enough context, it can link those downstream alerts to the root cause in real time and keep the incident channel readable. Baselines are dynamic too, learning daily, weekly and seasonal patterns and accounting for deployments and maintenance windows.

## How to roll it out

Her roadmap is pragmatic. Pilot on one well-understood application of moderate complexity, with basic capture and manual routing. Then build reusable middleware components and standards for classification and routing across the portfolio. Only then add ML classification, smart routing and cascade suppression. The success factors she credits are executive support through a period when development velocity dipped, low performance overhead, fail-safe design, and a culture that treats error detection as part of application design.

## Who should watch

Teams drowning in alert noise, SREs whose dashboards are green while customers complain, and platform engineers deciding where instrumentation should live. It describes the architecture rather than a specific vendor tool, so it transfers to whatever stack you run.

## Related Conf42 talks

- [Kirti Ranjan Parida and Sarav Jagadeesan on AI and data pipelines to reduce cost and MTTR](https://www.conf42.com/Observability_2025_Kirti_Ranjan_Parida_Sarav_Jagadeesan_mttr_pipelines_reduce) at Conf42 Observability 2025.
- [Israel Heringer on reliable monitoring and alerts for cloud applications](https://www.conf42.com/Cloud_Native_2024_Israel_Heringer_reliable_monitoring_alerts) at Conf42 Cloud Native 2024.

[Watch Sreelatha Pasuparthi's talk](https://www.conf42.com/Platform_Engineering_2025_Sreelatha_Pasuparthi_middleware_mttr_error), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/nMLdku1n7zc).

## Watch the talk

[Building Bulletproof Error Detection: A Middleware-First Approach to Reducing MTTR by 88.5%](https://www.conf42.com/Platform_Engineering_2025_Sreelatha_Pasuparthi_middleware_mttr_error) at Conf42 Platform Engineering 2025.
