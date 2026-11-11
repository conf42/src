# Rolling back a distributed saga from inside an Envoy filter

Conf42 Blog, 2022-04-28. https://www.conf42.com/blog/cloud2022/saga-rollback-inside-envoy-filter

In short: Alparslan Avci (Zapata Computing) at Conf42 Cloud Native 2022 on running saga compensation in an Istio Envoy filter, with Hazelcast holding the state

Your banking service throws a 500, and the product service has already decremented stock while the user service has already spent the customer's credits. Alparslan Avci, Software Developer at Zapata Computing, used his Conf42 Cloud Native 2022 talk to show that dual write problem live, then fix it without touching application code: an Envoy filter in the Istio sidecar notices the failure and triggers saga compensation, with transaction state kept in a Hazelcast cluster.

He is upfront that it is an experiment rather than a product. In his own words at the end, the solution is not production ready yet. What it shows well is how much a service mesh can do between services.

## Why do microservices end up with distributed transactions?

His setup is a large e-commerce business with hundreds of engineers, many teams and thousands of transactions a day. That organisation lands on microservices, in Docker containers on Kubernetes, and as the number of services grows, on a service mesh to take over east-west traffic: routing, security, observability. He names Istio, Consul and Linkerd as the top three and uses Istio.

Then a purchase has to touch the user, product and banking services, each with its own database, inside one transaction boundary.

"So since you are running in a distributed environment, prepare yourself to distribute transactions," Alparslan Avci said at Conf42 Cloud Native 2022.

## What does the dual write problem look like?

The demo makes it concrete. A single product with a stock of 10, a user with 10,000 pounds of credits, and a banking service rigged to fail. He buys three, paying partly from credits and partly from the bank account. The bank call returns an internal server error, and afterwards the stock reads 7 and the credits read 7,000. Nothing was bought, but two services committed their half anyway.

## Two-phase commit or saga?

He compares the two usual fixes.

**Two-phase commit** brings local transaction semantics to a distributed system: a coordinator asks every service to prepare, and commits only if all say yes, otherwise it tells the rest to roll back. You get strong consistency and read-write isolation. You also get blocking (nobody else can touch those records meanwhile), a requirement for XA-compatible data sources, scalability limits, and a coordinator that is a single point of failure.

**Distributed sagas** fit microservices better. Each service runs its own local transaction, and when one fails it triggers the compensation actions of the services that already succeeded. A compensation is not a real rollback but logic that semantically undoes the change. His travel example: plan the meeting, book the flight, book the hotel, book transport; the hotel fails, so it cancels the flight, which cancels the meeting. Sagas can be orchestrated (a central orchestrator) or choreographed (services react to events). They are asynchronous, scale, work across heterogeneous components and need no XA. The costs are eventual consistency with possible stale reads, no read-write isolation, and a compensation function you must write for every action, plus handling for when compensation itself fails.

## How does the mesh run the saga?

The trick is Envoy's HTTP filter chain. Since every call between pods goes through the Envoy sidecar, a filter there sees every request and response. He deploys a three-replica Hazelcast cluster and a small three-replica coordinator app that stores transaction data in it, then applies an Istio EnvoyFilter custom resource written in Lua, with two functions:

- **On request:** read the transaction ID from the headers and record the call with the coordinator app.
- **On response:** check the HTTP status. On a failure, fetch the transaction's details from the coordinator app (and so from Hazelcast) and call the compensation endpoint of every service that took part.

He reruns the purchase without redeploying the application, only with the filter applied. The bank fails again with a 500, and this time the stock stays at 7 and the credits stay at 7,000. Kiali, Istio's console, shows the calls: the banking service's failure leads to compensation calls on the user and product services.

## Who should watch

Engineers who know the saga pattern on paper and want to see it wired up end to end, and anyone curious how far Envoy filters can go beyond routing. Treat it as a design sketch: each service still needs its own compensation endpoint, and the open issues he mentions are real.

## Related Conf42 talks

- Dmitry Khorev on [the saga pattern for distributed transactions](https://www.conf42.com/Cloud_Native_2023_Dmitry_Khorev_saga_pattern_distributed_transactions) at Conf42 Cloud Native 2023.
- Nicolas Frankel on [migrating an app to the cloud with Quarkus, Kotlin, Hazelcast and GraalVM](https://www.conf42.com/Cloud_Native_2021_Nicolas_Frankel_app_migration_cloud_quarkus_kotlin_hazelcast_graalvm) at Conf42 Cloud Native 2021.
- Gufran Mirza on [securing Kubernetes with the Istio service mesh](https://www.conf42.com/DevSecOps_2023_Gufran_Mirza_securing_kubernetes_istio_service_mesh) at Conf42 DevSecOps 2023.

[Watch Alparslan Avci's talk](https://www.conf42.com/Cloud_Native_2022_Alparslan_Avci_distributed_transactions_service_mesh)

## From Zapata Computing

Avci works on the platform team at Zapata Computing, building the cloud-native backend applications behind the company's quantum computing work.

- Zapata Computing: [zapatacomputing.com](http://zapatacomputing.com)

[Watch the talk on YouTube](https://youtu.be/cD08bviNSt0).

## Watch the talk

[Distributed Transactions in Service Mesh](https://www.conf42.com/Cloud_Native_2022_Alparslan_Avci_distributed_transactions_service_mesh) at Conf42 Cloud Native 2022.
