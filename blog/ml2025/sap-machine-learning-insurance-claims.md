# SAP plus machine learning in insurance starts with the data migration

Conf42 Blog, 2025-05-06, updated 2026-11-09. https://www.conf42.com/blog/ml2025/sap-machine-learning-insurance-claims

In short: Satish Puram of Deloitte at Conf42 Machine Learning 2025 on pairing SAP S/4HANA with ML for insurance claims and underwriting, and why migration decides it.

Insurance runs on claims, policies and very old systems. At Conf42 Machine Learning 2025, Satish Puram, a Specialist Leader at Deloitte Consulting with 22 years of SAP implementations behind him, laid out how insurers combine SAP S/4HANA with machine learning for claims, underwriting and customer service, and why the unglamorous parts (data migration, integration, leadership) decide whether any of it works.

It is a leadership-perspective talk from a consultant who has done this many times. Expect frameworks and SAP module names, not model architectures.

## Why insurers are under pressure

Puram names four forces. Digital-first insurtech competitors move faster with lighter operations. Legacy infrastructure creates data silos and drives up operating cost. Cyberattacks against policyholder data keep getting more sophisticated. And customers now expect the same frictionless, personalized service they get everywhere else, which is a high bar for a claims process designed around paper.

His answer is the SAP stack, and he is upfront about it: S/4HANA as the real-time data and analytics foundation, SAP Insurance Analyzer for risk analysis and insurance-specific regulatory needs, a data management suite for integration and governance, and SAP CRM for the policyholder side. The headline numbers on his slides (processing-time cuts, efficiency gains, a return on investment within two years) are framed as industry results for SAP deployments, so treat them as the vendor-ecosystem view rather than one audited project.

## Where the machine learning goes

The ML part is three applications, each familiar to anyone who has worked near an insurer:

- **Claims automation.** Models review claim documents, flag fraud indicators and auto-approve the straightforward cases, which Puram says takes processing from days to minutes for those claims.
- **Dynamic underwriting.** Predictive models build personalized risk profiles and premiums, which also opens coverage to segments that were previously underserved.
- **AI-driven service.** Virtual assistants and sentiment analysis for round-the-clock support and proactive issue spotting.

None of this is exotic. The interesting part is what has to be true underneath for it to run.

## The pyramid, and the migration nobody budgets for

Puram's integration model is a pyramid: business value alignment at the base, then API-first architecture, then a data governance framework, then security by design. Start from the business case and build upward, so integration effort goes where it pays.

Then he says the quiet part: across his whole career, in insurance and every other industry, the biggest challenge has been data migration. His recipe has four steps. Discovery and assessment (audit every source and map it to the target SAP structures). Cleansing and enrichment (kill duplicates, fix quality, add attributes). Testing and validation over multiple cycles with representative samples. And post-migration monitoring, because the job does not end at cutover. If your ML model is trained on the claims history, this is the step that decides whether it learns from signal or from twenty years of duplicate customer records.

## Automation is a loop, and leadership is the hard part

His process automation framework runs from discovery (find candidates, compute ROI per process, align stakeholders) through design (RPA bots, ML models at decision points, SAP integration), phased testing and deployment, into continuous improvement with regular retraining on new data.

The leadership section covers three challenges he deals with daily: managing cross-functional teams of IT, business units and outside consultants; keeping claims and policy operations running during the transition; and building problem-solving frameworks for the technical surprises that always arrive. He closes with a case study of a midsize regional insurer that moved to S/4HANA with ML in phases, starting with claims and policy administration, and reports shorter processing times, lower costs and improved customer satisfaction.

## Who should watch

IT leaders and architects at insurers, and consultants scoping SAP programs, will find a clear map of where ML fits and what to sequence first. ML engineers looking for model detail will not find it here; the talk is about the program around the models.

## Related talks

- [Bhaskara Beeraka on AI applications and technical challenges in insurance](https://www.conf42.com/Cloud_Native_2025_Bhaskara_Beeraka_insurance_innovation_insights) at Conf42 Cloud Native 2025
- [Pravesh Nikhare on rule-based AI for dental insurance claims](https://www.conf42.com/Cloud_Native_2025_Pravesh_Nikhare_insurance_rules_processing) at Conf42 Cloud Native 2025
- [Gurucharann Visagamurthy on real-time underwriting at Kubernetes scale](https://www.conf42.com/Kube_Native_2025_Gurucharann_Visagamurthy_insurance_enrollment_realtime) at Conf42 Kube Native 2025

[Watch Satish Puram's talk](https://www.conf42.com/Machine_Learning_2025_Satish_Puram_insurance_leadership_transformation)

[Watch the talk on YouTube](https://youtu.be/UcznoO89xKk).

## Watch the talk

[Driving Digital Transformation in Insurance with SAP and Machine Learning: A Leadership Perspective](https://www.conf42.com/Machine_Learning_2025_Satish_Puram_insurance_leadership_transformation) at Conf42 Machine Learning 2025.
