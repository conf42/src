# Fluentd can turn an innocent log line into an early warning

Conf42 Blog, 2021-04-28. https://www.conf42.com/blog/cloud2021/fluentd-logs-as-early-warnings

In short: Phil Wilkins (Capgemini) at Conf42 Cloud Native 2021 on Fluentd as a log unification layer that routes and alerts before the outage, not after

Most teams read their logs the way historians read diaries: after the fact. At Conf42 Cloud Native 2021, Phil Wilkins, Senior Consultant and Tech Evangelist at Capgemini and author of the Manning book Logging in Action, made the case for Fluentd as a log unification layer that can spot trouble while the log line is still being written, and route it to Slack before the disk fills up.

It is an introduction to Fluentd with a working demo and a couple of real deployment shapes, aimed at people who know Fluentd as "the Docker log driver" and not much more.

## Why do logs need a unification layer?

Wilkins starts with the observation that everyone means something different by logging. Infrastructure people watch CPU, memory and disk; app developers watch textual logs from SLF4J or Log4j; business owners want to know who did what and how many transactions went through. Then security runs its own SIEM tooling, and capacity still matters even with elastic scaling, because a runaway autoscaler shows up on the bill.

The result in most organisations is several overlapping tools and, as he put it, a database server with three different agents on it. A single unification layer that collects once and fans out to every team's tool keeps the network simpler and, in his words, keeps "your security guys" a lot happier.

## What Fluentd actually is

Fluentd is a pluggable framework where nearly everything is a plugin: inputs, parsers, formatters, filters, buffers, outputs and storage. Plugins are written in Ruby, it runs on Windows as comfortably as Linux or a Mac, and the output side reaches Splunk, Prometheus, Grafana, Kafka, Slack, email and more. Every event has three parts: a tag, a timestamp and a record.

Buffering and caching are the unglamorous bits that matter: networks blip, so Fluentd holds events until the connection comes back rather than losing them. Position files track how far each source has been read, so a restarted node carries on where it left off, log rotation included.

## EFK instead of ELK

The familiar stack is Elasticsearch, Logstash and Kibana. Swap Logstash for Fluentd and you get EFK. His reasons: Logstash has a bigger footprint, and Elastic does less to encourage third-party plugins, so the number of systems Logstash reaches is smaller "by quite a margin". Docker ships a Fluentd log driver, and packaged Fluentd setups for Kubernetes are close to out of the box. He is clear there is nothing wrong with ELK; EFK just gives you more options.

## The demo: jokes as log events

The demo runs two simulated applications (his open source log simulator replays a file of jokes as live log events) and two Fluentd nodes on one laptop. Node one tails both files, uses a record transformer to rename one app's event field to match the other's message field, writes an audit copy to a buffered file, and forwards to node two every 5 seconds. Node two accepts anything, writes everything to stdout and sends to Slack only the events that mention computer, upper or lower case.

"Node two says oldest computer can be traced back to Adam and Eve," Wilkins said at Conf42 Cloud Native 2021, reading the Slack channel as the alerts scrolled in. Replace the joke with a log message your team has learned means trouble, and you have a pre-emptive alert, possibly with a link to the runbook.

## Legacy apps are where this pays off

The sharpest idea is about systems nobody wants you to touch. Over time you learn that some harmless-looking log message is the precursor to a serious failure. Fluentd can match that message and act on it without changing the application. In the real deployment he showed, a legacy app migrated to the cloud kept writing Log4j files, a Fluent Bit node picked them up, and they were merged with AWS CloudWatch data, Jaeger traces, Elasticsearch and Kibana, with alerts to Slack and email.

He also covered scaling: concentrator nodes with failover, a Kubernetes DaemonSet running Fluentd, Fluent Bit co-located in pods or as a sidecar, and Fluentd feeding Prometheus and routing Prometheus alerts back into the log analytics platform so you can see when a problem was flagged.

## Who should watch

Ops and platform engineers who run more than one logging tool, and anyone stuck monitoring a legacy app they can't modify. Fluentd veterans will know most of it; the value is the architecture walkthroughs.

## Related Conf42 talks

- Dharmendra Ahuja on [Fluent Bit on Amazon EKS](https://www.conf42.com/Observability_2025_Dharmendra_Ahuja_fluent_eks_aws) at Conf42 Observability 2025.
- Leonid Yankulin on [structured logging in Google Cloud](https://www.conf42.com/DevSecOps_2022_Leonid_Yankulin_structured_logging_google_cloud) at Conf42 DevSecOps 2022.
- Shyamkumar Kalariya on [logs at 3AM](https://www.conf42.com/Observability_2024_Shyamkumar_Kalariya_logs_3AM) at Conf42 Observability 2024.

[Watch Phil Wilkins's talk](https://www.conf42.com/Cloud_Native_2021_Phil_Wilkins_logs_fluentd)

## From Capgemini

Phil Wilkins's team at Capgemini UK works with Oracle Cloud, Oracle middleware and open source.

- [capgemini.com](https://www.capgemini.com/gb-en/)

[Watch the talk on YouTube](https://youtu.be/-HbNuEAT6BA).

## Watch the talk

[Making Logs Work for you with Fluentd](https://www.conf42.com/Cloud_Native_2021_Phil_Wilkins_logs_fluentd) at Conf42 Cloud Native 2021.
