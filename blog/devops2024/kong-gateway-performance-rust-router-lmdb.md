# How Kong made its gateway faster, and how it proves it every day

Conf42 Blog, 2024-01-25. https://www.conf42.com/blog/devops2024/kong-gateway-performance-rust-router-lmdb

In short: Wenchao Xiang (Kong) at Conf42 DevOps 2024 on Kong Gateway's Rust router, LMDB config store, plugin fixes and daily performance tests

At 10,000 routes, the router stops being a detail and becomes the gateway. At Conf42 DevOps 2024, [Wenchao Xiang](https://www.conf42.com/DevOps_2024_Wenchao_Xiang_kong_gateway_performance_enhancement), Senior Software Engineer at Kong, walked through the performance work behind recent Kong Gateway releases: a router rewritten in Rust, configuration moved to LMDB, a new event library for NGINX workers, plugin fixes for Prometheus and rate limiting, and the bare-metal test rig that catches regressions daily.

Every benchmark here is Kong measuring Kong, but the methods are worth copying.

## What changed in the plugins?

**Prometheus.** The plugin did fine with a few routes and slowed as route counts grew. The 3.4 release sped up metric scraping and cut high-cardinality metrics, and the slides credit three fixes: a table pool so scraping stops creating temporary Lua tables all the time, yields inside long loops so one scrape does not hog the CPU and stall request processing, and replacing functions LuaJIT could not compile (the NYI ones) so the plugin runs on the JIT. The talk showed a clear p99 latency drop from 3.3 to 3.4.

**Rate limiting.** With counters in external storage such as Redis, the old plugin talked to the store on every request. The new batch queue in 3.4 lets the plugin write counters to an in-memory queue and flush them asynchronously, with a new `sync_rate` setting to control how often. In Kong's comparison against an unnamed Go-based open-source gateway, p99 and RPS came out nearly twice as good.

## Why rewrite the router in Rust?

Almost every request passes through the router, so it is the hottest code in a gateway. Since version 3.0 Kong has shipped the ATC router, a DSL-based design where routes are written as expressions, which he says gives more flexibility and better performance without losing readability on large configurations. It is written in Rust for C-like speed with safer memory handling, which was not easy given that Rust is not natively supported in OpenResty.

He reported p99 latency in testing with 10,000 routes dropping from 1.5 seconds to 0.1 seconds. Two more changes help: a cheaper router rebuild, which per the slides cut worst-case rebuild latency from 20 seconds to 5 with 10,000 routes, and conditional rebuilds from 3.0 that only rebuild when routes have actually changed.

## What replaced shared memory?

Kong runs on NGINX and OpenResty, with a master process forking isolated workers. Two things used to live in NGINX shared memory, and both changed.

- **Configuration** moved to LMDB in 3.0. Shared memory used too much memory and was not transactional, so keeping data consistent meant extra code. LMDB, a transactional embedded key-value store, cut memory use and improved RPS while configuration was being pushed constantly, with a further 50% to 70% drop in rebuild time, especially with many workers.
- **Events between workers**, used for things like router rebuilds and health checks, moved to lua-resty-events, a publish-subscribe library in pure Lua. The old shared-memory version needed a lock for every access and a size fixed at startup. In tests posting 1,000 events every 5 ms and 10,000 events every 100 ms, the two libraries tied at low load and the new one won as load increased.

## How does Kong catch performance regressions?

This is the section to steal. The rig is two bare-metal machines on a private network, one generating load with wrk and one running Kong. Upstream and gateway sit on the loopback so wrk gets the network bandwidth, the NIC interrupts, upstream and gateway are pinned to separate CPU cores, and turbo boost is disabled so numbers stay stable.

Each test suite collects at least 100 samples, and RPS, latency and memory are compared by mean, median and standard deviation and by their PDF and CDF. Results from release tests and daily runs go into the same storage, and the daily run is compared against the baseline. Wenchao Xiang said at Conf42 DevOps 2024: "We do the test every day and if the difference happens the test is considered a failure and we will get a notification about it." When that happens, the team runs perf, reads the flame graph to find the guilty function, fixes it and reruns perf to confirm.

## What can you tune yourself?

Large payloads are the common exception to Kong's out-of-the-box tuning. A request body bigger than the buffer spills to disk, and disk I/O can block the NGINX event loop. Raising the request buffer size above the default helps, and so does the response buffer for large upstream responses. Do not turn buffering on for real-time traffic, long-lived or streaming connections, line-by-line processing, or memory-limited environments.

## Who should watch?

Teams running Kong at scale, and anyone building a performance regression pipeline for a proxy or gateway. The tuning section is short; the methodology is the reason to watch.

## Related Conf42 talks

- Roman Rastiehaiev's [comparison of open-source API gateways](https://www.conf42.com/Cloud_Native_2025_Roman_Rastiehaiev_api_gateways_comparison) at Conf42 Cloud Native 2025.
- Bobur Umurzokov on [observing your API with API gateway plugins](https://www.conf42.com/Observability_2023_Bobur_Umurzokov_api_gateway_plugins) at Conf42 Observability 2023.
- Adelina Simion and Andy Kuszyk on [load testing with F1](https://www.conf42.com/Golang_2022_Adelina_Simion_Andy_Kuszyk_load_testing_f1) at Conf42 Golang 2022.

[Watch Wenchao Xiang's talk](https://www.conf42.com/DevOps_2024_Wenchao_Xiang_kong_gateway_performance_enhancement), part of [Conf42 DevOps 2024](https://www.conf42.com/devops2024).

## From Kong

Kong makes Kong Gateway, an open-source API gateway with plugins for authentication, traffic control, transformation, logging and monitoring, plus enterprise editions and Kong Konnect, a hosted control plane for gateways and ingress controllers.

- [Kong website](https://konghq.com/)

[Watch the talk on YouTube](https://youtu.be/K8RtsZE6A0A).

## Watch the talk

[Elevating Excellence of Kong Gateway: Performance Enhancement and Best Practices](https://www.conf42.com/DevOps_2024_Wenchao_Xiang_kong_gateway_performance_enhancement) at Conf42 DevOps 2024.
