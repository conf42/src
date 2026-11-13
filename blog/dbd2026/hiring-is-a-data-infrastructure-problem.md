# Your hiring problem is a data infrastructure problem

Conf42 Blog, 2026-05-27, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/hiring-is-a-data-infrastructure-problem

In short: Zeeshan Khan (STV) at Conf42 Database DevOps 2026 on five layers from a legacy ATS to predictive hiring, with skills graphs, vector search and governance.

Every resume, interview note and candidate email is data, and in most companies it sits in a system built for compliance paperwork. At Conf42 Database DevOps 2026, Zeeshan Khan, HRIS Manager at STV, argues that organisations which think they have a hiring problem usually have an infrastructure problem, and lays out five layers that take recruiting from an applicant tracking system (ATS) to a predictive, self-improving pipeline.

It's an architecture-and-strategy talk from the HR technology side. Expect concepts and examples rather than schemas or code.

## The ATS was never meant to be smart

Zeeshan's starting point: traditional ATS platforms were built for compliance and administrative workflow, not intelligence. Sourcing, resume parsing, interviews and compliance training each store data in a different place, and those stores rarely talk to each other. There are dashboards and reports, but no real-time insight and no prediction. Buying a newer ATS doesn't fix it, he says, because the missing piece is the data foundation, not the product.

## Five layers, each built on the last

His maturity model runs from the basics to what he calls the north star:

1. **Administrative.** The core ATS: job posts, interviews, hires.
2. **Data enrichment.** HRIS, ATS and CRM connected so the process lives in one place. Still descriptive, not predictive.
3. **NLP and embeddings.** Systems that understand the intent of a job description or a resume instead of filtering on keywords.
4. **Skills graphs and vector search.** Skills attached to jobs, employees, tasks and learning, so search works on meaning.
5. **Predictive hiring,** ending in a self-optimising ecosystem where every decision feeds the next.

## Search by meaning, not by filter

The vector search examples are the most concrete part. A keyword filter for Python, New York and a product manager title returns exactly what you typed. A query describing someone with ownership of a product from design through implementation to output surfaces people whose experience matches, even if their titles don't. His other example: an electrician can be matched to a technician role on shared skills and certifications that a title search would never connect.

The catch is the one every data engineer expects. It only works with good data, proper indexing and properly categorised records. In his words, garbage in, garbage out is real.

## From a won contract to a requisition

The predictive layer is easiest to picture through his workforce planning scenario. A company wins a project starting in six months. An agent reads the project's tasks, checks which skills exist in the organisation and who is available, finds the gap, searches internal employees for mobility candidates, then the existing candidate pool, and only then opens a new requisition. Event-driven architecture keeps it current: instead of batch jobs, signals such as a high-priority candidate losing interest trigger a notification with the reason, so recruiters can act before the offer is lost.

Skills graphs also feed internal mobility and retention. Tailored learning paths for every employee in a company of a hundred thousand are impossible by hand, he notes, but realistic when the infrastructure holds the skills data.

## Governance is not optional here

Hiring is a high-stakes automated decision area, and the abstract notes that algorithmic screening tools face active regulatory scrutiny and litigation. Zeeshan's governance list: bias detection, explainability (the system must say why it recommended a candidate, with the evidence), model auditing for accuracy and compliance, and human oversight. He is emphatic that AI supports recruiters and does not replace them. His closing line: the future of hiring is infrastructure plus judgment.

## Who should watch

HRIS and people-analytics engineers planning what to build after the ATS, and data engineers asked to support a recruiting team's AI ambitions. If you want vector database internals, pick one of the talks below.

## Related Conf42 talks

- [MLOps at Scale: Production-Ready AI Systems for HR Transformation in Enterprise Shared Service Centers](https://www.conf42.com/MLOps_2025_Ramprasad_Reddy_Mittana_mlops_scale_production) by Ramprasad Reddy Mittana, running HR AI in production.
- [A gentle introduction to Vector Databases](https://www.conf42.com/Machine_Learning_2023_Zain_Hasan_vector_databases) by Zain Hasan, the mechanics behind meaning-based search.
- [Leveraging Global HCM Systems for HR Digital Transformation: A Strategic Implementation Approach](https://www.conf42.com/Machine_Learning_2025_Swetha_Priya_Sathiyam_hcm_transformation_implementation) by Swetha Priya Sathiyam, the HCM foundation those layers sit on.

[Watch Zeeshan Khan's talk](https://www.conf42.com/Database_DevOps_2026_Zeeshan_Khan_vectors_recruiting_semantic)

[Watch the talk on YouTube](https://youtu.be/YVJhvYuyBFs).

## Watch the talk

[AI in Hiring: How Data Infrastructure Powers Smarter Talent Decisions](https://www.conf42.com/Database_DevOps_2026_Zeeshan_Khan_vectors_recruiting_semantic) at Conf42 Database DevOps 2026.
