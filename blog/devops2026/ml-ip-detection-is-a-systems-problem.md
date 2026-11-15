# An accurate model you cannot roll back is still a failure

Conf42 Blog, 2026-01-12, updated 2026-11-09. https://www.conf42.com/blog/devops2026/ml-ip-detection-is-a-systems-problem

In short: Kanika Gupta of Amazon at Conf42 DevOps 2026 on ML-driven IP violation detection at marketplace scale, and the CI/CD, rollback and observability that make it safe.

"Production ML is a systems problem, not a modeling problem." That is the thesis Kanika Gupta, a software development engineer at Amazon, built her Conf42 DevOps 2026 talk around, using the system that detects intellectual property violations across millions of new marketplace listings a day. Her sharpest version of it: even a 99.9% accurate model is a failure if you cannot roll it back instantly when it meets a new kind of case.

## Why rules and reviewers cannot keep up

The decisions are high stakes in both directions: a false positive hurts a legitimate seller, a false negative lets a bad actor through, and both sit inside legal and regulatory requirements. Kanika lists five ways traditional approaches fail. Manual review cannot scale to the volume. Rule-based systems are brittle, and adversaries pivot as soon as they spot a static rule. Teams that only chase F1 scores ignore deployment and incident response. Static models decay as behaviour shifts. Siloed ML and infrastructure teams create blind spots and slow escalations.

## Many signals, swappable independently

The detection side is multimodal by design, because it is much harder to hide when text, image and behaviour are checked together. Images go through a fine-tuned YOLOv7 model for object detection, text through domain-adapted BERT models for semantic context rather than keyword matching, and behavioural signals such as seller history and past enforcement actions round it out, combined in a weighted ensemble.

The DevOps payoff of that split: the image model can be upgraded without touching the text model, which lowers regression risk and speeds up releases.

Matching relies on embeddings. Images and text become dense vectors, compared against a precomputed index of known violations with approximate nearest neighbour search on AWS OpenSearch, trading a sliver of recall for sub-second p99 latency. Every index is immutable and versioned, so a bad index deploy is an instant rollback.

## Built for failure from the queue up

Orchestration is event-driven: Amazon Kinesis for ingestion, SNS and SQS to route listings by model confidence, AWS Step Functions for workflows with built-in retries. Every component has circuit breakers and back pressure, and event streams are immutable so a decision can be replayed exactly to see why it was made.

Confidence maps directly to policy. High confidence, which requires more than 99% precision, can remove a listing or suspend an account. Medium confidence leads to a warning, education or removal depending on history. Low to medium goes to manual review. The thresholds live in app config, so legal and trust teams can change them without a retrain or a redeploy, a small design choice with large organisational value.

## An LLM for the grey zone

For medium-confidence cases, an LLM acts as a reasoning step that pulls together similarity scores, seller history and metadata into a structured decision with a rationale. Kanika reports a 78% auto-verification rate for those cases and a 68% cut in manual review workload. Because each decision comes with an explanation, sellers get defensible reasons, and she says appeal outcomes improved as a result.

## Models ship like software

Models are versioned artefacts in a registry with lineage and approvals. Each candidate is evaluated against holdout sets, then runs in shadow mode on production traffic without enforcing, compared with the live model, then rolled out gradually behind automated quality gates that trigger auto-rollback on degradation. Knowing the system protects itself is what she credits for doubling release velocity.

Monitoring covers business metrics (false positive and negative rates), system metrics (latency, throughput, errors) and model metrics such as feature drift. The early-warning signal is the distribution of confidence scores: a shift in it flags decay or an adversarial pivot, often within hours, before accuracy visibly drops. Trace IDs, event replay, structured logs and dead letter queues for bad data turn debugging, as she puts it, from an art into a repeatable science.

## Who should watch

ML engineers who have shipped a model and then had to own it, and platform teams supporting them. It is an architecture talk from inside Amazon, so expect AWS services throughout; the patterns (shadow mode, immutable indexes, confidence-tiered actions, config-driven thresholds) port anywhere.

## Related Conf42 talks

- [Green Evals, Broken Agents: Making Evals a First-Class Deployment Artifact](https://www.conf42.com/MLOps_2026_Dylan_Ler_evals_agents_deployment) by Dylan Ler applies the models-as-artefacts idea to agent evaluation.
- [Vector Databases 101 - How do they work?](https://www.conf42.com/Machine_Learning_2024_Stephen_Batifol_vector_databases_work) by Stephen Batifol explains the similarity search under the matching layer.
- [Advancing Financial Fraud Detection with Graph Databases: Innovations and Applications](https://www.conf42.com/Machine_Learning_2025_Venkateswarlu_Boggavarapu_fraud_detection_db_graph) by Venkateswarlu Boggavarapu tackles another adversarial detection problem.

[Watch Kanika Gupta's talk](https://www.conf42.com/DevOps_2026_Kanika_Gupta_intellectual_enforcement_pipelines)

[Watch the talk on YouTube](https://youtu.be/gWj0nun7lXw).

## Watch the talk

[ML-Driven IP Detection at Scale: CI/CD Meets Cloud-Native Enforcement](https://www.conf42.com/DevOps_2026_Kanika_Gupta_intellectual_enforcement_pipelines) at Conf42 DevOps 2026.
