# A four-tool observability stack for small teams on Kubernetes

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/lean-team-observability-stack-on-kubernetes

In short: Vignesh Iyer of NVIDIA at Conf42 Observability 2025 builds a low-cost stack from Fluentd, Prometheus, Jaeger and Grafana, plus three pitfalls to avoid.

You do not need an enterprise contract to see inside a distributed system. At Conf42 Observability 2025, Vignesh Iyer of NVIDIA showed small teams how to stand up a working observability stack on Kubernetes from four open-source tools (Fluentd, Prometheus, Jaeger and Grafana) with a handful of commands each, and then spent the most valuable minutes on how teams drown in their own signals.

It is pitched squarely at teams with little budget and a cluster to look after, and it says so in its first sentence. Think of it as a good first talk on assembling the pieces, with opinions attached.

## Four pillars, one tool each

Vignesh frames the stack around four pillars, each answering one question:

- **Logging** tells you what is happening in the system right now. His pick is Fluentd as the log aggregator.
- **Metrics** show how the system behaves over time. Prometheus, which he calls one of the most used components in Kubernetes clusters.
- **Tracing** finds the bottleneck in a request's path. He chose Jaeger over OpenTelemetry here because it is easier for a small team to set up.
- **Dashboards** decide how quickly you can act on all of it. Grafana, pulling data from the other three.

The Jaeger-over-OTel choice is worth noticing. It is a deliberate trade of future flexibility for setup speed, and for a three-person team that can be the right call.

## Install paths you can copy

For each tool he shows both the `kubectl apply` route, using the manifests the project maintains so you stay on the latest version, and the Helm route. Then the small details that trip people up: point applications at Fluentd's forward port and emit JSON logs so parsing stays easy; override the Prometheus Helm values to declare scrape targets for your services; send spans from the client libraries to the Jaeger agent by its in-cluster service name (his Python example used port 6831); and register Prometheus, Jaeger and your logs as Grafana data sources in the Helm config.

None of this is novel, but having it in one place in the right order saves an afternoon of tab-hopping.

## Alert on everything and you will hear nothing

The pitfalls section is where the talk earns its slot. First, alert fatigue. Vignesh described a previous company where alerts were set up for every issue; the team mailbox filled so fast that people stopped receiving alerts altogether and missed the ones that mattered. His rule: alert only on the specific issues you need to act on, and leave the rest to logging.

## Sample less, show less

Second, do not oversample metrics. Sending data every second turns signal into noise and grows your storage for no insight; he suggests something like once a minute as a reasonable balance, depending on the system.

Third, dashboard hygiene. The instinct that more panels mean more insight is, in his words, far from the truth. Build each dashboard for its audience: a high-level view of system health for a manager, deeper application detail and log access for a developer. A dashboard that tries to serve everyone serves the screenshot in the incident review.

## Who should watch

Small teams, side projects, startups and anyone who has been told there is no budget for observability and needs a credible starting point. Teams already running a mature OpenTelemetry pipeline will know the material, though the alerting and dashboard advice is a useful reminder for anyone.

## Related Conf42 talks

- Phil Wilkins' [Making Logs Work for you with Fluentd](https://www.conf42.com/Cloud_Native_2021_Phil_Wilkins_logs_fluentd) goes much further into the logging pillar.
- Prathamesh Sonpatki's [The Hidden Cost of Instrumentation](https://www.conf42.com/DevOps_2023_Prathamesh_Sonpatki_cost_instrumentation) pairs well with the oversampling warning.
- Pradeep Gaddamidi's [Mastering the Chaos](https://www.conf42.com/DevOps_2025_Pradeep_Gaddamidi_cloud_cost_monitoring) on keeping monitoring and logging costs under control.

[Watch Vignesh Iyer's talk](https://www.conf42.com/Observability_2025_Vignesh_Iyer_lightweight_teams_system)

[Watch the talk on YouTube](https://youtu.be/9VU_2ud21yA).

## Watch the talk

[Building lightweight observability system for Lean Teams](https://www.conf42.com/Observability_2025_Vignesh_Iyer_lightweight_teams_system) at Conf42 Observability 2025.
