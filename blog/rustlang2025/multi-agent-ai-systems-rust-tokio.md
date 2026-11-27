# Four layers of agents, building multi-agent AI systems on Tokio

Conf42 Blog, 2025-08-21. https://www.conf42.com/blog/rustlang2025/multi-agent-ai-systems-rust-tokio

In short: Sidhanta Panigrahy of Okta at Conf42 Rustlang 2025 on a four-layer multi-agent AI architecture in Rust, with Tokio coordination and a manufacturing case study.

A single monolithic AI service is a single point of failure with a very expensive GPU bill attached. At Conf42 Rustlang 2025, [Sidhanta Panigrahy](https://www.conf42.com/Rustlang_2025_Sidhanta_Panigrahy_memory_safety_zero), Director of Business Technology at Okta, presented a four-layer multi-agent architecture written in Rust and argued that memory safety and Tokio's async runtime are what keep a system of many cooperating agents stable under load.

## The monolith problem

Panigrahy opens with the bottleneck he sees in enterprise AI programmes: most organisations build one centralized AI system, the design itself creates a single point of failure, and garbage-collected runtimes add unpredictable latency spikes and memory overhead on top. Splitting the work across specialised agents fixes the first issue. Rust, he argues, fixes the second.

## Perception, cognition, action, coordination

The architecture has four layers, each made of specialised agents:

- **Perception** agents ingest data, filter it and normalise it.
- **Cognitive** agents run model inference and decision logic.
- **Action** agents execute business logic inside transactional flows.
- **Coordination** agents orchestrate workflows across the distributed system.

The split is a useful template even outside Rust: it separates the noisy input side from the decision side, and makes coordination a first-class job rather than something every agent improvises.

## Why Tokio, and why traits

Agent coordination runs on Tokio, with non-blocking I/O across agent boundaries and priority-based scheduling of agent tasks. He reported handling about 250% more concurrent agents than an equivalent Python or Go system. For the agents themselves he uses custom traits with static dispatch where agent types are known at compile time, so polymorphism costs nothing at runtime, and efficient serialization for messages between agents. He also names actor, embedded-database and ML crates as options beyond Tokio.

The safety argument is about the bugs that plague distributed agents: race conditions, parallel state updates, inconsistent error handling and protocol violations. His claim is that the Rust compiler catches the bulk of them before deployment, and that his systems showed zero memory leaks across more than 50 million agent interactions.

## The manufacturing case

The case study is a global manufacturer whose AI quality-control system had unpredictable latency, causing about 12% production delays. The Rust rebuild used 22 specialised agents across the four layers, integrated with legacy systems through PyO3 and WebAssembly bindings. Panigrahy reported a 43% reduction in quality inspection time with no increase in defects, and latency under 50 ms at three times normal load. The company is not named. His implementation roadmap runs for about 20 weeks, from architecture assessment through core infrastructure and integration to production rollout.

## Who should watch

Architects designing agent systems who worry about what happens at scale, and teams with Python agent prototypes that are starting to fall over. Expect architecture and results rather than code. For a different angle on the same architecture, Panigrahy also gave a platform-focused talk at Conf42 Platform Engineering 2025.

## Related Conf42 talks

- [From Monoliths to Microminds: Building Resilient AI Platforms with Multi-Agentic Architecture](https://www.conf42.com/Platform_Engineering_2025_Sidhanta_Panigrahy_microminds_monoliths_multi) by Sidhanta Panigrahy (Okta) at Conf42 Platform Engineering 2025.
- [Engineering Production-Grade Multi-Agent Systems in the Cloud](https://www.conf42.com/Cloud_Native_2026_Sandeep_Mannapur_ai_agents_workflows) by Sandeep Mannapur (ServiceNow) at Conf42 Cloud Native 2026.
- [Enhancing Gen-AI with Rust](https://www.conf42.com/Rustlang_2024_Karan_Khanna_genai_scalable_systems_ai) by Karan Khanna (Coupang) at Conf42 Rustlang 2024.

[Watch Sidhanta Panigrahy's talk](https://www.conf42.com/Rustlang_2025_Sidhanta_Panigrahy_memory_safety_zero) or the [YouTube recording](https://youtu.be/e_jm2WikexM).

## Watch the talk

[Building High-Performance Multi-Agentic AI Systems in Rust: 40% Faster Enterprise Transformation with Memory Safety Guarantees](https://www.conf42.com/Rustlang_2025_Sidhanta_Panigrahy_memory_safety_zero) at Conf42 Rustlang 2025.
