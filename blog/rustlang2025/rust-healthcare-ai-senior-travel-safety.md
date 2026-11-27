# Rust from wearable to hospital, a health platform for older travellers

Conf42 Blog, 2025-08-21. https://www.conf42.com/blog/rustlang2025/rust-healthcare-ai-senior-travel-safety

In short: Raphael Shobi Thomas at Conf42 Rustlang 2025 on a Rust healthcare AI stack for senior travellers, from no_std biosensors to WebAssembly translation.

By 2030, about 703 million travellers worldwide will be 60 or older, and many carry chronic conditions into places where they do not speak the language. At Conf42 Rustlang 2025, [Raphael Shobi Thomas](https://www.conf42.com/Rustlang_2025_Raphael_Shobi_Thomas_memory_safety_code), a senior software engineer and independent researcher, presented a health and safety platform for those travellers with Rust at every layer: biosensor firmware, data pipelines, risk models, in-browser translation and medical records.

## One language from the sensor to the cloud

The pitch for Rust is the usual trio (memory safety, native performance, compile-time thread safety) plus one that matters a lot here: cross-compilation to Windows, Linux, embedded targets, iOS and Android. A single language across devices is a real simplification when the same health record moves from a wrist to a hospital.

He described the platform handling 2,847 concurrent users, each with more than 47 health variables, at sub-millisecond latency, operating under GDPR across 34 countries.

## Firmware that survives bad connectivity

The embedded layer runs `no_std` Rust with embedded-hal on biosensors, which means no standard library, no OS services and tight memory. On top sits a custom protocol built for poor or intermittent connectivity: data is buffered locally and forwarded when the link returns, end-to-end cryptographic checks guard against tampering, and medical data gets priority. That is the right design for a traveller who walks out of mobile coverage mid-arrhythmia.

## The data and ML pipeline

On the server side, Tokio handles continuous health streams, zero-copy parsing reads biosensor data straight from byte buffers, and a custom Serde serialization pipeline processes medical records about 340% faster than a comparable Python implementation, by his measurement. Schema evolution relies on Rust's type system to keep old and new data formats compatible.

Risk assessment uses Candle and the tch-rs bindings, plus ONNX Runtime for pre-trained models on CPU or GPU. The predictor shares the model across threads behind `Arc` and `Mutex`, a deliberately simple pattern for safe concurrent access, and evaluates around 150 risk factors per assessment.

## Translation that never leaves the device

The WebAssembly piece is the most interesting design choice. Medical terminology translation runs as Rust compiled to WebAssembly in the browser or on the device, covering 23 languages at a reported 94% accuracy, with about 60% lower latency than server-side translation. Sensitive health data never goes to a server just to be translated.

Records use the Substrate framework to log every access on a blockchain, with patients managing permissions on chain and smart contracts enforcing consent.

## The Portugal scenario

His case study ties it together: a 72-year-old traveller in rural Portugal, a sensor detecting an irregular heart rhythm and elevated blood pressure, the model flagging a potential cardiac event with 92% confidence, the system finding the nearest medical facility, translating the medical history into Portuguese and sharing verified records with the receiving hospital.

## The honest part

He is upfront about the costs: few medical-domain crates compared with Python or Java, FFI work to reach existing healthcare systems, slow certification under GDPR, HIPAA and MDR for new tech, long early build times, and the ownership learning curve. His answers were custom domain crates, type-safe bindings, compliance checks in CI/CD, build tuning and team training.

## Who should watch

Engineers building health, wearable or edge-AI systems who want to see one Rust stack stretched from firmware to the browser. Compliance-minded teams will appreciate the challenges section.

## Related Conf42 talks

- [Building Resilient Healthcare Platforms at Scale: Engineering AI-Powered Solutions for 700M+ Global Senior Travelers](https://www.conf42.com/Platform_Engineering_2025_Raphael_Shobi_A_T_solutions_senior_travelers) by Raphael Shobi A T (ATPCO) at Conf42 Platform Engineering 2025.
- [Rust in Edge Computing: Enhancing Performance and Security](https://www.conf42.com/Rustlang_2024_Venukumar_Chirlawar_edge_computing_security) by Venukumar Chirlawar (Amazon) at Conf42 Rustlang 2024.
- [Transforming Healthcare Security: A Data-Driven Approach to Zero Trust and Digital Resilience](https://www.conf42.com/Python_2025_Avinash_Mavireddi_healthcare_security_resilience) by Avinash Mavireddi (CareDx) at Conf42 Python 2025.

[Watch Raphael Shobi Thomas's talk](https://www.conf42.com/Rustlang_2025_Raphael_Shobi_Thomas_memory_safety_code) or the [YouTube recording](https://youtu.be/Ms-vcA_96sI).

## Watch the talk

[Building High-Performance Healthcare AI Systems in Rust: A Senior Travel Safety Platform](https://www.conf42.com/Rustlang_2025_Raphael_Shobi_Thomas_memory_safety_code) at Conf42 Rustlang 2025.
