# AI projects stall in pilots when the infrastructure comes last

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/ai-native-platforms-start-with-infrastructure

In short: Bharath Reddy Baddam of New York Life gives Conf42 Platform Engineering 2025 a map of AI-native platforms, from GPUs and feature stores to observability.

Plenty of companies have an AI pilot. Far fewer have an AI product, and the gap between them is usually infrastructure nobody budgeted for. At Conf42 Platform Engineering 2025, Bharath Reddy Baddam, Senior Salesforce Developer at New York Life Insurance Company, lays out what an AI-native platform needs underneath it, from GPU scheduling to model observability, and why treating infrastructure as an afterthought keeps models stuck in experiments.

This is an orientation talk, a structured tour rather than a war story. If you are the platform engineer who just got told the company is doing AI now, it is a tidy checklist of the layers you will be asked to own.

## Training and inference are different animals

Baddam's first point is the one teams most often get wrong: training and inference have opposite shapes. Training is massively parallel and GPU-hungry. Inference, for recommendation engines, chatbots or fraud detection, is about millisecond responses and scaling out. Build one environment for both and you get the classic trio he names: over-provisioning, under-utilisation and costs that spiral.

The scheduling consequence is mixing CPUs and GPUs on purpose. Lightweight preprocessing runs on CPUs, heavy training goes to GPUs, and a scheduler that knows the difference saves real money. For scaling training itself he points to Kubernetes and container orchestration, distributed data parallelism across GPUs, network topology that can carry the traffic, and fault tolerance so one failed node does not kill a multi-day run.

## Data pipelines decide whether the model is any good

The data section leans on two components. Feature stores let teams reuse features across models and keep training and serving consistent. Stream processing adds real-time signals alongside batch pipelines over historical data. His fraud example makes the latency point well: if the pipeline lags by even a few cycles, the window to stop the fraudulent transaction has already closed.

## Observe three layers, not one

AI platforms need monitoring at the infrastructure level (GPU utilisation), the data level (pipeline health) and the model level, which he calls the most important: accuracy, precision, recall and fairness indicators, tracked continuously so drift, bias and degradation show up before they become an incident. Performance tuning gets practical notes too: managing GPU memory, NVMe storage, batching inference requests and caching frequently accessed features.

## No single blueprint

The implementation-patterns slide is a useful reality check. High-frequency trading needs ultra-low latency and real-time pipelines; content recommendation needs per-user personalisation at scale; healthcare puts compliance, accuracy and ethical safeguards first. One architecture will not fit all three, so the platform has to follow business goals rather than a reference diagram.

Governance closes the technical part: defending models against adversarial attacks, data privacy, role-based access, and explainability that holds up under regulations such as GDPR and HIPAA. The roadmap is phased: short-term wins like feature stores, observability in the medium term, and longer-term bets such as edge AI.

## Who should watch

Platform engineers and architects about to inherit ML workloads, and engineering managers who need a shared vocabulary with their data science teams. Seasoned MLOps practitioners will find it familiar ground; the training-versus-inference framing is still a good one to borrow when arguing for separate clusters.

## Related Conf42 talks

- [The machine learning pipeline is a myth](https://www.conf42.com/Python_2023_Jim_Dowling_pipeline_myth_production_ml_systems_feature_training_inference_pipelines) by Jim Dowling, Conf42 Python 2023, on feature, training and inference pipelines
- [E2E ML Platform on Kubernetes with just a few clicks](https://www.conf42.com/Machine_Learning_2021_Mofizur_Rahman_E2E_ML_Platform_Kubernetes) by Mofizur Rahman, Conf42 Machine Learning 2021
- [A Hitchhiker's Guide to the MLOps Experience](https://www.conf42.com/Machine_Learning_2023_Noa_Goldman_hitchhiker_guide_mlops_experience) by Noa Goldman, Conf42 Machine Learning 2023

[Watch Bharath Reddy Baddam's talk](https://www.conf42.com/Platform_Engineering_2025_Bharath_Reddy_Baddam_applications_architecting_modern)

[Watch the talk on YouTube](https://youtu.be/Duev48SQ9fQ).

## Watch the talk

[Architecting AI-Native Platforms: Engineering Scalable ML Infrastructure for Modern Applications](https://www.conf42.com/Platform_Engineering_2025_Bharath_Reddy_Baddam_applications_architecting_modern) at Conf42 Platform Engineering 2025.
