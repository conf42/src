# Warehouse IoT ML fails on data and integration, not models

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/warehouse-iot-ml-fails-on-data-not-models

In short: Dinesh Garg of Honeywell at Conf42 Machine Learning 2026 on feature engineering, MLOps and rollout tactics for ML on messy warehouse IoT data.

The shop floor says ten pieces, the system says eight, and the robot that was meant to record the move stopped logging during a heat wave. At Conf42 Machine Learning 2026, Dinesh Garg, a senior IT manager in digital supply chain at Honeywell, talked about turning that kind of warehouse IoT data into production ML, and he was refreshingly blunt that much of the industry is not there yet.

His thesis fits on a sticky note: raw data does not equal actionable intelligence.

## Three reasons ML stalls before production

Warehouses produce huge volumes of operational data; one inventory transaction alone writes several records. The problem is not collection. Dinesh listed three reasons models stay theoretical:

- **Data quality**: failed sensors, inventory drift between the floor and the system, network gaps and environmental interference.
- **Integration**: everything claims to be REST-compatible, and in practice much of it is not. Moving to the cloud adds latency and synchronisation problems between components.
- **Performance degradation**: behaviour on the floor keeps changing, so a model that fit last quarter slips.

He gave a sense of scale from his own job: months where support reports 10,000 failed transactions because one interface or one production-line sensor stopped recording properly.

## Features that respect time

The feature engineering advice is concrete. Replace static lead times with rolling windows. Track time since the last event, for instance since the last cycle count, so an adjustment that is far off the usual pattern stands out. Use time-series imputation for gaps instead of the planner guessing. Push compute to the edge where latency matters.

For missing data specifically he suggested time-series-aware imputation, multi-sensor fusion (with the caveat that more sensors cost more), and metadata features that help spot equipment health issues from the signals themselves.

## MLOps and rollouts that assume things break

The production architecture has three parts: containerised model serving on lean microservices, model versioning so a bad release can be rolled back to the previous version in minutes rather than rebuilt, and continuous monitoring for the drift he clearly spends a lot of time worrying about. He also suggested approximate matching with cosine similarity in place of exact lookups where 80-90% accuracy is good enough, because the current process often does worse.

Rollouts go in stages: shadow mode first, with predictions running beside the existing process and no operational effect, then canary, A/B testing and finally full rollout.

## Who should watch

Supply chain and manufacturing IT teams trying to get a first model live, and data scientists who have never seen how messy warehouse data is. It is a practitioner's view from the operations side, light on modelling detail and heavy on the reasons projects stall.

## Related Conf42 talks

- [SRE for Supply Chain: Building Reliable Human-AI Warehouse Operations at Scale](https://www.conf42.com/DevOps_2026_Vishnu_Prasad_supplychain_reliability_warehouses) by Vishnu Prasad.
- [Building a Production Computer Vision Verification System for Warehouse Receiving](https://www.conf42.com/Cloud_Native_2026_Anton_Solomonov_computer_vision_verification) by Anton Solomonov, another way to fix the "system says eight" problem.
- [Introduction to MLOps at the Edge](https://www.conf42.com/Machine_Learning_2023_Alejandro_Cantos_introduction_mlops_edge) by Alejandro Cantos.

[Watch Dinesh Garg's talk](https://www.conf42.com/Machine_Learning_2026_Dinesh_Garg_evaluation_benchmarks_metrics) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/v6am64xyEeA).

## Watch the talk

[ML-Powered IoT: From Warehouse Data to Production Intelligence in Real Time](https://www.conf42.com/Machine_Learning_2026_Dinesh_Garg_evaluation_benchmarks_metrics) at Conf42 Machine Learning 2026.
