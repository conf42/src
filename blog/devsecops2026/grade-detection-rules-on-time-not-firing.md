# An alert that fires too late is a log line: grading rules by deadline

Conf42 Blog, 2026-09-23, updated 2026-11-09. https://www.conf42.com/blog/devsecops2026/grade-detection-rules-on-time-not-firing

In short: At Conf42 DevSecOps 2026, security engineer Aleksander Kryukov replays 46 DeFi exploits to grade detection rules on timing, not just firing.

Most detection rules are tested like code: feed in a sample, check the alert fires. At Conf42 DevSecOps 2026, Aleksander Kryukov, a security engineer working in Web3, argued that the test that matters is whether the alert fires early enough for someone to act, and built a replay harness over 46 historical DeFi exploits to measure exactly that.

## Why DeFi makes a good lab

Kryukov's reason for using blockchain incidents is evidence quality. Every on-chain step of every attack sits in a public ledger nobody can edit, with block numbers and call traces, and an archive node can reconstruct the exact state of the world at any block. You can rerun history. The one gap is the pending phase, since a transaction can travel privately until it is included.

His opening case is the Balancer V2 drain in November 2025. Monitoring flagged the first transaction. Emergency controls triggered about twenty minutes later, and pausable pools were paused, protecting over nineteen million dollars. But the older pools had outlived their pause window, so there was nothing for any alert to press. The rule worked. The outcome did not.

## Three variables decide whether an alert mattered

He breaks it down into detection time (when the rule fired, measured from the triggering event plus the detector's own processing time), response latency (alert to mitigation actually taking effect, whether a bot or humans signing a multisig) and mitigation availability (does the pause still exist). He points at the Google SRE workbook's four alert attributes, precision, recall, detection time and reset time, and notes that a unit test with one transaction measures recall and nothing else.

## The harness

The dataset starts from DeFi Hack Labs, the open collection of Foundry proofs of concept, filtered to Ethereum mainnet incidents covered by mempool archives and ranked by reported loss. Each incident becomes a manifest: fork block, setup and exploit transactions, victim contracts, attacker addresses, and a kill chain label on every event.

The key design choice is not to use the proof of concept as the replay. A PoC squeezes deployment, exploit and drain into one test at one block, which is perfect for "is it exploitable?" and useless for "when could we have known?". So the harness forks Ethereum at the block before the attacker's first setup transaction and replays the chain's own transactions block by block. A chain clock merges execution with first-seen mempool times, a visibility filter models what one telemetry profile could see, and an oracle builds the loss curve from victim balance changes. Detectors never see the oracle. Chain time is the only clock.

## Deadlines come from the loss curve, not an SLA

Replays show how different incidents are. Beanstalk lost 182 million dollars in a single transaction. Harvest Finance bled over thirty transactions in under seven minutes. Nomad took more than eight hours. A fixed "alert within five minutes" SLA is too slow for the first and pointless when nobody is watching, as with Ronin, where the theft went unnoticed for six days until a user tried to withdraw.

So each incident gets its own deadline: if you want to lose no more than a given share, the alert must fire before the loss curve reaches that share, minus your response time. For a single-transaction exploit the deadline always lands before the exploit, which is why he grades rules by kill chain stage: funding, preparation, exploitation, laundering. Euler Finance is the cautionary tale: alerts fired ten minutes and three minutes before the attack, and it still lost, because the only response was a manual multisig.

## Budget false positives by reversibility

Early rules are tempting to wire to automatic pauses. Kryukov shows why that needs care: a published early-detection approach with strong lab precision flagged 129 of more than 23,000 new contracts in live use, and 26 were real attack contracts. Attacks are rare and new contracts are plentiful, so even a small false-positive rate swamps the true ones.

His answer is a mitigation ladder from easy to undo to hard to undo: notify, throttle outflow, pause, freeze. Each tier gets a false-action budget, the harness measures each rule's alert rate on incident-free block ranges, and a rule may drive a tier only if it fits. Irreversible actions get zero budget and a human decides.

The last constraint is visibility. Private transaction routing has grown sharply, which blinds the one rule family that relies on the public mempool, pre-inclusion simulation. The others work from what lands on chain.

## It maps straight onto your SOC

The closing section is the reason non-crypto teams should watch. The archive node is your retained raw telemetry. Block-by-block replay is replaying recorded telemetry through detection-as-code rules in CI. The loss curve is time until data is stolen. The pause is auto-remediation like disabling a key or isolating a host, with the same false-positive question. The private mempool is telemetry you simply do not collect.

Detection engineers, SOC leads and anyone wiring alerts to automated response will get a reusable method. Expect a lot of named incidents and numbers; it is dense, and worth it.

## Related Conf42 talks

- [Mandi Walls on tackling alert fatigue with SLOs](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Mandi_Walls_tackling_alert_fatigue).
- [Aleksandra Drobnjak on runtime Kubernetes threat detection with Falcosidekick](https://www.conf42.com/Kube_Native_2024_Aleksandra_Drobnjak_kubernetes_security_falcosidekick_threat_detection).
- [Leonid Yankulin on actionable alerts that fix problems quickly](https://www.conf42.com/Observability_2024_Leonid_Yankulin_actionable_alerts_fix).

[Watch Aleksander Kryukov's talk](https://www.conf42.com/DevSecOps_2026_Aleksander_Kryukov_detection_exploits_simulation)

[Watch the talk on YouTube](https://youtu.be/gILg5Jc9lME).

## Watch the talk

[Would Your Alert Have Fired in Time? Grading Detection Rules Against 46 Real Exploits](https://www.conf42.com/DevSecOps_2026_Aleksander_Kryukov_detection_exploits_simulation) at Conf42 DevSecOps 2026.
