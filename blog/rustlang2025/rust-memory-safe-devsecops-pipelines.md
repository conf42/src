# Your security scanner is attack surface too, so write it in Rust

Conf42 Blog, 2025-08-21. https://www.conf42.com/blog/rustlang2025/rust-memory-safe-devsecops-pipelines

In short: Naresh Yelkoti of U.S. Bank at Conf42 Rustlang 2025 on Rust container scanners, artifact signing and policy engines for memory-safe DevSecOps.

Security tools parse the most hostile input your pipeline sees: container layers, packages and configs pulled from strangers. At Conf42 Rustlang 2025, [Naresh Yelkoti](https://www.conf42.com/Rustlang_2025_Naresh_Yelkoti_memory_security_cloud), a senior information security engineer at U.S. Bank, pointed out that many of those tools are written in C and C++, "which means the tools designed to protect us can introduce new vulnerabilities". His answer is to build the scanners, signers and policy engines in Rust.

Yelkoti has run security pipelines across AWS, Azure and GCP and led migrations from Prisma Cloud to newer platforms, so the talk is grounded in what actually sits in a CI pipeline.

## A scanner is a parser of untrusted input

The core argument: if your container scanner has a buffer overflow, a crafted image can exploit the very tool inspecting it. Rust's ownership, borrowing and lifetime rules remove whole classes of parser and concurrency bugs at compile time, so the tool stops being a new attack vector.

He cites the industry baseline that around 70% of Microsoft's CVEs come from memory safety bugs, and reports from one financial services firm he worked with that its vulnerability backlog dropped by 30% in three months after adding Rust-based scanning.

## What a Rust container scanner looks like

The container section is the most detailed. Traditional scanners extract each image layer, compare installed packages against NVD and vendor advisories, and are often slow and noisy. The Rust design uses three ideas:

- **Zero-copy parsing** of layers straight from disk, without duplicating data in memory.
- **Parallel scanning** with Rayon across images.
- **Async reporting** with Tokio, so pushing results to dashboards never blocks the scan.

In his pipeline, a developer push builds the image, the Rust scanner runs before the image reaches the registry, critical findings block the deploy and go to ServiceNow or Slack, and only clean images are pushed. He also covers secret detection and flagging end-of-life base images.

## Signing, policies and static analysis

Beyond scanning, he walks through three more Rust-built tools. Static analysis on top of the syn and proc-macro2 crates to block insecure patterns such as SQL injection at commit time. Artifact signing and verification with ring and rustls, avoiding OpenSSL pitfalls and time-of-check to time-of-use gaps. And policy engines compiled to WebAssembly for sandboxed execution, with policies hot-swapped without restarts, for example a Kubernetes rule that only signed images may deploy.

His performance claims (three to ten times faster scans than Go or Python tools, 60% less memory, fewer false positives) lean on public reports from Dropbox, Discord and Cloudflare rather than his own benchmarks, and the talk is slide-driven rather than a live demo.

## Start with cargo audit

The integration advice is incremental: pre-commit hooks, GitLab CI jobs, Kubernetes admission controllers and API gateway middleware, no rewrite required. His suggested first step is the boring one, dependency scanning with cargo audit, then grow from there.

## Who should watch

DevSecOps and platform security engineers who maintain scanning and policy tooling, and anyone choosing a language for an internal security tool. If you already ship Rust, the container scanner design is the section to watch.

## Related Conf42 talks

- [Supply Chain Defense by Default: SBOMs, SLSA, and Provenance in CI/CD](https://www.conf42.com/DevSecOps_2025_Bhaskar_Bharat_Sawant_supply_chain_ci) by Bhaskar Bharat Sawant (Cornerstone Building Brands) at Conf42 DevSecOps 2025.
- [Securing the software supply chain: beyond SBOM](https://www.conf42.com/DevSecOps_2023_Marek_Najmajer_Aleksander_Baranowski_beyond_sbom_risk_assessment) by Marek Najmajer and Aleksander Baranowski (Linux Polska) at Conf42 DevSecOps 2023.
- [SBB - Secure Building Blocks](https://www.conf42.com/Rustlang_2023_Yashwanth_Singh_M_sbb_secure_building_blocks) by Yashwanth Singh M (Bosch Global Software Technologies) at Conf42 Rustlang 2023.

[Watch Naresh Yelkoti's talk](https://www.conf42.com/Rustlang_2025_Naresh_Yelkoti_memory_security_cloud) or the [YouTube recording](https://youtu.be/16Tc0QrLz-I).

## Watch the talk

[Rust-Powered Security Pipelines: Building Memory-Safe DevSecOps at Enterprise Scale](https://www.conf42.com/Rustlang_2025_Naresh_Yelkoti_memory_security_cloud) at Conf42 Rustlang 2025.
