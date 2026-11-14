# Third-party risk was built for annual reviews; ML makes it continuous

Conf42 Blog, 2026-02-14, updated 2026-11-09. https://www.conf42.com/blog/ml2026/third-party-risk-as-ml-system-circle

In short: Sagar Sudhir Behere (Circle) at Conf42 Machine Learning 2026 on rebuilding vendor risk management with NLP, semantic dedup, model ensembles and event-driven monitoring.

Risk does not wait for your annual vendor review. At Conf42 Machine Learning 2026, Sagar Sudhir Behere, Head of Third Party Risk Management at stablecoin issuer Circle, described how his team re-architected third-party risk management (TPRM) as a machine-learning system, replacing calendar reviews and static questionnaires with document extraction, adaptive questions and event-driven monitoring.

He pitches it as a playbook rather than a theory or a vendor pitch, and it is refreshingly specific about where humans stay in the loop.

## The process was designed for a slower world

Behere names three structural problems. Calendar-based reviews assume risk politely waits its turn, so a change in month two surfaces in month twelve, if you are lucky. Static questionnaires ask every vendor the same questions in the same order, burying low-risk vendors and under-examining high-risk ones. Manual evidence review has analysts reading stacks of policies and SOC reports, and two analysts can read the same PDF and reach different conclusions without either being wrong.

Meanwhile a modern enterprise depends on hundreds or thousands of third parties (cloud providers, SaaS, payment processors, data vendors, open-source dependencies) and regulators want more transparency and continuous oversight, not less. His summary: risk now moves at the speed of software, not audit cycles.

## Read the documents with NLP, keep the receipts

The architecture has four parts: continuous data ingestion, intelligent processing, dynamic risk evaluation and continuous monitoring. The first bottleneck they attacked was evidence review. NLP models extract and normalise control evidence from unstructured vendor artefacts, asking whether a document demonstrates the specific control rather than whether it looks fine.

The detail that matters for auditors is traceability: every extracted data point links back to the sentence in the source document, so you can click from a risk conclusion to the evidence. Humans moved from reading documents to validating judgements.

## Ask each question once

Next came questionnaire redundancy. Different frameworks (SOC, ISO, internal policy, regulatory requirements) ask for the same control in different words, so semantic similarity models cluster questions by meaning. Instead of five near-identical questions, the vendor sees one. Follow-ups adapt to the answers, digging deeper only where a control looks weak or ambiguous, and context-aware routing sends security questions to security people and finance questions to finance. Behere describes this as the point where vendors stopped calling the process painful.

## Never trust a single model

For the obvious "what if the model is wrong" question, the answer is ensembles. Multiple independent models evaluate the same risk signal; agreement raises confidence, disagreement flags the case. Every output carries a confidence score: high confidence moves the workflow forward, low confidence sends it to a person. That also answers the governance worries about single-model bias and black boxes, because you can explain both the conclusion and how sure the system is.

## From periodic reviews to listening for events

The bigger shift was to stop reassessing on a schedule and react to material events instead: threat intelligence, security advisories and CVEs, financial indicators such as credit ratings and market stress, public disclosures like breach notices and enforcement actions, and behavioural anomalies. Reassessing everything continuously would just create noise faster, so the system listens for meaningful changes and triggers action only then.

Models trained on historical cyber, operational and financial incidents look for the weak signals that tend to precede trouble (missed patches, delayed disclosures, financial stress) so the team can ask targeted questions or escalate controls early. Every score comes with its contributing factors and a full audit trail, built with regulatory expectations in mind from the start.

## Who should watch

Risk, compliance and security engineers in regulated companies, and ML engineers asked to build tooling for them. His closing advice is a sensible starting order: automate evidence extraction, cut redundant questions, then add signal-driven monitoring. No perfect model required.

## Related Conf42 talks

- [Rethinking Supply Chain Security in the Age of Agentic AI](https://www.conf42.com/DevSecOps_2026_Roshan_Piyush_supply_chain_security) by Roshan Piyush (Harness) covers the software side of third-party exposure.
- [Managing Vendor Incidents](https://www.conf42.com/Incident_Management_2024_Mandi_Walls_25_vendor_incidents_management) by Mandi Walls (PagerDuty) is what to do when a vendor's bad day becomes yours.
- [Cloud-Native Enterprise Architecture for Financial Risk Governance](https://www.conf42.com/Kube_Native_2025_Sreenivasulu_Gajula_fraud_governance_finance) by Sreenivasulu Gajula (Osmania University) looks at risk governance architecture in finance.

[Watch Sagar Sudhir Behere's talk](https://www.conf42.com/Machine_Learning_2026_Sagar_Sudhir_Behere_streaming_realtime_analytics)

[Watch the talk on YouTube](https://youtu.be/ri4E0oHXph8).

## Watch the talk

[Machine Learning–Driven Third-Party Risk Management at Scale](https://www.conf42.com/Machine_Learning_2026_Sagar_Sudhir_Behere_streaming_realtime_analytics) at Conf42 Machine Learning 2026.
