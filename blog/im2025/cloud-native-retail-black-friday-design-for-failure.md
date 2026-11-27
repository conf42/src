# Black Friday-proof retail: design for failure, migrate by strangler fig

Conf42 Blog, 2025-10-02, updated 2026-11-09. https://www.conf42.com/blog/im2025/cloud-native-retail-black-friday-design-for-failure

In short: Maruti Pradeep Pakalapati (Capital One) at Conf42 Incident Management 2025 on autoscaling, circuit breakers, real-time inventory and strangler-fig migration for retail.

When the product detail service slows down on Black Friday, the right answer is a cached page and a completed checkout, not an error. At Conf42 Incident Management 2025, Maruti Pradeep Pakalapati, Software Engineer Technical Lead at Capital One, laid out the cloud-native patterns retailers lean on to survive their biggest weekend, and tied each one back to incident response: how fast you detect, how small the blast radius stays, and whether revenue keeps flowing while you fix it.

The framing is retail-wide rather than a single company's case study, and it moves from why to how in a tidy order: autoscaling, microservices, personalisation, inventory, resilience, security, incidents, observability and migration.

## Peak weekends make every outage expensive

Pakalapati opens with the stakes. Black Friday and Cyber Monday can account for more than 20% of a retailer's annual revenue, customers expect sub-second responses on every channel, and inventory has to be accurate in real time across web and stores. The old answer was to buy servers at three to four times normal demand and let them idle most of the year. Elastic autoscaling, guided by demand forecasts and live monitoring, replaces that.

## Contain the blast radius

Monoliths fail as a unit: one checkout bug and the site is gone. Splitting catalogue, cart, checkout and payments into independent services lets each one scale, fail and deploy on its own. He pairs that with the classic resilience patterns: circuit breakers against cascading failure, bulkheads to isolate resources, back-pressure to stop overload, and async communication to loosen coupling.

The most useful example is graceful degradation. If the product detail service is slow, serve cached or simplified content instead of an error. The shopper still buys, revenue still flows and the incident stays small. Fallbacks and rate limiting are part of the design from day one, not something bolted on after the first bad Black Friday.

## Inventory as an event stream

Legacy inventory relied on batch updates that could lag by 15 to 60 minutes, which is how you sell the last pair of shoes twice. The cloud-native version publishes every sale as an event to Kafka or Kinesis, fans updates into Redis caches across regions and serves them through a GraphQL layer. He describes inventory visibility in under 200 milliseconds across digital and physical channels, enough to support buy-online, pick-up-in-store.

Personalisation gets a similar treatment: recommendation engines isolated as their own services, scaled separately on GPUs for inference and backed by session caching, so they don't drag down the rest of the site at peak.

## Observability tied to revenue

On incidents, he contrasts typical pre-cloud-native numbers (detection over 45 minutes, recovery over four hours) with what SRE practices deliver: detection in under a minute through automated alerting, and much faster resolution thanks to canary analysis, automated rollbacks and playbooks for partial failures. The figures he cites across the talk are industry-level claims rather than measurements from one system, so treat them as targets.

The sharper point is about what to watch. Metrics, structured logs with trace IDs and end-to-end traces are table stakes. Leading retailers also track cart abandonment against service latency, watch revenue impact during incidents and run synthetic shopping journeys that exercise checkout continuously. Recovery means the customer can buy again, not that the pods are green.

## Strangle the monolith, don't swap it

For legacy platforms he recommends the strangler fig pattern: an API gateway routes traffic to either the old system or new services, traffic shifts as each new service proves itself, and the monolith is retired quietly. Team structure matters too: product-aligned squads owning domains end to end, platform teams providing self-service infrastructure, SRE practices embedded in squads and security as code in CI/CD, with short-lived secrets and scanned immutable images.

## Who should watch

Engineers and architects at retailers planning for peak season, or partway through a monolith migration. It is a broad, well-organised overview rather than a deep implementation talk, and the graceful-degradation and observability sections are the most reusable.

## Related Conf42 talks

- [Cloud-Powered Retail: Serving Future Needs Today](https://www.conf42.com/Cloud_Native_2025_Rustam_Orudzhev_retail_services_optimization) by Rustam Orudzhev covers similar ground from the services side.
- [Feature Flags as a Migration Engine](https://www.conf42.com/Feature_Flags_2026_Jaya_Chand_Bandi_migration_payment_platforms) by Jaya Chand Bandi shows another way to decompose a monolith safely.
- [Leveraging AI-Driven Insights for Incident Management: Enhancing Customer Retention](https://www.conf42.com/Incident_Management_2024_Anandakumar_Kumaravelu_4_ai_retention_personalization) by Anandakumar Kumaravelu links incidents and personalisation to customer loyalty.

[Watch Maruti Pradeep Pakalapati's talk](https://www.conf42.com/Incident_Management_2025_Maruti_Pradeep_Pakalapati_retail_cloudnative_scalability)

[Watch the talk on YouTube](https://youtu.be/ZPVNHoJ3c-A).

## Watch the talk

[Cloud-Native Retail at Scale: Agility, Resilience, and Cost Efficiency](https://www.conf42.com/Incident_Management_2025_Maruti_Pradeep_Pakalapati_retail_cloudnative_scalability) at Conf42 Incident Management 2025.
