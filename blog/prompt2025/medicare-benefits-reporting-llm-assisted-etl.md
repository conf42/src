# LLM-assisted ETL for a Medicare benefits mandate, 102 benefit types

Conf42 Blog, 2025-11-01, updated 2026-11-09. https://www.conf42.com/blog/prompt2025/medicare-benefits-reporting-llm-assisted-etl

In short: Bandanawaz Mulla of Health Care Service Corporation at Conf42 Prompt Engineering 2025 on using prompts to build CMS supplemental benefit reporting on AWS.

Regulators set deadlines, not data models. At Conf42 Prompt Engineering 2025, Bandanawaz Mulla, Senior Manager of Platform Strategy at Health Care Service Corporation, described how his team used LLMs across the development lifecycle to meet a CMS mandate on Medicare Advantage supplemental benefits: 102 benefit types, more than ten source systems and over two million members.

The interesting part is where prompts were used. This is AI-assisted engineering of a compliance pipeline, not an AI product facing members.

## The mandate and the mess

The CMS requirement, due in December 2024, asked Medicare organisations to reach members who are entitled to supplemental benefits but have not used them, and tell them what is available and for how long. Doing that means knowing, per member, which of the benefits apply and what has been used.

The data problem Bandanawaz lays out: 102 supplemental benefits, each with its own structure; more than ten vendor source systems, some overlapping in what they cover; and two million plus members across medical and pharmacy (PDP) plans. Before anyone writes outreach, someone has to integrate and standardise all of it.

## Where the prompts went

The abstract lists the uses most clearly, and the talk follows it:

- Prototyping ETL logic for complex healthcare data transformations.
- Generating SQL for the dimensional model of a health event data mart.
- Creating test scenarios for edge cases in benefit utilisation patterns.
- Translating HIPAA and federal regulatory language into technical specifications, and generating audit logging frameworks.

The stack underneath is plain AWS: EC2 and Lambda for processing, S3 as the data lake for raw and processed data, and RDS for structured benefit and member data.

## Results, as reported

Bandanawaz reports 100% on-time federal reporting and a 40% reduction in development time from the prompt engineering approach. The longer-term payoff he describes is a single source of truth for benefits data, which removed redundant processing and now feeds member communication triggers for unused benefits and reusable components for future mandates.

## Lessons for regulated shops

His takeaways are the reason to watch if you work under HIPAA or similar rules:

- Prompts that combine domain knowledge with precise technical specifications produced more usable code than generic requests.
- AI-generated code needed repeated refinement to meet security and HIPAA standards; the first output was a draft, never the deliverable.
- LLMs helped bridge clinical, technical and business stakeholders by translating between their vocabularies.
- Put regulation and precise legal and clinical terminology into the prompt, demand audit trails, validate output against frameworks such as NIST and ISO, and refine prompts with clinical and legal experts.

He also maps AI help onto phases: discovery (analysing existing systems for integration points and hidden dependencies), design (generating architecture options), implementation (prototyping ETL pipelines), testing (edge-case scenarios) and documentation (technical and compliance reports).

Fair warning: the delivery leans on superlatives, and the talk stays at the strategy level, without showing a prompt or a schema. Read the abstract alongside it for the concrete list.

## Who should watch

Data engineering leads and architects in healthcare payers, or any regulated organisation facing a reporting mandate on a tight deadline, who want to know where LLM assistance helped and where humans still had to check every line.

## Related Conf42 talks

- [Nisheedh Raveendran on regulatory incidents in HIPAA, GDPR and DMA environments](https://www.conf42.com/Incident_Management_2025_Nisheedh_Raveendran_compliance_hipaa_gdpr) at Conf42 Incident Management 2025.
- [Venugopal Reddy Depa on API-led healthcare interoperability](https://www.conf42.com/Cloud_Native_2025_Venugopal_Reddy_Depa_api_healthcare_interoperability), the integration side of healthcare data.
- [Vijaya Kumar Guntumadugu on AI for banking anti-money-laundering compliance](https://www.conf42.com/Large_Language_Models_LLMs_2025_Vijaya_Kumar_Guntumadugu_banking_compliance_money), the same compliance pressure in finance.

[Watch Bandanawaz Mulla's talk](https://www.conf42.com/Prompt_Engineering_2025_Bandanawaz_Mulla_healthcare_cloud_solutions), part of [Conf42 Prompt Engineering 2025](https://www.conf42.com/prompt2025).

[Watch the talk on YouTube](https://youtu.be/6GAzUPlgjM0).

## Watch the talk

[Prompt Engineering Healthcare Compliance: Automating 102 Benefits for 2M+ Members](https://www.conf42.com/Prompt_Engineering_2025_Bandanawaz_Mulla_healthcare_cloud_solutions) at Conf42 Prompt Engineering 2025.
