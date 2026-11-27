# Edge devices sit outside your monitoring, and attackers know it

Conf42 Blog, 2025-06-05, updated 2026-11-09. https://www.conf42.com/blog/obs2025/edge-device-security-observability

In short: Chintan Udeshi of Palo Alto Networks at Conf42 Observability 2025 on real-time observability for edge devices as the first step in edge security.

Edge devices live outside the network boundary your monitoring tools were built for, which makes them an attractive way in. At Conf42 Observability 2025, Chintan Udeshi, a principal product manager at Palo Alto Networks, made the case that real-time observability of edge devices is where edge security starts, and laid out a roadmap from one device to a global fleet.

He is clear that monitoring is only the first step, and the talk spends real time on what has to come after it.

## Why the edge keeps growing

Chintan opens with the three reasons workloads move to the edge: latency drops to milliseconds for near-real-time applications; operations keep working when the internet does not (his example is a self-driving car in a remote area that still has to make critical decisions); and local processing saves bandwidth. He cites market projections showing steep growth through the next decade, which is why the security problem is getting bigger.

## Three ways in

The threat section explains why edge is different. Devices operate outside traditional network boundaries, so the cloud and on-prem monitoring stack does not see them. Legacy tools lack edge-specific threat detection. And edge hardware has limited CPU and memory, so teams often trade security capability for speed. He cites a study finding that 45% of organisations had at least one significant edge security incident in the past year.

The attack patterns follow from that:

- **Entry point and lateral movement:** compromise an edge device, then move into cloud and on-prem systems.
- **Data breaches:** poorly secured devices often hold unencrypted data.
- **DDoS:** limited devices cannot fend off sophisticated botnet traffic.

## What edge observability needs to do

His spec has three parts. Equip devices with small micro-agents that watch behaviour alongside CPU and memory use, so subtle deviations from known-normal stand out. Correlate those signals across all edge devices, not one at a time, so an attack shows up as a pattern. And automate the response, isolating a compromised device within milliseconds instead of waiting for a human, so threats do not move laterally.

The case study is a large automotive manufacturing plant that ran edge security monitoring for three months. Chintan reports fewer incident escalations, most unauthorised access attempts between edge and core infrastructure identified, and mean time to detection falling from 197 hours to about four.

## Monitoring is the start, not the finish

The section worth pausing on is his list of controls that must sit on top of visibility: continuous authentication in line with zero trust, least-privilege access, micro-segmentation so one infected device cannot reach everything, and runtime protection against unknown vulnerabilities. His reminder for that last one is Log4j, disclosed in December 2021 after sitting in software for years.

## The rollout roadmap

The implementation advice is incremental: inventory edge devices and their weak points, pick the most critical device, instrument it, and measure mean time to detection and lateral movement. Then integrate edge telemetry with the rest of the platform (public cloud, private cloud, on-prem, network fabric and IoT) for a single view, and finally expand to the whole worldwide fleet.

## Who should watch

Security and platform engineers responsible for factories, retail sites, vehicles or any fleet of devices that never touches the data centre. It is a product manager's strategic overview, vendor-neutral in content, without product demos or config.

## Related Conf42 talks

- [Venukumar Chirlawar on Rust in edge computing for performance and security](https://www.conf42.com/Rustlang_2024_Venukumar_Chirlawar_edge_computing_security) (Rustlang 2024).
- [Naveen Kumar Birru on implementing zero trust at enterprise scale](https://www.conf42.com/Machine_Learning_2025_Naveen_Kumar_Birru_zero_trust_enterprise) (Machine Learning 2025).
- [Thomas Labarussias on protecting applications with Falco and eBPF](https://www.conf42.com/Observability_2023_Thomas_Labarussias_falco_ebpf_protect_applications) (Observability 2023), for runtime detection in practice.

[Watch Chintan Udeshi's talk](https://www.conf42.com/Observability_2025_Chintan_Udeshi_edge_realtime_security)

[Watch the talk on YouTube](https://youtu.be/jH0ztwU3vxI).

## Watch the talk

[Real-Time Edge Observability: The New Frontier of Security Monitoring and Threat Detection](https://www.conf42.com/Observability_2025_Chintan_Udeshi_edge_realtime_security) at Conf42 Observability 2025.
