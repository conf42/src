# SAP pricing is a pipeline problem, not a condition table

Conf42 Blog, 2026-05-10, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/sap-pricing-ai-clean-core-badi

In short: Sirisha Ayyagari of IBM at Conf42 Database DevOps 2026 on real-time SAP pricing with an external AI engine, streaming data and clean core BAdIs.

Enterprises moved finance, procurement and supply chain to the cloud, yet pricing often still runs on condition records, access sequences and transports that take weeks. At Conf42 Database DevOps 2026, Sirisha Ayyagari, Software Developer at IBM, laid out a hybrid design where SAP stays the transactional system of record and an external AI engine, fed by streaming data, does the price optimization.

The talk is an architecture walkthrough for SAP SD people and the data engineers who have to integrate with them. No demo, but a clear blueprint.

## Why condition records can't keep up

Sirisha names three limits of classic SAP SD pricing. Version lag: any change to a pricing table goes through change requests, testing, transports and approvals, which can take days or weeks. Context blindness: rules cannot easily use live inventory, competitor feeds or demand forecasts. And exception proliferation: special conditions and overrides pile up until the pricing logic is fragile. Pricing teams end up spending their time on approvals and overrides rather than on pricing.

Her argument, and the line worth keeping, is that pricing should be treated as a real-time intelligent pipeline rather than a static configuration exercise.

## SAP keeps the authority, AI makes the suggestion

The architecture has three layers. The SAP transactional core handles order execution, compliance validation and financial posting. An integration layer bridges SAP and the outside world through APIs and BAdI extension points. The AI optimization layer runs inference and returns pricing, discount and risk-adjusted recommendations.

The important rule: AI does not replace SAP's authority. SAP still validates and commits every final price. That is also what keeps the design inside SAP's clean core principle, since no standard code is modified. Sirisha points to specific BAdIs: `PRICING_PREPARE` for condition value determination and `PRICING_COMPLETE` for net value calculation, with manual pricing control handled at the same level. The system stays upgrade-safe and cloud-ready, which anyone who has lived through an S/4HANA upgrade with modified standard code will appreciate.

## Feed it fresh data or don't bother

The AI engine is only as good as its inputs: SAP SD order history, inventory availability, customer behaviour, competitor pricing feeds and demand forecasts. Enterprise signals leave SAP through change data capture or SAP Integration Suite, external market feeds and macroeconomic indicators come in through APIs, and Apache Kafka or IBM Event Streams carries the events. The result is continuous pricing rather than periodic updates.

## Run the model like enterprise software

Operationalizing the model gets as much attention as building it. Each model version is traceable to its feature schema and training dataset. Drift detection watches production distributions. If accuracy degrades or latency thresholds are breached, traffic reverts automatically to the last stable model.

Auditability is non-negotiable in pricing: every recommendation is logged with model version, input features, confidence score and decision context, for financial compliance and regulators. Distributed caching keeps prices identical across SAP application servers within a transaction window, and she notes modern inference frameworks can answer in under 100 milliseconds at enterprise throughput.

## Who should watch

SAP architects under pressure to make pricing responsive without breaking clean core, and data platform teams asked to plug ML into ERP. If you have never seen a condition record, the SAP vocabulary will slow you down, but the pattern of keeping the system of record authoritative while an outside engine suggests applies well beyond SAP.

## Related Conf42 talks

- [Sirisha Ayyagari on zero-trust SAP pricing](https://www.conf42.com/DevSecOps_2026_Sirisha_Ayyagari_zerotrust_sap_pricing) at Conf42 DevSecOps 2026, the security side of the same system.
- [Sravan Kumar Nendrambaka on SAP enterprise optimization](https://www.conf42.com/Cloud_Native_2025_Sravan_Kumar_Nendrambaka_sap_enterprise_optimization) at Conf42 Cloud Native 2025.
- [Bogdan Sucaciu on event-driven architectures with Apache Kafka](https://www.conf42.com/Enterprise_Software_2021_Bogdan_Sucaciu_event_driven_architectures_apache_kafka) at Conf42 Enterprise Software 2021.

[Watch Sirisha Ayyagari's talk](https://www.conf42.com/Database_DevOps_2026_Sirisha_Ayyagari_telemetry_tracing_platform)

[Watch the talk on YouTube](https://youtu.be/El1S6XSSKLs).

## Watch the talk

[AI Meets SAP: Building Real Time Pricing Optimization Pipelines Beyond Rule Based Systems](https://www.conf42.com/Database_DevOps_2026_Sirisha_Ayyagari_telemetry_tracing_platform) at Conf42 Database DevOps 2026.
