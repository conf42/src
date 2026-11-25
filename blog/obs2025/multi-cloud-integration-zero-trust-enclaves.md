# Four building blocks for wiring multiple clouds together safely

Conf42 Blog, 2025-05-19, updated 2026-11-09. https://www.conf42.com/blog/obs2025/multi-cloud-integration-zero-trust-enclaves

In short: Naga Swetha Kattula (IEEE) at Conf42 Observability 2025 on AI-driven API management, confidential computing, zero trust and event-driven integration.

Running on AWS, Azure and Google Cloud at once avoids vendor lock-in and buys you three security models, three API styles and three ideas of what a data format is. At Conf42 Observability 2025, Naga Swetha Kattula, a Senior Member of IEEE, walked through four building blocks for integrating those platforms without leaving gaps: AI-driven API management, confidential computing, zero trust and event-driven architecture.

## The integration tax grows with every cloud

Naga frames the problem with the trade-off everyone in a multi-cloud shop knows. You pick each provider for what it does best, then pay for it in integration work: data synchronisation hurdles that cause delays and budget overruns, inconsistent API structures and auth mechanisms, different storage formats, and a separate security policy per provider. Her claim is that each added cloud raises integration complexity by at least 70%, and that the fix is a unified security and integration strategy instead of per-cloud glue.

## AI in the API gateway

The first block is API management that uses machine learning for design, documentation, traffic optimisation and attack detection. The talk compares traditional and AI-enhanced approaches on false-positive rate, attack detection and successful exploitation. Naga reports that ML models can detect up to 93% of API-based attacks while keeping false positives below 4%. It is the part of the talk closest to observability: the detector is only as good as the telemetry it watches.

## Protecting data in use, not just at rest

Confidential computing gets the most detail. Data at rest is covered by encryption, data in transit by TLS. Data in use, while it is being computed on, is the gap. Hardware-based trusted execution environments create enclaves that keep data encrypted during computation, so even system administrators and the cloud provider cannot read it. Naga notes that Intel SGX implementations have grown secure memory from 128 MB to 512 GB, which widens the set of workloads that fit inside an enclave.

The use cases are concrete: healthcare teams processing PHI in the cloud under HIPAA, financial institutions running analytics on sensitive data, and federated learning where several organisations train a model on combined data without seeing each other's raw records.

## Zero trust as the default posture

Zero trust appears in its standard form: never trust, always verify. Every entity is authenticated and authorised continuously regardless of network location, access follows least privilege, workloads sit in isolated zones, and real-time behaviour analytics watch for anything odd. The model assumes breach and treats each request as if it came from an untrusted network. Naga cites a 43% reduction in successful network intrusions and a 37% reduction in incident response costs for organisations that adopted such frameworks, and says real-time behaviour analytics spotted suspicious activity 73% faster than periodic scanning.

## Events instead of batch jobs

The last block is event-driven architecture: sources emit events, a bus routes them, subscribers react, and state is kept consistent across services. Loose coupling makes it a good fit for keeping data in sync across clouds in real time. Naga reports a 58% reduction in integration latency compared with scheduled batch processing, and gives an industrial IoT example of processing data from over 25,000 sensors with sub-second response.

## Who should watch

Architects drawing the first diagram of a multi-cloud integration strategy and wanting a checklist of the security pieces. This is a broad survey: each of the four topics gets a few slides, the figures are cited without naming the deployments behind them, and there is no code. Treat it as a map and go to the related talks below for the territory.

## Related Conf42 talks

- [Moritz Eckert on confidential computing with Go and Intel SGX](https://www.conf42.com/Golang_2021_Moritz_Eckert_confidential_computing_Intel_SGX_security_cloud_native) at Conf42 Golang 2021.
- [Srinivas Vallabhaneni on scaling secure enclaves in Go-powered distributed systems](https://www.conf42.com/Golang_2025_Srinivas_Vallabhaneni_enclaves_security_confidential) at Conf42 Golang 2025.
- [Bogdan Sucaciu demystifying event-driven architectures with Apache Kafka](https://www.conf42.com/Enterprise_Software_2021_Bogdan_Sucaciu_event_driven_architectures_apache_kafka) at Conf42 Enterprise Software 2021.

[Watch Naga Swetha Kattula's talk](https://www.conf42.com/Observability_2025_Naga_Swetha_Kattula_integration_platforms_secure)

[Watch the talk on YouTube](https://youtu.be/jXW32mGnU0k).

## Watch the talk

[Next-Gen Cloud: Enabling Secure and Seamless Cross-Platform Integration for Enterprise Transformation](https://www.conf42.com/Observability_2025_Naga_Swetha_Kattula_integration_platforms_secure) at Conf42 Observability 2025.
