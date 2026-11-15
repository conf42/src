# Treat climate risk models for food systems like software

Conf42 Blog, 2026-01-21. https://www.conf42.com/blog/devops2026/genai-climate-risk-pipelines-for-food-systems

In short: Poshan Kumar of Kyndryl at Conf42 DevOps 2026 on generative AI climate scenarios, adaptation advice and stakeholder briefs run as GitOps pipelines.

A climate model that informs a planting decision should be versioned, tested and rolled back like any other production service. That's the thesis [Poshan Kumar](https://www.conf42.com/DevOps_2026_Poshan_Kumar_climate_modeling_food), Senior Lead and Managing Consultant at Kyndryl, brought to the sustainability track at Conf42 DevOps 2026: generative AI can simulate climate risk, propose local adaptations and write briefs for decision-makers, and DevOps practice is what makes those outputs reliable enough to act on.

The talk is short and dense, a reference architecture packed with dataset and model names rather than a demo. Kumar describes himself as an analytics architect working where enterprise platforms meet climate resilience, and the talk sits at that crossing.

## The operational backdrop changed

He opens with 2024, likely the first calendar year above 1.5 degrees over the pre-industrial baseline, with compounding floods and heat stress hitting production, storage and transport. Food insecurity stays high, with around 2.3 billion people facing moderate or severe food insecurity in the figures he cites. The engineering takeaway he draws is that data and ML systems for food have to anticipate extremes, quantify uncertainty and keep adapting.

## The inputs are better than most teams realise

The convergence he describes has three parts. First, data: ERA5 reanalysis gives hourly global data back to 1940 at roughly 31 km with uncertainty estimates; Sentinel-2 provides multispectral surface imagery at 10 to 20 m, useful for vegetation stress; CMIP6 scenarios define possible futures for stress testing. Second, ML weather and climate models: GraphCast for 10-day global forecasts, NeuralGCM as a hybrid physics-ML model that runs stably over decades, and generative downscaling to kilometre scale for precipitation and near-surface fields, which is what a farm-level decision needs. Third, DevOps maturity: containers, GitOps and policy as code.

## Three capabilities, one pipeline

The core of the talk is three generative capabilities. Climate scenario generation builds synthetic extreme-event ensembles conditioned on emissions pathways, downscales them, and validates them against historical analogues from ERA5. Adaptation strategy generation uses LLM agent workflows to suggest local interventions, such as crop rotation, irrigation timing tied to soil moisture and seed selection for drought, conditioned on hydrology, soils and economics. Automated brief generation writes stakeholder-specific briefs for farmers, buyers and NGOs, including uncertainty bands, scenario IDs and data provenance so the output can be audited.

Between them sit the unglamorous steps: ingest from the Copernicus data APIs and soil databases, link weather stress indices such as heat degree days to yield models, and render farmer-friendly maps.

## The DevOps stack is the familiar one

The architecture uses Argo Workflows for the container DAG (ingest, generate, downscale, evaluate, brief), Kubeflow Pipelines v2 for reusable ML components and experiment tracking, KServe for autoscaled inference with canary rollouts for both predictive models and LLM endpoints, Argo CD for cluster state and drift detection, and a model registry (Azure ML or SageMaker) for promotion, lineage and approval gates. Pipelines fail on significant data or prediction drift, and dataset and model version IDs travel in metadata. Nothing in that list will surprise an MLOps engineer, which is the point: the climate part is new, the plumbing is not.

## Governance built in

For trust, Kumar maps the NIST AI Risk Management Framework (govern, map, measure, manage) and its 2024 generative AI profile onto pipeline stages, and wants a model card for each climate and LLM component. His closing advice: integrate AI into pipelines, treat climate LLM artifacts like versioned, tested software, promote them through GitOps, and keep outputs practical.

## Who should watch

MLOps and platform engineers working with geospatial or agricultural data, and climate-tech teams that need a production architecture rather than a notebook. The auto-generated captions struggle with the dataset names, so keep the slides at hand.

## Related Conf42 talks

- [Building Scalable Data Pipelines With Argo Workflows](https://www.conf42.com/Kube_Native_2022_David_Joyce_scalable_data_pipelines_argo_workflows) by David Joyce at Conf42 Kube Native 2022.
- [How to build your own green observability pipeline](https://www.conf42.com/Observability_2026_Diana_Todea_opensource_observability_sustainability) by Diana Todea at Conf42 Observability 2026.
- [Using Open Earth Observations for measuring economic indicators](https://www.conf42.com/Python_2021_Aakash_Gupta_Abha_Porwal__Apsal_K_earth_observations_measuring_economic_indicators) at Conf42 Python 2021.

[Watch Poshan Kumar's talk](https://www.conf42.com/DevOps_2026_Poshan_Kumar_climate_modeling_food) or the [YouTube recording](https://youtu.be/wIp392eKg7s).

## Watch the talk

[Generative AI Workflows for Climate Risk Modeling in Food Systems](https://www.conf42.com/DevOps_2026_Poshan_Kumar_climate_modeling_food) at Conf42 DevOps 2026.
