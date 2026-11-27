# Edge AI for IoT comes down to deploying, updating and shrinking models

Conf42 Blog, 2025-05-07, updated 2026-11-09. https://www.conf42.com/blog/ml2025/edge-ai-iot-deploy-update-compress

In short: Gayathri Jegan Mohan of Microsoft at Conf42 Machine Learning 2025 on running ML at the IoT edge with portable runtimes, OTA updates, quantization and cloud pipelines.

Running inference next to the sensor sounds simple until you have ten thousand sensors from six vendors and a new model to ship. At Conf42 Machine Learning 2025, Gayathri Jegan Mohan, Software Engineer at Microsoft, gave a structured introduction to edge AI for IoT: why inference is moving off the cloud, what breaks when it does, and four practices that keep a fleet of constrained devices manageable.

It is a good first talk on the subject. Engineers already shipping TFLite models to Jetsons will recognize most of it; everyone else gets a clean map.

## Why push inference to the edge at all

In the usual IoT setup, devices send data to the cloud, the cloud runs the model, and the result comes back. Edge AI removes those hops by running a pre-trained model on the device. Jegan Mohan lists the payoffs: lower latency for things like traffic-light control or spotting a failing appliance, less bandwidth, better privacy because raw data does not travel (or cross borders), operation with weak or no connectivity, and lower energy use. Her examples are everyday ones: a surveillance camera flagging anomalies locally, a factory robot inspecting parts without uploading images, a smart speaker recognizing your voice on the device.

Her framing number, from the abstract: by 2025, 75% of enterprise data will be processed at the edge.

## What makes the edge hard

The challenge list is honest. Devices have little compute, memory and storage, and many run on batteries, so a full-size ResNet is out. Pushing updates to a large fleet is hard, and version drift is a real risk. Devices on public networks need secure boot and lightweight secure protocols. Connectivity is intermittent, which complicates syncing results back. Compressed models trade away some accuracy. Observability shrinks to simple logs, because a heavy telemetry stack does not fit. And hardware diversity means every vendor brings its own OS and protocols.

## Four practices for running a fleet

**Deploy for portability.** Use portable model formats such as ONNX or TensorFlow Lite so the same model runs across hardware. Target accelerators with unified runtimes (NVIDIA Jetson, Intel, Arm NPUs) and package model plus dependencies in containers so every device behaves the same way. Walmart is her example here: thousands of store cameras running edge-optimized vision models on compact servers such as NVIDIA Jetson to track inventory and restocking.

**Update like a release, not a hotfix.** Over-the-air updates with version control, A/B rollouts to a slice of devices before the rest, and digital twins to test a new model against a virtual copy of the device first. Tesla's OTA pipeline for Autopilot models, with rollback, is her example.

**Shrink the model on purpose.** Quantization from 32-bit floats to 8-bit integers for smaller, faster inference on something like a Raspberry Pi; pruning insignificant weights and neurons; and knowledge distillation, where a small student model learns from a larger teacher. Google's MobileNet family, built with quantization and pruning for on-phone image classification that works in airplane mode, illustrates the payoff.

**Keep the cloud for the lifecycle.** The cloud does not leave the picture; it moves behind it. Cloud MLOps pipelines (she names Azure ML and AWS SageMaker) retrain on telemetry collected from the edge, CI/CD automates testing and rollout, and the improved model goes back out. Siemens' predictive maintenance on Azure IoT is the example, with a reported cut in machine downtime.

Each practice gets one real-world example, which makes the talk easy to follow.

## Who should watch

Engineers and architects starting an IoT or edge ML project who want the whole problem in one sitting. Teams already running a fleet may find the update and observability sections the most useful checklists. If you came for benchmarks or code, this is not that talk.

## Related talks

- [Madhu Niranjan Reddy Puduru on edge AI for smart camera devices without cloud dependencies](https://www.conf42.com/Internet_of_Things_IoT_2025_Madhu_Niranjan_Reddy_Puduru_vision_edge_processing) at Conf42 IoT 2025
- [Alejandro Cantos with an introduction to MLOps at the edge](https://www.conf42.com/Machine_Learning_2023_Alejandro_Cantos_introduction_mlops_edge) at Conf42 Machine Learning 2023
- [Pradeep Kumar Vattumilli on edge computing and TinyML for autonomous IoT](https://www.conf42.com/Golang_2025_Pradeep_Kumar_Vattumilli_edge_tinyml_ai) at Conf42 Golang 2025

[Watch Gayathri Jegan Mohan's talk](https://www.conf42.com/Machine_Learning_2025_Gayathri_Jegan_Mohan_iot_edge_future)

[Watch the talk on YouTube](https://youtu.be/NMTr3WnmXkg).

## Watch the talk

[Bringing AI to the Edge: How ML is Powering the Future of IoT](https://www.conf42.com/Machine_Learning_2025_Gayathri_Jegan_Mohan_iot_edge_future) at Conf42 Machine Learning 2025.
