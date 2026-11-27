# Supply chain digital twins in Rust, and why predictable beats fast

Conf42 Blog, 2025-08-21, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/supply-chain-digital-twins-rust-predictable-routes

In short: Shikha Duttyal of Meta at Conf42 Rustlang 2025 on digital twins, variance-based route optimization and a Rust infrastructure built for always-on monitoring.

The fastest shipping route is not always the best one; the most predictable one often is. That is the idea at the centre of Shikha Duttyal's talk at Conf42 Rustlang 2025. Shikha, a Supply Chain Solutions Program Manager at Meta, walked through digital twins for supply chains, variance-based route optimization, and why the engine underneath was built in Rust.

This is a talk from the operations side of the house. It speaks the language of inventory, safety stock and payback periods, with Rust appearing as the infrastructure choice that makes the twin trustworthy enough to run for months.

## A digital twin is a control tower that can simulate

Shikha drew a line between the traditional supply chain control tower, which mostly shows historical data on a dashboard, and a digital twin: a live virtual replica of the physical network that you can run scenarios against. Test a new product launch or a supplier change in the twin, find the bottleneck there, and only then commit trucks and contracts.

She listed the gains organizations report from this: faster launches, constraints found before they cost money, and better resource utilization from continuous automated scenario planning. The figures she quoted are industry results and case-study numbers rather than a benchmark she ran live, so treat them as direction, not a promise.

## Optimise for variance, not just the average

The sharpest section is the maritime routing case study. Traditional route optimization asks for the fastest or the cheapest path. Shikha's argument is that what planners actually need is the route that arrives in the most predictable time, every time.

The logic is tidy. A route with low transit variance makes arrival estimates accurate, accurate estimates make inventory planning precise, and precise planning lets you carry less expensive safety stock. In her example, the algorithms found lanes with much lower variance than others with similar average transit times, and a Fortune 500 manufacturer turned that into savings by cutting safety stock. Anyone who has padded an SLA to cover a flaky dependency will recognize the pattern: the p99 drives the buffer, not the mean.

## Where Rust earns its place

Supply chain monitoring applications run for months or years without a restart, so Shikha led with memory safety: the ownership model rules out the slow leaks that make long-running services degrade. Her code examples were small and illustrative. A function that takes ownership of a container record frees it when done, with no use-after-free possible. A `RouteOptimizer` trait lets you swap a variance-based optimizer for another implementation with static dispatch and no runtime cost.

She also pointed at fearless concurrency for high-velocity IoT streams and at WebAssembly as a way to run the same Rust code from low-power shipping sensors up to cloud servers. Her description of the organizational pattern is one many teams will recognize: Python for exploration and data science, Rust for the production services where failure is not acceptable.

## The second case study, and the roadmap

A global shipping company with a fleet of container vessels ran a twin on Rust-based edge computing, monitoring more than 1,200 parameters per vessel. Shikha highlighted a small memory footprint and efficient compression that cut satellite transmission costs, which matters when your bandwidth bill is priced per byte from mid-ocean.

The talk closes with an 18-month, four-phase roadmap: foundation and pilot choice, a first limited twin on ERP and WMS data, expansion with IoT sensors and a control tower, then optimization with ML and partner integration. She stressed change management as one of the three pillars, next to data integration and algorithms.

## Who should watch

Engineers building logistics or operations platforms, and technical leads who need to explain a Rust investment in business terms. If you want deep Rust internals, this is not that talk; it is about why the language choice matters to the outcome.

## Related Conf42 talks

- [AI-Powered Digital Twins for Smart Manufacturing](https://www.conf42.com/Cloud_Native_2025_Vinoth_Manamala_digital_twins_manufacturing) by Vinoth Manamala: the same idea on the factory floor.
- [Strengthening Supply Chains with Collaborative Forecasting](https://www.conf42.com/Golang_2025_Madhusudan_S_Vadigicherla_supply_chain_forecasting) by Madhusudan S Vadigicherla: the information-visibility side of the problem.
- [Last-mile delivery with cloud computing and IoT](https://www.conf42.com/Cloud_Native_2025_Maimoon_Saleem_logistics_optimization_efficiency) by Maimoon Saleem: where the route ends.

[Watch Shikha Duttyal's talk](https://www.conf42.com/Rustlang_2025_Shikha_Duttyal_ml_ai_rust)

[Watch the talk on YouTube](https://youtu.be/p2uT7ED2N3o).

## Watch the talk

[Transforming Supply Chain Performance Through Digital Twin Technology, Advanced Route Optimization & Rust-Powered Infrastructure](https://www.conf42.com/Rustlang_2025_Shikha_Duttyal_ml_ai_rust) at Conf42 Rustlang 2025.
