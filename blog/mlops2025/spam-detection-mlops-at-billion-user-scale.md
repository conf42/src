# Spam detection at billion-user scale is an ensemble and a graph

Conf42 Blog, 2025-08-24, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/spam-detection-mlops-at-billion-user-scale

In short: Prabhakar Singh (Meta) at Conf42 MLOps 2025 on production MLOps for multi-modal spam detection, from smart sampling to graph-based campaign detection.

At billion-user scale, a 0.1% false positive rate sounds tiny until you realise it means millions of legitimate people waking up to find their posts blocked. Prabhakar Singh, a software engineer at Meta, uses that arithmetic to open his Conf42 MLOps 2025 talk on production spam detection, and then lays out the blueprint: a hierarchical ensemble across text, images, video and behaviour, smart sampling to keep labelling affordable, and graph analysis to catch coordinated campaigns.

He describes the patterns of large-scale systems in general rather than disclosing internal Meta specifics, which keeps it portable to smaller platforms.

## The constraints are brutal

Billions of pieces of content, millions of evaluations per second at peak, and user-facing decisions that must return in under 100 ms. Spam here means fraud, phishing, scams and harmful content, across hundreds of languages, under GDPR and CCPA, against attackers who change tactics daily. His line for it is playing chess with millions of opponents who all change strategy overnight.

## Cheap filters first, specialists second

The model architecture is a hierarchical ensemble. Fast, lightweight pre-filters process the bulk of the volume and are tuned for high recall. Suspicious items go to specialist models for text, images, video and behaviour. A multimodal fusion stage combines signals with cross-attention, catching cases where the text looks fine but the image makes it obviously spam. A meta-learner weighs everything by historical reliability. His analogy is airport security: a quick scan for every bag, a closer look for the suspicious ones.

The features are where the signal lives: transformer embeddings and entity recognition for text, CNNs and OCR for images and memes, and behavioural and contextual signals like posting frequency, device fingerprints and account age. A post at 2 a.m. from a new device linked to a trending spam topic reads very differently from the same post on an old account.

## Label the samples that teach the model something

Labelling billions of samples is impossible, so the question is which ones matter. Prabhakar lists uncertainty sampling (send low-confidence cases to humans), diversity sampling (do not miss underrepresented languages and formats), adversarial sampling (seek out where the model fails), and time-sensitive sampling for new attack vectors. When attackers started hiding spam in memes, adversarial sampling surfaced it early enough to retrain.

## A campaign only shows up as a graph

Coordinated attacks are the interesting part. A single post looks normal; thousands of accounts acting together do not. Real-time streaming analysis spots activity anomalies, and graph neural networks model user-content interactions as dynamic graphs to expose suspicious clusters. His example is 10,000 accounts piling onto one post in under a minute: invisible individually, obvious as a graph. Countermeasures include throttling, CAPTCHAs and flagging clusters for review.

## Privacy and shipping discipline

Privacy is built in through federated learning, differential privacy, and cryptographic techniques such as homomorphic encryption, multi-party computation and zero-knowledge proofs. Models retrain daily, are validated against golden datasets, fairness slices and adversarial examples, run in shadow mode before progressive rollout, and can roll back instantly. Monitoring covers model performance, system performance, data drift and business impact, including false-positive appeals, with structured incident playbooks and post-mortems.

## Who should watch

Trust and safety engineers, anyone running abuse detection on a marketplace or social product, and ML engineers interested in cascaded inference under tight latency budgets. It is a dense overview; take notes on the sampling section.

## Related Conf42 talks

- [Ajay Krishnan Prabhakaran (Meta) on SMS spam detection with Python](https://www.conf42.com/Python_2025_Ajay_Krishnan_Prabhakaran_sms_spam_python), a hands-on starting point.
- [Georgina Tryfou (Gcore) on scalable AI moderation of harmful content](https://www.conf42.com/Machine_Learning_2025_Georgina_Tryfou_moderation_scalable_safety) at Conf42 Machine Learning 2025.
- [Andrei Shcherbinin (Social Discovery Group) on an ML auto-moderation system for LLM-augmented platforms](https://www.conf42.com/Large_Language_Models_LLMs_2026_Andrei_Shcherbinin_moderation_safety_platforms) at Conf42 LLMs 2026.

[Watch Prabhakar Singh's talk](https://www.conf42.com/MLOps_2025_Prabhakar_Singh_production_mlops_spam) for the full architecture.

[Watch the talk on YouTube](https://youtu.be/MZdSi1Fe1_8).

## Watch the talk

[Production MLOps for Spam Detection: Real-Time Multi-Modal AI at Billion-User Scale](https://www.conf42.com/MLOps_2025_Prabhakar_Singh_production_mlops_spam) at Conf42 MLOps 2025.
