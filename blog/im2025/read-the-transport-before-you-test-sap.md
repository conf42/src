# Read the SAP transport and the pull request before you pick your tests

Conf42 Blog, 2025-10-02, updated 2026-11-09. https://www.conf42.com/blog/im2025/read-the-transport-before-you-test-sap

In short: Vijay Kumar Kola (Intuitive) at Conf42 Incident Management 2025 on AI-driven, risk-based testing that keeps SAP S/4HANA and Salesforce changes safe.

Most enterprise incidents in SAP and Salesforce estates start as a change somebody tested too little, or tested the wrong things very thoroughly. At Conf42 Incident Management 2025, Vijay Kumar Kola, Senior Analyst in IT at Intuitive who has worked as a senior QA lead on SAP S/4HANA and Salesforce programmes, showed how AI-assisted testing reads what actually changed and points the regression effort at the risky parts, so failures get caught before go-live rather than after.

## Static test suites cannot keep up with quarterly releases

Vijay's problem statement will be familiar to anyone on an ERP programme. S/4HANA modules (sales and distribution, materials management, finance, transport management) depend on each other, so a change in SD can break MM or finance. Salesforce adds layers of customisation, CPQ pricing rules and multi-cloud setups, plus integrations with legacy systems and external APIs. SAP ships quarterly and service-pack updates; Salesforce ships seasonal releases; the testing window keeps shrinking.

Meanwhile regulated processes under SOX and GxP demand near-total accuracy, and resource limits leave large parts of the suite untested. He describes one recent project where a model adjustment in Salesforce meant retesting 70% of the suite. Static scripts age badly: an assessment he led on S/4 found 60% of test cases redundant because the scripts were outdated.

## Let the change tell you what to test

The idea at the centre of the talk is change-driven test selection. His team built agents that read the SAP side (transports and LiveCompare reports) and the Salesforce side (GitHub pull requests and change summaries), work out which objects and business processes are affected, and determine the regression impact. On one project that cut manual testing by 40 to 50%. Doing the impact analysis up front on another saved the regression team 35% of testing time.

Around that sit three techniques. Predictive analytics trained on historical defects and production issues forecasts where defects are likely, so compliance-critical workflows get priority. Machine learning on execution results removes redundant tests and highlights the impactful ones. NLP turns requirements in specs, user stories and emails into test cases; he describes using it on a long Salesforce CPQ specification and on a 20-page change log during an S/4HANA implementation.

The tooling named is Tricentis Tosca for model-based regression across SAP modules and RPA bots for repetitive financial checks such as journal postings and reconciliations, which, he said, caught SOX discrepancies that manual review would have missed.

## Salesforce gets its own three checks

For Salesforce, Vijay describes three tailored approaches. Declarative configuration validation tests flows and validation rules, including a CPQ pricing flow where discounts changed by country and customer; the AI tests caught a logic error during the pilot. Third-party integration testing simulates traffic across the boundaries with SAP or payment gateways; an agent predicted a sync delay under peak load, and the team adjusted API call frequency before go-live. User experience impact prediction flagged lag for mobile users after a CPQ update, prompting a redesign.

## Quality gates that can say no

The framework is pragmatic: assess current testing and pain points, build a data strategy from test results, defect logs and user behaviour, pick tools that fit your ecosystem, and integrate with CI/CD pipelines, test management tools and automation frameworks such as Selenium. In the pipeline, real-time quality gates make deployment decisions from test results and risk scores, and automated rollback watches post-deployment metrics. He also mentions self-healing tests that propose fixes to broken automation and wait for a human to confirm before updating the library.

His advice for starting is small: pilot predictive analytics on one module, such as SD, MM or finance, in your next SAP update.

## Who should watch

QA leads, release managers and SAP or Salesforce platform owners who own the regression suite and the go-live call. The abstract headlines a 68% reduction in incidents; the talk itself is a practitioner's tour of how his teams got their gains, so expect project anecdotes rather than a controlled study.

## Related Conf42 talks

- [Securing the AI Perimeter: Zero-Trust Integration Patterns for AI-Driven Pricing in SAP](https://www.conf42.com/DevSecOps_2026_Sirisha_Ayyagari_zerotrust_sap_pricing) by Sirisha Ayyagari, on the pricing integrations Vijay tests.
- [De-Risking a Legacy CRM Migration in Life Sciences](https://www.conf42.com/Feature_Flags_2026_Jaymin_Sutarwala_crm_migration_salesforce) by Jaymin Sutarwala, a feature-flag route to safer Salesforce rollouts in a GxP setting.
- [How Visual AI Makes Testing a Breeze](https://www.conf42.com/Machine_Learning_2022_Andrew_Knight_visual_ai_testing) by Andrew Knight, for the UI side of AI-assisted testing.

[Watch Vijay Kumar Kola's talk](https://www.conf42.com/Incident_Management_2025_Vijay_Kumar_Kola_sap_salesforce_testing)

[Watch the talk on YouTube](https://youtu.be/OZzch6Gm8LQ).

## Watch the talk

[AI-Powered Testing: Preventing SAP & Salesforce Incidents Before They Happen](https://www.conf42.com/Incident_Management_2025_Vijay_Kumar_Kola_sap_salesforce_testing) at Conf42 Incident Management 2025.
