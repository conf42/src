# GoFr wires tracing, metrics and health checks into gRPC for you

Conf42 Blog, 2025-05-10, updated 2026-11-09. https://www.conf42.com/blog/obs2025/gofr-grpc-observability-by-default

In short: GoFr contributor Divya Darshana demos at Conf42 Observability 2025 how the Go framework makes gRPC servers, clients and streams observable with zero instrumentation.

gRPC is fast, strongly typed and great at streaming, and out of the box it tells you almost nothing about what's happening inside those binary pipes. At Conf42 Observability 2025, Divya Darshana, an open source contributor to GoFr, the opinionated Go framework from GoFr.dev, demoed how GoFr closes that gap: every gRPC call, unary or streaming, gets logged, traced and measured, and health checks are registered, without writing a line of instrumentation code. It's a framework talk by a contributor, so expect GoFr front and centre.

## Why gRPC needs help

Darshana starts with the reasons teams pick gRPC: HTTP/2 multiplexing, protobuf binary serialisation, language-agnostic contracts that make schema mismatches rare, and bidirectional, client and server streaming. Then the catch: by default there's no request visibility and no health checks. Her analogy is driving blindfolded at night, fast and with no idea what's ahead.

The blind spots she lists are familiar to anyone who has run gRPC in production. No distributed tracing, so a request that touches 5, 10 or 20 services leaves a fragmented picture. Unstructured, context-free logs that turn a simple bug into a day of grepping. No latency, error rate or volume metrics, so a latency spike on a payment service or a silently failing streaming pipeline goes unnoticed until something downstream complains. Teams then spend weeks hand-instrumenting services to stitch the story together.

## The demo: proto in, observable server out

The live part is short and concrete. Start with a `greet.proto` service definition and run the protobuf compiler, which produces the usual `greet.pb.go` and `greet_grpc.pb.go`. Those files work, but they carry no observability and no health checks.

Then install the GoFr CLI and run its `wrap grpc server` command against the proto file. It generates several files next to the proto; the only one you edit is the server template, already wired with GoFr's context, observability hooks and health checks. Implement the handler (here, take a user's info and reply with a greeting), register the service with the GoFr app in `main.go`, and run it.

Call it from Postman and the request shows up in the logs. Metrics are exposed on a `/metrics` endpoint on port 2121, and traces, both built-in and custom, appear in the configured trace exporter. The GoFr context inside each handler also gives access to connected databases, metrics, logs and traces, so custom spans and DB calls don't need extra plumbing.

## Health checks that Kubernetes can use

GoFr adds a health service to every gRPC server, registered for the server as a whole and for each individual service. A health request against the server returns overall status; one against a named service returns just that service. You can also set a service's serving status at runtime, temporarily marking it unfit to serve and bringing it back, which maps neatly onto Kubernetes readiness checks.

## Streams get spans per message

The section that will interest gRPC veterans is streaming, where observability is usually weakest. GoFr instruments server, client and bidirectional streams the same way. In a chat service example, each message sent or received becomes its own span, and stream duration, message counts and in-stream errors are captured automatically. Clients built with GoFr's client wrapper get auto-instrumented upstream calls too, so the call graph is traceable across services.

## Who should watch

Go developers building gRPC microservices who are tired of copy-pasting interceptors, and teams evaluating Go frameworks. If you already have a mature OpenTelemetry interceptor setup, the streaming and health check parts are still worth a look. The docs and examples live at gofr.dev, and the project invites contributors.

## Related Conf42 talks

- Aryan Mehrotra on [building efficient, observable Go microservices with GoFr](https://www.conf42.com/Golang_2024_Aryan_Mehrotra_revolutionize_gofr_observable), the framework's wider tour.
- Aditya Mattos on [gRPC in Python. Build fast scalable APIs for your services](https://www.conf42.com/Python_2023_Aditya_Mattos_grpc_fast_scalable_apis).
- Krishna Rao Vemula on [Go-Powered Microservice Architecture: Optimizing Performance in Cloud-Native Applications](https://www.conf42.com/Golang_2025_Krishna_Rao_Vemula_microservices_performance_cloud).

[Watch Divya Darshana's talk](https://www.conf42.com/Observability_2025_Divya_Darshana_clarity_gofr_grpc)

[Watch the talk on YouTube](https://youtu.be/Cnx9lixzK2s).

## Watch the talk

[Bringing Clarity to gRPC through GoFr : The Role of Observability](https://www.conf42.com/Observability_2025_Divya_Darshana_clarity_gofr_grpc) at Conf42 Observability 2025.
