# Predictive maintenance pays, so why do most factory pilots fail?

Conf42 Blog, 2025-09-09, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/predictive-maintenance-why-most-pilots-fail

In short: Muruga Angamuthu of Techtronic Industries at Conf42 MLOps 2025 on AI predictive maintenance, its tech stack, and the reasons most initiatives stall.

A machine that breaks without warning costs far more than one you fix on your own schedule, and almost everyone in manufacturing knows it. At Conf42 MLOps 2025, Muruga Angamuthu, BI Manager and Data & Analytics architect at Techtronic Industries (TTI), made the case for AI-driven predictive maintenance and then spent a good part of his talk on the less glamorous question: why roughly 60% of these initiatives fail anyway.

It is a compact, overview-style talk from someone with 23 years across data engineering, BI and manufacturing. Expect a structured tour (stack, models, failure modes, roadmap) rather than code.

## Maintenance has four eras, and most plants are stuck in the first two

Muruga framed the problem as an evolution. Reactive maintenance fixes things after they break, with unpredictable cost and big production disruption. Preventive maintenance follows a fixed calendar and replaces parts too early or too late. Predictive maintenance services equipment based on its condition. The fourth stage, the one he argued for, is ML that predicts failures and keeps getting better as it learns.

The numbers he cited for the destination are the industry-report kind: up to $50,000 lost per hour of unplanned downtime, reactive repairs three to ten times pricier than predictive ones, and organisations reporting around half the downtime, roughly a third lower maintenance cost and a 385% return on investment. The figure that matters most operationally is the warning window: models giving eight to twelve days of advance notice, enough time to order spare parts and schedule the outage instead of discovering it.

## The stack: sensors, edge, cloud, and four model families

The architecture section is a useful checklist. IoT sensors on industrial machines capture temperature, vibration and pressure, and he put the volume at 1.5 to 2.3 terabytes a day per setup. Edge computing pre-filters that stream on site and handles instant alerts. A cloud data platform keeps the history and runs training, deployment and cross-facility benchmarking.

On top sit four techniques, each with a job: autoencoders that learn what normal looks like and flag deviations, random forest classifiers that name the specific failure mode, recurrent neural networks that read long time series for slow degradation, and digital twins that simulate the equipment to sharpen predictions. Nobody wins with a single model here; the anomaly detector says "something is off" and the classifier says what.

## Failure is mostly data and people

This is the part worth the watch. Muruga gave three reasons pilots die. Data integration first: legacy machines without sensors, siloed IT systems and inconsistent data quality, which he said trips up nearly 80% of deployments. Scope second: projects that run 30 to 40% over budget because the proof of concept was too wide or too weakly validated. People third: technicians who resist because they fear for their jobs or simply don't trust the model's recommendations.

His blueprint answers each one. Start with the equipment whose failure costs the most. Link maintenance, production and quality systems into one data architecture. Bring technicians in early so the tools fit their workflow. Scale in phases, proving ROI at each step. The roadmap that follows is concrete about timing: one to three months of foundation work, four to six months of pilot on the highest-impact assets, seven to twelve months of expansion with ERP integration, and a second year for digital twins and a predictive maintenance centre of excellence.

He also pointed at explainable AI as the fix for the trust problem: a technician who can see why the model flagged a bearing is far more likely to act on it.

## Who should watch

Data and ML engineers moving into industrial settings, and anyone handed a predictive maintenance project with a budget and a deadline. If you already run sensor pipelines at scale, the failure-modes and roadmap sections are the parts to skip to.

## Related Conf42 talks

- Muruga's own follow-up on the platform side: [Building Scalable AI/ML Platforms for Industrial IoT](https://www.conf42.com/Platform_Engineering_2025_Muruga_Angamuthu_industrial_iot_maintenance) at Conf42 Platform Engineering 2025.
- Abhijit Joshi (Deloitte Consulting) on [Generative AI for Predictive Maintenance in Kubernetes-Native Manufacturing Ops](https://www.conf42.com/Kube_Native_2025_Abhijit_Joshi_maintenance_predictive_manufacturing).
- Divakar Duraiyan (Tata Consultancy Services) takes digital twins to the sky in [Aircraft Observability Revolution](https://www.conf42.com/Observability_2025_Divakar_Duraiyan_aircraft_digital_twins).

[Watch Muruga Angamuthu's talk](https://www.conf42.com/MLOps_2025_Muruga_Angamuthu_transforming_manufacturing_ai)

[Watch the talk on YouTube](https://youtu.be/ADZwH-lsc2c).

## Watch the talk

[Transforming Manufacturing Through AI-Driven Predictive Maintenance: From Reactive Crisis to Proactive Excellence](https://www.conf42.com/MLOps_2025_Muruga_Angamuthu_transforming_manufacturing_ai) at Conf42 MLOps 2025.
