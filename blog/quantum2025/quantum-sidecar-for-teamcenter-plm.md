# A quantum sidecar for Teamcenter, not a PLM rewrite

Conf42 Blog, 2025-06-19, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-sidecar-for-teamcenter-plm

In short: Pradeep Karanam at Conf42 Quantum Computing 2025 on sending only the hardest PLM questions from Siemens Teamcenter to cloud quantum hardware.

Your PLM system already knows every part and option in the product; it just takes forever to answer a big "what if". Pradeep Karanam, Solutions Architect, used his talk at Conf42 Quantum Computing 2025 to show a small sidecar that sends only the hardest parts of those questions from Siemens Teamcenter (or any PLM tool) to a cloud quantum computer and writes the answer back. Nothing rewrites Teamcenter's core.

The abstract states the goal plainly: option lists that appear 8x faster and purchase plans that cut shortage risk by one third, without changing anyone's daily workflow.

## The pain is measured in dollars per day

Karanam opens with the business case. He cites a study putting the average cost of a major supply-chain disruption around $22 million, and a stopped production line burning roughly $1.5 million a day. Then the complexity problem: a car like the BMW Mini has trillions of valid option combinations, and the rule engines inside PLM check options close to one by one. His goal is to turn overnight batch jobs into answers you get over a coffee break.

## Four steps over REST

The architecture is the reason to watch. Teamcenter already sends heavy jobs to HPC clusters, so quantum is just another remote backend:

1. Pull the bill of materials or supply data through the Active Workspace REST API.
2. Convert it into the maths a quantum machine understands: a QUBO matrix for optimisation, or a probability model for simulation.
3. Send it to the cloud and wait a few seconds for the best answer.
4. Write the new configuration or risk score back into Teamcenter, where everyone already works.

He calls it a bolt-on microservice, not a rip and replace. For configuration, every rule becomes an energy penalty, and the annealer settles into a valid, low-energy build.

## The hardware list is refreshingly specific

Instead of a generic qubit diagram, the talk names what was reachable through cloud APIs at the time: D-Wave's Advantage2 annealer, Pasqal's neutral-atom machine on Google Cloud, IBM's 127-qubit Eagle, and Fujitsu's Digital Annealer, which he says is already in daily use at a Toyota plant. Gate-model chips, annealers and neutral-atom arrays get one line each on what they are good for. Because today's machines are noisy, the quantum core is always wrapped in classical code.

## Fewer Monte Carlo runs, more design iterations

For supply risk, planners run Monte Carlo simulations when a port closes. Karanam's point is that quantum amplitude estimation reaches the same confidence with about 10,000 scenarios instead of a million, and he cites D-Wave tests where scenario throughput rose sharply. The same pattern applies to engineering: the talk cites faster battery-cooling CFD, fewer crash FEA runs and overnight polymer simulations, all feeding the Teamcenter digital twin.

## Protect while you innovate

Two pieces of advice stand out because they apply even if you never buy quantum time. First, quantum computers threaten today's encryption, and NIST published its first post-quantum standards in 2024, so audit the Teamcenter supplier portal for RSA-2048 and plan the cutover. Second, his risk table: hybrid error-aware code for decoherence, open standards like QIR against vendor lock-in, a "quantum translator" role that speaks both PLM and quantum, and phase-gated ROI checkpoints so projects live or die on real numbers.

The roadmap is staged: a cloud proof of concept on one high-value use case in the first three months, a production microservice benchmarked against CPUs by month twelve, then more sites and post-quantum TLS on the supplier portal by month 24.

## Who should watch

PLM architects, manufacturing IT leads and supply-chain planners who want a quantum pilot small enough to get approved. The talk is short and dense; the four-step REST flow and the risk table are the parts to screenshot.

## Related Conf42 talks

- [Quantum and quantum-inspired annealing: the state of play](https://www.conf42.com/Quantum_Computing_2023_Peter_den_Haan_annealing_state_of_play) by Peter den Haan, background on the annealers this design relies on.
- [Standardised collaborative forecasting for stronger supply chains](https://www.conf42.com/Golang_2025_Madhusudan_S_Vadigicherla_supply_chain_forecasting) by Madhusudan S Vadigicherla, the classical forecasting side of supply-chain risk.

[Watch Pradeep Karanam's talk](https://www.conf42.com/Quantum_Computing_2025_Pradeep_Karanam_plm_teamcenter)

[Watch the talk on YouTube](https://youtu.be/O3MCMwLQ3VM).

## Watch the talk

[Plugging Quantum Power into PLM, Teamcenter: Faster Product Choices, Safer Supply Chains](https://www.conf42.com/Quantum_Computing_2025_Pradeep_Karanam_plm_teamcenter) at Conf42 Quantum Computing 2025.
