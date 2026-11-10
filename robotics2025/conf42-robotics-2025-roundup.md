# Conf42 Robotics 2025: the software and rules around the robots

Conf42 Blog, 2025-11-21. https://www.conf42.com/robotics2025/conf42-robotics-2025-roundup

In short: Conf42 Robotics 2025 roundup - post-quantum robot networks, DO-178C for electric aircraft, compliance-by-design, and AI in clinics and disaster response.

Conf42 Robotics 2025 ran online on November 20, 2025, with nine talks, and almost none of them were about motors or grippers. The lineup was about everything that has to be true around a robot before anyone lets it loose: how its network survives quantum computers, how its flight software gets certified, how its decisions are audited, and what data infrastructure feeds it. If you build the systems that robots plug into, this was your kind of robotics conference.

All talks are on the [Conf42 Robotics 2025 event page](https://www.conf42.com/robotics2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrDUt9JKK5BDogRgpbqPK4wc).

## Robots outlive their cryptography

The sharpest framing of the day came from [Nehal Singh](https://www.conf42.com/Robotics_2025_Nehal_Singh_robotics_quantum_security) of California State University, Long Beach. The robots deployed today in manufacturing, healthcare, defence, and logistics will still be running five, ten, even fifteen years from now. Large quantum computers are not here yet, but a fleet with that lifespan has to assume they will arrive while it is still in service. Robotic systems combine long-lived hardware, sensitive operational data, and real-time autonomy, which makes them an attractive target.

The talk walks through post-quantum cryptography based on the NIST standards, with the constraint robotics engineers care about most: securing the network without breaking real-time performance. A useful one if your hardware refresh cycle is measured in decades rather than sprints.

## Certification is the long pole

[Charles Antony Raj](https://www.conf42.com/Robotics_2025_Charles_Antony_Raj_avionics_certify_flight), Senior Manager of Systems and Software Engineering at Collins Aerospace, brought about two decades of aerospace experience to a problem most software engineers never meet: certifying flight software under DO-178C when it runs on multicore processors. Multicore chips are what electric aircraft programmes want for performance, and they are also what makes interference between cores hard to bound and hard to prove safe.

The talk covers the certification paths and strategies for cutting the delays they cause. It is a rare look at what "shipping" means when the regulator, not the CI pipeline, is the final gate.

## Compliance as an architecture choice

Two talks treated regulation as a design input rather than paperwork bolted on at the end.

[Sneha Nallapu](https://www.conf42.com/Robotics_2025_Sneha_Nallapu_compliance_design_finance) of J.B. Hunt Transport Services made the case for compliance-by-design in automated financial systems. The patterns are ones backend engineers will recognise: event sourcing, bi-temporal data so you can answer what you knew and when, graph lineage, CQRS, and adaptive workflows. Audit trails stop being a report someone generates and become a property of the system.

[Vinaya Nadig](https://www.conf42.com/Robotics_2025_Vinaya_Nadig_governance_banking_robots), a Principal Engineer at Amazon, opened with the 2008 financial crisis: algorithms making decisions with opaque logic and incomplete data, long before generative AI. Today AI approves loans, flags fraud, and advises on investments in real time. The argument is that a unified AI data governance framework is what keeps banking automation from repeating that history at machine speed.

## AI and robotics where the stakes are human

[Srinivasa SKN Ambati](https://www.conf42.com/Robotics_2025_Srinivasa_SKN_Ambati_healthcare_analytics_ai), an Engineer Lead at Anthem, looked at how advanced analytics and AI are changing clinical robotics, with an emphasis on building systems that are scalable and compliant enough for patient care.

[Vivek Karnam](https://www.conf42.com/Robotics_2025_Vivek_Karnam_cloud_response_robots) of Surge Technology Solutions started from the shortcomings of traditional emergency response and showed how cloud computing, robotics, and predictive analytics can combine into faster, smarter disaster response frameworks.

## The infrastructure underneath

The remaining talks went one layer down, to the data and even the walls that robotic systems depend on.

- [Adithya Sirimalla](https://www.conf42.com/Robotics_2025_Adithya_Sirimalla_oracle_azure_cloud) of Enliven Technologies gave a practical framework for tuning Oracle and SQL Server on AWS and Azure, on the premise that in automation every millisecond of database latency can shape a real-time decision.
- [Ankita Saxena](https://www.conf42.com/Robotics_2025_Ankita_Saxena_ai_insights_industry), a Senior Product Manager at Amazon, traced recommendation systems from a "you may also like" widget to strategic infrastructure, including in robotics-enabled marketplaces.
- [Rahul Pingale](https://www.conf42.com/Robotics_2025_Rahul_Pingale_iot_materials_smart), Technical Director at Wallquest, gave the most unexpected talk of the day: PVC-free non-woven wall surfaces with embedded sensors and connectivity, turning something as ordinary as a wall into part of a smart environment. Proof that the edge can be quite literal.

## Sponsors and what's next

Thanks to [LLMday](https://llmday.com/), the in-person LLM engineering conference series, which joined as a gold sponsor, and to the newsletter, podcast, and media partners listed on the event page.

Robotics 2025 was the first Conf42 event dedicated to the topic. For more hardware-meets-software talks, the [Conf42 IoT 2025](https://www.conf42.com/iot2025) lineup is the closest neighbour, and the [full robotics playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrDUt9JKK5BDogRgpbqPK4wc) is there whenever you have an evening and a soldering iron cooling down.
