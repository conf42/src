# A microphone on the machine can hear the failure coming

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/acoustic-iot-sensors-predictive-maintenance

In short: Karthikeyan Rajamani, Lead SRE at Thomson Reuters, at Conf42 Machine Learning 2025 on IoT, acoustic sensing and ML for predictive maintenance.

Scheduled maintenance assumes machines fail on a calendar. Karthikeyan Rajamani, Lead SRE at Thomson Reuters, opened his [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025) talk with a study he attributes to PTC finding that more than 80% of equipment failures are random, which is why preventive schedules alone cannot catch them. His answer is predictive maintenance: cheap IoT sensors, including plain microphones, feeding signal processing and ML models that flag a failure before it becomes downtime.

The talk is an accessible introduction that covers the whole pipeline from sensor to dashboard. If you run services rather than turbines, the structure will still feel familiar: it is observability for things with bearings.

## Three kinds of maintenance

Rajamani lays out the options. Breakdown maintenance reacts after the failure. Preventive maintenance runs on a schedule, like an oil change, quarterly or yearly. Predictive maintenance watches the equipment continuously and acts when the data says something is wrong. The benefits he lists are practical: downtime can be scheduled outside business hours, the technician arrives with the right spare part instead of diagnosing on site, maintenance costs fall, equipment lasts longer, and the failure data goes back to the design team for the next product.

## Why sound is a good signal

Sensors have become cheaper, lower power and more accurate, and can measure vibration, temperature, pressure, humidity and sound in real time. The acoustic angle is the most interesting part. He describes PTC's microphone-based monitoring as non-invasive: you place a microphone on a benign spot on existing machinery, without modifying it, and build an acoustic footprint of normal operation. Combined with vibration and temperature profiles, that multimodal picture is far more specific than any single sensor, and comparing it against previous failures reduces false positives.

## From waveform to prediction

The pipeline has five parts: data acquisition, signal processing, an ML model, edge computing, and feedback for model refinement. Signal processing converts the raw signal into the frequency domain so the model can look at where the peaks are, not just how loud the machine is. Models such as random forests and CNNs are trained to predict anomalies and maintenance needs.

Edge computing earns its place because sensors can sample every second or every few milliseconds. Processing locally and sending only what matters keeps the network from drowning and cuts latency. A supervised feedback loop improves accuracy over time, and the output lands on dashboards and as mobile alerts for service engineers. Any SRE who has tuned an alert to stop paging on noise will recognise the job.

## Where it applies and what gets in the way

Applications span manufacturing lines, energy (turbines and transformers), logistics fleets, automotive, oil and gas, railways and utilities. He cites market growth and studies reporting large reductions in downtime and maintenance costs.

The challenges section is honest. Factories with a "my system is working fine" mindset resist acting before failure. Skills in IoT, data analytics and acoustics are scarce. IoT devices are often fit-and-forget, with no regular updates and expiring certificates, which makes them a security liability. The data volume needs object storage such as Amazon S3. And retrofitting old equipment with no baseline profile takes real homework.

## What comes next

He closes on AR-guided repairs with remote experts, digital twins, models that learn with less supervision, and third-party cloud platforms offering predictive maintenance as a service.

## Who should watch

Engineers new to industrial IoT who want the end-to-end shape of a predictive maintenance system, and SREs curious how their alerting instincts translate to physical equipment. Specialists in vibration analysis will want more depth than an overview gives.

## Related Conf42 talks

- [Transforming manufacturing through AI-driven predictive maintenance](https://www.conf42.com/MLOps_2025_Muruga_Angamuthu_transforming_manufacturing_ai), Muruga Angamuthu, Conf42 MLOps 2025
- [Secure IoT edge architecture: predictive maintenance for medical diagnostic systems](https://www.conf42.com/Internet_of_Things_IoT_2025_Ramakrishna_Ambati_maintenance_predictive_medical), Ramakrishna Ambati, Conf42 Internet of Things 2025
- [Aircraft observability: how digital twins turn flight data into predictive maintenance insights](https://www.conf42.com/Observability_2025_Divakar_Duraiyan_aircraft_digital_twins), Divakar Duraiyan, Conf42 Observability 2025

[Watch Karthikeyan Rajamani's talk](https://www.conf42.com/Machine_Learning_2025_Karthikeyan_Rajamani_iot_accoustic_analysis)

[Watch the talk on YouTube](https://youtu.be/MQv1RS1QCQg).

## Watch the talk

[Revolutionizing Industrial Maintenance: Leveraging IoT and Acoustic Analysis for Predictive Solutions](https://www.conf42.com/Machine_Learning_2025_Karthikeyan_Rajamani_iot_accoustic_analysis) at Conf42 Machine Learning 2025.
