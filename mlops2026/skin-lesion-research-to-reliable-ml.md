# An AUC of 0.99 is where reliable medical ML starts, not where it ends

Conf42 Blog, 2026-11-10. https://www.conf42.com/mlops2026/skin-lesion-research-to-reliable-ml

In short: Deborah Adedigba (UK Ministry of Defence) at Conf42 MLOps 2026 uses her skin lesion classifier to show what a research pipeline needs to be trusted.

A strong metric on one dataset is a promising experiment, and nothing more. At Conf42 MLOps 2026 on November 19, Deborah Adedigba, Data Scientist at the UK Ministry of Defence, uses her own research on deep learning for skin lesion classification as a case study in what it takes to move from a good result to a reliable ML system.

The result in question is a good one. Her pipeline combines U-Net segmentation with CNN classifiers, including ResNet50, VGG16 and EfficientNetB4, and reached a reported AUC of 0.99 on the PH² dataset. The talk is about everything that number does not tell you.

## Why healthcare raises the bar

In medical imaging, model predictions could eventually inform clinical decisions. That changes what "done" means. Reproducibility, data quality, evaluation methodology and deployment readiness stop being nice extras and become as important as the architecture.

Deborah's framing is useful because it comes from the research side. Plenty of MLOps talks start from a production platform and work backwards. This one starts from a thesis-shaped pipeline and asks, honestly, what would be needed to trust it outside the lab.

## Two stages, one source of inconsistency

The workflow has two stages: segment the lesion, then classify it. Each stage has its own preprocessing, and each choice has to be applied identically during training, evaluation and any future inference. Deborah covers the challenges of structuring image-processing and classification workflows, and of keeping preprocessing and evaluation consistent across them.

If you have ever had a model degrade because inference resized images slightly differently from training, you already know why this section exists.

## Reading the metric, and its limits

A good part of the talk is about interpretation: what the performance metrics actually say, and the limitations of results obtained from a single dataset. An AUC of 0.99 on one evaluated dataset is a statement about that dataset. Whether it carries over to different cameras, clinics, skin tones or patient populations is a separate question that only independent validation can answer.

It is refreshing to see a speaker present a headline number and then spend time on why it should be handled with care.

## The path from experiment to system

The last section maps the gap between an experimental research pipeline and something more reproducible, monitored and deployment-ready. The list is the MLOps canon, applied to a concrete case:

- versioned data and models
- automated testing
- experiment tracking
- independent validation
- monitoring and maintenance once deployed

The point Deborah lands on is that reliable machine learning requires more than picking an architecture and hitting a strong metric. It takes a systematic approach to the whole lifecycle, from data preparation through to maintenance.

## Who should watch

Researchers and students with a promising model who want to know what production-grade would demand of it. Data scientists in healthcare or other high-stakes fields. MLOps engineers looking for a clean, real case study to explain to colleagues why "the model scores 0.99" is the start of the conversation. If you already run regulated medical ML in production, much of this will be familiar ground.

## Related Conf42 talks

- [DevOps Pipelines for Clinical AI: Deploying Real-Time Sepsis Detection at Scale](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai) by Swapna Chimanchodkar, clinical AI on the deployment side.
- [Building Resilient AI Platforms at Scale: Engineering Infrastructure for Real-Time Computer Vision Deployments](https://www.conf42.com/Platform_Engineering_2025_Manoj_Sai_Jayakannan_vision_computer_deployments) by Manoj Sai Jayakannan, the platform under computer vision models.

[Watch Deborah Adedigba's talk](https://www.conf42.com/MLOps_2026_Deborah_Adedigba_skin_lesion_classification) at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) on November 19.

## Watch the talk

[Research to Reliable ML: Lessons from a Deep Learning Pipeline for Skin Lesion Classification](https://www.conf42.com/MLOps_2026_Deborah_Adedigba_skin_lesion_classification) at Conf42 MLOps 2026.
