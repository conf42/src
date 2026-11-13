# One GraphQL call instead of two bloated REST calls, live in Quarkus

Conf42 Blog, 2021-03-24. https://www.conf42.com/blog/enterprise2021/graphql-fixes-over-and-under-fetching

In short: Phillip Krüger (Red Hat) at Conf42 Enterprise Software 2021 on fixing over- and under-fetching by turning a JAX-RS API into MicroProfile GraphQL

A REST endpoint gives you what the server decided you wanted, and then you make another call for the rest. At Conf42 Enterprise Software 2021, Phillip Krüger, Principal Software Engineer at Red Hat, builds a small API in JAX-RS, shows exactly where it wastes calls and bytes, then converts it to MicroProfile GraphQL on Quarkus in a few annotations. The takeaway: the fix for over- and under-fetching is mostly deleting code, and the interesting part starts after that.

It is a live-coding talk, fast and demo-heavy, with the occasional hot-reload hiccup that every Quarkus developer will recognise.

## What is wrong with the REST version?

The example is a gamification system: a big Person object stored in a relational database through JPA, and a Score service backed by a flat file on disk, each fronted by its own REST API. To show one person's page, the client fetches the whole person, picks out the id number, then calls the score service for more data than it needs.

Phillip Krüger said at Conf42 Enterprise Software 2021: "So I had to make two HTTP calls. Both returned too much data, but the first one didn't return all the data that I wanted."

That is the whole problem in two sentences. Over-fetching: data in the response you don't use (a mobile screen wants less than the web page). Under-fetching: not enough data from one endpoint, so you call a second one. He traces GraphQL's origin to the same pain at Facebook, where mobile traffic made every wasted byte expensive; it has been in use there since 2012 and public as a specification since 2015.

## How much code does the conversion take?

Very little. He copies the person REST resource, removes the JAX-RS annotations, marks the class as a GraphQL API and the two methods as queries. The Quarkus dev UI then offers a GraphQL UI next to Swagger UI, and the schema is built in, with no OpenAPI layer bolted on top. Asking for only names returns only names.

Under-fetching goes away with a source field: a method that takes a Person as its source and adds a list of scores onto it. The schema grows a scores field on Person, and one request now returns the person and their scores together.

## Where does it get slow, and how do you fix it?

A source field on a list of 1,000 people would mean 1,000 calls to the score backend. The log shows it happening. Batching changes the method to take the whole list of people, so the backend gets one call with all the ids.

He then adds an exchange-rate field on Person and a separate weather API that calls out to a real service on the internet, and combines person, exchange rate and weather for London into one request. Returning a CompletionStage makes it concurrent: weather no longer waits for the person, and with two destinations (pound and dollar, London and New York) the two exchange-rate lookups run in parallel too. Whether that matters, he notes, depends on your use case.

## What else comes in the box?

The second half is a tour of MicroProfile GraphQL features:

- **Partial results.** If the score system is down, the caller still gets the person, with null scores and an error entry. Runtime exceptions hide their message by default and checked exceptions pass it through; both are configurable per exception.
- **Mapping.** A Long id that the schema shows as BigInteger can be mapped to Int; JSON-B date formats work, as does the library's own date format annotation; a complex Email object can be exposed as a plain string, built from its toString and a constructor.
- **Mutations** for create, update and delete, whose results are queryable like any query.
- **Introspection**: querying the schema with GraphQL itself.
- **Security** through the normal Quarkus stack; he protects a query with a roles annotation and a JWT from Keycloak.
- **Context and events**: inject the query context into the backend service to see which fields were asked for, so the database query can be trimmed too.
- **Custom execution**: an injected execution service runs a query on a schedule, here a morning leaderboard mail.

Bean Validation, metrics, tracing, context propagation and generics are integrated as well; metrics and tracing need only the extension.

On the roadmap at the time: a dynamic client and a typesafe client (similar to the MicroProfile REST client), subscriptions over WebSockets, and annotations to make paging and filtering easier.

## Who should watch

Java developers who know JAX-RS and wonder what GraphQL costs them to adopt. It is a code-along, not a theory talk; the example code is on Phillip's GitHub ([graphql-example](https://github.com/phillip-kruger/graphql-example)).

## Related Conf42 talks

- Joe Wingard on [autoprovisioned REST, GraphQL and gRPC](https://www.conf42.com/JavaScript_2021_Joe_Wingard_Autoprovisioned_REST_GraphQL_gRPC) at Conf42 JavaScript 2021.
- Roy Derks on [TypeScript and GraphQL for web apps](https://www.conf42.com/JavaScript_2022_Roy_Derks_web_apps_future_typescript_graphql) at Conf42 JavaScript 2022.
- Nicolas Frankel on [migrating an app to the cloud with Quarkus, Kotlin and GraalVM](https://www.conf42.com/Cloud_Native_2021_Nicolas_Frankel_app_migration_cloud_quarkus_kotlin_hazelcast_graalvm) at Conf42 Cloud Native 2021.

[Watch Phillip Krüger's talk](https://www.conf42.com/Enterprise_Software_2021_Phillip_Krger_queryable_apis_microprofile_graphql)

## From Red Hat

Phillip works on the GraphQL support in Quarkus, the framework the whole demo runs on, with Keycloak providing the tokens.

- Red Hat: [redhat.com](https://www.redhat.com/)
- Quarkus: [quarkus.io](https://quarkus.io/)

[Watch the talk on YouTube](https://youtu.be/UnWnSYiGtTE).

## Watch the talk

[Writing queryable APIs with MicroProfile GraphQL](https://www.conf42.com/Enterprise_Software_2021_Phillip_Krger_queryable_apis_microprofile_graphql) at Conf42 Enterprise Software 2021.
