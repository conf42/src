# Driver assistance runs on chips rated in hundreds of TOPS

Conf42 Blog, 2024-01-25. https://www.conf42.com/devops2024/adas-sensors-chips-and-autonomy-levels

In short: Rajesh Reddy (ECARX) at Conf42 DevOps 2024 on ADAS and autonomous driving - the sensors, the compute, the software stack and the L0-L5 levels.

Lane keeping and automatic emergency braking look like small features on a spec sheet; underneath sits a sensor suite, a system-on-chip measured in hundreds of TOPS and a safety-certified software stack. At Conf42 DevOps 2024, Rajesh Reddy, Principal Product Manager at ECARX, gave a compact introduction to advanced driver assistance systems (ADAS) and autonomous driving (AD): what the sensors do, how much compute they need, what the software layers are, and how the five levels of autonomy fit together.

It is an overview talk for people outside the automotive industry, so expect breadth rather than code.

## What counts as ADAS, and what is AD?

ADAS is the suite of technologies that make driving safer and easier: collision warnings, adaptive cruise control and the like. AD is the next step, vehicles that operate without human input. "Think of adas as your car's superpower, which enhances safety and makes driving lot easier," Rajesh Reddy said at Conf42 DevOps 2024.

## The sensor squad

Reddy goes member by member:

- **Long-range radar** watches far down the road so the car can react before a hazard is close.
- **Short-range radar** covers the immediate surroundings: tight spaces, parking, blind spots.
- **Cameras** read traffic signs and lane markings and give a real-time visual feed; **infrared cameras** see in low light.
- **Ultrasonic sensors** catch obstacles at close quarters during low-speed manoeuvres.
- **Lidar** maps the surroundings in 3D with laser beams, for precise navigation in complex environments.

## Features come in packages

Car makers pick functions in three bundles. Safety: front collision warning, autonomous emergency braking, lane departure warning, lane keeping assist, blind spot detection, cross-traffic warnings, traffic sign and traffic light recognition. Comfort: adaptive cruise control, traffic jam and highway assist, curve speed assist, navigated lane changes, highway navigation pilot. Parking: 360-degree around-view monitor, parking distance control, auto, remote and home parking assist. Which bundle a model gets depends on whether it is an entry, mid or premium vehicle.

## How much compute does a car need?

He splits it into three dimensions. CPU: SoCs today reach beyond 100,000 DMIPS, with robotaxi-class applications needing as much as a million. GPU: ADAS needs relatively little, around 0.5 to 1 TFLOPS. Machine learning inference is the big one: automotive SoCs offer from about 5 to 200 INT8 TOPS depending on the vendor, higher-level autonomy can call for around 1,000, and two or more SoCs can be combined to get there.

The chips he cites:

| Chip | Peak AI compute |
|---|---|
| TI TDA4VH | 32 TOPS |
| Mobileye EyeQ Ultra | 176 TOPS |
| NVIDIA Orin | 254 TOPS |
| Horizon Robotics J6 | 560 TOPS |

Each has its own emphasis in his telling: Horizon Robotics on on-chip vision processing at the edge, NVIDIA's Orin and Thor on parallel GPU power for many neural networks at once, TI's TDA4 family on sensor fusion, and Mobileye's EyeQ on vision-based algorithms for features such as lane departure warning and collision avoidance.

## The software stack

Five layers. Fusion merges camera, radar and lidar data into one picture of the surroundings. Perception recognises objects, pedestrians and signs. Planning decides what to do. Middleware, such as the QNX real-time operating system and the AUTOSAR framework, connects hardware and software modules predictably. And functional safety, under standards such as ISO 26262, governs how the whole thing is built to prevent or control failures. For software engineers used to web services, that last layer is the culture shock: the stack is designed around certification, not just uptime.

## Five levels of autonomy

Level 0 is no automation. Level 1 adds basic assistance such as warnings, level 2 driving features such as adaptive cruise control, level 3 conditional automation where the car handles certain scenarios on its own, and level 5 fully self-driving in any environment. Reddy closes on the impact: fewer accidents, smoother traffic, better access for people with disabilities, and lower fuel use and emissions from optimised traffic flow.

## Who should watch

Software and DevOps engineers curious about what runs inside a modern car, and anyone moving into automotive who wants the vocabulary in one sitting. Practitioners already in ADAS will know all of it.

## Related Conf42 talks

- Spandana Sagam and Govardhan Reddy Kothinti on [software for mobility, vehicles and transportation](https://www.conf42.com/DevSecOps_2024_Spandana_Sagam_Govardhan_Reddy_Kothinti_mobility_vehicles_transportation) at Conf42 DevSecOps 2024.
- Utham Kumar on [V2X communication for vehicles](https://www.conf42.com/Golang_2025_Utham_Kumar_v2x_communication_vehicles) at Conf42 Golang 2025.
- Ravinder Katla on [sustainability in vehicle software](https://www.conf42.com/Machine_Learning_2025_Ravinder_Katla_sustainability_vehicle_software) at Conf42 Machine Learning 2025.

[Watch Rajesh Reddy's talk](https://www.conf42.com/DevOps_2024_Rajesh_Reddy_computing_software_vehicles)

## From ECARX

ECARX builds automotive computing platforms and software for car makers.

- [ECARX website](https://www.ecarxgroup.com/)

[Watch the talk on YouTube](https://youtu.be/dmuKqOI_nw8).

## Watch the talk

[Introduction to ADAS and Autonomous Driving](https://www.conf42.com/DevOps_2024_Rajesh_Reddy_computing_software_vehicles) at Conf42 DevOps 2024.
