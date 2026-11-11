# Scala cold starts of one to two seconds pushed a telecom team to Go

Conf42 Blog, 2022-03-31. https://www.conf42.com/blog/golang2022/scala-to-go-cold-starts-telephony

In short: Herve Ah-Leung (Smartnumbers) at Conf42 Golang 2022 on moving a fraud prevention team from Scala to Go microservices, and what Go did and did not fix

When your service sits in the path of a phone call, a one-second cold start is not a performance footnote. At Conf42 Golang 2022, Herve Ah-Leung, Senior Software Engineer at Smartnumbers, told how his fraud prevention team moved an almost-monolithic Scala system to Go microservices, starting with serverless cold starts that dropped from one to two seconds to milliseconds.

He is clear about the scope: this is a team's journey and its lessons, not a pitch for microservices or for Go.

## Why is latency the constraint that matters here?

Smartnumbers builds telecom software: fraud prevention, call management, telecoms migration and mobile solutions. Herve works on fraud prevention, where every millisecond a service adds is a millisecond a caller waits. Herve said at Conf42 Golang 2022: "So if a person is trying to contact emergency services, you can't wait forever to process the call."

## The microservices bill, itemised

Before praising anything, Herve lists what microservices cost, using his team's own AWS X-Ray service map as Exhibit A:

- **Communication complexity and cognitive load.** With 100 services, nobody remembers what each one does.
- **Latency.** Service A calls B calls C, and the hops add up.
- **Change propagation.** Adding or removing a field in a request or response means finding every consumer, across dev, UAT and production, without breaking any.
- **Shared library patches.** A security fix in a common library means 100 redeploys for 100 services.

Any language would face these. The question he asks is how to get the most out of Go against them.

## How much did Go cut the cold starts?

Three years before the talk, the team ran serverless functions in Scala on AWS Lambda. Cold start length depends on the language, the package size, and whether the function sits in a private network. On the JVM they saw cold starts of one to two seconds, and a Scala function calling another Scala function could chain them. A trial in Go brought cold starts down to milliseconds, which he puts down to lightweight Go binaries that the provider can fetch and provision quickly. That first latency win convinced them to move fully to Go.

## What else made the move easier?

His other reasons are less dramatic but just as practical. None of the team had Go experience, yet SDKs for AWS, GCP and Azure and a large supply of tutorials let them write HTTP and GraphQL servers, mocks, hashing and database code from scratch. The standard library covers crypto, encoding, errors, fmt, os, strings, sync and time without a single download, which he contrasts with picking between moment and date-fns, or between Mocha, Sinon and Cypress, in JavaScript. Go modules replaced dep once Go 1.13 arrived.

The third-party picks: Gomega and Ginkgo for testing, GoReleaser to build and version the shared libraries every microservice depends on, and gqlgen to generate a GraphQL server from a schema. He also gives GoLand a quick mention.

The new-joiner story is the nicest data point. Go has few keywords and explicit syntax, and a few months into the move a junior engineer presented Go to the whole engineering department. Juniors spend their energy on where a service fits in the fleet, not on the language.

## Where did Go get in the way?

Package layout first. The team started with an MVC-style split (controllers, services, models) that grew into large, meaningless packages, then reorganised by business context (order, customer) with one, at most two, levels of nesting. That also showed which packages to extract as shared libraries and which to leave alone.

Then the language itself: pointers, which confused newcomers and, after one misuse broke production, led the team to avoid them unless needed and lean towards immutability; and implicit interfaces, which beginners find hard to grasp.

Next on their list: Protocol Buffers for schema-validated, low-latency service contracts, the generics that had just landed in Go 1.18, and, half joking, writing infrastructure, pipelines, task runners and docs in Go so nobody has to write YAML.

## Who should watch

Teams weighing a JVM-to-Go move for latency-sensitive or serverless workloads, and leads onboarding engineers new to Go. It is a war story with practical lessons, not a benchmark study.

## Related Conf42 talks

- Lerna Ekmekcioglu on [moving from a monolith to microservices on AWS](https://www.conf42.com/Cloud_Native_2022_Lerna_Ekmekcioglu_monolith_microservices_aws) at Conf42 Cloud Native 2022.
- Bhaskara Beeraka on [scaling telecom microservices](https://www.conf42.com/Golang_2025_Bhaskara_Beeraka_telecom_microservices_scaling) at Conf42 Golang 2025.
- Savas Ziplies on [running Go web apps on AWS Lambda](https://www.conf42.com/Golang_2022_Savas_Ziplies_serverless) at Conf42 Golang 2022.

[Watch Herve Ah-Leung's talk](https://www.conf42.com/Golang_2022_Herve_AhLeung_successful_microservices_architecture)

## From Smartnumbers

Smartnumbers is a telecom software company covering fraud prevention, call management, telecoms migration and mobile solutions; Herve works on its fraud prevention products.

- Smartnumbers: [the Smartnumbers website](https://hubs.ly/Q016xG910)

[Watch the talk on YouTube](https://youtu.be/ycKBGzOHBgQ).

## Watch the talk

[Successful Go for microservices architecture](https://www.conf42.com/Golang_2022_Herve_AhLeung_successful_microservices_architecture) at Conf42 Golang 2022.
