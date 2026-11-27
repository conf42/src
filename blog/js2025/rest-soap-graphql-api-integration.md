# REST, SOAP or GraphQL? Pick by workload, then secure every layer

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/rest-soap-graphql-api-integration

In short: Darshini Jayaprakash of Driscoll's at Conf42 JavaScript 2025 on choosing API styles, middleware, layered API security and event-driven integration.

SOAP is not dead; it just moved to the parts of the economy where a failed transaction makes the news. At Conf42 JavaScript 2025, Darshini Jayaprakash, a senior application developer at Driscoll's, gave a broad tour of enterprise API integration: when REST, SOAP and GraphQL each make sense, what middleware platforms take off your plate, and why security has to be in the design from day one.

This is a fundamentals-and-strategy talk. It suits developers moving from building single services to owning integrations between many, and it stays at the level of patterns rather than code.

## Three paradigms, three jobs

Darshini's comparison is the backbone of the talk:

- **REST** stays dominant because it is simple, uses the HTTP verbs every developer already knows, and is stateless, so each request carries everything the server needs and it scales well in cloud-native systems. The tooling ecosystem around it is vast.
- **SOAP** is heavier, built on XML and strict schemas, but still the backbone in banking, healthcare and government, where WS-Security, reliable messaging and formal contracts between services are requirements, not preferences.
- **GraphQL** lets clients ask for exactly the fields they need, which cuts round trips and suits front ends and mobile apps with nested data and tight bandwidth.

Her summary is pragmatic: SOAP for strict enterprise transactions, REST for general-purpose APIs, GraphQL where flexible, efficient fetching matters.

## Middleware turns integration into configuration

As the number of connected systems grows, point-to-point code becomes fragile. Darshini makes the case for enterprise middleware platforms: prebuilt connectors for systems like Salesforce, SAP, AWS and databases; elastic scaling for seasonal spikes; real-time monitoring of metrics, logs and alerts; and visual, low-code design tools that let technical business users take part. The shift she describes is from writing integration code to configuring and optimising it.

## Security is not a phase at the end

Her strongest point is that security bolted on after the API is finished is the wrong order. The model she recommends is defence in depth: OAuth for token-based access, API gateways for rate limiting, validation and threat detection, and lifecycle management for versioning, deprecation and continuous auditing. Combined, those layers reduce endpoint exposure while keeping the API usable for legitimate clients.

For production, she adds three habits: consistent naming and predictable resource hierarchies, rigorous automated integration, performance and security testing before release, and documentation with interactive explorers, multi-language examples and a clear changelog.

## Where it is heading

The forward-looking section covers event-driven architecture (producers emit events, brokers such as Kafka or RabbitMQ route them, consumers react independently, so failures stay isolated) and AI-assisted testing that generates test cases and predicts failure points. She also sketches ideas still on the horizon, such as self-healing APIs and usage-aware rate limiting.

## Who should watch

Developers and junior architects who need one map of API styles, middleware and security before designing integrations, and teams arguing about whether to retire a SOAP service. Experienced platform engineers will find it familiar; the comparison section is the bit to forward.

## Related Conf42 talks

- [Anirudha Karandikar on API security built in, not bolted on](https://www.conf42.com/DevSecOps_2024_Anirudha_Karandikar_api_security) at Conf42 DevSecOps 2024.
- [Roman Rastiehaiev of HiBob comparing open source API gateways](https://www.conf42.com/Cloud_Native_2025_Roman_Rastiehaiev_api_gateways_comparison) at Conf42 Cloud Native 2025.
- [Dmitry Khorev on scalable event-driven applications with NestJS](https://www.conf42.com/JavaScript_2022_Dmitry_Khorev_scalable_eventdriven_applications_nestjs) at Conf42 JavaScript 2022.

[Watch Darshini Jayaprakash's talk](https://www.conf42.com/JavaScript_2025_Darshini_Jayaprakash_integration_tech_tools), part of [Conf42 JavaScript 2025](https://www.conf42.com/js2025).

[Watch the talk on YouTube](https://youtu.be/zAM9-l7W2yY).

## Watch the talk

[API Integration with JavaScript: Scalable, Secure, and Future-Ready Systems](https://www.conf42.com/JavaScript_2025_Darshini_Jayaprakash_integration_tech_tools) at Conf42 JavaScript 2025.
