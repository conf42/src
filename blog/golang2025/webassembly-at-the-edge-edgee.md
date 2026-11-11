# Why WebAssembly fits the edge, and where Go stands with it

Conf42 Blog, 2025-04-03, updated 2026-11-09. https://www.conf42.com/blog/golang2025/webassembly-at-the-edge-edgee

In short: Alex Casalboni of Edgee at Conf42 Golang 2025 on how CDNs became compute platforms, why Wasm suits the edge, and Go's WASI support.

Code that runs before and after every HTTP request gets a budget of a few milliseconds, and that rules out most of the compute models we're used to. At Conf42 Golang 2025, [Alex Casalboni](https://www.conf42.com/Golang_2025_Alex_Casalboni_cloud_edge_webassembly), Developer Advocate at Edgee and previously six years at AWS, explained why WebAssembly is the runtime that fits that budget, how far Go's support has come, and how Edgee builds its edge platform on it.

It's a sponsor talk with a clear structure: history and fundamentals first, then Edgee's own architecture. The first part works as a solid primer on server-side Wasm even if you never touch Edgee.

## CDNs quietly became clouds

Alex's history lesson runs in two parallel tracks. On the cloud side: AWS from 2006, then virtual machines, then containers and Kubernetes, then serverless functions around 2014 and 2015. On the CDN side: companies as old as Akamai built for caching and DDoS protection, with limited custom logic through things like the Varnish Configuration Language.

Then, roughly between 2016 and 2019, the tracks crossed. Cloudflare Workers, Lambda@Edge, CloudFront Functions and Fastly Compute put code on hundreds of points of presence. Key-value stores, databases, queues and object storage followed. His conclusion is that many CDN providers have become cloud providers, and the line between edge and cloud keeps blurring.

## Why Wasm and the edge match

WebAssembly was announced in 2015, shipped in 2017 and became a W3C recommendation in 2019. Alex focuses on the server side, where WASI, the WebAssembly System Interface, gives modules controlled access to files, sockets, clocks and HTTP. He also mentions the well-known remark from Docker's founder that Wasm plus WASI would have made Docker unnecessary.

The edge brings hard constraints. You get less memory and CPU than a VM or container, and because the logic sits in the path of every request, it needs to finish in single-digit milliseconds. Alex puts the target at five to ten. Containers that take seconds to start and serverless functions with hundreds of milliseconds of cold start don't fit.

Wasm's properties line up with that: near-native performance, small binaries with fast initialisation, and sandboxing by default. A module can't make an HTTP call or touch the filesystem unless the host grants it. That last one matters most if you're a platform running other people's untrusted code.

## Go and WebAssembly, version by version

For Gophers, this is the most useful section. Go has had a `wasm` target since Go 1.11 in 2018, with JavaScript glue for browser use. WASI preview 1 support arrived as experimental in Go 1.21 in 2023. For WASI preview 2 and the component model, Alex points to TinyGo plus `wit-bindgen-go`, which generates Go bindings from WIT, the interface definition language for components. Edgee defines its own WIT interfaces so developers can write components against them.

He also flags Go 1.24's expanded support for exporting Go functions to a Wasm host, and Google Cloud's announcement in the same post that its Application Load Balancer accepts service extensions written in Wasm, custom logic right in the request path. For runtimes, he recommends Wasmtime from the Bytecode Alliance rather than reinventing the host.

## What Edgee built

Edgee's first product is data collection and web analytics. The idea is to take heavy client-side SDKs, he names Google Analytics, Segment and Amplitude, and run them as Wasm components at the edge before the page reaches the browser. The proxy runs on Fastly today, with other CDNs such as Cloudflare planned, and talks to backend services, currently on AWS Lambda, for work that can't happen at the edge yet.

Around that sits a component registry for publishing and sharing public or private Wasm components, and an Edgee CLI that scaffolds, builds, tests and pushes components in Go, Rust, Python, C# and TypeScript. The proxy, the CLI and the components are open source. A/B testing, feature flags and AI inference were on the roadmap he described.

## Who should watch

Go developers curious about WebAssembly outside the browser, and platform engineers deciding what belongs at the edge versus in a region. If you already ship Wasm in production, skip to the Go version notes and the Edgee architecture. If you don't, the first half explains the "why" better than most docs.

## Related Conf42 talks

- [Go-ing Serverless with WebAssembly](https://www.conf42.com/Golang_2024_Thorsten_Hans_serverless_webassembly) by Thorsten Hans (Fermyon).
- [Go Containerless on Kubernetes with WebAssembly and Rust](https://www.conf42.com/Rustlang_2024_Deepu_K_Sasidharan_kubernetes_containerless_webassembly) by Deepu K Sasidharan (Auth0).
- [Go to the Edge](https://www.conf42.com/Golang_2022_Liam_Hampton_to_the_edge) by Liam Hampton (Microsoft), an earlier Go take on edge deployments.

[Watch Alex Casalboni's talk](https://www.conf42.com/Golang_2025_Alex_Casalboni_cloud_edge_webassembly).

## From Edgee

Edgee sponsored Conf42 Golang 2025.

- [Edgee](https://www.edgee.cloud/)
- [Edgee documentation](https://www.edgee.cloud/docs)
- [Edgee on GitHub](https://github.com/edgee-cloud/edgee)

[Watch the talk on YouTube](https://youtu.be/tp61nlI8DDw).

## Watch the talk

[From Cloud to Edge computing - Unleashing the power of WebAssembly at the edge](https://www.conf42.com/Golang_2025_Alex_Casalboni_cloud_edge_webassembly) at Conf42 Golang 2025.
