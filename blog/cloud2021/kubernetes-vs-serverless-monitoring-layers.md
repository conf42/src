# Kubernetes has five layers to watch; serverless leaves you one

Conf42 Blog, 2021-04-29. https://www.conf42.com/blog/cloud2021/kubernetes-vs-serverless-monitoring-layers

In short: Erez Berkner (Lumigo) at Conf42 Cloud Native 2021 comparing Kubernetes and serverless monitoring, from five Kubernetes layers to agentless tracing

Moving from Kubernetes to serverless takes most of the monitoring stack off your plate, and leaves the hardest part. At Conf42 Cloud Native 2021, Erez Berkner, CEO and co-founder of Lumigo, compared the two side by side: five layers to cover on Kubernetes with Prometheus, Grafana and the ELK stack, versus an agentless world on serverless where only your application is yours to watch, and where tracing across managed services is the new gap.

It is a short talk with a product demo at the end. The comparison table in the middle is the part to keep.

## From owning a car to calling an Uber

Berkner's metaphor is transport. You can own a car (buy it, fuel it, maintain it, drive it), rent one (no ownership, still the upkeep), take a train (just figure out the route) or call an Uber (just say where you're going). Cloud has followed the same path: physical servers, virtual machines that took the hardware away, containers where you mostly care about runtime, scale and code, and serverless, where you upload code and the provider covers the rest.

## What do you monitor on Kubernetes?

He lists five layers: the infrastructure and its vital signs, the cluster itself, the pods, the overall readiness and availability of the pods, and the application logs. Miss one and you lose part of the picture across hardware, infrastructure and application.

The tools he recommends are the familiar ones. Prometheus pulls metrics from the nodes, stores and analyses them, and sends alerts via Alertmanager to Slack or PagerDuty. Grafana draws the dashboards (his example shows pod usage, cluster availability and CPU in one view). Logstash and the ELK stack make application logs searchable. He also points to a lesser-known open source tool for visualising traffic between containers.

His tip for anyone with a service mesh: use it for monitoring too. A mesh such as Istio gives you a central point for metrics without adding another layer.

## Why doesn't that approach carry over to serverless?

Berkner's serverless is more than AWS Lambda: Fargate, DynamoDB, API Gateway, Stripe and Twilio all count, because you consume them without running a server. Three properties change the job. It is ephemeral, with nothing always up. There are hundreds of components rather than three tiers. And there are no servers, so there is nowhere to install an agent.

His comparison:

- **Agents:** fine on containers; on serverless, use APIs and code libraries instead.
- **Cost:** containers are billed per resource, serverless per request.
- **Your responsibility:** hardware and OS on Kubernetes; only the application on serverless.
- **Service discovery:** service mesh and existing tools on containers; the cloud provider's APIs on serverless.
- **Distributed tracing:** needed on both, because both are made of many small parts.

And the line that applies to both: you still own the monitoring. "Nobody will do that for you in containers or in serverless," Berkner said at Conf42 Cloud Native 2021.

## What serverless monitoring needs

His requirements: find and fix issues in minutes, which means something has to connect the dots and hand you debugging data on demand; automatic distributed tracing, because nobody can chase every new service by hand; bottleneck detection; and all of it agentless.

## The demo

The Lumigo demo starts from a dashboard covering invocations, failures, cold starts, cost, slow APIs and timeouts, then follows an alert to a Lambda that ran 7,000 times in seven days with almost 50% failures. From one failed invocation it reconstructs the request across services: the customer-facing API (so you can judge whether to fix it now), the stack trace and its parameters, the triggering event, environment variables, the message sent to EventBridge, the DynamoDB query and its empty response, and the Twilio request and response. The request's 62 log lines read in order, from authentication onwards.

## Who should watch

Teams running both Kubernetes and serverless, or moving workloads from one to the other, who want a quick checklist of what changes. Kubernetes monitoring veterans will know the first half; the comparison and the point about tracing through managed services like DynamoDB and EventBridge are the takeaways.

## Related Conf42 talks

- Aviad Mor on [observability across asynchronous managed services](https://www.conf42.com/Cloud_Native_2021_Aviad_Mor_observability_serverless_asynchronous_managed_services) at Conf42 Cloud Native 2021.
- Dotan Horovits on [monitoring microservices the right way](https://www.conf42.com/Cloud_Native_2021_Dotan_Horovits_monitoring_microservices) at Conf42 Cloud Native 2021.
- Yan Cui on [patterns for efficient serverless](https://www.conf42.com/Cloud_Native_2024_Yan_Cui_patterns_efficient_serverless) at Conf42 Cloud Native 2024.

[Watch Erez Berkner's talk](https://www.conf42.com/Cloud_Native_2021_Erez_Berkner_monitoring_kubernetes_serverless_based_applications)

## From Lumigo

Lumigo connects metrics, traces and logs from serverless and cloud native environments, without code changes, to build the end-to-end story of each request.

- [lumigo.io](https://lumigo.io/?utm_source=conf42)

[Watch the talk on YouTube](https://youtu.be/JhWfU82BoIM).

## Watch the talk

[Monitoring Kubernetes VS Serverless-based applications](https://www.conf42.com/Cloud_Native_2021_Erez_Berkner_monitoring_kubernetes_serverless_based_applications) at Conf42 Cloud Native 2021.
