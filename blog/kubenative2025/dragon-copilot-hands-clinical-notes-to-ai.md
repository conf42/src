# Dragon Copilot hands the clinical note-taking to ambient AI

Conf42 Blog, 2025-10-06, updated 2026-11-09. https://www.conf42.com/blog/kubenative2025/dragon-copilot-hands-clinical-notes-to-ai

In short: Tharun Nallamothu (Microsoft) at Conf42 Kube Native 2025 on how Dragon Copilot turns doctor-patient conversations into clinical notes with ambient AI.

Doctors finish a visit, then spend the evening on the paperwork, and the next patient gets a tired physician. At Conf42 Kube Native 2025, Tharun Nallamothu, Senior Software Engineer at Microsoft, presented Dragon Copilot, the AI clinical assistant he works on: it records the doctor-patient conversation ambiently, turns it into a structured note, and lets the doctor fix it by voice, so the hours go back to patients.

Honest scope: this is a product talk from an engineer on the team, covering Microsoft's own product, its architecture at a high level and his part in building it. Tharun has spent five to six years in healthcare software across Nuance Communications and Microsoft.

## The problem started before COVID and got worse during it

Tharun tells the origin story plainly. Every visit ends with documentation and prescriptions, which eats time, produces imperfect notes that bring patients back, and burns physicians out. The pandemic made it acute. The goal was to automate the documentation so the doctor's attention stays in the room.

## How it works

The pipeline he describes has four stages:

1. Ambient recording captures the conversation between physician and patient in real time.
2. Natural language understanding extracts the medically relevant information from the spoken conversation.
3. Generative models turn that unstructured input into structured clinical documentation: the note and the transcript, delivered back to the doctor.
4. Voice dictation lets the doctor review and edit the note hands-free when something is wrong or missing.

It also integrates with electronic health record systems, Epic in particular, which is where the note has to end up for the workflow to change at all. Multilingual transcription covers cases where doctor and patient speak different languages.

The figure he quotes on patient experience: 93% of patients said their physician seemed more attentive and personable with Dragon Copilot in the room.

## Healthcare means the security slide is the main slide

The implementation section is where the healthcare constraints show. Voice dictation and ambient recordings are encrypted and stored securely. The platform follows HIPAA, with strict separation so one doctor's patient information never reaches another doctor. Accessibility matters too: Tharun points out the app supports visually impaired users.

The challenges he lists are the ones anyone in clinical AI will recognise: robust multilingual transcription accuracy, secure data migration without loss or breaches, and fitting the whole thing into healthcare compliance and accessibility frameworks.

## What he built

Tharun's own contributions were on the client side and the architecture around it: leading end-to-end features on mobile and web, native mobile work on Apple's Cocoa frameworks, web work in React, Redux and TypeScript, RESTful APIs, and testing against Epic's environment. His point about scale is fair: anything designed at Microsoft has to work for millions of users.

## Who should watch

Engineers building AI features into regulated workflows, and anyone curious how an ambient-AI product is put together end to end. If you want model internals, evaluation methodology or the Kubernetes deployment, the talk doesn't go there; it stays at product and architecture level.

## Related Conf42 talks

- [DevOps Pipelines for Clinical AI](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai) covers deploying real-time sepsis detection, the pipeline side of clinical AI.
- [Evals for Generators: Testing an LLM That Writes Clinical Configuration](https://www.conf42.com/MLOps_2026_Ocean_Coldiron_evals_clinical_configuration) tackles the evaluation question this talk leaves open.
- [From Data to Decision: How Multimodal AI Is Transforming Patient-Centered Healthcare](https://www.conf42.com/Machine_Learning_2025_Hari_Suresh_Babu_Gummadi_healthcare_decision_patient) widens the lens beyond documentation.

[Watch Tharun Nallamothu's talk](https://www.conf42.com/Kube_Native_2025_Tharun_Nallamothu_copilot_clinical_workflows)

[Watch the talk on YouTube](https://youtu.be/DRVcilPzgzQ).

## Watch the talk

[Dragon Copilot: AI-Powered Clinical Assistant Transforming Healthcare Workflows and Patient Care](https://www.conf42.com/Kube_Native_2025_Tharun_Nallamothu_copilot_clinical_workflows) at Conf42 Kube Native 2025.
