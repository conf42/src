# Why HTTP/2 sent all our Kubernetes traffic to one pod

Conf42 Blog, 2026-03-04, updated 2026-11-09. https://www.conf42.com/blog/sre2026/http2-sends-all-traffic-to-one-kubernetes-pod

In short: Mariem Sboui (gridX) at Conf42 SRE 2026 on an incident where kube-proxy's connection-level balancing pinned HTTP/2 traffic to a single pod.

One pod at full CPU, its siblings idle, plenty of cluster capacity, and the autoscaler perfectly happy: that was the picture after Mariem Sboui's team switched some critical services to HTTP/2. At Conf42 Site Reliability Engineering (SRE) 2026, Mariem, Senior Site Reliability Engineer at gridX, walked through the incident and its cause: Kubernetes Services balance TCP connections, not requests, and HTTP/2 puts many requests on one long-lived connection.

It is a short, focused incident review, and the kind of talk that saves someone a very confusing afternoon.

## The symptoms didn't add up

External users saw extra latency, which Mariem put at more than 300 milliseconds. Not catastrophic, but real. Looking at the backends, one pod was serving essentially all incoming traffic while the others sat idle.

What made it confusing was everything that looked fine. Nodes and pods had idle capacity. The Horizontal Pod Autoscaler was working normally. And killing the hot pod didn't help: the traffic simply landed on another single pod, with no redistribution. Mariem is candid about the team's mistake. They assumed HTTP/2 would behave like HTTP/1.1 inside Kubernetes, without knowing what happens one layer down.

## Layer 4 balancing meets multiplexing

By default a Kubernetes Service does Layer 4 load balancing. When a new TCP connection arrives, kube-proxy picks a backend pod and every request on that connection goes to that pod. Nothing looks at individual requests.

That works for HTTP/1.x because clients typically open many short-lived connections, and each new connection can land on a different pod. HTTP/2 changes the deal: a client multiplexes many requests over a single connection, and those connections tend to stay open for a long time. So kube-proxy makes one choice and the whole stream follows it. One pod gets everything, its CPU spikes and throttles, and latency climbs for users.

## A quick patch, then a six-month fix

The short-term changes were all at the application level: tuning keep-alive settings, reducing connection reuse in the HTTP/2 clients, and increasing the number of active connections. That spread traffic out enough to stop the bleeding, and Mariem is clear that it was only a stopgap.

The permanent fix is Layer 7 routing: a service mesh, an HTTP-aware proxy, or an API gateway or ingress that routes per request. Her team chose a service mesh, specifically Istio, and the rollout took about six months. The proxy inspects each HTTP request and decides per request, taking into account paths, headers, routing rules, backend latency and health. Distribution afterwards isn't perfectly equal, but it is far better than the default.

That six-month number is worth remembering. The incident fix took days; the architectural fix took two quarters.

## The takeaways

- Don't rely on default kube-proxy load balancing for HTTP/2-based traffic. That includes gRPC and anything else that keeps connections open.
- Put Layer 7 load balancing in front of those services.
- Run enough backend pods that capacity can actually absorb the distribution.

## Who should watch

Anyone about to enable HTTP/2 or gRPC inside a Kubernetes cluster, and anyone staring at one hot pod with an autoscaler that sees no problem. Platform teams debating whether a mesh is worth the cost will find a concrete reason here. It's short, practical, and has a real incident at its centre.

## Related Conf42 talks

- [A Developer's Introduction to Service Mesh](https://www.conf42.com/Cloud_Native_2022_Rosemary_Wang_introduction_service_mesh) by Rosemary Wang (HashiCorp), if Layer 7 routing is new territory.
- [Developing custom Load Balancer using Envoy](https://www.conf42.com/Golang_2024_Sandeep_Bhat_custom_load_balancer_envoy) by Sandeep Bhat (Harness), for the proxy-level view.
- [gRPC in Python. Build fast scalable APIs for your services](https://www.conf42.com/Python_2023_Aditya_Mattos_grpc_fast_scalable_apis) by Aditya Mattos (Kandji), the protocol most likely to trigger this.

[Watch Mariem Sboui's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Mariem_Sboui_kubernetes_default_load)

[Watch the talk on YouTube](https://youtu.be/bxwisgR2XHQ).

## Watch the talk

[Why Kubernetes Default Load Balancing Doesn’t Work for HTTP/2 Traffic](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Mariem_Sboui_kubernetes_default_load) at Conf42 Site Reliability Engineering (SRE) 2026.
