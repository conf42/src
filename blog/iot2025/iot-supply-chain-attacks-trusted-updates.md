# IoT supply chain attacks come in through the trusted update

Conf42 Blog, 2025-12-18, updated 2026-11-09. https://www.conf42.com/blog/iot2025/iot-supply-chain-attacks-trusted-updates

In short: Cybersecurity risk analyst Gresshma Atluri at Conf42 IoT 2025 on defending connected devices from supply chain attacks with secure by design and zero trust.

The scariest IoT attacks do not break down the front door; they ship inside the box. At Conf42 Internet of Things (IoT) 2025, cybersecurity risk analyst Gresshma Atluri laid out how supply chain attacks reach connected devices through firmware, components and trusted updates, and the governance-heavy playbook she uses with regulated industries to push back.

Gresshma comes at this from GRC work rather than exploit research, and the talk reads that way: a structured walk from threat to roadmap, built on her research and consulting in heavily regulated sectors. It is a strategy talk, not a hands-on hardening lab.

## One component, one mistake

She opens with a story from a hospital she consulted for. A small pump from a trusted vendor carried a vulnerability in its firmware, introduced during manufacturing, which allowed unauthorized access. Nobody checked, because the vendor was trusted, and patient safety was suddenly on the line.

That is the core of her argument: trust is implicit across the IoT supply chain, so attackers aim for the parts nobody inspects. She lists the attack surface in layers. Microcontrollers and chips sourced from many countries, third party and open source code that may be outdated or malicious, contract manufacturers who do not follow security processes, update servers that can push malware as a legitimate update, and cloud backends whose compromise hands over every connected device at once.

The examples are familiar but still sobering: Mirai turning default passwords on baby monitors and cameras into a global DDoS, and a logistics firm she worked with where smart scanners were hijacked through compromised firmware to gain a foothold in backend systems. Her line about a toaster talking to the light hub, and both talking to the Wi-Fi, is the most concise threat model of a smart home you will hear.

## Secure by design, then trust nothing

The defensive half starts with building security in rather than patching it on later. Her analogy is earthquake-proofing in California: you reinforce the structure before the quake, not after. The must-haves she lists are threat modeling when a product is designed, hardware features such as secure boot, vetting suppliers the way you would vet a new hire (including their breach history), and maintaining a software bill of materials so you always know what is running on a device.

On top of that comes zero trust. Every device, request and update must prove it is legitimate. Each device gets a unique identity, talks only to the services it actually needs, encrypts all communication and receives only the access it requires.

## Behaviour beats signatures

Signature-based detection loses the race, she argues, because attackers change faster than signature databases. Behaviour modeling catches the device that suddenly sends far more traffic than usual at 2 AM. Her comparison is a fitness tracker that knows your resting heart rate and flags an unexplained spike.

Incident response gets its own IoT-flavoured checklist: detect both digital and physical anomalies, contain by segmenting smartly instead of shutting down a whole network, investigate with IoT-specific forensic tools, remediate by distributing clean firmware securely, then feed the lessons back into controls.

## Start with the boring wins

The roadmap is refreshingly unglamorous. Begin with a maturity assessment, kill default passwords, tighten password policy, and do basic segmentation. Then build cross-functional teams spanning security, supply chain and product, and track live metrics such as time to detect and time to fix. Her closing ask is aimed at manufacturers and buyers alike: do not trade security for the cheapest part, push for transparent supply chains, and expect more regulation and lightweight cryptography for constrained devices.

## Who should watch

Security, risk and procurement folks who need a shared vocabulary for IoT supply chain risk, and product teams starting a connected device who want a checklist to argue from. If you are after firmware reverse engineering or attestation code, this is the wrong half hour.

## Related Conf42 talks

- [Nathalie Takpah on the impact of IoT on supply chain cyber security](https://www.conf42.com/DevOps_2025_Nathalie_Takpah_iot_supply_chain_security) at Conf42 DevOps 2025.
- [Swapnil Shinde on blockchain for secure, immutable firmware updates](https://www.conf42.com/Internet_of_Things_IoT_2023_Swapnil_Shinde_blockchain_immutable_firmware) at Conf42 IoT 2023.
- [Brian Contos on what two million interrogated enterprise IoT devices revealed](https://www.conf42.com/Incident_Management_2022_Brian_Contos_cameras_cacs_clocks_enterprise_iot) at Conf42 Incident Management 2022.

[Watch Gresshma Atluri's talk](https://www.conf42.com/Internet_of_Things_IoT_2025_Gresshma_Atluri_security_supplychain_defense) from [Conf42 IoT 2025](https://www.conf42.com/iot2025).

[Watch the talk on YouTube](https://youtu.be/xXIjY2Bo2PM).

## Watch the talk

[IoT Supply Chain Security: Defending Connected Device Ecosystems from Cyberattacks](https://www.conf42.com/Internet_of_Things_IoT_2025_Gresshma_Atluri_security_supplychain_defense) at Conf42 Internet of Things (IoT) 2025.
