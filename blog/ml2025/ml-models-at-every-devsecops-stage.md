# Putting a different ML model at every DevSecOps pipeline stage

Conf42 Blog, 2025-05-05, updated 2026-11-09. https://www.conf42.com/blog/ml2025/ml-models-at-every-devsecops-stage

In short: Srikanth Potla, Senior Product Security Engineer at SoFi, at Conf42 Machine Learning 2025 maps supervised, unsupervised and NLP models onto CI/CD.

Security reviews that take a month are a release blocker with a badge. Srikanth Potla, Senior Product Security Engineer at SoFi, argued at [Conf42 Machine Learning 2025](https://www.conf42.com/ml2025) that machine learning can close the gap between development speed and security review, as long as you match the model type to the pipeline stage: supervised models for known vulnerabilities, unsupervised models for runtime anomalies, and NLP for infrastructure-as-code.

The talk is a framework plus figures from industry data and a case study. It names Snyk as one example tool, but it is not a product pitch, and it does not show Potla's own pipeline at SoFi.

## The security development gap

Potla's opening is that conventional security cannot keep up with modern delivery cycles. He cites 94% of enterprises using cloud services and a sharp rise in AI-powered attacks since 2022, and calls the result a "security development gap": every week between writing code and reviewing it is a window for an attacker. The figures he leads with, from what he describes as data across more than 500 enterprise implementations, are fewer security incidents, faster secure deployments, and mean time to remediate dropping from 38 days to just over four.

## Pick the model for the threat you know (and the one you don't)

**Supervised learning for known vulnerabilities.** Models trained on large datasets of known vulnerable code patterns flag similar issues in new code before deployment, and get better as new vulnerability data arrives. His example is Snyk's ML-enhanced scanning in 2024, which he says caught far more vulnerabilities before production than traditional static analysis.

**Unsupervised learning for the unknown.** Baselines of normal behaviour per environment, continuous monitoring, and self-learning models that flag deviations. This is where novel attacks and zero-days show up, and he says it has been especially effective for runtime detection in containers.

**Container security across the lifecycle.** Image scanning, behavioural runtime protection, network monitoring for unexpected connections, and configuration checks against best practice.

**NLP for infrastructure-as-code.** The most interesting idea in the talk. Regex-based IaC scanners match patterns; NLP-based analysis tries to understand what a Terraform or CloudFormation file intends, so it can catch overly permissive policies or insecure defaults that a pattern match would miss, and suggest code-level fixes.

## Wire it into every stage

Put together, the pipeline looks like this: ML-powered pre-commit analysis at commit, supervised scanning of container images and dependencies at build, ML-generated security tests aimed at likely weak points in test, NLP infrastructure scanning before provisioning, and unsupervised runtime monitoring in production.

The case study is a financial services company whose mobile banking releases waited around 27 days for security review. After adding an ML pipeline that prioritised vulnerabilities and opened pull requests for common issues automatically, reviews dropped to two days, and the automated remediation now handles most common issues without a human. That frees the security team for the problems that need judgment.

## Start small

The implementation advice is modest: document existing controls and gaps, define success metrics, build a cross-functional team, start with code scanning in CI and container monitoring, set up feedback loops, then add unsupervised runtime models and automated remediation. Pick one tool, measure it, then expand.

## Who should watch

AppSec and platform engineers building a case for ML-assisted scanning, and security leaders who want a stage-by-stage map. Teams already running mature DevSecOps tooling will find the framework familiar; the IaC section is the part most likely to give them a new idea.

## Related Conf42 talks

- [DevSecOps as an approach to building and deploying secure applications by shifting left](https://www.conf42.com/DevSecOps_2024_Peter_De_Tender_devsecops_applications_shifting), Peter De Tender, Conf42 DevSecOps 2024
- [Your SBOM stops at the model](https://www.conf42.com/DevSecOps_2026_Emmy_Eide_sbom_models_supplychain), Emmy Eide, Conf42 DevSecOps 2026
- [Secretless multi-cloud authentication with workload identity for DevSecOps pipelines](https://www.conf42.com/DevSecOps_2026_Venkata_Velavarthipati_workloadidentity_oidc_secretless), Venkata Velavarthipati, Conf42 DevSecOps 2026

[Watch Srikanth Potla's talk](https://www.conf42.com/Machine_Learning_2025_Srikanth_Potla_pipeline_security_devsecops)

[Watch the talk on YouTube](https://youtu.be/NYhDGMUrPLI).

## Watch the talk

[Machine Learning in the DevSecOps Pipeline: Revolutionizing Predictive Security for Cloud-Native Applications](https://www.conf42.com/Machine_Learning_2025_Srikanth_Potla_pipeline_security_devsecops) at Conf42 Machine Learning 2025.
