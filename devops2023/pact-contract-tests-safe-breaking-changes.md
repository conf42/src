# Contract tests tell you which breaking changes aren't breaking

Conf42 Blog, 2023-01-26. https://www.conf42.com/devops2023/pact-contract-tests-safe-breaking-changes

In short: Frank Kilcommins (SmartBear) at Conf42 DevOps 2023 on bi-directional contract testing with Pact and OpenAPI to evolve microservice APIs safely

Removing an endpoint from a public API is, by the textbook, a breaking change that needs a new major version. Frank Kilcommins, API Technical Evangelist at [SmartBear](https://smartbear.com/), showed at Conf42 DevOps 2023 how bi-directional contract testing with Pact and PactFlow lets a provider prove nobody uses that endpoint and ship the change safely, while blocking the innocent-looking change that would actually break a consumer.

The talk is half API design advice, half a CI walkthrough, and the first half stands on its own.

## Why is API evolution getting harder?

Microservices keep driving API growth, Kilcommins says, citing SmartBear's and Postman's industry reports, and managing the sprawl is outgrowing the tools. He quotes a Gartner prediction that by 2025, less than 50% of enterprise APIs will be managed. The unmanaged rest risk becoming zombie APIs, poorly maintained and open to vulnerabilities, while shadow APIs appear because nobody knows what already exists. The deeper problem is blindness: providers lose track of who consumes what, which makes safe evolution close to impossible.

## Is good extensibility design enough?

It helps, and his cheat sheet is worth keeping:

- Design from the outside in, describe the surface with OpenAPI, and treat APIs as products.
- Define extension points: tell consumers which parts are stable and which are newer and likely to change.
- Communicate an extensibility pattern, usually must-ignore: clients must not break on fields they don't recognise.
- Use semantic versioning, let clients test against the next version early, and keep a changelog.
- Don't add required inputs, remove outputs or make them optional, or change a property's type, and don't be inconsistent in your process.

But extensibility alone fails because of Hyrum's Law: with enough users, all observable behaviour of your API will be depended on by somebody, documented or not. Unsure whether a change is breaking, teams reach for a new major version just in case, and major version proliferation costs real money and cognitive load.

## Why don't end-to-end tests solve it?

Carrying a monolith's testing strategy into microservices produces an unbalanced pyramid: every small consumer change needs all the downstream services and their test data stood up. It is expensive, slow (he mentions waiting 30 minutes or more for a pipeline), unreliable and not targeted. The flaky test that passes on a rerun is the tell: once you rerun until green, nobody trusts the suite.

Environments make it worse. With consumer and provider versions spread across CI, staging and production, promoting one component on its own means checking it against whatever version of its partner sits in the next environment, and the matrix grows with every component.

"If you can't deploy services independently, then you don't have microservices," Frank Kilcommins said at Conf42 DevOps 2023, quoting his colleague Beth Skurrie, a co-founder of Pact and PactFlow. What you have instead is a distributed monolith.

## How does bi-directional contract testing work?

Unlike consumer-driven contract testing, it is schema-based rather than specification by example, suits a design-first provider workflow, and lets teams bring their own tools:

1. The provider publishes its OpenAPI document plus proof that the implementation matches it, using any verification tool (Dredd, REST Assured, ReadyAPI, Postman, Schemathesis).
2. The consumer keeps unit testing against its own mock (Cypress, WireMock, Mountebank) and serialises its expectations into a pact file: consumer name, provider name, the expected interactions.
3. The PactFlow broker checks that the consumer's expectations are a subset of what the provider's contract supports.
4. The can-i-deploy check gates each release by querying the matrix: every consumer and provider version, which pairs are compatible, and where each is deployed.

Verification is asynchronous, one integration at a time, and it does not need access to the provider's code, so designers, QAs and SDETs can take part too.

## What does the demo show?

A .NET products API with three endpoints, tested with Schemathesis, and a .NET console consumer tested with xUnit and WireMock, which writes the pact file. The consumer expects a 404 from get-product-by-id for an unknown ID. Both sides run in GitHub Actions with can-i-deploy as a gate.

Then two product owner requests. First: remove the delete endpoint, it belongs in the admin API. Traditionally breaking, but the broker shows no consumer uses it, so it deploys. Second: stop returning 404s because client errors make the reports look bad. That one fails can-i-deploy, and PactFlow says exactly why: the provider no longer returns the 404 the consumer expects.

His takeaway is a rebalanced pyramid with fewer end-to-end and integration tests and a versioning strategy that is, as he put it, more pragmatic rather than dogmatic.

## Who should watch

API owners who version defensively because they cannot see their consumers, and teams whose integration suite takes longer than the change it is testing.

## Related Conf42 talks

- Hari Krishnan on [contract-driven development for microservices](https://www.conf42.com/Incident_Management_2022_Hari_Krishnan_contract_driven_development_microservices) at Conf42 Incident Management 2022.
- Arlemi Turpault on [API-first](https://www.conf42.com/Chaos_Engineering_2022_Arlemi_Turpault_how_to_win_friends_and_influence_people_with_api_first) at Conf42 Chaos Engineering 2022.
- Navendu Pottekkat on [SRE best practices for API design](https://www.conf42.com/Site_Reliability_Engineering_2022_Navendu_Pottekkat_sre_best_practices_api_design) at Conf42 SRE 2022.

[Watch Frank Kilcommins's talk](https://www.conf42.com/DevOps_2023_Frank_Kilcommins_dont_break_my_api)

## From SmartBear

SmartBear builds API and testing tools, including PactFlow for contract testing and ReadyAPI for API testing.

- [SmartBear website](https://smartbear.com/)

[Watch the talk on YouTube](https://youtu.be/Q0hp6meYi48).

## Watch the talk

[Let's Make a Pact - Don't Break my API!](https://www.conf42.com/DevOps_2023_Frank_Kilcommins_dont_break_my_api) at Conf42 DevOps 2023.
