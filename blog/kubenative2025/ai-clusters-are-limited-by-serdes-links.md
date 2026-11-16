# AI clusters now live or die by their SerDes links

Conf42 Blog, 2025-09-25, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/ai-clusters-are-limited-by-serdes-links

In short: Phani Paladugu (Synopsys) at Conf42 Kube Native 2025 on why AI workloads push SerDes to 224G and beyond, and the power and signal-integrity bill that follows.

Your GPU cluster's bottleneck may be a few millimetres of copper. At Conf42 Kube Native 2025, Phani Paladugu, Executive Director of Product Management at Synopsys, explained why serializer/deserializer (SerDes) links, the high-speed interfaces behind Ethernet and PCIe, have become a design constraint for AI systems, and what chip designers are doing about it.

Fair warning for a Kubernetes crowd: this talk lives below the operating system, at the silicon and package level. That is exactly why it is interesting. Every pod you schedule on an AI node depends on these links.

## Compute grew faster than the wires

Phani's starting point: generative AI model sizes have been doubling every three to four months, training runs stretch into weeks and months despite parallelism, and memory and interconnect bandwidth have not kept pace with compute. So the links have to get faster. Ethernet SerDes are moving from 112G to 224G per lane, and PCIe from 64G to 128G with Gen 7.

Faster alone is not enough. Power efficiency has to stay around four to five picojoules per bit while driving long-reach channels with 45 to 50 dB of loss at 224G, or 35 to 40 dB for PCIe Gen 7. At those rates reflections, crosstalk, jitter and inter-symbol interference all get worse. He calls the combination a design paradox, and it is hard to disagree.

## Training and inference want different links

A point software people rarely hear: workload shape should drive SerDes design. Inference traffic is bursty, often asymmetric, more memory-bound than compute-bound, and latency-sensitive. Training is compute-bound and needs sustained high bandwidth, with latency still mattering. Phani's advice is to understand the exact use case before optimising for performance, power, area and latency, because no single design wins all four.

## PAM4, DSPs and machine-learned tuning

The signal chain has changed. Older NRZ SerDes used analogue equalisers: a feed-forward equaliser on transmit, and a continuous-time linear equaliser plus decision-feedback equaliser on receive. At today's rates the signalling moved to PAM4, and receivers became DSP-based, with multi-tap equalisers and high-performance data converters. That shift toward digital architectures also lets designers ride process scaling and voltage scaling for power.

Real-time adaptation tunes parameters to each channel, and machine learning algorithms now handle calibration and adaptation. Clock and data recovery uses digital bang-bang phase detectors and multi-phase sampling, and forward error correction (Reed-Solomon or LDPC) is chosen against the channel's loss, power and latency budget.

Configurability matters too: lanes configurable from one to sixteen, and multi-protocol SerDes that can serve Ethernet or PCIe on the same silicon.

## Hundreds of lanes, one power budget

AI chips use hundreds of SerDes lanes, so power is attacked at every level: supply scaling, adaptive biasing and clock gating in circuits; power islands and workload-aware power states in the architecture; dynamic voltage and frequency scaling and thermal-aware floorplanning at the system level. Placement on all four edges of the die and the package escape routing become part of the design.

Phani also maps links to topologies: Ultra Accelerator Link for scale-up inside a system, Ultra Ethernet for scale-out across the data centre.

## What comes after 224G

Ethernet is heading to 448G per lane within two to three years, with PCIe and UALink following. Co-packaged optics moves the optics next to switches and accelerators, cutting channel loss and the need for long-reach SerDes, and Phani cited five to eight times more bandwidth with two to three times less power from these technologies. Chiplets and 3D packaging bring their own SerDes requirements.

## Who should watch

Infrastructure and platform engineers who buy, rack or schedule AI hardware and want to understand why network and node specs look the way they do. Hardware engineers will find it a compact overview; Kubernetes operators will find it a useful look under the floor.

## Related Conf42 talks

- [Overcoming Interconnect Bottlenecks in GPU-Accelerated HPC Clusters for Scalable Exascale Performance](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Murali_Krishna_Reddy_Mandalapu_overcoming_interconnect_bottlen) by Murali Krishna Reddy Mandalapu (Renesas Electronics), the cluster-level view.
- [AI Infrastructure over Ethernet: Secure, Scalable, High-Performance Design](https://www.conf42.com/DevSecOps_2025_Nazim_Khan_ethernet_ai_infra) by Nazim Khan (Cisco Systems), from the network side.
- [Machine Learning Innovations in Hardware Verification for High-Speed Protocol Testing](https://www.conf42.com/Machine_Learning_2025_Jena_Abraham_hardware_verification_innovations) by Jena Abraham (Intel Corporation), on testing these links.

[Watch Phani Paladugu's talk](https://www.conf42.com/Kube_Native_2025_Phani_Paladugu_serdes_ai_architectures)

[Watch the talk on YouTube](https://youtu.be/nkDGvtQzvZg).

## Watch the talk

[Reimagining SerDes for Scalable AI: Architectures, Bottlenecks, and Breakthroughs](https://www.conf42.com/Kube_Native_2025_Phani_Paladugu_serdes_ai_architectures) at Conf42 Kube Native 2025.
