# What SAP AI on BTP actually does, industry by industry

Conf42 Blog, 2025-06-19, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/sap-ai-on-btp-industry-tour

In short: Levi Strauss & Co. SAP project manager Venkata Kalyan Chakravarthy Mandavilli tours SAP AI use cases at Conf42 Quantum Computing 2025.

Most ERP users meet SAP's AI as a recommendation in a screen they already use, not as a model they deploy. Venkata Kalyan Chakravarthy Mandavilli, SAP Project Manager at Levi Strauss & Co., spent his session at Conf42 Quantum Computing 2025 mapping which techniques sit behind those features on SAP's Business Technology Platform (BTP), across retail, healthcare, manufacturing, finance, supply chain, energy and agriculture.

Fair warning on scope: this is an SAP AI talk that happened to land at a quantum conference. There are no qubits in it. What it offers instead is a catalogue of classical ML patterns mapped onto the ERP processes they serve, from someone who has spent years leading SAP implementations across manufacturing, pharma, food and beverage and more.

## The stack: BTP underneath, AI core on top

Mandavilli starts with the architecture. BTP provides the integration layer, API management and data orchestration. On top, SAP's AI core offers machine learning services (classification, regression, clustering, anomaly detection), natural language processing (entity extraction, sentiment, document understanding) and computer vision (object detection, defect identification, visual inspection). The pitch is that these plug into existing SAP systems rather than living in a separate data science silo.

## Retail and healthcare: familiar models, specific inputs

For retail, recommendations come from hybrid models that combine collaborative filtering with content-based filtering, using purchase history and browsing patterns. Demand forecasting ensembles LSTM networks with classical ARIMA models and adds external signals like seasonality, market trends and social media sentiment.

Healthcare is the more interesting example. Admission prediction uses regression and classification over historical admissions, seasonal illness patterns, population demographics, facility utilisation and the local event calendar, which is a neat reminder that a marathon in town is a capacity-planning input. NLP mines unstructured clinical notes alongside structured data, with HIPAA compliance kept in the loop.

## Manufacturing gets the numbers

The manufacturing section has the talk's firmest figures, presented as industry results for predictive maintenance: unplanned downtime reduced by up to 50% and maintenance costs down 10 to 40% compared with scheduled maintenance. The loop is IoT sensor data collection, pattern analysis to predict failures, maintenance scheduling before they happen, then continuous learning. For quality, CNN-based visual inspection is cited as catching up to 99% of surface defects against 80 to 90% for traditional machine vision and human inspectors.

## Finance, supply chain, energy, fields

The rest of the tour moves quickly:

- **Finance**: graph neural networks that model relationships between entities to flag fraud, with SHAP and LIME for explainable decisions, and reinforcement learning for forecasting.
- **Supply chain**: multi-objective evolutionary algorithms balancing cost, time and environmental impact, early-warning ensembles, digital twins and automatic rerouting.
- **Energy and utilities**: reinforcement learning for consumption optimisation, hybrid physics-plus-ML renewable forecasting, storage charge cycles and microgrid balancing.
- **Agriculture**: multispectral satellite imagery for moisture stress and pest detection, field sensors, and gradient-boosted trees for yield prediction.

## Who should watch

SAP functional leads, solution architects and project managers who need a vocabulary for which model fits which SAP process, and data scientists joining an SAP shop. If you were hoping for quantum, pick another talk from the same event; if you have an SAP roadmap on your desk, this one is a useful checklist.

## Related Conf42 talks

- [The next generation of SAP Cloud ERP with AI](https://www.conf42.com/Cloud_Native_2025_Sravan_Kumar_Nendrambaka_sap_enterprise_optimization) by Sravan Kumar Nendrambaka, on S/4HANA Cloud editions.
- [AI-driven master data governance for incident management in SAP](https://www.conf42.com/Incident_Management_2025_Gobinath_Kasimayan_sap_governance_agility) by Gobinath Kasimayan, because every model above depends on clean master data.
- [Building event-driven AI agents for proactive SAP incident management](https://www.conf42.com/AI_Agents_2026_Pon_Murugesh_Devendren_sap_incidents_events) by Pon Murugesh Devendren, where SAP AI goes agentic.

[Watch Venkata Kalyan Chakravarthy Mandavilli's talk](https://www.conf42.com/Quantum_Computing_2025_Venkata_Kalyan_Chakravarthy_Mandavilli_sap_ai_transformation)

[Watch the talk on YouTube](https://youtu.be/k2xCTw7bPA4).

## Watch the talk

[SAP AI's Transformative Power: Technical Insights & Industry-Specific Applications](https://www.conf42.com/Quantum_Computing_2025_Venkata_Kalyan_Chakravarthy_Mandavilli_sap_ai_transformation) at Conf42 Quantum Computing 2025.
