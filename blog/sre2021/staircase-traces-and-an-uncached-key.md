# Logs could not find it, a Jaeger trace found an uncached key

Conf42 Blog, 2021-09-30. https://www.conf42.com/blog/sre2021/staircase-traces-and-an-uncached-key

In short: Dotan Horovits (Logz.io) at Conf42 Site Reliability Engineering 2021 on how distributed tracing found two latency bugs that logs had hidden for years

An observability company that could not explain its own slow UI is a story with built-in irony, and Dotan Horovits, Product Evangelist at [Logz.io](https://logz.io), tells it on himself. At Conf42 Site Reliability Engineering 2021 he walks through how Logz.io, then fully instrumented for logs and metrics, chased a creeping UI slowdown, failed twice with logs, and finally found the cause in a Jaeger timeline. The takeaway: in a multi-cloud, multi-region microservices system, logs tell you what happened inside each service, and only traces tell you what happened between them.

## Why weren't logs enough?

The setup was the hard kind: microservices on AWS and Azure, multi-region, multi-tenant, thousands of requests per minute and plenty of internal service-to-service traffic. The metrics said requests were getting slower in different flows across the app, with no single service to blame.

The first attempt was the usual one, searching the logs. Request sequences were long and the data looked identical. The second attempt was a homemade trace: add a request ID to every log line and group by it in Kibana. That meant touching every suspected service to accept the ID, log it and pass it downstream, and the result was a bucket of log lines with no parent-child relationships. Nobody was going to convince the other teams to hand-propagate IDs through their code either.

Third attempt, proper distributed tracing. Horovits gives a compact primer on spans (a structured log with a trace ID, start time, duration and parent), context propagation through tracer SDKs, and the Gantt-style timeline view the backend rebuilds from the spans.

## What did the first traces show?

The team picked Jaeger over Zipkin (both ran for a while), instrumented only two Node.js front-end services first, and used the OpenTracing API so the backend could be swapped later. He is upfront that OpenTracing has since merged with OpenCensus into OpenTelemetry, which is where anyone starting today should go.

The first trace view exposed a staircase: calls running one after another that had no reason to be sequential. Making them concurrent was easy and gave a big performance win, but it was not the root cause.

Filtering by minimum duration turned up the real one. A request that fetched user data took anywhere from 100 milliseconds to almost 10 seconds, and the browser had to wait for it before rendering. It fanned out through several microservices, some not yet instrumented, down to Java code and the database. Dotan Horovits said at Conf42 Site Reliability Engineering 2021: "And what we found was one key that is read for some user requests which was mistakenly not cached." That is why the slowness looked random: only the calls needing that key went to the database.

The side effect sold tracing to the rest of the company. Jaeger draws a live service dependency diagram from the calls it sees. Dotan Horovits said at Conf42 Site Reliability Engineering 2021: "We don't need to maintain a sequence diagram anymore and update it every couple of weeks."

## How should you start instrumenting?

His tips, in order:

- **Don't instrument everything on day one.** Start with the critical services, often the front-end request endpoints, and work back along the call path.
- **Use OpenTelemetry.** One API and SDK per language for traces, metrics and logs, the OTLP protocol, and a collector that ships to whichever backend you like: Jaeger, Prometheus or a SaaS.
- **Lean on auto-instrumentation.** Agents for Node.js frameworks like hapi and Express, Java with Spring and Log4j, Ruby and more cut the code you write by a lot.

## Which trace patterns should you look for?

The last part is a field guide to timeline shapes, worth bookmarking:

- **Staircase**: serial calls that could run in parallel, or be replaced by a bulk query or a join. Sometimes it is just a thread pool setting.
- **Span spike**: long spans that vary between runs, often slow queries or caching problems. Optimise the longest span on the critical path first.
- **Gaps between spans**: slow inter-service communication, or a component with no instrumentation, such as an uninstrumented database driver. He points to SQLCommenter, which Google had just contributed to OpenTelemetry, for tying queries back to application code.
- **Spans finishing at the same time**: timeouts, connectivity trouble or a shared lock releasing everyone at once. Add instrumentation around the shared resource.

Add filters by duration and by span tags, and put the trace ID in your log lines so traces and logs join up without the propagation pain the team had with request IDs.

## Who should watch

Anyone running microservices who still debugs latency by grepping logs, and teams that have traces but only look at them during outages. It is a practical talk: a real incident, then a checklist.

## Related Conf42 talks

- Dotan Horovits on [monitoring microservices](https://www.conf42.com/Cloud_Native_2021_Dotan_Horovits_monitoring_microservices) at Conf42 Cloud Native 2021.
- Nicolas Frankel on [OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing) at Conf42 DevOps 2023.
- Dave McAllister on [Murphy's laws of observability](https://www.conf42.com/Site_Reliability_Engineering_2021_Dave_McAllister_murphys_law_observability), also at SRE 2021.

[Watch Dotan Horovits's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Dotan_Horovits_performance_issues_Microservices_Arch_Distributed_T)

## From Logz.io

Logz.io runs an observability platform for logs, metrics and traces, built on open source tools, and takes in OpenTelemetry data from the collector.

- [Logz.io website](https://logz.io)

[Watch the talk on YouTube](https://youtu.be/04uoYLtFI78).

## Watch the talk

[Investigating Performance Issues In Microservices Arch. With Distributed Tracing](https://www.conf42.com/Site_Reliability_Engineering_2021_Dotan_Horovits_performance_issues_Microservices_Arch_Distributed_T) at Conf42 Site Reliability Engineering 2021.
