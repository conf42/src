# Six places to put a cache in Kubernetes, and how to pick one

Conf42 Blog, 2021-04-29. https://www.conf42.com/blog/cloud2021/caching-patterns-kubernetes-decision-tree

In short: Rafal Leszko (Hazelcast) at Conf42 Cloud Native 2021 on embedded, client-server, cloud, sidecar and reverse proxy caching, with a decision tree

Every microservice diagram has the same unanswered question hiding in it: where does the cache go? At Conf42 Cloud Native 2021, Rafal Leszko, Cloud-Native Team Lead at Hazelcast (previously at Google and CERN), walked through every caching topology you can run on Kubernetes, from a library inside your app to a proxy your app never knows exists, and finished with a decision tree for choosing between them.

He opens with a challenge: you already use one of these patterns, because the list is complete. The question is whether you should switch.

## Embedded: simple, until the load balancer gets involved

The simplest cache lives inside the application as a library. Check the cache, return on a hit, run the business logic and store the result on a miss. It is so simple you could write it yourself with a ConcurrentHashMap, and his advice is blunt: never do that. A plain concurrent collection has no eviction policy, no size limit, no statistics, no expiry and no notifications. Use Guava or Ehcache in Java, or the equivalent in your language.

Spring users get caching with one annotation, with a catch: Spring defaults to a ConcurrentHashMap, so change the cache manager.

The real problem appears with two pods. A request computed and cached in pod A gets load balanced to pod B next time, and pod B does the expensive work again because the two caches know nothing of each other. The fix is an embedded distributed cache, such as Hazelcast embedded in each instance, so all instances form one cluster. On Kubernetes, Hazelcast auto-detects the environment and uses the Kubernetes API to discover its peers.

Embedded caching is easy to deploy and fast, but it scales only with your application, and it ties you to your app's language (Hazelcast embedded means the JVM).

## Client-server and cloud: a separate thing someone has to run

Client-server is database style: the cache server runs separately (as a StatefulSet on Kubernetes) and applications connect through a client. That buys separate scaling and backups and lets services in any language share it, because the protocol is well defined. Redis and Memcached support only this topology. With Hazelcast it starts with a Helm chart or operator, plus a client configured to use Kubernetes discovery.

Cloud is the same pattern with someone else running the server: start a cluster in a console, paste the discovery token into your app.

The catch for both is latency. Caching is a low-latency game, and Leszko warned that even one router hop is a lot. On premises, keep cache and app on the same local network. In the cloud, pick the same provider and region, then set up VPC peering so there is no hop at all.

## Sidecar: embedded and client-server at once

A cache container in every pod, all of them forming one cluster. The application talks to localhost, so there is no discovery to configure, latency is low, and the cache can be written in a different language from the app. The trade-offs: it still scales with the application, and the data lives in the application's pod, isolated only at container level.

## Reverse proxy: the app doesn't know, and that's the catch

The last family puts the cache in front of the application. NGINX is the mature choice, configured at the HTTP level, but it is not distributed, not highly available, and can offload data to disk. The newer variant is a reverse proxy sidecar: an init container rewrites iptables so traffic hits a caching proxy before the application. Envoy had just added HTTP caching, which he expected to make this pattern big with Istio and other service meshes.

The appeal is declarative caching: point at service one, version one, add a cache, change no code. The cost is cache invalidation. When the app knows about the cache, business logic can evict stale values. When it doesn't, you are left with what HTTP offers, mostly timeouts.

"There is no such thing as a free lunch," Leszko said at Conf42 Cloud Native 2021, on why caching your apps don't know about makes invalidation harder.

## The decision tree

His summary, which he admits is oversimplified:

- App doesn't need to know about caching: reverse proxy with NGINX, or a reverse proxy sidecar with Envoy if you're an early adopter.
- App knows, modest data, no security restrictions: embedded or embedded distributed, or sidecar if you need language independence.
- Lots of data or security restrictions: client-server on premises, cloud if your deployment already is.

## Who should watch

Backend and platform engineers adding a cache to a microservice system, or wondering whether the one they have is in the right place. It is a Hazelcast talk with Hazelcast examples, but the patterns and trade-offs apply to any cache.

## Related Conf42 talks

- Sylvain Combraque on [HTTP caching](https://www.conf42.com/Cloud_Native_2023_Sylvain_Combraque_http_caching_world) at Conf42 Cloud Native 2023.
- Wisdom Matthew on [distributed caching and queueing](https://www.conf42.com/Cloud_Native_2025_Wisdom_Matthew_distributed_caching_queueing) at Conf42 Cloud Native 2025.
- Shailin Saraiya on [caching for millions at low latency](https://www.conf42.com/Platform_Engineering_2025_Shailin_Saraiya_cache_millions_latency) at Conf42 Platform Engineering 2025.

[Watch Rafal Leszko's talk](https://www.conf42.com/Cloud_Native_2021_Rafal_Leszko_architectural_caching_patterns_kubernetes)

## From Hazelcast

Hazelcast makes distributed software: at the time of the talk, the Hazelcast in-memory data grid, Hazelcast Jet and Hazelcast Cloud.

- [hazelcast.com](https://hazelcast.com)

[Watch the talk on YouTube](https://youtu.be/3FE1wMMfw2w).

## Watch the talk

[Architectural Caching Patterns for Kubernetes](https://www.conf42.com/Cloud_Native_2021_Rafal_Leszko_architectural_caching_patterns_kubernetes) at Conf42 Cloud Native 2021.
