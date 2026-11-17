# Let sensor data, not the calendar, write the maintenance work order

Conf42 Blog, 2025-09-19, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/genai-predictive-maintenance-car-plants-erp

In short: Abhijit Joshi (Deloitte Consulting) at Conf42 Kube Native 2025 on using GenAI on IoT sensor data to drive ERP maintenance work orders in automotive plants.

Most factory maintenance still runs on the calendar: every three months, whether the robot worked hard or sat idle. At Conf42 Kube Native 2025, Abhijit Joshi of Deloitte Consulting, a supply chain transformation specialist with 20 years in automotive manufacturing who started his career in plant maintenance, made the case for letting generative AI read sensor data and decide when the ERP system should raise a work order.

The stakes he quoted are blunt: unplanned equipment downtime costing automotive manufacturers up to 22,000 per minute, and traditional strategies that cannot keep up. His claim is that putting GenAI between IoT data and ERP maintenance planning can cut unplanned downtime by around 40%.

## Calendar, usage and condition all miss something

Joshi walked through the three classic approaches, using the analogy of servicing your own car. Calendar-based maintenance services equipment at fixed intervals, regardless of how much it ran, so it is either too early or too late. Usage-based maintenance waits for a run count or cycle threshold. Condition-based maintenance acts when a monitored parameter crosses a limit. All three are reactive in practice, waste resources, and ignore most of the historical data the plant already has.

## Three drivers, one loop

His framework stacks three components. IoT sensors on the line capture vibration, temperature and pressure continuously, something no human inspector can do. The ERP system already knows inventory, work orders, parts, instructions and technician capacity. Generative AI sits on top: it models equipment behaviour, generates synthetic data to simulate operating conditions the plant has not seen yet, learns failure patterns from history plus live data, and tells the ERP when a work order is due based on actual deterioration.

The output is three actions: an automated maintenance work order to a technician, a plan that schedules work around expected downtime, and KPIs from the same data. ERP feedback then refines the model.

## Start with the robots and the paint shop

He named two target applications where failures hurt most in car plants: automated assembly and welding robots, where continuous monitoring of operating patterns catches early failure, and paint application lines, where predictive maintenance on booths and spray systems prevents both downtime and quality defects.

Implementation advice is deliberately low-drama. Use existing sensors and infrastructure rather than building new ones, feed the data through a warehouse into a readable format, plug predictions into the existing work order flow, and roll out one plant or even one line at a time.

## The numbers come with a caveat

Joshi presented ballpark results from studied deployments: downtime down 40%, forecasting accuracy improved by around 85%, false alarms cut by 50%, maintenance costs down 30%, and first-time fix rates reaching 90%. He was clear these vary by company and are expected outcomes rather than one client's figures. His end state is the zero-downtime factory, with systems that eventually self-diagnose.

## Who should watch

Manufacturing IT and ERP teams, maintenance planners and anyone scoping an industrial IoT project who needs to explain the business flow to plant leadership. Despite the conference name, the talk is about the maintenance and ERP workflow, not Kubernetes, so platform engineers looking for cluster patterns should pick one of the related talks below.

## Related Conf42 talks

- [Transforming Manufacturing Through AI-Driven Predictive Maintenance](https://www.conf42.com/MLOps_2025_Muruga_Angamuthu_transforming_manufacturing_ai) by Muruga Angamuthu (Techtronic Industries) covers the same shift from the MLOps side.
- [AI Driven Vectorized Motor Health Monitoring for Reliable Industrial Operations](https://www.conf42.com/DevOps_2026_Avinash_Sista_maintenance_industrial_ai) by Avinash Sista (MongoDB) zooms in on turning motor signals into predictions.
- [Secure IoT Edge Architecture: Predictive Maintenance for Medical Diagnostic Systems](https://www.conf42.com/Internet_of_Things_IoT_2025_Ramakrishna_Ambati_maintenance_predictive_medical) by Ramakrishna Ambati (Visby Medical) applies it to medical devices at the edge.

[Watch Abhijit Joshi's talk](https://www.conf42.com/Kube_Native_2025_Abhijit_Joshi_maintenance_predictive_manufacturing)

[Watch the talk on YouTube](https://youtu.be/LDYtrShQAMs).

## Watch the talk

[Generative AI for Predictive Maintenance in Kubernetes-Native Manufacturing Ops](https://www.conf42.com/Kube_Native_2025_Abhijit_Joshi_maintenance_predictive_manufacturing) at Conf42 Kube Native 2025.
