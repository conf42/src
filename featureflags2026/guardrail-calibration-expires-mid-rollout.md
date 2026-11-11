# Your rollout guardrail can look healthy after its calibration expired

Conf42 Blog, 2026-10-13, updated 2026-11-09. https://www.conf42.com/featureflags2026/guardrail-calibration-expires-mid-rollout

In short: Rakshay Pawar of Codeflow Capital at Conf42 Feature Flags 2026 uses a 35-year Treasury yield backtest to show why clustered misses break rollout guardrails.

Two guardrails can both miss 10% of the time, and one of them is fine while the other fails ten times in a row exactly when the rollout reaches a new cohort. At Conf42 Feature Flags 2026, Rakshay Pawar, a quantitative finance senior associate at Codeflow Capital, used a backtest on U.S. Treasury yields to show why average coverage hides failures that cluster in time, then proposed how rollout guardrails should carry their scope and calibration history with them.

He's careful about what's evidence and what's proposal throughout: the Treasury results are an empirical financial backtest; the feature-flag framework is an application of those lessons that would need its own validation on deployment data. That honesty is part of why the talk is worth your time.

## The threshold stayed, the population moved

A guardrail is usually calibrated for the rollout's first shape: internal users, one region, low-volume customers, a device type. Then targeting expands, and the dashboard line stays exactly where it was while the people behind the metric change. Rakshay names three ways this drifts. Exposure is dynamic, so a targeting change shifts the user mix even when the code didn't change. Later cohorts may have different baselines, like a region with different network conditions. And the original calibration goes stale. A targeting change doesn't always mean a meaningful distribution shift, he notes; it means you need to check.

## Same average, different danger

His illustration: 100 observations, 10 misses each. In one row the misses are spread out and probably noise. In the other they come back to back, which suggests the environment changed and the guardrail is failing precisely when risk is highest. Both report a 10% miss rate. So watch the sequence of failures and the length of miss streaks, not just the percentage.

## What 6,502 forecasts showed

The study uses daily Treasury par yields across six maturities from 1990 to 2025, with 6,502 walk-forward forecasts and a 99% coverage target (a 1% target miss rate). Four methods compete: a Gaussian full-curve benchmark, rolling conformal and adaptive conformal full-curve calibration, and an adaptive fixed-family method that covers five declared portfolios instead of every possible exposure.

The Gaussian method missed 141 times, a 2.169% miss rate, and the conditional coverage test rejects it strongly. Rolling and adaptive conformal each hit exactly 1.000% on average, which looks ideal, but their misses cluster, with a conditional coverage p-value of 0.0166. The fixed-family method missed 64 times (0.984%) with no evidence against conditional coverage over the full sample, and its region was much tighter: the full-curve radius was 57.1% larger, which he calls a universality premium.

Then the regime table spoils the easy conclusion. In 2020-2021 the fixed-family method's miss rate reached 2.191%, more than twice target, while the full-curve adaptive method sat at 1.195%. The narrow guardrail is tighter and more reliable inside its declared scope, and breaks its guarantee when something genuinely new shows up. A good overall average can hide a bad period, which anyone who's watched a canary pass at 5% and wobble at 25% will recognise.

## Two layers and a contract

The proposed software translation is a two-layer monitor. A broad layer watches general service health across many rollout configurations and serves as the fallback. A specialised layer holds bounds calibrated for declared cohorts or exposure families, so it can be more specific. Each has its own review trigger: broad thresholds when operating conditions change, specialised ones when a new cohort or exposure type appears.

A guardrail becomes a contract: the population and targeting rule, the metric and statistical target, the calibration window and version, the valid scope, and the response rule. His hypothetical shows why matched controls matter. At 25% rollout, if the flagged and control groups both rise from 1% to 2% errors, that calls for a scope and calibration review, not a verdict on the feature. If control is at 2% and the flagged group at 2.8%, pause and investigate. And when degradation can't be explained, the answer is to investigate and control exposure, not to recalibrate until the warning goes away.

## Who should watch

Experimentation and release-safety engineers who set guardrail thresholds, and anyone who trusts a green indicator after a targeting change. It's statistics-dense, but the five closing questions on scope, change, adaptation, temporal reliability and fallback work without the maths.

## Related Conf42 talks

- [Why Good Models Fail After Deployment](https://www.conf42.com/Machine_Learning_2026_Oleksandr_Pyvovar_robustness_reliability_models) by Oleksandr Pyvovar of Meta at Conf42 Machine Learning 2026.
- [AgentCast: Autonomous AI-Driven Time Series Forecasting for DevOps at Scale](https://www.conf42.com/DevOps_2026_Premanand_Tiwari_forecasting_time_autonomy) by Premanand Tiwari of Amazon at Conf42 DevOps 2026.

[Watch Rakshay Pawar's talk](https://www.conf42.com/Feature_Flags_2026_Rakshay_Pawar_guardrails_rollout_risk) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/0DPV8SENK64).

## Watch the talk

[Guardrails That Outlive the Rollout: Adaptive Statistical Risk Control for Feature Flags](https://www.conf42.com/Feature_Flags_2026_Rakshay_Pawar_guardrails_rollout_risk) at Conf42 Feature Flags 2026.
