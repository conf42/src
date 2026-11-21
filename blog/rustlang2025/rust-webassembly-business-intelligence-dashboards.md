# Keep React, move the math, Rust and WebAssembly for BI dashboards

Conf42 Blog, 2025-08-11. https://www.conf42.com/blog/rustlang2025/rust-webassembly-business-intelligence-dashboards

In short: Shahzeb Akhtar of UnitedLex at Conf42 Rustlang 2025 on fast BI dashboards, with heavy computation in Rust compiled to WebAssembly and the UI left in JavaScript.

Everyone has opened a dashboard and watched it think. At Conf42 Rustlang 2025, [Shahzeb Akhtar](https://www.conf42.com/Rustlang_2025_Shahzeb_Akhtar_memory_security_rust), Director of IP Strategy and Technology at UnitedLex, argued that the fix is not a new frontend framework: keep React or Vue for rendering and move the aggregation, filtering and heavy calculations into Rust compiled to WebAssembly.

Akhtar leads the IP data science team behind Vantage for IP, a patent intelligence platform that runs natural language processing over very large patent collections, so dashboards that crunch a lot of data in the browser are his day job.

## Why dashboards are slow

His diagnosis has three parts. Heavy data processing done in JavaScript leads to slow rendering. JavaScript's dynamic nature, and untrusted code running in the browser, widen the attack surface. And inefficient code with frequent data transfers wastes CPU on both the client and the server.

## WebAssembly as a compilation target

He spends a moment on what WebAssembly actually is, which is useful if you have only heard the name. It is not a language but a low-level binary format for a stack-based virtual machine. "Think of it as the assembly language of the web." Modules run close to native speed in a sandbox, so a buggy or malicious module cannot reach the rest of the page.

## Rewrite only the hot path

The workflow is deliberately selective:

1. Identify the performance-critical parts of the dashboard and write only those in Rust.
2. Compile to a `.wasm` module plus the JavaScript glue, with wasm-bindgen handling the calls between the two.
3. Import the module from the existing frontend like any other library.
4. Keep rendering in your existing UI framework.

He maps this onto three layers: a data layer (SQLx for database access, Polars for data frames), a processing layer (Rayon for parallelism, ndarray for numerics) and a visualization layer. For charts in Rust he lists Plotters, Charming (a Rust API over Apache ECharts) and Plotly, plus Tauri for desktop apps.

## The evidence he picked

Akhtar's examples are public ones rather than his own benchmarks. Figma rewrote its multiplayer engine in Rust and reported a 3.8x reduction in memory and 6x reduction in CPU usage; he admits it is not a dashboard, but the real-time sync problem is similar. A graph visualization of related Spotify artists went from under 10 frames per second to 60 after moving its calculations to Rust and WebAssembly. And Databento uses Polars, which he cited as outperforming pandas by 8 to 15x on benchmarks.

## Fast and useless is still useless

The second half is a reminder that performance is not the product. His design principles: know your audience (a CEO and an analyst need different dashboards), keep it simple, provide context through benchmarks and targets, use visual hierarchy, allow customization and drill-down, choose the right chart type, and design for colour blindness, keyboards and screen readers. He closes with a chart-selection infographic as bonus material.

## Who should watch

Frontend and data engineers whose dashboards stall on client-side computation, and teams wondering whether WebAssembly is worth the build complexity. If you already ship Rust to the browser, the design half is the part with new material.

## Related Conf42 talks

- [Beyond Static Dashboards: How Rust-Powered Dynamic UIs Transform Cloud Infrastructure Management](https://www.conf42.com/Remix_2026_Tashi_Garg_cloud_ai_rust) by Tashi Garg (Juniper Networks) at Conf42 Remix 2026.
- [Using Rust and WASM](https://www.conf42.com/Rustlang_2024_Andrey_Makarov_wasm_assembly_code_web) by Andrey Makarov (Islamic Coin) at Conf42 Rustlang 2024.
- [Building Adaptive Web Components with Rust](https://www.conf42.com/Rustlang_2024_Nitish_Mehrotra_web_adaptive_components_design) by Nitish Mehrotra (Meta) at Conf42 Rustlang 2024.

[Watch Shahzeb Akhtar's talk](https://www.conf42.com/Rustlang_2025_Shahzeb_Akhtar_memory_security_rust) or the [YouTube recording](https://youtu.be/EZQjOx1ZwYE).

## Watch the talk

[Rust-Powered Business Intelligence: Building High-Performance User-Centric Dashboard](https://www.conf42.com/Rustlang_2025_Shahzeb_Akhtar_memory_security_rust) at Conf42 Rustlang 2025.
