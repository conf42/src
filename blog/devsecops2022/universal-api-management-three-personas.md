# API sprawl needs one control plane, whatever the APIs run on

Conf42 Blog, 2022-12-01. https://www.conf42.com/blog/devsecops2022/universal-api-management-three-personas

In short: Akshata Sawant (MuleSoft) at Conf42 DevSecOps 2022 on sustainable API management - design-time governance, policies and Flex Gateway for APIs on any cloud

APIs multiply faster than anyone can catalogue them, and the ones nobody can see are the ones nobody secures. Akshata Sawant, Developer Advocate at [MuleSoft](https://www.mulesoft.com/), used her Conf42 DevSecOps 2022 talk to describe what she calls sustainable API management: one place to design, govern, secure and publish APIs regardless of the technology they are built in or the cloud they run on, shown through MuleSoft's Universal API Management on Anypoint Platform.

Be clear about what this is: a product walkthrough, organised around three personas. The useful part for a non-customer is the shape of the workflow, especially governance checks that run while the API is still being designed.

## What problem does API proliferation create?

Sawant names three. Limited visibility, because there is no central management pane across ecosystems, clouds and environments. Inconsistency, because governance and security rules cannot be applied uniformly to APIs that live in silos. Slow troubleshooting, because when something changes or breaks, finding and debugging the right API takes longer. Her example of the goal: a Mule API on AWS and a Microsoft API on Azure, managed under one roof.

## The API developer: design first, governed early

The first persona, an API developer whose organisation insists on design-first, works like this:

- **Design** in Anypoint Design Center, as a REST API in RAML or OAS or as an async API, from scratch, from an import, or through a guided mode that writes the spec from a few answers (name, protocols, media type, base URI, endpoints such as get and post orders).
- **Mock** the endpoints straight from the spec, to see the responses consumers will get before any implementation exists.
- **Govern at design time** with rule sets. In the demo, a security best-practice rule set flags the spec as it is written, and calling the mock without basic auth returns a bad request.
- **Publish** to Anypoint Exchange, the catalogue with versions and lifecycle stage, which also holds MuleSoft's templates and examples.
- **Implement** in Anypoint Studio (built on Eclipse) by scaffolding from the spec and dragging in connectors, Salesforce in her example, rather than writing integration code by hand.

"I'm not waiting for it till the end or I'm actually saving lot more iterations as well," Akshata Sawant said at Conf42 DevSecOps 2022, on why the checks run in the design stage.

## The API owner: policies, gateways, alerts

The second persona owns operations and security. Here she shows:

- **API Governance profiles** that apply rule sets (Anypoint best practices, security best practices) to APIs selected by tag, mark each one conformant or not, and email the API contact when one drifts. She compares it to SonarQube for API specs.
- **API Manager policies** applied without code changes: basic authentication, IP allow and block lists, JSON threat protection, JWT validation, CORS, plus quality of service, transformation and message logging policies for troubleshooting a deployed API.
- **Alerts** on response times, timeouts and policy violations, and **SLA tiers** grouped into contracts.
- **Runtime Manager** for deployment state and logs, and **Anypoint Flex Gateway**, a lightweight gateway you install on the operating system or environment of your choice to manage Mule and non-Mule APIs wherever they are deployed.

## The API product manager: getting APIs reused

The third persona's job is adoption. Her line is that an API reused by a different team without hiccups is rare, so the documentation, versions and access have to live in one place. Exchange serves as the shared catalogue for technical and non-technical readers, with sharing to internal or external collaborators; API Experience Hub and API Community Manager give a more customised developer portal for wider communities.

## What makes it sustainable?

In her summary: APIs on any technology and any cloud, managed under one roof, which gives consistency, security and reliability, and makes APIs easier to share and adopt. Strip the branding and the takeaways travel: lint specs against security rules before implementation, keep policies out of application code, and treat discoverability as part of the API's lifecycle rather than an afterthought.

## Who should watch

Teams already on MuleSoft or evaluating it, and platform teams designing their own API governance who want to see a complete design-to-portal flow in one sitting. Expect demos rather than architecture debate.

## Related Conf42 talks

- Pubudu Gunatilaka on [API governance and API management on Kubernetes](https://www.conf42.com/Kube_Native_2024_Pubudu_Gunatilaka_api_governance_kubernetes_api_management) at Conf42 Kube Native 2024.
- Navendu Pottekkat on [SRE best practices for API design](https://www.conf42.com/Site_Reliability_Engineering_2022_Navendu_Pottekkat_sre_best_practices_api_design) at Conf42 SRE 2022.
- Arlemi Turpault on [API-first](https://www.conf42.com/Chaos_Engineering_2022_Arlemi_Turpault_how_to_win_friends_and_influence_people_with_api_first) at Conf42 Chaos Engineering 2022.

[Watch Akshata Sawant's talk](https://www.conf42.com/DevSecOps_2022_Akshata_Sawant_sustainable_api_management)

## From MuleSoft

MuleSoft's Anypoint Platform covers integration and API management, from design and implementation to gateways, governance and developer portals.

- [MuleSoft website](https://www.mulesoft.com/)
- [Discover Anypoint Platform](https://videos.mulesoft.com/watch/bakFGgwqNDJzoJFNydiMiH)
- [Join the MuleSoft Community](https://www.mulesoft.com/community)
- [Try Anypoint Platform](https://anypoint.mulesoft.com/login)

[Watch the talk on YouTube](https://youtu.be/ek-xNIdhbn0).

## Watch the talk

[Sustainable API Management](https://www.conf42.com/DevSecOps_2022_Akshata_Sawant_sustainable_api_management) at Conf42 DevSecOps 2022.
