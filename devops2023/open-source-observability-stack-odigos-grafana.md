# Day-one observability for microservices, built from open source only

Conf42 Blog, 2023-01-27. https://www.conf42.com/devops2023/open-source-observability-stack-odigos-grafana

In short: Shubham Srivastava (Zenduty) at Conf42 DevOps 2023 on wiring Odigos, Prometheus, Loki, Tempo and Grafana into day-one observability without code changes

Observability is usually sold as a big platform project. Shubham Srivastava, who leads developer relations at [Zenduty](http://www.zenduty.com/), spent his Conf42 DevOps 2023 talk showing the opposite: a local Kubernetes cluster, a microservices demo app and a fully open-source stack (Odigos, Prometheus, Loki, Tempo and Grafana) that gives you correlated metrics, traces and logs within minutes and without touching application code.

The first third is the why; the rest is a speedrun you can follow along with.

## Why observability from day one?

Srivastava's argument is about complexity. Five or so years earlier, a typical system was a classic LAMP stack: one big database, an app tier, a web layer, caching and basic load balancing. You could predict most failures and build a few dashboards that answered nearly every root-cause question. Microservices, polyglot persistence and containers replaced that with a long list of unique questions, and failure modes that combine in ways nobody planned for.

Without observability, teams guess: one theory, one change, then the next, while customers wait. Kubernetes self-healing helps, he says, but can also hide a system running suboptimally, and bottlenecks can trigger premature autoscaling.

"Indeed, there are cases where the first signs of failure is an astronomically high cloud computing bill," Shubham Srivastava said at Conf42 DevOps 2023.

He is also clear that the goal is not hoarding data: observability means the right metrics for the key performance indicators of your software, plus the ability to ask new questions on the fly.

## What does the stack look like?

There is no single database that stores logs, traces and metrics well, so the backend is three stores and one view:

- **Prometheus** for metrics, as a time series database with flexible queries and alerting.
- **Loki** for logs, horizontally scalable and multi-tenant, inspired by Prometheus.
- **Tempo** for distributed traces, needing only object storage and integrating tightly with the other two.
- **Grafana** for dashboards and exploration across all three.

On top sits **Odigos**, an open-source observability control plane. It does two jobs: automatic instrumentation that produces traces and metrics without code changes, and collector management, deploying and scaling collectors according to application traffic so nobody hand-tunes them.

## How long does the setup take?

The prerequisites are kind (local Kubernetes clusters in Docker containers, a go install and a create cluster command if you have Go 1.17+ and Docker), kubectl and Helm. The target application is a fork of Google's Bank of Anthos microservices example, deployed with one kubectl apply. One Helm chart installs Tempo, Prometheus, Loki and a pre-configured Grafana; a second installs Odigos, whose UI you reach with a port-forward.

Odigos offers two selection modes. Opt-in instruments only the applications you pick. Opt-out instruments everything, including every application deployed in future, with exclusions where you need them; the demo uses opt-out. Add Loki, Prometheus and Tempo as destinations, wait a few seconds while Odigos deploys collectors, and the data starts flowing.

## What do you get at the end?

In Grafana he walks the classic path from overview to root cause:

1. A Tempo service graph of the application's services.
2. Request rate and latency metrics for one service. Odigos reports three kinds: application metrics (HTTP requests, latency, database connections), language runtime metrics (threads, heap) and host metrics (CPU, memory, disk).
3. Exemplars on a latency histogram, the small diamonds that link a metric data point to a specific trace, opened in Tempo to see how long each part of the request took, with database queries and HTTP headers attached.
4. Loki queries filtered by that trace ID, to read the logs for exactly that request end to end.

## Where does Zenduty come in?

Only at the end, and briefly. Once you can detect and diagnose, the remaining risk is human: miscommunication and slow coordination during the firefight. That is where he suggests teams consider whether incident response tooling such as Zenduty would help keep responders on the same page.

## Who should watch

Teams without an observability stack who want a working reference on a laptop in an afternoon, and anyone curious how far automatic instrumentation gets you before you write a single span by hand. Experienced Grafana users will mostly enjoy the Odigos part.

## Related Conf42 talks

- Bruno Ferreira on [the OpenTelemetry Collector](https://www.conf42.com/DevOps_2024_Bruno_Ferreira_observability_opentelemetry_collector) at Conf42 DevOps 2024.
- Jhonnatan Gil Chaves on [observability metrics with open source tools](https://www.conf42.com/Kube_Native_2023_Jhonnatan_Gil_Chaves_observability_metrics_open_source_tools) at Conf42 Kube Native 2023.
- Nicolas Fränkel on [OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing) at Conf42 DevOps 2023.

[Watch Shubham Srivastava's talk](https://www.conf42.com/DevOps_2023_Shubham_Srivastava_observability_microservices_open_source)

## From Zenduty

Zenduty is an incident management and response orchestration platform for DevOps, SRE and production engineering teams.

- [Zenduty website](http://www.zenduty.com/)

[Watch the talk on YouTube](https://youtu.be/n9Q-LONGcec).

## Watch the talk

[Observability of Microservices using Open Source Solutions](https://www.conf42.com/DevOps_2023_Shubham_Srivastava_observability_microservices_open_source) at Conf42 DevOps 2023.
