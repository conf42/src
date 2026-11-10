# Life of a token: from agents to silicon and back

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Alessandro Vozza](https://www.conf42.com/speaker_Alessandro_Vozza) (AI Architect @ Volt Datacenters). Page: https://www.conf42.com/MLOps_2026_Alessandro_Vozza_token_silicon_agents

## Abstract

What really happens between your agent's prompt and the GPU in a self-hosted AI stack?  Every AI agent call ends up as tokens on a GPU somewhere, and most developers never see what happens in between. In this talk we follow a single token from an agent running in Kubernetes, through an AI gateway that enforces identity and policy, through an inference-aware router, down to vLLM on bare-metal GPUs, and all the way back. Along the way you'll learn why LLM traffic breaks traditional load balancing, what prefill and decode mean for latency and cost, and what it takes to run the whole stack on infrastructure you control.
