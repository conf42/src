# AI for clinical handoffs has to fail safely before it helps

Conf42 Blog, 2026-03-13, updated 2026-11-09. https://www.conf42.com/blog/sre2026/ai-clinical-handoffs-need-sre-discipline

In short: Abhiram Potharaju of Wells Fargo at Conf42 SRE 2026 on SBAR-aligned AI handoff summaries built with SRE habits - safe degradation, explainability, governance.

A shift change in a hospital is an on-call handover where the system being handed over is a person. At Conf42 Site Reliability Engineering 2026, Abhiram Potharaju, Senior Software Engineer at Wells Fargo, looked at AI-augmented clinical handoffs through an SRE lens: how to build an assistant that summarises patient data reliably, stays honest about uncertainty, and leaves every clinical decision with the clinician.

It is a design and governance talk rather than a system demo, and it is careful not to oversell: the goal is fewer missed details, not automated medicine.

## Handoffs fail for three boring reasons

Communication breakdowns during handoffs are a known contributor to adverse events, and he narrows the causes to three. Cognitive overload: clinicians juggle many patients under time pressure. Fragmented EHR data: the facts exist but are scattered across notes, labs, vitals and medication lists. Variable quality: even with SBAR (Situation, Background, Assessment, Recommendation) in place, execution differs between clinicians and shifts.

Any SRE who has received a one-line handover note that says all good, watch the queue, will recognise the pattern. His point is that this is a patient safety and reliability problem, not a documentation one.

## Use the format clinicians already trust

The proposed system ingests structured data (vitals, medications, orders, labs) and unstructured notes, and produces a concise summary aligned to SBAR. That alignment is the clever, unglamorous choice: it fits a framework clinicians already use instead of inventing a new one. Situation carries current status and the immediate concern, Background the relevant history, Assessment the meaningful trends, and Recommendation the next steps that need attention.

The abstract adds the monitoring side: continuously watching vital sign trends, medication changes and lab deviations to highlight early signs of deterioration. The aim is to reduce variability and speed up situational awareness, so less time is spent searching records.

## Reliability here means degrading safely

This is where the SRE framing earns its place. In healthcare, being useful is not enough; the assistant has to stay dependable when data is incomplete, inconsistent or late. He lists the familiar toolkit (observability, fault tolerance, incident awareness, proactive maintenance) and adds the healthcare-specific requirements: safe behaviour under uncertainty and safe degradation, so that a gap in the input shows up as a gap in the summary rather than a confident fabrication.

Explainability is treated as a reliability property too. If the system flags a risk, the clinician should be able to see what drove it. That builds appropriate trust and guards against over-reliance, which in this domain is its own failure mode.

## Governance is part of the system, not paperwork around it

The deployment section reads like a production readiness review. Validate carefully before broad rollout, keep monitoring accuracy, reliability and workflow impact afterwards, train staff on how and when to use it, and set clear escalation paths and oversight for when outputs look wrong. He recommends starting with pilot programs on clearly defined use cases, involving clinicians early in workflow design, and measuring outcomes from real workflow behaviour. Adoption, in his framing, is not a one-time event.

## Who should watch

Engineers building AI features for clinical, legal or other high-stakes workflows, and SREs asked to put an LLM summary in front of people who will act on it. It stays at the level of principles, with no metrics or architecture diagrams to copy, so treat it as a framework for your design review rather than a blueprint.

## Related Conf42 talks

- [DevOps Pipelines for Clinical AI: Deploying Real-Time Sepsis Detection at Scale](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai) by Swapna Chimanchodkar.
- [Evals for Generators: Testing an LLM That Writes Clinical Configuration](https://www.conf42.com/MLOps_2026_Ocean_Coldiron_evals_clinical_configuration) by Ocean Coldiron, on proving the output is right before anyone relies on it.
- [Dragon Copilot: AI-Powered Clinical Assistant Transforming Healthcare Workflows and Patient Care](https://www.conf42.com/Kube_Native_2025_Tharun_Nallamothu_copilot_clinical_workflows) by Tharun Nallamothu.

[Watch Abhiram Potharaju's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhiram_Potharaju_reliable_clinical_handoffs) at [Conf42 Site Reliability Engineering 2026](https://www.conf42.com/sre2026).

[Watch the talk on YouTube](https://youtu.be/bvaMsr0AztU).

## Watch the talk

[Reliable AI for Clinical Handoffs: SRE Lessons for Safer Care Transitions](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhiram_Potharaju_reliable_clinical_handoffs) at Conf42 Site Reliability Engineering (SRE) 2026.
