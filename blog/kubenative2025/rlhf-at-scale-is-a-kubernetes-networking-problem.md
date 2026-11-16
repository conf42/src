# RLHF at scale is a networking and data problem on Kubernetes

Conf42 Blog, 2025-10-13, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/rlhf-at-scale-is-a-kubernetes-networking-problem

In short: Jyotirmoy Sundi, CTO of Votal.ai, maps at Conf42 Kube Native 2025 how RLHF training runs across multi-GPU Kubernetes clusters, and where it breaks.

The models get the headlines, but the hard parts of reinforcement learning from human feedback are moving weights between GPUs fast enough and getting enough good human labels. At Conf42 Kube Native 2025, Jyotirmoy Sundi, co-founder and CTO of Votal.ai, walked through how RLHF systems run on multi-GPU Kubernetes clusters, which frameworks people reach for, and where the bottlenecks really are.

It is a survey talk with a practitioner's checklist, not a code walkthrough. Good as a map if you are about to stand up your first distributed training cluster.

## From MDPs to transformers

Sundi starts with the theory in one breath: classic RL comes from Markov decision processes, an agent maximising cumulative reward step by step. Swap the policy for a transformer and the same loop can learn far richer functions over text, images, audio and video. Policy optimisation algorithms such as PPO, GRPO and DDPO, plus actor-critic setups, do the learning; which one wins depends on your data and how you define the reward.

He spends real time on that last point. A sloppy reward function invites reward hacking, where the model finds a way to score well that you didn't intend. If you remember one warning from the talk, make it that one.

## Data parallel, model parallel, and the checkpoint that saves your week

On the distributed side, the two shapes are data parallelism (the same model on every pod, the data split across them, gradients gathered by a coordinating server and sent back) and model parallelism for models too large for one GPU, where the network itself is split across pods. Training runs can take weeks, so checkpointing is not optional: a pod failure at 50% should resume from the last checkpoint, not from zero.

Kubernetes handles the orchestration, resource management and failure recovery, plus the state for replay buffers and terabytes of training data. It doesn't do GPUs out of the box: you install NVIDIA's device plugins and typically request four, sometimes eight, GPUs per pod.

## The network is the bottleneck you pay for

Sundi keeps returning to communication overhead. Every step means sharing policy or weight parameters across the cluster, and slow links turn into idle GPUs and a bigger bill. NVLink for GPU-to-GPU traffic and NVIDIA's NCCL library for collective communication are the baseline. On frameworks he names IMPALA, Ray, Lightning AI, DeepSpeed (for models that must be split), PyTorch DDP, Ray Train from Anyscale, and Kubeflow's PyTorch and TensorFlow job operators.

In production, watch GPU utilisation closely: badly sharded data leaves some GPUs underused while others work flat out, and finding the right distribution takes trial and error. He also recommends circuit breakers for unstable policies and robust failover, so one bad pod doesn't sink the run.

## Human feedback is the golden dataset

The bigger long-term constraint, in his view, is labels. Supervised fine-tuning depends on expert-made data (doctors, physicians, maths olympiad winners), and feedback loops can take months. Labelling companies such as Scale AI help, but he expects the next two to three years to be about collecting specialised human data. His bets for easing it: reinforcement fine-tuning, where a good reward function lets the model generate new training data from a small seed; feedback captured inside products; and federated RLHF that learns on edge devices and syncs weights centrally.

## Who should watch

ML platform engineers asked to run RLHF or fine-tuning on Kubernetes, and infra folks who want to know why the ML team keeps asking for faster interconnects. Researchers after new algorithms won't find them here.

## Related talks

- Sundi gave a companion talk at Conf42 JavaScript 2025: [Scaling Reinforcement Learning: From Human Feedback to Distributed Intelligence](https://www.conf42.com/JavaScript_2025_Jyotirmoy_Sundi_scaling_reinforcement_learning).
- For the GPU-utilisation monitoring Sundi recommends, Nishant Modak asks [Which Workload Owns This GPU Metric?](https://www.conf42.com/MLOps_2026_Nishant_Modak_gpu_workload_metric)
- RL pointed at a different target: Vijay Kumar Valaboju on [Leveraging Reinforcement Learning for Adaptive, AI-Driven Security Assessments in DevSecOps](https://www.conf42.com/DevSecOps_2024_Vijay_Kumar_Valaboju_reinforcement_learning_assessments).

[Watch Jyotirmoy Sundi's talk](https://www.conf42.com/Kube_Native_2025_Jyotirmoy_Sundi_reinforcement_learning_distributed)

[Watch the talk on YouTube](https://youtu.be/IniG11g2KeU).

## Watch the talk

[Scaling Reinforcement Learning with Human Feedback in Distributed Cloud Systems](https://www.conf42.com/Kube_Native_2025_Jyotirmoy_Sundi_reinforcement_learning_distributed) at Conf42 Kube Native 2025.
