# Low-code platforms can pull clinical research out of paperwork

Conf42 Blog, 2025-08-06, updated 2026-11-09. https://www.conf42.com/blog/platform2025/low-code-clinical-research-platforms

In short: Lalitha Potharalanka of the FDA at Conf42 Platform Engineering 2025 on modular low-code platforms that automate clinical trial data capture and compliance.

In clinical research, the bottleneck is often a spreadsheet, not the science. At Conf42 Platform Engineering 2025, Lalitha Potharalanka, Senior Appian Developer at the US Food and Drug Administration, with 18 years in financial and healthcare IT and a background as a QA automation architect, showed how modular low-code platforms take manual data entry and audit scrambles out of clinical trials, and what it takes to get risk-averse research staff to use them.

## Where the hours go

The numbers she opens with make the problem tangible. Research coordinators spend 60% of their time on documentation and manual data entry. A researcher logs into three to five different systems a day just to do core work. And 25% of clinical trials are delayed by administrative bottlenecks rather than scientific ones. The three root causes are paperwork overload, regulatory complexity across ethics boards, agencies and institutional review boards, and fragmented data systems (EHRs, lab systems, trial management tools) that someone has to reconcile by hand.

## Why low-code fits this problem

Her case for low-code rests on three properties. Rapid prototyping, so a team can test and deploy a new workflow in days rather than months, which matters when regulations or trial protocols change. Customisability, because no two trials are alike and each workflow needs tailoring without a rebuild. And accessibility: clinical coordinators and regulatory leads can help design the workflows they live in, instead of filing requirements and waiting.

## A modular platform, five parts

The architecture is a set of independently deployable components. Data capture takes clinical data from electronic forms, APIs or system input and validates it at entry. An integration engine connects EHRs, lab systems and third-party software into one workflow. Workflow automation handles routing, notifications and approvals. Compliance monitoring is built in, with audit trails generated as a side effect of normal work. An analytics dashboard shows performance and bottlenecks. Because each part stands alone, the platform can adapt to new regulatory or clinical needs without a full overhaul.

## From periodic audits to continuous compliance

The strongest idea in the talk is moving compliance from scheduled audits to a continuous property of the system. Validation rules catch inconsistencies as data is entered, automated cross-checks compare data across systems in the background, every interaction lands in an audit trail, and regulatory reports are generated on demand. In her case study, trial setup that used to take weeks dropped to days, and she reports error rates down 87% and compliance preparation time cut by 65%. Her ROI slide adds administrative time down 42%.

## The human half

Lalitha is clear that technology alone does not shift a clinical organisation. Her adoption playbook: involve researchers, coordinators and regulatory staff early so features match real needs; train people and roll out in phases; design interfaces for mixed technical skill; and run small pilots that create internal champions. To overcome resistance she recommends showing regulators and staff how automation strengthens compliance, documenting outcomes rigorously, and securing an executive sponsor.

Looking forward, she points to AI-driven analytics on trial data, blockchain-backed audit records for multi-site trials, global interoperability, and patient-facing platforms with mobile and wearable reporting and trial matching.

## Who should watch

Engineers building systems in heavily regulated domains, teams weighing low-code against custom builds for internal workflows, and anyone who has watched an audit consume a quarter. It is a platform and process talk, light on code and heavy on how regulated organisations actually change.

## Related Conf42 talks

- [Anoosha Cherukuri on low-code automation with minimal engineering](https://www.conf42.com/MLOps_2025_Anoosha_Cherukuri_low_code_meets) at Conf42 MLOps 2025.
- [Swapna Chimanchodkar on DevOps pipelines for real-time sepsis detection](https://www.conf42.com/DevOps_2026_Swapna_Chimanchodkar_clinical_healthcare_ai) at Conf42 DevOps 2026.

[Watch Lalitha Potharalanka's talk](https://www.conf42.com/Platform_Engineering_2025_Lalitha_Potharalanka_research_clinical_manual), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/zSj5xkYtRSU).

## Watch the talk

[Building Clinical Research Platforms: From Manual Chaos to Automated Excellence](https://www.conf42.com/Platform_Engineering_2025_Lalitha_Potharalanka_research_clinical_manual) at Conf42 Platform Engineering 2025.
