# Nine ways SOX audit teams use AI, and the sign-offs each one needs

Conf42 Blog, 2026-06-03, updated 2026-11-09. https://www.conf42.com/blog/llms2026/ai-in-sox-audits-validation-is-not-review

In short: Karishma Velisetty at Conf42 LLMs 2026 maps nine AI use cases in SOX and ICFR audit work to their risks and the human controls that make them reliable.

AI tools are good at producing text that sounds right, and in a SOX audit that is precisely the danger. At Conf42 Large Language Models (LLMs) 2026, independent researcher Karishma Velisetty walks through nine places internal audit teams now use AI, from reviewing analytics scripts to drafting control narratives, and for each one names the risk and the control that makes the output fit for reliance.

If you build tooling for finance or audit teams, this is a rare look at how auditors themselves think about your output.

## Three kinds of tools, three risk profiles

Karishma groups the tools in use: code and analytics assistants (Copilot, Cursor, Claude, ChatGPT) used by data-savvy auditors to write and review scripts; language and document AI for drafting, reviewing and summarizing; and specialist audit AI wired directly into SOX workflows. Each carries a different risk, and the governance has to match.

## The five that are already common

- **Reviewing audit analytics scripts.** The big risk is over-reliance. If an auditor accepts an AI's explanation of a script without understanding the logic, human review becomes a rubber stamp. Her controls: a formal human sign-off on AI findings, a log of each AI review session (tool, date, findings) for external auditors and PCAOB purposes, and a second-level reviewer.
- **Contract review.** Contracts are confidential and often hold material non-public information. Her rule is simple: consumer AI never touches them, and enterprise AI is used only in a private, controlled deployment. Then check for misread clauses and hallucinated lease or accounting terms.
- **Invoice matching and reconciliation.** One of the highest-return uses, with one condition external auditors test first: population completeness. Run the match on an incomplete population and the results aren't audit evidence.
- **Control narratives.** This is where she sees the most enthusiasm and the most quiet quality loss. The fix is mandatory process-owner validation that the described steps match what actually happens.
- **Test sheets and workpapers.** The concern is coverage of the relevant assertions, and numbers the AI makes up. A suggested sample size has to come from your sampling policy and materiality, not from the model.

## Four that are growing fast

Journal entry testing, user access review, flux analysis and walkthrough documentation are earlier in adoption. AI makes full-population journal entry analysis feasible, but again only if you can prove it ran on the full population. Segregation-of-duties analysis is only as good as the role matrix; a stale matrix gives confident nonsense, and certification decisions can't be delegated to AI. For flux analysis she warns about well-written AI drafts containing assertions management never reviewed. Walkthrough recordings bring a legal question before an audit one: recording consent.

## Validation is not the same as review

The closing message is one sentence long and worth pinning above the desk: review means reading the output, validation means an accountable person formally signs off that it is correct and complete. Technical controls matter most for code and analytics, people and process controls for contracts and narratives, and monitoring keeps the whole framework honest. Confidentiality is non-negotiable: one material non-public information leak into a consumer tool is a regulatory and legal problem.

Note on scope: the abstract also mentions security scanners such as Bandit, SonarQube and CodeQL. The recorded talk spends its time on the nine use cases and the governance controls.

## Who should watch

Internal audit and SOX teams adopting AI, engineers building analytics or AI tools for finance functions, and anyone writing a policy for AI use in a regulated workflow.

## Related Conf42 talks

- [AI-Driven Financial Reconciliation](https://www.conf42.com/Large_Language_Models_LLMs_2025_Naveen_Gowda_financial_reconciliation_compliance) by Naveen Gowda (Couchbase), on human-AI reconciliation workflows.
- [Adding Tamper-Evident Audit Trails to AI Agents in Production](https://www.conf42.com/MLOps_2026_Joao_Marques_audit_tamper_agents) by Joao Marques (Asqav), on proving what an AI actually did.
- [Security and auditing tools in Large Language Models (LLM)](https://www.conf42.com/Large_Language_Models_LLMs_2025_Jose_Manuel_Ortega_security_auditing_tools) by Jose Manuel Ortega, on auditing the models themselves.

[Watch Karishma Velisetty's talk](https://www.conf42.com/Large_Language_Models_LLMs_2026_Karishma_Velisetty_governance_audit_assistants)

[Watch the talk on YouTube](https://youtu.be/ogTyNTckfXw).

## Watch the talk

[From Acceleration to Assurance: Governing AI Code Assistants in SOX and ICFR Audit Analytics](https://www.conf42.com/Large_Language_Models_LLMs_2026_Karishma_Velisetty_governance_audit_assistants) at Conf42 Large Language Models (LLMs) 2026.
