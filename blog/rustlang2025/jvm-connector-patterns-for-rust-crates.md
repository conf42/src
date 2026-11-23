# Porting JVM library design to Rust crates, pattern by pattern

Conf42 Blog, 2025-07-26, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/jvm-connector-patterns-for-rust-crates

In short: Venkata Appalapuram of Ritepros at Conf42 Rustlang 2025 on mapping a Spark JMS connector's provider interfaces and exceptions to Rust traits and Results.

Good library design survives a change of language; only the syntax moves. That is the thesis of Venkata Appalapuram's talk at Conf42 Rustlang 2025. Venkata, of Ritepros Inc, used the Spark JMS connector built for Capital One as a case study and walked through how each of its JVM design decisions translates into Rust crate design.

If you write libraries in Java or Scala and are starting on Rust, this is a practical side-by-side: provider interfaces next to traits, exception hierarchies next to `Result`, Mockito next to trait mocks.

## The connector that set the requirements

The project background gives the patterns their weight. The Spark JMS connector reads financial transactions from several message queue providers (ActiveMQ, IBM MQ and others), feeds real-time pipelines including fraud detection, and is reused across departments. It has to be fast and it cannot lose messages, because a customer whose transaction vanished does not care which broker was at fault.

The other hard requirement was normalizing many different message patterns into one schema before handing them on. From that, Venkata drew five universal design challenges: abstraction boundaries, configuration, error propagation, extensibility without breaking compatibility, and performance overhead.

## Provider interfaces become traits

On the JVM side, the connector used provider interfaces with dependency injection, so the implementation for a given broker can be swapped based on the user's configuration. Venkata's point is that this pattern has a natural counterpart in Rust's trait system, with the bonus of compile-time polymorphism and zero-cost dispatch, and trait objects available when you genuinely need runtime choice.

Separation of concerns carries over the same way. In the JVM connector, message consumers do not know which queue a message came from, acknowledgement is handled by the connection layer rather than the processing code, and error handlers plug in and out. In Rust, the module system enforces those boundaries, ownership makes it explicit who is responsible for a connection, and the borrow checker discourages leaky abstractions.

## Exceptions become Results, and the compiler checks your homework

The error-handling section is the most useful comparison. The JVM version uses checked and unchecked exceptions with detailed messages and stack traces, with some care about the cost of throwing. The Rust version encodes success or failure in `Result`, uses custom error enums for composable error types, adds context with the `anyhow` and `thiserror` crates, and relies on exhaustive `match` so no error case is silently ignored.

Configuration follows a similar arc. Both sides use a builder pattern with sensible defaults and validation at construction time. Rust can push more of that validation into the type system, including const generics for static configuration.

## Testing and docs travel well too

Testing strategies map almost one to one: Mockito against trait mock implementations, Testcontainers for real broker instances in integration tests, and property-based testing with JUnit theories or jqwik on the JVM against proptest and quickcheck in Rust. Documentation goes from Javadoc and example classes to rustdoc with doc tests that are compiled and run, so examples cannot rot.

Venkata reported a 10x performance improvement and a 99.9% reliability target met for the work. The closing lessons are the parts to keep: abstraction principles are language-neutral, use each language's strengths, testing strategy is portable even when test code is not, and document intent, not just implementation.

## Who should watch

JVM engineers building their first serious Rust crate, and anyone maintaining a library across two ecosystems. Seasoned Rust library authors will find the patterns familiar but may enjoy the JVM mirror.

## Related Conf42 talks

- [Rust for Java Programmers: a Personal Perspective](https://www.conf42.com/Rustlang_2023_Ovidiu_Ionescu_java_programmers_personal_perspective) by Ovidiu Ionescu: the same migration, from the individual developer's side.
- [Lessons Learned From Maintaining an SDK in Python for Three Years](https://www.conf42.com/Python_2024_Adam_Furmanek_lessons_learned_maintaining_sdk_in_python) by Adam Furmanek: library maintenance lessons from another ecosystem.
- [No JVM, no Kafka: streaming data pipelines](https://www.conf42.com/Kube_Native_2024_Bobur_Umurzokov_jvm_kafka_streaming_data) by Bobur Umurzokov: what message pipelines look like without the JVM.

[Watch Venkata Appalapuram's talk](https://www.conf42.com/Rustlang_2025_Venkata_Appalapuram_systems_architecture_ai)

[Watch the talk on YouTube](https://youtu.be/IXu91eoXL1I).

## Watch the talk

[Cross-Language Library Design: Lessons from Building JVM Data Connectors That Translate to Rust Crate Development](https://www.conf42.com/Rustlang_2025_Venkata_Appalapuram_systems_architecture_ai) at Conf42 Rustlang 2025.
