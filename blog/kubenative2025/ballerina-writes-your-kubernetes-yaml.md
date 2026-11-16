# Ballerina writes your Kubernetes YAML so you don't have to

Conf42 Blog, 2025-10-09, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/ballerina-writes-your-kubernetes-yaml

In short: Anupama Pathirage of WSO2 shows at Conf42 Kube Native 2025 how Ballerina turns integration code into Docker and Kubernetes artifacts with one build.

Integration code has an awkward habit: the business logic takes an afternoon, and the Dockerfile, the Deployment, the Service and the resource limits take the rest of the week. At Conf42 Kube Native 2025, Anupama Pathirage, Director and Head of Engineering for Integration at WSO2, showed how Ballerina, the open-source language WSO2 started in 2016, closes that gap by building the container and Kubernetes artifacts straight from the source code.

It is a product-focused talk from the team that builds the language, and it says so. What makes it worth the time is the live demo: a small REST service goes from VS Code to a running Kubernetes deployment without anyone typing a line of YAML.

## Integration is a data, network and concurrency problem

Pathirage frames integration as three jobs: moving data around in many shapes, talking over many protocols, and doing all of it concurrently. Ballerina gives each one a first-class abstraction. Services and clients are part of the language syntax rather than a framework bolted on top. A resource function looks like an ordinary function whose name maps to the resource path, with typed input parameters and return types, so the network plumbing stays out of the business logic.

Data lives in records, Ballerina's canonical representation for whatever arrives over the wire, whether that is JSON or something else. If you've written a C-family language (C, C++, Java, Go), she argues the syntax will feel familiar; the new parts are those integration constructs.

## Every program is also a diagram

The feature that gets the most screen time is code-and-diagram parity. Every Ballerina program has an equivalent flow or sequence diagram, kept in sync automatically by the VS Code plugin. In the demo she adds an `if` node in the diagram and the matching code appears in the source file; edit either side and the other follows. The same idea extends to a service designer for HTTP and GraphQL, a visual data mapper with an AI-assisted auto-map for records with many fields, debugging from diagram nodes, and an ER-style view of your types.

There is also tooling for contract-first work: point the OpenAPI tool at a spec and it generates the service and client code in one command, with similar tools for other formats.

## Code to cloud, minus the YAML

The demo app checks the weather for a location, maps the weather to a mood and asks Spotify for a matching playlist. Two APIs, one service, three resources. She runs it locally with `bal run`, tries a couple of cities, then moves on to the part the talk is named for.

A `bal build` with the cloud option set to Docker produces the image and a Dockerfile in the target folder. Set it to Kubernetes and the compiler emits the deployment YAML too, reading the port and other settings from the source and filling in default CPU and memory values that you override with a config file. Then it is plain `kubectl`: apply, check the deployment, expose the service. She mentions the same approach for serverless targets such as AWS Lambda and Azure Functions, and OpenTelemetry-based observability on the operations side.

## Who should watch

Integration developers who live between APIs and SaaS connectors, and platform teams who are tired of reviewing hand-written manifests for small services. If you need a Kubernetes primer, this is not it; if you want to see how far a language can absorb deployment concerns, it is a tidy half hour.

## Related talks

- Pathirage covered the deployment side in more depth a year earlier in [From Code to Cloud: Mastering Kubernetes Deployments with Ballerina](https://www.conf42.com/Kube_Native_2024_Anupama_Pathirage_kubernetes_ballerina_deployments).
- Anuruddha Liyanarachchi looks at the network side in [Simplify Network Services for Real-World, Cloud Native Applications with Ballerina](https://www.conf42.com/Kube_Native_2023_Anuruddha_Liyanarachchi_network_services_realworld_ballerina).
- For the gateway in front of all those services, Roman Rastiehaiev compares open-source options in [Navigating the World of API Gateways](https://www.conf42.com/Cloud_Native_2025_Roman_Rastiehaiev_api_gateways_comparison).

[Watch Anupama Pathirage's talk](https://www.conf42.com/Kube_Native_2025_Anupama_Pathirage_ballerina_integration_opensource)

[Watch the talk on YouTube](https://youtu.be/5WOoGTRU4IQ).

## Watch the talk

[Ballerina Unleashed: Open Source Mastery in Cloud-Native Integration](https://www.conf42.com/Kube_Native_2025_Anupama_Pathirage_ballerina_integration_opensource) at Conf42 Kube Native 2025.
