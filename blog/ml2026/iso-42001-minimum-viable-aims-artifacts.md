# ISO 42001 for beginners: the 16 documents an AI audit asks for

Conf42 Blog, 2026-02-19, updated 2026-11-09. https://www.conf42.com/blog/ml2026/iso-42001-minimum-viable-aims-artifacts

In short: Security engineer Aleksandra Drobnjak at Conf42 Machine Learning 2026 maps the minimum ISO 42001 paperwork that makes an AI management system auditable.

Sooner or later someone asks who approved a model change, what data went into it, and whether anyone can explain it. At [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026), security engineer Aleksandra Drobnjak answered that question with a short list: the 16 documentation artifacts an ISO 42001 auditor expects to see before concluding that an organisation manages its AI systems in a controlled, repeatable way. She calls it "Minimum Viable AIMS", and the point is clarity about risk, ownership and change, not perfect paperwork.

Drobnjak comes at this from both sides of the table. She has spent more than ten years in engineering roles across multi-cloud and container security, supported ISO and SOC 2 audits, and trained as an ISO 27001 and ISO 42001 lead auditor. So the talk reads less like a summary of the standard and more like a walk through what an auditor actually opens first.

## The standard in one paragraph

ISO 42001 was published in 2023 and is the first certifiable standard for managing AI at the organisational level. It doesn't tell you which models or tools to use. It has ten clauses, with clauses 4 to 10 holding the auditable requirements, plus Annex A with 38 controls across nine control objectives. Not every control is mandatory: you pick them by risk, scope and context. It follows the plan-do-check-act cycle, so it sits comfortably next to ISO 27001. Certification runs as a stage one documentation audit, a stage two effectiveness audit, then annual surveillance audits inside a three-year cycle.

A nice practical aside: you can pull the ISO 42001 certificates behind AWS services such as Amazon Bedrock, Transcribe and Textract from AWS Artifact, then check the certificate number yourself on IAF CertSearch. Drobnjak says it takes a couple of minutes.

## Scope is where shadow AI gets caught

The first artifact, the AIMS scope (clause 4.3), sounds dull and does the most work. Her MLOps example is familiar: a model starts in a notebook, someone wires it into a pipeline, and it is influencing real workflows before anyone decided whether it belongs inside governance. The same gap covers engineers pasting company material into personal AI accounts whose default settings may let the vendor train on it.

She also points at ordinary infrastructure mistakes: Jupyter, Kubeflow or MLflow instances left reachable from outside or from production networks. A written scope forces the question of which ML tools may run in production and which environments need authentication, logging and approvals.

## Risks that never become tickets don't count

The planning artifacts (clause 6) exist because risks get discussed, even documented, and then nothing changes. Each risk or opportunity needs an owner, a decision and a concrete next step that lands on someone's board. A repeatable risk assessment method stops one team calling a model change low risk while another blocks the same change outright. She treats model artifacts as executable components, not just data, which is why promotion shouldn't be "just another commit".

The statement of applicability example she shows is control A.5.5 on societal impact, and she makes it concrete: energy use and carbon footprint, who gains or loses access to tools, whether a decision can be understood and challenged, and effects on health and wellbeing.

## Operations, audits and the closing loop

The rest of the list follows the lifecycle: competence records (7.2), the documentation your teams actually rely on (7.5, the place for release notes and prompt changes that otherwise live in Slack DMs), operational controls (8.1), the risk register, treatment plans (8.3), AI system impact assessments (8.4), monitoring results (9.1), internal audit (9.2), management review (9.3), and nonconformities with corrective actions (10.2). She explains the difference between a minor nonconformity, such as a missing approval record, and a major one that signals a systemic breakdown and can delay or suspend certification.

Her strongest takeaway is the one engineers tend to nod at: "advanced models rarely cause problems by themselves." Missing ownership, missing traceability and missing feedback loops do. She is also frank that certification costs time, attention and budget, so a risk-based approach beats trying to do everything at once.

## Who should watch

Watch it if you run ML platforms or security and someone has just said the word "audit" in a meeting, or if you need a checklist to start an AIMS without boiling the ocean. It is a beginner-friendly talk by design; if you have already been through an ISO 42001 stage two audit, you'll mostly be checking your own list against hers.

## Related Conf42 talks

- [GenOps: a governance-driven model for safe, high-velocity AI in CI/CD](https://www.conf42.com/DevOps_2026_Neeraj_Kumar_Singh_Beshane_governance_genai_velocity), Neeraj Kumar Singh Beshane (Meta), Conf42 DevOps 2026
- [Compliance as a pipeline stage: automating AI governance in MLOps](https://www.conf42.com/MLOps_2026_Arpita_Sheth_compliance_governance_pipeline), Arpita Sheth, Conf42 MLOps 2026
- [Responsible AI product management for production LLM lifecycles](https://www.conf42.com/Large_Language_Models_LLMs_2026_Vijayalakshmi_Narasimhan_governance_lifecycle_products), Vijayalakshmi Narasimhan, Conf42 LLMs 2026

[Watch Aleksandra Drobnjak's talk](https://www.conf42.com/Machine_Learning_2026_Aleksandra_Drobnjak_documentation_artifacts_beginners)

[Watch the talk on YouTube](https://youtu.be/ecd60IxMPU4).

## Watch the talk

[Minimum Viable AIMS: ISO 42001 Required Documentation Artifacts for Beginners](https://www.conf42.com/Machine_Learning_2026_Aleksandra_Drobnjak_documentation_artifacts_beginners) at Conf42 Machine Learning 2026.
