# Low-code ships fast; public code and governance keep it honest

Conf42 Blog, 2025-08-19, updated 2026-11-09. https://www.conf42.com/blog/mlops2025/low-code-needs-public-code-and-governance

In short: Anoosha Cherukuri (State of Tennessee) at Conf42 MLOps 2025 on pairing low-code delivery with open, auditable public code and real engineering standards.

Low-code gets you speed, public code gets you trust, and you need both if the software belongs to citizens. That is the argument Anoosha Cherukuri, a senior software developer with the State of Tennessee, makes at Conf42 MLOps 2025: let business experts build the user-facing layer visually, keep the core logic open and auditable, and treat every drag-and-drop artifact like source code.

It is a short, structured talk, closer to an architecture primer than a war story. If you have ever inherited a pile of unversioned workflows built by someone who left, the premise will feel personal.

## The bottleneck is people, not tools

Anoosha opens with the pressure every government IT shop knows. Citizens expect public services to behave like the apps on their phone, regulators want transparency, executives want a return on every technology dollar, and there are not enough skilled developers to go around. She cites an IDC forecast of a global shortage of 4 million developers and the familiar Standish Group finding that a large share of software projects arrive late, over budget or not at all.

Her answer splits the problem in two. Low-code addresses speed and access: visual builders, prebuilt connectors to databases, APIs and authentication, and prototypes in days. Public code addresses trust and sustainability: software built in the open, documented so it can be audited, and reusable so the next agency does not pay for the same thing twice. Her example of public code done at national scale is Estonia, which runs nearly all government services on open standards.

## Put the forms in low-code and the rules in the open

The most useful section is the set of architecture patterns for making the two coexist. In a hybrid workflow, the user-facing layer lives in the low-code platform while business logic sits in public code. A customer-support chatbot might be assembled visually, but its escalation logic is coded and published.

API-first design keeps that split clean: forms call reusable APIs instead of writing straight into a database, so the same rule serves the portal, the back office and whatever comes next. Event-driven pipelines give you audit trails as a side effect, because every request is an event someone can trace later.

## A drag-and-drop workflow is still code

Anoosha's governance list is where the talk earns its place at an MLOps event. Every low-code artifact goes into version control. Workflows stored in Git get tested in CI with Jenkins, GitHub Actions or Azure DevOps, the same as anything else. Security is designed in through role-based access, encryption and audit trails, and dev, test and production must be identical, or the designer preview becomes the new works-on-my-machine.

She is candid about how this goes wrong. Low-code platforms can buckle under millions of transactions a day. Proprietary tools turn into cages. Citizen developers produce workflows nobody monitors. Her cautionary tale is a global insurer that adopted low-code widely and, a year later, had hundreds of apps with no central governance and months of auditing ahead of it.

## Who should watch

Platform and DevOps engineers in the public sector, healthcare or any regulated shop being asked to enable citizen developers without losing control of the estate. It is also a decent briefing for architects who need language to explain to leadership why low-code still needs pipelines. If you want deep ML content, this one is about the delivery plumbing around it, not models.

## Related Conf42 talks

- [Balaji Bodicherla (T-Mobile) on low-code/no-code platforms for faster delivery](https://www.conf42.com/Machine_Learning_2025_Balaji_Bodicherla_development_transformation_platforms) at Conf42 Machine Learning 2025.
- [Sanjiv Kumar Bhagat on building trust in AI-enhanced public sector systems](https://www.conf42.com/Machine_Learning_2025_Sanjiv_Kumar_Bhagat_algorithms_trust_sector), the trust half of the same problem.
- [Anirudh Peri on public sector operations with Salesforce Government Cloud](https://www.conf42.com/Golang_2025_Anirudh_Peri_salesforce_cloud_government) at Conf42 Golang 2025.

[Watch Anoosha Cherukuri's talk](https://www.conf42.com/MLOps_2025_Anoosha_Cherukuri_low_code_meets) for the full set of patterns and her take on AI-assisted low-code for digital government.

[Watch the talk on YouTube](https://youtu.be/1olXcU-PWIQ).

## Watch the talk

[Low-Code Meets Public Code: Automating with Minimal Engineering](https://www.conf42.com/MLOps_2025_Anoosha_Cherukuri_low_code_meets) at Conf42 MLOps 2025.
