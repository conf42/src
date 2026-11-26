# Enterprise interfaces that notice cognitive overload, ethically

Conf42 Blog, 2025-05-18. https://www.conf42.com/blog/obs2025/enterprise-uis-that-notice-cognitive-overload

In short: Karthik Mohan Muralidharan at Conf42 Observability 2025 on inferring user stress from typing, mouse and workflow signals and adapting enterprise UIs, with consent.

Your typing slows down, you start correcting more mistakes and you wander off the usual path through a form. To an emotionally aware interface, that pattern says overload, and it can respond by simplifying the screen or offering help. At Conf42 Observability 2025, Karthik Mohan Muralidharan, a software engineer with about eight years in full-stack Salesforce development, presented research on adaptive enterprise interfaces that infer cognitive and emotional state without cameras or biometrics, and the ethical guardrails they need.

This is a research survey rather than a product demo. It turns observability inward: instead of watching the system, the system watches how people are coping with it.

## Enterprise software is behind consumer apps

The opening gap is striking. Citing research, Muralidharan says only around 18% of enterprise systems use any affective computing principles, against nearly 69% of consumer applications with adaptive elements, and adoption is lowest where stakes are highest: financial platforms, healthcare management and critical infrastructure. His view is that the hurdles are now more organisational than technical.

The cited benefits are what make the case: studies he references report fewer diagnostic errors and higher decision confidence for clinicians using emotionally responsive interfaces, lower cognitive load and better task accuracy across sectors.

## Reading state from ordinary interaction

The detection methods are all non-invasive. Typing rhythm correlates with cognitive load; a drop in keyboard speed is a consistent signal of increased mental demand. Error patterns are telling: clustered errors predict fatigue, a jump in corrections often signals frustration, and navigation errors versus data entry errors carry different signatures. Workflow sequencing shows hesitation when users drift from optimal task paths. Mouse movement and dwell time add more: longer dwell on a complex element correlates with confusion, and more frequent attention switching indicates information overload. Ensemble models then classify five emotional states, with accuracy he puts in the high 70s.

He also notes that cloud processing has cut inference latency sharply since 2020, and that federated learning keeps most of a centralised model's accuracy without pooling sensitive data.

## How the interface adapts

Once a state is inferred, the interface responds in five ways. Information density modulation reduces complexity during overload. Contextual assistance offers help when confusion is detected, which he links to fewer support tickets and less task abandonment. Workflow simplification restructures complex tasks during stressful periods. Contrast enhancement directs attention to critical elements. And intelligent timing of notifications cuts interruptions. The architecture is four layers: data collection, inference engine, adaptation rules and the interface itself, fast enough to adapt in real time.

## Support, not surveillance

The ethics section is the reason to watch. Transparent consent and granular opt-in permissions raise acceptance far above blanket consent. Low-confidence inferences should fall back to a static interface rather than guess. Unmitigated models show accuracy gaps across cultural backgrounds and age groups, which balanced training data and cultural calibration reduce. Most enterprise users worry this data will be used for performance reviews, so technical safeguards that prevent extracting individual performance metrics are essential, along with easy user overrides. His summary is that ethics by design is also the path to adoption.

## Who should watch

Product designers and front-end engineers building internal tools for high-stakes work, and anyone curious about affective computing beyond webcams and wearables. The talk leans heavily on cited study figures, so follow up on the sources before quoting them in a design review.

## Related Conf42 talks

- [Empowering User Experience with Adaptive User Interfaces in JavaScript](https://www.conf42.com/JavaScript_2024_Abhinav_Chunchu_2_adaptiveinterfaces_datadrivenux) by Abhinav Chunchu at Conf42 JavaScript 2024.
- [Beyond Barriers: AI-Powered Cognitive Support Systems Reshaping Digital Accessibility](https://www.conf42.com/Machine_Learning_2025_Vignesh_Kuppa_Amarnath_accessibility_support_cognitive) by Vignesh Kuppa Amarnath at Conf42 Machine Learning 2025.
- [The AI Trust Triad for DevOps: Reinforcement Learning, Federated Learning, and Explainable AI](https://www.conf42.com/DevOps_2026_Saideepak_Kandibanda_trust_explainability_regulation) by Saideepak Kandibanda at Conf42 DevOps 2026.

[Watch Karthik Mohan Muralidharan's talk](https://www.conf42.com/Observability_2025_Karthik_Mohan_Muralidharan_intelligence_adaptive_interfaces) or the [YouTube recording](https://youtu.be/gPi-ktY-sDY).

## Watch the talk

[Emotional Intelligence in the Cloud: Adaptive Interfaces for Enterprise Decision-Making](https://www.conf42.com/Observability_2025_Karthik_Mohan_Muralidharan_intelligence_adaptive_interfaces) at Conf42 Observability 2025.
