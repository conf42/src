# Platform thinking is how digital transformation actually ships

Conf42 Blog, 2025-09-04, updated 2026-11-09. https://www.conf42.com/blog/platform2025/platform-engineering-digital-transformation-invoices

In short: Manik and Prachita Kashikar at Conf42 Platform Engineering 2025 map platform engineering onto a paper-heavy medical invoicing workflow, layer by layer.

Most digital transformation programmes stall because every team rebuilds the same plumbing. At Conf42 Platform Engineering 2025, Manik Kashikar, Principal Consultant at Thoughtworks, and co-presenter Prachita Kashikar argued that platform engineering is the missing operating model, then showed it on a concrete case: medical invoice processing that ran on paper, stamps and manual forwarding.

This is a framing talk with one worked example, not a tooling demo. Its value is the vocabulary: if you have ever had to explain to a business sponsor why building a platform belongs on the transformation roadmap, it gives you the slides in your head.

## A platform is town planning, not a pile of tools

Manik's definition is simple: a platform is a reusable digital foundation that hides complexity, standardises how teams operate and speeds up new work. His analogy: "Think of it like town planning." You lay roads, utilities and rules first, so the houses that follow do not each need their own sewer.

He splits platform strategy into four kinds, each framed "as a service":

- **Engineering platform:** IT as a service for developers. Self-service infrastructure, pipelines and monitoring, so engineers stop doing plumbing.
- **Business capabilities platform:** reusable business services, so new products assemble from parts instead of fresh fragmented builds.
- **Data platform:** data as products, discoverable and governed, so teams subscribe to datasets instead of hunting for them.
- **Customer experience platform:** one profile and consistent personalisation across web, app and partner channels.

The point is that they stack. Delivery infrastructure, API and service boundaries, self-service data, experimentation with feature toggles and telemetry, and customer touch points each become shared capabilities rather than per-team projects.

## Digitisation, digitalisation, transformation

The talk also untangles three words that get used interchangeably. Digitisation converts analogue to digital, like scanning paper. Digitalisation automates the workflows you already have. Digital transformation reimagines how the business creates value with technology at the core. Manik's argument is that a system-centric approach, with siloed apps and brittle integrations, gets you stuck at step two.

## The invoice pipeline, rebuilt as layers

Prachita then takes the healthcare use case. The starting point: a medical invoicing operation handling over a million documents a week, where every invoice needed physical verification of signatures and stamps and manual forwarding to claims teams. The pains are the familiar ones: data entry errors, fraud exposure, no real-time visibility for stakeholders, and a system that only scaled by hiring.

The redesigned flow runs through a web portal: invoices are uploaded in batches, sanity-checked and stored in the cloud, scanned with OCR and NLP to extract fields, and passed through deep learning to pull out signatures and stamps. A government representative still audits those signatures by hand, a deliberate human-in-the-loop step against fraud. Then the insurer approves, rejects or puts the claim on hold, and approvals trigger the payment workflow.

The platform view is the interesting part. The same flow is redrawn as layers: a shared ingestion layer for hospitals, insurers and government bodies; reusable data services (the OCR and NLP engines serve claims, compliance and audit alike); validation as a service, with AI models plus human review; an orchestrated claims processing platform; and an experience layer of chatbots and real-time dashboards. Their summary line is the one to steal for your next architecture review: instead of scaling people linearly, scale capabilities.

## Measuring it in three columns

They close with success metrics split three ways: customer metrics, business value (fraud reduction, compliance by design, lower cost to serve) and operational metrics (uptime, accuracy, fraud detection rate, throughput). Success, in their framing, is when all three move together. The roadmap is phased: value stream mapping and an e-invoicing platform first, then OCR, NLP and fraud detection, then cross-stakeholder automation, dashboards and wider rollout.

## Who should watch

Architects and platform leads who have to sell platform work to business stakeholders, and anyone in regulated, paper-heavy domains like insurance and healthcare. If you want Backstage plugins or Terraform modules, this is the wrong half hour; it stays at the operating-model level.

## Related Conf42 talks

- [Zach Gardner on why digital transformations fail and how to succeed](https://www.conf42.com/Cloud_Native_2023_Zach_Gardner_digital_transformation_fails__how_to_succeed) at Conf42 Cloud Native 2023.
- [Vasipally Nagireddy on driving digital transformation for e-governance](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Vasipally_Nagireddy_driving_digital_transformation) at Conf42 SRE 2025.

[Watch Manik and Prachita Kashikar's talk](https://www.conf42.com/Platform_Engineering_2025_Manik_Kashikar_Prachita_Kashikar_gap_bridging_digital), part of [Conf42 Platform Engineering 2025](https://www.conf42.com/platform2025).

[Watch the talk on YouTube](https://youtu.be/QiqItGyy_iw).

## Watch the talk

[Platform Engineering and Digital Transformation: Bridging the Gap](https://www.conf42.com/Platform_Engineering_2025_Manik_Kashikar_Prachita_Kashikar_gap_bridging_digital) at Conf42 Platform Engineering 2025.
