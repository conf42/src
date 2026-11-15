# Why delivery pricing needs switchback tests instead of A/B tests

Conf42 Blog, 2026-01-28, updated 2026-11-09. https://www.conf42.com/blog/ml2026/switchback-testing-delivery-pricing-experiments

In short: Rothesay quant Sergei Nasibian at Conf42 Machine Learning 2026 on switchback testing and change-point analysis for system-level pricing experiments.

Raise the delivery fee for half your users and the other half get a better service, because the couriers you freed up are now waiting for them. At [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026), Sergei Nasibian, a quantitative strategist at Rothesay, used food delivery pricing to show why user-level A/B tests break in marketplaces, and how switchback testing plus change-point analysis measures what a price change actually does.

The examples are FoodTech, but the method applies anywhere users share a constrained resource: ride-hailing, logistics, ad auctions, cloud capacity.

## The pricing problem in one curve

Nasibian keeps the scope tight: short-term revenue optimisation, not lifetime value, which he treats as a separate and harder strategic problem. Charge too much for delivery and revenue per order rises while orders fall; charge too little and the opposite. Somewhere in between sits a sweet spot. The quantity you need is demand elasticity: how conversion from a session to an order changes with the delivery fee. The relationship is monotonically decreasing, and for small changes a linear approximation, a single first-derivative number, is good enough.

## Why A/B tests lie here

A/B testing splits users randomly and assumes they are independent. In a three-sided marketplace of users, restaurants and couriers, they are not. Supply is often the bottleneck. Increase prices for the test group, they order less, courier capacity frees up, and the control group gets faster deliveries, possibly cheaper ones too if your pricing algorithm accounts for courier distance. The experiment ends up measuring the price change plus a side effect you didn't intend.

## Switch time, not users

A switchback experiment randomises over time instead. All orders in a time window get the same pricing algorithm, and the system alternates. His example splits a 48-hour experiment into 12 four-hour blocks. The design question is window size: too short and the system has no time to react, so results are noise; too long and local seasonality, such as lunch peaks, gets mistaken for the effect. Two practical fixes he describes: flip the mode at night when volume is low, so each time of day sees both algorithms across days, and run for at least two weeks so every weekday appears under both modes.

## Evaluate it as a change-point problem

A/B results are a classic hypothesis test: two-sample t-test, Welch's test when variances differ, permutation tests, applied to order size, revenue per order or conversion. Switchback results are better treated as change-point detection in a time series, which also catches shifts in variance and frequency, not just in averages.

His recipe:

1. Keep a sliding window of observations and compute its mean: a simple moving average, an EWMA, or a GARCH-based estimate.
2. Pick a recent stable period with no interventions, split it into equal windows, compute each window's mean the same way, and take pairwise absolute differences between windows. That gives the empirical distribution of differences when nothing changed.
3. Use a high quantile of that distribution, typically 0.95, as the threshold for declaring a change point.
4. Validate detected change points against the known flip schedule; the size of the jump above the threshold is your impact estimate.

The same monitor can watch several order metrics at once, so you also see any unintended negative effect of the experiment.

## Who should watch

Data scientists and engineers running experiments on marketplaces or any shared-capacity system, and anyone whose A/B results look too good when supply is tight. It's statistics-forward and concise, and the threshold recipe is directly reusable.

## Related Conf42 talks

- [A/B testing platform at scale](https://www.conf42.com/Chaos_Engineering_2023_Riteek_Srivastava_ab_testing_platform_at_scale), Riteek Srivastava (Gojek), Conf42 Chaos Engineering 2023
- [AI-driven task pricing: reducing costs in micromobility operations](https://www.conf42.com/Large_Language_Models_LLMs_2025_Kaan_Tas_task_pricing_costs), Kaan Tas (Lime), Conf42 LLMs 2025
- [Building resilient AI pricing platforms: real-time decision systems at scale](https://www.conf42.com/Platform_Engineering_2025_Amaresh_Sahoo_pricing_decision_time), Amaresh Sahoo (Xometry), Conf42 Platform Engineering 2025

[Watch Sergei Nasibian's talk](https://www.conf42.com/Machine_Learning_2026_Sergei_Nasibian_knowledge_graphs_reasoning)

[Watch the talk on YouTube](https://youtu.be/iDFQ9bEu9Yo).

## Watch the talk

[System-Level Experimentation at Scale: Pricing, Supply, A/B and Switchback Testing in FoodTech](https://www.conf42.com/Machine_Learning_2026_Sergei_Nasibian_knowledge_graphs_reasoning) at Conf42 Machine Learning 2026.
