# AgentCast lets an agent pick, tune and retrain your forecasting model

Conf42 Blog, 2025-12-23, updated 2026-11-09. https://www.conf42.com/blog/devops2026/agentcast-autonomous-forecasting-capacity-planning

In short: Amazon applied scientist Premanand Tiwari at Conf42 DevOps 2026 on AgentCast, an agent that chooses, tunes and retrains capacity forecasting models.

Capacity planning usually needs a data scientist, a planner and an ops engineer in the same room, and none of them are cheap. At Conf42 DevOps 2026, Premanand Tiwari, an applied scientist at Amazon who builds forecasting models for capacity and inventory planning, presented AgentCast: an agent that looks at your time series, picks the model family, tunes it, deploys it and retrains it when accuracy slips, with no human choosing anything along the way.

It is a design walkthrough of a system he built, not a tutorial. If you want to know what an "autonomous forecaster" has to decide on your behalf, it is a tidy map.

## The model zoo is the point

The core argument is that no single model wins on infrastructure data, so the agent carries a whole toolkit and chooses per dataset. Tiwari lists the shelves: statistical models (ARIMA, auto ARIMA, Holt-Winters) for simple series, gradient boosting such as XGBoost when you have many independent variables and a short or medium horizon, and deep models (Temporal Fusion Transformers, N-BEATS, DeepAR, LSTMs and GRUs) when the horizon is long and the dependencies stretch across months.

The agent trains candidates, runs hyperparameter search itself (he notes it builds the search grid from the data rather than asking you for one), scores them on MAE, MAPE, RMSE, WAPE or a custom metric you supply, and can ensemble two or three models when no single one is best. Anyone who has hand-tuned a Holt-Winters model at midnight will see the appeal.

## Probabilistic forecasts beat a single line

A design choice worth copying even without the agent: AgentCast emits P10, P50, P70 and P90 rather than one point forecast. For capacity, the spread is the useful part. A wide band tells you demand is volatile and you need headroom; a narrow one says you can run closer to the line. The same horizon knob covers sub-minute operational views up to monthly, quarterly and multi-year planning.

## Forecasts as a cheaper autoscaler

The most DevOps-flavoured idea in the talk is a jab at reactive autoscaling. Tiwari's point is that autoscaling works, but the bill at the end of the month can be painful. His alternative is to feed the agent's forecasts into your scaling configuration, so pods, CPUs or GPUs are added ahead of a predicted spike (holiday traffic is his example) instead of after the CPU graph has already gone vertical.

He also describes the operational wrapper you would want around any model in production: daily or weekly retraining, live tracking of error metrics against an acceptable band, automatic re-selection of the model when the data changes shape, versioning with rollback, and A/B testing one deployment against another.

## Honest scope

The abstract promises live demos; the recording is a slide walkthrough of the architecture and the expected workflow (CPU, memory and network traffic forecasts), not a screen-share. There are no accuracy numbers either, so treat it as the shape of a system rather than proof that it beats your current planner. The questions it raises are the good ones: what does the agent do when the data is sparse or intermittent, and who signs off when it swaps the model under you?

## Who should watch

Platform and SRE folks who own capacity planning and keep losing arguments with the finance team. ML engineers thinking about how far AutoML-style selection can be pushed into an agent loop will get a useful checklist. If you already run a mature forecasting service, you can skim.

## Related Conf42 talks

- [Piotr Stepinski on forecasting time series with Polars and Deno](https://www.conf42.com/Machine_Learning_2024_Piotr_Stepinski_forecasting_timeseries) at Conf42 Machine Learning 2024, a hands-on counterpart to the model zoo.
- [Pawel Skrzypek and Anna Warno on advanced ensembling for time series forecasting](https://www.conf42.com/Python_2022_Pawel_Skrzypek_Anna_Warno_ensembling_techniques_time_series_forecasting), for the ensembling step AgentCast automates.
- [Vasuki Uday Kiran Vudathala on turning observability signals into peak readiness](https://www.conf42.com/Observability_2026_Vasuki_Uday_Kiran_Vudathala_loadtesting_performance_capacityplanning) at Conf42 Observability 2026, the capacity side of the same problem.

[Watch Premanand Tiwari's talk](https://www.conf42.com/DevOps_2026_Premanand_Tiwari_forecasting_time_autonomy)

[Watch the talk on YouTube](https://youtu.be/3Xx9AH3onCk).

## Watch the talk

[AgentCast: Autonomous AI-Driven Time Series Forecasting for DevOps at Scale](https://www.conf42.com/DevOps_2026_Premanand_Tiwari_forecasting_time_autonomy) at Conf42 DevOps 2026.
