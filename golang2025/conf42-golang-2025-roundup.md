# Conf42 Golang 2025: real dependencies in tests, hidden ones in go.mod

Conf42 Blog, 2025-04-04. https://www.conf42.com/golang2025/conf42-golang-2025-roundup

In short: Conf42 Golang 2025 roundup: 64 talks on testing Go services, dependency hygiene, Wasm and eBPF, confidential computing and Go in banking and fintech.

Conf42 Golang 2025 ran on April 3, 2025, with 64 talks, the biggest lineup of any Conf42 Golang so far, under the usual greeting to the gophers from outer space. Two ideas kept coming back: test against real dependencies instead of mocks, and know exactly which dependencies you're carrying. Around them, Go showed up at the edge, in the kernel, inside secure enclaves and in a lot of banks. The full lineup is on the [event page](https://www.conf42.com/golang2025) and the recordings are in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrDbxTLhVidTfS-6lJeAH6m-).

## Test against the real thing

Two talks made the same argument from different directions. [Manuel de la Pena](https://www.conf42.com/Golang_2025_Manuel_de_la_Pena_testing_go_integration), Staff Software Engineer at Docker and maintainer of Testcontainers for Go, showed a talk-rating service tested against real Postgres, Redis and Redpanda containers, plus an AWS Lambda running inside LocalStack. He then broke the average calculation on purpose and watched the test catch it in seconds. His tour of wait strategies is a good reason never to write `time.Sleep` in a test again.

[Nikolay Kuznetsov](https://www.conf42.com/Golang_2025_Nikolay_Kuznetsov_testing_go_services) of Zalando gave the companion piece: a practical guide to testing a Go service layer by layer. He leans on the testing trophy over the classic pyramid, since integration tests are now cheap enough to run more of them, and tests the repository layer against a real database rather than a mock. His toolkit covers Testcontainers, mocks generated with mockery, `httptest` for handlers, testify and go-cmp for comparing whole structs, and randomised test data. [Sridhar Dachepelly](https://www.conf42.com/Golang_2025_Sridhar_Dachepelly_testing_erp_orchestration) of Dell Technologies applied Go to test orchestration in large ERP systems.

## Know what's in your binary

[Andrii Raikov](https://www.conf42.com/Golang_2025_Andrii_Raikov_dependencies_code_management), Principal Software Engineer at Delivery Hero, asked the audience to name the indirect dependencies of their current project, then showed why most can't. Importing `fmt` silently pulls in `io`, `os`, `reflect` and more, and a few lines using the AWS SDK make a binary several times bigger. The second half covered patterns he has seen at Delivery Hero: a v2 client library that broke its v1 interfaces and stranded teams on the old version, and a `helpers` package that drifts into circular dependencies. His most practical advice: don't skip the import block in code review.

On the framework side, [Divya Darshana](https://www.conf42.com/Golang_2025_Divya_Darshana_http_communication_apis), an open source contributor to GoFr, showed circuit breakers, authentication and health monitoring for inter-service HTTP calls using the GoFr framework. And [Namkat Cedrick](https://www.conf42.com/Golang_2025_Namkat_Cedrick_career_experience_journey) of Iknite Studio gave the most personal talk of the day, "How Golang Changed My Life", revisiting old programming fears with a new mindset.

## Go beyond the server

[Alex Casalboni](https://www.conf42.com/Golang_2025_Alex_Casalboni_cloud_edge_webassembly), Developer Advocate at Edgee, explained why WebAssembly suits edge computing, where logic in the request path has a budget of a few milliseconds. He traced Go's Wasm support from the `wasm` target in Go 1.11 to WASI preview 1 in Go 1.21, pointed to TinyGo for the component model, and showed how Edgee runs analytics SDKs as Wasm components at the edge.

[Pranshu Srivastava](https://www.conf42.com/Golang_2025_Pranshu_Srivastava_cilium_ebpf_networking) of Cloudera spoke to people starting with eBPF who don't want to write their user space code in Rust, sharing his experience with Cilium, why he chose it and which mistakes to avoid. [Brian Loomis](https://www.conf42.com/Golang_2025_Brian_Loomis_cloud_platforms_resilience), Director of Architecture at Progress, covered a distributed job runner designed to survive an unreliable network. [Utham Kumar](https://www.conf42.com/Golang_2025_Utham_Kumar_v2x_communication_vehicles) of Nanyang Technological University took Go into vehicle-to-everything networks for connected cars.

## Security in Go services

[Srinivas Vallabhaneni](https://www.conf42.com/Golang_2025_Srinivas_Vallabhaneni_enclaves_security_confidential) of Walmart showed how Go fits confidential computing, keeping sensitive data inside secure enclaves in distributed systems without giving up performance. [Aditi Mallesh](https://www.conf42.com/Golang_2025_Aditi_Mallesh_identity_security_microservices) of Microsoft built identity orchestration as high-performance Go microservices across clouds, and [Santosh Bompally](https://www.conf42.com/Golang_2025_Santosh_Bompally_security_iac_threat) of Humana combined infrastructure as code with AI-driven threat detection. [Sudeep Shanubhog](https://www.conf42.com/Golang_2025_Sudeep_Shanubhog_security_cloud_adaptive) of Tential Solutions covered adaptive, real-time security for Microsoft cloud services written in Go.

## Go where the money moves

Finance had a strong showing. [Srinivas Allam](https://www.conf42.com/Golang_2025_Srinivas_Allam_banking_modernization_fintech) of Core ITS described Go modernising a tier-1 bank's legacy IBM iSeries infrastructure with zero-downtime migrations. [Deepu Komati](https://www.conf42.com/Golang_2025_Deepu_Komati_fintech_cloud_infrastructure) of PenFed Credit Union built financial decision systems in Go, and [Srinivas Reddy Mosali](https://www.conf42.com/Golang_2025_Srinivas_Reddy_Mosali_fintech_infrastructure_scaling) of Visa made the case for fintech infrastructure that never blinks. Beyond banking, [Ankita Kamat](https://www.conf42.com/Golang_2025_Ankita_Kamat_notification_latency_scaling) of Microsoft used Go's concurrency model for notification systems that handle millions of messages while keeping millisecond latency, [Hardik R Patel](https://www.conf42.com/Golang_2025_Hardik_R_Patel_data_pipelines_analytics) of PayPal designed multi-hop data pipelines for real-time analytics, and [Srikar Kompella](https://www.conf42.com/Golang_2025_Srikar_Kompella_serverless_migration_aws) of Prime Video used Go for a serverless SaaS migration on AWS.

## Sponsors

Thanks to [SREday](https://www.sreday.com/), our diamond sponsor, and [Rapydo](https://www.rapydo.io/), our gold sponsor. Silver sponsors [Edgee](https://www.edgee.cloud/), [Tential](http://www.tential.com/), [Delivery Hero](https://careers.deliveryhero.com/deliveryhero-jobs) and [Docker](https://www.docker.com/) all joined in, each with a speaker on the lineup. Thanks also to [StarterAI](https://www.starterai.dev/) for the newsletter.

## What's next

All 64 talks are linked from the [Conf42 Golang 2025 page](https://www.conf42.com/golang2025). The gophers return for [Conf42 Golang 2026](https://www.conf42.com/golang2026) on May 21, 2026. Until then, go read your `go.sum`.
