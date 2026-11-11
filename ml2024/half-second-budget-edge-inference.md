# Real-time AI has a half-second budget, and the network eats it first

Conf42 Blog, 2024-05-30. https://www.conf42.com/ml2024/half-second-budget-edge-inference

In short: Michele Taroni (Gcore) at Conf42 Machine Learning 2024 on serving models at the edge to keep end-to-end inference under half a second

A well-optimised model can still feel slow if the request has to cross an ocean first. At Conf42 Machine Learning 2024, [Michele Taroni](https://www.conf42.com/Machine_Learning_2024_Michele_Taroni_global_pipeline_edge) of Gcore explained how the company built inference at the edge: shrink the model's compute time, route each request to the nearest GPU region over a CDN backbone, and keep the whole round trip under the half second humans perceive as instant.

It is a sponsor talk about Gcore's own platform, but the latency arithmetic in the middle applies to anyone serving models to users spread across continents.

## Why does serving location matter more than training location?

His framing: as AI moves from pilots into production, the main compute workload moves from training to inference, and inference has an end user waiting on it. Training wants raw throughput. Gcore's training side is NVIDIA A100 and H100 clusters with NVLink inside a node and InfiniBand between nodes. Serving wants low latency wherever the user happens to be.

His example uses Mistral 7B run locally: a prompt of about 200 tokens and an answer of about 20 took around 250 milliseconds. That feels real-time. Put the user in Tokyo and the model in a US data centre, and network latency alone can double or treble that, so the end-to-end time creeps towards a second.

Michele Taroni said at Conf42 Machine Learning 2024: "around half a second is around about the time which as a human we perceive that to be in real time." Any slower and people notice the lag. Chatbots are the familiar case, but he also listed autonomous driving, live streaming and quality inspection in mining and manufacturing. Some of those also need data processed locally for regulatory or privacy reasons.

## What has to be true to hit real time?

He named three requirements: distributed compute close to users, a low-latency backbone connecting it, and runtime deployment that can be reconfigured without drama.

### Make the model cheaper to run

For the compute side, focused on LLMs, Gcore used four families of optimisation:

- **Operator fusion**, merging operators to cut overhead per step.
- **Quantization**, storing weights and activations in fewer bits.
- **Compression**: sparsity to trim unnecessary connections, and distillation to train a smaller model that mimics a larger one.
- **Parallelism**: tensor parallelism across devices and pipeline parallelism for larger models.

He noted the obvious catch: each of these trades some accuracy for speed, and you have to check you have not traded away too much.

### Make the trip shorter

The network side borrows the logic of 5G and CDNs. With 180 CDN points of presence, a request reaches Gcore's network and back in about 30 milliseconds on average, and gets to an inference node in about 50, compared with a few hundred milliseconds in a typical public cloud setup, by his estimate. If the optimised model takes 100 to 400 milliseconds, the total stays under half a second. He put automatic speech recognition, object detection and text-to-speech in the same bucket.

### One endpoint, many regions

Deployment is container as a service behind a single anycast endpoint. A user in Kyoto hits a local CDN node, and smart routing sends the request to the nearest inference region, Tokyo; a user in Rio de Janeiro is served in Brazil. The data and the model stay in-region, which also means you could run a different model per region, such as one trained only on Japanese user data in Japan. Each region autoscales, so compute follows demand both up and down.

## What did the demos show?

Three demos. A face avatar that changes as prompts are typed (Elon Musk, Bill Gates, Madonna, a Jeff Bezos from his hair era). An English-to-Luxembourgish voice-to-text translation that came back in under half a second, which is handy since, as he admitted, he does not speak Luxembourgish despite the head office being in Luxembourg. And a generated video from a customer's generative platform that trains on Gcore's H100 infrastructure and serves its models through Gcore's inference services.

At the time of the talk the edge inference product was entering beta, with a model catalogue including Mistral and Stable Diffusion alongside bring-your-own models, and DDoS protection on the endpoint. He said the team was working to bring latency down to a few tens of milliseconds.

## Who should watch?

ML engineers moving a model from a notebook to users in several regions, and anyone who has optimised inference down to 200 milliseconds and still gets complaints from Asia. Expect architecture and demos, not code.

## Related Conf42 talks

- Murali Krishna Reddy Mandalapu on [real-time AI inference at the edge for autonomous vehicles](https://www.conf42.com/Golang_2025_Murali_Krishna_Reddy_Mandalapu_ai_inference_edge) at Conf42 Golang 2025.
- Alex Casalboni on [WebAssembly from cloud to edge](https://www.conf42.com/Golang_2025_Alex_Casalboni_cloud_edge_webassembly) at Conf42 Golang 2025.
- Lukasz Karwacki of Gcore on [protecting infrastructure and web applications together](https://www.conf42.com/DevSecOps_2024_Lukasz_Karwacki_protection_Infra_web_apps) at Conf42 DevSecOps 2024.

[Watch Michele Taroni's talk](https://www.conf42.com/Machine_Learning_2024_Michele_Taroni_global_pipeline_edge), part of [Conf42 Machine Learning 2024](https://www.conf42.com/ml2024).

## From Gcore

Gcore is a global cloud, edge and AI provider: GPU instances for training, managed Kubernetes, and inference at the edge served through its CDN network.

- [Gcore website](https://gcore.com/)

[Watch the talk on YouTube](https://youtu.be/jyM0f5Gy9gA).

## Watch the talk

[Global Intelligence Pipeline: How We’re Crafting Inference at the Edge](https://www.conf42.com/Machine_Learning_2024_Michele_Taroni_global_pipeline_edge) at Conf42 Machine Learning 2024.
