# Use your traces as test assertions and delete the mocks

Conf42 Blog, 2023-06-09. https://www.conf42.com/obs2023/trace-based-testing-instead-of-mocks

In short: Adnan Rahic (Tracetest) at Conf42 Observability 2023 on observability-driven development, with OpenTelemetry spans as integration test assertions.

Backend integration tests are 90% plumbing and 10% test, and the plumbing is mostly mocks that drift from reality. At Conf42 Observability 2023, Adnan Rahic, Senior Developer Advocate at Tracetest, proposed observability-driven development: instrument the code with OpenTelemetry as you write it, then assert against the spans your real system emits, including the ones from services your test never calls directly.

It's a short talk built on a small demo (a books service, an availability service, one database) and Tracetest, the open source tool Adnan works on. The idea, trace-based testing, doesn't depend on the tool.

## What's wrong with integration tests today?

Adnan's list of pains in microservice testing: you don't know where in the chain an HTTP transaction fails, you can't easily track service-to-service calls, and those calls are hard to mock. A backend integration test needs a trigger, database access, auth, environment propagation, maybe a message bus, plus monitoring to collect logs. His rough split is 90% of the code to make the test run and 10% for the assertions.

The traditional example on screen makes the point: a Node.js test with chai imports, a JSON mock of the books list, a request, and two lines that check for a 200 and a body equal to the mock. Change the response structure and you rewrite the mock. "Now I like saying no mocks a lot because I don't like mocking at all," Adnan Rahic said at Conf42 Observability 2023.

## What is a trace-based test?

A distributed trace records the path a request takes through APIs and services; each step is a span carrying the operation's details, such as HTTP status codes, timings and database statements. A trace-based test triggers the system and asserts against both the response and those span attributes.

The equivalent Tracetest definition is a few lines of YAML: an HTTP trigger on the books endpoint, a selector for the GET span asserting the status code is 200, and a selector for a custom Books List span asserting the books.list.count attribute equals three. No mocks, and no dependency on the language the service is written in.

## How does TDD still work?

The demo keeps the red-green loop. Adnan writes the assertions first and runs them: the status code passes, but there is no span with a books count, so the test fails. He adds a span attribute in the handler, reruns, and it passes. He then adds a timing assertion, span duration under 500 milliseconds, watches it fail against a slow endpoint, fixes the code, and it goes green.

That is the observability-driven part: the instrumentation gets written alongside the code because the tests need it, which also means production gets the same traces.

## Where does it beat a normal API test?

The strongest example tests something a response check can't see. The books service calls the availability service for each book, and that service records an isAvailable attribute on its span. Adnan asserts that all three checks return true. One book has zero stock, so the test fails, even though the API response itself is a perfectly healthy 200. You're validating the whole transaction, not just its front door.

The same applies to asynchronous work: values pulled off RabbitMQ or Kafka show up in spans, so you can assert on them. Wildcard assertions cover rules such as every database span finishing under 100 milliseconds. Tests can be chained into transactions that pass outputs to inputs.

## How does it fit an existing setup?

Tracetest sits beside your OpenTelemetry pipeline. It triggers the app over HTTP or gRPC, then reads the resulting trace either straight from the OpenTelemetry Collector or from a trace store such as Jaeger, OpenSearch or Tempo, and runs the assertions. Adnan lists Lightstep, New Relic and Elastic among the tracing back ends it works with. It installs as a CLI plus a server container, with Docker Compose and Kubernetes supported, and tests run from the web UI or the CLI.

## Who should watch

Teams that already have OpenTelemetry tracing and still maintain a separate set of mocked integration tests. If you have no tracing yet, this is a good argument for adding it, but expect to do that work first. "Testing distributed systems is even harder," Adnan said, and the talk doesn't pretend otherwise.

Related Conf42 talks: [Nicolas Fränkel on OpenTelemetry tracing](https://www.conf42.com/DevOps_2023_Nicolas_Frankel_opentelemetry_tracing), [Henrik Rexed on event-driven observability with OpenTelemetry](https://www.conf42.com/Observability_2023_Henrik_Rexed_event_driven_observability_opentelemetry) from the same event, and [Ivan Pesenti on TDD for a complex app](https://www.conf42.com/Golang_2023_Ivan_Pesenti_complex_app_tdd).

[Watch Adnan Rahic's talk](https://www.conf42.com/Observability_2023_Adnan_Rahic_observabilitydriven_development) from [Conf42 Observability 2023](https://www.conf42.com/obs2023).

## From Tracetest

Tracetest is an open source trace-based testing tool from Kubeshop, listed by the CNCF, that uses OpenTelemetry spans as test assertions.

- Tracetest: [tracetest.io](https://tracetest.io/)
- [Download Tracetest](https://tracetest.io/download)
- Adnan's tutorial post: [The difference between TDD and ODD](https://tracetest.io/blog/the-difference-between-tdd-and-odd)

[Watch the talk on YouTube](https://youtu.be/xtkgZxNbnPI).

## Watch the talk

[What is observability-driven development?](https://www.conf42.com/Observability_2023_Adnan_Rahic_observabilitydriven_development) at Conf42 Observability 2023.
