# Telecom reliability needs better signals, not more alerts

Conf42 Blog, 2025-05-12. https://www.conf42.com/blog/obs2025/telecom-needs-better-signals-not-more-alerts

In short: Ajay Averineni of IBM at Conf42 Observability 2025 on moving telecom monitoring from reactive alerts to AI anomaly detection with LSTMs, NLP and closed loops.

The outage that starts Ajay Averineni's talk is a familiar one: dozens of alerts from different systems, none of them clear, hours spent finding the root cause, and the signals sitting in the data days earlier. At Conf42 Observability 2025, Averineni, Lead Application Developer at IBM, walked through how a telecom operations team moved from reactive monitoring to AI-assisted anomaly detection, and why the hardest part was getting the operators to trust it.

His takeaway from that outage fits in one line: "We don't need more alerts." What the team needed was better intelligence on top of the alerts they already had.

## Telecom data is big, siloed and short on context

Averineni frames the problem with scale. He cited telecom networks generating up to 25 terabytes of operational data a day, a number growing with 5G and IoT, and the claim that most outages are preventable if the early signals get caught. Traditional monitoring fails in three ways in his telling: it is reactive (users notice first), siloed (network, infrastructure and applications watched separately) and short on context (alerts fire on narrow metrics with no bigger picture). He compares troubleshooting under those conditions to solving a puzzle with half the pieces missing.

The fix he describes is the observability one: collect metrics, logs and traces across domains, replace fixed thresholds with dynamic baselines so normal fluctuations stop triggering alert storms, and let self-learning models keep adjusting those baselines.

## Two models for two kinds of data

The technical core is short and concrete. For metrics, the team used LSTM-based models to catch temporal anomalies in high-dimensional time series. For logs, they applied natural language processing to pull patterns out of unstructured text. Correlating the two, structured time series plus unstructured logs, is what he says traditional tools could not match.

The build order matters too. They started by aggregating 18 months of telemetry, trained deep learning models on telecom-specific patterns (which he stresses look very different from standard enterprise data), and then added tracing through every layer from hardware to virtual network functions.

## Trust was the real bottleneck

The section worth the watch is the one on culture. Operations engineers were sceptical, so the team brought them in from day one: operators tested the models, flagged false positives and suggested new inputs. Averineni says that buy-in changed everything, and it is the bit most AIOps rollouts skip.

Two engineering choices supported that trust. A unified entity model tied infrastructure, virtual functions and services together so an anomaly could be placed in context. And an explainable AI layer with visual tools showed operators why an alert fired, which he credits with cutting false positives by 27%. Edge filtering and intelligent sampling kept the terabytes-a-day problem manageable.

## The architecture closes the loop

The final design has three layers: distributed agents collecting telemetry, a stream processing layer running ML pipelines in real time, and a knowledge and automation layer driving auto-remediation and model refinement. Each incident feeds back into the models, so detection, root cause analysis and remediation become a loop instead of a ticket queue. His closing roadmap is sensible: assess the current stack, pilot one domain, scale gradually while unifying data, and only then automate remediation.

## Who should watch

Operations and SRE teams in telecom or any network-heavy business drowning in alerts, and anyone planning an AIOps pilot who wants a realistic order of operations. It is a short, high-level talk; you will not get model hyperparameters, but you will get a sensible sequence and an honest note on adoption.

## Related Conf42 talks

- [Go-Powered Telecom BSS: Scaling Enterprise Solutions with Microservices, AI, and Cloud-Native Architecture](https://www.conf42.com/Golang_2025_Bhaskara_Beeraka_telecom_microservices_scaling) by Bhaskara Beeraka at Conf42 Golang 2025.
- [AIOps: New Approaches to Reduce Alert Noise](https://www.conf42.com/DevSecOps_2024_Birol_Yildiz_aiops_alert_noise) by Birol Yildiz at Conf42 DevSecOps 2024.
- [Anomaly Detection with Apache Pinot & ThirdEye](https://www.conf42.com/Cloud_Native_2023_Yoav_Nordmann_anomaly_detection_apache_pinot_thirdeye) by Yoav Nordmann at Conf42 Cloud Native 2023.

[Watch Ajay Averineni's talk](https://www.conf42.com/Observability_2025_Ajay_Averineni_service_telecom_reliability) or the [YouTube recording](https://youtu.be/WfxRXjcf6Bk).

## Watch the talk

[Observability-Driven Intelligence: AI-Powered Anomaly Detection for Telecom Service Reliability](https://www.conf42.com/Observability_2025_Ajay_Averineni_service_telecom_reliability) at Conf42 Observability 2025.
