# RAG agents for investment banking reconciliation, trade by trade

Conf42 Blog, 2025-10-23, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/rag-agents-investment-banking-reconciliation

In short: Swamy Biru of JPMorgan Chase at Conf42 Prompt Engineering 2025 on RAG-backed multi-agent systems for trade processing, reconciliation and compliance.

Reconciliation is the job nobody in a bank brags about and everybody depends on. At Conf42 Prompt Engineering 2025, Swamy Biru, a Vice President of Software Engineering at JPMorgan Chase, laid out how retrieval-augmented generation plus a set of specialised agents can move trade validation, reconciliation and compliance checks from overnight batches to something close to real time.

This is an architecture talk, not a demo. It is a map of where LLMs fit in front, middle and back office systems, and which guardrails a regulated shop needs around them.

## The problem: the same trade, ten slightly different records

Swamy frames the pain in three parts: data inconsistency, manual processes and real-time risk. A single trade generates data points that must agree across front-office trading systems, middle-office risk platforms and back-office settlement. The inputs come from internal systems, market data vendors, regulatory platforms and counterparty messages, each with its own format and update rhythm.

Batch processing leaves windows where systems disagree. Highly paid people then spend their days hunting discrepancies that add little strategic value but cannot be skipped. And regulators want audit trails and data lineage on top of all of it.

## Retrieval first, then specialised agents

The architecture he shows routes a query (a trade, in whatever format it arrives) to an LLM that first pulls context from a vector database, then hands work to specialised agents: trade processing, risk assessment, compliance monitoring and settlement reconciliation. Each agent owns one domain and they coordinate through defined interfaces, which keeps the system modular.

Why retrieval matters here: the model answers from transaction databases, settlement platforms and counterparty communications rather than from what it absorbed in training. That gives you current information and an audit trail. Semantic search over embeddings handles the fact that financial terminology varies across desks, counterparties and time periods, so the system can find the relevant rule or record even when the query is phrased differently.

Prompt engineering sits in the middle of the data flow: templates, intent classification and prompt optimisation turn market data, internal reports and regulatory documents into compliance alerts, recommendations and client reports. Swamy's claim is that engineered prompts reduce hallucination and keep answers within the domain.

## Reconciliation that knows what equivalent means

The sharpest section compares traditional and AI-assisted reconciliation. Traditional: overnight batches, discrepancies found late, and lots of false positives from format differences, each one investigated by hand. The AI version runs continuously and, crucially, understands context: different spellings of a counterparty name, a settlement date shifted for a holiday, a price difference within tolerance. Those are not real breaks, and treating them as such is what buries reconciliation teams.

He extends the same idea to risk (spotting correlations across positions that standard models miss) and compliance (flagging patterns before they become violations, and tracking regulatory changes across jurisdictions).

## The guardrails a bank will ask about

Swamy lists six security and compliance pieces: encryption at rest, in transit and in use; role- and attribute-based access control; tamper-proof audit logging; an explanation for every AI decision that a human reviewer can check; ongoing model validation as markets shift; and automated incident response. The microservice layout lets services scale independently during volatile market periods and keeps a failure in one component from taking down the rest.

The abstract puts the results at 40% efficiency gains and 95% accuracy at major investment banks; the talk itself focuses on the architecture rather than walking through those measurements.

## Who should watch

Engineers and architects in financial services sketching where LLMs go in a trade lifecycle, and anyone who needs a vocabulary for talking to compliance about RAG. If you want code, benchmarks or a live system, this is a whiteboard session.

## Related Conf42 talks

- [Swamy Biru on securing RAG and agentic systems in finance](https://www.conf42.com/DevSecOps_2025_Swamy_Biru_finance_rag_ai), his security-focused companion talk at Conf42 DevSecOps 2025.
- [Jaya Krishna Vemuri on cloud-driven reconciliation in investment banking](https://www.conf42.com/Chaos_Engineering_2025_Jaya_Krishna_Vemuri_investment_banking_accuracy) at Conf42 Chaos Engineering 2025.
- [Ofer Mendelevitch on measuring hallucinations in RAG](https://www.conf42.com/Large_Language_Models_LLMs_2024_Ofer_Mendelevitch_rag_measuring_hallucinations), for the question of how you know the answer is right.

[Watch Swamy Biru's talk](https://www.conf42.com/Prompt_Engineering_2025_Swamy_Biru_finance_efficiency_agents), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/IEc3URt5fIg).

## Watch the talk

[RAG Agents in Finance: Prompt Engineering for 40% Efficiency Gains](https://www.conf42.com/Prompt_Engineering_2025_Swamy_Biru_finance_efficiency_agents) at Conf42 Prompt Engineering 2025.
