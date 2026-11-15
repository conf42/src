# Let the pipeline learn which tests matter

Conf42 Blog, 2025-11-07, updated 2026-11-09. https://www.conf42.com/blog/devsecops2025/generative-ai-in-devsecops-qa-pipelines

In short: Baradwaj Bandi Sudakara of Ascension Health at Conf42 DevSecOps 2025 on generative AI test creation, ML risk-based testing and anomaly alerts.

Deployments went continuous years ago; most QA and security reviews did not. At Conf42 DevSecOps 2025, Baradwaj Bandi Sudakara, Senior Software Engineer at Ascension Health, argued that the gap closes when generative AI writes the tests and machine learning decides which ones to run, without replacing the CI/CD pipeline or security policies you already have.

## Static checks against a moving system

His framing: teams ship daily into distributed microservices with shifting attack surfaces, while test suites, security reviews and scripted automation stay static. Rigid tests and predefined rules cannot keep pace with systems that behave in fluid, unpredictable ways, so the distance between deployment speed and assurance keeps growing. The move he proposes is from reactive to predictive, manual to automated, gatekeeping to acceleration.

## Generative AI as the test author

The first lever is test and security script generation. Baradwaj describes what he sees GitHub Copilot doing day to day: reading user stories, understanding code context, generating complete test suites and security validation scripts, and even adding stories to Jira through plugins. The value he stresses is coverage of scenarios humans tend to skip, rather than raw speed.

The test data case study is the more interesting one. Realistic, interconnected test data for microservices is notoriously painful to build. AI reads the schemas, studies production data patterns, synthesises realistic datasets and generates boundary and edge-case values. Data preparation time drops sharply while coverage across service boundaries goes up.

## Machine learning as the test scheduler

The second lever is predictive quality engineering. Models trained on production logs, historical defects, code changes and system behaviour predict which modules are risky and which areas are likely to break. That feeds a risk-based testing pyramid: critical paths and high-risk modules first, then recently changed code and integration boundaries, with stable low-risk areas last. You run less and catch more, and the pipeline gets smarter with each release.

The same idea powers his anomaly detection example. ML learns what normal looks like across services and flags performance drift, suspicious access patterns, latency spikes and unusual memory use. In his setup an anomaly fires a Slack alert, and if it is bad enough, a phone call. If your on-call rotation already ignores half its alerts, this is the part to watch carefully.

He also covers AI-assisted static analysis, runtime behaviour monitoring and dependency intelligence that ranks patches by exploitability and impact.

## Adopt it in phases, not in one weekend

Baradwaj is emphatic that this is no overhaul. His four phases: assess and pilot (start with AI test generation and vulnerability scanning), integrate and train (connect tools to CI/CD, train models on historical logs and incidents), scale and optimise (more services, feedback loops), and finally autonomous operation where AI makes real-time calls like test prioritisation. Security policies and the CI/CD pipeline stay as they are; AI goes where manual effort and risk are highest.

His takeaways: start with one pilot, fix data quality, build cross-functional teams, feed production incidents back into the models, and position AI as an enabler rather than a replacement.

## Who should watch

QA leads and SDETs drowning in flaky suites, and DevSecOps engineers looking for a phased argument to take to their managers. It is a strategy talk with a few concrete cases rather than a tooling walkthrough, so bring your own stack.

## Related talks

- [Machine Learning in the DevSecOps Pipeline](https://www.conf42.com/Machine_Learning_2025_Srikanth_Potla_pipeline_security_devsecops) by Srikanth Potla, on predictive security for cloud-native apps.
- [GenOps: A Governance-Driven Model for Safe, High-Velocity AI in CI/CD Pipelines](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity) by Neeraj Kumar Singh Beshane, for the guardrails side.

[Watch Baradwaj Bandi Sudakara's talk](https://www.conf42.com/DevSecOps_2025_Baradwaj_Bandi_Sudakara_ai_ml_secure)

[Watch the talk on YouTube](https://youtu.be/5xYaLtd5Iic).

## Watch the talk

[AI-Driven DevSecOps: Redefining Quality, Security, and Speed with Generative AI & ML](https://www.conf42.com/DevSecOps_2025_Baradwaj_Bandi_Sudakara_ai_ml_secure) at Conf42 DevSecOps 2025.
