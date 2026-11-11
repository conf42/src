# Conf42 Machine Learning 2026: shipping models is the hard part

Conf42 Blog, 2026-02-20. https://www.conf42.com/blog/ml2026/conf42-machine-learning-2026-roundup

In short: Conf42 Machine Learning 2026 roundup - why models fail after deployment, switchback tests, explainable recommenders, ML security and agents, in 35 talks.

Conf42 Machine Learning 2026 ran online on February 19, 2026, with 35 talks, and very few of them were about training a better model. The lineup was about everything that happens after the notebook: drift, data skew, failing pipelines, experiments that lie, recommendations nobody can explain, and the identities and compliance rules wrapped around the whole thing. The abstract of a talk by Ancilia Dmello of Ford summed up the mood in six words: shipping ML is harder than training it.

All sessions are on the [Conf42 Machine Learning 2026 event page](https://www.conf42.com/ml2026) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrAxRHbUdOPlp1-OnsVso-nC).

## Good models, bad production

[Oleksandr Pyvovar](https://www.conf42.com/Machine_Learning_2026_Oleksandr_Pyvovar_robustness_reliability_models), a machine learning engineer at Meta, opened with the scenario every ML team knows: a model hits 95% accuracy in the lab and six months later barely beats random guessing. His explanation is that good models rarely fail because they were wrong; the world changes after deployment. The talk walks through data drift (train a self-driving car only on sunny days, then send it to a foggy city), concept drift, label drift, feature pipeline degradation, training-serving skew, and feedback loops that amplify bias, followed by a monitoring framework and a remediation playbook.

[Ancilia Dmello](https://www.conf42.com/Machine_Learning_2026_Ancilia_Dmello_forecasting_inventory_retail) of Ford Motor Company laid out an observable MLOps framework on Google Cloud covering real-time, batch, and streaming inference, drift detection, CI/CD, and retraining. [Srihari Godleti](https://www.conf42.com/Machine_Learning_2026_Srihari_Godleti_fairness_bias_mitigation) of Roku made the case that slow training is often data skew rather than bad code, with three Apache Spark techniques to fix it. [Kiran Ramanna](https://www.conf42.com/Machine_Learning_2026_Kiran_Ramanna_retraining_lifecycle_models) of ServiceNow and [Srinivas Talasila](https://www.conf42.com/Machine_Learning_2026_Srinivas_Talasila_compliance_governance_ai) of SAP covered the organisational and infrastructure halves of the same problem: readiness to stop pilot sprawl, and HA, DR, and zero trust for the platforms models run on.

## Predict the failure before it burns compute

[Pavel Solikov](https://www.conf42.com/Machine_Learning_2026_Pavel_Solikov_security_adversarial_attacks) of J.P. Morgan had one of the most practical talks of the day. His team's Prefect flows can run for 30 minutes or two hours and fail at the end. Since Prefect already knows the parameters, environment, and metadata at the start, and the first tasks can cheaply fingerprint data quality, a gradient boosting model can score the risk of failure in the first minute or two and abort, reroute, or warn the developer with a reason.

[Tim Markin](https://www.conf42.com/Machine_Learning_2026_Tim_Markin_feature_stores_management) of GiftHorse turned the same idea on software delivery: a production ML system that scores pull requests for risk and estimates delivery time before coding starts, using repo metadata, AST features, and CI signals.

## Experiments and recommendations you can trust

[Sergei Nasibian](https://www.conf42.com/Machine_Learning_2026_Sergei_Nasibian_knowledge_graphs_reasoning), a Quantitative Strategist at Rothesay, explained why classic A/B tests break for delivery pricing in food tech: when you change prices, you change courier supply and other users' experience too. Switchback testing, which alternates treatments over time rather than splitting users, is the alternative.

[Lev Fedorov](https://www.conf42.com/Machine_Learning_2026_Lev_Fedorov_optimization_performance_efficiency) of Amazon showed how his team turned a black-box recommender into a traceable ranking system, with per-user recommendation traces and user-facing reasons, such as a productivity video shown because you once liked one about effective planning. The trigger was users reporting irrelevant content and developers unable to say why it appeared. [Rohan Mitra](https://www.conf42.com/Machine_Learning_2026_Rohan_Mitra_experimentation_reproducibility_science) of PhonePe gave a hands-on tutorial on writing the spec for a recommendation system, and [Murthy Chandrapaty and Chakravarthy Kalva](https://www.conf42.com/Machine_Learning_2026_Murthy_Chandrapaty_Chakravarthy_Kalva_decisioning_b2c_marketing) of Adobe argued that send-time optimisation should grow from a prediction problem into decisioning.

## ML in money and markets

Finance and marketing filled two tracks. [Avaneendra Kanaparti](https://www.conf42.com/Machine_Learning_2026_Avaneendra_Kanaparti_experimentation_abtesting_optimization) of American Express covered customer lifetime value models for approvals and credit lines, [Balakumaran Sugumar](https://www.conf42.com/Machine_Learning_2026_Balakumaran_Sugumar_anomaly_detection_signals) of Synchrony mapped where ML sits in payment platforms, and [Vivek Kumar](https://www.conf42.com/Machine_Learning_2026_Vivek_Kumar_responsible_ethics_ai) of Majesco used telemetry to predict performance problems in high-volume transaction systems. [Abhinay Kumar Reddy Seella](https://www.conf42.com/Machine_Learning_2026_Abhinay_Kumar_Reddy_Seella_satisfaction_prediction_telemetry) of Roku predicted user satisfaction in real time from LLMs and behavioural telemetry instead of waiting for surveys, and [Ashutosh Verma](https://www.conf42.com/Machine_Learning_2026_Ashutosh_Verma_scalability_architecture_distributed) of Meta connected online and offline journeys for attribution.

## Securing the pipeline, and the people with access to it

The security track treated ML platforms like any other production system. [Reshma Vemula](https://www.conf42.com/Machine_Learning_2026_Reshma_Vemula_pipelines_orchestration_mlops) of Loma Linda University Health showed how PHI leaks into development environments, and [Neha Asthana](https://www.conf42.com/Machine_Learning_2026_Neha_Asthana_simulation_synthetic_data) of Abbott argued that ML platforms are only as secure as the identities behind them. [Aleksandra Drobnjak](https://www.conf42.com/Machine_Learning_2026_Aleksandra_Drobnjak_documentation_artifacts_beginners) gave a beginner-friendly guide to the minimum ISO 42001 documentation for an AI management system, for the moment someone asks who approved this model and what data it used. [Sagar Sudhir Behere](https://www.conf42.com/Machine_Learning_2026_Sagar_Sudhir_Behere_streaming_realtime_analytics) of Circle and [Sudheer Kumar Aluvala](https://www.conf42.com/Machine_Learning_2026_Sudheer_Kumar_Aluvala_optimization_hyperparameters_tuning) of HCL America applied ML to third-party risk and zero trust compliance.

## Agents arrive, carefully

Agents had their own track, with an emphasis on guardrails. [Sumit Kaul](https://www.conf42.com/Machine_Learning_2026_Sumit_Kaul_architecture_design_patterns) of PayJoy designed incident response agents that propose root causes and mitigations while humans keep decision authority. [Marat Kenzhebulatov](https://www.conf42.com/Machine_Learning_2026_Marat_Kenzhebulatov_vision_computer_imaging) of Booking.com covered AI agents in security-critical backend work, [Rajeshwari Sah](https://www.conf42.com/Machine_Learning_2026_Rajeshwari_Sah_labeling_annotation_quality) of Apple built a clinical documentation scribe as a LangGraph state machine, and [Sujith Vadakkepati](https://www.conf42.com/Machine_Learning_2026_Sujith_Vadakkepati_deployment_containers_kubernetes) of Oracle combined RAG with ERP data for explainable supplier risk.

Further afield, [Sowmiya Narayanan Govindaraj](https://www.conf42.com/Machine_Learning_2026_Sowmiya_Narayanan_Govindaraj_risk_modeling_assessment) of Motional covered unified perception models for autonomous driving, and [Mohamed Najaaf](https://www.conf42.com/Machine_Learning_2026_Mohamed_Najaaf_recommendation_ranking_systems) of AWS showed how to cut the carbon footprint of generative AI workloads. Operations talks from [Anu Arora](https://www.conf42.com/Machine_Learning_2026_Anu_Arora_personalization_recommendation_platforms) of ServiceNow, [Dinesh Garg](https://www.conf42.com/Machine_Learning_2026_Dinesh_Garg_evaluation_benchmarks_metrics) of Honeywell, and [Pallab Haldar](https://www.conf42.com/Machine_Learning_2026_Pallab_Haldar_orchestration_workflows_ai) of Cognizant covered autonomous IT support, IoT warehouse data, and inventory forecasting.

## Sponsors and what's next

Thanks to gold sponsors [LLMday](https://llmday.com/) and the [Prompt Engineering Conference](https://promptengineering.rocks/), the [HockeyStick](https://www.hockeystick.show/) podcast, and the media partners on the event page.

The next edition, [Conf42 Machine Learning 2027](https://www.conf42.com/ml2027), is set for February 18, 2027. Until then, check your drift dashboards.
