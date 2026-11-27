# Seven signatures needed, three signers showed up. Now what?

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/federated-multisig-observability-grafana-alloy

In short: Onyebuchi Mark Irozuru of Botanix Labs at Conf42 Observability 2025 on monitoring a federated Bitcoin multisig with Grafana Alloy, Loki, Prometheus and Tempo.

A multisig is secure because its signers are spread across operators, hardware vendors and continents, and that is exactly what makes it hard to debug. At Conf42 Observability 2025, Onyebuchi Mark Irozuru, DevOps lead at Botanix Labs, a Bitcoin layer-2 startup, showed how his team built shared observability for a federated multisig without taking control away from the independent operators who run the nodes.

The setup is Grafana Alloy on each operator's side, shipping to central Loki, Prometheus and Tempo endpoints.

## The invisible complexity of distributed signing

Mark opens with the Bitcoin motto about keys and coins, then gets to the operational problem. A multisig spreads the attack surface by requiring signatures from multiple locations, states, hardware vendors and validator sets. Now picture seven signatures needed from 12 validators on four continents, and only three show up. Is a validator offline? Did it receive the transaction? Is the mempool full? Is it a network problem, a protocol problem, or an attack?

Without good telemetry, he says, you have no answers to any of those questions.

## What usually gets monitored, and what does not

Teams already watch the easy things: transactions, signature counts, hot and cold wallet balances. What stays hidden is the interesting part: the signature collection pattern (who signed what, and when), which nodes have been active and pushing the most transactions, network topology health, cryptographic performance and bottlenecks in proof generation. He walks through the flow of a 3-of-3 signing (initialisation, hash, signature collection, aggregation and verification) to show how many steps users never see.

In a federation, operational silence means slow recovery. Timeouts and slow signers translate directly into slow block production.

## Federated observability keeps the federation federated

The design principle is the part worth stealing for any multi-party system: each operator stays independent, with their own configuration on Kubernetes, Docker, bare metal or cloud, while contributing to a shared visibility layer. Nobody hands over the keys to their infrastructure to get a shared dashboard.

Grafana Alloy is the collector of choice because it combines logs, metrics, traces and profiling in one open-source agent and can run as a sidecar. Each operator tunes Alloy locally; all data flows to shared endpoints: Loki for logs, Prometheus for metrics, Tempo for traces. Access to those endpoints is secured with tokens, so the shared layer does not become the weak point.

## Before and after

The before picture is grim and familiar: blind spots in signature collection, hours of debugging a failed transaction by asking operators to send logs over various channels, unstructured logs, network issues found too late, and malicious nodes participating unchecked.

After, the team can see who the slow signer is, trace how requests propagate across signers, catch failures in real time and set alerts on service level indicators before users notice.

## Who should watch

Infrastructure engineers in Web3, and anyone running a system where several independent organisations each own a piece, such as consortiums, partner networks or federated platforms. It is short and architectural; bring your own Alloy config. Mark closes with open questions for the audience, including how to find the monitoring gaps specific to your own network.

## Related Conf42 talks

- [Shyam Sreevalsan on why decentralized monitoring matters](https://www.conf42.com/Observability_2024_Shyam_Sreevalsan_decentralized_monitoring_matters) (Observability 2024).
- [Sharath Chandra Adupa on blockchain for data integrity and security](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sharath_Chandra_Adupa_harnessing_blockchain_data) (SRE 2025).
- [Steve Flanders and Curtis Robert on mastering OpenTelemetry Collector configuration](https://www.conf42.com/Observability_2024_Steve_Flanders_Curtis_Robert_mastering_collector_configuration) (Observability 2024), for the collector side of the pipeline.

[Watch Onyebuchi Mark Irozuru's talk](https://www.conf42.com/Observability_2025_Onyebuchi_Mark_Irozuru_signatures_observability_federated)

[Watch the talk on YouTube](https://youtu.be/7d0NeC0VEw0).

## Watch the talk

[Seeing Beyond the Signatures: Federated Multisig Observability](https://www.conf42.com/Observability_2025_Onyebuchi_Mark_Irozuru_signatures_observability_federated) at Conf42 Observability 2025.
