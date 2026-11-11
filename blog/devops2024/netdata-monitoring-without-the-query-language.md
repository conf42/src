# Observability standards stop at data exchange, and that's the problem

Conf42 Blog, 2024-01-26. https://www.conf42.com/blog/devops2024/netdata-monitoring-without-the-query-language

In short: Costa Tsaousis (Netdata) at Conf42 DevOps 2024 on why open standards don't fix monitoring, and Netdata's per-second, zero-config, ML-at-the-edge answer.

OpenTelemetry, the CNCF and the W3C have made it easy to move telemetry between tools. At Conf42 DevOps 2024, Costa Tsaousis, founder and CEO of Netdata, argued that this is the easy part: the real cost of monitoring sits in everything around the data (query languages, cardinality, dashboards, alert tuning), and nobody has standardised that. His answer is opinionated, zero-configuration monitoring, and he spends the second half showing how Netdata does it.

It is a vendor talk with a real thesis, and the first half stands on its own.

## Where does the time in monitoring actually go?

He walks through the classic stack: exporters, a time series database, a logs database, a dashboard tool, an alerting engine. Each hides work. The TSDB needs care for cardinality, memory, disk I/O, clustering and high availability. The logs store adds indexes and retention. The dashboards need you to learn a query language and the visualisation tool's quirks. At scale you add cost management, noise and compliance; in a team you add policies, change management and documentation.

To make the point he asked ChatGPT for two word clouds. The first, what monitoring engineers think about daily: scrape intervals, label relabelling regexes, federation, TSDB I/O bottlenecks. The second, what people running infrastructure should think about: incident response, service availability, cost optimisation, client satisfaction. Today's tools, he says, force us to live in the first list.

Standards bodies focus on the arrow between applications and databases. Useful, he concedes, but most of the complexity is outside it. And the analysts' answer, a DevOps engineer who is at once data scientist, software engineer and network architect, is a utopia. The result: monitoring quality mirrors the skills of the team, and is often severely under-engineered or, in his word, illusional. He includes himself: before Netdata he had a good team and plenty of dashboards and still could not troubleshoot with them.

## What does Netdata do differently?

The premise is that our infrastructures are built from the same Lego bricks (operating systems, databases, web servers, standard libraries), so the tool can ship knowing them. From there:

- Everything collected every second, high-fidelity rather than a helicopter view. "I wanted to kill the console for monitoring," Costa Tsaousis said at Conf42 DevOps 2024: every metric you would reach for in a console tool should be in the monitoring system.
- Every metric visualised automatically, with filtering and group-by controls on each chart instead of a query language.
- 344 predefined, dynamic alerts that attach themselves to disks, interfaces, databases and web servers as they are discovered.
- Installable mid-crisis: no anomaly history yet, but correlation, similarity search and journal log exploration work immediately.

Each agent is a full monitoring stack in one binary (collector, TSDB, visualisation, alerting, ML, logs). Agents can stream to a parent, parents to grandparents, and parents can be clustered in a loop, relying on replication instead of a write-ahead log.

## The numbers and the ML

In Netdata's stress test against Prometheus (500 servers, 40,000 containers, about 2.7 million metrics per second, both collecting per second), he reports 35% less CPU, half the memory, 12% less bandwidth and 98% less disk I/O for Netdata, and a smaller storage footprint thanks to up to five downsampling tiers. These are the vendor's own benchmarks, so read them as such.

The anomaly detection is unsupervised and trained at the edge, per metric, because a shared model of what a healthy Postgres looks like would be full of false positives. Netdata trains 18 models over roughly the last 57 hours, and a sample counts as anomalous only when all 18 agree. The anomaly rate is stored alongside each time series, which powers an anomaly-rate button across the whole dashboard and the Anomaly Advisor: highlight a spike in the host-level anomaly chart and get every metric ranked by anomaly rate for that window. "The whole point is to have your aha moment within the top few items," Costa Tsaousis said at Conf42 DevOps 2024.

He closes on footprint: about 5% of a single CPU core and around 100 MB of RAM per node.

## Who should watch

SREs and platform engineers tired of maintaining the monitoring stack rather than the system it watches, and anyone evaluating Netdata against a Prometheus and Grafana setup. Expect a strong opinion and a product walkthrough.

## Related Conf42 talks

- Samuel Arogbonlo on [logs and metrics with Prometheus](https://www.conf42.com/Site_Reliability_Engineering_2022_Samuel_Arogbonlo_logmetrics_prometheus) at Conf42 SRE 2022.
- Shahar Azulay on [Kubernetes observability with eBPF](https://www.conf42.com/Cloud_Native_2023_Shahar_Azulay_kubernetes_observability_ebpf) at Conf42 Cloud Native 2023.
- Adam Furmanek on [observability for PostgreSQL and MySQL](https://www.conf42.com/DevOps_2024_Adam_Furmanek_observability_postgresql_mysql) at Conf42 DevOps 2024.

[Watch Costa Tsaousis's talk](https://www.conf42.com/DevOps_2024_Costa_Tsaousis_observability_standardization)

## From Netdata

Netdata is open source; the agent includes the machine learning features described here, and Netdata Cloud offers a combined view across agents with the same dashboard.

- [Netdata website](https://www.netdata.cloud/)

[Watch the talk on YouTube](https://youtu.be/LpW4uhFGPEI).

## Watch the talk

[Observability Standardization: the elephant is still in the room!](https://www.conf42.com/DevOps_2024_Costa_Tsaousis_observability_standardization) at Conf42 DevOps 2024.
