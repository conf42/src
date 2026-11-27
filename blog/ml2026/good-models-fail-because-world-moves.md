# Good models fail after deployment because the world keeps moving

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/good-models-fail-because-world-moves

In short: Oleksandr Pyvovar (Meta) at Conf42 Machine Learning 2026 maps five production failure modes, from data drift to feedback loops, with a fix for each.

A model that scores well in the lab can be close to a coin flip six months later, and nothing in the code changed. At Conf42 Machine Learning 2026, Oleksandr Pyvovar, a machine learning engineer at Meta, catalogued why that happens, how to detect each cause and what to do about it, all in one tidy taxonomy.

The abstract puts the thesis well: great models "don't usually fail because they're wrong" but because the world changes after they ship. The talk then earns that line with detection methods you can actually implement.

## Five ways production quietly breaks a model

Pyvovar walks through data drift, concept drift, label drift, feature pipeline degradation with training-serving skew, and feedback loops with bias amplification. Each gets an analogy, a real incident and a detect-then-resolve pair.

Data drift is the self-driving car trained on sunny days and deployed in fog; his real-world example is Zillow Offers and its pricing model failing to adapt to post-pandemic market volatility. Concept drift keeps the inputs but changes their meaning, which is the daily life of fraud models whose adversaries simply move to a VPN or shift their attack hours. Label drift is the add-to-cart model calibrated on a normal week meeting Black Friday, or a loan-default model trained in a calm economy meeting a recession.

## Every failure mode gets its own detector

What makes the talk useful is that the detectors differ per failure mode. For input drift he covers Population Stability Index for tracking key features over time, the Kolmogorov-Smirnov test for numerical features and Jensen-Shannon for categorical ones. Concept drift needs performance monitoring against labels, adaptive sliding windows that grow or shrink as the data shifts, or error-rate thresholds. Label drift is caught by watching the class distribution, a chi-square test, or simply the share of positive predictions.

The fixes are equally specific: Platt scaling or isotonic regression to recalibrate after label drift, class weighting and cost-sensitive learning, online learning or windowed ensembles for concept drift, and domain adaptation when relabelling is not an option.

## Your pipeline is part of the model

The feature pipeline section is the one platform teams should bookmark. His example is Google's diabetic retinopathy model, which matched specialists on clean lab images and then struggled in clinics in Thailand where photos were taken in poor light. Same model, worse ingredients.

The prescriptions are the ones you know you should already have: Great Expectations or Deequ for data validation, schema monitoring, logging inputs and outputs in both training and serving to catch skew, data contracts between teams, containers for environment parity, and a feature store as the industry standard that removes a whole class of skew bugs.

Feedback loops get the heaviest example, the COMPAS recidivism tool, and three countermeasures: deliberate exploration (a random slot or two in a recommendation batch), positional debiasing, and fairness constraints at training time.

## Retrain on signals, not on the calendar

On retraining, he compares time-based schedules (simple but wasteful), performance triggers (precise but reactive, since the losses already happened), drift triggers (proactive but noisy) and a hybrid policy, which he recommends while admitting it needs a lot of threshold tuning. Monitoring is split into model performance, data health and system health, with open-source options like Evidently AI, NannyML and Alibi Detect alongside commercial platforms.

The closing practices are the kind you tape to a monitor: design for drift from day one, keep training-serving parity, roll out gradually starting with a small slice of traffic, instrument for ground truth, document everything, and treat ML as a product rather than a project.

## Who should watch

ML engineers shipping their first or fifth model, and SREs who inherited a model and want a mental checklist for the week a model got worse while nobody deployed anything. Seasoned MLOps folks will know most of the tools, but the per-failure-mode mapping of detector to fix is a handy reference.

## Related Conf42 talks

- [When Ground Truth Arrives Late: Building Reliable AI Systems in Production](https://www.conf42.com/MLOps_2026_Avneesh_Sharma_reliable_ai_production) by Avneesh Sharma (Amazon) picks up exactly where label feedback gets slow.
- [AI Model Monitoring: Building Reliable Alert Systems](https://www.conf42.com/Chaos_Engineering_2025_Muddassar_Sharif_ai_model_systems) by Muddassar Sharif (Virtuans.ai) turns detection into alerting.
- [Data Quality and Validation in ML Pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation) by Sunil Kumar Mudusu (Church Mutual Insurance Company) expands the pipeline-validation half.

[Watch Oleksandr Pyvovar's talk](https://www.conf42.com/Machine_Learning_2026_Oleksandr_Pyvovar_robustness_reliability_models)

[Watch the talk on YouTube](https://youtu.be/uKpS8xTtEoU).

## Watch the talk

[Why Good Models Fail After Deployment](https://www.conf42.com/Machine_Learning_2026_Oleksandr_Pyvovar_robustness_reliability_models) at Conf42 Machine Learning 2026.
