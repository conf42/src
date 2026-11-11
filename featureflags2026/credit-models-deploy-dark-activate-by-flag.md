# Deploy credit models dark, then let a governed flag activate them

Conf42 Blog, 2026-09-27, updated 2026-11-09. https://www.conf42.com/featureflags2026/credit-models-deploy-dark-activate-by-flag

In short: Pavan Rupanguntla at Conf42 Feature Flags 2026 on separating deployment from activation for ML credit models, with shadow challengers and governed kill switches.

A credit model that passed validation is ready to deploy, but that doesn't mean it should start deciding anyone's credit line. At Conf42 Feature Flags 2026, Pavan Rupanguntla, a credit risk and model risk management practitioner at Bank of America, argued that feature flags give lenders the missing control point: deploy the model inactive, check it in production, then let an approved configuration change turn it on, cohort by cohort. He notes the views are his own, not his employers'.

He brings more than seventeen years in consumer credit, card underwriting and model validation, including roles at Bank of America and Barclays, and it shows in the questions he asks. Not only does the model work, but can we control it, explain it, observe it and stop it?

## Validation passed, production is a different population

Pavan's starting point is the difference between deterministic code and learned behaviour. A model can do well in validation and still surprise you live because of population shift, attributes that go missing or arrive late, or customer behaviour that moved with the economy. That is a known risk in any ML system; in credit, the surprise lands on real exposure and real customers.

So he splits one event into two. Deployment means the model is in production, infrastructure checked, logging confirmed, inference pipeline and monitoring connected. Activation is an approved configuration change that lets it influence decisions, with no new software release needed to widen or shrink exposure. That boundary also separates authority: technology verifies the system works, model risk verifies the model and its controls, and business and risk stakeholders decide when customers feel it. Between the two, you can check whether features actually arrive on time and whether decision distributions look as expected.

## Shadow challengers and governed canaries

Rollout runs as approved stages rather than an engineer nudging a percentage. Start with a small, documented population (his simple example is existing clients before non-clients), with traceability for every decision: which model version, which cohort, and why this customer got this outcome.

Champion and challenger fit naturally. The challenger runs in shadow first, getting the same inputs while its output is recorded and compared, never applied. Where do the two disagree, which segments diverge most, and does risk segmentation shift the way you expected? The advantage is learning in the real production environment without touching customer outcomes.

The canary needs a wider definition of healthy than a web service. Latency, error rate and CPU still matter, but a credit canary also watches decision distributions, credit exposure and fairness indicators, and customer and portfolio outcomes. Expansion criteria, investigation triggers and rollback conditions are agreed before anyone flips anything. Turning it on for a few customers to see what happens isn't a canary, it's a gamble with a dashboard.

## A kill switch needs a fallback that still works

The kill switch is where separating deployment from activation pays off: an authorised team can deactivate the new model and restore an approved fallback without a release. Pavan's governance rider is that someone has to define who holds that authority, what conditions justify it, how it's documented and what investigation follows. The critical dependency is fallback readiness. The previous model, or a rule-based business-as-usual policy, must stay production-ready during the rollout. A rollback strategy isn't real if the fallback path has been removed.

## Flags as governed assets

Every flag decision should log the model version, policy path, timestamp and rollout cohort, so you can trace a decision back through features, policy logic and governance records, explain adverse action reasons, and tell a one-off from a systemic issue. Approvals may span technical validation, model risk review, business and compliance. And every flag needs an owner, documentation, a periodic review and an end date, or the organisation collects permanent flags nobody can explain.

His platform warnings are practical: flag proliferation, flags that outlive their team, flags that depend on other flags, and poor naming. An identifier that makes sense to an engineer can be opaque to a risk analyst, so naming standards are part of governance. The cultural point lands last: under pressure for lift and growth, pausing, observing longer or rolling back is a legitimate control action, not a failure.

## Who should watch

ML engineers and platform teams in lending or other regulated decisioning, and model risk folks who want to see how flags fit their controls. It's process-heavy rather than code-heavy, from someone who has sat in audit exams.

## Related Conf42 talks

- [The Fairness Paradox: Why Your Compliant ML Model May Be Causing the Most Harm](https://www.conf42.com/MLOps_2026_Neelima_Verma_fairness_compliant_harm) by Neelima Verma (FairLens) at Conf42 MLOps 2026.
- [Maximizing Credit Card Profitability with Machine Learning–Driven CLV](https://www.conf42.com/Machine_Learning_2026_Avaneendra_Kanaparti_experimentation_abtesting_optimization) by Avaneendra Kanaparti of American Express at Conf42 Machine Learning 2026.
- [Compliance as a Pipeline Stage: Automating AI Governance in MLOps](https://www.conf42.com/MLOps_2026_Arpita_Sheth_compliance_governance_pipeline) by Arpita Sheth at Conf42 MLOps 2026.

[Watch Pavan Rupanguntla's talk](https://www.conf42.com/Feature_Flags_2026_Pavan_Rupanguntla_credit_model_rollouts) from [Conf42 Feature Flags 2026](https://www.conf42.com/featureflags2026).

[Watch the talk on YouTube](https://youtu.be/sRHM3uemo4g).

## Watch the talk

[Feature Flags for Safer Machine Learning Credit Decisions and Controlled Model Rollouts](https://www.conf42.com/Feature_Flags_2026_Pavan_Rupanguntla_credit_model_rollouts) at Conf42 Feature Flags 2026.
