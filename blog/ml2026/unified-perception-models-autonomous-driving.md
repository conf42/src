# One shared perception model beats a stack of single-task models

Conf42 Blog, 2026-02-17, updated 2026-11-09. https://www.conf42.com/blog/ml2026/unified-perception-models-autonomous-driving

In short: Sowmiya Narayanan Govindaraj (Motional) at Conf42 Machine Learning 2026 on unified, transformer-based perception that fuses camera and lidar for self-driving.

A self-driving stack that runs one model for detection, another for segmentation and a third for depth is reading the same scene three times and never agreeing on what it saw. At Conf42 Machine Learning 2026, Sowmiya Narayanan Govindaraj, Senior Machine Learning Engineer at Motional, explained why the autonomous vehicle industry is moving to unified end-to-end perception models, and what changes once those models leave the lab.

It is a compact, conceptual talk from someone who takes perception models from research into safety-critical deployment. No code, but a clear architecture and a useful list of production lessons.

## Fragmented stacks duplicate work and cascade errors

The classic perception pipeline trains separate models per task, and sometimes per sensor. Each processes the same inputs independently, which means duplicated computation, higher latency and errors that cascade from one stage to the next. The deeper problem, as Govindaraj frames it, is that the modules are optimised locally rather than globally, so the system never forms a cohesive understanding of the scene and becomes brittle and hard to maintain over time.

## Shared encoders, light task heads

The unified alternative trains one system that jointly learns spatial, semantic and temporal representations. All sensors feed shared encoders, and lightweight heads branch off for each output. Because features are shared, improving one task helps the others: segmentation informs depth, detection benefits from both. Fewer models, better accuracy.

Transformers make this practical. Self-attention captures long-range context across the scene, cross-modal attention aligns camera appearance with lidar geometry without hand-written fusion rules, and token representations cope with different sensor resolutions. The architecture has three parts: a shared backbone, cross-modal alignment into a common latent space, and temporal fusion over multiple frames, since one frame can be ambiguous but motion reveals intent. Images bring texture and semantics, point clouds bring precise geometry, and training 2D and 3D together gives steadier boxes and depth for tracking and planning downstream.

## Sensors fail unevenly, so fusion has to adapt

The most practical lesson: rain and darkness hurt cameras, while fog and sparse returns hurt lidar. Static fusion weights cannot handle that, so the model uses adaptive attention that weights each sensor by its current reliability and leans on the others when one degrades. The goal is graceful degradation rather than sudden failure.

Outside controlled settings come weather, geography, domain shift and the long tail: construction zones, emergency vehicles, unusual pedestrian behaviour. These matter most for safety and appear least in training data, so the team relies on targeted collection, balanced sampling and continual learning. For new cities, domain adaptation techniques such as adversarial feature alignment, test-time adaptation and rapid fine-tuning keep the model adjusting. Perception, Govindaraj says, is not something you train once and freeze.

## Labels are the bottleneck, so learn without them

Labelling driving data at scale is very expensive, so self-supervised methods (contrastive alignment, temporal consistency, cross-sensor reconstruction) let training scale on unlabelled data. That leads into foundation models pre-trained on large driving datasets, with lightweight heads for detection, tracking or prediction, and zero-shot generalisation to scenarios nobody labelled.

The engineering payoff is a single forward pass: lower latency, simpler deployment and easier debugging. It is rare for an architecture change to cut complexity and improve accuracy at once, and the talk ties both back to safety through fewer disengagements and more consistent behaviour.

## Who should watch

ML engineers in robotics, autonomy or any multi-sensor system who are weighing a multi-task model against a zoo of specialists. Newcomers get a clear map of the modern perception stack; specialists get a short list of what tends to break in deployment.

## Related Conf42 talks

- [Introduction to ADAS and Autonomous Driving](https://www.conf42.com/DevOps_2024_Rajesh_Reddy_computing_software_vehicles) by Rajesh Reddy (ECARX) is the primer if you want the vehicle context first.
- [Optimizing Real-Time AI Inference at the Edge: Accelerating Autonomous Vehicle Safety and Efficiency](https://www.conf42.com/Golang_2025_Murali_Krishna_Reddy_Mandalapu_ai_inference_edge) by Murali Krishna Reddy Mandalapu (Renesas Electronics) covers running these models on the car.
- [AI-Driven Safety Innovations: Advancing Autonomous Vehicle Technology Through Real-Time Intelligence](https://www.conf42.com/Internet_of_Things_IoT_2024_Rajesh_Kamisetty_ai_safety_autonomous) by Rajesh Kamisetty (S&P Global) adds the safety-systems angle.

[Watch Sowmiya Narayanan Govindaraj's talk](https://www.conf42.com/Machine_Learning_2026_Sowmiya_Narayanan_Govindaraj_risk_modeling_assessment)

[Watch the talk on YouTube](https://youtu.be/CASEFDC9FvQ).

## Watch the talk

[Towards Unified Perception: End-to-End Scene Understanding Models for Autonomous Driving](https://www.conf42.com/Machine_Learning_2026_Sowmiya_Narayanan_Govindaraj_risk_modeling_assessment) at Conf42 Machine Learning 2026.
