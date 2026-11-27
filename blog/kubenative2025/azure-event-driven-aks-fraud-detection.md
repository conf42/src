# Event Grid, Service Bus and AKS for sub-two-second fraud checks

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/azure-event-driven-aks-fraud-detection

In short: Ashif Anwar (Wolters Kluwer) at Conf42 Kube Native 2025 on event-driven patterns on Azure and a fraud pipeline on Event Grid, Service Bus, Functions and AKS.

Kubernetes gives you the stage, but events are what make anything happen on it. At Conf42 Kube Native 2025, Ashif Anwar, Principal Engineer at Wolters Kluwer, explained how to combine Azure Kubernetes Service with Azure's event services, and walked through a fraud detection system that cut response time from minutes to under two seconds.

His argument for event-driven design is the letter-versus-phone-call analogy: you post the letter and get on with your day instead of waiting on the line. Services that communicate asynchronously through events are loosely coupled, scale with the flow of traffic, contain failures instead of cascading them, and react the moment something happens, with no polling.

## Each Azure service has one job

Anwar mapped the Azure toolkit onto distinct roles. Event Grid is the nervous system: a hyperscale pub/sub router with massive fan-out, attribute-based filtering, built-in retries and dead-lettering, suited to IoT telemetry or microservices that react to the same event. Service Bus is the circulatory system: durable queues and topics, sessions for first-in-first-out ordering, and dead-letter queues for messages that cannot be delivered. That matters wherever a lost or reordered message means money, such as high-value financial transactions.

Azure Functions are the reactive glue: serverless handlers triggered by Event Grid, Service Bus, HTTP or Blob Storage, scaling from zero to thousands of concurrent executions for enrichment, filtering and routing. AKS runs the heavy, long-lived workloads and integrates natively with the messaging services.

## Patterns matter more than products

The patterns section is a clear refresher. CQRS separates read and write models so each can be optimised. Event sourcing stores the sequence of events instead of only the latest state, which gives you a full audit trail and the ability to rebuild any past state. Sagas coordinate multi-service transactions with compensation, his example being a trip where a cancelled flight must undo the hotel and car booking. And he advised finding a balance between choreography, where services react independently, and orchestration, where a controller directs them.

## The fraud pipeline, step by step

The case study starts with legacy fraud detection that took minutes or hours, and a goal of under two seconds with 95% accuracy. Every transaction from payment services on AKS becomes an event. Event Grid routes it to Service Bus for reliable ordering. An Azure Function enriches it with customer history and context. A machine learning model on GPU-backed AKS pods scores it within milliseconds. A final function approves, rejects or flags the transaction for review.

For Black Friday-style peaks, Event Grid absorbs millions of events per second, Service Bus retries and dead-letters so no message is lost, Functions scale out instantly and the model pods scale horizontally. The results he reported: sub-two-second response, 15% fewer false positives, 100% uptime during peak periods, and correlation IDs that trace every event end to end.

## The lessons are the reusable part

Four lessons apply well beyond finance. Make handlers idempotent so a redelivered event does not charge someone twice. Version event schemas semantically so consumers can handle old and new. Always carry correlation IDs. And use managed identities and RBAC instead of hard-coded credentials. He closed with healthcare telemetry, retail inventory sync and insurance claims as other places the same patterns apply.

## Who should watch

Engineers building on Azure who are choosing between Event Grid, Service Bus and Functions, and architects moving a synchronous monolith towards events. Azure-specific, but the patterns and lessons travel to any cloud.

## Related Conf42 talks

- [So You Want To Build An Event Driven System?](https://www.conf42.com/Cloud_Native_2024_James_Eastham_event_driven_system) by James Eastham (AWS) covers the fundamentals from the AWS side.
- [An Introduction to Saga Pattern for Distributed Transactions](https://www.conf42.com/Cloud_Native_2023_Dmitry_Khorev_saga_pattern_distributed_transactions) by Dmitry Khorev (Mero) goes deeper on sagas and compensation.
- [Building Resilient Asynchronous Commerce Systems](https://www.conf42.com/Observability_2025_Anup_Raja_Sarabu_asynchronous_eventdriven_commerce) by Anup Raja Sarabu (T-Mobile) is about observing event-driven systems in production.

[Watch Ashif Anwar's talk](https://www.conf42.com/Kube_Native_2025_Ashif_Anwar_azure_eventdriven_patterns)

[Watch the talk on YouTube](https://youtu.be/b4o5x4SQ5P4).

## Watch the talk

[Scaling Kubernetes-Native Systems with Event-Driven Patterns on Azure](https://www.conf42.com/Kube_Native_2025_Ashif_Anwar_azure_eventdriven_patterns) at Conf42 Kube Native 2025.
