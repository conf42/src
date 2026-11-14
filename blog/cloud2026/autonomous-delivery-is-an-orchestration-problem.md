# Robots, drones and driverless trucks need one modality-agnostic brain

Conf42 Blog, 2026-04-05, updated 2026-11-09. https://www.conf42.com/blog/cloud2026/autonomous-delivery-is-an-orchestration-problem

In short: Cijin Lonappan Kappani of Walmart at Conf42 Cloud Native 2026 on autonomous last-mile and middle-mile delivery and the cloud-edge architecture that runs it.

Last-mile delivery accounts for 40 to 50 percent of total logistics cost, which makes it, in Cijin Lonappan Kappani's words, a structural tax on every e-commerce transaction. At Conf42 Cloud Native 2026, Cijin, Principal Technical Program Manager at Walmart working on drone and autonomous vehicle delivery with partners including Wing, Zipline and DroneUp, explained how sidewalk robots, drones and driverless trucks fit together, and why the hard part is the cloud-native orchestration layer that coordinates them.

It is a practitioner's overview from inside a retailer running these systems, with real deployments named, rather than a code-level tour of one platform.

## Three machines, three sweet spots

- **Sidewalk robots** run on existing pedestrian infrastructure, typically one to five miles from a fulfilment node with payloads around 15 pounds: groceries, pharmacy items, convenience goods. They depend on low-latency 5G or LTE for obstacle detection, remote supervision and routing, so losing connectivity is a failure mode the platform must handle. Curbs, snow and construction make path planning hard, and GPS degrades in urban canyons, so they rely on sensor fusion of lidar, cameras and odometry.
- **Drones** skip ground congestion entirely, targeting delivery in under 30 minutes for light items, typically around five pounds. Weather and regulation are the constraints, and the cloud integration point is unmanned traffic management: real-time airspace conflict resolution, weather monitoring and rerouting.
- **Autonomous trucks** are the most mature, because highway driving on fixed warehouse-to-store routes has far fewer edge cases. Walmart and Gatik run fully driverless box trucks on middle-mile routes in Arkansas, with no safety drivers. Cijin is emphatic that this is production, not a pilot.

## Hand-offs are where it gets hard

The most interesting case is multimodal. In the Serve Robotics and Wing pilot in Dallas, a sidewalk robot picks up packages from a micro-fulfilment node and carries them to an autoloader station, where a drone takes them for the final aerial leg. Each machine does the segment it is good at. The cost is coordination: transfer hand-offs need sub-minute arrival precision, scheduling has to weigh order velocity, robot availability, weather and drone capacity at once, every agent needs a consistent view of state, and when one modality fails the system must reroute without dropping orders. If that sounds like event-driven architecture with shared state and fault tolerance, that is exactly his point.

## Cloud, edge, fleet

The reference architecture has three layers. The cloud orchestration layer is the brain: fleet management, order state, telemetry ingestion, route optimization and remote supervision, horizontally scalable and observable. The edge coordination layer makes the low-latency calls (a robot dodging a pedestrian cannot wait for a cloud round trip) and must keep working on partial connectivity. The fleet layer is the robots, drones and trucks with their own onboard compute, executing locally and reporting state continuously.

His four design principles are the takeaway engineers can use anywhere: abstract the modality so orchestration does not care which vehicle delivers, degrade gracefully so one modality's failure does not cascade, coordinate through events so subsystems scale independently, and keep unified observability so any order can be traced across any agent.

## Regulation is a software requirement

Unlike technical problems, regulation cannot be engineered away. Drones in the US need FAA Part 107 certification, beyond-visual-line-of-sight waivers granted inconsistently by corridor, and now Remote ID. Trucks need state-level permits, with Arkansas and Texas leading. Sidewalk robots face a city-by-city patchwork. The engineering consequence is geofencing that enforces regulatory boundaries in real time, with different rule sets applied per jurisdiction. Weather adds another dependency: when wind grounds drones, the platform must reroute to ground modes and adjust delivery promises dynamically, because static SLAs do not survive weather-dependent fleets.

Walmart evaluates deployments with a four-quadrant risk framework (operational, technical, strategic, market) and takes a portfolio approach across technologies and partners rather than betting on one.

## Who should watch

Engineers building fleet, IoT or logistics platforms, and anyone who likes seeing distributed systems patterns applied to physical machines. If you want the economics of retail automation, the closing section on cost curves and a phased outlook to 2035 covers it; if you want code, this talk does not show any.

## Related Conf42 talks

- [Pavan Boppidi on confidence-gated human-AI logistics systems](https://www.conf42.com/Feature_Flags_2026_Pavan_Boppidi_autonomy_ai_logistics) at Conf42 Feature Flags 2026.
- [Maimoon Saleem on last-mile delivery with cloud computing and IoT](https://www.conf42.com/Cloud_Native_2025_Maimoon_Saleem_logistics_optimization_efficiency) at Conf42 Cloud Native 2025.
- [Chiara Civardi and Petr Aubrecht on robotic applications at the edge](https://www.conf42.com/Internet_of_Things_IoT_2024_Chiara_Civardi_Petr_Aubrecht_robotics_applications_edge) at Conf42 Internet of Things 2024.

[Watch Cijin Lonappan Kappani's talk](https://www.conf42.com/Cloud_Native_2026_Cijin_Lonappan_Kappani_devops_cicd_automation)

[Watch the talk on YouTube](https://youtu.be/rVqMHAPMtew).

## Watch the talk

[Autonomous Delivery and Multi-Modal Fulfillment in Cloud Native Commerce](https://www.conf42.com/Cloud_Native_2026_Cijin_Lonappan_Kappani_devops_cicd_automation) at Conf42 Cloud Native 2026.
