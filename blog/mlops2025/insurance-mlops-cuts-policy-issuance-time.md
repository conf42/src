# How MLOps cut insurance policy issuance time by 99%

Conf42 Blog, 2025-09-18, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/insurance-mlops-cuts-policy-issuance-time

In short: Sameer Joshi of Cognizant at Conf42 MLOps 2025 on feature stores, model registries and compliance pipelines behind AI in insurance operations.

Insurance used to issue a policy in three to four days and assess a claim in weeks. At Conf42 MLOps 2025, Sameer Joshi, Senior Manager Projects at Cognizant and a technical architect on Duck Creek cloud platforms, walked through how MLOps practices compress those cycles, and why the plumbing (registries, feature stores, validation pipelines) matters more than any single model in a regulated industry.

The talk is a brisk, slide-driven survey across the main insurance use cases. Treat the headline percentages as the speaker's reported results rather than a benchmark you can reproduce; the value is in seeing where ML lands in an insurer and what infrastructure each use case leans on.

## The before picture is paperwork

Sameer started with the traditional carrier: paper applications and manual data entry, underwriting that depended on who was looking at the file, claims assessments stretching for weeks and risk evaluated once a year. The cost of that is long cycle times and a customer experience that varies by desk. His figure for adoption was that carriers went from about 18% experimenting with AI to 54% once MLOps practices made models operable.

## Four components do most of the work

The architecture he described is standard MLOps, applied to an industry where every decision may need defending to a regulator. GitOps-style automated deployment pipelines. Monitoring for real-time drift detection. Experimentation platforms for A/B testing. Centralised feature stores with versioning, which he credited with cutting feature engineering time by 67%, and model registries for traceability.

Data integration sits underneath: eight to twelve sources joined per decision, from customer and property records to IoT, telematics, credit scores and satellite imagery. Policy issuance is where it pays off most visibly: a three-to-four-day process cut by a reported 99%, the figure in the title, at 93.6% accuracy.

## Three use cases with very different shapes

Catastrophe modelling swapped static data and quarterly updates for live weather feeds, satellite imagery and ensembles that mix physics models with ML. Computer vision for property and casualty runs on drones with edge-deployed models, so an inspection that used to take days finishes in minutes, with champion/challenger frameworks keeping the models honest. Telematics pulls more than 300 driving features from OBD-II devices and smartphones through Kafka-based streaming pipelines into containerised inference that scales with traffic.

Each is a different MLOps problem: batch retraining on fresh climate data, edge deployment, and high-throughput streaming. Seeing them side by side is the most useful part of the talk.

## Compliance belongs in the pipeline

The section on fairness is short but pointed. Automated adversarial testing before deployment catches bias early, validation pipelines generate the documentation regulators ask for, and LIME and SHAP explanations make individual decisions explainable. In insurance, a model nobody can explain is a model nobody can ship.

His roadmap is three phases: foundation (registries, versioning, pipelines) over three to four months, operationalising training and monitoring over two to three, then optimisation with automated retraining, A/B testing and compliance automation. Under a year from proof of concept to production, by his estimate. The next step he gave the audience is refreshingly practical: assess your ML maturity, pick high-value use cases, and build compliance in from day one.

## Who should watch

Engineers and architects at carriers or insurance software vendors who need a map of where MLOps fits, and anyone pitching feature stores to a compliance team. If you want implementation detail on any one use case, pair it with a deeper talk.

## Related Conf42 talks

- Gurucharann Visagamurthy (Humana) on [Cloud-Native Insurance: Real-Time Underwriting & Enrollment at Kubernetes Scale](https://www.conf42.com/Kube_Native_2025_Gurucharann_Visagamurthy_insurance_enrollment_realtime).
- Harsha Vardhan Reddy Yeddula on [Harnessing AI for Next-Gen Underwriting in Insurance](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Harsha_Vardhan_Reddy_Yeddula_harnessing_ai_next).
- Bhaskara Beeraka (American Family Insurance) on [Transforming Insurance Through AI](https://www.conf42.com/Cloud_Native_2025_Bhaskara_Beeraka_insurance_innovation_insights).

[Watch Sameer Joshi's talk](https://www.conf42.com/MLOps_2025_Sameer_Joshi_ai_driven_insurance)

[Watch the talk on YouTube](https://youtu.be/NUmzhqVXe_A).

## Watch the talk

[AI-Driven Insurance Operations: MLOps Strategies Delivering 65% Efficiency Gains and 99% Processing Time Reduction](https://www.conf42.com/MLOps_2025_Sameer_Joshi_ai_driven_insurance) at Conf42 MLOps 2025.
