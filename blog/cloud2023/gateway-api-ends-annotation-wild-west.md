# Gateway API is how Kubernetes leaves the annotation Wild West

Conf42 Blog, 2023-03-30. https://www.conf42.com/blog/cloud2023/gateway-api-ends-annotation-wild-west

In short: Shane Utt (Kong) at Conf42 Cloud Native 2023 on why Gateway API succeeds Ingress, its role-based resources, conformance levels and the GA roadmap

Ingress got Kubernetes traffic in the door, and then 22-plus implementations bolted their own annotations onto it until no two controllers behaved alike. At Conf42 Cloud Native 2023, Shane Utt, Staff Software Engineer at Kong, a chair of Kubernetes SIG Network and a Gateway API maintainer, explained what replaces it: Gateway API, a set of role-oriented, conformance-tested resources that is where new Kubernetes routing features land, plus a demo with Kuma and a tour of the roadmap as it stood in March 2023.

It is mostly an upstream project talk from someone who helps run the project. Kong appears as one of the implementers, with a Kuma demo in the middle.

## What was wrong with Ingress?

Ingress has been around for five-plus years and does a few things: host and path matching, forwarding to a Service, TLS. The limits he lists:

- Many non-portable extensions across 22-plus implementations, with annotations everywhere.
- An insufficient permission model.
- Mostly HTTP, mostly north-south traffic.
- Heavy reliance on the Kubernetes Service API.

"We call this sort of the annotation Wild west, where no two ingress controllers behave, usually even like remotely, that similar to one another," Shane Utt said at Conf42 Cloud Native 2023. Kong, he admits, was part of it, with CRDs and annotations that only worked in Kong.

The goals for the replacement were extensibility, multi-protocol support (gRPC, TCP and more) and conformance.

## What does Gateway API look like?

Gateway API is the successor to Ingress: new features go there, not into Ingress. It splits the job by role. A GatewayClass names the controller responsible (similar to IngressClass). A Gateway, often owned by the cluster operator, defines listeners and is an actual proxy instance; you can have several. Routes such as HTTPRoute, often owned by application teams, attach to one or more Gateways through parentRefs and send traffic to backendRefs, which default to Services but can point at anything an implementation supports. Attaching a route to two Gateways at once even gives you a way to migrate between implementations.

What you get over Ingress: header, method and query parameter matching, cross-namespace route binding and forwarding, header modification, request mirroring, redirects, URL rewrites and weight-based traffic splitting.

## How do you standardise without freezing features?

With three conformance levels. Core features every implementation must support consistently (HTTP prefix path matching). Extended features are optional, but when supported they must follow the spec (header modification). Custom features may vary by implementation (regex path matching). Features can graduate upwards as adoption grows, which brings vendor extensions back upstream instead of into annotations.

## What did the demo show?

Kong maintains three implementations: the Kong Kubernetes Ingress Controller (KIC), the Kong Gateway Operator (KGO), and Kuma with Kong Mesh. The demo uses Kuma on a kind cluster with the Kuma counter demo, a web app plus Redis, both with Envoy sidecars in the mesh. Kuma ships a GatewayClass; he applies a basic HTTP Gateway, waits for an IP, then applies an HTTPRoute with a path prefix to the demo app on port 5000. The browser shows the counter app reached from outside the cluster, with the app still talking to Redis inside the mesh. All upstream Kubernetes resources, no annotations.

## Beyond HTTP, and what was next

At the time GRPCRoute, TLSRoute, UDPRoute and TCPRoute were alpha, while ReferenceGrant, which lets a Gateway in one namespace use a Secret in another, was beta and drawing interest from other SIGs. The roadmap he walked through:

- **GA** with GatewayClass, Gateway and HTTPRoute at v1, tracked via a Road to GA project.
- **GAMMA**, Gateway API for Mesh Management and Administration, with Consul, Istio, Kuma, Kong Mesh and Linkerd contributors working on HTTPRoute for east-west traffic.
- **Conformance profiles**: implementations subscribe to profiles such as HTTP or gRPC, run the test suite and send back a conformance report, so the project can see what is actually implemented.
- Experimental layer 4 support, policy attachment, multi-cluster services and path rewrites; provisional timeouts and egress.

The long-term North Star is replacing LoadBalancer-type Services, since the Service API has become overloaded and upstream wants to keep its scope clean.

## Who should watch

Anyone still running Ingress with a page of annotations, platform teams choosing an ingress or mesh layer, and people who want to contribute to SIG Network. Useful pointers include the ingress2gateway converter (Go, CLI or library) and Blixt, a layer 4 load balancer with a Go control plane and a Rust and eBPF data plane, meant for testing and CI rather than production. Pair it with [Yuri Bacciarini on moving from Ingress to Gateway API](https://www.conf42.com/DevOps_2024_Yuri_Bacciarini_kubernetes_ingress_gateway_api), [Gregorio Palama on the Kubernetes Gateway API](https://www.conf42.com/DevOps_2024_Gregorio_Palama_k8s_gateway_api) and [Rosemary Wang's introduction to service mesh](https://www.conf42.com/Cloud_Native_2022_Rosemary_Wang_introduction_service_mesh).

[Watch Shane Utt's talk](https://www.conf42.com/Cloud_Native_2023_Shane_Utt_beyondkubernetes_ingress_gateway_api)

## From Kong

- [Kong](https://konghq.com/): API gateway, Kubernetes ingress controller and Kong Mesh, the products behind the three Gateway API implementations in this talk.
- [Kong Kubernetes Ingress Controller and Gateway API](https://docs.konghq.com/kubernetes-ingress-controller/latest/concepts/gateway-api/)
- [Kuma and Gateway API](https://kuma.io/docs/latest/explore/gateway-api/)

[Watch the talk on YouTube](https://youtu.be/c-w-WbRrQ9s).

## Watch the talk

[Beyond Kubernetes Ingress (with Gateway API)](https://www.conf42.com/Cloud_Native_2023_Shane_Utt_beyondkubernetes_ingress_gateway_api) at Conf42 Cloud Native 2023.
