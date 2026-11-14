# Healthcare denial letters are a reliability problem, then an AI one

Conf42 Blog, 2026-02-28, updated 2026-11-09. https://www.conf42.com/blog/sre2026/healthcare-letters-are-a-reliability-problem

In short: Prakash Easwaran (ZeOmega) at Conf42 SRE 2026 on automating utilization management letters, then using AI with human review to make denials readable.

"How hard can it be?" is what Prakash Easwaran, Implementation Manager at ZeOmega, says engineers think when they first hear about generating a letter, and his talk at Conf42 Site Reliability Engineering (SRE) 2026 is the answer. In healthcare utilization management, every approval or denial must reach the member as a legally binding letter within tight deadlines, and his team first made that pipeline reliable with automation inside ZeOmega's Jiva platform, then added generative AI to make denials understandable, with a human reviewing every one.

## A letter is a regulatory artifact

Utilization management is how health insurers review and authorize care. Each decision (approved, denied, extended, more information needed) produces a letter governed by CMS, state insurance departments and NCQA standards. Prakash says turnaround windows can be as tight as 24 to 72 hours, and a member may be waiting on that letter to schedule surgery.

The complexity is a matrix: decision types crossed with state rules crossed with plans. The same denial needs different appeal language in New York than in Texas. Before automation, staff picked templates by hand from a library, pasted clinical rationale from other systems, saved PDFs to shared drives and emailed them to print vendors. Nobody could say in real time whether a letter had been generated, sent to fulfillment or mailed. Problems surfaced as complaints or audit flags. Every manual hop was also a place where protected health information could leak.

He cites the regulatory reality that even a small slip, one missing required statement or a one-day delay, can push compliance violations up by 75%. Small process gaps, not outages, were the risk.

## Automate the easy letters first

The rollout was phased over years rather than a big bang: letter configuration in 2023, the denial matrix in 2024, approval letter automation in 2025, and denial, extension and additional-information letters plus the start of AI in 2026.

Approval letters went first because they are structurally simpler. Now a decision in the clinical system triggers generation automatically, the template is chosen by rules, fields are populated programmatically, and the letter goes straight to the printing and fulfillment system. Work that sat in a queue for hours or days happens in seconds or minutes. Every step logs a timestamp (decision, generation, transmission), so when a regulator asks for the audit trail it exists already.

Denials are harder: they must carry the clinical rationale, regulatory citations, appeal rights and state language. The denial matrix is the rules engine that maps decision type, state and plan to the right template and language blocks. Unlike approvals, denials keep a human review step before print dispatch, but the reviewer now checks a correctly assembled letter instead of building one from scratch.

## Then make it readable

A letter can be correct, compliant and on time and still be useless to the person reading it. Members who can't understand a denial don't file the appeals they are entitled to. The AI layer works on top of the compliant letter:

- rewrites dense clinical and legal language into plain English without dropping required content,
- adjusts tone so the letter is respectful rather than bureaucratic,
- explains this member's specific decision instead of a generic statement,
- flags missing or unclear appeal language for the reviewer.

The guardrails are the part SREs should copy. The AI can suggest, enhance and flag, but it cannot publish a letter on its own. Everything it changed is logged with when and why. Templates and rules are versioned as regulations change, and dashboards track turnaround, error rates and review queues. Next on the roadmap: compliance scoring at generation time, predictive risk flags before dispatch, and confirmation of actual delivery.

## Who should watch

Anyone automating documents or workflows in a regulated industry, and teams trying to add an LLM to a process where a wrong answer is a legal problem. The order of work (deterministic automation first, AI on top, human review where impact is highest) is the reusable lesson. It is a domain-heavy talk with no code.

## Related Conf42 talks

- [SRE and Healthcare Data Compliance: Balancing Security and Reliability](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Sidhartha_Velishala_sre_healthcare_data) by Sidhartha Velishala (Humana).
- [GenAI in Healthcare Claims: Accelerating Processing and Detecting Fraud](https://www.conf42.com/Kube_Native_2025_Amala_Umakanth_genai_healthcare_fraud) by Amala Umakanth (McKinsey & Company).
- [Prompt Engineering Healthcare Compliance](https://www.conf42.com/Prompt_Engineering_2025_Bandanawaz_Mulla_healthcare_cloud_solutions) by Bandanawaz Mulla (Health Care Service Corporation), on automating benefits configuration.

[Watch Prakash Easwaran's talk](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Prakash_Easwaran_reliable_driven_letters)

[Watch the talk on YouTube](https://youtu.be/xVvwaJHLB0g).

## Watch the talk

[Reliable AI-Driven UM Letters: Automating Compliance in Healthcare Systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2026_Prakash_Easwaran_reliable_driven_letters) at Conf42 Site Reliability Engineering (SRE) 2026.
