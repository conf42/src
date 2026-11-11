# Gate every automated IT fix on a confidence score

Conf42 Blog, 2026-10-31, updated 2026-11-09. https://www.conf42.com/blog/platform2026/confidence-gated-agents-for-self-healing-ops

In short: Madhu Chenna (Electronic Arts) at Conf42 Platform Engineering 2026 presents ADOF, a reference architecture for self-healing IT ops with confidence-gated AI agents.

The disk that fills up slowly is the classic IT ticket nobody needed to file: the signal was there for days. At Conf42 Platform Engineering 2026, Madhu Chenna, Senior Manager at Electronic Arts, presented the Autonomous Digital Operations Framework (ADOF), a conceptual reference architecture for moving enterprise IT support from firefighting to governed automation, built around one design decision: every automated action has to earn a confidence score before it runs.

Honest scope, which Madhu states clearly himself: ADOF is a blueprint, not a product and not a case study. Its numbers are illustrative targets proposed for future validation.

## Silos make IT reactive

Monitoring, endpoint management and ITSM tools rarely talk to each other. An alert shows up in one, a spike of slowness tickets in another, and a human connects the dots under pressure. Madhu cites industry data, which he says his own experience validates, that up to 40% of Level-1 requests come from issues existing telemetry could have anticipated. Even repeatable, low-risk fixes such as clearing a temp folder or restarting a known flaky service still wait on a person.

## Unify, retrieve, specialise

ADOF's foundation is signal unification: endpoint telemetry (CPU, memory, disk, crashes, patch state), ITSM context (incident history, SLAs, change records) and asset metadata (owner, criticality, lifecycle) in one queryable stream. His example: a specific laptop model used by developers has frequent GPU driver crashes. One tool sees isolated crashes; correlated with who uses those laptops and a rise in slowness tickets from the same people, it becomes a systemic issue flagged before it hits a critical team.

On top sits RAG over runbooks, KB articles, postmortems and vendor docs, continuously ingested so agents retrieve the current fix rather than last year's. Then six specialised agents instead of one general one: incident prediction, asset health (for example predicting laptop battery failure), auto-remediation, procurement intelligence (order the replacement before the old machine dies), user experience (tie slow app loads to backend events), and a compliance and audit agent that checks every proposed action against policy.

## The confidence gate

Before acting, an agent computes a composite score from three dimensions. Enterprise health: is the environment already unstable, so the blast radius of any change is bigger? Business impact: is this an internal wiki or a production game authentication server? Automation confidence: how often has this exact action pattern worked before?

Example thresholds: above 85%, execute autonomously. Between 60% and 85%, create a ticket with the probable root cause and a recommended fix behind a one-click approval. Below 60%, full manual review. Madhu's argument is that this middle band, assisted recommendation, is where human trust gets built.

Every outcome feeds back. Successful fixes raise the confidence for that pattern; human overrides become labelled training signals; drift detection notices when a fix that used to work starts failing. Autonomy grows through a five-level maturity model: observe, recommend, assisted execution (the gate switches on), supervised autonomy with humans reviewing exceptions, and finally full autonomy with continuous policy validation and audit logging.

## What to take back on Monday

His four patterns are usable without adopting the whole framework: unify signals before automating anything; gate on a confidence score instead of static rules; start with one specialised agent domain, such as asset health; and build outcome capture first, since a system that doesn't record whether its fixes worked can't improve.

## Who should watch

IT operations and internal platform leaders sketching an AIOps roadmap who want a vocabulary for governed autonomy. If you want production results and a war story, this isn't that; it's an architecture proposal, presented as one.

## Related Conf42 talks

- [Reliable API Support: Human-in-the-Loop Agentic RAG for SRE](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Vishal_Shah_reliable_support_human) by Vishal Shah (Visa)
- [Zero Service Desk: Applying Machine Learning for Autonomous IT Support](https://www.conf42.com/Machine_Learning_2026_Anu_Arora_personalization_recommendation_platforms) by Anu Arora (ServiceNow)
- [From Alerts to Answers: Modern SRE with Observability, AI, and Agentic Ops](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Savi_Grover_alerts_answers_modern) by Savi Grover (Tekskills)

[Watch Madhu's talk](https://www.conf42.com/Platform_Engineering_2026_Madhu_Chenna_healing_rag_telemetry)

[Watch the talk on YouTube](https://youtu.be/3SLIcosY9WY).

## Watch the talk

[Designing a Self-Healing Ops Platform: Telemetry, RAG, and Confidence-Gated AI Agents](https://www.conf42.com/Platform_Engineering_2026_Madhu_Chenna_healing_rag_telemetry) at Conf42 Platform Engineering 2026.
