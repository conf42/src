# Nineteen services, zero calls between them, and nobody paged at 3 a.m.

Conf42 Blog, 2021-09-30. https://www.conf42.com/blog/sre2021/event-driven-services-with-zero-dependencies

In short: Daniel Selans (Batch) at Conf42 Site Reliability Engineering 2021 on event-driven design as the route to self-healing services with tiny failure domains

Reliability nirvana, by Daniel Selans's definition, starts with not being woken up at 3 a.m. on a Saturday. The co-founder of [Batch](https://batch.sh/) and former New Relic SRE argues at Conf42 Site Reliability Engineering 2021 that the next step up in reliability is not more infrastructure but a different way for services to talk: not at all. In an event-driven system each service only reads and writes events on a bus, owns its own state, and picks up where it left off after a crash. Batch runs 19 Go services this way, with zero inter-service dependencies. He is just as clear about the cost, which is mostly organisational.

He opens with a promise worth holding him to. Daniel Selans said at Conf42 Site Reliability Engineering 2021: "So everything that I talk about I have done in production, none of this is theoretical."

## What is wrong with microservices as they are?

Nothing in the platform, he says. Microservices, containers, Kubernetes, service meshes, APM and tracing are all good. The trouble is the services. With 20 or 30 of them calling each other, nobody knows how big the failure domain is: one service can take down six others and slow three more. The standard fix, Hystrix-style circuit breakers, is easy to misconfigure so it trips when nothing is down and drops real requests. And what happens to a request in flight during an autoscaling event? Often it just fails, and the team accepts a small failure rate per deploy.

What he wants instead is effortless reliability: services that don't rely on each other, no per-service fault tolerance code, one blanket firewall rule instead of punched holes, every state change visible, and a full history of system data for a future data science team.

## What makes a system event-driven?

Three actions: something emits an event, something consumes it, something reacts. The rules he insists on:

- **The event is the source of truth.** No service knows the whole system state, only its own.
- **Everything goes through a message bus.**
- **Everything is idempotent.** Track which events you have handled; ignore duplicates; decide in business logic what an out-of-order event means.
- **Accept eventual consistency.** You trade guaranteed consistency for availability; the system is mostly correct and will eventually be correct.

He quotes Ben Morris on the ordering trap. Daniel Selans said at Conf42 Site Reliability Engineering 2021: "bear in mind that if you rely on message ordering, then you are effectively coupling your applications together in a temporal or time based sense." Design so order doesn't matter, and treat exactly-once delivery with suspicion: Kafka supports it, with many caveats, and handling duplicates is simpler.

## What are the building blocks?

- **Event bus: RabbitMQ**, about 20,000 messages a second, with dead lettering and header-based routing that you would have to build yourself on Kafka. Most teams that think they need Kafka, he says, don't.
- **State and config: etcd**, distributed, tolerant of high latency between links, and not going anywhere since Kubernetes depends on it. Services checkpoint which messages they have processed there.
- **Event store: S3**, cheap and reliable.
- **An event archiver** that moves events from the bus into S3, grouped and compressed so you don't end up with a million files in one place.

The payoff list: a crashed service resumes from unacknowledged messages with no extra code, the failure domain shrinks to one service plus the bus and etcd, teams become truly autonomous, one central schema repo (Protobuf or Avro) replaces a zoo of API specs, and the network can refuse all inbound connections.

## What does it look like at Batch?

Batch is an AWS shop on EKS and MSK. Its services are built from one public Go template; most have exactly three dependencies, RabbitMQ, etcd and Kafka. Only the front end's public API is synchronous. There is no service mesh, no service discovery, and mTLS only between services and Kafka. Instead of curl, engineers trigger behaviour by emitting a Protobuf event with plumber, Batch's open source CLI. The archive: an average event of 4 KB, about 15 million system events and roughly 100 GB in S3 since December 2020, a couple of dollars a month.

## How long does it take, honestly?

His slides put rough numbers on it. The easy part is the foundational infrastructure, under two weeks. Schemas take under a week, the schema publishing pipeline about a week, and an example service for developers about two. The hard parts are an event archiver (two to four weeks), a replay mechanism (three-plus), an event viewer (four-plus), and the human work: convincing leadership (two to four weeks) and communicating the architecture across engineering (four-plus).

On existing systems, migrate gradually, using change data capture to expose database updates as events. Daniel Selans said at Conf42 Site Reliability Engineering 2021: "Do not try to do it in one big fell swoop. It never works." Never let one service depend half on CDC and half on events, and don't make CDC the primary source of truth; let services create the events. Expect debugging to get harder, write everything down, and SREs should lead the design rather than watch it.

## Who should watch

Architects and SREs tired of cascading failures, and teams debating whether their next platform should be event-driven. It is an opinionated, production-tested talk with real numbers and an honest bill.

## Related Conf42 talks

- Bogdan Sucaciu on [event-driven architectures with Apache Kafka](https://www.conf42.com/Enterprise_Software_2021_Bogdan_Sucaciu_event_driven_architectures_apache_kafka) at Conf42 Enterprise Software 2021.
- James Eastham on [building an event-driven system](https://www.conf42.com/Cloud_Native_2024_James_Eastham_event_driven_system) at Conf42 Cloud Native 2024.
- Julien Jakubowski on [picking the right messaging platform, RabbitMQ included](https://www.conf42.com/DevOps_2024_Julien_Jakubowski_right_messaging_platform_rabbitmq) at Conf42 DevOps 2024.

[Watch Daniel Selans's talk](https://www.conf42.com/Site_Reliability_Engineering_2021_Daniel_Selans_reliability_nirvana)

## From Batch

Batch, a Y Combinator company, builds observability for the high-throughput data that flows through message brokers such as Kafka and RabbitMQ, and maintains the open source plumber CLI.

- [Batch website](https://batch.sh/)

[Watch the talk on YouTube](https://youtu.be/3ZLBQ1iQP50).

## Watch the talk

[Reliability Nirvana](https://www.conf42.com/Site_Reliability_Engineering_2021_Daniel_Selans_reliability_nirvana) at Conf42 Site Reliability Engineering 2021.
