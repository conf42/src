# Conf42 Quantum Computing 2025: hybrid sidecars, cloud QPUs and PQC

Conf42 Blog, 2025-06-20. https://www.conf42.com/quantum2025/conf42-quantum-computing-2025-roundup

In short: Conf42 Quantum Computing 2025 roundup: 19 talks on preparing architecture and cryptography, cloud quantum services, hybrid sidecars and finance use cases.

Conf42 Quantum Computing 2025 ran on June 19, 2025, with 19 talks and a useful tension between them. Some speakers treated quantum advantage as a business plan for this year; the most practical ones treated it as an engineering problem: wrap a small, noisy quantum core in classical systems you already run, and get your architecture and cryptography ready before the hardware forces the issue. The full lineup is on the [event page](https://www.conf42.com/quantum2025) and the recordings are in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrDLJsZ2QLy2_0A5YjP6CaRq).

## Get ready before the hardware is

[Laxmikanth Mukund Sethu Kumar](https://www.conf42.com/Quantum_Computing_2025_Laxmikanth_Mukund_Sethu_Kumar_classical_quantum_enterprise), Executive Director at JPMorgan Chase, gave the most grounded framing of the day. Quantum isn't production-ready for every enterprise use case, he said, but architects can lay groundwork now with patterns they already know: event-driven design, hybrid orchestration and API-driven interfaces that a quantum service could slot into later. He drew on platforms he has designed for banks, airlines and government systems, and kept the quantum mechanics to a minimum.

The cryptography side got its own warning. [Pavan Nutalapati](https://www.conf42.com/Quantum_Computing_2025_Pavan_Nutalapati_quantum_cloud_security) laid out how quantum computing threatens today's encryption in the cloud, the emerging standards, and how to build a quantum-safe strategy. [Sarah Choudhary](https://www.conf42.com/Quantum_Computing_2025_Sarah_Choudhary_quantum_algorithms_problem) covered the algorithms behind the cryptography and optimisation headlines for anyone who wants to know what the machines would actually run.

## Quantum arrives as a cloud service

Most engineers will meet quantum hardware through an API. [Naga Murali Krishna Koneru](https://www.conf42.com/Quantum_Computing_2025_Naga_Murali_Krishna_Koneru_cloud_aws) of Hexaware Technologies walked through Amazon Braket and hybrid quantum-classical workflows on AWS. [Srinivas Sriram Mantrala](https://www.conf42.com/Quantum_Computing_2025_Srinivas_Sriram_Mantrala_quantum_cloudops_devops) explored what quantum-enhanced DevOps and hybrid cloud integration could look like, and [Srikar Kompella](https://www.conf42.com/Quantum_Computing_2025_Srikar_Kompella_quantum_saas_architecture) of Twilio looked at multi-tenant SaaS architecture where quantum and edge processing meet.

Then [Denish Tomar](https://www.conf42.com/Quantum_Computing_2025_Denish_Tomar_quantum_cloud_qum) of Qumulus asked the question nobody else did: who is going to understand the bill? He opened with a founder whose usual monthly cloud spend jumped several times over because an autoscaling setting sent a cluster to 50 servers instead of five, for three days instead of two hours. If we can't predict classical cloud costs, he argued, usage-based pricing for quantum will be worse, and bundled, predictable resource models are the way out. The only quantum talk of the year where the scariest number was on an invoice.

## Hybrid sidecars and research tooling

Two talks showed what a sensible first step looks like. [Pradeep Karanam](https://www.conf42.com/Quantum_Computing_2025_Pradeep_Karanam_plm_teamcenter) of Facebook described a small sidecar for Siemens Teamcenter, the product lifecycle management system, that sends only the hardest part of a "what if" question about product options or purchase plans to a cloud quantum computer. Everyone's daily workflow stays the same, and the classical system does everything else. He also explained why today's noisy machines are always wrapped in classical code.

[Vamsi Praveen Karanam](https://www.conf42.com/Quantum_Computing_2025_Vamsi_Praveen_Karanam_low_code_experimentation) of Amazon tackled the research side with a schema-driven approach: one JSON schema, stored versioned and immutable, generates a React control panel, a serverless Step Functions workflow that runs and post-processes circuits, and a lineage tracker that tags every run. Researchers edit a manifest instead of copying notebooks, and the audit trail comes for free.

## Finance wants to go first

Financial services supplied the most use cases, and the most optimism. [Nikhil Kassetty](https://www.conf42.com/Quantum_Computing_2025_Nikhil_Kassetty_quantum_payments_latency) of Intuit looked at how quantum could affect real-time payments, fraud detection and settlement, based on emerging pilots and experiments. [Venkateswarlu Boggavarapu](https://www.conf42.com/Quantum_Computing_2025_Venkateswarlu_Boggavarapu_finance_optimization) of JPMorganChase covered data engineering for quantum-enhanced personalisation, and [Siva Prakash](https://www.conf42.com/Quantum_Computing_2025_Siva_Prakash_quantum_data_streaming) and [Ganesh Marimuthu](https://www.conf42.com/Quantum_Computing_2025_Ganesh_Marimuthu_quantum_trading_systems) took on streaming feature stores and trading systems. [Sai Kaushik Ponnekanti](https://www.conf42.com/Quantum_Computing_2025_Sai_Kaushik_Ponnekanti_quantum_business_value) of Meta argued that business value is available in the NISQ era already, with today's noisy machines.

## Edge and IoT

Two speakers pushed quantum toward the edge. [Anushree Nagvekar](https://www.conf42.com/Quantum_Computing_2025_Anushree_Nagvekar_quantum_edge_ai) of AEye presented a hybrid quantum-classical architecture for embedded edge AI, and [Gayathri Jeganmohan](https://www.conf42.com/Quantum_Computing_2025_Gayathri_Jeganmohan_quantum_iot_security) of Microsoft looked at what quantum means for IoT security and optimisation as device counts keep climbing.

## Sponsors

Thanks to [Rapydo](https://www.rapydo.io/), our gold sponsor, to [StarterAI](https://www.starterai.dev/) for the newsletter and to [HockeyStick](https://www.hockeystick.show/) for the podcast partnership.

## What's next

All 19 talks are linked from the [Conf42 Quantum Computing 2025 page](https://www.conf42.com/quantum2025). Next on the Conf42 calendar is [Conf42 Rustlang 2025](https://www.conf42.com/rustlang2025) on August 21, a good place to rewrite your classical half in something memory-safe while the qubits settle down.
