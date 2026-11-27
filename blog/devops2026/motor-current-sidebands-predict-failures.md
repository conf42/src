# The sidebands you filter out as noise can predict motor failure

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/motor-current-sidebands-predict-failures

In short: Avinash Sista (MongoDB) at Conf42 DevOps 2026 on four-layer, vectorised motor health monitoring that turns sensor data into predictive maintenance.

Run the current feeding an AC motor through a Fast Fourier Transform and you get the expected harmonics plus small sidebands that most people discard as noise. At Conf42 DevOps 2026, Avinash Sista, a principal at MongoDB who manages system-integrator partnerships in IoT and AI, argued that those sidebands are a signature, and that combining them with design data, sensor reactions and a vectorised learning loop lets you predict which part of a motor is failing before it fails.

Sista is an electrical engineer with a master's in mechanical engineering, and it shows: this is an electro-mechanical reliability talk first and a data platform talk second. It is based on his own research into AC motors, with brushless DC and switched reluctance motors also in scope.

## Commodity parts, expensive failures

Motors are everywhere: dishwashers, washing machines, HVAC, and in industry compressors, conveyors and robotics. They are also commodities, often bought by weight with limited per-unit R&D. When one fails, you get downtime and sometimes catastrophic damage.

Today's protection is mostly threshold alarms (temperature, emergency stop) plus the intuition of an engineer who has listened to motors for years. Sista's critique is that these inputs live in silos. Nobody stitches design specs, electrical signals, temperature, vibration and experience into one model that says when, where and how a motor will fault.

## Four layers of diagnosis

His approach is a multi-layer decision process, mapped onto the motor as an input-process-output block:

1. **Design signature analysis.** How should this motor behave? Torque, RPM, 50 or 60 Hz supply, four-pole or six-pole, no-load versus full-load thermal behaviour. Traditionally checked with circle diagrams in the lab; here digitised as a baseline.
2. **Current signature analysis.** Feed the supply current through an FFT and you expect spikes at 60, 120, 180 Hz and so on. Because every motor is also a generator, back EMF distorts the wave and sidebands appear around those spikes. That pattern is specific to the motor's design, and as the motor ages the sidebands change in amplitude or width. That change is the anomaly to watch.
3. **Reaction analysis.** The output side: heat, vibration, noise and efficiency. His analogy is the kitchen blender in India that you knew was overloaded by its sound and how hot it got, with a sensor doing the listening instead of a person. A rattle in your car is the same diagnostic instinct.
4. **Aging signature analysis.** Combine layers one to three against the baseline to spot the trend, and attribute it: bearing wear, winding losses, resistance changes, insulation breakdown.

## Fix the bearing, not the compressor

His worked example is a motor driving a compressor whose output values started skewing and hampering plant operations. The old response is to swap the compressor, the motor or both. With current signatures describing motor health, reaction data pointing at the application, and design conformance defining expected behaviour, the aging trend tells you which component is degrading, so you can do targeted predictive maintenance before anything breaks.

## Vectors and a learning loop

The data side uses the sensors motors already have, plus soft sensors, and vectorises temperature, vibration and electrical inputs to relate cause and effect. Sista is careful that vectorisation alone doesn't give early detection: it comes from matching against similar measurements and known defects, and gets better as the system learns more failures. That continuous learning loop leans on a document database to store unstructured data, including photos and video, feeding vector models. Given his employer, the document-model choice is unsurprising, but the talk doesn't turn into a product pitch.

He frames the outcome in DevOps terms: data-driven decisions, continuous monitoring and resilient operations, with preventive rather than firefighting maintenance. Research is continuing on purely resistive and more complex loads.

## Who should watch

Engineers working on industrial IoT, predictive maintenance or any telemetry pipeline where domain physics should shape the features. Software people get a clear, friendly explanation of motor-current signature analysis. If your anomaly detection treats every sensor as an anonymous time series, this is a good argument for learning what the signal means.

## Related Conf42 talks

- [Transforming Manufacturing Through AI-Driven Predictive Maintenance](https://www.conf42.com/MLOps_2025_Muruga_Angamuthu_transforming_manufacturing_ai) by Muruga Angamuthu (Techtronic Industries) covers the plant-floor rollout side.
- [Aircraft Observability Revolution: Digital Twins for Predictive Maintenance](https://www.conf42.com/Observability_2025_Divakar_Duraiyan_aircraft_digital_twins) by Divakar Duraiyan (Tata Consultancy Services) does the same for flight data.
- [AIOps in AWS: Choosing the Best Approach for Predictive Maintenance](https://www.conf42.com/Incident_Management_2024_Indika_Wimalasuriya_17_aiops_aws_maintenance) by Indika Wimalasuriya (Virtusa) compares cloud options.

[Watch Avinash Sista's talk](https://www.conf42.com/DevOps_2026_Avinash_Sista_maintenance_industrial_ai)

[Watch the talk on YouTube](https://youtu.be/yb6CF76VLKk).

## Watch the talk

[AI Driven Vectorized Motor Health Monitoring for Reliable Industrial Operations](https://www.conf42.com/DevOps_2026_Avinash_Sista_maintenance_industrial_ai) at Conf42 DevOps 2026.
