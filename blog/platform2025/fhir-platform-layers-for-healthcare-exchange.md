# Healthcare Interoperability Is a Platform Problem, Built in Layers

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/fhir-platform-layers-for-healthcare-exchange

In short: Gunjan Desai Rajendrakumar (UT Austin) at Conf42 Platform Engineering 2025 on a layered, FHIR-first platform for healthcare data exchange.

A patient arrives in the emergency room and nobody can see their allergies. At Conf42 Platform Engineering 2025, Gunjan Desai Rajendrakumar of The University of Texas at Austin argued that this is a platform engineering problem: point-to-point integrations between hospital systems don't scale, and the fix is a layered exchange platform that speaks FHIR at the edge and keeps every concern in its own lane.

It's a short, architecture-level talk, closer to a reference design than a war story, and that's what makes it useful as a map.

## Point-to-point integration is the thing that breaks

The opening framing is blunt. Healthcare data lives in legacy EHRs, lab systems, imaging systems and personal apps, in formats ranging from HL7 FHIR to custom schemas. Wiring each system to every other one works for a clinic and collapses for a regional network. The cost of that collapse shows up as duplicate tests and doctors deciding without the history in front of them.

So the talk treats interoperability the way a platform team treats any shared capability: build it once, expose it through a contract, and let applications rely on the contract instead of the plumbing.

## Four layers, four jobs

The architecture splits into layers that each own one problem:

- **Ingestion** connects to the diverse source systems through standardized connectors.
- **Transformation** normalizes formats, and this is where AI earns its place: machine learning and NLP speed up schema mapping, which is traditionally slow manual work, and turn free-text clinical notes into something searchable.
- **Orchestration** validates business rules, checks consent and resolves conflicts.
- **Application interface** exposes FHIR-compliant APIs that apps can build on, including SMART-on-FHIR patient apps.

The point of the separation is that a specialist, a family doctor and an ER physician end up reading the same record instead of three partial copies. Underneath sit the usual cloud-native tools: microservices on Kubernetes, serverless for spiky workloads, and infrastructure as code for consistency and compliance.

## Security is role-shaped, because care is role-shaped

The security section is the most healthcare-specific part. Access is fine-grained and role-based because an emergency physician may need broad access while a specialist needs only the relevant slice. Data is encrypted end to end with automated key rotation, and audit logging records every read and write so compliance reports don't require a human to assemble them. Gunjan frames the whole thing as trust between providers and with patients, which is a nicer way of saying the auditors will ask.

## Run it like any other production platform

The back half applies familiar operations practice to a domain that often lags on it. Monitoring tracks API response times and transformation throughput; data-flow monitoring follows messages through the pipeline with processing and success rates; anomaly detection flags bad data. Automated deployment pipelines with rollback replace manual releases, which the talk calls error prone for integration systems this tangled. Performance work covers parallel processing, caching repeated lookups, database partitioning and auto-scaling.

The case studies are described in outline rather than numbers: a regional health information exchange giving ER doctors patient histories in minutes, hospital consolidations migrating gradually without disrupting care, and patient-facing apps built on FHIR APIs. Looking ahead, Gunjan points to blockchain for tamper-proof audit trails and patient-controlled sharing, and to LLMs for clinical documentation, while noting that performance and compliance questions remain open.

## Who should watch

Engineers new to healthcare who need the vocabulary and the shape of an exchange platform in one sitting: the layers, where FHIR sits, and why consent and audit are first-class. If you already run an HIE, this will be familiar ground. If you build integration platforms in any regulated domain, the layering transfers well beyond hospitals.

## Related Conf42 talks

- [Venugopal Reddy Depa on API-led healthcare transformation and interoperability](https://www.conf42.com/Cloud_Native_2025_Venugopal_Reddy_Depa_api_healthcare_interoperability) at Conf42 Cloud Native 2025.
- [Santhosh Kumar Rai on cloud-native data engineering for precision medicine](https://www.conf42.com/Cloud_Native_2025_Santhosh_Kumar_Rai_data_engineering_healthcare_precision), the analytics side of the same data.

[Watch Gunjan Desai Rajendrakumar's talk](https://www.conf42.com/Platform_Engineering_2025_Gunjan_Desai_Rajendrakumar_interoperability_exchange_fhir)

[Watch the talk on YouTube](https://youtu.be/3QbNa-bC8Aw).

## Watch the talk

[Platform Engineering for Healthcare Interoperability: Building Scalable Data Exchange Systems with AI-Enhanced FHIR](https://www.conf42.com/Platform_Engineering_2025_Gunjan_Desai_Rajendrakumar_interoperability_exchange_fhir) at Conf42 Platform Engineering 2025.
