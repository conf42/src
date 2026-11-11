# 5,000 serverless apps on one Kubernetes node is a WebAssembly argument

Conf42 Blog, 2024-03-21. https://www.conf42.com/cloud2024/webassembly-serverless-density-cold-starts

In short: Sohan Maheshwar (Fermyon) at Conf42 Cloud Native 2024 on why serverless WebAssembly beats containers and microVMs on density and cold starts

Cold starts and idle containers are both density problems, and WebAssembly attacks both. At Conf42 Cloud Native 2024, [Sohan Maheshwar](https://www.conf42.com/Cloud_Native_2024_Sohan_Maheshwar_future_cloud_webassembly), Developer Relations Lead at Fermyon and formerly at AWS, argued that the next wave of cloud compute is serverless WebAssembly: functions that start in under a millisecond, pack thousands to a node, and run on any architecture, built with the open-source Spin framework.

The talk is a good first look at Wasm on the server, with a live Spin demo and a comparison against Firecracker microVMs, and it ends on Fermyon's SpinKube and its commercial Kubernetes platform.

## What is wrong with containers and serverless today?

He names three problems. Containers are provisioned for peak load, so they mostly sit idle, burning money and electricity; he cited an Andreessen Horowitz estimate of about 100 billion dollars of market value lost to this. Configuration keeps growing with every dependency. And serverless has cold starts, which teams pay to work around by keeping instances warm.

For an outside opinion he quotes Docker founder Solomon Hykes, who tweeted that if Wasm and WASI had existed in 2008, there would have been no need to create Docker.

## What is WebAssembly, minus the hype?

The boring answer, as he puts it, is that it is just another bytecode format: a portable compilation target, built in the mid-2010s by browser vendors including Mozilla. Compile from many languages to a Wasm module and run it in any Wasm runtime (Wasmtime is the most popular) on any OS or architecture, from Kubernetes to a Raspberry Pi. Think JVM, minus the single language.

Two properties matter for servers. Wasm is sandboxed by default, so a module gets nothing until you grant it, the reverse of how most code runs. And WASI, the WebAssembly System Interface, adds files, clocks, random numbers and networking outside the browser while keeping that sandbox around I/O.

## How fast is the Spin workflow?

Spin is Fermyon's open-source framework for serverless Wasm apps, with 15+ languages and 4.6K GitHub stars at the time. The demo was four commands: `spin new` (picking an HTTP or Redis trigger, with community triggers for MQTT and SQS, then a language, Rust here), `spin build`, `spin up` to test locally with curl, and `spin deploy` to push to Fermyon Cloud.

The application manifest is TOML and maps routes to components, and each component can be written in a different language, so one route of a calculator in Python and another in JavaScript works. The manifest is also where capabilities live: a module may only call an HTTP host listed in its allowed outbound hosts.

## Why does it suit serverless so well?

He gave four reasons, with numbers from his slides:

- **Binary size**: a Rust hello world is about 2 MB, about 300 KB compiled ahead of time; the demo's HTTP API was about 2.3 MB JIT and 1.1 MB AOT.
- **Startup time**: comparable to native code, only 2.3x slower in the benchmark he cited.
- **Portability**: the same build runs across operating systems and architectures.
- **Security**: a capability-based sandbox.

The bigger argument is multitenancy. Borrowing from Marc Brooker, a system's value is set by long-term average traffic and its cost by short-term peak traffic, so the more tenants you can safely pack onto the hardware, the closer cost gets to value. VMs packed a few apps, containers more, Wasm functions far more. His analogy: gas, liquid, solid.

## How does it compare with Firecracker?

He uses the characteristics of an ideal serverless unit from the Firecracker paper (Agache et al., 2020), the microVM behind AWS Lambda. Isolation and performance come out even: both are sandboxed and near-native. Wasm wins in two places. Density: thousands of functions per node needed a 48-core, 382 GB RAM, 3,360 GB disk machine for microVMs, against 8 cores, 32 GB RAM and 100 GB disk for Wasm. And fast switching: about 125 ms from startup to cleanup for a microVM, under 1 ms for Wasm. He was candid that soft allocation (overcommitting resources, which Lambda does at up to 10x) is still untested for Wasm.

## What about Kubernetes?

SpinKube, launched just before the talk, is an open-source project with contributions from Microsoft, Liquid Reply, SUSE and Fermyon. It combines a containerd shim for Spin, a runtime class manager, a Spin operator that manages Spin apps as custom resources, and a Spin plugin that scaffolds the deployment YAML.

Fermyon's enterprise Fermyon Platform for Kubernetes pushes density further. Sohan Maheshwar said at Conf42 Cloud Native 2024: "You can actually run 5000 serverless apps in one Kubernetes node." A prerecorded demo showed 5,000 apps on an Azure Kubernetes cluster answering with sub-millisecond cold starts, which his slides put at 50x workload density.

When will this go mainstream? His answer was "gradually and then suddenly", noting that 2023 was the year of WebAssembly that didn't quite happen.

## Who should watch?

Platform and serverless engineers tired of paying for warm instances or idle pods who want the case for server-side Wasm with real numbers.

## Related Conf42 talks

- Sohan Maheshwar on [building a serverless WebAssembly app in Python with Spin](https://www.conf42.com/Python_2024_Sohan_Maheshwar_serverless_webassembly_app_spin) at Conf42 Python 2024.
- Thorsten Hans of Fermyon on [going serverless with WebAssembly in Go](https://www.conf42.com/Golang_2024_Thorsten_Hans_serverless_webassembly) at Conf42 Golang 2024.
- Deepu K Sasidharan on [containerless Kubernetes with WebAssembly](https://www.conf42.com/Rustlang_2024_Deepu_K_Sasidharan_kubernetes_containerless_webassembly) at Conf42 Rustlang 2024.

[Watch Sohan Maheshwar's talk](https://www.conf42.com/Cloud_Native_2024_Sohan_Maheshwar_future_cloud_webassembly), part of [Conf42 Cloud Native 2024](https://www.conf42.com/cloud2024).

## From Fermyon

Fermyon builds Spin, the open-source framework for serverless WebAssembly apps, contributes to SpinKube, and runs Fermyon Cloud and Fermyon Platform for Kubernetes.

- [Fermyon developer site](https://developer.fermyon.com/)

[Watch the talk on YouTube](https://youtu.be/S8v1qg56GRo).

## Watch the talk

[The Future of the Cloud is WebAssembly](https://www.conf42.com/Cloud_Native_2024_Sohan_Maheshwar_future_cloud_webassembly) at Conf42 Cloud Native 2024.
