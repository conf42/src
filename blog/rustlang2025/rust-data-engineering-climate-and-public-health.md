# Rust data pipelines for climate monitoring and public health

Conf42 Blog, 2025-08-01, updated 2026-11-09. https://www.conf42.com/blog/rustlang2025/rust-data-engineering-climate-and-public-health

In short: Ritesh Kumar Sinha of Kotak Mahindra Bank at Conf42 Rustlang 2025 on Rust data engineering with Tokio, Arrow and DataFusion, applied to climate and health data.

Ritesh Kumar Sinha, AVP at Kotak Mahindra Bank, used his Conf42 Rustlang 2025 talk to argue that Rust's value in data engineering goes beyond speed: predictable pipelines matter most where the data is about satellites watching forests or hospitals tracking an epidemic. The tools are Tokio, Apache Arrow and DataFusion; the examples are climate monitoring and public health.

It is a short talk, well under twenty minutes of material, and best treated as an introduction to the Rust data stack with a clear sense of why it matters.

## The problem: big pipelines, unpredictable runtimes

Ritesh opened with the scale of data the world now produces and the failure modes of the usual tools at that scale: garbage collection making Java pipelines unpredictable, memory leaks risking corruption, Python slowing down. His summary is that petabyte processing needs a rethink for safety and scale, and Rust offers low-level performance with high-level safety.

He added a personal note that will ring true for anyone who has maintained native code: he has seen teams spend weeks on memory issues in C++, which Rust's compiler would have rejected up front.

## The borrow checker as a strict librarian

His explanation of ownership is the friendliest line in the talk: it is like a strict librarian. You can borrow the book, but you cannot keep it forever or lend it out twice. For data pipelines this matters because it makes data flows explicit, so it is always clear which stage owns a buffer, and corruption from two stages writing the same memory simply does not compile.

## The stack, from bytes to SQL

Ritesh walked through three code examples that together sketch a pipeline:

- **Tokio** for async ingestion: read lines without blocking, parse the stream with minimal copying, transform in parallel without locks, then serialize safely to the sink while reusing buffers.
- **Apache Arrow** for zero-copy columnar batches, fast aggregations, and interop with Python for mixed-language teams.
- **DataFusion** for SQL: register a CSV, run an average-temperature query with filters, and get vectorized execution over Arrow data.

He also showed an atomic, lock-free counter for shared metrics, the kind of small detail that keeps a hot loop free of mutex contention.

## Two case studies with a purpose

The first is climate monitoring: terabytes of satellite data arriving at remote sites with limited hardware, processed by efficient Rust pipelines at the edge, for uses like tracking deforestation in near real time. The second is public health: national-scale data for epidemic tracking, where Ritesh stressed memory safety and privacy enforced at compile time and fast queries over very large record sets during a crisis.

The figures he gave for both, along with headline numbers like large throughput gains over JVM tools and big compute savings, are presented without methodology, so take them as the speaker's reported results.

## Fast, safe, and cheaper on the planet

Ritesh closed on an angle few data talks take: efficiency as ethics. Lower compute per record means lower energy use and lower carbon, ownership boundaries help enforce privacy, and efficient processing leaves headroom for bias checks in ML pipelines. His call to action is modest and sensible: try a Rust pipeline in one small part of your next project.

## Who should watch

Data engineers new to Rust who want a quick tour of Tokio, Arrow and DataFusion, and anyone working on environmental or health data who wants the case for predictable pipelines. If you already ship DataFusion in production, this is a refresher.

## Related Conf42 talks

- [EpiRust: an ultra large-scale epidemic simulator in Rust](https://www.conf42.com/Rustlang_2022_Jayanta_Kshirsagar_Sapana_Kale_epirust_ultra_largescale_epidemic_simulator) by Jayanta Kshirsagar and Sapana Kale: Rust applied to epidemics, in depth.
- [Using Rust for Numerical Applications](https://www.conf42.com/Rustlang_2023_Felipe_Zapata_numerical_applications) by Felipe Zapata: the scientific-computing side.
- [Managing AWS streaming data pipelines at scale](https://www.conf42.com/Cloud_Native_2024_Akshay_Jain_aws_streaming_pipeline) by Akshay Jain: operating the pipeline once it is built.

[Watch Ritesh Kumar Sinha's talk](https://www.conf42.com/Rustlang_2025_Ritesh_Kumar_Sinha_memory_safety_zero)

[Watch the talk on YouTube](https://youtu.be/fohPVZ_Asoc).

## Watch the talk

[Rust-Powered Data Engineering: Building Performance-Critical Systems for Global Impact](https://www.conf42.com/Rustlang_2025_Ritesh_Kumar_Sinha_memory_safety_zero) at Conf42 Rustlang 2025.
