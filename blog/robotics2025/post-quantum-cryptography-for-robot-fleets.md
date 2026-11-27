# Robots shipped today will still be running when quantum breaks RSA

Conf42 Blog, 2025-11-20, updated 2026-11-09. https://www.conf42.com/blog/robotics2025/post-quantum-cryptography-for-robot-fleets

In short: Nehal Singh of California State University, Long Beach at Conf42 Robotics 2025 on moving robot fleets to post-quantum crypto with hybrid TLS and Dilithium.

A warehouse robot bought this year may still be on the floor in fifteen years, which is long enough for a quantum computer to read everything it ever sent. At Conf42 Robotics 2025, Nehal Singh, Senior Manager for IT Infrastructure and Productivity Apps at California State University, Long Beach, laid out how to move robot networks to post-quantum cryptography without breaking real-time behaviour.

The talk is short and practical: threat model, the NIST algorithms, a reference architecture, and a migration checklist.

## Harvest now, decrypt later already applies to robots

Shor's algorithm is expected to break RSA and ECC, the schemes that protect robot command channels and firmware today. Nehal's sharper point is timing. Attackers can collect encrypted telemetry, maps, sensor logs and firmware blobs now and decrypt them once the hardware exists. Robots produce exactly that kind of long-lived data, and they receive updates and commands that must stay trustworthy for years.

Robots also widen the blast radius. A breach isn't only a data leak; spoofed control channels or manipulated lidar and camera input can make a machine do something physical. Add OTA updates, cloud APIs, message brokers and containerized services, and every layer is its own door.

## Kyber for keys, Dilithium for trust

The NIST post-quantum standards give two lattice-based workhorses. Kyber is a key encapsulation mechanism that replaces RSA and ECC key exchange. Dilithium is a signature scheme, and Nehal maps it to the jobs robots care about most: command authentication and firmware signing, so a robot trusts an update fifteen years from now just as it does today. Open-source libraries exist and hardware support is starting to land.

## Run both until one breaks

Nobody swaps a fleet's crypto overnight. The recommended bridge is hybrid cryptography: classical and post-quantum algorithms side by side, so if either one falls the other still holds. Hybrid TLS or SSH lets you upgrade links without stranding legacy components. It's belt and braces, and in this case wearing both is the design.

The architecture spreads the load sensibly. Robots, with tight compute and power budgets, do lightweight local verification. Edge gateways take on the heavier PQC operations. Cloud APIs, remote debugging and management channels run PQC-enabled TLS or SSH. Zero trust sits across all of it: every device, action and packet verified continuously, with quantum-safe signatures making identities hard to forge later.

## Start with an inventory, not an algorithm

The plan Nehal proposes is refreshingly unglamorous:

1. Build a cryptographic inventory across devices, gateways and cloud pipelines.
2. Prioritize firmware, command channels and OTA.
3. Pilot hybrid TLS on one gateway-to-cloud link and watch handshake latency and compatibility.
4. Check that HSMs, TPMs and secure enclaves can support PQC.
5. Write down governance and incident response.

The pitfalls are just as practical: silent fallback to a weaker algorithm unless policy forbids it, legacy boxes that need wrapping in a secure gateway, vendors without a PQC roadmap, and crypto code that needs independent testing. The closing line is worth stealing for your next budget slide: the "best time to secure these systems was yesterday."

## Who should watch

Robotics and IoT platform engineers, security architects who own device fleets, and anyone writing an OTA pipeline that will outlive its current signing keys. If you already run hybrid TLS in production, this is a checklist rather than news.

## Related Conf42 talks

- [Rajasingh Gandhi Ramdas: Post-Quantum Cryptography for Multi-Cloud APIs](https://www.conf42.com/Cloud_Native_2026_Rajasingh_Gandhi_Ramdas_distributed_systems_architecture) applies the same migration to cloud APIs.
- [Quantum-Resistant Kubernetes](https://www.conf42.com/Kube_Native_2025_Derek_Asir_Muthurajan_Caleb_quantum_security_infrastructure) covers the cluster side of the post-quantum move.
- [Victor Oriakhi: Securing Embedded Systems in IoT](https://www.conf42.com/DevOps_2025_Victor_Oriakhi_iot_embedded_devops) brings a DevOps view to device security.

[Watch Nehal Singh's talk](https://www.conf42.com/Robotics_2025_Nehal_Singh_robotics_quantum_security)

[Watch the talk on YouTube](https://youtu.be/yPdOXma-pcM).

## Watch the talk

[Securing Robot Networks for the Quantum Era](https://www.conf42.com/Robotics_2025_Nehal_Singh_robotics_quantum_security) at Conf42 Robotics 2025.
