# Why Kubernetes API gateways need a service mesh behind them

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/api-gateway-plus-service-mesh-kubernetes

In short: Niharika Jha (Microsoft) at Conf42 Kube Native 2025 on pairing Kubernetes-native API gateways with Istio or Linkerd for traffic control, mTLS and observability.

A traditional API gateway in front of a few hundred microservices tends to become the one box everybody is afraid to restart. At Conf42 Kube Native 2025, Niharika Jha, Senior Software Engineer at Microsoft, gave a compact tour of the alternative: Kubernetes-native API gateways layered with a service mesh, so north-south and east-west traffic share policies, security and telemetry.

The talk runs about 15 minutes and works as a structured overview rather than a deep implementation session. It is a good map of the moving parts for teams that are hitting service sprawl and have not yet picked a mesh.

## The gateway was never built for this many services

Jha's problem statement is service sprawl: the number of services outpaces what a traditional gateway can manage. The symptoms are slow releases blocked on integration, gateways that become single points of failure, manual service discovery and static config that does not survive multi-cloud, and configuration drift between dev, staging and production. All of it adds operational load and slows teams down.

Her answer is a layered architecture. A Kubernetes-native gateway handles the edge, a service mesh handles service-to-service traffic, and together they give end-to-end traffic control, one place to enforce policy and a single view of what is happening, across Azure, AWS or Google Cloud.

## Istio if you need everything, Linkerd if you need less

On the mesh itself she covered Istio's split between a control plane that manages policy and discovery centrally and Envoy sidecars that do routing and load balancing per pod, with mutual TLS for zero-trust traffic between services. For teams that want a lighter footprint, Linkerd offers mTLS, routing and observability with less resource overhead.

The traffic patterns that make a mesh worth its sidecars are the ones she highlighted: automated canary deployments that shift traffic gradually and roll back when health checks fail, circuit breakers that stop one failing service from cascading, and load balancing driven by real-time metrics.

## Security and observability as defaults

Security gets two layers. Kubernetes RBAC with automated service accounts and least privilege controls who can do what in the cluster, while OAuth 2.0 and JWTs handle stateless authentication at the API level, wired to external identity providers. Observability is the standard trio of Prometheus for metrics, Grafana for dashboards and Jaeger or Zipkin for traces.

Helm charts standardise deployments as configuration-as-code across environments. Adaptive rate limiting throttles traffic based on downstream health, and it works together with HPA and VPA for scaling. Operators and custom resource definitions give developers self-service with GitOps principles.

## APIs as products

The less common angle is monetisation. Jha treated APIs as business products: usage-based pricing, analytics on consumption, namespace isolation for multi-tenant customers, and self-service developer portals for discovery. If your platform team is asked to justify its budget, that section gives you the vocabulary.

Her rollout framework has four steps: assess the current architecture, deploy Istio or Linkerd with the right security settings, integrate the gateway so traffic management and observability line up, then tune for production performance and scale.

## Who should watch

Engineers and architects who own an ingress or gateway layer and are weighing whether to add a mesh, plus platform leads who need a one-slide-per-concept overview to share with their team. If you already run Istio in production, it will be familiar ground.

## Related Conf42 talks

- [K8s Gateway API 101](https://www.conf42.com/DevOps_2024_Gregorio_Palama_k8s_gateway_api) by Gregorio Palama (Lutech) explains the Gateway API that replaces Ingress.
- [Navigating the World of API Gateways](https://www.conf42.com/Cloud_Native_2025_Roman_Rastiehaiev_api_gateways_comparison) by Roman Rastiehaiev (HiBob) compares Kong, Traefik, Envoy and friends.
- [Service Mess to Service Mesh](https://www.conf42.com/Kube_Native_2023_Rob_Richardson_service_mess_service_mesh) by Rob Richardson covers when a mesh is worth adopting at all.

[Watch Niharika Jha's talk](https://www.conf42.com/Kube_Native_2025_Niharika_Jha_gateway_servicemesh_scalable)

[Watch the talk on YouTube](https://youtu.be/2WAkavT1rr4).

## Watch the talk

[Kubernetes API Gateway: Cloud-Native Service Mesh Strategies for Scalable Solutions](https://www.conf42.com/Kube_Native_2025_Niharika_Jha_gateway_servicemesh_scalable) at Conf42 Kube Native 2025.
