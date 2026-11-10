# Evals for Generators: Testing an LLM That Writes Clinical Configuration

A talk at [Conf42 MLOps 2026](https://www.conf42.com/mlops2026) by [Ocean Coldiron](https://www.conf42.com/speaker_Ocean_Coldiron) (Forward Deployed AI Engineer @ ModMed). Page: https://www.conf42.com/MLOps_2026_Ocean_Coldiron_evals_clinical_configuration

## Abstract

When an LLM writes prose, "looks good" might be enough. When it generates clinical configuration and test protocols, such as allergy skin-test setups and EHR note templates, a wrong answer becomes a patient-safety ticket. This talk covers how I built an evaluation harness for an AI-driven configuration and test-protocol generator. It includes golden datasets built from real (de-identified) configs, schema and rule-based validators that run before any LLM judge, diff-based regression tests across model and prompt changes, and SME review loops that turn expert corrections into new test cases. We'll look at which metrics predicted real-world defects and which ones were vanity numbers. The methods carry over to any structured-output generator, whether it produces SQL, YAML, JSON, or forms.  **Takeaways:** 1. Layer deterministic validators before LLM-as-judge. 2. Build golden sets and regression gates for structured outputs. 3. Close the loop with domain experts at low cost.
