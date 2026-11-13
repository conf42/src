# Compliance risk lives between the documents, not inside them

Conf42 Blog, 2026-06-08, updated 2026-11-09. https://www.conf42.com/blog/llms2026/compliance-risk-lives-between-documents

In short: Varsha Shah at Conf42 LLMs 2026 on correlating payroll, tax and procurement records with graphs, risk scoring and LLMs to catch hidden compliance risk.

A payroll record can be correct, a tax filing can be correct, and the company can still be out of compliance. At Conf42 Large Language Models 2026, Varsha Shah, an enterprise technical architect, showed a framework that connects payroll, tax, procurement and transaction data so the risk that sits between systems becomes visible.

Her one-line diagnosis of most compliance failures: "The organization did not lack the data, the organization lacked correlation."

## The employee who moved

The example that makes the talk click is small and very familiar to anyone who has touched HR systems. An employee relocates. HR records the new work location. Payroll pays them correctly. The tax filing system submits the required filing on time. Every system, checked on its own, is green.

Connect the records and the problem appears: the new location puts the employee under a different tax jurisdiction with different reporting rules and deadlines, and the filing was based on the old one. No rule engine looking at one document at a time would flag it, because no single document is wrong.

## Three questions, three components

Shah structures the architecture around three questions: what is connected, what is risky, and what does the risk mean in this regulatory context.

- **A graph-based entity correlation engine** links employees to payroll records, payroll to tax filings, vendors to procurement, and transactions to the wider business process. LLMs help resolve ambiguous references, so the same entity spelled two ways in two systems ends up as one node.
- **An adaptive probabilistic risk model** combines signals such as unusual transaction patterns, jurisdictional inconsistencies, entity relationships, history and prior audits into a confidence-weighted risk score, so investigators work the highest-exposure cases first.
- **A jurisdictional normalization layer** aligns currencies, tax codes and reporting requirements across countries, which she describes as a translation layer for compliance intelligence.

The feedback loop ties them together: every audit outcome and investigation result goes back into the risk model, so the system learns which patterns were real.

## The LLM is the reasoning layer, not the chat window

The part most relevant to an LLM audience is where the model sits. In this design the LLM is not the user interface. It reads the unstructured material that rule engines ignore (contracts, policies, audit notes, regulatory guidance), connects it to the structured records, and writes the explanation an auditor will read.

Shah's point is that finding a risk is only half the job. Explaining why the risk exists is what lets a compliance team act on it, and that is where the language model earns its place.

## Evaluated on enterprise-shaped data

The framework was tested on about three million anonymized records spanning payroll, tax, procurement and transactions, across four jurisdictions and five years of history. She reports stronger detection of cross-system patterns, fewer false positives than rule-based systems and less auditor time spent gathering evidence. She does not put exact precision and recall figures on screen, so treat the results as directional.

She is also candid about the limits: LLM hallucination means every finding must be grounded in verified evidence, legacy data is messy and inconsistent, and regulations keep moving. Her conclusion is that AI is a force multiplier for compliance experts, not a replacement.

## Who should watch

Architects and data engineers building compliance, audit or fraud platforms in multi-country organizations, and anyone who has been asked to "add AI" to a rule engine and wants a sensible place to put it. If you are looking for model internals or code, this is an architecture talk rather than an implementation one.

## Related Conf42 talks

- [Advancing Financial Fraud Detection with Graph Databases: Innovations and Applications](https://www.conf42.com/Machine_Learning_2025_Venkateswarlu_Boggavarapu_fraud_detection_db_graph) from Conf42 Machine Learning 2025 goes further into the graph side.
- [Designing for Defensibility: Evidence-Centric Compliance Architecture in Customer-Facing Financial Platforms](https://www.conf42.com/Golang_2026_Manasa_Uppula_designing_defensibility_evidence) from Conf42 Golang 2026 is about making the evidence hold up afterwards.
- [AI-Driven Financial Reconciliation: Enhancing Accuracy, Speed, and Compliance Through Human-AI Synergy](https://www.conf42.com/Large_Language_Models_LLMs_2025_Naveen_Gowda_financial_reconciliation_compliance) from Conf42 LLMs 2025 covers a neighbouring problem with the same human-plus-AI stance.

[Watch Varsha Shah's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Varsha_Shah_correlation_fraud_compliance)

[Watch the talk on YouTube](https://youtu.be/Kr4V2ehzueI).

## Watch the talk

[LLM Enabled Multi Document Correlation for Financial Compliance and Fraud Detection](https://www.conf42.com/Large_Language_Models_LLMs_2026_Varsha_Shah_correlation_fraud_compliance) at Conf42 Large Language Models (LLMs) 2026.
