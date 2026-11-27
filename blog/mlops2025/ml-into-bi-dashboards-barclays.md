# Most finance ML dies after training. MLOps gets it into BI dashboards

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/ml-into-bi-dashboards-barclays

In short: Mallikarjun Ramasani (Barclays) at Conf42 MLOps 2025 on the ML lifecycle for finance and wiring model output into Tableau and Qlik.

The bottleneck in financial ML is rarely the model. It is everything that happens after. At Conf42 MLOps 2025, Mallikarjun Ramasani, a software engineer and BI developer at Barclays, walked through the ML lifecycle as it plays out in finance and finished where a BI developer naturally would: getting predictions into the Tableau and Qlik dashboards people already trust.

## The maturity gap

Mallikarjun opens with a figure meant to sting: 83% of ML models in finance never make it to production. That is talent and platform spend with no business value. His reasons are familiar to anyone in a bank: complex requirements that slow deployment, legacy systems that resist integration, and real-time performance needs most pipelines cannot meet.

The fix he proposes is MLOps as the bridge between model development and business impact: automated deployment, logging, compliance checks, versioning and monitoring, so a risk review that took weeks can happen in days or hours.

## The lifecycle, with a financial twist at each stage

Each stage gets a finance-specific note. Ingestion is not pulling CSV files; it is streaming market data, payment data and alternative datasets. Feature engineering is where risk signals live: rolling windows, credit utilisation ratios, liquidity metrics. Training needs hyperparameter tracking and regulatory documentation, because every decision must be explainable. Deployment is containerised and runs through CI/CD. Monitoring covers drift, performance, compliance auditing and financial impact.

For market data he highlights temporal features (how price and volume evolve, short-term versus long-term trends) and market microstructure features like bid-ask spread, order book depth imbalance, transaction costs and slippage.

## A tool for every stage

The stack slide is a useful shopping list: Apache Airflow, Spark and Kubeflow for pipelines; DVC for data versioning; MLflow for experiment tracking and the model registry, with Neptune.ai for comparing runs; Docker and Kubernetes for scalable deployment, plus BentoML and Amazon SageMaker; and Evidently AI for drift detection and metrics.

CI/CD in his framing is a governance framework as much as a DevOps practice. New data passes quality and bias checks, the training pipeline generates documentation and risk reports automatically, canary releases reduce rollout risk, and compliance reviews are built into the pipeline as gates instead of email threads.

## Drift, measured

The drift section is concrete. Monitor input features and predictions over time, watch for training-serving skew, check pipeline health, backtest continuously, and alert on unexpected changes. For detection he names population stability index and KL divergence, with recalibration or retraining on recent data when drift is flagged. Governance rests on model cards aligned with SR 11-7, SHAP and LIME explainability reports, immutable logs and reproducible environments, with encrypted pipeline components, strict role-based access and container scanning.

## The BI bit

The part that sets this talk apart is integration with BI tools. Mallikarjun describes four approaches: APIs exposing model predictions as endpoints, embedded Python for in-dashboard computation, pre-computed feature stores for low-latency access, and custom visualisation extensions for model insights, across platforms like Tableau, Power BI, Looker and ThoughtSpot. The pay-off is predictive analytics and automated insights sitting inside tools business users already open every morning.

His takeaways: design the pipeline with financial requirements in mind from day one, integrate early with the BI tools users trust, and build compliance into the workflow rather than adding it later.

## Who should watch

BI developers and analytics engineers in finance who want to bring ML into their dashboards, and MLOps engineers who need a stage-by-stage tool map. It is a broad survey, so expect breadth over depth.

## Related Conf42 talks

- [Intelligent Incident Management: AI, ML, and the Future of Resilient Cloud Operations](https://www.conf42.com/Incident_Management_2025_Mallikarjun_Ramasani_intelligence_cloud_future), Mallikarjun's talk at Conf42 Incident Management 2025
- [AI-Powered Business Intelligence in Healthcare: Leveraging Go for Scalable, Real-Time Analytics](https://www.conf42.com/Golang_2025_Satya_Manesh_Veerapaneni_healthcare_bi_analytics)
- [Using Cloud, AI, and Metadata for Scalable Cost Reduction in Financial Systems](https://www.conf42.com/Machine_Learning_2025_Srinivasa_Rao_Akyana_metadata_financial_reduction)

[Watch Mallikarjun Ramasani's talk](https://www.conf42.com/MLOps_2025_Mallikarjun_Ramasani_operationalizing_ai_finance)

[Watch the talk on YouTube](https://youtu.be/YQwEkucJILs).

## Watch the talk

[Operationalizing AI in Finance: MLOps for Scalable BI and Real-Time Analytics](https://www.conf42.com/MLOps_2025_Mallikarjun_Ramasani_operationalizing_ai_finance) at Conf42 MLOps 2025.
