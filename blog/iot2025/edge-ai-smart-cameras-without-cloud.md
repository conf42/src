# Smart cameras that think locally and only send the verdict

Conf42 Blog, 2025-11-30, updated 2026-11-09. https://www.conf42.com/blog/iot2025/edge-ai-smart-cameras-without-cloud

In short: Madhu Niranjan Reddy Puduru of Synchronoss at Conf42 IoT 2025 on running quantized neural networks on IoT cameras to cut bandwidth, latency and battery drain.

A camera that streams every frame to the cloud so a server can say "person detected" is paying a lot of bandwidth for one sentence. At Conf42 Internet of Things (IoT) 2025, Madhu Niranjan Reddy Puduru, Software Engineering Manager at Synchronoss Technologies, made the case for edge AI on smart cameras: optimize the model, run inference next to the sensor, and ship only events.

This is one of the denser talks of the event, a full pipeline from model compression to frame buffers to joules per frame, with case studies at the end.

## The cloud-first camera does not scale

Madhu lists the bottlenecks of cloud-only vision: bandwidth that climbs with every camera added, latency from the network round trip, privacy exposure from shipping raw video, and compute plus storage bills that become unsustainable across dozens or hundreds of devices. Construction sites and rural deployments make it worse, since good connectivity is the first thing they lack.

Moving inference onto the device flips that. In his numbers, sending only events cuts bandwidth use by about 85%, battery life improves four to five times because the radio does less, and local processing gets frames done in under 50 milliseconds. The raw video never leaves the camera, which matters for homes, public spaces and regulated industries.

## Shrinking the model is a three-stage job

The optimization pipeline is the core of the talk:

1. **Architecture selection.** Start from families built for constrained hardware, such as MobileNet V3 and SqueezeNet, or lightweight encoder-decoder networks with residual connections that land at a few megabytes.
2. **Quantization and compression.** Convert FP32 weights to 8-bit integers for a fourfold size reduction and faster, lower-power inference, with accuracy loss he puts usually under 2%. Knowledge distillation and pruning trim further.
3. **Platform-specific compilation.** TensorFlow Lite for ARM, the Edge TPU compiler for Google Coral, Qualcomm's toolchain for Hexagon, with graph optimization, operator fusion and memory layout tuning so each operation lands on the best available CPU, NPU or TPU.

He is blunt about why CPUs alone fall short: general-purpose chips are not built for the matrix math, while NPUs and TPUs bring parallel multiply engines and optimized memory paths. Hardware support spans 512 MB to 1 GB ARM Cortex boards, Raspberry Pi 3 and 4 in the middle, and Coral, Hexagon and NVIDIA Jetson at the top.

## The real-time loop, budgeted in milliseconds

To hold 30-plus frames per second, frames land in a ring buffer so a busy processor never drops them. Preprocessing (resize, colour adjustment, normalization) uses SIMD and should stay under about 10 milliseconds. Inference on mid-range hardware takes roughly 30 to 45 milliseconds. Post-processing filters noise, applies thresholds and turns raw outputs into something an app can act on.

## Memory, not math, eats the battery

The energy section has the most surprising detail: he notes that a DRAM access costs on the order of 100 to 200 times more energy than the arithmetic itself, so compressing models and reusing buffers pays off more than people expect. Add adaptive scheduling (run inference more often when there is motion, idle the radio otherwise) and he reports 60 to 70% energy savings against cloud-based setups. Per frame, an ARM CPU uses 0.5 to 0.8 joules, accelerators drop that to 0.1 to 0.2, while continuous cloud streaming can reach 3 joules. The optimized model itself is around 600 KB, with 4 to 8 MB of total memory including buffers.

The case studies make it concrete: a smart doorbell on a Raspberry Pi 3 with 72% less bandwidth and 4.25 times the battery life, and an industrial defect detection prototype with 50-plus cameras flagging anomalies in under 100 milliseconds while cutting transmitted data by over 90%. He closes with federated learning and cameras that share workloads as next steps.

## Who should watch

Embedded and ML engineers shipping vision on battery-powered or bandwidth-starved devices, and product owners deciding between cloud and edge inference. If you have never quantized a model, this is a good map of the steps; if you have, the energy and memory numbers are the part to steal.

## Related talks

- [Pradeep Kumar Vattumilli on edge computing and TinyML for autonomous IoT](https://www.conf42.com/Golang_2025_Pradeep_Kumar_Vattumilli_edge_tinyml_ai) at Conf42 Golang 2025.
- [Chiara Civardi and Petr Aubrecht on robotic applications at the edge](https://www.conf42.com/Internet_of_Things_IoT_2024_Chiara_Civardi_Petr_Aubrecht_robotics_applications_edge) at Conf42 IoT 2024.
- [Tim Spann and David Kjerrumgaard on the FLiPN stack for edge AI](https://www.conf42.com/Internet_of_Things_IoT_2023_Tim_Spann_David_Kjerrumgaard_flipn_stack_edge_ai_flink_nifi_pulsar) at Conf42 IoT 2023.

[Watch Madhu Niranjan Reddy Puduru's talk](https://www.conf42.com/Internet_of_Things_IoT_2025_Madhu_Niranjan_Reddy_Puduru_vision_edge_processing) from [Conf42 IoT 2025](https://www.conf42.com/iot2025).

[Watch the talk on YouTube](https://youtu.be/2Ot50kFPT1k).

## Watch the talk

[Edge AI for Smart Camera IoT Devices: Real-Time Image Processing Without Cloud Dependencies](https://www.conf42.com/Internet_of_Things_IoT_2025_Madhu_Niranjan_Reddy_Puduru_vision_edge_processing) at Conf42 Internet of Things (IoT) 2025.
