# Fraud checks in milliseconds, a five-layer Rust pipeline for gig apps

Conf42 Blog, 2025-08-17. https://www.conf42.com/blog/rustlang2025/real-time-fraud-prevention-gig-platforms-rust

In short: Prabhakar Singh of Meta at Conf42 Rustlang 2025 on real-time fraud prevention for gig platforms in Rust, with Tokio, Candle and petgraph.

On a food delivery or ride-sharing app, the money leaves the moment the job is done, so a fraud check that is late is a fraud check that did not happen. At Conf42 Rustlang 2025, [Prabhakar Singh](https://www.conf42.com/Rustlang_2025_Prabhakar_Singh_memory_safety_systems), a software engineer at Meta, walked through a five-layer fraud prevention architecture for gig platforms, written end to end in Rust, including the ML inference.

## Why gig fraud is harder than bank fraud

"Fraud prevention in gig platforms is a game of millisecond." Singh's point is that every constraint is tighter than in banking. Approve a transaction slowly and the customer abandons the order or the driver assignment times out. Workers and customers are scattered across cities and countries, so fraud patterns vary by geography and change weekly. Payouts are instant, with no hold period to investigate. And the models have to analyse thousands of transactions a minute without choking.

The attacks he lists will look familiar: account takeover with leaked credentials, synthetic identities stitched from real and fake details, driver-customer collusion to fake trips, GPS spoofing, and stolen cards used for instant payouts.

## Five layers, each a safety net

The architecture stacks five detectors, each catching what the others miss:

1. **Stream processing** with Tokio, ingesting transactions asynchronously.
2. **Rules** using Rust pattern matching for known signals, such as the same card used in three countries within an hour.
3. **Statistical anomaly detection** with time-series models for unusual spikes or dips in behaviour.
4. **ML classification** with Candle, Hugging Face's pure-Rust ML framework, which imports models from PyTorch or TensorFlow via ONNX and runs on CUDA or Metal.
5. **Graph analysis** with petgraph, looking for connected components, centrality and structural similarity.

Two implementation details made the biggest difference, he said: Tokio's async streams, and zero-copy deserialization with Serde so JSON or protobuf is parsed straight from bytes. Those are what keep the pipeline inside its latency budget.

## No Python in production

Running inference in Candle means the whole pipeline stays in one memory-safe language: no language boundary, no GIL and no extra process hop. It is the most opinionated part of the talk and the most interesting, because most fraud stacks still keep Python for the model.

## The graph catches the ring

The graph layer has the best story. A group of 32 drivers and 18 customers ran a fake-order scam for weeks without tripping the standard ML models; graph analysis in petgraph surfaced them as a cluster. Fraud rings are relationships, and per-transaction features cannot see them.

## The numbers he reported

From a major food delivery company's production benchmarks, he reported Rust at 93% of C++ performance, 6.2x faster than Java and 2.4x faster than Python with TensorFlow, with tail latency consistently under 35 ms and much lower CPU use than Python. In a ride-sharing case, a platform losing about $3.2 million a month to GPS spoofing and fake identities replaced its Python fraud stack with Rust microservices, WebAssembly rule modules and Candle, and saw 87% less fraud loss, 65% fewer false positives and 99.98% uptime over 12 months. The companies are not named.

He also covers privacy-preserving techniques (homomorphic encryption, federated learning, differential privacy, secure enclaves) and a roadmap toward behavioural biometrics and SHAP or LIME-style explanations in Rust.

## Who should watch

Fraud, risk and payments engineers on marketplace platforms, and ML engineers curious whether Rust-native inference is ready for production. The petgraph section is worth it on its own.

## Related Conf42 talks

- [Advancing Financial Fraud Detection with Graph Databases](https://www.conf42.com/Machine_Learning_2025_Venkateswarlu_Boggavarapu_fraud_detection_db_graph) by Venkateswarlu Boggavarapu (JPMorganChase) at Conf42 Machine Learning 2025.
- [AI-Powered Payment Systems: Balancing Security and Experience Through Intelligent Fraud Prevention](https://www.conf42.com/Large_Language_Models_LLMs_2025_Arpit_Mittal_payment_security_fraud) by Arpit Mittal (PayPal) at Conf42 Large Language Models 2025.
- [Harnessing Machine Learning to Combat E-commerce Fraud](https://www.conf42.com/Machine_Learning_2025_Surendra_Lakkaraju_ecommerce_fraud) by Surendra Lakkaraju (Amazon) at Conf42 Machine Learning 2025.

[Watch Prabhakar Singh's talk](https://www.conf42.com/Rustlang_2025_Prabhakar_Singh_memory_safety_systems) or the [YouTube recording](https://youtu.be/O78C-GDKd-s).

## Watch the talk

[Building Real-Time AI Fraud Prevention Systems for Gig Platforms in Rust](https://www.conf42.com/Rustlang_2025_Prabhakar_Singh_memory_safety_systems) at Conf42 Rustlang 2025.
