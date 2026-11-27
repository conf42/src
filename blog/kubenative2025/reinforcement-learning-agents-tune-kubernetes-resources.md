# Reinforcement learning agents can tune Kubernetes better than thresholds

Conf42 Blog, 2025-10-16, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/reinforcement-learning-agents-tune-kubernetes-resources

In short: Deepika Annam (Nike) at Conf42 Kube Native 2025 on DQN, PPO and SAC agents for Kubernetes scheduling and autoscaling, with safe rollout guardrails.

A flash sale hits, the static HPA thresholds react too late, some services fall over while others sit on idle capacity, and someone edits configs at midnight. At Conf42 Kube Native 2025, Deepika Annam, Senior Data Engineer at Nike, used that retail story to make the case for deep reinforcement learning in Kubernetes: agents that learn workload patterns and adjust scheduling and resources ahead of the spike instead of after it. In her experiments, RL-optimised clusters cut application response time by 30% compared with static autoscaling.

The talk covers the algorithms, how they plug into Kubernetes, and, most usefully, how to stop a learning agent from breaking production.

## Thresholds react; agents anticipate

Deepika's critique of standard autoscaling is that it is reactive: a metric crosses a line, the system responds, and it never learns from last week. An RL agent observes the cluster, learns cyclical spikes, seasonal trends and correlations between microservices, and adjusts proactively. One result she called surprising was agents anticipating traffic surges before they happened, from patterns in historical data. She also saw fewer scaling events overall, which makes resource management calmer and cheaper.

She targets four areas: pod scheduling, resource allocation, traffic routing in the service mesh, and multi-cluster orchestration.

## Pick the algorithm by the shape of the decision

The algorithm section is a good primer on matching method to problem:

- **Deep Q-Networks** for discrete choices: which node gets this pod, which resource tier. Experience replay keeps training stable by sampling past experiences at random.
- **PPO** for continuous allocation such as CPU and memory, because its clipped objective keeps policy updates gradual, so resources don't lurch.
- **Soft Actor-Critic** for multi-objective work. Entropy regularisation keeps the agent exploring, and the reward can weigh cost, performance and reliability together. In her experiments SAC did best on highly variable, multi-service workloads, with lower response times and better cost efficiency than DQN and PPO.

The hard part in every case was the reward function. Reward only CPU utilisation and the agent will happily ignore latency. Weighting several metrics correctly was the key to getting the behaviour they wanted.

## Custom controllers do the translating

Integration runs through custom controllers that collect cluster metrics, feed them to the agent, and turn its recommended actions into Kubernetes API calls, with error handling and rollback so every action is reversible. The pain points she lists are honest: metric latency, Kubernetes API changes, and RBAC so the agent can only take safe, authorised actions. Debugging an agent whose decisions look counter-intuitive needs detailed logs of state and reward calculations.

Multi-cluster adds state synchronisation and network latency to the mix. Her suggestion there is federated learning: each cluster trains locally and shares only model updates, so raw data never leaves the cluster.

## Guardrails before glory

The production section is the one to bookmark. Circuit breakers halt the agent if it starts behaving unexpectedly. New policies roll out as canaries on a small subset of workloads, with automated rollback if performance drops. Models are versioned and A/B tested against each other. And everything is visible in Prometheus and Grafana, so humans can audit what the agent did. Her adoption advice is to start with non-critical workloads and capture baseline metrics first, so the improvement is provable.

## Who should watch

Platform engineers who have tuned HPA thresholds one too many times, and ML engineers looking for a well-scoped infrastructure problem. The talk is conceptual on the algorithms and practical on the safety rails; you won't get code, but you will get the architecture and the questions to answer before trying it.

## Related Conf42 talks

- [Kubernetes Scaling for Savings and Stability: Beyond HPA and VPA](https://www.conf42.com/Observability_2026_Joshua_Fox_kubernetes_autoscaling_reliability) explores non-RL ways past threshold autoscaling.
- [Scaling Reinforcement Learning: From Human Feedback to Distributed Intelligence](https://www.conf42.com/JavaScript_2025_Jyotirmoy_Sundi_scaling_reinforcement_learning) goes deeper on RL itself.
- [The Frugal k8s Engineer: Strategies for Amazon EKS](https://www.conf42.com/Kube_Native_2024_Piyush_Mattoo_Dariush_Azimi_karpenter_kubernetes_optimization) is the cost-first, Karpenter-based baseline to compare against.

[Watch Deepika Annam's talk](https://www.conf42.com/Kube_Native_2025_Deepika_Annam_optimization_reinforcement_performance)

[Watch the talk on YouTube](https://youtu.be/JCLkoojSl0M).

## Watch the talk

[Intelligent Kubernetes Workload Optimization: Applying Deep Reinforcement Learning for Cloud-Native Performance](https://www.conf42.com/Kube_Native_2025_Deepika_Annam_optimization_reinforcement_performance) at Conf42 Kube Native 2025.
