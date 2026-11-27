# Watch first, enforce later: firewalls in front of AI services

Conf42 Blog, 2026-01-22, updated 2026-11-09. https://www.conf42.com/blog/devops2026/ngfw-security-for-ai-workloads

In short: Gurdeep Gill of Cisco at Conf42 DevOps 2026 on next-generation firewalls for AI workloads, from identity-based policy as code to model extraction and prompt injection.

Everything in CI is green, no critical CVEs, Terraform compliant, and the AI endpoint you shipped last week is getting requests that feel a little too curious. At Conf42 DevOps 2026, Gurdeep Gill, a software engineering technical leader at Cisco Systems, argued that AI moves the security problem from static code to runtime behaviour, and that next-generation firewalls (NGFWs) can cover that runtime gap without slowing delivery, provided you roll them out in the right order: monitor, then enforce, then optimise.

The talk is told through two characters, Maya who runs a DevOps team shipping several times a day and Luke who is trying to prevent the headline. Gurdeep works at Cisco and the talk is about the NGFW category, but it describes capabilities and rollout patterns rather than demoing a specific product.

## Why AI services are a different security animal

His list of reasons is a good mental checklist. Inputs are unstructured paragraphs, images or audio, so field validation and regex rules help little. Outputs are non-deterministic, which complicates baselining and even reproducing a bug. The model itself is valuable intellectual property that can be copied through its API. Poisoning in the data pipeline may show up much later. And new attack classes, such as prompt injection, adversarial inputs and membership inference, happen at runtime.

That is why he frames the answer as shift left plus shield right. Scanning code, dependencies, containers and IaC stays essential, but misrouted egress, over-broad permissions and abusive API usage look like perfectly valid behaviour to a scanner.

## What a next-generation firewall adds

A legacy firewall reads the address on the envelope; an NGFW also reads what kind of delivery it is, who signed for it, and whether the contents match policy. Concretely: layer 7 awareness of APIs and protocols, payload inspection, a deliberate TLS inspection strategy, behavioural anomaly detection and identity context.

## Identity and policy as code are the foundation

Two ideas carry the integration framework. First, anchor policy on identity, not IPs, which are temporary coordinates in Kubernetes. Identity comes from service mesh mTLS certificates, API gateway tokens and cloud workload identities, so a rule such as letting the inference service reach the model store and feature store, with no open internet egress, travels with the service across clusters, regions and autoscaling.

Second, firewall policy lives in Git. Changes arrive by pull request alongside the service change, CI checks syntax, rule conflicts, forbidden patterns such as overly broad egress, data-location compliance and drift, and policy deploys and rolls back together with the app. Security becomes boring in the best way.

## Learn out of band, then go inline

Inline enforcement can block in real time, and a misconfiguration can also cause downtime. So Gurdeep starts out of band: mirror traffic, build baselines for time of day, release days and legitimately chatty services, measure performance headroom, and see what the firewall would have blocked. Move inline only once that is understood, with high availability, clear failover and performance budgets.

## Model extraction and prompt injection

Model extraction looks like high, uniform, automated query volume probing edge cases from identities that come and go. Maya sees great adoption; Luke sees a pattern that is not human. The response is graduated: detect, warn, throttle, challenge, then block by confidence, so heavy legitimate users are not cut off.

For prompt injection, network controls offer pattern signals, baselines on prompt length and structure, output monitoring for leakage and throttling of identities with repeated jailbreak-like attempts. He is explicit that this is one layer next to application guardrails. The bigger risk is what the model can reach, and identity-based egress policy can stop a tricked model from touching secret stores, metadata endpoints or sensitive databases.

## Encryption, PQC and alerts people trust

He recommends selective decryption of high-risk paths rather than inspecting everything, with capacity planning treated as a security requirement, since a control that cannot keep up gets bypassed. On post-quantum cryptography, it is a planning message for harvest-now-decrypt-later risk: build a cryptographic inventory, prioritise long-lived sensitive data, pilot hybrid approaches. Alerts should arrive as narratives (service identity, deploy version, unusual egress, confidence, suggested action) so they help rather than create a second on-call job.

## Who should watch

Platform and security engineers putting LLM or model-serving endpoints into production, especially where network policy is still ticket-driven. The phased roadmap at the end is a ready-made plan to take back to a team.

## Related Conf42 talks

- [Gentle Introduction to LLM Security](https://www.conf42.com/Large_Language_Models_LLMs_2024_Eugene_Neelou_gentle_introduction_llm_security) by Eugene Neelou covers the application-layer guardrails this talk assumes.
- [When AI Joins the Request Path: Securing API-Backed AI Systems](https://www.conf42.com/DevSecOps_2026_Jayakumar_Ramalingam_apis_inference_guardrails) by Jayakumar Ramalingam looks at the same inference APIs from the API side.
- [Quantum-Resistant Kubernetes: Securing Cloud Native Infrastructure for the Post-Quantum Era](https://www.conf42.com/Kube_Native_2025_Derek_Asir_Muthurajan_Caleb_quantum_security_infrastructure) by Derek Asir Muthurajan Caleb expands on the PQC readiness steps.

[Watch Gurdeep Gill's talk](https://www.conf42.com/DevOps_2026_Gurdeep_Gill_firewalls_ai_protection)

[Watch the talk on YouTube](https://youtu.be/yOMiadE7LtQ).

## Watch the talk

[Building Security Into Your DevOps Pipeline: How NGFWs Protect AI Workloads Without Slowing You Down](https://www.conf42.com/DevOps_2026_Gurdeep_Gill_firewalls_ai_protection) at Conf42 DevOps 2026.
