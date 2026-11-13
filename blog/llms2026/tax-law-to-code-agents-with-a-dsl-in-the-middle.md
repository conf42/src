# Turning tax law into code with agents and a DSL in the middle

Conf42 Blog, 2026-06-02, updated 2026-11-09. https://www.conf42.com/blog/llms2026/tax-law-to-code-agents-with-a-dsl-in-the-middle

In short: Abdul Basit Iqbal (Amazon) at Conf42 LLMs 2026 on a multi-agent pipeline that turns regulatory changes into validated, auditable tax logic.

A tax jurisdiction changes a rule, and the enterprise typically takes three to six months to get it into production. At Conf42 Large Language Models (LLMs) 2026, Abdul Basit Iqbal, a Senior Software Development Engineer and lead architect of Amazon's global tax engine, lays out an agentic architecture meant to shrink that cycle to hours, and spends as much time on the governance around the models as on the models.

## Compliance drift lives in the handoffs

Abdul names the problem compliance drift. Between a law changing and the system applying it there are four human handoffs: legal interpretation, compliance translation, developer implementation, QA. Each is slow and lossy, and while they run you are over-collecting, under-collecting or applying the wrong rule. His examples are mundane on purpose: a Canadian First Nations exemption, a ZIP code boundary shift in Tennessee.

Classic rule engines never fixed this because tax law isn't written to be structured. Phrases like substance over form have been argued over in court for decades, one regulation can reference treaties and a guidance document from 1998, and the same transaction can be taxed differently depending on entity structure or where a billing address falls. That is the opening for LLMs: the first technology that can read legal prose and emit structured output.

## Four stages, each allowed to say "not sure"

The architecture, which he calls Autonomous Compliance Infrastructure, is a set of purpose-built agents rather than one model:

1. **Monitoring** watches gazettes, tax authority sites and treaty databases continuously and classifies each change by tax type, jurisdiction and effective date.
2. **Legal NLP** extracts the semantics and scores its own confidence. A clear rate change with a date proceeds; ambiguous language or a contested ruling goes to a human before any rule is extracted.
3. **A domain-specific language** captures conditions, thresholds, rates and exemptions in a human-readable, technology-independent form.
4. **A Tax-to-Code engine** uses fine-tuned coding models to generate implementations from the DSL.

Isolation is the point. A low-confidence interpretation escalates instead of flowing downstream, and a failed validation stops the pipeline, so failures stay contained.

## The DSL is the real product

Abdul calls the DSL the strategic centre. Natural language is ambiguous and code is tied to one system; the DSL sits between them. One DSL rule can generate compliant code for a Java billing system, a Python microservice and a TypeScript front end, and because it's version-controlled like source, you can always ask what a rule looked like on January 1st and why it changed. His second lesson is that DSL design is strategic intellectual property: get it wrong and everything downstream is wrong too.

## Nothing generated ships unvalidated

Generated code goes through static analysis, regression tests, differential tests that compare old and new rule outputs, and formal property checks on boundary conditions. Then the rollout is staged: shadow mode, canary, gradual activation, full deployment with rollback kept live. Humans keep three kinds of decision: novel or low-confidence interpretations, changes spanning many jurisdictions, and anything touching an active audit or disputed position. Every rule traces back to the statute that produced it, and every approval is tied to an authenticated identity.

His lessons are refreshingly unglamorous. Confidence estimation matters more than accuracy. Some governments publish machine-readable rules and others publish scanned PDFs. And governance maturity decides success more than model quality: if nobody has defined who approves a rule change, the system stalls at the first hard call. Start with simple single-rate VAT regimes before cross-border complexity.

## Who should watch

Engineers building LLM systems for any regulated domain (tax, finance, insurance, legal), and architects who want a concrete pattern for confidence-gated escalation. It is an architecture talk, with no live demo or code.

## Related Conf42 talks

- [Prompt Engineering for AML: Building Reliable Compliance Workflows at Scale](https://www.conf42.com/Prompt_Engineering_2026_Pratik_Patel_aml_compliance_workflows) by Pratik Patel (Hexaware Technologies), on LLMs inside financial-crime workflows.
- [SRE for National-Scale Regulatory Reporting](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Bhargavaram_Potharaju_national_scale_regulatory) by Bhargavaram Potharaju (Wells Fargo), on keeping compliance-critical platforms up and audit-ready.
- [eLicensing and ePermitting with AI](https://www.conf42.com/Golang_2025_Sneha_Kalagarla_elicensing_ai_compliance) by Sneha Kalagarla, on AI for government rules from the other side of the counter.

[Watch Abdul Basit Iqbal's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Abdul_Basit_Iqbal_compliance_agents_tax)

[Watch the talk on YouTube](https://youtu.be/Om4un3fTh7Q).

## Watch the talk

[Agentic AI for Autonomous Compliance in Enterprise Tax Systems Using LLM-Driven Tax-to-Code Pipelines](https://www.conf42.com/Large_Language_Models_LLMs_2026_Abdul_Basit_Iqbal_compliance_agents_tax) at Conf42 Large Language Models (LLMs) 2026.
