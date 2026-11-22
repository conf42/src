# Rust machine vision on the EV line, from battery cells to ADAS

Conf42 Blog, 2025-08-02, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/rust-machine-vision-ev-battery-inspection

In short: Sankar Subramanian of Lucid Motors at Conf42 Rustlang 2025 on Rust-based machine vision for EV manufacturing, covering battery inspection, 3D vision and ADAS calibration.

On an electric vehicle line, a vision system that crashes is a line that stops, and a missed crack in a battery cell is a thermal event waiting to happen. At Conf42 Rustlang 2025, Sankar Subramanian, Staff Engineer at Lucid Motors, walked the whole EV manufacturing flow, from cell inspection to ADAS calibration, and showed where Rust-based machine vision fits at each stage.

Sankar brings more than 20 years in control and automation, across semiconductor lasers, fiber optics and EV manufacturing. The result is a talk that is more about the factory than the language, which is exactly why it is interesting.

## Why EVs make inspection harder

EVs pack more components more densely, need micron-level precision, and carry battery safety risks that push manufacturers towards inspecting every part. At line speed, Sankar argued, traditional inspection methods cannot keep up, and the system that replaces them has to be fast and must not fall over in a 24/7 plant where downtime costs add up by the minute.

His Rust case maps to the floor: memory safety to avoid crashes in production, fearless concurrency to process several camera feeds at once without data races, near-C performance to handle high-resolution images at line speed, and FFI to integrate with existing C and C++ vision libraries and ML frameworks.

## The inspection pipeline

The core flow has four stages. Image acquisition captures multiple views of each part at line speed. Pre-processing uses SIMD-optimized Rust for real-time noise reduction and contrast enhancement. AI-based classification runs custom neural networks that catch subtle defects threshold-based systems miss. Automated response rejects the part, flags rework, or adjusts the process based on the defect class.

Sankar reported a clear increase in defect detection rate over conventional machine vision, and stressed that the Rust system avoided the crashes common in C and C++ environments.

## Battery cells and packs get the most attention

The battery section is the most detailed. Electrode alignment for anode and cathode, measured with structured light at sub-millimetre precision. Surface defect detection for microscopic cracks, dents and contamination that could lead to thermal runaway. Electrolyte fill verification with IR imaging. Pack-level thermal monitoring with IR cameras to spot hot spots during formation cycling, with Rust handling the real-time thermal mapping.

At module level he added wire bond assessment, laser weld verification, thermal imaging during module pulsing to find resistance anomalies, and 3D profile mapping after assembly.

## 3D vision, traceability and calibration

Beyond inspection, Sankar covered 3D vision for assembly automation (time-of-flight cameras guiding robots, stereo disparity mapping in optimized Rust, laser triangulation, dense point cloud processing), and integration with the manufacturing execution system: OCR and barcode traceability for every component, assembly sequence verification, and automated documentation for compliance and recall readiness.

At the end of the line, ADAS calibration validates forward cameras, lidar, radar and surround-view cameras within a tight time budget per vehicle, and vision data feeds a factory digital twin for predictive maintenance. The ML side uses transfer learning to cut training data needs, with Rust FFI into TensorFlow and ONNX Runtime and inference deployed on edge devices beside the line.

## Who should watch

Engineers in manufacturing, robotics and industrial automation, and Rust developers curious what a real factory pipeline demands. It is a systems tour rather than a code session; there are no crate-level details, but the domain picture is rich.

## Related Conf42 talks

- [Platform Engineering Lessons from Automotive Manufacturing](https://www.conf42.com/Platform_Engineering_2025_Nikunj_Karoliya_complex_automotive_manufacturing) by Nikunj Karoliya: the software platform behind an auto plant.
- [Edge AI for Smart Camera IoT Devices](https://www.conf42.com/Internet_of_Things_IoT_2025_Madhu_Niranjan_Reddy_Puduru_vision_edge_processing) by Madhu Niranjan Reddy Puduru: image processing on the device, no cloud required.
- [A Production Computer Vision Verification System for Warehouse Receiving](https://www.conf42.com/Cloud_Native_2026_Anton_Solomonov_computer_vision_verification) by Anton Solomonov: vision-based verification in a different industry.

[Watch Sankar Subramanian's talk](https://www.conf42.com/Rustlang_2025_Sankar_Subramanian_memory_safety_zero)

[Watch the talk on YouTube](https://youtu.be/47iC6_1xywU).

## Watch the talk

[AI-Powered Machine Vision in Rust: Transforming EV Manufacturing Quality & Automation](https://www.conf42.com/Rustlang_2025_Sankar_Subramanian_memory_safety_zero) at Conf42 Rustlang 2025.
