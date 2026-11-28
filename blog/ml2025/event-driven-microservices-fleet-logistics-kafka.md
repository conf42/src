# Fleet logistics on Kafka, Kubernetes and edge computing

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/event-driven-microservices-fleet-logistics-kafka

In short: Venkata Anil Kumar Nilisetty (Cognizant) at Conf42 Machine Learning 2025 on event-driven microservices for GPS tracking, route optimisation and fleet management.

A delivery truck does not wait for your monolith's four-hour deploy window. At Conf42 Machine Learning 2025, Venkata Anil Kumar Nilisetty, a manager at Cognizant Technology Solutions with more than 15 years building enterprise applications, showed how an event-driven microservices architecture on Spring Boot, Kafka and Kubernetes changed fleet management and logistics, with results across tracking, maintenance, warehouses and last-mile delivery.

It is a short talk, and almost every slide carries a number.

## Why the monolith had to go

Venkata starts with the state of logistics IT. He says 60 to 80% of IT budgets in the sector go into maintaining legacy systems that take four to six hours for minor changes, go down for two to three hours per update cycle, and degrade sharply beyond about a thousand users. Add rising fuel costs, tight delivery windows and complex urban routing, and the case for a rewrite makes itself.

The replacement is textbook: Spring Boot for modular services, Kafka for event streaming, Kubernetes for autoscaling and resilience. Services deploy independently, scale on demand and keep failures local.

## Tracking and edge: put the compute near the truck

Three use cases carry the talk. The first is GPS tracking with a hybrid active-passive model, reaching five to ten metres accuracy in cities and 15 to 20 metres in rural areas. Kafka handles up to 25,000 updates per vehicle per hour with 95% transmission success even in poor signal areas.

The second is edge computing for traffic management. Speed and behaviour checks run on the vehicle side rather than in the cloud, responding to speed violations in 85 milliseconds and to complex behaviour in 120. That cuts false alarms and bandwidth use by up to 78%. It is the right call: a speeding alert that arrives after the driver has slowed down is just a log line.

The third is AI route optimisation using historical data, live traffic and customer delivery windows, which he reports gives 40% faster route planning, 25% more deliveries per vehicle and up to 20% lower delivery costs.

## The business results

The numbers Venkata reports are broad: 45% fewer vehicle breakdowns, 25% lower maintenance costs, 98.5% fleet tracking accuracy, 35% better driving behaviour, 30% fewer accidents and 20% lower insurance premiums. For a 100-vehicle fleet he puts savings at over $350,000 a year from fuel and maintenance alone.

Warehouses get the same treatment: intelligent order batching cut picking times by 38%, real-time inventory improved space use by 42%, and better route planning and load consolidation reduced last-mile costs by 30% and carbon emissions by 28%.

## Resilience by design

The infrastructure slide is the one platform engineers will want to pause on. Pods autoscale between three and ten instances around 70% CPU, uptime holds at 99.95% even during updates, load shedding prevents cascading failures, and active replication recovers from outages in under 30 seconds.

## Who should watch

Engineers modernising a logistics or fleet platform, and anyone pitching Kafka-plus-Kubernetes to a business that still deploys on Sundays. The talk shows results rather than code, so expect architecture and outcomes, not configs.

## Related Conf42 talks

- [Vamsi Anumolu (iCrossing) on fleet management with AI, IoT and Kubernetes](https://www.conf42.com/Cloud_Native_2025_Vamsi_Anumolu_fleet_iot_optimization), a second take on the same problem.
- [Shalini Katyayani Koney (Walmart) on scaling Kafka on Kubernetes past 100,000 messages per second](https://www.conf42.com/Kube_Native_2025_Shalini_Katyayani_Koney_kafka_streaming_scalable), the event backbone under load.
- [Maimoon Saleem (Amazon) on last-mile delivery with cloud and IoT](https://www.conf42.com/Cloud_Native_2025_Maimoon_Saleem_logistics_optimization_efficiency), for the final hop.

[Watch Venkata Anil Kumar Nilisetty's talk](https://www.conf42.com/Machine_Learning_2025_Venkata_Anil_Kumar_Nilisetty_logistics_chain_services)

[Watch the talk on YouTube](https://youtu.be/LTlBTCeYQz0).

## Watch the talk

[Transforming Supply Chain: Smart Logistics & Fleet Management through Event-Driven Microservices](https://www.conf42.com/Machine_Learning_2025_Venkata_Anil_Kumar_Nilisetty_logistics_chain_services) at Conf42 Machine Learning 2025.
