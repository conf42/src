# Nobody deletes microservices, so read your traces like a database

Conf42 Blog, 2021-04-28. https://www.conf42.com/blog/cloud2021/microservices-grow-tracing-data-mocks

In short: Michael Haberman (Aspecto) at Conf42 Cloud Native 2021 on why microservice risk grows with the diagram, and how OpenTelemetry traces can feed docs and mocks

Ask a team how many services they added last year and you get a number. Ask how many they removed and you get a pause. At Conf42 Cloud Native 2021, Michael Haberman, co-founder and CTO of Aspecto and previously chief architect over about 120 microservices, argued that this one-way growth is the core risk of microservices, and that OpenTelemetry tracing data is useful well beyond debugging: as a source for dependency maps, API documentation and realistic test mocks.

The title promises not breaking your APIs; the talk gets there by way of understanding who calls whom, which is the precondition for not breaking anyone.

## How does a microservices project get complicated?

Haberman tells it as a journey. A company migrates off a monolith that is slow to deploy and full of regressions, and starts with a greenfield feature: three services talking HTTP, easy to run locally, easy to draw on a whiteboard, easy to onboard into. It works, so the business asks for more, and a few months later the diagram is a dozen services with dependencies everywhere.

Three questions get hard to answer: what the big picture looks like, who consumes a given service, and how (route, verb, payload contract). His equation for the rest of the talk is simple: as the picture grows, so does the risk of production issues.

The usual fixes are fine and he says so: an architecture document (never fully accurate, always a step behind), a service map or catalogue, and OpenAPI for the HTTP contracts.

## Kafka fixes data loss and hides the consumers

Then comes the first outage. Service A calls service B over HTTP, B is down, and the data is gone. The standard answer is asynchronous messaging (Kafka, Redis pub/sub, RabbitMQ, Amazon SQS); he uses Kafka. The broker persists messages until the consumer is ready, so a dead consumer no longer means lost data.

But look at it from service A's side: it publishes to a topic and no longer knows who reads it. The only way to find out is to search other codebases for the topic name, which is fine with 3 services and painful with 120. There's no response to the message, local debugging now needs the broker running too, and OpenAPI doesn't describe a Kafka payload. He redraws his twelve-service diagram with Kafka added on one side only, and it is already a mess.

## Traces tell the story of one request

His tool for getting the picture back is distributed tracing with OpenTelemetry, the CNCF project. Each service reports what it did (the API call it received, the DB query, the Redis write) to a central place. The first service starts trace 1, span 1, and injects a header into its outgoing call; the next service reports span 2 under the same trace. The demo shows Aspecto's own backend in Jaeger: an API docs service calling an account service to authenticate, then a Lambda querying DynamoDB.

The cheap trick he urges everyone to adopt: log the trace ID with every log line. When a generic exception turns up in your logs, paste its trace ID into Jaeger and see the whole flow that led to it.

Jaeger's dependency graph helps, but only at service level. It shows that A talks to B and C, not that A calls C on the v1 items endpoint and calls B only on v1 purchase. That endpoint-level detail is what developers need, and it is the gap Aspecto targets.

## Tracing data is a database, so query it

The idea that stays with you is the last one. Send spans through the OpenTelemetry Collector to a store such as Elasticsearch, put Jaeger on top, and you hold a record of how production actually communicates. API docs can be generated from real traffic instead of written by hand. Unit test mocks, usually static and never updated, can be pulled from real traces with real usage.

"Go once a week to your database, have a look there. I'm pretty sure you're going to find some interesting stuff," Haberman said at Conf42 Cloud Native 2021.

## Who should watch

Teams somewhere between ten and a hundred services, especially ones adding Kafka or another broker, and anyone who hasn't yet put the trace ID in their logs. Experienced tracing users can skip to the last third for the docs-and-mocks idea.

## Related Conf42 talks

- Michael Haberman on [distributed tracing with OpenTelemetry](https://www.conf42.com/JavaScript_2021_Michael_Haberman_distributed_tracing_OpenTelemetry) at Conf42 JavaScript 2021.
- Nicolas Fränkel on [OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing) at Conf42 DevOps 2023.
- Bogdan Sucaciu on [event-driven architectures with Apache Kafka](https://www.conf42.com/Enterprise_Software_2021_Bogdan_Sucaciu_event_driven_architectures_apache_kafka) at Conf42 Enterprise Software 2021.

[Watch Michael Haberman's talk](https://www.conf42.com/Cloud_Native_2021_Michael_Haberman_microservice_apis)

## From Aspecto

Aspecto builds tooling on OpenTelemetry data to help developers understand and work with microservices; its blog covers more uses of distributed tracing data.

- [aspecto.io](https://aspecto.io/?utm_source=conf42-2021&utm_medium=referral)

[Watch the talk on YouTube](https://youtu.be/IV2KHDxy7dQ).

## Watch the talk

[Hundreds of Microservices without breaking your APIs](https://www.conf42.com/Cloud_Native_2021_Michael_Haberman_microservice_apis) at Conf42 Cloud Native 2021.
