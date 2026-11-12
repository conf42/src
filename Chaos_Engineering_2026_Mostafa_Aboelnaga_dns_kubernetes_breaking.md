# What Happens When DNS Stops Working? Breaking Kubernetes on Purpose.

A talk at [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026) by [Mostafa Aboelnaga](https://www.conf42.com/speaker_Mostafa_Aboelnaga) (Engineering Manager @ SolarWinds). Page: https://www.conf42.com/Chaos_Engineering_2026_Mostafa_Aboelnaga_dns_kubernetes_breaking

## Abstract

Kubernetes makes it easy to deploy distributed applications, but what happens when one of its most fundamental dependencies becomes unreliable?  In this session, we'll deliberately introduce DNS failures into a running Kubernetes environment and explore how seemingly healthy applications start behaving unexpectedly.  Using a live demo with a small microservices application, we'll inject DNS resolution failures, examine their impact on service-to-service communication, and investigate how retry policies, connection pooling, DNS caching, and readiness probes influence application behavior.  We'll then experiment with different recovery strategies and compare their effectiveness under failure.
