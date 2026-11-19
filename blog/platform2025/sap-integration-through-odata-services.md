# Untangling SAP integration with OData services

Conf42 Blog, 2025-08-31, updated 2026-11-09. https://www.conf42.com/blog/platform2025/sap-integration-through-odata-services

In short: Volkswagen's Venkateswaran Petchiappan at Conf42 Platform Engineering 2025 on swapping SAP middleware tangles for tuned RESTful OData APIs.

Every new system you bolt onto SAP makes integration worse at more than a linear rate. Venkateswaran Petchiappan, Senior Solution Architect Lead at Volkswagen, made that the starting point of his Conf42 Platform Engineering 2025 talk, and his way out is to expose SAP data through OData services: standard REST over HTTP, with the platform handling security, monitoring and errors centrally instead of in every point-to-point connector.

If your mental model of SAP integration is a batch job written in a hurry in 2009 and a middleware licence nobody dares to cancel, this talk is a tidy tour of the alternative.

## How SAP integration got here

Venkateswaran walks through the stages. Early SAP integration meant custom programs and batch jobs: fine for basic needs, useless for anything real time. Then came middleware layers and connectors, which needed specialised skills and tended to create silos. OData services shifted things to RESTful, standardised APIs. The last step is a platform-first model where the cross-cutting concerns live at the platform level rather than at each integration point.

The problems he lists will be familiar to anyone who has stared at an SAP interface diagram. Large organisations run five to 15 distinct systems. Middleware dependencies drive up cost. Huge data volumes bottleneck at interface boundaries. Exposing confidential data to cloud apps opens security gaps. And different systems model the same business concept in entirely different ways, so every connection carries its own translation logic. Pile enough of that up and you get the fragile web he calls integration debt.

## Why OData fits SAP

OData extends REST principles to SAP's shape of data. Entity models line up with the SAP application layer, metadata descriptions make services self-documenting, and the usual HTTP verbs (GET, POST, PUT, DELETE) work as expected. Third-party applications can consume the definitions while keeping the business semantics intact. The principle he repeats is connect once, reuse often: one well-defined service instead of a new bespoke interface per consumer. He adds flexible querying and a simpler entity relationship model that can make full use of SAP HANA's in-memory processing.

## Ask for less data

The performance section is the practical core. The techniques are simple and the gains come from using all of them:

- Server-side filtering with `$filter`, so only the rows you need leave SAP.
- Pagination with `$skip` and `$top`, so large result sets arrive in manageable chunks.
- Response compression to cut bandwidth.
- Batch requests that fold multiple operations into one call.
- Field projection with `$select`, returning only the columns you asked for.
- Delta queries that fetch only what changed since the last sync.

With those in place, he says response times can drop to around 700 milliseconds even for complex data scenarios. None of it is exotic; the point is that most slow SAP integrations skip half of these because the connector made it easy to pull everything.

## Results by industry, and the mobile angle

He closes with sector numbers from case studies: 32% fewer parts shortages in manufacturing through real-time supply chain sync, retail inventory accuracy up from 82% to 98.5%, and an 80% drop in integration-related data errors for healthcare providers. He also shows a layered mobile architecture where apps consume SAP data over JSON and HTTP through a security layer, without legacy RFC-based plumbing in the middle.

## Who should watch

Integration architects and platform engineers who own the boundary between SAP and everything else, and developers whose backlog is full of requests for one more field out of SAP. It is an overview of the approach and its tuning knobs rather than a live build, so bring your own OData endpoint to try the query options on.

## Related Conf42 talks

- [Sravan Kumar Nendrambaka (Nike) on the next generation of SAP Cloud ERP with AI](https://www.conf42.com/Cloud_Native_2025_Sravan_Kumar_Nendrambaka_sap_enterprise_optimization), for where S/4HANA itself is heading.
- [Pon Murugesh Devendren (Deloitte) on event-driven AI agents for SAP incident management](https://www.conf42.com/AI_Agents_2026_Pon_Murugesh_Devendren_sap_incidents_events), once the integrations exist and need watching.
- [Vamsi Srivangipuram (DIRECTV) on enterprise application integration for offer management](https://www.conf42.com/Platform_Engineering_2024_Vamsi_Srivangipuram_management_integration_datadriven), a non-SAP take on the same integration debt.

[Watch Venkateswaran Petchiappan's talk](https://www.conf42.com/Platform_Engineering_2025_Venkateswaran_Petchiappan_orchestrating_sap_pipelines)

[Watch the talk on YouTube](https://youtu.be/5uCEZv0sywU).

## Watch the talk

[Platform-First SAP Integration: Orchestrating Enterprise Data Pipelines with Cloud-Native Automation](https://www.conf42.com/Platform_Engineering_2025_Venkateswaran_Petchiappan_orchestrating_sap_pipelines) at Conf42 Platform Engineering 2025.
