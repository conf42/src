# EV charging networks need cloud-native design to keep up

Conf42 Blog, 2025-10-06, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/cloud-native-design-for-ev-charging-networks

In short: Preeti Sali (Ford Motor Company) at Conf42 Kube Native 2025 on microservices, predictive maintenance, smart routing and V2G for EV charging.

Range anxiety is mostly a data problem: drivers don't know whether the charger ahead works or is free. At Conf42 Kube Native 2025, Preeti Sali, Senior Technical Program Manager at Ford Motor Company, laid out how cloud-native design (microservices, Kubernetes and open APIs) turns EV charging from a patchy network of boxes into a system that predicts failures, routes drivers and talks to the grid.

It is a vision-and-architecture talk from a program manager with an electrical engineering background, aimed at the why and the what more than the YAML.

## Adoption is outrunning infrastructure

Preeti's starting point is the gap. She cites 14 million EVs sold globally last year, nearly one in five cars sold worldwide, and drivers who expect chargers to be as reliable as gas stations always were. The goal, in her framing, is smarter chargers, not merely more of them.

She names three hurdles in today's networks:

- scalability: traditional networks weren't designed for exponential growth or global coverage
- grid integration: legacy systems handle dynamic load management and renewables poorly
- user experience: patchy availability, poor visibility and too much downtime

## The cloud-native answer is the usual one, applied somewhere new

The architecture will look familiar to anyone at a Kubernetes conference. Microservices split the system into payments, routing, user interfaces and the rest. Kubernetes orchestrates and scales them as demand spikes. Open APIs connect vehicles, utilities and third-party apps. What makes it interesting is the domain: the services sit between cars, drivers and a power grid.

## Predict failures, route drivers, spread the load

Reliability gets the first application. With predictive maintenance, IoT sensors monitor charger health, machine learning predicts failures, and cloud systems schedule repairs, which she says can cut downtime by as much as 40%. Fewer surprises for drivers, better use of technicians.

Convenience comes next. Real-time charger status and queue lengths feed routing that sends drivers to the best station by traffic, charging speed and availability. Distributed load balancing uses chargers evenly while easing grid strain. The pay-off is the one in the title of most EV marketing decks: drivers know before they arrive.

Energy management is the third. Cloud-native scheduling shifts sessions to off-peak times using pricing, grid conditions and user preferences, cheaper for consumers and gentler on the grid.

## Cars as batteries

The most ambitious part is vehicle-to-grid (V2G). Treat millions of parked EVs as distributed storage: absorb excess solar or wind when supply is high, feed power back when demand spikes. Preeti's argument is that only a cloud-native platform can orchestrate that at scale, and it is where mobility and energy systems converge.

## Roll it out in waves

Scaling, she says, needs phases: core charging platform first, Kubernetes for horizontal scaling across sites, then advanced features like V2G and AI-driven optimisation once the network is stable. She points to the International Energy Agency projection of roughly four times as many public chargers needed by 2030 as the reason the approach has to be operationally simple. Analytics, edge computing for local low-latency decisions, and machine learning that keeps improving routing and maintenance predictions sit underneath it all.

## Who should watch

Engineers and product people working on EV, energy or IoT platforms who want a structured map of where cloud-native patterns apply, and Kubernetes engineers curious about a domain where a failed pod might strand a driver. Expect a framework, not an implementation.

## Related Conf42 talks

- [Building Robust V2X Communication Networks in Go](https://www.conf42.com/Golang_2025_Utham_Kumar_v2x_communication_vehicles) covers the connected-vehicle networking underneath.
- [Transforming Fleet Management with AI, IoT, and Kubernetes](https://www.conf42.com/Cloud_Native_2025_Vamsi_Anumolu_fleet_iot_optimization) applies a similar stack to fleets.
- [Driving Sustainability: Efficient Power Moding in Vehicle Software](https://www.conf42.com/Machine_Learning_2025_Ravinder_Katla_sustainability_vehicle_software) looks at energy use inside the car.

[Watch Preeti Sali's talk](https://www.conf42.com/Kube_Native_2025_Preeti_Sali_ev_charging_infrastructure)

[Watch the talk on YouTube](https://youtu.be/AiN_W4Av6RA).

## Watch the talk

[Cloud-Native EV Charging: Scalable, Smart Infrastructure for Electric Mobility](https://www.conf42.com/Kube_Native_2025_Preeti_Sali_ev_charging_infrastructure) at Conf42 Kube Native 2025.
