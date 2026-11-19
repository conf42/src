# Forecasting Models Fail in Deployment, Not in the Notebook

Conf42 Blog, 2025-08-27, updated 2026-11-09. https://www.conf42.com/blog/platform2025/forecasts-fail-in-deployment-not-notebooks

In short: Amazon's Shivendra Kumar at Conf42 Platform Engineering 2025 on platform-first forecasting: microservices, APIs and asymmetric error costs.

Shivendra Kumar, who leads a team of demand planners and forecasters at Amazon, made one argument at Conf42 Platform Engineering 2025 that is worth the whole talk: a moderately accurate forecast that ships reliably every week beats a brilliant model that never leaves a research notebook. Everything else in "Platform-First Forecasting" is about building the platform that gets models out of the notebook and into decisions.

He comes at it with about 13 years in planning, supply chain and S&OP across Caterpillar, Dell and Amazon, so the framing is practitioner first.

## Accuracy is one metric among five

Most forecasting teams report MAPE or RMSE and call it a day. Shivendra lists what the business actually judges a forecast on:

- **Business alignment**: does the number come with context? Is it high against last week, low against the same week last year, growing at the rate the business expects?
- **Operational efficiency**: good science with a bad deployment gets perceived as a bad model.
- **Reliability and consistency**: output every week, through peak and off-peak, with a plan for the periods where it degrades.
- **User satisfaction**: are planners using it to make decisions?

The line about bad deployments is the one that will sting anyone who has watched a strong model lose trust because the Monday run failed twice.

## Put the business's risk appetite in the loss function

The most useful section is on asymmetric error handling. A single-number forecast hides the fact that over-forecasting and under-forecasting cost different amounts. For some products stockouts are expensive and spare inventory is cheap; for others excess stock is the disaster. Capacity planning has the same shape: overbuild and you carry depreciation, underbuild and service degrades. Financial forecasting trades compliance effort against speed.

His conclusion is that loss functions should reflect real business consequences, not mathematical convenience, and that the platform has to take that feedback in. If your model treats a missed sale and an overstocked pallet as the same error, it is optimising something nobody asked for.

## Decompose the monolith into four services

The architecture section splits a forecasting system into microservices: data ingestion (sources with daily or hourly cadence, quality checks), feature engineering, model training, and prediction serving with low-latency interfaces. Supporting pieces include Kafka-style stream processing, security controls and feature stores. Containerisation follows the workload: horizontal pod autoscaling, persistent storage planned for a dataset that will keep growing for years, and batch jobs where consumers only need yesterday's published version rather than a fresh query over billions of rows.

APIs get the same discipline: versioned, RESTful, with flexible request schemas, per-profile authorisation and progressive disclosure of complexity, so a new user isn't handed every knob on day one.

## Lego blocks for very different SKUs

In the e-commerce example, forecasting pens and forecasting couches need different methods, data and users. Building the system as reusable blocks lets each use case assemble only what it needs. Logistics works the same way: first, middle and last mile each have their own customers, on shared foundations. The abstract's revenue figure isn't something the talk walks through, so take the architecture as the takeaway.

## Who should watch

Data scientists who wonder why their models aren't adopted, and platform engineers asked to host ML workloads. It moves fast (he admits the time was short for the topic), so expect principles over code.

## Related Conf42 talks

- [Jubin Thomas on AI and ML demand forecasting in supply chains](https://www.conf42.com/Machine_Learning_2025_Jubin_Thomas_forecasting_supply_chain).
- [Madhusudan S Vadigicherla on supply chain forecasting](https://www.conf42.com/Golang_2025_Madhusudan_S_Vadigicherla_supply_chain_forecasting).
- [Piotr Stepinski: Forecasting time-series with Polars and Deno](https://www.conf42.com/Machine_Learning_2024_Piotr_Stepinski_forecasting_timeseries), for the hands-on end.

[Watch Shivendra Kumar's talk](https://www.conf42.com/Platform_Engineering_2025_Shivendra_Kumar_value_business_drive)

[Watch the talk on YouTube](https://youtu.be/aelVxuOUL-8).

## Watch the talk

[Platform-First Forecasting: Engineering Scalable ML Systems That Drive Business Value](https://www.conf42.com/Platform_Engineering_2025_Shivendra_Kumar_value_business_drive) at Conf42 Platform Engineering 2025.
