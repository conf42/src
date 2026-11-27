# Microservices, edge and serverless from a JavaScript architect's view

Conf42 Blog, 2025-10-30, updated 2026-11-09. https://www.conf42.com/blog/js2025/microservices-edge-and-serverless-for-js-architects

In short: Ford Credit tech lead Surya Prabha Busi surveyed microservices, edge, multi-cloud, serverless and zero trust for JS teams at Conf42 JavaScript 2025.

JavaScript started as the language of the browser and now runs a good share of the cloud. At Conf42 JavaScript 2025, Surya Prabha Busi, Technical Lead at Ford Credit with more than 18 years of building cloud-native applications, gave a tour of the architecture choices JavaScript teams now face: microservices, edge computing, multi-cloud, serverless, a look at quantum computing, and the zero trust security that has to wrap all of it.

This is a survey talk. It covers a lot of ground quickly, with industry figures on each slide, and works best as a briefing for someone stepping into architecture decisions.

## From monolith to services, and the hard part in between

She starts with the familiar story. A monolith ships frontend, backend and business logic as one unit, which is simple until the app grows and every update becomes risky. Microservices split that into independent services with their own logic, easier to deploy, update and scale where traffic actually is.

She cited adoption rising from 45% in 2019 to 91% in 2024, a 76% reduction in deployment time and around 50% operational cost savings from smaller, containerised services. The challenge she highlighted is the one every team hits: drawing the service boundaries. Decomposing business logic into services takes real domain knowledge, and she put the share of teams struggling with it at 67%.

## Edge computing belongs in the first design

Edge computing moves computation closer to where data is produced, which matters most where data is time-sensitive, such as healthcare and manufacturing. Her figures: 45% faster processing, 42% better real-time data handling, a 33% efficiency boost in healthcare and 56% faster emergency response in manufacturing. Her practical point is that edge has to be planned from the start of an application's design, not retrofitted.

## Multi-cloud: flexibility you pay for in governance

On multi-cloud she was candid about the trade-off. Early adopters ran into integration problems, and choosing between public, private and hybrid cloud is a real decision: public is cheaper because you share it, private costs more but is yours alone, hybrid mixes both. With structured governance she cited up to 41% reduction in governance overhead and 32% cost optimisation. Success, in her framing, depends on orchestrating public, private and edge resources based on how critical the data is.

## Serverless, quantum, and zero trust

Serverless cuts development cycles (she cited 33%) by removing infrastructure work, with automatic scaling and pay-per-execution pricing. Quantum computing got an honest label: still research, with quantum-inspired algorithms starting to show up in JavaScript libraries, worth knowing about rather than planning around.

Security closes the talk. More services and more clouds mean more surface, so she recommends zero trust: least privilege, access granted on need, and continuous authentication and authorisation for every service integration.

## Who should watch

Developers moving into a lead or architect role who want one session that names the main architectural options and their trade-offs. Experienced platform engineers will know the material; the figures are useful conversation starters, but the talk doesn't break down where each one comes from, so check sources before putting them in a business case.

## Related talks

- [Embracing Hexagonal Architecture with Serverless](https://www.conf42.com/JavaScript_2021_Luca_Mezzalira_hexagonal_architecture_serverless) shows how to structure serverless JavaScript code.
- [Patterns for efficient serverless development](https://www.conf42.com/Cloud_Native_2024_Yan_Cui_patterns_efficient_serverless) is a practitioner's view of the same model.
- [Multi-Cloud Magic: Leveraging Multi-Cloud Clusters in Real-World Scenarios](https://www.conf42.com/Cloud_Native_2021_Adrienne_Tacke_multicloud_magic_clusters) gets specific about running across clouds.

[Watch Surya Prabha Busi's talk](https://www.conf42.com/JavaScript_2025_Surya_Prabha_Busi_building_microservices_edge)

[Watch the talk on YouTube](https://youtu.be/mZn4e0390no).

## Watch the talk

[Building the Future: Microservices, Edge & Cloud Innovation at Scale](https://www.conf42.com/JavaScript_2025_Surya_Prabha_Busi_building_microservices_edge) at Conf42 JavaScript 2025.
