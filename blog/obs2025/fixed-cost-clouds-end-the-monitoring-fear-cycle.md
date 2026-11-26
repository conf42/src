# The monitoring fear cycle, and how fixed-cost clouds break it

Conf42 Blog, 2025-05-15. https://www.conf42.com/blog/obs2025/fixed-cost-clouds-end-the-monitoring-fear-cycle

In short: Denish Tomar of Qumulus at Conf42 Observability 2025 on why metered observability makes teams self-censor dashboards, and a fixed-cost alternative.

You are halfway through debugging a production incident when finance pings you: the cloud bill just went up by $5,000, what happened? Denish Tomar, Developer Relations Engineer at Qumulus, opens his Conf42 Observability 2025 talk with that moment and argues that per-unit observability pricing quietly makes systems less observable, because engineers start rationing the very data they need.

This is a short talk from a vendor. The diagnosis applies to any metered stack; the proposed fix is the fixed-cost platform Tomar works with.

## The monitoring fear cycle

Tomar's central diagram is a loop most teams have lived through. Deploy a service with basic monitoring. An incident shows visibility is not enough, so add metrics, logs and traces. The bill spikes, finance asks for cuts, monitoring gets scaled back. Another incident. Repeat.

He gives an example from a team he worked with: great dashboards covering response times, error rates and database behaviour, until the service grew from 10 to 50 and monitoring costs climbed so much that they deleted dashboards and sampled metrics at 10%.

## What rationing costs you

The list of side effects is the strongest part of the talk. Self-censoring, where engineers do not build the dashboards they need. Delayed detection, because the right data is not collected. Blind debugging when an incident hits. Crisis monitoring, where full telemetry only gets switched on during an emergency. And a knowledge gap, because new team members never learn tools that are treated as scarce.

His incident timeline makes it concrete: users report slowness at 10:00, the team checks basic metrics at 10:15, asks permission to enable detailed monitoring, waits for data, and pinpoints a database bottleneck at 11:15. Nearly two hours of impact, most of it spent waiting for visibility. The next day, detailed monitoring is scaled back again. He also recalls a senior engineer spending three hours optimising monitoring to save $200 a month, which is a strange use of a senior engineer.

## Four meters on every byte

Tomar breaks the cost down to the architecture: agents collect data, ship it to a central service, which stores and indexes it and runs queries for dashboards and alerts. That creates four separate cost drivers. Data transfer, especially across regions or to third-party tools. Ingest processing for parsing and indexing. Storage, particularly at high resolution. And query costs, where you can end up paying to read your own data. Add unpredictability from traffic spikes or a chatty bug, and teams build deliberately compromised monitoring.

## Observability as a platform feature

His alternative is to make observability part of the infrastructure rather than a metered add-on. In a fixed-cost model, metrics and logs are collected automatically, with no transfer fees, predictable included retention and no charge for querying. He demos the platform he works with: a new server comes with dashboards for CPU, memory, disk I/O and network, 30 days of high-resolution history, and logs, with no setup step. Replaying the same incident, the alert fires within minutes, the database connection issue is found quickly and the fix lands in about 25 minutes, after which the team adds a dashboard for that scenario without asking anyone's permission.

## Who should watch

Engineers and engineering managers who have ever dropped a log level, shortened retention or killed a dashboard to save money. Even if you stay on a metered platform, the fear-cycle diagram is a useful thing to show the person who signs off the bill.

## Related Conf42 talks

- [Mastering the Chaos: A DevOps Engineer's Journey to Cost-Effective Cloud Monitoring and Logging](https://www.conf42.com/DevOps_2025_Pradeep_Gaddamidi_cloud_cost_monitoring) by Pradeep Gaddamidi at Conf42 DevOps 2025.
- [The Hidden Cost of Instrumentation](https://www.conf42.com/DevOps_2023_Prathamesh_Sonpatki_cost_instrumentation) by Prathamesh Sonpatki at Conf42 DevOps 2023.
- [How to build your own green observability pipeline](https://www.conf42.com/Observability_2026_Diana_Todea_opensource_observability_sustainability) by Diana Todea at Conf42 Observability 2026.

[Watch Denish Tomar's talk](https://www.conf42.com/Observability_2025_Denish_Tomar_dashboards_clouds_fun) or the [YouTube recording](https://youtu.be/tj7QhAu4-3k).

## Watch the talk

[Dashboards, Not Drama: How Fixed-Cost Clouds Made Observability Fun Again](https://www.conf42.com/Observability_2025_Denish_Tomar_dashboards_clouds_fun) at Conf42 Observability 2025.
