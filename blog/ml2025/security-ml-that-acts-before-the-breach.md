# Signature-based security can't see a zero-day; baselines can

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/security-ml-that-acts-before-the-breach

In short: Amazon's Dinesh Rajasekharan explained at Conf42 Machine Learning 2025 how anomaly detection, pattern mining and threat intel make security predictive.

If your defence works by matching known attack signatures, a brand-new tactic sails straight through it. At [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025), Dinesh Rajasekharan, a product management leader for security and developer experience at Amazon, made the case for moving security from reactive to predictive with machine learning, and was candid about the parts that still don't work well.

It's a brisk talk, around ten minutes, that works as an executive-level map of AI in security operations.

## Three reasons the old model runs out of road

Rajasekharan frames the problem with the projected global cost of cybercrime, $10.5 trillion a year by 2025, then lists why traditional security can't keep up. It's reactive and only kicks in after damage is done. The volume of data in modern networks overwhelms static rules. And signature-based detection depends on known attack vectors, so a zero-day leaves you blind. His image for it is using a map of the past to navigate terrain that keeps moving.

As examples of what ML can do, he cites MIT's AI2 platform detecting 85% of attacks, and a financial firm seeing a 60% drop in false positives after adopting AI.

## Learn normal, then flag the 3 AM database dump

The pipeline he describes is collect, pre-process, model, act: gather everything from firewall logs to user behaviour, clean and structure it, let models find patterns and anomalies, then hand security teams actionable insights or trigger automated containment.

Three techniques carry it. Anomaly detection builds a baseline of who logs in when and what they do, then flags deviations: an employee suddenly reading an entire database at 3 AM gets noticed. Crucially, the baseline keeps adapting as normal behaviour changes, which is how false positives come down over time. Pattern recognition mines historical logs for attack fingerprints, such as login anomalies followed by privilege escalation, and graph-based analysis can link coordinated campaigns across distributed systems. Real-time threat intelligence correlates activity across endpoints, servers and cloud apps with global feeds, and some systems isolate infected machines automatically.

He also maps model types to jobs: supervised learning on labelled past attacks (say, phishing) to catch similar ones, unsupervised clustering to spot new kinds of threat, and deep learning for high-volume, high-complexity environments like cloud infrastructure. His case studies include a bank detecting more new fraud types, an e-commerce company using AI against DDoS, and a healthcare provider catching insider threats through unusual patient-record access.

## Garbage labels make garbage detectors

The honest section is the one to remember. ML needs clean, labelled data, and getting it is often the bottleneck. Black-box models create a trust and compliance gap when nobody can explain why something was flagged. False positives still happen, and frequent ones desensitise analysts into alert fatigue. Surveillance and data-use ethics need deliberate handling. His outlook covers explainable AI, adversarial ML to defend against AI-powered attacks, federated learning for privacy-preserving analytics, and more autonomous security systems, which he notes are already in research labs and startups rather than a decade away.

## Who should watch

Security leads and product managers who need a quick, balanced framing of where ML helps a SOC and where it bites. There's no tooling demo, so engineers wanting detection-engineering detail should go straight to the related talks.

## Related Conf42 talks

- [Synergizing Threat-Informed Defense: When Cloud Attack Emulation Meets Detection Engineering](https://www.conf42.com/Cloud_Native_2024_Kennedy_Torkura_threat_informed_defense) by Kennedy Torkura is the hands-on detection side.
- [Atomic Red Team - Closing the Gap with Threat Actors](https://www.conf42.com/Incident_Management_2023_Christopher_Haller_atomic_red_team_threat_actors) by Christopher Haller tests whether your detections fire at all.
- [Security Threats in Modern LLM Applications: Risks & Defenses](https://www.conf42.com/Large_Language_Models_LLMs_2025_Kartheek_Medhavi_Penagamuri_Shriram_threats_risks_defenses) by Kartheek Medhavi Penagamuri Shriram covers the AI-side attack surface.

[Watch Dinesh Rajasekharan's talk](https://www.conf42.com/Machine_Learning_2025_Dinesh_Rajasekharan_cybersecurity_threats_predictive)

[Watch the talk on YouTube](https://youtu.be/cfnCGTx69LM).

## Watch the talk

[From Reactive to Predictive: AI-Powered Cybersecurity in the Age of Advanced Threats](https://www.conf42.com/Machine_Learning_2025_Dinesh_Rajasekharan_cybersecurity_threats_predictive) at Conf42 Machine Learning 2025.
