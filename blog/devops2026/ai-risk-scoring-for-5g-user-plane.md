# Scoring every 5G session for risk before it reaches the UPF

Conf42 Blog, 2026-01-22. https://www.conf42.com/blog/devops2026/ai-risk-scoring-for-5g-user-plane

In short: Binu Govindan of Microsoft at Conf42 DevOps 2026 on multi-factor AI risk scoring and a tiered mitigation pipeline for the 5G user plane function.

Signature-based detection catches the attacks you have already seen. At Conf42 DevOps 2026, [Binu Govindan](https://www.conf42.com/DevOps_2026_Binu_Govindan_network_screening_mitigation), Principal SDET at Microsoft working on 5G and Azure, described a different approach for the 5G user plane function: give every session a risk score from several behavioural factors, then let a tiered pipeline shape, isolate or terminate it, with an analyst in the loop.

Govindan was clear that the talk reflects his own views, not his employer's. It's an architecture overview of about 15 minutes, aimed at people who run telecom or cloud-native network infrastructure and wonder how to secure UPF at scale.

## Why the user plane is the target

The UPF is the heart of the network, he explains: it carries the bulk of user traffic from devices out to external networks. And 5G gives attackers more to work with than earlier generations. The protocols are complex, with loopholes in signalling and the data plane. The core is virtualised and service-based, running on cloud and Kubernetes, which adds the usual cloud-native attack surfaces. And slice misconfigurations have historically opened doors to exploitation.

## Five signals instead of one signature

His risk scoring framework weighs five kinds of evidence for each session:

- **Behavioural analysis**: how the session behaves over time, including duration and packet sizes.
- **Geographic context**: sessions from areas where threats have been seen before score higher.
- **Temporal indicators**: time-based patterns of activity.
- **Volumetric metrics**: how much data and usage, which is where DDoS and resource congestion show up.
- **Historical intelligence**: a database of past attacks and their nature.

The model combines them into a high, medium or low score per session. The real-time loop collects traffic and telemetry, including CDR-style records from calls, scores sessions, classifies threats and triggers responses, and keeps learning as attack patterns evolve.

## Mitigation is a pipeline with escalating steps

The part DevOps teams will recognise is the response, written as an automated, tiered pipeline. Level one is enhanced monitoring, pulling data from Prometheus and call records. When a session looks risky, the pipeline applies traffic shaping and QoS adjustments. A high-risk session gets isolated, and the last step terminates it. The policies live as rules in the pipeline, and the AI can propose new rules too.

Humans stay involved: a trained analyst executes response actions for sessions classified as threats. The operational benefits he lists are the ones you'd expect: less alert fatigue, because some automated action has already happened before an alert reaches an analyst, faster incident response and more consistent operations. Think of it as a circuit breaker for subscribers rather than services.

## Fitting into a DevOps workflow

For integration, Govindan describes a GitOps-compatible, containerised deployment with Prometheus metrics, OpenTelemetry, an API-first design that plugs into CI/CD, and Kubernetes-friendly packaging. His rollout advice is the right kind of cautious: establish a baseline first, letting the system observe the network for one to several weeks to learn what good and bad sessions look like; then define policies on top of the telemetry pipeline and train analysts; and only then scale gradually towards full automation. He calls the end state 5G SecOps.

## Who should watch

Telecom engineers, network security teams and SREs running a 5G core on Kubernetes. The talk stays at the architecture level, with no model details or evaluation results, so treat it as a blueprint to compare against your own design.

## Related Conf42 talks

- [Observability-Driven Intelligence: AI-Powered Anomaly Detection for Telecom Service Reliability](https://www.conf42.com/Observability_2025_Ajay_Averineni_service_telecom_reliability) by Ajay Averineni at Conf42 Observability 2025.
- [Harnessing AI for Autonomous Threat Defense in Multi-Cloud Security](https://www.conf42.com/Machine_Learning_2025_Pradeep_Kurra_threat_defense_autonomous) by Pradeep Kurra at Conf42 Machine Learning 2025.
- [Go-Powered Telecom BSS: Scaling Enterprise Solutions with Microservices, AI, and Cloud-Native Architecture](https://www.conf42.com/Golang_2025_Bhaskara_Beeraka_telecom_microservices_scaling) by Bhaskara Beeraka at Conf42 Golang 2025.

[Watch Binu Govindan's talk](https://www.conf42.com/DevOps_2026_Binu_Govindan_network_screening_mitigation) or the [YouTube recording](https://youtu.be/kVJYMsg5d1w).

## Watch the talk

[AI-Driven Threat Screening for 5G UPF with Automated Risk Mitigation](https://www.conf42.com/DevOps_2026_Binu_Govindan_network_screening_mitigation) at Conf42 DevOps 2026.
