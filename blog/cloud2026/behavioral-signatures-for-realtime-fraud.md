# How you type and click is a fraud signal, in real time

Conf42 Blog, 2026-04-14. https://www.conf42.com/blog/cloud2026/behavioral-signatures-for-realtime-fraud

In short: Sharath Reddy Polu at Conf42 Cloud Native 2026 on behavioral analytics for fraud prevention: signatures, contextual signals and a real-time scoring pipeline.

A stolen password gets an attacker into an account, but it doesn't teach them how the real owner types. At Conf42 Cloud Native 2026, [Sharath Reddy Polu](https://www.conf42.com/Cloud_Native_2026_Sharath_Reddy_Polu_cloudarchitecture_backend_infra), a University of Southern California alumnus, presented his published research on behavioral analytics for real-time fraud prevention: building dynamic profiles from navigation, keystrokes, devices and spending, and scoring every transaction against them.

Honest scope: this is a research overview, not a walkthrough of a specific production system. It's useful as a map of the techniques and how they fit together.

## From static rules to behavioral profiles

The starting point is the classic rule: flag a transaction over a certain amount or from an unusual location. Polu puts those systems at about 45% detection, false alerts close to 37% of the time, and an average response of 95 seconds. Behavioral systems in his research reach 87% detection with around 7% false alerts and an eight-second average response, and he reports cost savings rising from 22% to 76%. Those figures come from the research he presented; the talk doesn't break down the underlying datasets.

## Four dimensions of a behavioral signature

The profile is built from four kinds of signal:

- **Navigation patterns**: click sequences, page-flow preferences and interaction timing, which form a distinctive footprint of how a person moves through an app.
- **Keystroke dynamics**: how long each key is held, the flight time between keys, and how someone corrects mistakes. Typing rhythm turns out to be a biometric.
- **Device fingerprints**: OS, browser configuration, screen resolution and installed plugins, checked against devices the user has transacted from before.
- **Transaction sequences**: merchant preferences, timing and amount distributions, so the system can spot activity that drifts from past behaviour.

## Three layers of models, plus explanations

The analytical stack is layered. Supervised models such as decision trees, random forests and gradient boosting learn from labelled legitimate and fraudulent examples. Unsupervised clustering watches for new patterns that don't match established ones, the kind designed to slip past rules. Deep learning models, LSTMs and CNNs, look for sequential deviations and relationships in multidimensional data.

On top sits SHAP for explainability, so an analyst can see why a transaction was scored the way it was. In fraud, where a false positive means a real customer stuck at checkout, that matters.

## Context turns a signal into a decision

Behaviour alone isn't enough, so the systems add context. Location consistency catches impossible travel, like a transaction in New York followed by one in London 30 minutes later, while allowing for real travel and VPN use. Environmental context looks at time zones, connection types, unfamiliar networks and IPs from high-risk regions. Device identifiers flag unknown hardware.

## The real-time pipeline

The architecture he describes has four stages. A collection layer captures behavioral signals at every touchpoint, which he estimates at over 50 signals per transaction. An analysis engine runs neural models, with edge computing pushing some analysis toward endpoints to cut latency. Risk scoring computes a fraud probability per transaction against dynamic thresholds tuned to the individual or their peer group. Then an automated response either blocks the transaction or challenges it with step-up authentication.

The models keep learning from feedback, which he says lets them adapt in days rather than the months-long manual update cycles of rule-based systems.

## Who should watch

Engineers and product people in fintech who own fraud rules and are curious what a behavioral approach adds, and security teams thinking about step-up authentication as a risk-scored decision rather than a blanket rule. Expect concepts and reported results rather than code.

## Related Conf42 talks

- [AI-Powered Fraud Detection in Cloud-Native Financial Systems: Enhancing Security with Predictive and Behavioral Analytics](https://www.conf42.com/Cloud_Native_2025_Sandeep_Jarugula_fraud_detection_analytics_security) by Sandeep Jarugula at Conf42 Cloud Native 2025.
- [Voice Biometrics in Healthcare: Securing Systems and Streamlining Workflows](https://www.conf42.com/Incident_Management_2025_Sreenivasul_Reddy_Meegada_healthcare_biometrics_security) by Sreenivasul Reddy Meegada at Conf42 Incident Management 2025.
- [Harnessing AI & LLMs for Next-Gen Digital Payment Security: Fraud Detection, Predictive Analytics, and Quantum-Resistant Innovations](https://www.conf42.com/Large_Language_Models_LLMs_2025_Sandeep_Katuri_security_payment_fraud) by Sandeep Katuri at Conf42 Large Language Models (LLMs) 2025.

[Watch Sharath Reddy Polu's talk](https://www.conf42.com/Cloud_Native_2026_Sharath_Reddy_Polu_cloudarchitecture_backend_infra) or the [YouTube recording](https://youtu.be/vE-PohH3MCY).

## Watch the talk

[Behavioral Analytics for Real-Time Fraud Prevention](https://www.conf42.com/Cloud_Native_2026_Sharath_Reddy_Polu_cloudarchitecture_backend_infra) at Conf42 Cloud Native 2026.
