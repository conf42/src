# Quantum-accelerated trading should start with one Treasury book

Conf42 Blog, 2025-06-17, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-trading-start-with-one-treasury-book

In short: Ganesh Marimuthu at Conf42 Quantum Computing 2025 on hybrid quantum-classical trading systems, what firms measured, and why to start with a narrow use case.

The best place to try quantum in a trading stack is not the whole stack. At Conf42 Quantum Computing 2025, Ganesh Marimuthu, a trading technologist with a background in fixed income, argued for hybrid quantum-classical trading systems and closed on the advice that makes the rest credible: start with one bottleneck, such as portfolio optimisation for a slice of US Treasuries, and grow from there.

Marimuthu has worked on fixed income and commodity trading platforms, market-making and risk-adjusted strategies, and products such as ION and Bloomberg, across US Treasuries, swaps, credit and equities. That desk-side view shapes the talk more than the physics does.

## The data has outgrown the latency budget

He opens with the scale: leading exchanges generate around 342 billion market data messages a day, and classical architectures have fundamental limits in processing that within trading-grade latency. In high-frequency trading, nanoseconds decide profit or loss, so every model you add has to fit inside the same response time.

His argument for quantum techniques is parameter capacity. More parameters inside the same latency window means trading models that can weigh a wider range of market factors and signals at once, instead of trading on a simplified picture.

## What the firms measured

The talk presents a set of headline figures: a 78% reduction in complex calculation time, 67% lower computational resource requirements with quantum-inspired algorithms, a 41% reduction in forecasting error rates, and 99.9% execution reliability for the hybrid framework. It also follows three trading firms through a four-step process: find computational bottlenecks in the existing infrastructure, develop quantum-inspired optimisation algorithms for portfolio management, deploy a hybrid architecture, and evaluate.

By asset class, he reports the largest gains in derivatives, where complex mathematical models benefit most from optimisation, with equities, FX and commodities also improving. Note the wording: much of this is quantum-inspired algorithms on classical and accelerated hardware, and the talk doesn't detail the baselines or the hardware, so read the numbers as the speaker's results rather than reproducible benchmarks.

## Each layer does what it's good at

The architecture is a clean division of labour. Classical systems ingest high-throughput market data. Quantum processors take the complex optimisation problems. Hardware acceleration provides deterministic, minimal-latency execution for the algorithms that have to run on every tick. Anyone who has worked with FPGA-accelerated order paths will recognise the shape; the new tenant is the optimiser.

He also makes a time-to-market argument: firms using these frameworks can develop and deploy advanced strategies faster, which matters most during periods of high volatility.

## Four obstacles, honestly named

The challenges section is practical:

- **Talent.** People who understand both quantum computing and financial markets are rare; firms are building training programmes and academic partnerships.
- **Reliability.** Early quantum processors have higher error rates, so hybrid designs add error correction and verification.
- **Integration.** Connecting quantum processing to existing trading systems through APIs without losing performance.
- **Regulation.** Frameworks for quantum-enhanced trading are still being developed, and trade surveillance and spoofing analysis are part of that conversation.

## Start narrow, then scale

His closing recommendations are the useful part. Apply quantum-enhanced algorithms to one specific computational bottleneck rather than across rates, commodities and credit at once; build internal capability in hybrid design; and prepare systems so that, as hardware matures over the next three to five years, the firm can scale quickly.

## Who should watch

Trading technologists and quants who want a business-side map of where quantum and quantum-inspired methods fit in a trading stack. It's strategy and results, not circuits.

## Related Conf42 talks

- Ganesh Marimuthu on [Observability in Modern Treasury Trading Platforms](https://www.conf42.com/Observability_2025_Ganesh_Marimuthu_trading_treasury_platforms), the same desks from the monitoring side.
- Sunny Guntuka on [Algorithmic Trading with Python](https://www.conf42.com/Python_2025_Sunny_Guntuka_trading_algorithmic_python).
- Kiran Purushotham on [Swarming LLM Agents for Real-Time Market Insight](https://www.conf42.com/Kube_Native_2025_Kiran_Purushotham_trading_llm_insight).

[Watch Ganesh Marimuthu's talk](https://www.conf42.com/Quantum_Computing_2025_Ganesh_Marimuthu_quantum_trading_systems)

[Watch the talk on YouTube](https://youtu.be/1RYM42ZJzkg).

## Watch the talk

[Quantum-Accelerated Trading Systems: Revolutionizing Financial Markets Through Computational Advantage](https://www.conf42.com/Quantum_Computing_2025_Ganesh_Marimuthu_quantum_trading_systems) at Conf42 Quantum Computing 2025.
