# Four golden signals, one Grafana dashboard and a cat generator

Conf42 Blog, 2022-06-10. https://www.conf42.com/blog/sre2022/golden-signals-and-a-cat-generator

In short: Michael McAllister (Teleport) at Conf42 Site Reliability Engineering 2022 on latency, traffic, errors and saturation as the starting point for actionable monitoring

Ten years ago Michael McAllister collected dozens of Nagios metrics per host, from CPU to inode usage, and got paged at night for any of them, without a clear idea which mattered. At Conf42 Site Reliability Engineering 2022, the SRE Team Lead at [Teleport](https://goteleport.com/) explained the four golden signals (latency, traffic, errors and saturation) as the foundation for monitoring that pages you only for things users feel, then built the dashboard live for a small Go service that serves cat pictures.

It's a lightning-length intro with a hands-on demo: Kubernetes, Prometheus, Nginx and Grafana, all running locally.

## Why monitor at all?

Before the signals, Michael lists the jobs monitoring does: alerting and troubleshooting, trend analysis (how fast are daily active users growing, how big is the database getting) for capacity planning, comparing before and after a rollout, and judging experiments shipped to a subset of users. Underneath all of them, monitoring should be the single place where anyone supporting a service can see its health.

His Nagios example shows the problem with metrics without meaning: an in-memory database using 70% of its RAM might be fine, the same number on an HTTP server might not.

"If I'm going to be paged, I want to make sure that it's actionable and clear what the issue is," Michael McAllister said at Conf42 Site Reliability Engineering 2022.

## The four signals, with the traps

**Latency** is the time to serve a request, and users notice it first; nobody waits long for a page or a shopping cart. The trap is mixing successful and failed requests. A back end goes down, the front end serves errors very fast, and your latency graph looks great. Track error latency too, since slow errors aren't much better than fast ones.

**Traffic** is demand: HTTP requests per second for a web server, images processed per second for an image pipeline. Whatever the service does, it should say how busy it is.

**Errors** include the explicit ones, like HTTP 500s or failed gRPC calls by status code, and implicit ones. A request slower than your SLO's one-second limit can count as a failure. Serving the wrong content with an HTTP 200 is still a failure.

**Saturation** is how full the service is, which means knowing your most constrained resource. For an I/O-heavy database that's disk queue depth and how fast the disk fills. CPU, memory and disk are the usual indirect signals, but you can also load test, set a static limit and alert as traffic approaches it.

## CatGen: building the dashboard

The demo service, CatGen, has a front end of static assets served by Nginx and a Go back end that serves a random cat JPEG with an artificial delay of 0 to 50 milliseconds, recorded in a Prometheus histogram. Both run as pods on local Kubernetes, and curl generates load.

In Grafana Michael plots traffic as requests per second from Nginx's response metrics, errors as the same rate broken out by status (200s against everything else), and back-end latency from the histogram as a heatmap in milliseconds. For saturation he plots CPU per pod, since CatGen is CPU-bound.

## The bot in the saturation graph

The saturation panel is the most instructive moment. The front end is doing far more work than the back end, because curl fetches the HTML but never downloads the image, so the back end never gets those requests. In real life that pattern might mean scaling the front end, or recognising that a bot is hitting you and throttling or blocking it. With load testing he could add a static high watermark, say 500 requests per second, and alert as traffic gets close.

He closes with a reminder that the golden signals are a starting point, not the whole list: Kubernetes hosts, kubelets and Prometheus itself all expose metrics worth plotting.

## Who should watch

Engineers setting up their first service dashboard, and on-call teams drowning in host-level alerts who want a principled way to cut them. Experienced SREs will know the signals; the error-latency trap and the bot in the CPU graph are the takeaways.

Related Conf42 talks from the same event: Ricardo Castro on [alerting with SLOs and error budget policies](https://www.conf42.com/Site_Reliability_Engineering_2022_Ricardo_Castro_alerting_slos_error_budget_policies), Aliaksandr Valialkin on [Kubernetes monitoring](https://www.conf42.com/Site_Reliability_Engineering_2022_Aliaksandr_Valialkin_kubernetes_monitoring), and Samuel Arogbonlo on [log metrics with Prometheus](https://www.conf42.com/Site_Reliability_Engineering_2022_Samuel_Arogbonlo_logmetrics_prometheus).

[Watch Michael McAllister's talk](https://www.conf42.com/Site_Reliability_Engineering_2022_Michael_McAllister_four_golden_signals_monitoring_health_service) from [Conf42 Site Reliability Engineering 2022](https://www.conf42.com/sre2022).

## From Teleport

Teleport unifies access to SSH servers, Kubernetes clusters, web applications and databases across environments; this talk is a general monitoring session rather than a product demo.

- Teleport: [goteleport.com](https://goteleport.com/)
- [About Teleport](https://goteleport.com/about)
- [Get started with Teleport](https://goteleport.com/pricing)
- [Teleport on YouTube](https://www.youtube.com/channel/UC1O9RGv3FGJau091DD09ooQ)

[Watch the talk on YouTube](https://youtu.be/rZzGr5Zj1KM).

## Watch the talk

[Four Golden Signals: Monitoring the health of your service](https://www.conf42.com/Site_Reliability_Engineering_2022_Michael_McAllister_four_golden_signals_monitoring_health_service) at Conf42 Site Reliability Engineering 2022.
