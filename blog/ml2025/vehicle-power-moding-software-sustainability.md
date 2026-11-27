# Your parked car is still burning power, and software can fix it

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/vehicle-power-moding-software-sustainability

In short: Ravinder Katla, infotainment integration engineer at General Motors, at Conf42 Machine Learning 2025 on power moding across a vehicle's ECUs.

Charge an electric car to 280 miles of range, leave it in the garage overnight, and it can show 270 in the morning. Ravinder Katla, an advanced infotainment systems integration engineer at General Motors with 12 years across embedded, firmware and integration roles, explained at [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025) where that missing range goes: dozens of electronic control units that keep drawing power when nobody is driving. His case is that power moding, the software that decides which ECUs are awake and when, is one of the cheapest sustainability levers a carmaker has.

It is an engineer's walkthrough from inside the industry rather than an ML talk. AI shows up mainly as the next step for power management, and the talk does not describe GM's internal implementation.

## A car is 16 to 32 computers with opinions

Katla starts with the architecture. A modern vehicle has roughly 16 to 32 ECUs depending on the manufacturer, each owning a function: the body control module handles lighting, brakes and other body functions, others handle infotainment, telematics and so on. Each draws power differently, and some need power constantly. The power states that matter are propulsion (driving), run, and sleep, and the problem lives in sleep: a parked car whose modules keep running background work drains the battery and shortens its life.

## Sense, analyse, adjust, repeat

His model for power moding has four steps. Environmental sensing: monitor usage patterns, driver behaviour and conditions. Real-time analysis: measure how much each component draws in each power state. Dynamic adjustment: rebalance power between ECUs, especially in sleep. Continuous optimisation: keep cutting consumption as data accumulates.

For EVs, the benefits are efficiency, range (he notes that HVAC alone noticeably affects range) and battery lifespan, which is also why manufacturers recommend charging to 80%. For combustion vehicles, less electrical load means less fuel burned to generate it; he cites fuel consumption reductions of a few percent and CO2 savings per vehicle per year. Multiply small per-car gains by millions of cars a year and the numbers stop being small.

## Updates while you sleep

The implementation section is the most concrete. Over-the-air updates and ECU firmware upgrades often have to run while the vehicle sleeps, so power moding has to allow critical updates without leaving the car awake all night. His rollout model goes from software updates on a test fleet, through power management protocol integration, to algorithm tuning from fleet data, driving patterns and environment, then a monitoring period (he gives 12 months as an example) to find which ECUs consume the most and verify improvements.

## Some modules must never nap

The challenges are what make this harder than "turn things off". ECUs come from different suppliers with different mechanisms, and they talk to each other and to the outside world, such as the telematics module reaching carrier networks, so a unified power model is genuinely hard. Safety-critical functions, such as theft detection, crash response or an alarm when a door opens, have to stay awake, and ISO 26262 functional safety requirements must be respected across every power transition. Cybersecurity functions that prevent unauthorised control also stay on. Older platforms may lack the hardware for advanced power states, so retrofits raise costs.

He calls for standardised ECU power management architectures across manufacturers and suppliers, and cross-industry working groups with semiconductor and software companies.

## Where AI comes in

The future section is where the ML angle appears. Today's power modes are discrete states triggered by predefined conditions. Next comes AI-driven optimisation that asks, per ECU, whether the power it is drawing is necessary right now and shuts it down if not; vehicle-to-everything integration for coordinated power with infrastructure and other vehicles; and distributed intelligence where each component decides for itself whether to wake. His key takeaway: unlike hardware improvements, this ships through software updates to cars already on the road.

## Who should watch

Embedded and automotive software engineers, and anyone in IoT who has to keep a battery-powered device both responsive and asleep. ML practitioners looking for models will find the AI part brief; the systems problem is the reason to watch.

## Related Conf42 talks

- [Scalable HIL architecture: observability-driven validation in software-defined vehicles](https://www.conf42.com/Observability_2026_Sumaiyya_Fatima_automotive_embedded_simulation), Sumaiyya Fatima, Conf42 Observability 2026
- [Building robust V2X communication networks in Go](https://www.conf42.com/Golang_2025_Utham_Kumar_v2x_communication_vehicles), Utham Kumar, Conf42 Golang 2025
- [Green DevOps: building sustainable software](https://www.conf42.com/DevOps_2024_Neel_Shah_green_sustainable_software), Neel Shah, Conf42 DevOps 2024

[Watch Ravinder Katla's talk](https://www.conf42.com/Machine_Learning_2025_Ravinder_Katla_sustainability_vehicle_software)

[Watch the talk on YouTube](https://youtu.be/X42hfggfHx4).

## Watch the talk

[Driving Sustainability: Environmental Benefits of Efficient Power Moding in Vehicle Software](https://www.conf42.com/Machine_Learning_2025_Ravinder_Katla_sustainability_vehicle_software) at Conf42 Machine Learning 2025.
