# One blocking call and your reactive Spring app is not reactive

Conf42 Blog, 2021-03-26. https://www.conf42.com/blog/enterprise2021/one-blocking-call-breaks-reactive-chain

In short: Nicolas Frankel (Hazelcast) at Conf42 Enterprise Software 2021 on migrating Spring Boot from imperative to reactive in steps, with BlockHound to catch blocking calls

Swapping Spring MVC for WebFlux takes one dependency change. Making the app actually reactive takes the rest of the talk. At Conf42 Enterprise Software 2021, Nicolas Frankel, Developer Advocate at Hazelcast, migrates a small Spring Boot app from blocking to reactive one step at a time, and shows the step most migrations skip: proving that nothing in the chain still blocks.

He opens by saying he is no reactive guru and that this is a gentle introduction. It is, but it is also a practical migration recipe with the potholes left in.

## Why go reactive at all?

He starts with the Reactive Manifesto of 2014 and its four properties: responsive, resilient, elastic and message-driven, the last being the one he rates most important. The actor model behind it is the default on Erlang/OTP, but in Java the industry settled on Reactive Streams instead: a single event loop on a single thread dispatching messages to handlers. Nicolas Frankel said at Conf42 Enterprise Software 2021: "Non blocking is at the roots of reactive and reactive streams."

Scale is the wrong reason, in his view. Thread-per-request Tomcat or Jetty hits a limit somewhere, but "We are not Google, we are not Facebook, we are not Amazon." The better reason is the cloud bill: on hardware you already bought, wasted CPU cycles cost nothing extra, while in the cloud you pay for CPU, memory and storage, and a blocked thread is money spent on waiting.

## What does reactive cost you?

He lists the downsides before writing any code. A method call is now a subscription to a response you hope arrives later, which is harder to reason about. Debugging is harder because the thread may have switched and the stack no longer tells the story. You learn new APIs whose methods look alike across frameworks but differ in semantics. And the whole request-response chain must be reactive, since a single blocking call anywhere makes the chain blocking again.

The Reactive Streams API itself is small: publisher, subscriber, subscription (with a request method that gives you backpressure) and processor. Project Reactor builds Flux (zero to many items) and Mono (zero or one) on top, with no dependency on Spring; Spring depends on it. JDK 9 shipped the same four interfaces in the Flow class in 2017, and four years later, he notes, nobody uses them.

## The migration, step by step

The demo app uses Spring Data JPA on H2, with Hibernate's second-level cache backed by Hazelcast and Hibernate statistics on, so every cache miss, put and hit is visible in the log.

1. **Annotations to functional routes in Spring MVC.** Controllers become router function beans; handlers move to a dedicated class; routes nest under one parent path. Nothing is reactive yet, but the code now has the same shape as WebFlux's functional API. He recommends this detour because annotated code looks the same whether MVC or WebFlux runs it, and you can't tell at a glance which one is blocking.
2. **MVC to WebFlux.** Swap the web starter for the WebFlux starter and change the package names; the types are the same. The repository still blocks, so the response uses a body value instead of a publisher. It works, and it is not reactive, because JDBC under JPA still blocks.
3. **JPA to R2DBC.** Spring Data R2DBC with the H2 R2DBC driver. The schema and data scripts now need running by hand before the app accepts requests (later swapped for Spring's connection factory initializer), the repository becomes a reactive sorting repository returning Flux and Mono, and the Hibernate cache is gone.
4. **Prove it.** BlockHound, an agent added in development, throws a runtime exception whenever it detects a blocking call where none should be.
5. **New behaviour, reactive style.** A 404 for a missing person can't be an if-null check any more; it is switchIfEmpty returning a Mono error.
6. **Bring the cache back.** A caching service between handler and repository. The first version calls the cache synchronously, and BlockHound fails the request at once. The fix uses Hazelcast's asynchronous API, bridges its CompletionStage into Reactor, falls back to the database on empty, and puts the result into the cache asynchronously.

That BlockHound failure is the best moment in the talk: the safety net catching the speaker's own deliberate mistake.

## The advice he ends on

Migrate to the functional API first, don't mix annotations with the reactive engine, and use BlockHound because code review alone won't find every blocking call. Kotlin users should look at coroutines; the demo repository has a Kotlin branch. And reactive is a trade-off, not a default.

## Who should watch

Spring Boot developers weighing WebFlux, and anyone who already migrated and suspects a JDBC call is still hiding in the chain.

## Related Conf42 talks

- Rob Hedgpeth on [relational databases with R2DBC](https://www.conf42.com/Enterprise_Software_2021_Rob_Hedgpeth_relational_databases_r2dbc) at Conf42 Enterprise Software 2021.
- Grace Jansen on [reacting to an event-driven world](https://www.conf42.com/Enterprise_Software_2021_Grace_Jansen_event_driven_world) at Conf42 Enterprise Software 2021.
- Nicolas Frankel on [migrating an app to the cloud with Quarkus, Kotlin, Hazelcast and GraalVM](https://www.conf42.com/Cloud_Native_2021_Nicolas_Frankel_app_migration_cloud_quarkus_kotlin_hazelcast_graalvm) at Conf42 Cloud Native 2021.

[Watch Nicolas Frankel's talk](https://www.conf42.com/Enterprise_Software_2021_Nicolas_Frankel_imperative_reactive)

## From Hazelcast

Hazelcast makes an in-memory data grid (distributed data structures, replicated or sharded across a cluster) and Hazelcast Jet for in-memory stream processing. In the talk it is the cache: first behind Hibernate, then called directly through its asynchronous API.

- Hazelcast: [hazelcast.com](https://hazelcast.com)

[Watch the talk on YouTube](https://youtu.be/EgSt47s8tFo).

## Watch the talk

[Migrating from Imperative to Reactive](https://www.conf42.com/Enterprise_Software_2021_Nicolas_Frankel_imperative_reactive) at Conf42 Enterprise Software 2021.
