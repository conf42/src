# Adaptive optimisation for Node.js backends and React frontends

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/adaptive-optimization-for-node-and-react-apps

In short: Nike's Deepika Annam argued at Conf42 JavaScript 2025 for runtime-adaptive tuning across Node.js and React, citing up to 2.29x throughput gains.

Static performance tuning is driving a car stuck in one gear: fine on the flat, painful on hills. At Conf42 JavaScript 2025, Deepika Annam, Senior Data Engineer at Nike, made the case for "intelligent optimisation", where Node.js backends and React, Vue and Angular frontends adjust their own resources at runtime, and cited results of up to 2.29x throughput.

It's a high-level talk: lots of analogies, a checklist of techniques, and headline numbers. Good for framing a performance programme, less so for copying code.

## Why static configs lose under real traffic

Her scenario is a retailer during a big sale: thousands of users hit the site in different ways, the backend strains and the frontend falls behind. Fixed configurations and manual tweaks don't keep up when load changes minute to minute. The alternative she describes is a system that watches memory pressure and request spikes and adapts while running, like streaming players that switch video quality to match bandwidth.

## Node.js: pools that resize themselves

On the backend, the levers are adaptive worker pools, connection pools and event loop monitoring, so the server can shift resources when traffic jumps and keep latency down. She compares it to a head chef watching orders and moving staff around the kitchen. These patterns matter most where API throughput is the business, such as finance, retail and logistics.

## React: only the actors who are needed on stage

On the frontend, the problem is unnecessary re-renders. The fixes are familiar ones applied deliberately: watch render cycles, memoise components, lazy-load, and give critical UI updates priority while deferring the rest. She also covers framework-specific angles: rendering and state management in React, the reactivity system and templates in Vue, change detection and ahead-of-time compilation in Angular.

## The numbers, and how to read them

The headline results she presented: 2.29x throughput, 40% smaller bundles, 60% faster load times, and 3x better API response. She also mentioned retailers reporting checkout times dropping from several seconds to under two during peak sales. The talk doesn't attach these to a named application or a published benchmark, so treat them as the scale of improvement to aim for, not a guarantee.

Her point about architecture is that none of this needs heavy infrastructure: a light runtime layer with low CPU and memory overhead can deliver most of the gain.

## The usual suspects, with fixes

The challenges section works as a checklist:

- **Bundle size**: code splitting, tree shaking, dynamic imports with loading priorities.
- **Runtime efficiency under peak load**: adaptive resource allocation and caching.
- **DOM update overhead**: batch operations, an efficient virtual DOM, render what's visible first.
- **API bottlenecks**: request prioritisation, caching, and predictive prefetching (her example: travel sites loading flight data before the user searches).

She also recommends TypeScript for optimisation code that has to scale, with generics, type guards, decorators and union types, and decorators for performance monitoring.

Her closing advice is the right order of operations: measure a baseline first, then move from static config to runtime adaptation, keep the optimisation layer light, and test in production because that's the performance users actually get.

## Who should watch

Engineering leads planning a performance push across a full JavaScript stack, and developers who want a structured list of techniques to check their app against. If you already profile your event loop and React renders, you'll know most of the tools; the value is in seeing them as one system.

## Related talks

- [React is Killing your Performance and it's Your Fault](https://www.conf42.com/JavaScript_2021_Assaf_Krintza_React_Performance) goes much deeper on re-renders.
- [Mission: Performance Impossible – Real time chat webapp's performance with 100k active users](https://www.conf42.com/JavaScript_2024_Mohammed_Zubair_Ahmed_41_realtimechat_performance_100kusers) is a concrete case study under real load.
- [Intelligent Kubernetes Workload Optimization: Applying Deep Reinforcement Learning for Cloud-Native Performance](https://www.conf42.com/Kube_Native_2025_Deepika_Annam_optimization_reinforcement_performance) is the same speaker on adaptive tuning at the infrastructure layer.

[Watch Deepika Annam's talk](https://www.conf42.com/JavaScript_2025_Deepika_Annam_revolutionizing_performance_intelligent)

[Watch the talk on YouTube](https://youtu.be/hbSOSWDjOa4).

## Watch the talk

[Revolutionizing JavaScript Performance: How Intelligent Optimization Delivers 2.29X Throughput Gains in Modern Web Applications](https://www.conf42.com/JavaScript_2025_Deepika_Annam_revolutionizing_performance_intelligent) at Conf42 JavaScript 2025.
