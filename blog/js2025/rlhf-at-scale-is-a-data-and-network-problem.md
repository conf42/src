# RLHF at scale is a data problem and a network problem

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/rlhf-at-scale-is-a-data-and-network-problem

In short: Votal AI CTO Jyotirmoy Sundi explained at Conf42 JavaScript 2025 how RLHF training runs on Kubernetes GPU clusters and where it gets stuck.

Reinforcement learning from human feedback is why chat models follow instructions, and running it across a GPU cluster is mostly a fight with networking, checkpoints and the slow supply of good human labels. That was the argument Jyotirmoy Sundi, co-founder and CTO of Votal AI, made at Conf42 JavaScript 2025, in a talk that maps the distributed RL stack from policy algorithms down to NVLink.

Fair warning: despite the venue, there is no JavaScript here. This is an ML infrastructure talk, and a useful one if you're the person asked to keep the training cluster alive.

## From MDPs to transformers, and why the reward function bites

He starts with the shift from classic reinforcement learning, built on Markov decision processes that maximise reward step by step, to transformer-based networks that can learn far richer functions across text, images, video and audio.

The training loop he describes for language models: pre-train on a large cluster, then supervised fine-tuning on instruction data (question and answer pairs written by domain experts such as doctors or maths olympiad winners), then optimise against a reward model using policy algorithms like PPO or GRPO, or actor-critic setups. The warning he repeats is about reward hacking. If the reward function is defined loosely, the model will find a way to score well without doing what you meant, and the consequences can be unpleasant. Every engineer who has written a metric and then watched a team optimise it will recognise the pattern.

## Data parallel, model parallel, and checkpoint everything

On the infrastructure side, most of these runs live on large Kubernetes clusters. With data parallelism, every pod holds the same model and gets a slice of the data; workers send updated weights back to a main server after each batch, which combines them and sends them out again. When the model is too big for one GPU, model parallelism splits the network itself across pods.

Runs can take weeks, so checkpointing is not optional: losing a run halfway and restarting from zero burns compute you won't get back. Replay buffers, actor-critic state and terabytes of data all need state management that survives pod restarts.

## The cluster plumbing

The concrete bits are worth having in one place:

- Kubernetes doesn't schedule GPUs natively; you install NVIDIA's device plugin and request GPUs per pod (four is typical, up to eight).
- Fast GPU-to-GPU communication needs NVLink and the NCCL library, because moving weights and state between pods quickly becomes the bottleneck.
- Frameworks he mentioned include IMPALA, Ray (with Ray Train from Anyscale), Microsoft's DeepSpeed for models too big for one GPU, PyTorch DDP for data parallelism, and Kubeflow's PyTorchJob and TFJob operators.

In production he stresses GPU monitoring (he mentions tools like Datadog), because a bad data split leaves some GPUs underused while others work hard. Add circuit breakers for unstable policies and failover that resumes from the last checkpoint instead of killing the whole run.

## Human feedback is the bottleneck

His main point is that the hardest part isn't the frameworks; it's getting enough high-quality human feedback. Feedback loops can take months, and companies such as Scale AI exist to produce labelled examples at volume. That's why he sees reinforcement fine-tuning as promising: start from a seed dataset, define a solid reward function, and let the model generate new training examples itself instead of waiting on experts.

Other open problems he lists: communication overhead between nodes, preferences that change over time, and consistency, since retraining should give results close to the last run even if they're not identical. Emerging directions include federated RLHF, where learning happens on edge devices and only weights sync to a central server, multimodal training, and feedback collected inside the product and used either for fine-tuning or as context in RAG prompts.

## Who should watch

Platform and MLOps engineers who run or are about to run GPU training on Kubernetes, and ML engineers who want a single overview of the RLHF pipeline and its failure points. Frontend developers looking for JavaScript can skip this one.

## Related talks

- [Scaling Reinforcement Learning with Human Feedback in Distributed Cloud Systems](https://www.conf42.com/Kube_Native_2025_Jyotirmoy_Sundi_reinforcement_learning_distributed) is the same speaker on the same subject at Conf42 Kube Native 2025.
- [Instant KAI Sandboxes with vCluster: Multi-Tenant, Multi-Scheduler GPU Sharing](https://www.conf42.com/Kube_Native_2025_Piotr_Zaniewski_sandboxes_gpu_multitenant) covers sharing GPUs between teams on Kubernetes.
- [Fine-tuning LLMs: A Cost-Benefit Analysis for Businesses](https://www.conf42.com/Large_Language_Models_LLMs_2025_Muddassar_Sharif_fine_tuning_business) asks whether you should be fine-tuning at all.

[Watch Jyotirmoy Sundi's talk](https://www.conf42.com/JavaScript_2025_Jyotirmoy_Sundi_scaling_reinforcement_learning)

[Watch the talk on YouTube](https://youtu.be/1a6bzhPfQvE).

## Watch the talk

[Scaling Reinforcement Learning: From Human Feedback to Distributed Intelligence](https://www.conf42.com/JavaScript_2025_Jyotirmoy_Sundi_scaling_reinforcement_learning) at Conf42 JavaScript 2025.
