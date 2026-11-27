# A loan valuation you cannot replay is one you cannot defend

Conf42 Blog, 2026-11-19. https://www.conf42.com/blog/mlops2026/reproducible-pipelines-illiquid-loan-valuation

In short: Ankur Mehra at Conf42 MLOps 2026 on valuing illiquid loans with pinned versions, signed run manifests and event-driven revaluation.

A stock has a quoted price. A mortgage or a commercial loan sitting on a bank's book does not, so its value has to be modelled, and remodelled every time rates, spreads or borrower behaviour move. At Conf42 MLOps 2026, Ankur Mehra, who has spent more than fifteen years in financial risk technology for major US banks, argues that the model is only half of that job. The other half is a pipeline in which every valuation run pins its data, assumptions and model config, so any historical number can be replayed from its manifest.

His two opening points set the bar. Accuracy alone is insufficient if the model cannot be run consistently at scale, and auditability is non-negotiable because regulators expect every valuation to be traceable back to its inputs.

## Three stages, each allowed to say no

The pipeline has three stages: market data ingestion, scenario setup and cash flow modelling, where payments are projected and discounted to a present value. Each stage is independently versioned, testable and auditable, and failures are isolated. "A bad input should stop the pipeline," Ankur Mehra said at Conf42 MLOps 2026. It should never pass silently downstream into a number someone signs off on.

Market data is treated as a first-class artifact. Rate curves, credit spreads and prepayment indices come from multiple providers, and every ingestion batch gets a timestamp and a hash, so you can prove which data a valuation used. Schema validation and anomaly detection run at the boundary, and rejected batches go to a dead letter queue where they are quarantined and reviewable.

Scenarios are separated from model logic. A registry stores each named, versioned scenario as an immutable artifact, overrides are injected when the pipeline is invoked and never hard-coded, and base, stress and regulatory cases fan out in parallel against the same cash flow engine. That is faster, and it guarantees they all ran on identical inputs.

The engine itself is stateless and deterministic. Prepayment and credit models are pluggable, discount curves are injected, and the engine outputs intermediate cash flows as well as the final NPV. When a value moves, those intermediate numbers are how you explain why.

## Reproducibility breaks in four boring ways

Ankur's list will sound familiar outside finance too. Reference data gets overwritten in place. Model parameters live only in someone's notebook. Someone makes a manual override to an assumption and does not document it. A dependency is upgraded in the middle of a cycle.

The fix is versioning in three layers and a manifest that ties them together. The data layer covers the market data snapshot, portfolio positions and reference data. The assumption layer covers prepayment speeds, credit loss curves and discount rate conventions. The model config layer covers algorithmic parameters, feature sets and calibration output. Every run ID pins a specific version in all three.

Each run then emits a signed manifest with the data snapshot IDs, the assumption set hash, the model config version, a hash of the pipeline and a digest of the execution environment, kept in append-only storage. "That manifest is your audit defense," he said. In his closing principles he puts the reason plainly: mutation is the root cause of most reproducibility failures.

## Rollback has to be one command

Changing a live valuation model follows a promotion path: shadow mode on real data with outputs unused, a challenger test against the current baseline, a staged rollout to a subset of the portfolio, then full cutover. At every step, rollback must be a single command with zero manual intervention. "If going back is hard, people hesitate, and that's when problem starts."

Around that sit the controls. Four categories of metrics answer four questions: is the pipeline healthy, are the inputs healthy, do the results look plausible, and do portfolio-level business rules hold before anything is published. He calls the last one the most important, the final gate between the pipeline and the people who rely on its numbers.

Testing has four layers as well: unit tests for cash flow and discounting logic, integration tests on synthetic loan portfolios, regression tests against pinned historical baselines so you know if a code change moved a number, and stress tests for numerical stability at extreme inputs. Lineage should answer in seconds which runs consumed a given version of a rate curve. When a vendor calls to say a curve was wrong, that query is the difference between a quiet afternoon and a long week.

Every production run also produces an audit pack: the signed manifest, a lineage graph report, intermediate cash flow snapshots, output distribution statistics, the business rule validation report and the approval record.

## Stop revaluing loans where nothing changed

Most valuation systems revalue the whole portfolio on a schedule, spending most of the compute on loans where nothing changed. Ankur's last chapter flips that: a rate curve update revalues the affected tranches, a position change revalues the impacted loans, and an assumption update triggers a scoped rerun with lineage showing which numbers were refreshed and why. This only works because every input is versioned and every dependency tracked, so the system knows what needs recomputing.

## Who should watch

Engineers and quants running valuation, risk or pricing models in regulated finance, and MLOps people who want a clean example of reproducibility taken seriously. The talk is an architecture walkthrough of about sixteen minutes with no code, no demo and no named tools, so come for the design rules and bring your own stack. The patterns transfer to any model whose output someone has to sign.

## Related Conf42 talks

- [Ledger to Lake: Automating Database DevOps for ML in Finance with BigQuery, Liquibase, and Harness CI](https://www.conf42.com/MLOps_2026_Alejandro_Mercado_bigquery_liquibase_harness) by Alejandro Mercado at Conf42 MLOps 2026.
- [Compliance as a Pipeline Stage: Automating AI Governance in MLOps](https://www.conf42.com/MLOps_2026_Arpita_Sheth_compliance_governance_pipeline) by Arpita Sheth at Conf42 MLOps 2026.
- [SRE for National-Scale Regulatory Reporting: HA, DR, and Audit-Ready Design](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Bhargavaram_Potharaju_national_scale_regulatory) by Bhargavaram Potharaju at Conf42 SRE 2026.

[Watch Ankur Mehra's talk](https://www.conf42.com/MLOps_2026_Ankur_Mehra_loan_valuation_pipelines) from [Conf42 MLOps 2026](https://www.conf42.com/mlops2026).

## Watch the talk

[Building Resilient MLOps Pipelines for Illiquid Loan Portfolio Valuation](https://www.conf42.com/MLOps_2026_Ankur_Mehra_loan_valuation_pipelines) at Conf42 MLOps 2026.
