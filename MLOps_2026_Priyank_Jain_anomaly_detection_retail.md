# Building a KPI-Agnostic Anomaly Detection Pipeline for Retail Operations at Scale

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Priyank Jain](https://www.conf42.com/speaker_Priyank_Jain) (Data Scientist II @ Boost Mobile / Echostar Corporation). Page: https://www.conf42.com/MLOps_2026_Priyank_Jain_anomaly_detection_retail

## Abstract

Most anomaly detection systems are built for a single metric and have to be rebuilt every time the business asks a new question. This talk walks through the design of a generalizable, KPI-agnostic anomaly detection pipeline built for a retail network of roughly 3,000 stores, starting with foot traffic data and designed to extend to any time-series KPI with minimal changes. It covers why a three-model ensemble (Prophet, Isolation Forest, and an autoencoder) outperformed any single approach, how severity scoring and automated reason-labeling were layered on top, and the practical data quality problems that showed up along the way, from zero-traffic days to extreme outliers. The talk closes with the roadmap for adding LLM-based root cause reasoning to explain anomalies automatically.
