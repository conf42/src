# Breaking up a payment monolith moves PCI from network to service

Conf42 Blog, 2025-12-01, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/payment-gateway-microservices-devsecops

In short: Silpa Potluri of GoodLeap at Conf42 DevSecOps 2025 on keeping payment gateways PCI-compliant while migrating from monoliths to microservices.

A payment monolith is slow to change and, for the same reason, easy to fence in. Split it into dozens of services and the fence disappears. At Conf42 DevSecOps 2025, [Silpa Potluri](https://www.conf42.com/DevSecOps_2025_Silpa_Potluri_payment_api_secure) of GoodLeap, who brings two decades in software and more than ten years in payments, explained how DevSecOps keeps payment gateways secure and PCI-compliant through a monolith-to-microservices migration, and why compliance has to move from the network to the individual service.

It's a clear overview talk, good for teams at the start of such a migration. It names the right patterns rather than showing implementations.

## Why payments left the monolith

Potluri starts with the business pressure. Payment systems were built as large monoliths, stable and predictable but slow and risky to modify, with long development cycles. Real-time payments, international commerce, mobile-first users and round-the-clock demand pushed processors towards microservices for agility, independent scaling, faster updates and better fault isolation. The catch is that the same architecture makes security and compliance much harder.

Her framing of DevSecOps is the familiar contrast: security used to arrive at the end, after development and QA, which caused delays and friction. With several deployments a day that model can't keep up, so security moves into design, build, deployment and operations.

## PCI DSS stops being a perimeter

The core of the talk is what changes for PCI DSS, which sets rules for protecting cardholder data, access control, network segmentation, encryption, logging and monitoring. Monolithic setups leaned on perimeter controls: isolated networks, firewalls, DMZs. In microservices, data moves across many services, the perimeter blurs and the attack surface grows. So compliance has to go from network-based to service-based, and it becomes a constant priority rather than an annual exercise.

She names three shifts. The attack surface expands, from one app to many entry points. Infrastructure becomes dynamic, with containers scaling up and down constantly. And security responsibility becomes shared across every team and service.

## The architecture that replaces the fence

Her answer comes in layers. A service mesh provides mutual TLS, authorisation and traffic policies automatically, so developers aren't hand-coding them. An API gateway acts as the secure front door with authentication, rate limiting, threat detection and input validation. Zero trust means every service authenticates and authorises every request, internal ones included.

For the data itself: tokenisation replaces card data with tokens to shrink PCI scope, data at rest is encrypted with keys in a secure vault, everything in transit uses TLS, and secrets live in vaults rather than code, environment files or repos. Defence in depth, applied to the thing attackers want most.

## Automation keeps security at deployment speed

To the obvious objection, that all these checks will slow releases, her answer is to automate them: static analysis early, dynamic testing against running applications, container image scanning. Infrastructure as code gives consistent, version-controlled environments, and compliance as code turns PCI requirements into automated checks, so compliance is validated on every deployment instead of waiting for the quarterly or annual audit.

In the pipeline she lists source control protections (secret detection, required reviews), dependency scanning in the build, artifact signing so images and binaries are trusted and unmodified, deployment gates that block insecure builds, and quick rollbacks. After deployment, detection matters: a SIEM to correlate logs, real-time fraud detection models, distributed tracing to follow a single transaction across services, and anomaly detection. On cloud platforms she reminds teams of the shared responsibility model: the provider secures the platform, you still own code, configuration and access.

## How migrations succeed

Her success strategies are practical: migrate in phases, start small and iterate; appoint security champions on each team; threat model before writing code; and keep test environments close to production so real vulnerabilities show up. The abstract mentions a drop in security incidents alongside daily releases; the talk itself focuses on the patterns that get you there.

## Who should watch

Engineers and architects planning or in the middle of a payments migration, and compliance owners who need to understand what changes when the cardholder data environment becomes a mesh of services.

## Related Conf42 talks

- [IoT Payment Systems: Microservices Architecture for Connected Devices](https://www.conf42.com/Internet_of_Things_IoT_2025_Silpa_Potluri_payments_microservices_architecture) is Potluri on payment microservices for connected devices.
- [AI-Powered Fraud Detection in Cloud-Native Digital Payments](https://www.conf42.com/Cloud_Native_2025_Sandeep_Katuri_fraud_detection_digital_payments_security) expands the detection layer.
- [Distributed Transactions in Service Mesh](https://www.conf42.com/Chaos_Engineering_2022_Alparslan_Avci_distributed_transactions_in_service_mesh) tackles consistency once payments span services.

[Watch Silpa Potluri's talk](https://www.conf42.com/DevSecOps_2025_Silpa_Potluri_payment_api_secure)

[Watch the talk on YouTube](https://youtu.be/mBQhrJ3eS2s).

## Watch the talk

[Securing Payment Gateway Evolution: DevSecOps in Microservices Migration](https://www.conf42.com/DevSecOps_2025_Silpa_Potluri_payment_api_secure) at Conf42 DevSecOps 2025.
