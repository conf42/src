# Predict NPS from telemetry instead of waiting for surveys

Conf42 Blog, 2026-01-31, updated 2026-11-09. https://www.conf42.com/blog/ml2026/predict-nps-without-sending-a-survey

In short: Abhinay Kumar Reddy Seella of Roku at Conf42 Machine Learning 2026 on a multi-modal model that predicts Net Promoter Score per session in real time.

Net Promoter Score has a sampling problem: fewer than 5% of users answer the survey, the ones who do are the delighted and the furious, and the result lands weeks after the session that caused it. At Conf42 Machine Learning 2026, Abhinay Kumar Reddy Seella, Senior Software Engineer at Roku, presented Dynamic NPS (DNPS), a model that predicts a user's NPS category for every session from behaviour, telemetry and text, with no survey at all.

## Surveys measure the loud minority, late

Abhinay opened with the standard arithmetic (promoters 9-10, passives 7-8, detractors 0-6, NPS is promoters minus detractors) and then the four ways collection breaks: the participation gap, the speed barrier, response bias towards the extremes, and the fact that by the time a team reads the score, the chance to fix the experience is gone.

His question is simple: what if the score could be computed from what users do, while they are still doing it?

## Three models, each reading a different signal

DNPS ingests three kinds of data. Behavioural interaction data covers click patterns, navigation flows, session duration, drop-offs and error events. Telemetry covers backend event logs, performance metrics and device metadata. Text covers in-app comments, support messages and chat transcripts. A processing layer cleans, normalises and, critically, aligns timestamps so events from different sources are ordered correctly.

The modelling is a hybrid:

- Gradient-boosted trees (XGBoost or LightGBM) on structured behavioural and telemetry features.
- A sequence model (LSTM or transformer) for how behaviour changes across a session.
- A text model built on embeddings for sentiment and topic.

A fusion layer learns how much to weight each model rather than averaging them, then produces the final score.

## The numbers, and what removing a signal costs

Abhinay reported about 85.9% accuracy, a mean absolute error around 1.21, strong F1 across all three categories, and inference at roughly 80 milliseconds, quick enough for live dashboards. The ablation is the most useful slide: dropping text pulls accuracy down to about 55%, while dropping behavioural and telemetry data lands near 78%. If you were planning to skip the messy text pipeline, that result argues otherwise.

## Explanations that point at the UI

SHAP and LIME sit on top so each prediction comes with the features that drove it. The findings are the kind a product team can act on: frequent back clicks track with negative sentiment, short sessions often signal dissatisfaction, and deliberate clicking tends to go with promoters. That turns a score into a pointer at friction, such as UI confusion or buffering.

He was candid about limits: the approach needs large, high-quality datasets, struggles with cold-start users, adds operational complexity, and text signals can carry bias.

## Who should watch

Data scientists and product engineers who own customer-experience metrics and are tired of quarterly survey decks. The talk is architecture and results, not code, so bring your own pipeline ideas.

## Related Conf42 talks

- [Building Intelligent Retention Engines: Real-Time Churn Detection with AI on Kubernetes](https://www.conf42.com/Kube_Native_2025_Gaurav_Sunkar_retention_churn_ai) by Gaurav Sunkar, the churn side of the same early-warning idea.
- [AI-Driven Customer Experience: How to Start, Scale, and Succeed in the Enterprise](https://www.conf42.com/DevSecOps_2025_Rajanikant_Vellaturi_start_scale_succeed) by Rajanikant Vellaturi.
- [Architecting Real-Time Analytics: Building Scalable Data Pipelines for Customer Experience Excellence](https://www.conf42.com/DevOps_2025_Amarnath_Immadisetty_analytics_data_customer) by Amarnath Immadisetty, for the pipeline underneath.

[Watch Abhinay Kumar Reddy Seella's talk](https://www.conf42.com/Machine_Learning_2026_Abhinay_Kumar_Reddy_Seella_satisfaction_prediction_telemetry) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/n5fPEQpgYLw).

## Watch the talk

[Beyond Surveys: Real-Time User Satisfaction Prediction with LLMs and Telemetry](https://www.conf42.com/Machine_Learning_2026_Abhinay_Kumar_Reddy_Seella_satisfaction_prediction_telemetry) at Conf42 Machine Learning 2026.
