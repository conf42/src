# Skip both lift-and-shift and the rewrite, recompile your Java instead

Conf42 Blog, 2021-04-28. https://www.conf42.com/blog/cloud2021/middle-path-java-cloud-migration-quarkus

In short: Nicolas Frankel (Hazelcast) at Conf42 Cloud Native 2021 on migrating a legacy JAX-RS app to the cloud with Quarkus and a GraalVM native image

Nicolas Frankel, Developer Advocate at Hazelcast, argued at Conf42 Cloud Native 2021 that a legacy JVM web app has two bad routes to the cloud and one sensible one. Lift and shift wastes money on an app that was never built for metered resources; a rewrite costs millions and chases a moving target. The middle path keeps your existing annotated code and swaps the engine underneath, here Quarkus compiled to a GraalVM native executable, with a Kotlin URL shortener backed by Hazelcast as the demo.

## Why migrate at all?

Frankel's good reasons are visibility, flexibility and a low barrier to entry. On-premise costs are a best guess built from contracts and spreadsheets; a cloud bill breaks down exactly what each service used. Owned hardware is sized for Black Friday and wasted the rest of the year. And a solo developer with a good idea can start on day one without buying servers.

The bad reason is doing it because everyone else is, and he is blunt about the money. Expecting the cloud to save you money, or at least waste less, is where he draws the line. "That's probably a very wrong assumption, and please be aware of that," Nicolas Frankel said at Conf42 Cloud Native 2021.

## Why does a classic JVM app fit the cloud badly?

He scores a standard JVM web application against the twelve-factor app and it fails on several counts. A WAR expects an application server it never declares; even a self-contained JAR with embedded Tomcat silently depends on a JVM of some minimum version. Configuration lives in each environment's application server, where a virtual data source name is mapped to the real one. Logs go to several files written by the app and the servlet container, not one stream.

The big one is startup. Kubernetes assumes a killed pod's replacement starts quickly, and the JVM starts slowly, then runs slowly until it warms up. Frameworks such as Spring and Java EE make it worse with reflection and classpath scanning for annotations at boot. On-premise that waste didn't matter much. On the cloud, every CPU cycle and megabyte is on the bill.

## Why not just rewrite it?

Because the business will ask what competitive edge a feature-for-feature rewrite buys, and the honest answer is none. If you get the budget anyway, the legacy app keeps gaining features while you rebuild it, so you chase a moving target. The old code has had most of its bugs found; the new code hasn't. And you need extra people, usually contractors maintaining the legacy app, who then keep interrupting the team that knows it.

## How does GraalVM make the middle path work?

GraalVM is a bag of features: a JDK, polyglot support through the Truffle framework, and Substrate VM, which compiles existing bytecode ahead of time into a native executable. That last one is the migration tool. It has limits he lists plainly: reflection needs configuration files telling the compiler which classes to keep, there is no security manager, and you build per platform, macOS on macOS and Windows on Windows.

His trade-off table is fair to the JVM. Native executables use less memory and start fast. The JVM gives you write once, run anywhere and, after warm-up, can tune compiled code to the real workload, which kept it on par with C and C++. In the cloud, he concludes, the native side wins. Frameworks such as Micronaut and Quarkus use GraalVM and handle reflection differently; Micronaut, for example, generates dedicated classes at compile time.

## What did the demo show?

A URL shortener that trades CPU for storage: generate a random short link and store both mappings in a Hazelcast in-memory data grid. The legacy version is a Java EE WAR on Tomcat, written in Kotlin with JAX-RS annotations, talking to Hazelcast through the client JAR.

The migrated version keeps the JAX-RS code and replaces Tomcat with Quarkus and its Hazelcast client extension. In development it still runs on the JVM, so breakpoints and debugging work. For production, the Quarkus-generated native Dockerfile builds a single native binary, the slow step of the build, and Docker Compose runs it beside one Hazelcast node. The curl calls behave the same as before. His advice: reuse existing code, let a cloud native framework run it, and think about return on investment.

## Who should watch?

Java teams with a Java EE or Spring estate who have been told to move to Kubernetes and can't get a rewrite funded. It is a 101 on native images with a working demo; the demo code is public.

## Related Conf42 talks

- Elder Moraes on [getting Java code cloud native ready](https://www.conf42.com/Cloud_Native_2021_Elder_Moraes_java_code_cloud_native_ready) at Conf42 Cloud Native 2021.
- Frank Kriegl on [HotSpot, GraalVM and OpenJ9](https://www.conf42.com/Enterprise_Software_2021_Frank_Kriegl_hotspot_vm_graalvm_openj9) at Conf42 Enterprise Software 2021.
- JJ Asghar on [migrating a monolith to cloud native](https://www.conf42.com/Site_Reliability_Engineering_2021_JJ_Asghar_migrating_monolith_cloudnative_stumbling_blocks) at Conf42 SRE 2021.

[Watch Nicolas Frankel's talk](https://www.conf42.com/Cloud_Native_2021_Nicolas_Frankel_app_migration_cloud_quarkus_kotlin_hazelcast_graalvm), part of [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From Hazelcast

Hazelcast makes the in-memory data grid used as the demo's store, and Jet, its in-memory stream processing engine. Nicolas Frankel is a developer advocate there.

- [Hazelcast website](https://hazelcast.com)

[Watch the talk on YouTube](https://youtu.be/-0J5-_pCUs0).

## Watch the talk

[Pragmatic App Migration to the Cloud: Quarkus, Kotlin, Hazelcast and GraalVM in action](https://www.conf42.com/Cloud_Native_2021_Nicolas_Frankel_app_migration_cloud_quarkus_kotlin_hazelcast_graalvm) at Conf42 Cloud Native 2021.
