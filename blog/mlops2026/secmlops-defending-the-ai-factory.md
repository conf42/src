# SecMLOps: treat every model file as untrusted code

Conf42 Blog, 2026-11-18. https://www.conf42.com/blog/mlops2026/secmlops-defending-the-ai-factory

In short: Jose Manuel Ortega (Alicante University) at Conf42 MLOps 2026 on securing the ML lifecycle: pickle files, poisoned data, registries and endpoints.

Loading a pre-trained model can run someone else's code with your credentials before a single prediction is made. That is the example Jose Manuel Ortega, security researcher and lecturer at Alicante University, uses at Conf42 MLOps 2026 to show why the DevSecOps practice you already have stops short of the machine learning lifecycle. His talk is a stage-by-stage tour of what he calls SecMLOps, with an open source tool named for almost every gap.

## Your scanners do not look where the models live

Jose's starting point is a comparison. Existing DevSecOps handles source code, containers, infrastructure as code and signed, versioned artifacts well. Machine learning adds things that practice was not built for: data that shapes behaviour, models that are non-deterministic and so resist a simple pass/fail security unit test, artifacts that are opaque binaries, and attack types such as evasion, extraction, model inversion and membership inference that have no classical equivalent.

Meanwhile feature stores, experiment trackers, model registries and inference endpoints are rarely in scope for vulnerability scanners. He maps each lifecycle stage to its attack: poisoning at the data stage, malicious dependencies and compromised notebooks at training, tampering and unsigned models at the registry, adversarial samples and extraction at serving, and undetected drift at monitoring, which is how a successful attack stays invisible. For a shared vocabulary between security and data science he points to the OWASP Machine Learning Security Top 10, MITRE ATLAS and the NIST AI Risk Management Framework.

## A model file is a program

Most model formats historically rely on Python pickle, and here the talk gets concrete. "A pickle is not a data format," Jose Manuel Ortega said at Conf42 MLOps 2026. Loading one executes whatever the file tells Python to execute, so a user who thinks they are loading weights can end up running an attacker's command with their own data access.

His mitigation is to treat every model file as untrusted code and scan it before loading. The tool he shows is ModelScan, an open source scanner that reads the file byte by byte looking for unsafe code signatures and ranks findings as critical, high, medium or low. It covers formats used by PyTorch, TensorFlow, Keras and scikit-learn, and it runs about as fast as your machine can read the file.

## Poisoning happens before the model exists

Data poisoning is nearly invisible afterwards. Jose lists three forms: label flipping, backdoor or trigger attacks that look perfect in evaluation and misbehave on demand, and abuse of a feed the attacker can influence. His principle is that "the data pipeline is a security boundary" and so it needs validation gates, where most teams have a transformation script.

The code example defines a strict Pydantic model for each record, with an amount constrained to a range and a label that must be zero or one. Rows that fail go to quarantine for audit. Then the batch's label distribution is compared with history: a sudden jump in fraud labels is a fingerprint of label flipping and gets flagged before training. Great Expectations does the same job for schemas, value ranges and statistical distributions.

For dependencies the recipe is to freeze, scan and sign: pip-tools for hashed lock files, a software bill of materials you can query the next time a big CVE drops, pip-audit and Safety for known vulnerabilities, and Sigstore's cosign to verify that an artifact was signed by your key before deployment.

## The registry is a production artifact repository

Whether it is MLflow or SageMaker Model Registry, the registry deserves production controls. Jose names three attacks: an unauthorized model swap by someone with too much access, weight tampering that changes behaviour without any code diff, and a stage gate bypass where an unapproved model skips evaluation. The defences are role-based access control on who can register and promote, plus hashing the artifact on write and verifying it on load.

At the endpoint, the hardening example has four parts: authentication on every call so access can be scoped and revoked, Pydantic input validation that rejects extra fields and malformed vectors, per-identity rate limiting with SlowAPI because extraction and adversarial probing need volume, and minimal outputs. Return a class label and keep the full probability vector to yourself, since every extra digit of confidence helps someone attempting model inversion. To test your own models first, he recommends the Adversarial Robustness Toolbox.

## Security as a stage that cannot be skipped

The last section wires it into CI/CD: signed commits and protected branches, an SBOM at build, policy as code with Open Policy Agent or Checkov at the gate, signature checks at admission and canary rollouts. On identity he asks for separate roles across dev, staging and production, short-lived credentials, secrets in HashiCorp Vault or a cloud secrets manager, and Gitleaks and TruffleHog scanning repositories and notebooks.

Monitoring gets a security reading too. A quality drop or input shift, watched with a tool like Evidently, can be poisoning or an adversarial campaign. And incident runbooks need ML-specific entries, because, in his words, a generic security playbook "won't tell the on-call engineer to roll back a model version".

## Who should watch

ML platform engineers and security engineers who have been handed the model pipeline and need a checklist with tool names attached. It is a survey at intermediate level: broad coverage, short code samples, no single topic explored at length. The recording is delivered at a slow, careful pace, and the slides carry the structure well. Specialists in adversarial ML will know the attack taxonomy already.

## Related Conf42 talks

- [Securing the AI Stack: From Models to Agents to Infrastructure](https://www.conf42.com/MLOps_2026_Kriti_Faujdar_securing_agents_infrastructure) by Kriti Faujdar at Conf42 MLOps 2026.
- [Your SBOM Stops at the model](https://www.conf42.com/DevSecOps_2026_Emmy_Eide_sbom_models_supplychain) by Emmy Eide at Conf42 DevSecOps 2026.
- [When AI Joins the Request Path: Securing API-Backed AI Systems](https://www.conf42.com/DevSecOps_2026_Jayakumar_Ramalingam_apis_inference_guardrails) by Jayakumar Ramalingam at Conf42 DevSecOps 2026.

[Watch Jose Manuel Ortega's talk](https://www.conf42.com/MLOps_2026_Jose_Manuel_Ortega_security_factory_mlops) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Defending the AI Factory: Practical Security Strategies for MLOps](https://www.conf42.com/MLOps_2026_Jose_Manuel_Ortega_security_factory_mlops) at Conf42 MLOps 2026.
