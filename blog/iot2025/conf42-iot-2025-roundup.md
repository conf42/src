# Conf42 IoT 2025: from houseplants to Kafka, edge AI and payments

Conf42 Blog, 2025-12-19. https://www.conf42.com/blog/iot2025/conf42-iot-2025-roundup

In short: Conf42 IoT 2025 roundup - Grafana-monitored houseplants, IoT data pipelines and lakehouses, edge AI cameras, supply chain security and device payments.

Conf42 Internet of Things (IoT) 2025 ran online on December 18, 2025, with ten talks that followed sensor data from the moment it is measured to the moment someone pays for it. The data track was the strongest, with four talks on moving and storing device telemetry at scale. Around it sat edge AI, supply chain security, payments, and one talk about keeping houseplants alive that may be the best introduction to observability Conf42 has published.

Every session is on the [Conf42 IoT 2025 event page](https://www.conf42.com/iot2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrAoyYvqm9wESh0loKTsm84Y).

## Observability, explained to an eight-year-old

[Marie Cruz](https://www.conf42.com/Internet_of_Things_IoT_2025_Marie_Cruz_sensors_gardening_analytics), Senior Developer Advocate at Grafana Labs and co-author of Contract Testing in Action, declared 2025 the year of no plant casualties. She teamed up with her eight-year-old daughter on a beginner-friendly project: a soil moisture sensor that reports to Grafana Cloud and tells them when to water.

The project is fun, but the real value is the vocabulary. Marie explains IoT, monitoring, and observability through gardening analogies: each plant gets a little helper in the soil that detects moisture and tells you when it needs water. If you have ever struggled to explain your job at a family dinner, take notes. If you have ever killed a house plant, you are the target audience; Marie asks for a show of hands on exactly that.

## The data track: streams, lakehouses, feature stores

Four talks dealt with what happens after billions of devices start talking.

- [Rehmat Kharal](https://www.conf42.com/Internet_of_Things_IoT_2025_Rehmat_Kharal_streaming_scalability_governance) of Conduktor looked at making IoT streams on systems like Kafka reliable, secure, and usable, covering messy pipelines, outages, and governance. The hard part, as the talk frames it, is the move from devices producing data to data producing value.
- [Ketul Dusane](https://www.conf42.com/Internet_of_Things_IoT_2025_Ketul_Dusane_messaging_latency_throughput), a Software Development Engineer at AWS, covered messaging at scale with three pillars: low latency, high throughput, and operational resilience, using caching, load balancing, and anomaly detection.
- [Bhanudeepti Chinta](https://www.conf42.com/Internet_of_Things_IoT_2025_Bhanudeepti_Chinta_lakehouse_analytics_scalable), an Engineering Manager for data, made the point that organisations rarely fail at IoT because they cannot collect data. They struggle because the cost and complexity of managing it grow faster than the value extracted, which is where lakehouse architectures that unify telemetry, device logs, and analytics come in.
- [Manmohan Alla](https://www.conf42.com/Internet_of_Things_IoT_2025_Manmohan_Alla_warehousing_featurestores_optimization) of Apple showed how Snowflake plus a structured feature store turns raw sensor data into ML-ready features, with examples from manufacturing, utilities, energy grids, and smart monitoring.

Watched back to back, these four make a decent reference architecture for device data, from broker to model.

## Edge AI: make the camera think

[Madhu Niranjan Reddy Puduru](https://www.conf42.com/Internet_of_Things_IoT_2025_Madhu_Niranjan_Reddy_Puduru_vision_edge_processing), a Software Engineering Manager at Synchronoss Technologies, made the case against cloud-only smart cameras. Streaming raw video costs bandwidth, adds latency that real-time safety alerts cannot afford, raises GDPR and CCPA privacy questions, and gets expensive across hundreds of cameras. Running the model next to the sensor and sending only events like "person detected" fixes all four. The abstract promises neural networks on $10 hardware, which is the kind of constraint that makes edge work interesting.

[Ramakrishna Ambati](https://www.conf42.com/Internet_of_Things_IoT_2025_Ramakrishna_Ambati_maintenance_predictive_medical), an Enterprise Solutions Architect at Visby Medical, applied edge computing, machine learning, and zero trust security to medical diagnostic devices, moving maintenance from reacting to failures to predicting them, with results from a real deployment.

## Security: the attack comes in the box

[Gresshma Atluri](https://www.conf42.com/Internet_of_Things_IoT_2025_Gresshma_Atluri_security_supplychain_defense), a cybersecurity risk analyst, opened with a story from a hospital she consulted for, where a vulnerability planted during manufacturing put patient safety at risk. Supply chain attacks do not break in through the front door; they arrive in trusted updates and embedded components. She also recalled the Mirai botnet built from baby monitors and cameras with default passwords, and a logistics company whose smart scanners were hijacked through compromised firmware. The defences: hardware attestation, network segmentation, and behavioural analytics.

## Money moves at the edge too

Two talks looked at finance. [Silpa Potluri](https://www.conf42.com/Internet_of_Things_IoT_2025_Silpa_Potluri_payments_microservices_architecture) of GoodLeap, with more than ten years in the payments industry, explained how payment gateways moved from monoliths to microservices to handle transactions initiated by connected devices acting on our behalf. [Swetha Lakkaraju](https://www.conf42.com/Internet_of_Things_IoT_2025_Swetha_Lakkaraju_banking_modular_modernization), with more than 18 years in mainframe-based core banking, argued for modular core architectures that let banks decouple from legacy systems without a big-bang rewrite.

## Partners and what's next

Conf42 IoT 2025 was supported by the [StarterAI](https://www.starterai.dev/) newsletter, the [HockeyStick](https://www.hockeystick.show/) podcast, and the media partners listed on the event page.

For earlier editions of the series, see [Conf42 IoT 2024](https://www.conf42.com/iot2024). And if the data track was your favourite part, the [Conf42 Robotics 2025](https://www.conf42.com/robotics2025) lineup covers similar ground with more moving parts.
