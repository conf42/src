# Put the database in the test, not in the CI config

Conf42 Blog, 2025-04-04, updated 2026-11-09. https://www.conf42.com/golang2025/testcontainers-go-integration-tests-docker

In short: Manuel de la Pena of Docker, maintainer of Testcontainers for Go, at Conf42 Golang 2025 on integration tests against Postgres, Redis, Redpanda and LocalStack.

If reproducing one failing integration test means starting the whole application, the test setup is in the wrong place. At Conf42 Golang 2025, [Manuel de la Pena](https://www.conf42.com/Golang_2025_Manuel_de_la_Pena_testing_go_integration), Staff Software Engineer at Docker and maintainer of Testcontainers for Go, showed how to move databases, brokers and even AWS Lambda out of the CI configuration and into the Go test that needs them.

The talk is mostly live code: one small service, four real dependencies, four test files, and timings on screen. It shows Docker's open source library, and it is about as practical as Go testing talks get.

## The CI server is a bad place for dependencies

Manuel starts with the setup many teams still run. A CI server, Jenkins or GitLab runners or GitHub Actions, is configured by you or a platform team to start every database, queue and cloud emulator your tests need. Those dependencies must match production versions and configuration, and the workers must be big enough to run all of them next to the tests.

Every dependency upgrade becomes a CI change, often in a system developers don't own. Each new service adds load to shared runners. And when a test fails, there's no easy way to run just that test on your laptop.

## Containers as test fixtures

Testcontainers for Go gives your test code programmatic access to the Docker engine: create, start, stop and terminate containers right where they're used. Testing the persistence layer means starting one Postgres container in that test, not the whole stack.

Each container's well-known port (5432 for Postgres, 3306 for MySQL) is mapped to a random host port, so many containers can run in parallel. Manuel lists three benefits: consistency, because dependencies run in containers instead of on your host; test data isolation, because each container has its own data; and build speed. Onboarding shrinks to installing Docker and running the tests, which the project calls the clone and run experience.

## One service, four dependencies

The demo app rates conference talks in real time. It stores ratings in PostgreSQL through `pgx`, caches in Redis, streams events through Redpanda with the `franz-go` Kafka client, and calls an AWS Lambda to compute statistics.

Each repository takes a connection string, which is what makes it testable. The Postgres test uses the Postgres module with an init SQL script, database name and credentials, waits until a log line appears twice, and hands the connection string to the repository. On the Postgres 15 Alpine image it passes in about 10 seconds. Redis needs no customisation and passes in about seven. Redpanda, with topic auto-creation on, takes 14 seconds on the first run because it pulls the image, and five on the next.

The Lambda test is the clever one. A Makefile builds and zips the function. The test starts LocalStack, copies the zip into the container, and runs the create-function command inside it once the container is up. It then reads the function URL and swaps in the randomly mapped port. Then Manuel breaks the average calculation on purpose, reruns, and the test catches it in seconds: total count correct, average wrong. A Lambda tested end to end on a laptop, with no AWS account involved.

## The parts of the API worth knowing

The second half tours the building blocks behind the modules:

- **ContainerRequest** defines image, exposed ports, network and readiness conditions.
- **Lifecycle hooks** run your code before and after create, start, readiness, stop and terminate.
- **Files** are copied in after the container is created but before it starts, so a database can boot with a known state.
- **Ryuk**, the extra container you may have spotted in `docker ps`, cleans up containers, networks, volumes and images when tests finish.
- **Wait strategies** replace `time.Sleep`: wait for an exec result, an exit, a file, a health check, a listening port, an HTTP response with a given status or header, a log line or regex, a SQL query, or all of them together.

Testcontainers can also build an image from a Dockerfile and run it, which is handy when the dependency is your own service.

## Who should watch

Go developers whose integration tests either live only in CI or don't exist, and platform teams tired of maintaining test databases on shared runners. If you already use Testcontainers, the LocalStack Lambda pattern and the wait strategies list are the parts to steal.

## Related Conf42 talks

- [How to test your code with Testcontainers in Go](https://www.conf42.com/Golang_2024_Julien_Breux_test_testcontainers_container) by Julien Breux (Google Cloud), a gentler first container test.
- [Tackling Flaky Tests: Strategies for Reliability in Continuous Testing](https://www.conf42.com/DevOps_2025_Mike_Morgan_testing_flaky_strategies) by Mike Morgan (Buildkite).
- [Cloud Testing Without the Wait](https://www.conf42.com/Cloud_Native_2025_Anita_Ihuman_kubernetes_development_testing) by Anita Ihuman (MetalBear), on testing against real Kubernetes from your machine.

[Watch Manuel de la Pena's talk](https://www.conf42.com/Golang_2025_Manuel_de_la_Pena_testing_go_integration).

## From Docker

Docker sponsored Conf42 Golang 2025 and maintains Testcontainers.

- [Docker](https://www.docker.com/)
- [Testcontainers](https://testcontainers.com/)
- [Testcontainers for Go docs](https://golang.testcontainers.org/)

[Watch the talk on YouTube](https://youtu.be/VsiaUdMes3k).

## Watch the talk

[Delightful integration tests in Go applications](https://www.conf42.com/Golang_2025_Manuel_de_la_Pena_testing_go_integration) at Conf42 Golang 2025.
