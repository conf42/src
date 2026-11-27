# API-first means your front end can start before your back end

Conf42 Blog, 2022-03-09. https://www.conf42.com/blog/ce2022/api-first-mocks-and-contract-tests

In short: Arlemi Turpault (Postman) at Conf42 Chaos Engineering 2022 on API-first design with OpenAPI specs, mock servers and consumer-driven contract tests

Most team friction over APIs comes from one side waiting on the other. At Conf42 Chaos Engineering 2022, Arlemi Turpault, Senior Developer Advocate at Postman, made the case for API-first design: agree the interface as a specification before writing the back end, and you can generate docs, mocks and tests from it, let teams work in parallel, and catch breaking changes in a pipeline before production does. The chaos engineering link is prevention: find failures before they become outages.

He is upfront about where he works. "This is not a title to hide marketing stuff," Arlemi Turpault said at Conf42 Chaos Engineering 2022, and most of the talk is tool-agnostic, drawn from conversations with Postman's users (17 million at the time).

## What does API-first actually mean?

It depends whom you ask, which is why he starts with Postman's State of the API survey of roughly 28,000 people. In the 2021 edition, 11% were unsure what API-first meant, down 2 points on the year before. The rest split between three readings: designing APIs and schemas before development, building APIs before the apps that integrate with them, and starting from business requirements before any API design. Respondents who called themselves fully API-first mostly chose the first, and that is the definition the talk uses.

## What goes wrong with code-first?

The opposite of API-first is not API-last but code-first: build the core functionality, slap an API on top, then plug in the web app. Then an admin app arrives, then mobile, then a third party, and every layer has to change. He quotes Stephanie Schirmer from Etsy, whose website code had to be rebuilt as an API for the iOS and Android apps, and Ben Christensen of Netflix from 2013 on not letting a single team become the bottleneck.

His list of code-first problems: bottlenecks that delay contributors and consumers, rework late in the cycle, building things nobody wants, thin documentation, and an API constrained by the data model. The API-first benefits mirror them: earlier validation, decoupled dependencies, faster growth, freedom from constraints.

## Which tools make it real?

Three, in order.

**API specifications.** OpenAPI, RAML, GraphQL, AsyncAPI and friends. Postman's data at the time showed OpenAPI v2 with the largest share but declining, OpenAPI v3 growing fastest, and Swagger v1, WADL and RAML barely used. A definition gets linted like code, and teammates can review it before a line of back end exists.

**Mock servers.** Generated from the definition, they are live URLs returning example responses. The front end builds against the mock while the back end is written, testers and writers start on it too, and when the real service is ready you swap the base URL. It works because both sides come from the same definition.

**Consumer-driven contract testing.** The provider publishes a contract; each consumer writes tests describing how they use it; the provider runs every consumer's tests in its pipeline on each change and stops the deploy if one breaks. In his words, "consumer driven contract testing is what stops your app from breaking at the last minute." Inside Postman, each squad keeps a blueprint collection based on its API definition, generates mocks for parallel work, and runs contract tests between squads, so an identity squad's change cannot quietly break everyone who depends on it.

## Is API-first for everyone?

Not quite. For an app only you use, it may not be worth the ceremony; once you have several users, devices or consuming teams, it is. He closes with Kin Lane's warning that switching from code-first is hard, and his own view that the sooner you start, the more friends you make.

## Who should watch

Teams where front end and back end keep blocking each other, and anyone who has heard of consumer-driven contracts but never seen how they fit a deploy pipeline. Expect Postman screens in the demos; the workflow applies to any OpenAPI tooling, and he points to the OpenAPI.Tools list for alternatives.

## Related Conf42 talks

- Hari Krishnan on [contract-driven development for microservices](https://www.conf42.com/Incident_Management_2022_Hari_Krishnan_contract_driven_development_microservices) at Conf42 Incident Management 2022.
- Alparslan Avci on [distributed transactions in a service mesh](https://www.conf42.com/Chaos_Engineering_2022_Alparslan_Avci_distributed_transactions_in_service_mesh), from the same event.
- Sakshyam Shah on [steady states and developing hypotheses](https://www.conf42.com/Chaos_Engineering_2022_Sakshyam_Shah_steady_states_developing_hypotheses).

[Watch Arlemi Turpault's talk](https://www.conf42.com/Chaos_Engineering_2022_Arlemi_Turpault_how_to_win_friends_and_influence_people_with_api_first) from [Conf42 Chaos Engineering 2022](https://www.conf42.com/ce2022).

## From Postman

Postman is an API collaboration platform for designing, mocking, documenting and testing APIs.

- Postman: [postman.com](https://www.postman.com/)

[Watch the talk on YouTube](https://youtu.be/LI8ZBjGT0YA).

## Watch the talk

[How to Win Friends and Influence People with API First](https://www.conf42.com/Chaos_Engineering_2022_Arlemi_Turpault_how_to_win_friends_and_influence_people_with_api_first) at Conf42 Chaos Engineering 2022.
