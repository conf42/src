# Microservices broke the dotted metric name; labels fixed it

Conf42 Blog, 2021-04-29. https://www.conf42.com/blog/cloud2021/microservices-monitoring-labels-not-dots

In short: Dotan Horovits (Logz.io) at Conf42 Cloud Native 2021 on why StatsD and Graphite stop scaling with microservices, and what to require instead

A metric called prod.webserver.html.request.total.count was fine when the web server was one machine. At Conf42 Cloud Native 2021, Dotan Horovits of Logz.io, organiser of CNCF Tel Aviv and host of the OpenObservability Talks podcast, explained why that naming scheme falls apart once the web server is a service spread over pods and nodes, and laid out three requirements for a monitoring system that copes.

It is a compact talk, and once the short company intro is done it is vendor-neutral. As he put it, "enough vendor talk. Let's talk about monitoring microservices."

## What changed since StatsD and Graphite?

The old setup: apps push metrics over UDP to StatsD, which aggregates them and sends them over TCP to Graphite for storage and graphs. The metric name is a hierarchy that mirrors the deployment: environment, server, service, metric.

Horovits names three shifts that broke it. Microservices exploded the number of things to monitor: the Amazon and Netflix death-star diagrams, but even a modest monolith becomes dozens of services, each a cluster, each with its own language, database and release cadence. Cloud native added dimensions (pod, node, namespace, version, cluster) plus new critical systems to watch, from the container runtime to the kubelet, kube-proxy, etcd and the scheduler. And every system now leans on a pile of open source and cloud services, from databases to message brokers, that also need monitoring and keep changing.

## Requirement one: query any dimension you didn't plan for

In dot notation, a new dimension means a new metric name. Want the request count for pod 7 on node 2? That is another metric. Want it for the whole service? Another one. Want all the 500s across a set of servers, grouped by something you didn't pre-aggregate? Good luck.

The fix is the labelling model that Prometheus introduced with PromQL: one metric, http_requests_total, with key-value labels for environment, service and server. Filter by server to see one pod, by service to see the whole thing, or combine them. With real web apps carrying labels for method, status code and endpoint, the number of ad hoc questions you can ask becomes, in his words, almost endless.

## Requirement two: scrape and discover, don't push

Asking every microservice, and every third-party tool whose code you don't own, to push metrics is impractical. Prometheus flipped it: discover the targets and scrape them. That works because of OpenMetrics, an open standard based on the Prometheus format, in the CNCF sandbox and proposed to the IETF. Kafka, RabbitMQ, MongoDB, MySQL, Apache, NGINX and Jenkins all expose metrics in that format, usually on a /metrics endpoint you can open in a browser. Prometheus also discovers targets through the Kubernetes API, Consul and cloud providers.

## Requirement three: scale beyond one node

Prometheus is by design a single-node installation. You can federate and shard instances, which gets complicated, or use remote write to send data to a long-term store. There is a wide choice, including the CNCF's own Thanos and Cortex, self-managed or as a service.

## Who should watch

Engineers still running StatsD and Graphite, or anyone who needs to explain to their team why high cardinality matters. Prometheus users will know the material; it works well as a short, clear argument for the model. It is a 2021 snapshot of the tooling.

## Related Conf42 talks

- Piyush Verma on [building an OpenMetrics exporter](https://www.conf42.com/Site_Reliability_Engineering_2022_Piyush_Verma_openmetrics_exporter) at Conf42 Site Reliability Engineering 2022.
- Samuel Arogbonlo on [logs and metrics with Prometheus](https://www.conf42.com/Site_Reliability_Engineering_2022_Samuel_Arogbonlo_logmetrics_prometheus) at Conf42 Site Reliability Engineering 2022.
- Phil Wilkins on [making logs work for you with Fluentd](https://www.conf42.com/Cloud_Native_2021_Phil_Wilkins_logs_fluentd) at Conf42 Cloud Native 2021.

[Watch Dotan Horovits's talk](https://www.conf42.com/Cloud_Native_2021_Dotan_Horovits_monitoring_microservices)

## From Logz.io

Logz.io runs a SaaS platform for cloud native observability: send logs, metrics and traces to a managed service for storage, indexing, analytics and visualisation, built on open source such as Kibana, Elasticsearch, Prometheus, Jaeger and OpenTelemetry.

- [logz.io](https://logz.io)

[Watch the talk on YouTube](https://youtu.be/XatQZUjI9LI).

## Watch the talk

[Monitoring Microservices The Right Way](https://www.conf42.com/Cloud_Native_2021_Dotan_Horovits_monitoring_microservices) at Conf42 Cloud Native 2021.
