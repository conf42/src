# Your APM ships raw spans home to compute a latency number

Conf42 Blog, 2022-10-20. https://www.conf42.com/blog/kubenative2022/apm-should-decide-at-the-edge

In short: Shahar Azulay (groundcover) at Conf42 Kube Native 2022 on why centralised APM can't scale with microservices and how eBPF moves decisions to the edge.

Most APM bills are the cost of shipping raw spans to a vendor so the vendor can tell you your p95. At Conf42 Kube Native 2022, Shahar Azulay, co-founder and CEO of groundcover, argues that this centralised design, set a decade ago, is why APM doesn't scale with microservices, and that eBPF lets the agent make the expensive decisions next to the data instead.

It's a sponsor talk, and the last few minutes map the argument onto groundcover's product. The first twenty are a crisp architecture history that explains a pain most teams feel at invoice time.

## Why is APM the least adopted pillar?

Shahar starts with three layers of observability: logs, infrastructure monitoring and application performance monitoring. APM is the one closest to the business, covering trace capture for troubleshooting and the golden signals (throughput, error rate, latency) that SLOs are built on.

Yet by the figures he quotes, almost 70% of teams use some kind of log management and almost 60% monitor their infrastructure, while "application monitoring, or APM, is clearly under adopted with only 22% of the population actually using an APM solution of some kind," Shahar Azulay said at Conf42 Kube Native 2022.

He admits there are many reasons. He picks one: APM stores huge amounts of irrelevant data to produce a little insight, and the cost grows faster than the business.

## How did we end up storing everything?

The history is the best part of the talk. Infrastructure could be watched from an external agent, but APM vendors needed to see inside the application, so they handed developers an SDK to instrument their code. Wrap each API handler, time the start and end of the request, report.

That choice dictated everything else. Code that runs inside your web server has to be tiny, fast and incapable of crashing it; nobody accepts a monitoring library that halves their throughput. So the SDK stays dumb: sample raw data, send it home. All the clever work (picking traces, building span-based metrics, computing golden signals) happens on the vendor's backend.

Shahar calls the result a debt towards scale, and splits it in two:

- **You store raw data to get digested insights.** At a million requests per second on a cluster, you pay to store spans when what you wanted first was the latency per service.
- **Data is collected at equal depth.** If you want the payload of the one failing request in 10,000, a simple SDK makes you store payloads for every request or for none.

## The visibility-depth versus cost trade-off

That second point is what he names the visibility-depth versus cost trade-off: going deeper on the cases you care about means paying to store more of everything. Every team already lives with its workarounds, keeping warning logs and up, dropping a metric because cardinality hurts, cutting trace sampling to 1%.

Random sampling is the giveaway. Nobody wants one trace in a hundred. You want the traces that took ten times longer than the rest, and the 10 seconds of info logs around a 500.

## What changes when the agent runs in the kernel?

Shahar's answer is edge observability: move the decision-making from the vendor's backend to the agent running next to the data. The enabler is eBPF, which runs logic inside the Linux kernel and can capture what an instrumented SDK would, golden signals included, from outside the application.

Because the agent runs out of band, it adds no overhead to the application, and it can afford to be clever. He gives two examples:

- **In-host span-based metrics.** Compute latency and error rates inside the eBPF agent as requests flow, without storing spans or sending them off the node.
- **Variant-depth capturing.** A 500 triggers capture of the full payload plus logs around the request. A latency outlier at the p95 triggers capture of the other requests hitting the server at the time and high-resolution CPU usage. The healthy flow gets sampled at 1%, enough to show what normal looks like.

That last pattern is the reusable idea, whatever tool you run: decide depth per scenario, not per system.

## Who should watch

Anyone who has trimmed their tracing to save money and lost the trace they needed. The talk is architecture, not a demo: there are no benchmarks or customer numbers, and the eBPF section stays at the level of what it enables. For the mechanics, pair it with [Nikolay Sivko on zero-instrumentation observability with eBPF](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Nikolay_Sivko_zeroinstrumentation_observability_ebpf) at Conf42 SRE 2024, [Alejandro Mercado on Kubernetes observability with eBPF](https://www.conf42.com/Kube_Native_2025_Alejandro_Mercado_observability_kubernetes_ebpf) at Conf42 Kube Native 2025, and Shahar's own follow-up, [Kubernetes observability with eBPF](https://www.conf42.com/Cloud_Native_2023_Shahar_Azulay_kubernetes_observability_ebpf) at Conf42 Cloud Native 2023.

[Watch Shahar Azulay's talk](https://www.conf42.com/Kube_Native_2022_Shahar_Azulay_cloudnative_observability_distributed_architectures) from [Conf42 Kube Native 2022](https://www.conf42.com/kubenative2022).

## From groundcover

In the talk, Shahar describes groundcover as a Kubernetes application monitoring product built on the two ideas above: eBPF instrumentation instead of an in-code SDK, so there's no R&D work to integrate it, and edge-based algorithms that build metrics and sample data on the node.

- groundcover: [groundcover.com](https://www.groundcover.com/)
- groundcover community Slack: [groundcover.com/join-slack](https://www.groundcover.com/join-slack)

[Watch the talk on YouTube](https://youtu.be/YofLXDGn2KI).

## Watch the talk

[Cloud-Native Observability at Scale: Why Distributed Architectures are Here to Stay](https://www.conf42.com/Kube_Native_2022_Shahar_Azulay_cloudnative_observability_distributed_architectures) at Conf42 Kube Native 2022.
