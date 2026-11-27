# Quantum payments need post-quantum security before they need speed

Conf42 Blog, 2025-06-19, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-payments-routing-fraud-and-pqc

In short: Intuit's Nikhil Kassetty at Conf42 Quantum Computing 2025 on quantum routing, fraud detection and settlement for real-time payments, and the security catch.

The same machine that could route a payment in microseconds could also read the payment's encryption. At Conf42 Quantum Computing 2025, Nikhil Kassetty, Software Engineer at Intuit, made the case that quantum computing will reshape real-time payments, routing, fraud detection and risk, and that the industry has to build quantum-safe infrastructure in parallel or the upside turns into exposure.

It's a forward-looking talk rather than a build log. Kassetty is clear that the field is in what he calls the experimentation era: pilots, not production.

## From batch windows to path search

The problem he starts from is familiar to anyone who has waited three days for a bank transfer. Payments still move in batch cycles, held up by processing windows, settlement queues and routing inefficiencies. His thesis is that quantum-enhanced routing could evaluate a huge number of possible paths at once, weighing currency conversion, regulatory constraints and network conditions, and pick the most efficient one.

Settlement is where he sees the biggest change: work that takes hours or days today shrinking towards milliseconds, which improves liquidity and cuts risk along the way. He grounds the claim in a real initiative, the Bank for International Settlements working with the central banks of France and Germany on a project around cross-border settlement and monetary infrastructure.

## Fraud detection before the transaction completes

The second use case is fraud. Kassetty describes quantum sorting and analytics over massive financial data sets to spot anomalies and patterns in real time, flagging suspicious activity before a transaction finishes rather than after. He extends the same idea to anti-money laundering, where tracing behaviour across complex transaction chains and hidden networks is a graph problem that grows ugly fast on classical hardware.

Risk management gets its own pass: portfolio optimisation across many assets and constraints, asset pricing models that keep more variables instead of simplifying them away, market and credit risk simulated at scale, and consumer analytics for more personalised services.

## The quantum security paradox

The section that makes this talk more than a hype reel is the one Kassetty names the Quantum Security Paradox. Payment systems rely on RSA and ECC, both of which a capable quantum computer can break. Worse, harvest attacks are already possible: collect encrypted transactions, personal data and interbank traffic now, decrypt them once the hardware catches up.

His conclusion is that post-quantum cryptography has to arrive before quantum computers reach maturity, and that security "must evolve parallel with innovation". If you work on payments, that is the slide to take back to your team.

## A phased path, not a switch

The preparation advice is practical. Build a strategic roadmap that assesses talent and where quantum creates the most value. Expect regulators, central banks and industry bodies to shape the standards. And plan the transition in phases, starting with hybrid models and gradually introducing post-quantum cryptography, because nobody flips a global payment network from old to new overnight.

He is also honest about the limits: qubits remain fragile, the hardware is still evolving and timelines are uncertain.

## Who should watch

Payment and fintech engineers who want a structured map of where quantum might matter in their domain, and security folks who need the harvest-now argument framed for a payments audience. If you want algorithms and benchmarks, this isn't that talk; it's the strategy layer.

## Related Conf42 talks

- Sandeep Katuri on [fraud detection and digital payments security](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security), the classical baseline quantum has to beat.
- Husayn Gokal on [Quantum Cybersecurity: Securing the Future in the Age of Quantum Computing](https://www.conf42.com/Quantum_Computing_2023_Husayn_Gokal_securing_future).
- Sudhakar Kandhikonda on [AI-Enhanced Fraud Detection with real-time analytics](https://www.conf42.com/Machine_Learning_2025_Sudhakar_Kandhikonda_fraud_detection).

[Watch Nikhil Kassetty's talk](https://www.conf42.com/Quantum_Computing_2025_Nikhil_Kassetty_quantum_payments_latency)

[Watch the talk on YouTube](https://youtu.be/pdicFktAeXs).

## Watch the talk

[From Milliseconds to Microseconds: How Quantum Computing Could Transform Real-Time Payments](https://www.conf42.com/Quantum_Computing_2025_Nikhil_Kassetty_quantum_payments_latency) at Conf42 Quantum Computing 2025.
