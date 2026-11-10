# From Diffusion to Production: How vLLM-Omni Unifies Multimodal Inference

A talk at [Conf42 Large Language Models (LLMs) 2026](https://www.conf42.com/llms2026) by [Kosseila Haddalene](https://www.conf42.com/speaker_Kosseila_Haddalene) (Founder | AI infrastructure Lead @ Cloudthrill). Page: https://www.conf42.com/Large_Language_Models_LLMs_2026_Kosseila_Haddalene_multimodal_inference_vllm

Video: https://www.youtube.com/watch?v=Z_pGSa7umwU

## Abstract

Most LLM engineers know autoregressive models inside out, but diffusion transformers play by completely different rules. They don't generate token by token. They denoise. They're compute-bound, not memory-bound. But how do you keep serving LLMs while still generating videos and images in the same inference engine? Is there a way for diffusion to sit inside the same serving pipelines as your LLMs?  vLLM-Omni is the inference engine built for exactly this reality. In this talk, we'll start with just enough diffusion fundamentals  from noise to pixel  the denoising loop, why timesteps matter, and how DiT differs fundamentally from AR models. Then we'll dive into vLLM-Omni's architecture and how it integrates both worlds together: natively disaggregated AR and DiT stages, the OmniRouter dispatch logic, available acceleration for diffusion, and OpenAI-compatible endpoints serving text, images, video, and audio from a single engine.  You'll leave with a clear mental model of where multimodal inference is heading  and what it actually takes to serve it in production.
