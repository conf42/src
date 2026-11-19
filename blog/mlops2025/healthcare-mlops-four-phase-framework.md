# Healthcare AI fails at deployment, so build the deployment first

Conf42 Blog, 2025-08-30, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/healthcare-mlops-four-phase-framework

In short: Aishwarya Pai (Deloitte) at Conf42 MLOps 2025 on a four-phase MLOps framework for getting clinical models into hospitals safely.

Most healthcare AI projects do not die in the notebook. They die on the way to the ward. At Conf42 MLOps 2025, Aishwarya Pai, Senior Consultant at Deloitte, opened with that gap and a blunt figure from her abstract: 68% of healthcare ML projects fail in production. Her answer is a four-phase framework that treats model assessment, infrastructure, pipelines and monitoring as one programme.

It is a short, structured talk, closer to a consultant's playbook than a code walkthrough, and it is honest about that.

## The hard part is not the model

Aishwarya asks the audience a question that frames the rest: which is harder, building the AI model or getting it safely into production? Her view, and probably yours, is deployment. Healthcare adds four hurdles most industries do not stack together:

- **Regulation**, meaning FDA and HIPAA requirements.
- **Sensitive data**, where patient privacy is non-negotiable.
- **Workflow fit**, because doctors cannot be slowed down by clunky systems.
- **Monitoring at scale** across many hospitals, not one tidy environment.

## Four phases, explained as building a hospital

The framework is model assessment, infrastructure readiness, pipeline automation and monitoring. Her analogy is a construction project: check the materials, make sure the building is safe and compliant, automate the elevators and security, then keep the whole thing under round-the-clock surveillance.

**Model assessment** goes past accuracy. Does the model work across different patient groups? Is it fair? Can clinicians understand its decisions, and can you prove all of that to regulators?

**Infrastructure readiness** is about compute, security and HIPAA-compliant data flows, plus integration with EHR systems so the model shows up inside the clinician's existing workflow. Her line here is memorable: trying to run MRI scans on a laptop just won't work.

**Pipeline automation** handles pre-processing and de-identification, training with version control, safe deployments with canary tests and rollbacks, and automatic generation of documentation for regulators. That last item is the one teams forget until an audit arrives.

**Monitoring** tracks accuracy in real time, watches for data drift as patient populations change, and alerts clinicians when something looks wrong. Aishwarya calls this the most critical phase, because it is the one that keeps patients safe after launch.

## A plain stack and a year-long rollout

For the engineers in the room she names the tooling: Git for version control, CI/CD pipelines with approvals, Docker and Kubernetes for deployment, Prometheus and Grafana for monitoring. Nothing exotic, which is rather the point. The difficulty is in the process around the tools, not the tools themselves.

The rollout plan takes about a year. Months one and two assess and plan, three and four build the foundation, five and six pilot a single model, and seven to twelve scale to more hospitals. She leaves the audience with a real trade-off to argue about: a faster pilot, or a more cautious system-wide rollout?

The abstract and slides cite improvements from structured MLOps (higher success rates, faster deployment, annual savings). Treat those as the research figures she presents rather than a single case study you can reproduce; the framework itself is the useful takeaway.

## Who should watch

Engineering leads and consultants starting MLOps work in a hospital system, and anyone who has to explain to a clinical stakeholder why "the model works" is not the same as "the model is ready". If you want deep implementation detail on drift detection or de-identification, pair it with something more hands-on.

## Related Conf42 talks

- [When Bad Data Reaches the Model: Engineering Data Quality Into MLOps at Healthcare Scale](https://www.conf42.com/MLOps_2026_Saiteja_Jonnalagadda_healthcare_quality_data)
- [From Data to Decision: How Multimodal AI Is Transforming Patient-Centered Healthcare](https://www.conf42.com/Machine_Learning_2025_Hari_Suresh_Babu_Gummadi_healthcare_decision_patient)
- [Beyond Compliance: Architecting Secure Distributed Healthcare Systems](https://www.conf42.com/Machine_Learning_2025_Sachin_Telalwar_compliance_healthcare)

[Watch Aishwarya Pai's talk](https://www.conf42.com/MLOps_2025_Aishwarya_Pai_mlops_healthcare_scaling)

[Watch the talk on YouTube](https://youtu.be/2YHCklhGJrU).

## Watch the talk

[MLOps in Healthcare: Scaling AI Model Deployment Through Strategic Automation and Monitoring Frameworks](https://www.conf42.com/MLOps_2025_Aishwarya_Pai_mlops_healthcare_scaling) at Conf42 MLOps 2025.
