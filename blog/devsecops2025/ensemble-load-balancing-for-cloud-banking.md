# Round robin is too polite for banking traffic

Conf42 Blog, 2025-12-04, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/ensemble-load-balancing-for-cloud-banking

In short: Raghunadha Dornala of Miracle Software Systems at Conf42 DevSecOps 2025 on ECBA, a hybrid ensemble load balancer for secure cloud banking transactions.

Round robin treats every server as equal and every request as the same size, which is a generous assumption for a bank on payday. At Conf42 DevSecOps 2025, [Raghunadha Dornala](https://www.conf42.com/DevSecOps_2025_Raghunadha_Dornala_banking_load_cloud), senior cloud architect at Miracle Software Systems, presented the Ensemble Cloud Banking Algorithm (ECBA): a hybrid of weighted round robin and adaptive load balancing that routes transactions on live metrics and forecasts, with security hooks built in.

It's a short research talk that walks from the problem to a simulation-based evaluation. Dornala notes his own day job is mostly pharmacy, retail and food, so this is a cross-industry idea brought to banking rather than a production story from a bank.

## Why the classic algorithms fall short

Dornala's diagnosis is short and familiar. Round robin hands requests out in sequence without looking at server capacity or current load, so utilisation gets uneven. Least connections looks at open connections but ignores processing power and response times. Under dynamic banking workloads both lead to bottlenecks, idle capacity next to hot nodes, and degraded service quality.

Digital banking makes that worse. Transaction systems have to be fast, secure, compliant with regulation and continuously available, all at once, and the traffic is anything but uniform: payments, fraud checks and analytics don't cost the same.

## ECBA routes on what the servers are actually doing

ECBA watches server capacity, transaction types, latency and throughput, and routes each request using real-time metrics plus predictive analytics. AI forecasting and reinforcement learning let it anticipate spikes before they arrive instead of reacting after queues build. The weighted round robin half keeps distribution fair; the adaptive half shifts load when the numbers move.

He lists the side effects that make it more than a scheduler: fraud detection, predictive routing, compliance monitoring and self-healing. That's where the DevSecOps angle comes in.

## Security travels with the traffic

In Dornala's design the balancer sits inside the DevSecOps framework rather than in front of it. Transactions are encrypted end to end, AI-driven compliance monitoring scans continuously for anomalies and regulatory risk, audit trails are generated as traffic flows, and threat detection flags suspicious traffic patterns in real time through behaviour analysis and automated risk scoring. He positions it alongside a zero-trust architecture.

The appeal is that the component already looking at every request is a natural place to notice when requests look wrong. The trade-off, which the talk doesn't go into, is that your load balancer becomes a much bigger piece of software to secure and operate.

## How it was tested

The evaluation is Python-based simulation, not a live bank. Dornala ran workloads from a thousand up to ten thousand transactions, compared ECBA against round robin, least connections and a standalone adaptive balancer, and measured response time, throughput and utilisation using real-world banking transaction patterns, with anomaly detection integrated to check behaviour under unexpected load.

He reports ECBA posting the lowest response times of the group and, at 5,000 transactions, holding 36.9 requests per second at 83.3% utilisation. Future work is to feed historical transaction data into models that predict workload spikes. Read the numbers as a simulation benchmark: useful for comparing algorithms, not a promise about your traffic.

Deployment, in his outline, starts with an infrastructure assessment, then metric configuration, then rigorous testing, followed by continuous tuning. Use cases run from payment processing to fraud detection.

## Who should watch

Engineers who own traffic management for payment or core banking platforms, and anyone weighing whether a smarter balancer is worth the operational cost. If you want production incident data, this isn't it; if you want a clear argument for capacity-aware, predictive routing, it's a quick watch.

## Related Conf42 talks

- [Developing custom Load Balancer using Envoy](https://www.conf42.com/Golang_2024_Sandeep_Bhat_custom_load_balancer_envoy) shows what building your own balancing logic looks like in practice.
- [Chaos Engineering at Citi Bank](https://www.conf42.com/Chaos_Engineering_2024_Charles_Akl_citi_bank) is about testing banking systems under failure.
- [Cloud-Driven Reconciliation for Financial Accuracy](https://www.conf42.com/Chaos_Engineering_2025_Jaya_Krishna_Vemuri_investment_banking_accuracy) covers another cloud-scale banking workload.

[Watch Raghunadha Dornala's talk](https://www.conf42.com/DevSecOps_2025_Raghunadha_Dornala_banking_load_cloud)

[Watch the talk on YouTube](https://youtu.be/FbOT1XTfqqQ).

## Watch the talk

[Ensemble Load Balancing in Cloud Banking: Secure, Scalable, and Reliable Transactions](https://www.conf42.com/DevSecOps_2025_Raghunadha_Dornala_banking_load_cloud) at Conf42 DevSecOps 2025.
