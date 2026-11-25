# A plain-language tour of Shor, Grover, QAOA and VQE

Conf42 Blog, 2025-05-20, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/quantum-algorithms-tour-shor-grover-qaoa

In short: Sarah Choudhary walks through the four quantum algorithms worth knowing at Conf42 Quantum Computing 2025, plus where pilots run and where the hype is.

Four algorithms carry most of the weight in quantum computing today, and you can understand all four without a physics degree. At Conf42 Quantum Computing 2025, Sarah Choudhary, a Principal SME architect and data scientist with two decades in data and AI systems, gave a 30-minute tour of Shor, Grover, QAOA and VQE, then spent just as long on what the hardware still can't do. It is an introduction and it says so up front: the promise is clarity for researchers, cloud architects and the merely curious.

## Classical computers aren't wrong, they're the wrong tool sometimes

Choudhary starts with the von Neumann architecture, the 1940s design that took us from floppies to the cloud, and its limit: nature doesn't compute in ones and zeros. Simulating a molecule with classical logic is, in her words, "trying to paint the ocean with a pencil". Later she offers an even better one: modelling quantum systems on a classical machine is like translating poetry with a calculator.

The argument isn't that quantum replaces anything. She is explicit that a quantum computer will not run your spreadsheet faster or replace your phone's processor. It complements classical machines on a specific class of problems that lean on superposition, entanglement and interference. The talk also tells the 2019 Google Sycamore random circuit sampling story honestly, including IBM's rebuttal that a classical supercomputer could have done it in days rather than millennia.

## The four algorithms, one sentence each

The core of the talk is a compact field guide:

- **Shor (1994)** factors large integers exponentially faster than classical methods, which is why RSA has an expiry date and why post-quantum cryptography is now a national security topic.
- **Grover (1996)** searches unsorted data in square-root time. Her haystack example: a million possibilities in about a thousand steps.
- **QAOA** is a hybrid classical-quantum optimiser aimed at routing, load balancing and portfolio problems, where classical solvers settle into a local minimum.
- **VQE** estimates the ground-state energy of molecules, the route to faster drug and materials design.

She ties each to who is testing it: Roche and AstraZeneca on molecular simulation, Goldman Sachs and JPMorgan Chase on portfolio optimisation and Monte Carlo, Volkswagen and DHL on traffic and route planning, ExxonMobil and BASF on catalysts.

## Light might beat the fridge

The section most intros skip is photonic quantum computing. Instead of superconducting circuits cooled near absolute zero, photonic machines encode qubits in particles of light, run at room temperature and reuse fibre-optic components that are already mass-produced. Xanadu's Borealis and PsiQuantum get named, along with the honest catch: generating single photons reliably and building logic gates from light is still less mature than superconducting tech.

She then lines up the four hardware families (superconducting at IBM and Google, trapped ions at IonQ and Honeywell, photonics, and the earlier-stage neutral-atom and topological approaches, Microsoft among them) and admits nobody knows which one wins.

## The hype section is the best part

Choudhary is blunt about the NISQ era. Qubits decohere in microseconds, one reliable logical qubit may need hundreds or thousands of physical ones, and for many real-world problems nobody has yet proven a quantum solution beats classical. She also warns that some companies sell quantum solutions that are not quantum at all. Her timeline: hybrid models common in R&D by about 2028, error-corrected systems after that, and quantum as an API call in the cloud after 2032. Treat the dates as a forecast, not a promise.

The closing advice is practical: you can start now with Qiskit, Cirq, Azure Quantum's Q#, Amazon Braket and PennyLane, most of them free to try in the cloud.

## Who should watch

Engineers and architects who need one talk that maps the vocabulary (qubits, interference, NISQ, QAOA) to real problems and real companies. If you already write Qiskit circuits, the history section will be familiar; jump to the hardware comparison and the hype warning.

## Related Conf42 talks

- [Quantum inspired algorithms as a means of getting quantum benefit in the NISQ era](https://www.conf42.com/Quantum_Computing_2023_Abhigyan_Mishra_algorithms_quantum_benefit_nisq_era) by Abhigyan Mishra, for what you can run before the hardware matures.
- [High level programming for quantum circuits](https://www.conf42.com/Quantum_Computing_2024_Vincent_van_Wingerden_programming_quantum_circuits) by Vincent van Wingerden, the next step once the algorithms make sense.
- [Quantum computing: is it real or just hype?](https://www.conf42.com/Quantum_Computing_2023_Michal_Jankowski_real_or_hype) by Michal Jankowski, a second opinion on the hype question.

[Watch Sarah Choudhary's talk](https://www.conf42.com/Quantum_Computing_2025_Sarah_Choudhary_quantum_algorithms_problem)

[Watch the talk on YouTube](https://youtu.be/hLmKDz24VTo).

## Watch the talk

[Quantum Algorithms in Action: Revolutionizing Problem Solving](https://www.conf42.com/Quantum_Computing_2025_Sarah_Choudhary_quantum_algorithms_problem) at Conf42 Quantum Computing 2025.
