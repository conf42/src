# vLLM-Omni serves diffusion models and LLMs from one engine

Conf42 Blog, 2026-06-18, updated 2026-11-17. https://www.conf42.com/blog/llms2026/vllm-omni-diffusion-and-llms-one-engine

In short: Kosseila Haddalene (Cloudthrill) at Conf42 Large Language Models (LLMs) 2026 on how vLLM-Omni runs autoregressive and diffusion stages in one runtime.

Text generation is memory bound and diffusion is compute bound, which is why teams that ship text and images behind one product have ended up running two serving stacks. At Conf42 Large Language Models (LLMs) 2026, Kosseila Haddalene, founder and AI infrastructure lead at Cloudthrill and a vLLM production stack contributor, explains how vLLM-Omni puts both under one runtime: the autoregressive engine inherited from vLLM, a diffusion engine built natively beside it, and a connector that moves data between independently scaled stages.

## Two brains with different physics

Kosseila's comparison table is the mental model for the whole talk. An autoregressive model generates token by token, caches keys and values, has a sequence length that varies per request and uses causal attention. A diffusion transformer denoises over a fixed number of steps, and every step is a full forward pass, sometimes two. Its sequence length is fixed by the output size and every latent patch attends to everything. Early models needed around 50 steps per image; recent ones get by with far fewer.

vLLM-Omni keeps what vLLM already does well on the autoregressive side (KV cache management, paged attention, continuous batching) and adds the diffusion engine as a peer. Around them sit modality encoders on the way in and modality generators on the way out, which gives text, image, audio and video in any combination. He counts more than 40 supported architectures under the one runtime, including the Qwen image, omni and TTS models, FLUX, Hunyuan, Wan, Stable Diffusion and NVIDIA's Cosmos world model, and more than 5,000 GitHub stars for a project whose public launch was the previous December.

For existing vLLM users the entry cost is low: the usual serve command plus an omni flag, with offline and async online paths and OpenAI-compatible endpoints.

## A stage is a unit of work

A request is routed by modality or load, then travels through stages. His concrete example is a Qwen omni text-to-speech request with three: a thinker that understands the input and produces text tokens and hidden states, a talker that turns those into codec codes, and a code-to-wave stage, the vocoder, that renders audible audio.

Each stage is its own engine with its own GPU budget, set in a deploy YAML. In his sample config the thinker is pinned to one GPU with 90 percent of its memory because understanding is the heavy part, while the talker takes 60 percent and the vocoder 10 percent of a second GPU. Three stages, two GPUs. "A stage doesn't equal a GPU," Kosseila Haddalene said at Conf42 Large Language Models (LLMs) 2026. A stage can share a device or span several, and each stage replicates independently, so a bottleneck in one does not force you to scale the whole pipeline.

He admits the split between pipeline and deploy config confused him most. The pipeline is Python that defines the stages for a model, and you never touch it to deploy. The deploy YAML is the placement: devices per stage, memory use, and overrides layered on defaults.

## Shared memory on one box, Mooncake across the network

The Omni connector separates a control plane for light metadata from a fast path for heavy tensors such as KV cache, prompt embeddings and latents. Inside a node, data moves GPU to GPU with no host round trip. Across nodes it goes through a memory pool managed by a transfer engine, usually Mooncake, over RDMA or TCP. His rule of thumb: "shared memory on one machine, Mooncake the moment you cross the network". The swap is a YAML change, with no code edits.

## Caching is the easy win for diffusion

After a short primer on the denoising loop, timesteps, classifier-free guidance (two passes per step, so better prompt adherence costs latency) and the VAE that decodes latents back to pixels, Kosseila goes through the acceleration options. Cache backends are his favourite because they need no code changes and give up to a four times speedup. TeaCache skips work on similar consecutive timesteps and is mostly useful for images; Cache-DiT is his pick for video. For outputs too large for one GPU, such as 4K images, sequence parallelism and ring attention split the work across devices.

The demo is a recorded replay on a rented Nebius GPU node, since he was not going to keep one running all day for a live session. A script picks between Z-Image, Wan 2.2 video, Qwen TTS and Cosmos 3. He feeds Cosmos 3 a screenshot of a racing image NVIDIA had posted, and the server returns a video with sound in three minutes forty. He notes that the published recipe was not quite accurate and that the mandatory Cosmos guardrail has to be downloaded separately with its own license. With Cache-DiT he measured generation about four times faster.

For speech, vLLM-Omni now streams audio in chunks as the talker produces them. The benchmark he shows has time to first audio packet twelve times faster, and batching raises throughput up to four times over Hugging Face Transformers.

## Who should watch

Engineers who already serve LLMs with vLLM and are being asked for images, video or speech next. Expect a long, fast-moving architecture tour with config examples and a replayed demo; some slides lean on his companion blog posts for depth. If you have never touched diffusion, the six-term primer in the middle is enough to follow the rest.

## Related Conf42 talks

- [Running vLLM Inference on Kubernetes Across Clouds: A Production-Ready GPU Blueprint](https://www.conf42.com/MLOps_2026_Kosseila_Haddalene_vllm_kubernetes_gpu) by Kosseila Haddalene (Cloudthrill) at Conf42 MLOps 2026.
- [LLM-Enhanced Multimodal AI for Audio and Video Interaction](https://www.conf42.com/Large_Language_Models_LLMs_2025_Waseem_Syed_multimodal_audio_video) by Waseem Syed at Conf42 Large Language Models 2025.
- [Which Workload Owns This GPU Metric?](https://www.conf42.com/MLOps_2026_Nishant_Modak_gpu_workload_metric) by Nishant Modak at Conf42 MLOps 2026.

[Watch Kosseila Haddalene's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Kosseila_Haddalene_multimodal_inference_vllm) from [Conf42 Large Language Models (LLMs) 2026](https://www.conf42.com/llms2026).

[Watch the talk on YouTube](https://youtu.be/Z_pGSa7umwU).

## Watch the talk

[From Diffusion to Production: How vLLM-Omni Unifies Multimodal Inference](https://www.conf42.com/Large_Language_Models_LLMs_2026_Kosseila_Haddalene_multimodal_inference_vllm) at Conf42 Large Language Models (LLMs) 2026.
