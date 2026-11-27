# Serverless ML inference pays off until the cold start bites

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/serverless-ml-inference-tradeoffs

In short: Shreya Gupta of the University of Southern California weighs serverless AI deployment at Conf42 Observability 2025, from platform benchmarks to cold starts.

Thirty-eight dedicated servers running at about a third of their capacity is the kind of number that makes a finance team ask questions. At Conf42 Observability 2025, Shreya Gupta of the University of Southern California made the case for serverless AI, where ML models run as stateless functions that scale with demand and bill only for execution time. She backs it with benchmark figures, two industry case studies and, to her credit, a full section on where serverless falls over.

The numbers in the talk come from the studies and case reports she presents; treat them as the speaker's sources rather than your next SLA.

## Event in, prediction out

Gupta's architecture is the standard serverless loop applied to ML. Event sources (an API request, a data change, a scheduled job) trigger function containers that hold the model code. Because each invocation is stateless, the platform can run them in parallel and scale automatically, while managed services handle authentication, storage and monitoring. Her analogy: power is only on while you hold the light switch.

The implementation cycle is model encapsulation (package the model in a function, usually behind an HTTP inference endpoint), deployment with its trigger configuration, execution, and automatic scaling up and down. She notes that models from 75 MB up to 1.8 GB are being served this way.

## The platform choice is mostly a cold start choice

The most practical slide compares the big clouds using benchmark studies with identical models (ResNet-50, BERT base, YOLOv4). In those numbers, Google Cloud Functions had the lowest average inference latency for image classification at 112 ms and the fastest cold start, AWS Lambda followed at 136 ms with SnapStart helping Java cold starts and GPU support limited to T4, Azure Functions had the most consistent cold starts plus container-based GPU support, and IBM Cloud Functions trailed on both counts without direct GPU support.

The lesson she draws is about cold starts: the delay when a function wakes after idling matters most for GPU-accelerated functions, so your latency sensitivity should drive the platform pick.

## Two migrations, told with numbers

The case studies are where the cost story lives. A global investment bank moved risk analysis off those 38 underused servers over about four and a half months; the talk reports 68.2% lower infrastructure cost and average risk-analysis latency falling from 8.2 to 3.1 seconds, plus better audit trails for regulators. A healthcare diagnostics provider, previously waiting an average of 86 days to expand capacity, moved containerised imaging models to serverless over seven months; model update cycles reportedly dropped from 36 days to 4.8, with autoscaling handling swings from 50 to 5,000 images an hour without manual intervention.

## Where serverless still hurts

Gupta lists the limits plainly. Cold starts for complex deep learning models can reach 6.2 seconds. Memory caps constrain model size. Execution time limits cut off long-running jobs. Vendor lock-in makes moving from one cloud to another expensive. And CPU and memory options per function are narrower than a dedicated VM, which matters for large or specialised models. On security, she points to function isolation, fine-grained IAM at the function level and short-lived credentials as the defences that carry most of the weight.

Her future section sketches "nano functions" that execute parts of a computational graph instead of a whole model, standardised function interfaces to ease lock-in, and lighter container formats for AI.

## Who should watch

ML engineers and platform teams deciding where to host inference for spiky, request-driven workloads. If your models are huge, long-running or latency-critical on first request, the limitations section is the part to take to your design review. If they're small and bursty, the case studies are your business case.

## Related Conf42 talks

- Murali Mallina on [Building a Serverless GenAI Platform](https://www.conf42.com/Platform_Engineering_2024_Murali_Mallina_serverless_genai_platform).
- Gangadharan Venkataraman on [developer-centric ML inference platforms on Kubernetes](https://www.conf42.com/Platform_Engineering_2025_Gangadharan_Venkataraman_inference_orchestration_kubernetes), the non-serverless alternative.
- Murali Krishna Reddy Mandalapu on [optimizing real-time AI inference at the edge](https://www.conf42.com/Golang_2025_Murali_Krishna_Reddy_Mandalapu_ai_inference_edge).

[Watch Shreya Gupta's talk](https://www.conf42.com/Observability_2025_Shreya_Gupta_scalability_efficiency_ml)

[Watch the talk on YouTube](https://youtu.be/HF35ZCP17_I).

## Watch the talk

[Serverless AI's Rise: Revolutionizing ML Deployment with Scalability & Cost Efficiency](https://www.conf42.com/Observability_2025_Shreya_Gupta_scalability_efficiency_ml) at Conf42 Observability 2025.
