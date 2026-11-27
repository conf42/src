# Real-time translation is a systems problem, not a model problem

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/real-time-translation-is-infrastructure

In short: At Conf42 Platform Engineering 2025, Amit Arora showed that sub-200 ms speech translation rests on modular pipelines, edge nodes and GPU scheduling.

A translation model that scores well on a benchmark is the easy part. At Conf42 Platform Engineering 2025, Amit Arora, a software engineering manager with more than 20 years in the trade, argued that the hard part is the platform around the model: hitting a response time under 200 milliseconds for millions of daily conversations in 40-plus languages, without the meaning falling out somewhere between Mumbai and a data centre in Virginia.

His framing is useful for anyone running AI in production, not just translation teams. Four requirements pull against each other: latency, scale, reliability and accuracy. Optimise one in isolation and you break another. The talk is about getting all four to hold at once.

## Five services, each doing one job

The pipeline Amit describes is a chain of separate microservices: automatic speech recognition turns audio into text, a pre-processing step normalises it, neural machine translation converts it, post-processing cleans it up, and text-to-speech produces the audio on the other side. Keeping these apart is the whole point. Each stage can be scaled, upgraded and monitored on its own, so a better speech recogniser does not require redeploying the translator.

The models ship as containers on Kubernetes, which gives version control and lets domain-specific models (medical vocabulary, say) run next to general-purpose ones. New models go out with blue-green and canary releases: a small slice of users first, a check on how it performs, then everyone. For a system where a mistranslation can land in a hospital, an instant rollback is a feature, not an afterthought.

## The speed of light is a product requirement

The section worth the price of admission is on edge computing. If a user in India or Africa needs a sub-200 ms round trip and every request travels to a US region, the budget is gone before the model even runs. Amit's answer is to push the ASR, MT and TTS components out to edge nodes close to users. In his numbers that cut latency by 40% and upstream bandwidth by almost 60%, and it keeps sensitive audio inside the local jurisdiction, which makes the compliance team happier than any slide deck could.

Under that sits the plumbing: Kafka and Flink for low-latency streaming ingestion, batch pipelines for retraining and analytics, careful GPU scheduling so models do not collide at peak load, and aggressive caching of common phrases, domain terms and user dictionaries. GPUs are the bottleneck, so when they run short the platform degrades gracefully to simpler models instead of falling over.

## Telemetry as the nervous system

Amit treats observability as the core of the platform: latency, throughput, accuracy and error rates per stage, distributed tracing to find which microservice is slow, and user corrections fed back into the models. Fault tolerance is designed in from day one, with redundancy across regions, self-healing restarts and load balancing. His point is that resilience is never an accident; it has to be engineered in at the start.

## Where it matters

The case studies are the reason the talk sticks. A hospital system put domain-specific medical translation models on edge nodes inside its hospitals and saw a 35% reduction in critical medical communication errors. Online classrooms added live captioning and translation to video calls. Enterprises embedded translation into Teams and Slack for international meetings. He closes on what comes next: personalised and context-aware translation models, federated learning at the edge, multimodal input, and lower energy use for GPU-heavy workloads.

## Who should watch

Platform and SRE engineers who have been handed an "AI feature" with a hard latency budget, and ML engineers who want a checklist of everything their model will depend on in production. It is an architecture overview rather than a code walkthrough, so expect diagrams and principles, not Helm charts.

## Related Conf42 talks

- [Pratim Bhosale on reinventing speech-to-text with Go and Whisper](https://www.conf42.com/Golang_2023_Pratim_Bhosale_speechtotext_transcriptions_whisper), the ASR end of the same pipeline.
- [Sai Prasad Mukala on GPU-accelerated AI at the edge](https://www.conf42.com/Machine_Learning_2025_Sai_Prasad_Mukala_intelligence_edge_gpu), for the hardware side of pushing inference close to users.
- [Hubert Dulay on the streaming plane](https://www.conf42.com/Platform_Engineering_2024_Hubert_Dulay_streaming_plane), if the Kafka and Flink layer is where your platform lives.

[Watch Amit Arora's talk](https://www.conf42.com/Platform_Engineering_2025_Amit_Arora_translation_communication_global)

[Watch the talk on YouTube](https://youtu.be/6nC8EJnncRs).

## Watch the talk

[Engineering Real-Time Translation Platforms: Building Scalable AI Infrastructure for Global Communication](https://www.conf42.com/Platform_Engineering_2025_Amit_Arora_translation_communication_global) at Conf42 Platform Engineering 2025.
