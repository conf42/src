# Scale on the forecast, not on the CPU alarm

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/scale-on-the-forecast-not-the-alarm

In short: Vivek Kumar of Majesco at Conf42 Machine Learning 2026 on using telemetry-trained models to scale transaction platforms before the spike.

A scaling rule that fires when CPU crosses 70% is a smoke detector: it tells you about the fire once the kitchen is already full of smoke. At Conf42 Machine Learning 2026, Vivek Kumar, a staff developer at Majesco with 16 years of building insurance and finance platforms, argued for flipping that around: train models on the telemetry you already collect and scale on the forecast, before latency climbs.

It is an overview talk rather than a code walkthrough, and a good one to hand to a team that still tunes threshold alerts by hand.

## Static thresholds react after the damage

Vivek's starting point is the setup most transaction platforms share: Spring Boot microservices, REST APIs behind a gateway, Kafka for events, a database per service. That architecture scales well, but it also makes performance harder to reason about, because the bottleneck moves around.

Rule-based scaling handles this badly. By the time the threshold trips and new capacity arrives, he pointed out, users have already seen the slowdown, and sometimes the downtime. The rule is reactive by design.

## Your telemetry is already a training set

The core idea is that every system emits the data needed to predict its own load: CPU, latency, thread utilisation, request rates, queue depth, transaction volume. Vivek treats those as model features. Concurrency level, queue depth, volume and resource use become the inputs that tell a model what the next few minutes will look like.

He walked through three model families and the job each does:

- **LSTM networks** for forecasting load from time-series history, such as future CPU or request volume.
- **Anomaly detection** for spotting behaviour that suddenly departs from normal.
- **Regression** for predicting how many resources a given workload needs.

## Three things the model can actually turn

Prediction is only useful if it drives an action. Vivek grouped the actions into adaptive autoscaling (add capacity on the forecast), dynamic caching, and real-time configuration tuning: connection timeouts, batch sizes and retry policies adjusted to the current workload instead of a value someone picked during the last incident.

His comparison slide credits ML-driven systems with 73% fewer performance incidents and 28% lower infrastructure cost, the latter from scaling back down in quiet hours. Treat those as the talk's headline figures rather than a benchmark you can reproduce from the slides.

## The loop matters more than the model

The architecture he closed on is a feedback loop: telemetry flows from a tool such as CloudWatch into the model, the model emits a prediction, the autoscaler adjusts containers or Kubernetes capacity, and the new telemetry feeds the next round. He pointed to AWS predictive auto scaling and Azure Kubernetes Service as proof that the cloud providers already run this pattern.

His production advice is the sensible kind: models sitting in the transaction path need consistent latency and high availability themselves, so start with one focused use case, deploy with safeguards, and widen the loop only when it has earned trust.

## Who should watch

Platform and SRE engineers who own autoscaling policies and want the vocabulary for a predictive approach. If you already run forecast-driven scaling in production, this will be familiar ground; the value is in the clean framing you can reuse in a design review.

## Related Conf42 talks

- [Proactive cluster autoscaling in Kubernetes](https://www.conf42.com/Cloud_Native_2023_Chris_NesbittSmith_proactive_cluster_autoscaling_kubernetes) by Chris Nesbitt-Smith, the infrastructure side of scaling ahead of demand.
- [Forecasting based proactive optimization of cloud resources](https://www.conf42.com/Chaos_Engineering_2021_Pawe_Skrzypek_Alicja_Reniewicz_proactive_optimization_cloud_resources) by Paweł Skrzypek and Alicja Reniewicz, the same idea applied to cloud resource planning.
- [Kubernetes Scaling for Savings and Stability: Beyond HPA and VPA](https://www.conf42.com/Observability_2026_Joshua_Fox_kubernetes_autoscaling_reliability) by Joshua Fox, for what comes after the default autoscalers.

[Watch Vivek Kumar's talk](https://www.conf42.com/Machine_Learning_2026_Vivek_Kumar_responsible_ethics_ai) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/Dw8zO4qk6Qc).

## Watch the talk

[Applying Machine Learning to Performance Optimization in High-Volume Transaction Systems](https://www.conf42.com/Machine_Learning_2026_Vivek_Kumar_responsible_ethics_ai) at Conf42 Machine Learning 2026.
