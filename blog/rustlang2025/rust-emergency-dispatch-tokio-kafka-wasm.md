# A Rust emergency dispatch system on Tokio, Kafka and Wasm

Conf42 Blog, 2025-08-21, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/rust-emergency-dispatch-tokio-kafka-wasm

In short: Lakshmi Vara Prasad Adusumilli of Conduent at Conf42 Rustlang 2025 on building life-critical emergency response systems in Rust with Tokio, Kafka and WebAssembly.

When an earthquake hits, emergency call volume spikes at exactly the moment infrastructure starts failing, and the dispatch system gets no second chance. At Conf42 Rustlang 2025, Lakshmi Vara Prasad Adusumilli, Senior DevOps Lead and Cloud Lead at Conduent, walked through an emergency dispatch architecture built in Rust and explained why each component is there.

Lakshmi comes to Rust from cloud and DevOps work, and it shows in a good way: the talk spends as much time on Kafka semantics and edge deployment as on the borrow checker, and explains both with patient analogies.

## Survival requirements, not performance requirements

The scenario frames everything: a disaster drives call volumes far above normal, the system must handle very high message rates without dropping one, and uptime targets have to hold while the surrounding infrastructure is collapsing. Lakshmi's point is that these are survival requirements.

Lakshmi traced failures in traditional stacks to two sources: memory-safety bugs in C and C++ code, and garbage-collection pauses in Java at the moment an instant response is needed. Rust addresses both with ownership and borrowing, zero-cost abstractions, compiler-checked concurrency, and deterministic cleanup.

## Invalid states should be unrepresentable

Ownership rules sound simple, the talk notes, but they remove leaks, data races and null references even at high concurrency. The analogy offered is strict airport security: nothing unsafe gets through.

The type-system section is the strongest design idea in the talk. A patient ID is not just an integer; it is a type that can only be constructed validly. Encoding domain rules in types moves error detection from an unpredictable runtime failure to a predictable compile-time check, so the business rules are enforced by the compiler.

## The architecture, component by component

The dispatch system combines four pieces:

- **async/await** for non-blocking I/O. Lakshmi's kitchen analogy: blocking I/O is a chef staring at a pot of pasta until it boils; async is the chef setting a timer and prepping something else.
- **Tokio** as the runtime: task scheduler, I/O event loop, timers.
- **Apache Kafka** as the durable event bus, with a clear explanation of topics, ordered partitions, producers, consumers and brokers, and why replay from an earlier offset and consumer-group failover matter in an emergency system.
- **WebAssembly at the edge** for sandboxed, portable modules with fast cold starts, running close to the incident.

One call flow ties it together: geolocate the caller, pull their information and query historical incidents concurrently, then let an ML model recommend resources and trigger dispatch.

## Edge computing as resilience

The edge section makes the best argument. Processing hazard data locally detects problems faster than a central system, keeps working during network outages, keeps sensitive data local, and reduces bandwidth when the network is saturated. In a disaster, Lakshmi argued, the edge is how the system survives losing the centre. Rust traits let one code path cover environmental sensors, traffic cameras and building structural monitors without runtime penalty.

Fault tolerance closes the design: circuit breakers that isolate failing components, and fallbacks that keep critical operations running in degraded mode.

## What 18 months taught them

Lakshmi reported no memory-related crashes over 18 months of operation, along with easier compliance and lower infrastructure costs. The challenges named are honest: the learning curve, gaps in legacy integrations, and longer compile times, which Lakshmi considers solvable with training and a maturing ecosystem.

## Who should watch

Engineers on public-safety, healthcare or other life-critical systems, and anyone who wants a clear explanation of async Rust and Kafka in one sitting. Rust veterans will find the language material introductory; the architecture is the draw.

## Related Conf42 talks

- [Building Resilient Emergency Response Platforms](https://www.conf42.com/Platform_Engineering_2025_Lakshmi_Vara_Prasad_Adusumilli_response_emergency_approach) by Lakshmi Vara Prasad Adusumilli: the same domain from the platform engineering side.
- [Predicting and Mitigating Emergency Situations on the Roads](https://www.conf42.com/Internet_of_Things_IoT_2024_Maksim_Kariagin_data_road_emergency) by Maksim Kariagin: a data-driven take on emergencies.
- [Nuclear Rust](https://www.conf42.com/Rustlang_2023_John_Darrington_nuclear_rust) by John Darrington: Rust in another field where failure is not an option.

[Watch Lakshmi Vara Prasad Adusumilli's talk](https://www.conf42.com/Rustlang_2025_Lakshmi_Vara_Prasad_Adusumilli_memory_safety_systems)

[Watch the talk on YouTube](https://youtu.be/wAccRwg0qQE).

## Watch the talk

[Building Mission-Critical Emergency Response Systems in Rust: Memory Safety Meets Life-Critical Performance](https://www.conf42.com/Rustlang_2025_Lakshmi_Vara_Prasad_Adusumilli_memory_safety_systems) at Conf42 Rustlang 2025.
