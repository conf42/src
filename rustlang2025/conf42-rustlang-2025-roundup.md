# Conf42 Rustlang 2025: Rust leaves the systems niche

Conf42 Blog, 2025-08-22. https://www.conf42.com/rustlang2025/conf42-rustlang-2025-roundup

In short: Conf42 Rustlang 2025 roundup - Rust in data lakes, AWS Lambda, networks, 5G, factory vision, security pipelines and carbon-aware Kubernetes, in 27 talks.

Conf42 Rustlang 2025 ran online on August 21, 2025, with 27 talks, and the striking thing was who gave them. Very few speakers were compiler hackers or crate maintainers; most were data engineers, network engineers, security engineers, and architects at banks, carmakers, telcos, and retailers, explaining why Rust ended up in their production stack. The borrow checker has clearly left the systems programming niche and found a job in the enterprise.

All sessions are on the [Conf42 Rustlang 2025 event page](https://www.conf42.com/rustlang2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrBMebMWQQ03iUNjed9luMsp).

## Rust under the data stack

Data infrastructure was the most convincing track. [Rahul Joshi](https://www.conf42.com/Rustlang_2025_Rahul_Joshi_memory_rust_tech), a Distinguished Data Engineer at Capital One, walked through three eras of enterprise data: on-prem Hadoop with its JVM garbage collection and memory overheads, cloud warehouses like Snowflake and Redshift, and today's lakehouses built on open formats with storage separated from compute. His argument is that Rust, through projects like Apache Arrow and DataFusion, has become a critical piece of that third era because it offers memory safety without a garbage collector.

[Venkata Appalapuram](https://www.conf42.com/Rustlang_2025_Venkata_Appalapuram_systems_architecture_ai) of Ritepros gave the most transferable talk for library authors. Starting from a Spark JMS connector built at Capital One to read from ActiveMQ, IBM MQ, and Amazon SQS, he mapped JVM library patterns to Rust crate design: provider interfaces become traits, exception handling becomes `Result`, plus testing and documentation strategies that work across both ecosystems.

[Narendra Reddy Mudiyala](https://www.conf42.com/Rustlang_2025_Narendra_Reddy_Mudiyala_memory_safety_systems) of Accenture applied Rust to data mesh, and [Ritesh Kumar Sinha](https://www.conf42.com/Rustlang_2025_Ritesh_Kumar_Sinha_memory_safety_zero) of Kotak Mahindra Bank to large-scale pipelines for climate data.

## Rust in the cloud

[Vamsi Praveen Karanam](https://www.conf42.com/Rustlang_2025_Vamsi_Praveen_Karanam_aws_cloud_scale), a Software Development Engineer at Amazon, gave a practical tour of the AWS SDK for Rust. His comparison is a fair one: Go is strong on Lambda but carries a bigger runtime, Java has the ecosystem but pays for cold starts and memory, Python wins at prototyping but slows at scale. Rust's small binaries mean faster Lambda cold starts, and with Tokio you can run thousands of async calls to AWS services.

[Bandhavi Sakhamuri](https://www.conf42.com/Rustlang_2025_Bandhavi_Sakhamuri_cloud_ai_rust), a Senior SRE at SolarWinds, built a carbon-aware Kubernetes scheduler in Rust. Default schedulers weigh performance and availability but not where the electricity comes from; the framework adds that signal, whether you run on EKS, AKS, or GKE. [Uday Kiran Yedluri](https://www.conf42.com/Rustlang_2025_Uday_Kiran_Yedluri_cloud_security_rust) covered Rust across multi-cloud enterprise environments, and [Karthik Mohan Muralidharan](https://www.conf42.com/Rustlang_2025_Karthik_Mohan_Muralidharan_edge_cloud_divide) of Walmart Global Tech looked at orchestration patterns between the edge and the cloud.

## Packets, radios and robots

Rust's home turf, low-latency systems, still had a strong showing. [Rahul Tavva](https://www.conf42.com/Rustlang_2025_Rahul_Tavva_memory_code_zero) of Kairos Technologies covered zero-copy packet processing and async routing, [Prasanth Kosaraju](https://www.conf42.com/Rustlang_2025_Prasanth_Kosaraju_memory_safety_systems) of Dataquest applied Rust to network infrastructure in educational and industrial settings, and [Riddhi Patel](https://www.conf42.com/Rustlang_2025_Riddhi_Patel_memory_safety_zero) of DRC System explored how the ownership model fits ultra-low-latency 5G systems. [Venu Madhav Nadella](https://www.conf42.com/Rustlang_2025_Venu_Madhav_Nadella_memory_safety_zero) of Spectrum moved telecom operations from reactive to predictive.

On the factory floor, [Sankar Subramanian](https://www.conf42.com/Rustlang_2025_Sankar_Subramanian_memory_safety_zero), a Staff Engineer at Lucid Motors with over 20 years in control and automation, showed zero-copy machine vision pipelines for spotting battery defects in EV manufacturing. [Anushree Nagvekar](https://www.conf42.com/Rustlang_2025_Anushree_Nagvekar_edge_memory_safety) of AEye looked at edge AI for autonomous vehicles, where zero-cost abstractions and memory safety both matter.

## When a crash is not an option

Several talks made the safety argument where it hits hardest. [Lakshmi Vara Prasad Adusumilli](https://www.conf42.com/Rustlang_2025_Lakshmi_Vara_Prasad_Adusumilli_memory_safety_systems) of Conduent started from a blunt premise, that when 911 systems crash, people die, and showed compile-time guarantees in emergency response systems. [Raphael Shobi Thomas](https://www.conf42.com/Rustlang_2025_Raphael_Shobi_Thomas_memory_safety_code) covered a healthcare and travel safety platform for seniors, and [Prabhakar Singh](https://www.conf42.com/Rustlang_2025_Prabhakar_Singh_memory_safety_systems) of Meta built real-time fraud prevention for gig platforms.

Security engineers had their say too. [Naresh Yelkoti](https://www.conf42.com/Rustlang_2025_Naresh_Yelkoti_memory_security_cloud) of U.S. Bank built security scanning pipelines in Rust, [Sachin Kapoor](https://www.conf42.com/Rustlang_2025_Sachin_Kapoor_memory_security_safety) walked through zero trust fundamentals implemented in Rust, and [Ketankumar Patel](https://www.conf42.com/Rustlang_2025_Ketankumar_Patel_memory_safety_zero) of Wind River proposed a framework for ethical AI in Rust.

## Agents, dashboards and business systems

Rust for AI agents appeared too. [Sidhanta Panigrahy](https://www.conf42.com/Rustlang_2025_Sidhanta_Panigrahy_memory_safety_zero) of Okta built a Tokio-based multi-agent system, and [Sarat Piridi](https://www.conf42.com/Rustlang_2025_Sarat_Piridi_agents_zero_systems) of Hanwha Qcells covered Rust-powered process automation across industries. Dashboards got two takes: [Tashi Garg](https://www.conf42.com/Rustlang_2025_Tashi_Garg_cloud_ai_rust) of Juniper Networks on dynamic UIs for cloud infrastructure, and [Shahzeb Akhtar](https://www.conf42.com/Rustlang_2025_Shahzeb_Akhtar_memory_security_rust) of UnitedLex on business intelligence.

The business-systems corner rounded it out: [Swetha Priya Sathiyam](https://www.conf42.com/Rustlang_2025_Swetha_Priya_Sathiyam_systems_memory_code) of ADP on HR tech, [Nageswara Rao Nelloru](https://www.conf42.com/Rustlang_2025_Nageswara_Rao_Nelloru_memory_ai_zero) on claims management APIs, and [Shikha Duttyal](https://www.conf42.com/Rustlang_2025_Shikha_Duttyal_ml_ai_rust) of Meta on digital twins for supply chains.

## Partners and what's next

Conf42 Rustlang 2025 was supported by the [StarterAI](https://www.starterai.dev/) newsletter, the [HockeyStick](https://www.hockeystick.show/) podcast, and the media partners listed on the event page.

For more, the earlier editions are still online, starting with [Conf42 Rustlang 2024](https://www.conf42.com/rustlang2024). Fair warning: you may come out wanting to rewrite something.
