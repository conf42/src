# Rust AI copilots for loans, shelves and SCADA, from reusable parts

Conf42 Blog, 2025-08-21. https://www.conf42.com/blog/rustlang2025/rust-ai-copilot-automation-across-industries

In short: Sarat Piridi of Hanwha Qcells at Conf42 Rustlang 2025 on Rust AI copilots for finance, retail, manufacturing and utilities, and the patterns behind them.

Enterprise automation usually dies in the integration layer, somewhere between a modern API and a point-of-sale terminal that has never heard of one. At Conf42 Rustlang 2025, [Sarat Piridi](https://www.conf42.com/Rustlang_2025_Sarat_Piridi_agents_zero_systems), a senior engineer at Hanwha Qcells, showed how he would build AI copilots in Rust for loan processing, retail inventory, procurement and utilities, and which design patterns keep them maintainable.

It is a long, wide-ranging talk. The industry examples are described in general terms rather than as named deployments; the architecture and the patterns are the parts worth your time.

## Three building blocks

Piridi's copilot has three parts:

- **A data extraction engine** that pulls from spreadsheets, documents, databases and older file formats, processing many streams at once without wasting memory.
- **An agent system**, the brain, which uses AI models to understand data, make decisions, coordinate tasks and roll back actions when something goes wrong.
- **An integration layer** that connects to modern systems through APIs and to legacy systems that have none.

His reuse argument is that Rust's type system and modules make these parts behave like building blocks: a parser or decision model built for a finance project can be configured for healthcare or retail later, much like a modular ERP where each customer enables a different subset of features.

## Four industries, one shape

- **Finance:** loan processing that checks documents, verifies information and applies regulatory rules, with the core analysis in Rust and approvals left in tools like Power Platform.
- **Retail:** real-time inventory across hundreds of stores without two systems overwriting each other, predictive reordering, and an integration layer that pulls transaction data out of legacy POS systems.
- **Manufacturing:** procurement agents that check supplier availability, compare prices and place orders in parallel.
- **Utilities:** extending SCADA systems without replacing them, with fault-tolerant monitoring and automated regulatory reporting for audits.

## Patterns that make the compiler do the review

The design-pattern section is the best part. The actor model lets components run independently without stepping on each other's data. The command pattern packages each task so it can be undone, which is exactly what a copilot that takes actions needs. The repository pattern hides storage so you can switch databases without rewriting logic. Feature flags control rollouts.

The standout is the typestate pattern, which encodes the steps of a workflow in types so that, in his words, "we can't accidentally run the process in the wrong sequence". For loan approvals and audits, a compile error beats a post-incident review. His crate list: Tokio for concurrency, Serde for data formats, rust-bert for NLP, Rayon for parallel processing and Tonic for gRPC.

## The claimed payoff

Piridi cites 60 to 75% less development time for new workflows once the core components exist, 89% fewer production incidents and 83% faster overall process times, along with about 30% lower memory use. These are presented as typical results, not tied to a named system. His advice for starting is sensible: pick one process where reliability really matters, pilot a Rust copilot there, and reuse what you built in the next project.

## Who should watch

Engineers building AI-assisted business automation that must talk to legacy systems, and anyone who wants a quick tour of typestate and command patterns applied to agents.

## Related Conf42 talks

- [Orchestrating Enterprise Intelligence: Designing Multi-Agent AI for ERP and Hybrid IT Systems](https://www.conf42.com/Prompt_Engineering_2025_Kasee_Palaniappan_enterprise_erp_intelligence) by Kasee Palaniappan (SAP Ariba) at Conf42 Prompt Engineering 2025.
- [Cloud-Native AI in Procurement](https://www.conf42.com/Cloud_Native_2025_Parameswara_Rao_Tatini_procurement_automation_resilience) by Parameswara Rao Tatini (SAP) at Conf42 Cloud Native 2025.
- [AI-Driven Productivity Enhancements in Enterprise Engineering](https://www.conf42.com/Rustlang_2024_Vinay_Puri_ai_enhancements_productivity_enterprise) by Vinay Puri (Amazon) at Conf42 Rustlang 2024.

[Watch Sarat Piridi's talk](https://www.conf42.com/Rustlang_2025_Sarat_Piridi_agents_zero_systems) or the [YouTube recording](https://youtu.be/WdXl4mTDKRQ).

## Watch the talk

[Building Rust-Powered Copilot Automation: Cross-Industry AI Process Systems](https://www.conf42.com/Rustlang_2025_Sarat_Piridi_agents_zero_systems) at Conf42 Rustlang 2025.
