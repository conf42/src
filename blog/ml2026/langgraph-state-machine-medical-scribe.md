# A medical scribe as a LangGraph state machine, not one big prompt

Conf42 Blog, 2026-01-20, updated 2026-11-09. https://www.conf42.com/blog/ml2026/langgraph-state-machine-medical-scribe

In short: Apple ML engineer Rajeshwari Sah at Conf42 Machine Learning 2026 builds a four-agent LangGraph scribe that turns doctor-patient talk into checked SOAP notes.

One huge prompt that turns a doctor-patient conversation into a clinical note will produce something that looks right. When it isn't, you can't tell which part failed. At [Conf42 Machine Learning 2026](https://www.conf42.com/ml2026), Rajeshwari Sah, a machine learning engineer at Apple, rebuilt the task as a LangGraph state machine with four narrow agents, a typed shared state and a consistency checker, and ran it live on a 7B model on her laptop.

Her definition of "agentic" is pleasantly unromantic: break a complex task into specialised, testable steps, make each step a node that transforms a shared state, and let the graph decide what happens next. The agency lives in workflow design, routing, retries and quality checks.

## Why clinical notes punish shortcuts

The output format is SOAP (Subjective, Objective, Assessment, Plan). The input is a messy human conversation where patients jump topics and a critical fact may appear once. Clinical language adds traps: negation ("denies chest pain"), temporality ("started last week"), uncertainty ("possible viral URI") and context ("family history of diabetes"). Ask one prompt to transcribe, extract, prioritise, format and validate at once and it fails quietly. Her line for the whole design: "plausible but wrong is worse than no output."

She is clear that this is an educational prototype. Real clinical use needs validation, privacy controls and clinician oversight.

## Four agents, one typed state

The pipeline is transcription (Whisper for audio, or text input), information extraction, summarisation into SOAP, and a consistency check. Every node reads and writes a single state object holding the transcript, the extracted encounter, the SOAP note, the consistency report, logs and errors. Nodes behave like pure functions: state in, state out. That makes them unit-testable, replayable and diffable across versions.

Extraction is treated as an API contract. Pydantic models describe symptoms, vitals, diagnoses, medications, tests and follow-ups, combined into a `ClinicalEncounter`. The schema guides the model and validates its output. If validation fails, the node retries once with a stricter prompt; if it fails again, it sets an error and stops cleanly. Nodes never crash the workflow, they record the failure and let the router decide.

## Summarise from facts, then check the facts

Summarisation reads the structured encounter, not the raw transcript, with temperature zero and a no-new-facts rule. The consistency agent then compares the note against the encounter, combining cheap deterministic checks (does the blood pressure in Objective match the extracted value?), semantic checks with an LLM as judge, and safety checks for invented medications or labs. The report flags issues for a clinician or triggers a revision; it never replaces human review.

## The demo, on a laptop

The recorded demo runs the whole graph in Streamlit against Qwen 2.5 7B served locally through Ollama. From a respiratory-infection conversation it extracted six symptoms, three vital signs, one diagnosis and two prescriptions, wrote the SOAP note, and the consistency agent caught that difficulty breathing was missing from the Subjective section. The code is on her GitHub, linked from the slides.

## Measure each agent, not just the note

Evaluation is per node: entity-level precision, recall and F1 by category for extraction; ROUGE-L plus omissions, contradictions and readability for summaries; consistency issues per note over time. She suggests starting with 20 to 50 annotated conversations, simulated if needed. Extensions include a grounding node for ICD-10 and SNOMED codes, and a redaction node before logs are persisted.

## Who should watch

Anyone building multi-step LLM workflows in a regulated domain, healthcare or not. The state-plus-router pattern transfers directly to claims, contracts or support tickets. If you already run LangGraph in production, the evaluation and failure-handling sections are the useful bits.

## Related Conf42 talks

- [DevOps pipelines for clinical AI: deploying real-time sepsis detection](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai), Swapna Chimanchodkar, Conf42 DevOps 2026
- [Reliable AI for clinical handoffs: SRE lessons for safer care transitions](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Abhiram_Potharaju_reliable_clinical_handoffs), Abhiram Potharaju (Wells Fargo), Conf42 SRE 2026
- [Building a production-ready voice AI agent with LangGraph, RAG and evaluation](https://www.conf42.com/MLOps_2026_Arjun_Thakur_voice_langgraph_rag), Arjun Thakur, Conf42 MLOps 2026

[Watch Rajeshwari Sah's talk](https://www.conf42.com/Machine_Learning_2026_Rajeshwari_Sah_labeling_annotation_quality)

[Watch the talk on YouTube](https://youtu.be/JKyT_8Def2c).

## Watch the talk

[Orchestrating Agentic State Machines with LangGraph: Learnings from Automating clinical documentation](https://www.conf42.com/Machine_Learning_2026_Rajeshwari_Sah_labeling_annotation_quality) at Conf42 Machine Learning 2026.
