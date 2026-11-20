# Stop guessing alert thresholds and derive them with statistics

Conf42 Blog, 2025-08-20, updated 2026-11-09. https://www.conf42.com/blog/platform2025/alert-thresholds-you-can-prove

In short: Emmanuel Bakare of Twilio shows at Conf42 Platform Engineering 2025 how IQR, the law of large numbers and curve fitting turn thresholds into math.

Every on-call engineer has a threshold they did not choose and do not trust: CPU over 80%, error rate over 1%, numbers somebody picked years ago and nobody has dared to move. At Conf42 Platform Engineering 2025, Emmanuel Bakare, Senior DevOps Engineer at Twilio, takes that problem apart with numerical methods: how to derive a static threshold you can defend, and when to switch to dynamic thresholds that follow the system as it grows.

This is the rare platform talk with actual maths in it, delivered in a friendly walk-through style. Bakare also builds CostCraft at Baseline HQ Cloud, which applies similar methods to right-sizing Kubernetes requests and limits; he mentions it, but the talk is about the methods, not the product.

## Static versus dynamic, honestly compared

Bakare starts with definitions. A threshold is an upper or lower bound at time t, and you act when a metric crosses it for long enough. Static thresholds are a fixed line through the noise: easy to set and easy to diagnose, but prone to noise, blind to organic growth, and usually tied to a single variable. Dynamic thresholds move with observations, rely on past and present data in a feedback loop, can combine signals such as CPU and memory, and produce fewer false positives, at the price of needing more data and more understanding of how your system behaves.

## Clean the data before you trust the line

For static thresholds he gives a three-step recipe. First, filter outliers, because a static threshold never adapts, so whatever skew you bake in stays there. The interquartile range method is his suggested starting point: compute Q1 and Q3, then set bounds at Q1 minus 1.5 times the IQR and Q3 plus 1.5 times the IQR. Z-scores and standard deviation are the next step up. Second, pick an aggregate: a percentile or a plain mean. Third, reduce the error.

## The law of large numbers does the arguing for you

That third step is the heart of the talk. Take a percentile over rolling windows (p99 over each five minutes, say) and average across many windows. Outlier windows still happen, but the average converges towards the true value as samples accumulate. Bakare demonstrates it with a cron job that runs health checks three times a minute, enumerates the pass and fail combinations, and simulates one versus ten jobs over many iterations. Comparing p90 with p99.999, the p90 shows far more deviation, which suits a spiky system, while the tight percentile fits strict SLOs. Watching the standard deviation fall as iterations grow tells you the estimate is converging; watching it rise tells you it is not.

The payoff is a threshold you have proven over many iterations rather than guessed. Bring that to the next argument about whether the alert is too sensitive.

## Curve fitting for systems with a rhythm

Dynamic thresholds are anomaly detection under another name. Bakare covers supervised methods (logistic regression, KNN, naive Bayes, support vector machines), unsupervised ones (isolation forests, DBSCAN, PCA) and spends his time on the one he has used most: curve fitting. With simulated hourly sales data that rises and falls in a wave, he fits a sine-style function by iterating over amplitude, phase and constant within sensible bounds, and judges the fit with a chi-squared goodness-of-fit test, which he prefers over standard deviation because it accounts for sample count.

## Who should watch

SREs tuning noisy alerts, platform engineers building autoscaling policies, and anyone who has ever eyeballed a Grafana panel and typed a number into a YAML file. Bakare's own closing advice is fair: sometimes eyeballing is enough, but when systems behave strangely, statistics can save months of headache.

## Related Conf42 talks

- [Techniques for SLOs and Error Budgets at Scale](https://www.conf42.com/Observability_2023_Fred_Moyer_slos_error_budgets_scale) by Fred Moyer, Conf42 Observability 2023
- [Alerting on SLOs and Error Budget Policies](https://www.conf42.com/Site_Reliability_Engineering_2022_Ricardo_Castro_alerting_slos_error_budget_policies) by Ricardo Castro, Conf42 SRE 2022
- [Anomaly Detection with Apache Pinot & ThirdEye](https://www.conf42.com/Cloud_Native_2023_Yoav_Nordmann_anomaly_detection_apache_pinot_thirdeye) by Yoav Nordmann, Conf42 Cloud Native 2023

[Watch Emmanuel Bakare's talk](https://www.conf42.com/Platform_Engineering_2025_Emmanuel_Bakare_math_exploring_thresholds)

[Watch the talk on YouTube](https://youtu.be/SpuPsdponuw).

## Watch the talk

[Exploring the math of thresholds](https://www.conf42.com/Platform_Engineering_2025_Emmanuel_Bakare_math_exploring_thresholds) at Conf42 Platform Engineering 2025.
