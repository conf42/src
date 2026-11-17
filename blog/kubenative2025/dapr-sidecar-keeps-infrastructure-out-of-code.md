# Dapr moves the plumbing out of your microservices and into a sidecar

Conf42 Blog, 2025-09-23, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/dapr-sidecar-keeps-infrastructure-out-of-code

In short: Christophe Gigax (Hager Group) at Conf42 Kube Native 2025 shows how Dapr's sidecar and building blocks keep state stores and brokers out of app code.

Your service should not know whether its orders land in Redis or Cosmos DB. That is the pitch Christophe Gigax, Cloud Solution Architect at Hager Group and a Microsoft MVP, made at Conf42 Kube Native 2025: put Dapr, the Distributed Application Runtime, next to every service as a sidecar, talk to it over plain HTTP or gRPC, and let YAML decide what sits behind it.

It is an introduction, and an honest one. If you have heard "Dapr" in a CNCF slide and never run it, this is a good first half hour.

## The pain is the glue code, not the services

Christophe starts where most microservice migrations hurt. Small, focused services buy team autonomy and independent deploys, but debugging a bug that spans five of them means running all five locally, and the interdependencies pile up until nobody can follow the flows. On top of that, most languages and frameworks were never designed with distributed systems in mind, and apps end up tied to one hosting platform.

Dapr's answer is to standardise the outside world. Service-to-service invocation, state management, pub/sub, resource bindings and triggers, actors, distributed tracing and secrets all become building blocks behind the same API, from any language. He counted more than a hundred pluggable components available off the shelf, and you can write your own.

## Your code only ever talks to localhost

The core idea is the sidecar pattern. Launch a service and a Dapr sidecar starts next to it; every external interaction goes through that sidecar. Saving state is a call to the state API with a store name. Calling another service is a call that names the target app ID and method, and Dapr does the service discovery.

The demo uses the official Dapr quickstarts repository. A Node.js app exposes endpoints to create and fetch orders, but its code never mentions a database: it posts to the Dapr port, 3500, with the name of a configured state store. `dapr init` had already pulled a Redis container locally, so `dapr run` with an app ID wires everything up and the logs show the Redis state store and pub/sub components loading. A small Python client then loops forever creating orders, calling the Node app through its own sidecar rather than directly. Neither app knows the other's address, and neither knows Redis exists.

That is the part worth watching: two short programs with zero infrastructure imports, still talking to each other and to a database.

## Swapping the broker is a YAML change

Every component (state store, pub/sub broker, binding, secret store) gets its own YAML file holding the connection details. Want Cosmos DB instead of Redis, or Azure Service Bus instead of RabbitMQ? Change the component file; the service code stays put. Pub/sub works the same way: a service publishes to Dapr, Dapr forwards to whichever broker is configured, and subscribers expose an endpoint Dapr calls with each new message.

Telemetry follows the same logic. Dapr speaks OpenTelemetry, so the backend you send traces to can change without touching the app.

## On Kubernetes, the injector does the work

For production Christophe recommends Kubernetes. Installing Dapr there adds four system pods, including the sidecar injector, the actor placement service and Sentry for security, plus the operator. The injector adds a sidecar to every pod you annotate, and from then on the app code is identical to what ran on your laptop. He also noted that Dapr became a graduated CNCF project in November 2024, which matters if your architecture review board asks about maturity before anything else.

## Who should watch

Developers and architects weighing how much distributed-systems plumbing to write themselves, and teams that keep rewriting the same Redis or Kafka client wrapper in three languages. If you already run Dapr in production, you will know most of this; the value here is a clear mental model you can hand to a new team.

## Related Conf42 talks

- [Enhancing Workflow Reliability with Dapr: Techniques to Minimize Failure Costs](https://www.conf42.com/Cloud_Native_2025_Siri_Varma_Vegiraju_workflow_dapr_failure) by Siri Varma Vegiraju (Microsoft), the next step once the basics click.
- [Ambient Mesh: The new sidecar less & faster Istio for zero trust](https://www.conf42.com/Kube_Native_2023_Md_Azmal_ambient_mesh_sidecar_zero_trust) by Md Azmal (IMESH), for the case against sidecars.
- [Debugging a container with a sidecar in Kubernetes using Gefyra](https://www.conf42.com/Cloud_Native_2022_Michael_Schilonka_debugging_container_sidecar_kubernetes_gefyra) by Michael Schilonka (Unikube), on the local-debugging pain Christophe opens with.

[Watch Christophe Gigax's talk](https://www.conf42.com/Kube_Native_2025_Christophe_Gigax_dapr_architectures_cloudnative)

[Watch the talk on YouTube](https://youtu.be/avKQI0V9rGg).

## Watch the talk

[Shaping next generations of architectures with Dapr](https://www.conf42.com/Kube_Native_2025_Christophe_Gigax_dapr_architectures_cloudnative) at Conf42 Kube Native 2025.
