# One JSON schema can generate the UI and pipeline for quantum runs

Conf42 Blog, 2025-06-14, updated 2026-11-09. https://www.conf42.com/blog/quantum2025/json-schema-generates-quantum-experiment-portals

In short: Amazon's Vamsi Praveen Karanam at Conf42 Quantum Computing 2025 turns a JSON schema into a React form, a Step Functions pipeline and lineage for Braket jobs.

Quantum research has a notebook problem: every new experiment starts as a copy of the last one, with a parameter changed and a dependency nobody wrote down. At Conf42 Quantum Computing 2025, Vamsi Praveen Karanam, Software Development Engineer at Amazon, showed a fix borrowed from platform engineering: describe the experiment in one JSON schema and generate the UI, the pipeline and the lineage tracking from it.

It's the most software-engineering-shaped talk of the event, and a compact one: one architecture, real numbers.

## The manifest replaces the monolith

Karanam's diagnosis is that research tooling lags the science. Hardware and error mitigation techniques change constantly, so notebooks get cloned, logic hides in scripts, documentation drifts and auditing becomes nearly impossible, which hurts most in regulated industries.

The framework puts a single JSON schema at the centre, "a machine readable contract that defines what an experiment can and cannot accept". From it, the system generates three things: a React form so scientists never touch HTML or JavaScript, an AWS Step Functions workflow that runs circuits and post-processes results serverlessly, and a lineage tracker that tags and versions every run. In his comparison, about 30 lines of schema replace a hand-coded notebook.

## A small, serverless architecture

The plumbing is pure AWS. The schema lives in S3 with Object Lock, so it is versioned and immutable. A CI/CD pipeline triggers two generators: one builds the React portal, the other compiles the Step Functions state machine. The state machine calls Amazon Braket to run quantum jobs, invokes Fargate containers for post-processing and stores results in S3. OpenTelemetry feeds Grafana dashboards.

The engineering numbers are pleasingly tiny. Three CDK stacks (portal, pipeline, observability). A schema file of about 375 bytes. A React bundle of 1.2 KB gzipped. A state machine of 23 states with no Lambda functions at all. Local testing runs on LocalStack, deploys go through GitHub Actions, and most dev and test work fits within the AWS free tier.

## Validation up front is the real win

Karanam lists four benefits, and the third is the one any SRE will recognise: configuration errors drop to zero because schema validation runs before anything is submitted. Researchers fill a form that is guaranteed to be valid instead of discovering a typo after a queue wait. Schemas also live in git with pull requests and diffs, and new team members can run experiments without learning internal SDKs.

## The VQE sweep numbers

To test it, his team ran a one-million-shot VQE sweep and compared the schema portal with the notebook baseline across five metrics:

- Setup time per parameter variant: 18 minutes down to 3.
- Wall-clock time for the suite: from 13.4 to 11.8 hours, thanks to better concurrency and simulator fallback when QPU queues back up.
- Configuration errors: 7 down to 0.
- Cost: about 200 USD saved, mostly from fewer retries.
- Learnability: researchers rated the portal 4.8 out of 5, against 3.1 for notebooks.

He stresses these came from real jobs on Braket with simulator fallback and Fargate post-processing, not synthetic benchmarks.

## What comes next

The roadmap has three items: chaining multiple experiments so one stage's output feeds the next, encrypting results with post-quantum algorithms aligned with NIST standards, and portable backends for Azure Quantum and Google Cirq using the same schema and UI.

## Who should watch

Anyone building internal tooling for researchers or data scientists, quantum or not. The pattern (schema as contract, generated UI, generated workflow) works for ML experiments and load tests too. Quantum specialists will get the most from the VQE sweep comparison.

## Related Conf42 talks

- Oskar Neumann on [Modern Application Architecture with AWS Step Functions](https://www.conf42.com/Cloud_Native_2023_Oskar_Neumann_modern_application_architecture_aws_step_functions).
- Anoosha Cherukuri on [Low-Code Meets Public Code](https://www.conf42.com/MLOps_2025_Anoosha_Cherukuri_low_code_meets).
- Karthikeyan Rajamani on [Site Reliability at the Quantum Frontier](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Karthikeyan_Rajamani_site_reliability_quantum), keeping hybrid quantum-classical systems robust.

[Watch Vamsi Praveen Karanam's talk](https://www.conf42.com/Quantum_Computing_2025_Vamsi_Praveen_Karanam_low_code_experimentation)

[Watch the talk on YouTube](https://youtu.be/4QVRaDASDDw).

## Watch the talk

[Schema-Driven Experiment Portals: Low-Code UI & Pipeline Generation for Quantum R&D](https://www.conf42.com/Quantum_Computing_2025_Vamsi_Praveen_Karanam_low_code_experimentation) at Conf42 Quantum Computing 2025.
