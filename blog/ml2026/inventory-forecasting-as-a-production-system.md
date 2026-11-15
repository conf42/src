# Inventory forecasting belongs in a pipeline, not a spreadsheet

Conf42 Blog, 2026-02-06, updated 2026-11-09. https://www.conf42.com/blog/ml2026/inventory-forecasting-as-a-production-system

In short: Pallab Haldar of Cognizant at Conf42 Machine Learning 2026 on an Azure reference architecture that moves inventory forecasts into production ML.

Order 70 units when you needed 30 and the excess sits in a warehouse; order 10 and the line stops. At Conf42 Machine Learning 2026, Pallab Haldar, Technical Architect at Cognizant, walked through a reference architecture for taking inventory forecasting out of spreadsheets and static rules and running it as a production ML system that orders close to the real need.

It is an architecture talk, built on Azure, with healthcare and logistics scenarios rather than one deep case study.

## Why forecasts fail

Pallab's diagnosis is that inventory planning lives in a volatile environment: demand swings, supply disruptions, approval processes, regulations and audits all get in the way. Manual, spreadsheet-driven planning adds delay on top, and the result is stockouts on one side and excess inventory on the other. The three failures he named explicitly are static rules, stale data and the lack of a feedback loop.

## The reference architecture: data, features, model, decision

The pipeline has four stages, and the first gets the most care.

**Data ingestion.** Different warehouses run different systems: one has an ERP, another a point-of-sale feed, another IoT devices. Azure Data Factory pipelines pull them into Data Lake Storage Gen2, where data is harmonised and cleaned. Quality and governance sit at this layer: validation, cleansing, schema checks, lineage, a catalogue, and role-based access.

**Feature engineering.** Lag features, seasonal signals, promotions and weather, the inputs that turn order history into a forecast that knows about next month.

**Model validation.** Backtesting with MAE and MAPE, plus checks for bias and fairness and outlier removal before anything is promoted.

**Deployment and MLOps.** CI/CD for models, a model registry with versioning and metadata for audit, and monitoring with alerts once the model is live.

## What "good" looks like

Pallab's example of the target behaviour is plain: if the right order is 30 units, a trained model should come back with 28 or 29, never 10 and never 70. Getting close consistently is what reduces stockouts and carrying cost and lets ordering from suppliers run without a planner in the loop.

He then mapped the same pattern onto two industries. In healthcare, demand forecasting feeds capacity planning and proactive replenishment. In logistics, it feeds route optimisation, disruption prediction and risk planning. The point of the scenarios is that the four-stage pipeline stays the same while the decisions on top change.

## Who should watch

Architects and data engineers asked to "add ML" to a supply-chain planning process, especially on Azure. If you want model internals or a single company's results, this is not that talk; if you need a reference diagram to argue from, it is.

## Related Conf42 talks

- [Demand Forecasting in Supply Chain Using Artificial Intelligence Basis Machine Learning](https://www.conf42.com/Machine_Learning_2025_Jubin_Thomas_forecasting_supply_chain) by Jubin Thomas, the modelling side of the same problem.
- [Cloud-Native AI in Procurement: Automating Sourcing, Reducing Costs, and Enhancing Supply Chain Resilience](https://www.conf42.com/Cloud_Native_2025_Parameswara_Rao_Tatini_procurement_automation_resilience) by Parameswara Rao Tatini.
- [Predictive Observability: Prevent Supply Chain Outages Before They Break Your Production](https://www.conf42.com/DevOps_2026_Raghu_Bhupatiraju_predictive_analytics_outages) by Raghu Bhupatiraju.

[Watch Pallab Haldar's talk](https://www.conf42.com/Machine_Learning_2026_Pallab_Haldar_orchestration_workflows_ai) from [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026).

[Watch the talk on YouTube](https://youtu.be/nExYGDbszKs).

## Watch the talk

[Transforming Inventory Forecasting with Production ML](https://www.conf42.com/Machine_Learning_2026_Pallab_Haldar_orchestration_workflows_ai) at Conf42 Machine Learning 2026.
