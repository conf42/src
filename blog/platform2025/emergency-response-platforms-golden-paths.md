# Emergency response platforms where a new service ships in 3 minutes

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/emergency-response-platforms-golden-paths

In short: Lakshmi Vara Prasad Adusumilli (Conduent) at Conf42 Platform Engineering 2025 on golden paths, GitOps and multi-region failover for 911-grade systems.

Most platform teams measure success in developer hours saved. Lakshmi Vara Prasad Adusumilli, Senior DevOps Lead and Cloud Lead at Conduent, measures it against a hurricane making landfall while 911 call volume surges. At Conf42 Platform Engineering 2025 he showed how a 12-person platform team supporting more than 80 developers took emergency-service deployments from two weeks to three minutes, using the same building blocks most internal developer platforms use, held to a much stricter bar.

## Downtime during the disaster is the one outage that matters

The setup is simple and grim. Emergency systems have to scale instantly in a crisis, talk to legacy and government systems, stay compliant, and never go down in the exact moment demand peaks. Before the platform work, Lakshmi describes the usual pain: two-week deployments, frequent configuration errors, limited redundancy, isolated ops teams and geographic failover that needed specialist knowledge. Long release cycles and manual steps cannot keep up when a call spike arrives with no warning.

## Golden paths do the thinking nobody has time for

The developer portal is the centre of his platform, and golden paths are its main feature. During a disaster nobody should be working out TLS, network policy or logging by hand, so the pre-approved templates ship with all of it. A new emergency microservice built from a golden path comes pre-wired with centralised logging, TLS and dashboards. He names Backstage as the kind of portal that hosts this, with Helm charts, Terraform modules and Kubernetes YAML blueprints underneath.

Two more portal pieces round it out. A service catalogue lets teams pick databases, queues, caches and object storage without opening tickets; his example is an engineer provisioning a pre-configured Kafka cluster from the catalogue during an incident instead of waiting days. Service scorecards give every microservice a report card for uptime, error rates, recovery time, security posture and latency, fed by Prometheus, Grafana and OpenTelemetry.

## GitOps as the drift alarm

Everything is code and everything goes through Git. Terraform provisions clusters across regions with identical settings; Argo CD or Flux reconciles live state against what is committed, and reverts anything changed directly in the cluster. Lakshmi reports full drift-detection coverage with 73% of deviations auto-remediated. For a regulated emergency system the audit trail is a feature in its own right: every change has a commit, a history and an approval.

## Failover at every layer

The resilience design is layered all the way up. Multiple Kubernetes clusters per region run active-active, regional load balancers are themselves redundant, and individual services such as dispatch or geolocation fail over from cluster A to cluster B without manual intervention. Global traffic management routes users to the nearest healthy region and fails over a whole region if a flood takes a data centre offline. A service mesh adds circuit breaking and mutual TLS so partial failures stay partial. He cites an 800% spike in emergency calls as the kind of load this design spreads across clusters.

Policy as code closes the loop: a deployment that violates a security rule is blocked automatically, without a human gate slowing the team down.

## Who should watch

Platform engineers who already run a portal and want a reference for what "production-grade" means when the users are first responders. It's a broad architecture walkthrough rather than a deep implementation session, and its best advice is the closing one: start with one golden path, measure rigorously, then expand.

## Related Conf42 talks

- [When Clusters Collide: The Misadventures of Disaster Recovery in Kubernetes](https://www.conf42.com/Platform_Engineering_2024_Lev_Andelman_clusters_disaster_kubernetes) by Lev Andelman (TeraSky), for what goes wrong when the failover plan meets reality.
- [Enhancing Business Resilience with Azure Site Recovery](https://www.conf42.com/Cloud_Native_2025_Somaning_Turwale_resilience_disaster_mitigation) by Somaning Turwale (Microsoft), on cloud disaster recovery tooling.
- [Predicting and Mitigating Emergency Situations on the Roads: A Data-Driven Approach](https://www.conf42.com/Internet_of_Things_IoT_2024_Maksim_Kariagin_data_road_emergency) by Maksim Kariagin (Metyis), the data side of emergencies.

[Watch Lakshmi Vara Prasad Adusumilli's talk](https://www.conf42.com/Platform_Engineering_2025_Lakshmi_Vara_Prasad_Adusumilli_response_emergency_approach)

[Watch the talk on YouTube](https://youtu.be/U1py0sXQijY).

## Watch the talk

[Building Resilient Emergency Response Platforms: A Cloud-Native Platform Engineering Approach](https://www.conf42.com/Platform_Engineering_2025_Lakshmi_Vara_Prasad_Adusumilli_response_emergency_approach) at Conf42 Platform Engineering 2025.
