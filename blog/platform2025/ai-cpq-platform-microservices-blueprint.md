# An AI-powered CPQ platform, layer by layer

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ai-cpq-platform-microservices-blueprint

In short: Kishore Epuri at Conf42 Platform Engineering 2025 lays out a microservices blueprint for AI quoting and pricing, from Kafka events to GitOps and SLOs.

Configure, price, quote sounds like a form with a total at the bottom, until you have thousands of product options, discount approvals and a sales team waiting on a number. At Conf42 Platform Engineering 2025, Kishore Epuri, a CPQ solution architect with more than 15 years in the field, walked through a microservices platform that puts machine learning behind every quote and still answers in about 200 milliseconds.

## Three kinds of model, three kinds of service

The core of the design is not one big model. Epuri splits the AI work into three integration patterns, each behind its own service:

- **Gradient boosting** for pricing optimisation, exposed through standard APIs.
- **Neural networks** for configuration recommendations: guided selling and bundles, the backend telling the user what most customers buy with this configuration and what a bundle would save.
- **Real-time adjustment** that nudges prices based on current market conditions.

Data scientists pick the serving framework per model type (he names TensorFlow Serving and MLflow), while the platform gives one monitoring and management layer across all of them. That separation is the platform-engineering point of the talk: the model team chooses its tools, ops still gets one dashboard.

## Every price is an event

Between services sits Kafka, carrying what he describes as millions of pricing events a day, with standardised schemas so the platform can evolve without breaking consumers. Topics are organised by business domain and carry timestamps and correlation IDs.

The useful twist is event sourcing. Because every pricing decision and configuration change is kept as an event, you get a full history for free: what price was offered last week, which configurations users built over time, and an audit trail for compliance and debugging. When finance asks why a customer got that discount, the answer is a replay, not an archaeology project.

## GPUs only when the neural nets need them

The infrastructure section covers Terraform modules across AWS, Azure and Google Cloud to avoid vendor lock-in, a service mesh for encrypted service-to-service traffic and canary releases, and GitOps with Argo CD doing blue-green deploys of new model versions.

Two cost ideas stand out. The autoscaling feeds on model-serving metrics as well as CPU, so scaling reflects actual model performance. And node selection weighs cost against performance, provisioning GPU nodes only when neural-network workloads ask for them. Batch work runs on spot instances with fallback to on-demand, and training jobs run off-peak.

## SLOs that include the model

Epuri's SLO framework starts with the usual 99.9% availability and adds latency targets: 95% of pricing calculations within 200 ms, and an average ML inference latency of 50 ms. On top he puts AI-specific indicators: inference accuracy, prediction consistency across replicas and feature freshness for real-time predictions. That last trio is the bit most platforms still lack.

The rest of the stack is what you would hope for in enterprise software: mutual TLS with certificates rotated by cert-manager, OAuth 2.0 and OpenID Connect, secrets in Vault, a feature store shared by training and serving, Docker Compose environments with mock models for local development, and automated runbooks for incident response.

## The results he reported

For the case study, Epuri said the platform scaled from 10,000 to over 100,000 monthly requests through horizontal scaling, response times fell from around 800 ms to under 200 ms, and time to market for new features dropped by 65%. The talk presents these as headline outcomes rather than walking through the measurement, so read them as one team's report.

## Who should watch

Architects building ML into transactional enterprise systems (CPQ, ERP, order management) will get a complete checklist in one place. It is a slide walkthrough of the architecture rather than a demo or code, and it moves quickly across many layers; if you only care about one, jump to the event-driven or SLO sections.

## Related Conf42 talks

- Bogdan Sucaciu [demystifying event-driven architectures with Apache Kafka](https://www.conf42.com/Enterprise_Software_2021_Bogdan_Sucaciu_event_driven_architectures_apache_kafka) at Enterprise Software 2021, for the event-sourcing half.
- Sirisha Ayyagari on [zero-trust integration patterns for AI-driven pricing in SAP](https://www.conf42.com/DevSecOps_2026_Sirisha_Ayyagari_zerotrust_sap_pricing) at DevSecOps 2026.

[Watch Kishore Epuri's talk](https://www.conf42.com/Platform_Engineering_2025_Kishore_Epuri_cpq_microservices_powered)

[Watch the talk on YouTube](https://youtu.be/OmePnDW1JhM).

## Watch the talk

[Building Scalable AI-Powered Platforms: Microservices Architecture for Enterprise CPQ Systems](https://www.conf42.com/Platform_Engineering_2025_Kishore_Epuri_cpq_microservices_powered) at Conf42 Platform Engineering 2025.
