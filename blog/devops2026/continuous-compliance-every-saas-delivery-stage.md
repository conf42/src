# Compliance belongs in every stage of SaaS delivery, not just the audit

Conf42 Blog, 2025-12-30, updated 2026-11-09. https://www.conf42.com/blog/devops2026/continuous-compliance-every-saas-delivery-stage

In short: Oracle engineering manager Pooja Ranjan at Conf42 DevOps 2026 maps where compliance lives in each SDLC stage of SaaS delivery and what to automate.

The gap between 99.95% and 99.99% availability looks like a rounding error on a contract. In practice it is the difference between a few hours of downtime a year and under an hour. At Conf42 DevOps 2026, Pooja Ranjan, an engineering manager at Oracle America, used that gap as the entry point to a stage-by-stage tour of where compliance actually lives in SaaS delivery, and why automating it is how you keep promises like that without burning out your engineers.

It is a broad overview from someone with over a decade in B2B cloud software, good as a first talk on the topic.

## The SLA is the first compliance artefact

Ranjan starts before any code exists. In feature planning, product managers (increasingly with data-science tooling, including LLMs mining structured and unstructured data) decide what to build, and the legal side signs NDAs and contracts that fix the service level agreement: availability, scaling, and what happens financially when you miss. Everything downstream exists to keep that promise.

## Design and code reviews are compliance too

At architecture review, compliance means checking that every third-party component is either open source or properly licensed, and sending the design to an internal security team for a full posture review against things like denial of service and cross-site scripting. Findings send the design back to the architecture board.

In development, it means good coding practice, generated unit tests, design-doc revisions when something proves infeasible or risky, and a CI/CD gate stack: AI code-review bots, linters, and scanners that catch outdated or vulnerable package versions before merge, plus human reviewers.

## Tests are what auditors read

The testing stage is where her talk is most concrete. She describes a coverage bar of 95% or above as standard practice, black-box functional tests run continuously and touchlessly against production from Kubernetes or cron, white-box tests that catch infinite loops and null pointer exceptions, and load tests with Locust or JMeter to confirm that latency targets (such as requests completing within 500 milliseconds) actually hold.

Two US standards get a closer look. SOX requires documented acceptance criteria for every ticket and evidence of how they were met, kept ready for audit (Jira fields will do). VPAT, the Voluntary Product Accessibility Template, matters for federal customers: you test the UI with tools like screen readers, document results in an accessibility conformance report with screenshots, and redo it every year.

## Production is where governance never ends

After deploy, compliance becomes data handling: access control, isolation between customers' data, audited logging, constant dependency upgrades, and alarms (CloudWatch, Grafana) feeding scaling decisions. Ranjan notes that engineers at cloud providers can spend over 30% of their time just maintaining software, which is the argument for automating everything that can be. Her closing link is sustainability: less wasted engineering time and better-optimised code mean less hardware and a smaller carbon footprint.

## Who should watch

Engineers new to regulated SaaS delivery, and managers who need a map of where compliance work happens to explain it to a team. If you already run SOC 2 or FedRAMP programmes, the overview will be familiar; the VPAT section may still be news.

## Related Conf42 talks

- [Kira Balabanova on incorporating compliance into the product development process](https://www.conf42.com/Incident_Management_2024_Kira_Balabanova_21_compliance_development_process) at Conf42 Incident Management 2024.
- [Mamatha Swamy on hyperautomating compliance and risk intelligence in cloud-native finance](https://www.conf42.com/Kube_Native_2025_Mamatha_Swamy_compliance_automation_risk) at Conf42 Kube Native 2025.
- [Vinay Puri on ML-based compliance monitoring for automated risk detection](https://www.conf42.com/DevSecOps_2026_Vinay_Puri_ml_compliance_monitoring) at Conf42 DevSecOps 2026.

[Watch Pooja Ranjan's talk](https://www.conf42.com/DevOps_2026_Pooja_Ranjan_compliance_saas_governance)

[Watch the talk on YouTube](https://youtu.be/j-JAhJ5I8eQ).

## Watch the talk

[Automating Continuous Compliance for Scalable and Sustainable SaaS Delivery](https://www.conf42.com/DevOps_2026_Pooja_Ranjan_compliance_saas_governance) at Conf42 DevOps 2026.
