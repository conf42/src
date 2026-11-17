# Put AI compliance in the pipeline, not in a pre-launch meeting

Conf42 Blog, 2026-11-12, updated 2026-11-17. https://www.conf42.com/blog/mlops2026/compliance-as-a-pipeline-stage

In short: Arpita Sheth at Conf42 MLOps 2026 on AI compliance as code: risk labels at registration, required lineage, policy gates and generated documentation.

An auditor emails you three questions: what data trained the model in production right now, who approved it, and how has it behaved since launch? Arpita Sheth, a staff AI engineer, opens her Conf42 MLOps 2026 talk with that thought experiment and notes that for a lot of teams the answer takes days, sometimes weeks. Her fix is to make compliance behave like tests: the policy is the rule, the pipeline writes the evidence on every run, and a failed check stops a deployment the way a failed test blocks a merge.

## The model you reviewed is not the one in production

Her running example is a model that helps screen job applications. Before launch it got a proper review: legal signed off and the bias tests looked fine. Then it retrains weekly on new applications. Someone on another team changes how years of experience is calculated in the feature store. Nobody calls that a release, so nobody calls the review team. Six months later the production model is a different model. "It just has the same name," Arpita Sheth said at Conf42 MLOps 2026.

The review was accurate when it happened and stopped being true the week after. Nobody runs unit tests once before launch and calls it done, and compliance can work the same way. "The policy is the rule, and the pipeline produces the proof."

On why now, she keeps the legal part short. The EU AI Act sorts systems by risk, a hiring model counts as high risk, and what the law asks for reads like an MLOps backlog: know your data, keep technical documentation, log what the system does, keep a human involved, monitor after launch. In the US, many companies follow the voluntary NIST AI Risk Management Framework while state rules keep changing. And under GDPR, a deletion request means knowing which models learned from that person's data.

## Five layers, read from the bottom up

None of it needs new infrastructure. You already have a model registry, metadata, CI/CD and monitoring.

**Risk classification at registration.** The team answers a few questions: what is the model for, does it use personal or sensitive data, does it make the final call on a person. Hiring plus a decision about a person means high risk, which brings more checks, more documentation and a required human sign-off. Keep it as clear rules with a person confirming the result, because a model labelled low risk by mistake quietly switches off every later check.

**Lineage.** Every training run writes down which data and version it used, which features and how they were calculated, which code, and the results, along with consent and delete-by details. It is written while training happens, not pieced together from old chat threads. With it, the deletion question becomes a query that takes seconds. Her rule: a run that does not record its lineage fails.

**Policy gates.** One before training: may we use this data for this purpose, did unexpected personal information sneak in, is anything past its delete-by date? One before deployment: does the model meet the fairness bar, is the documentation complete, has a person signed off? Then the lesson she says she learned the hard way: "A gate that just says policy violation is kind of useless." If engineers do not know why it failed or how to fix it, they will find a way around it.

**Monitoring.** Drift alerts saved as dated records, fairness measured in production, and sampled prediction logs with the model version. Put a delete date on the logs or the audit trail becomes its own privacy problem.

**Documentation.** With the first four layers working, the pipeline fills in a template for every model version. People write only the judgment parts: what the model is for and how humans can step in.

## LLM features use the same layers with more in them

Add an LLM that summarises each resume and lineage grows: the base model and its version, any fine-tuning data, the prompt version and the documents retrieved. A small prompt edit can change behaviour as much as a retrain, so prompts get versioned like code. The gate becomes a test suite run before every release: harmful content, leaked personal information, instruction override, made-up facts.

## Thresholds are a negotiation

Her lessons from building such systems at scale are the part worth replaying. Start at registration, not with the dashboard. Record data history from day one, since adding it later is like trying to find the receipt for something you bought a year ago. And agree thresholds jointly. Set by compliance alone they are too strict and engineers quietly build side pipelines. Set by engineering alone they are too loose and you are exposed in an audit.

She admits the costs: gates slow teams down, and one fairness bar will not fit every model. Her answers include the same dashboard for compliance and engineering, and an exception path that is a logged temporary override with an expiry date, so the exception itself becomes evidence.

Her test for next week: pick your highest-risk model and ask which data trained the version in production. If you can answer with a query, you are in good shape. "If it takes a meeting, that's where to start."

## Who should watch

ML platform leads, governance engineers and anyone whose model retrains more often than legal meets. It is a concept talk with one worked example and no tooling demo. Teams with lineage and gates already in place can skip to the trade-offs near the end.

## Related Conf42 talks

- [Automating the 'Governance': Building a Rules Engine for AI Use Case Governance at Scale](https://www.conf42.com/MLOps_2026_Ankur_Gupta_rules_engine_governance) by Ankur Gupta at Conf42 MLOps 2026.
- [The Fairness Paradox: Why Your Compliant ML Model May Be Causing the Most Harm](https://www.conf42.com/MLOps_2026_Neelima_Verma_fairness_compliant_harm) by Neelima Verma at Conf42 MLOps 2026.
- [The Paved Road Had a Compliance Gate](https://www.conf42.com/Platform_Engineering_2026_Sumeet_L_Ram_compliance_gate_paved) by Sumeet L. Ram at Conf42 Platform Engineering 2026.

[Watch Arpita Sheth's talk](https://www.conf42.com/MLOps_2026_Arpita_Sheth_compliance_governance_pipeline) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Compliance as a Pipeline Stage: Automating AI Governance in MLOps](https://www.conf42.com/MLOps_2026_Arpita_Sheth_compliance_governance_pipeline) at Conf42 MLOps 2026.
