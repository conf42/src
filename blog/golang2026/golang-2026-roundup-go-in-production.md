# Conf42 Golang 2026 - Go as the boring backbone under AI and money

Conf42 Blog, 2026-05-22. https://www.conf42.com/blog/golang2026/golang-2026-roundup-go-in-production

In short: Conf42 Golang 2026 in review, 22 talks on MCP servers in Go, monolith surgery at Fleet, O(log N) leaderboards, fallback search at eBay and GPU profiling.

[Conf42 Golang 2026](https://www.conf42.com/golang2026) aired on May 21, 2026 with 22 talks, and the language itself rarely took centre stage. Go showed up the way it does in most companies: as the dependable layer under an MCP server, a leaderboard, a search fallback, a fraud engine or an insurance core. Speakers from eBay, Fleet Device Management, METRO AG, Hewlett Packard Enterprise, General Motors, Ford, Salesforce, Walmart and SoftSwiss showed what that layer has to survive.

## Go as the plumbing for LLMs

The most hands-on AI talk came from [Shadi Elyafi](https://www.conf42.com/Golang_2026_Shadi_Elyafi_mcp_b2b_workflow) (METRO AG), who built an MCP server in Go for a real B2B workflow on a platform serving more than 1 million company profiles. It exposes tools for Claude, talks to a GraphQL backend through AWS AppSync, and draws careful read/write boundaries so mutations stay safe. He also covers how TDD with mock GraphQL clients keeps the MCP layer from turning into a fragile demo.

[Swati Kumari](https://www.conf42.com/Golang_2026_Swati_Kumari_beyond_chatbots_building) (NucleusTeq) made the case that most chatbots fail because they cannot reach CRM, order management or billing, and showed Go backend integrations that let them act. [Sanjay Basu](https://www.conf42.com/Golang_2026_Sanjay_Basu_building_cognitive_commerce) (TCS) sketched Go-based architectures for LLM-driven grocery and e-commerce platforms, and [Venkat Kamma](https://www.conf42.com/Golang_2026_Venkat_Kamma_from_reactive_predictive) (StarGroup Innovations) applied the same idea to Oracle Cloud PPM, catching cost overruns before they happen instead of in the monthly report. [Rejenish Kiran](https://www.conf42.com/Golang_2026_Rejenish_Kiran_assisted_test_execution) (Citizens Property Insurance Corporation) positioned AI-assisted test execution as an augmentation layer on top of existing Go test frameworks rather than a replacement.

## Data structures still win the incident

The talk most likely to end up in a team chat was [Ivan Balashov's](https://www.conf42.com/Golang_2026_Ivan_Balashov_engineering_high_performance) (SoftSwiss). A production leaderboard was causing daily outages thanks to O(N²) updates, CPU spikes and memory pressure. The fix was an indexed skip list with span counters for O(log N) position queries plus hash-based deduplication, replacing a naive slice-based leaderboard in two days. A good reminder that your outage might be a CS201 exercise wearing a pager.

[Amol Lele](https://www.conf42.com/Golang_2026_Amol_Lele_real_time_training) (Hewlett Packard Enterprise) built a multi-layer ML training profiler in Go with 2-5% runtime overhead and walked through the three costliest failure modes he found: data pipeline bottlenecks, communication overhead in distributed training, and straggler workers in heterogeneous clusters. [Akshaya Jayaram](https://www.conf42.com/Golang_2026_Akshaya_Jayaram_ammf_attention_based) (Salesforce) presented AMMF, an attention-based fusion model for spotting the same vulnerable function across architectures, a problem Go's easy cross-compilation makes very real.

## Failing gracefully on purpose

[Hima Bindu Yanala](https://www.conf42.com/Golang_2026_Hima_Bindu_Yanala_designing_resilient_self) (eBay) treated fallback as a first-class feature of self-service search: a dedicated lightweight fallback index, circuit breakers routing traffic through closed, open and half-open states, and bulkheads protecting fallback capacity. Her point about fan-out amplification, where rare shard outliers become systemic failures, applies well beyond search.

[Yogesh Pugazhendhi Duraisamy Rajamani](https://www.conf42.com/Golang_2026_Yogesh_Pugazhendhi_Duraisamy_Rajamani_building_self_healing) (Ford Motor Company) described self-healing streaming pipelines in Go with a reinforcement-learning control plane adjusting ingestion, messaging and compute across Kafka, Pulsar and Flink. [Sudhakar Pallaprolu](https://www.conf42.com/Golang_2026_Sudhakar_Pallaprolu_autonomous_cloud_infrastructure) covered self-healing infrastructure and AIOps from the platform side.

## Evolving the code you already have

[Victor Lyuboslavsky](https://www.conf42.com/Golang_2026_Victor_Lyuboslavsky_modularizing_year_monolith) (Fleet Device Management) gave the talk he says the Go community lacks: a real, open source, decade-old Go monolith mid-way to a modular design while still shipping to production. It started as an investigation into slow builds and tests and turned up oversized packages, uncontrolled dependencies and boundaries that no longer matched how engineers thought about the system. The people side gets as much airtime as the architecture.

[Sulabh Jain](https://www.conf42.com/Golang_2026_Sulabh_Jain_building_cloud_native) took the same question to insurance core systems, where catastrophe-driven claims spikes punish monoliths, and [Sana Fatima](https://www.conf42.com/Golang_2026_Sana_Fatima_from_code_correctness) (General Motors) argued that code which compiles and passes unit tests can still fail at system level in embedded automotive software, so behaviour validation has to move earlier.

## Compliance and money, engineered in

Regulated platforms got a strong block. [Manasa Uppula](https://www.conf42.com/Golang_2026_Manasa_Uppula_designing_defensibility_evidence) (Virtusa) designs financial platforms so that every critical customer interaction produces structured evidence by default: what was shown, how consent was captured, how a decision was made. Audits then become a query, not an archaeology dig. [Sridhar Muthineni](https://www.conf42.com/Golang_2026_Sridhar_Muthineni_driven_fraud_detection) (Capgemini) combined fraud detection and personalisation in Go fintech systems, and [Devi Manoharan](https://www.conf42.com/Golang_2026_Devi_Manoharan_building_high_performance) (ASTA CRS) covered AI-driven claims processing on EDI pipelines. [Emmanuela Opurum](https://www.conf42.com/Golang_2026_Emmanuela_Opurum_building_secure_pipelines) (SoftNet Technologies) showed Go-based automation for secure CI/CD across AWS, Azure and GCP.

The programme also stretched to [DOCSIS networks](https://www.conf42.com/Golang_2026_Harsha_Vardhani_Talluri_building_unified_docsis) (Harsha Vardhani Talluri), [3PL warehouse design](https://www.conf42.com/Golang_2026_Vivek_Sander_data_driven_warehouse) (Vivek Sander, Sunland Logistics Solution), [digital PMOs in retail](https://www.conf42.com/Golang_2026_George_Job_digital_pmos_retail) (George Job, Walmart) and [design systems for analytics platforms](https://www.conf42.com/Golang_2026_Sonali_Priya_scalable_design_systems) (Sonali Priya, LB Networks).

## Sponsors and where to watch

Thanks to [Harness](https://www.harness.io/), the Diamond sponsor, and to [SREday](https://www.sreday.com/) and [Virtana](https://www.virtana.com/) at Gold. All 22 talks are on the [event page](https://www.conf42.com/golang2026) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrCKzSYaULw7l2nLQKxk2IkS).

Next up for the gophers: [Conf42 Golang 2027](https://www.conf42.com/golang2027).
