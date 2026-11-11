# NEPA permitting with LLMs needs prompts that act like governed rules

Conf42 Blog, 2026-10-04, updated 2026-11-09. https://www.conf42.com/blog/prompt2026/nepa-permitting-prompts-as-governed-rules

In short: Mohit Upadhyay of Tech Mahindra at Conf42 Prompt Engineering 2026 on evidence-first prompts, provenance and RAG for NEPA categorical exclusions.

A cell tower next to a historic district looks like a routine install until someone asks whether it disturbs the ground, changes the visual character of a landmark or needs sign-off from three agencies. At Conf42 Prompt Engineering 2026, Mohit Upadhyay, Principal Solutions Architect at Tech Mahindra, walked through how his team builds AI support for National Environmental Policy Act (NEPA) Categorical Exclusion determinations, and why the prompt there has to behave like a versioned, tested business rule.

The headline idea: permitting is about evidence, and a fluent answer is never proof that an exclusion applies.

## The domain, briefly

Federal infrastructure, telecom, utility and defence projects near protected sites face NEPA plus Section 106 of the National Historic Preservation Act. Analysts check thresholds such as ground disturbance and structure height across several agencies, mostly by hand. Mohit's platform combines LLMs with computer vision, geospatial data and retrieval over sources like Google Street View, NPS IRMA, FCC ULS, EPA ECHO, USGS 3DEP and State Historic Preservation Office systems.

If you don't work in permitting, the patterns still transfer. That's the reason to watch.

## Every fact keeps its provenance

The evidence model is the most reusable part. Project facts (footprint, excavation, elevation, access, utilities) stay separate from retrieved reference material. Each fact carries its source file, collection date, extraction method and reviewer status. Geospatial records keep their coordinate system, precision and processing history.

Mohit also insists that missing data must never turn into a clearance. A true negative, a failed query and an inaccessible record are three different outcomes. If the authoritative source is unreachable, the system asks a human for manual evidence instead of assuming the best.

## Keep NEPA and Section 106 in separate fields

One small rule with big consequences: hold separate status fields for NEPA and historic preservation, and never call a NEPA pathway complete while other reviews are unresolved. Similar-looking sites don't get to inherit each other's outcomes either. Every site is evaluated on its own evidence, with no bias from previous approvals of a similar nature.

## The prompt defines what the AI may not do

In Mohit's framing, the prompt is a controlled operating instruction. It authorises the model to identify applicable rules, extract facts, expose uncertainty and draft for review. It forbids non-existent citations, unverified site conditions and claims that an approval was granted. Observed facts, inferred facts, open questions and applicable rules stay in separate sections, and a second verification prompt checks that each citation supports the conclusion drawn from it.

The output schema follows the same logic: the action under review, the controlling authority, observed facts with citations, missing evidence, next steps for the environmental specialist, and a status from a fixed set (cleared, conditionally cleared, pending review, not approved). Conflicting engineering drawings or disputed historic effects trigger escalation.

## Retrieval: filter first, never average conflicts

Before any search, filter by jurisdiction, agency, document status and effective date. Use hybrid semantic and keyword search to catch definitions and exceptions, and chunk clauses with their headings, definitions and neighbours so an exception travels with its rule. Conflicts get flagged, never averaged.

On the vision and spatial side, a buffer or overlap is a screening signal, not an effects determination, and every machine-derived feature gets a confidence or review status. Retrieved web content is treated as untrusted and tested for prompt injection.

## Success is a reviewable record

The workflow has three human-supervised steps (intake validation, rules retrieval, a dossier of site conditions), with a rules engine handling measurable conditions and the language model explaining and drafting around them. A designated approval is required before any external submission. Mohit's measure of success is a reviewable decision record that helps experts find evidence and see what remains uncertain, not a verdict that a project is compliant.

## Who should watch

Engineers building LLM features for regulated, evidence-heavy decisions: permitting, legal review, audits. The delivery is dense and slide-driven rather than a code walkthrough, so treat it as a design checklist. Mohit is clear that each new domain still needs fresh legal mapping and evaluation.

## Related Conf42 talks

- [Designing for Defensibility: Evidence-Centric Compliance Architecture in Customer-Facing Financial Platforms](https://www.conf42.com/Golang_2026_Manasa_Uppula_designing_defensibility_evidence) by Manasa Uppula of Virtusa at Conf42 Golang 2026.
- [An Advanced Validation Pipeline for Summary Evaluation in High-Stakes Environments](https://www.conf42.com/Large_Language_Models_LLMs_2026_Liliya_Imasheva_Michael_Banf_validation_summaries_evaluation) by Liliya Imasheva and Michael Banf of Perelyn at Conf42 Large Language Models 2026.
- [Stop AI Agents from Making Up Facts: Graph-RAG for Reliable Data Retrieval](https://www.conf42.com/MLOps_2026_Elizabeth_Fuentes_Leone_graph_rag_retrieval) by Elizabeth Fuentes Leone of AWS at Conf42 MLOps 2026.

[Watch Mohit Upadhyay's talk](https://www.conf42.com/Prompt_Engineering_2026_Mohit_Upadhyay_nepa_compliance_automation) from [Conf42 Prompt Engineering 2026](https://www.conf42.com/prompt2026).

[Watch the talk on YouTube](https://youtu.be/kRY4wobAIz0).

## Watch the talk

[Prompt Engineering for AI-Powered NEPA Compliance Automation](https://www.conf42.com/Prompt_Engineering_2026_Mohit_Upadhyay_nepa_compliance_automation) at Conf42 Prompt Engineering 2026.
