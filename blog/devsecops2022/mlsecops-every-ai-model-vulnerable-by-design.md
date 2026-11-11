# Your firewall can't see an adversarial example

Conf42 Blog, 2022-11-30. https://www.conf42.com/blog/devsecops2022/mlsecops-every-ai-model-vulnerable-by-design

In short: Eugene Neelou (Adversa) at Conf42 DevSecOps 2022 on MLSecOps, a stage-by-stage plan for securing AI pipelines that are vulnerable by design

Machine learning models fail in ways no vulnerability scanner checks for. At Conf42 DevSecOps 2022, Eugene Neelou, Co-Founder and CTO of Adversa, walked through MLSecOps, his framework for building security into every stage of the AI lifecycle, from planning to monitoring. The takeaway: AI systems inherit every classic software bug and add three new classes of attack on top.

The origin story is a good one. Eugene's team built machine learning models for insider threat detection, tested the product before release and found it was easy to fool their own security models. That sent him into adversarial machine learning. He says he coined the term MLSecOps in 2017 to separate two work streams: using ML for security, and protecting the ML itself. Adversa followed in 2019 as a research company focused on AI vulnerabilities.

## Why is AI a new kind of attack surface?

Eugene's framing is Software 2.0: deterministic algorithms written by developers get replaced or augmented by probabilistic ones trained on data. That brings new roles (data engineers, data scientists, ML engineers) and new artifacts: data sets, model weights, metrics, experiments. Each is something an attacker can tamper with.

He groups the threats into three families. Infection happens at development time, by poisoning training data or supplying a trojaned model. Manipulation happens at runtime, fooling model decisions with adversarial examples or degrading performance. Exfiltration steals the model's algorithm or extracts private data through inference attacks. On top of that sit the usual suspects: input validation, access control, misconfiguration.

The numbers are blunt. He cites over 5,000 research papers on attacking and defending AI, and says Adversa's own penetration tests of AI systems have had a 100% success rate across industries such as automotive, biometrics, internet and finance. In the MLSEC AI hacking competition, where his team built the facial recognition track, all top ten contestants used different strategies and all of them fooled the models.

## Shift left, because retraining is expensive

The case for shifting left is practical. If a late stage reveals the model needs retraining, you redo everything from data packaging through experiments and model selection. "Essentially, we want to build security into the way software is built, not after software is built," Eugene Neelou said at Conf42 DevSecOps 2022.

The framework walks six stages, each with tasks, problems and solutions.

**Plan.** The common gap is no risk assessment, no threat modelling and no security governance. The fixes are a risk register, a mapped attack surface and security baselines that turn risk into a go or no-go for deployment.

**Collect.** Data sets often carry private information the model doesn't need, come from sources you can't verify, and can be poisoned one entry at a time. His advice: drop sensitive fields you don't need, anonymise or tokenise the rest, filter anomalous entries, and keep data sets under secure version control.

**Build.** Eugene calls this probably the most dangerous stage. Pretrained models from GitHub or big vendors are external code with weights attached, and a realistic vehicle for malicious models. Data scientists are often expected to write production-ready, secure code. Academic tooling wasn't built with security in mind; loading models from Python pickle files is his standard example of a known insecure practice. Treat external models like external code: trusted sources, hash checks, model version control, dependency scanning, and adversarial training or federated learning depending on the threat.

**Validate.** Most models are barely tested beyond accuracy metrics. The most mature teams he sees are US banks, thanks to model risk management regulation, and self-driving companies. He suggests testing playbooks that start with a basic adversarial sanity check, move to a broader attack library (his comparison is the OWASP Top 10), and finish with threat-based scenarios. And scan the Docker containers the models ship in.

**Deploy.** The deployed model may not be the one you validated if someone swapped it in the model store. Check model authenticity, control who can roll out to production, harden against the threats in your model, and add operational defences such as rate limiting, mutual authentication and encryption in transit.

**Monitor.** AI systems are non-deterministic, so monitoring covers accuracy, drift and anomalies in inputs and outputs. The common failures are logs nobody can query, no idea what normal looks like, and passive watching. The mature end is automated response: alerting, safety filters for prompt injection, or blocking accounts.

## The pipeline is a target too

He closes on access control for the ML pipeline itself: who can commit code, publish models and data sets, approve releases and promote models, plus secure configuration of feature stores and experiment trackers.

His final point is the one DevSecOps teams can act on tomorrow: defences are often more operational than algorithmic, so build the infrastructure now and share threat knowledge with AI developers, who rarely see it.

## Who should watch

Security engineers whose product teams just added a model, and ML engineers who have never been threat-modelled. It's a framework talk, organised and concept-first; there are no tool demos, and Eugene says as much.

For more on the attacks, see [Anmol Agarwal's beginner's guide to adversarial machine learning](https://www.conf42.com/Machine_Learning_2024_Anmol_Agarwal_beginners_guide_adversarial), [Pavel Solikov on adversarial attacks](https://www.conf42.com/Machine_Learning_2026_Pavel_Solikov_security_adversarial_attacks), and [Manuel Heinkel and Puria Izady on generative AI security](https://www.conf42.com/Large_Language_Models_LLMs_2024_Manuel_Heinkel_Puria_Izady_generative_ai_security).

[Watch Eugene Neelou's talk](https://www.conf42.com/DevSecOps_2022_Eugene_Neelou_ai_introducing_mlsecops_for_software_20) from [Conf42 DevSecOps 2022](https://www.conf42.com/devsecops2022).

## From Adversa

Eugene presents Adversa as a research company focused on AI vulnerabilities, founded in 2019, and points to its report covering known AI vulnerabilities by industry, application and data type, plus a write-up of the MLSEC hacking competition.

- Adversa AI: [adversa.ai](https://adversa.ai/)
- AI vulnerabilities report: [adversa.ai/conf42-report](https://adversa.ai/conf42-report)
- MLSEC hacking competition: [adversa.ai/conf42-mlsec](https://adversa.ai/conf42-mlsec)

[Watch the talk on YouTube](https://youtu.be/JHc2An3a0Ws).

## Watch the talk

[DevSecOps for AI: Introducing MLSecOps for Software 2.0](https://www.conf42.com/DevSecOps_2022_Eugene_Neelou_ai_introducing_mlsecops_for_software_20) at Conf42 DevSecOps 2022.
