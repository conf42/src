# Platform engineering when a dropped frame can hide a lesion

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/endoscopy-imaging-platform-latency-and-uptime

In short: Johnson & Johnson's Santosh Suresh at Conf42 Platform Engineering 2025 on endoscopy imaging platforms with sub-200 ms video, tiered storage and 99.99% uptime.

In most systems a moment of lag is an annoyance. In bronchoscopy, Santosh Suresh pointed out, it could mean missing a critical airway lesion. Santosh, a Principal Engineer at Johnson & Johnson, used his Conf42 Platform Engineering 2025 talk to walk through the infrastructure behind advanced flexible endoscopy: real-time video with end-to-end latency under 200 milliseconds, 99.99% uptime, and storage that never loses an image it cannot recreate.

At about eight minutes it moves fast, close to a narrated reference architecture. That makes it dense, and useful as a checklist.

## The requirements are unusually unforgiving

A single procedure produces massive uncompressed data. The target is end-to-end photon latency below 200 ms, and Santosh says their best systems sit at 90 to 120 ms. Uptime has to be 99.99%. Multiple imaging modalities (RGB, near-infrared, fluorescence) each produce their own data stream with their own processing needs, and modern endoscopes are at least HD. A storage failure is not a retry: the diagnostic imagery is gone.

## Compute, network and a video pipeline

The core infrastructure is clusters with hundreds of CPU cores and multiple high-end GPUs for real-time processing, with dedicated resources for encoding and transcoding, and separate compute pools so batch jobs never steal from live procedures. The network has a 10 Gbps backbone, quality-of-service rules that prioritise endoscopic traffic, multiple edge ingestion points with automatic failover, and low-latency paths for clinical workflows.

The video pipeline runs ingestion, then image enhancement (noise reduction, enhancement, colour correction), then H.265 encoding to save bandwidth while keeping quality, then multi-protocol streaming with adaptive bitrate to viewing stations.

## Three storage tiers, by age

Storage is tiered by how recently a procedure happened:

- **Hot:** NVMe for active and recent examinations, sub-millisecond access.
- **Warm:** SSD for procedures up to 30 days old.
- **Cold:** historical procedures with intelligent compression for cheap long-term retention.

Scaling relies on stateless microservices on Kubernetes with automatic pod scaling, load balancing that considers data locality and network topology, and session affinity so a procedure's stream stays on consistent processing. Performance tricks include GPU acceleration, zero-copy buffer management to minimise memory transfers, caching for hot content, and time-series databases for procedure metrics.

## Designing for failure during a procedure

High availability means no single points of failure (redundant power and network), continuous health monitoring with very fast failure detection, automated failover and geographic resilience. Santosh calls chaos engineering and regular failover testing essential, including partial failures, network partitions and cascading failures under controlled conditions.

Data flows through Kafka buffering for the high-bandwidth feeds, stream processing for validation and enrichment, and a lambda architecture combining stream and batch. Security covers HIPAA with AES-256 at rest, hardware security modules, tamper-proof audit logs with cryptographic signatures, end-to-end encryption from capture to archive, and context-aware authorisation with MFA and SSO. Hospital integration uses DICOM interfaces that turn video into multi-frame objects, PACS connectivity, DICOMweb for REST access, and cross-enterprise sharing.

## The case study

At a 1,200-bed academic medical center running 50,000 endoscopic procedures, the platform brought latency under 200 ms, handled 200-plus concurrent procedures at peak, integrated with the EMR through a federated architecture that preserved video quality, and cut operational cost by about 40% through performance optimisation. Next on his list: deeper AI and ML integration, edge computing, ultra-high-definition and 8K imaging, and 3D reconstruction from endoscopic video for navigation assistance.

## Who should watch

Engineers on real-time video, medical devices or any platform where latency is a safety property. Pause often; the slides carry more than the narration.

## Related Conf42 talks

- [Santosh Suresh on high-definition flexible endoscopy](https://www.conf42.com/Machine_Learning_2025_Santosh_Suresh_flexible_endoscopy), his clinical-side companion talk from Conf42 Machine Learning 2025.
- [Ramakrishna Ambati (Visby Medical) on secure IoT edge architecture for medical diagnostic systems](https://www.conf42.com/Internet_of_Things_IoT_2025_Ramakrishna_Ambati_maintenance_predictive_medical), more medical hardware at the edge.

[Watch Santosh Suresh's talk](https://www.conf42.com/Platform_Engineering_2025_Santosh_Suresh_flexible_advanced_imaging)

[Watch the talk on YouTube](https://youtu.be/uOpzfCw0azU).

## Watch the talk

[Platform Engineering for Advanced Flexible Endoscopy: Scaling Medical Imaging Infrastructure](https://www.conf42.com/Platform_Engineering_2025_Santosh_Suresh_flexible_advanced_imaging) at Conf42 Platform Engineering 2025.
