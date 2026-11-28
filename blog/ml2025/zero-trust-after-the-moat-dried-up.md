# Zero trust starts where the castle and moat stop working

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/zero-trust-after-the-moat-dried-up

In short: AWS's Vaibhav Anil Vora walked through zero trust at Conf42 Machine Learning 2025, from least privilege and microsegmentation to adaptive authentication.

For decades the security model was a castle with a moat: strong walls, and once you were inside, everyone trusted you. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Vaibhav Anil Vora, Senior Cloud Technical Account Manager at AWS, explained what replaces it when cloud, remote work and supply chains drain the moat: continuous verification of every request, from every user and device, every time.

It's a thorough, well-structured overview of the zero trust model, and a good choice if you need the whole picture in one sitting.

## Verified a minute ago means nothing now

Vora's core point is that zero trust treats each access request as potentially hostile, even if the same user was verified a minute earlier. Identity becomes the main control point. He rests it on three foundations: continuous verification, least privilege, and comprehensive monitoring, because you can't verify what you can't see.

The history section explains why the old model failed in practice. Attackers who got past the perimeter could move laterally with little resistance and then linger undetected for long periods. The response was a conceptual shift from asking where a request came from to asking who or what is making it and what it wants to reach. The working assumption becomes: assume breach.

## Least privilege has a clock on it

The least-privilege section is more detailed than most. Just-in-time access grants elevated rights only for a specific task and only for its duration, shrinking the window an attacker can use. Attribute-based controls decide access on device health, location, time of day and data sensitivity, not just role. Identity governance keeps checking whether permissions are still needed after people change teams.

Microsegmentation gets similar care. Software-defined networking sets policy centrally, independent of the physical network. Application-layer segmentation restricts traffic by the identity of the software rather than IPs and ports, which holds up when the network changes underneath. Workload isolation goes down to individual containers or processes. None of it works without dependency mapping: you need to know which services legitimately talk to which before you write the rules.

## Risk scores decide how hard to ask

The adaptive authentication walkthrough is the most practical part. Establish a baseline of normal behaviour, monitor telemetry from endpoints, networks, apps and identity systems in real time, score each access attempt on behaviour, device, location, time and resource sensitivity, then respond. Low risk means standard MFA. High risk, such as sensitive data from a new location at an odd hour, means extra steps, a block, or an alert. Data gets its own track: discover sensitive data, classify it against rules like GDPR and HIPAA, protect it with encryption and DLP, then govern its use.

For rollout, he recommends assess, plan, phase and integrate: start with high-value or high-risk environments, and adapt the security gateways and proxies you already own rather than ripping everything out. Zero trust, in his words, is a journey rather than a destination.

## Who should watch

Engineers and architects who keep hearing zero trust in planning meetings and want a structured, vendor-light explanation. There's no product demo despite the AWS badge. If you already run JIT access and service identity everywhere, the future-trends section on ML behavioural analytics and DevSecOps is the part to skip to.

## Related Conf42 talks

- [Don't Trust anyone... Secure your Microservices with ZeroTrust approach](https://www.conf42.com/Kube_Native_2023_Jonathan_Vila_secure_microservices_zerotrust_approach) by Jonathan Vila shows the model in microservice code.
- [Zero Trust MLOps: Securing AI Pipelines from Development to Production](https://www.conf42.com/MLOps_2025_Sudheer_Obbu_zero_trust_mlops) by Sudheer Obbu applies it to ML pipelines.
- [Real Zero Trust Security for Containerized Environments](https://www.conf42.com/JavaScript_2024_Ammar_Khan_zero_trust_security) by Ammar Khan takes it into containers.

[Watch Vaibhav Anil Vora's talk](https://www.conf42.com/Machine_Learning_2025_Vaibhav_Anil_Vora_zero_trust_security)

[Watch the talk on YouTube](https://youtu.be/m6dLQazzP0E).

## Watch the talk

[Zero Trust Security: From Perimeter Defense to Continuous Verification in the Modern Enterprise](https://www.conf42.com/Machine_Learning_2025_Vaibhav_Anil_Vora_zero_trust_security) at Conf42 Machine Learning 2025.
