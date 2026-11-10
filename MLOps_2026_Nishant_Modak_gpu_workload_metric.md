# Which Workload Owns This GPU Metric?

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Nishant Modak](https://www.conf42.com/speaker_Nishant_Modak) (Chief Evals Officer (CEO) @ Last9). Page: https://www.conf42.com/MLOps_2026_Nishant_Modak_gpu_workload_metric

## Abstract

GPU telemetry starts with a device identifier. An ML platform starts with a job, pod, model, or team. Those names do not line up.  This talk shows how we built an OpenTelemetry Collector processor that joins node-level GPU data to the Kubernetes workload using the device. We will follow one metric from its GPU UUID through device allocation, pod discovery, and workload ownership until it becomes useful for capacity, performance, and failure analysis.  The join is the interesting part. MIG changes what a device means. Pods move. Short jobs disappear before a cache refreshes. Device assignments and telemetry arrive on different clocks. A mapping layer can quietly attach the right metric to the wrong workload unless it preserves uncertainty.  We will build the attribution path, examine its Kubernetes API and RBAC boundary, and then break it with the cases above. The result is ordinary OTLP with pod, namespace, deployment, and job identity. No backend-specific GPU model is required.  This is a systems talk about the missing layer between GPU monitoring and useful MLOps telemetry.
