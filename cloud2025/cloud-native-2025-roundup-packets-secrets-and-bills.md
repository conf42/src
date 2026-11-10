# Conf42 Cloud Native 2025 - follow the packet, rotate the secret, read the bill

Conf42 Blog, 2025-03-07. https://www.conf42.com/cloud2025/cloud-native-2025-roundup-packets-secrets-and-bills

In short: Conf42 Cloud Native 2025 in review, 81 talks on EKS networking, dynamic secrets, edge APIs, Wasm on Kubernetes, microservices, cloud costs and databases.

[Conf42 Cloud Native 2025](https://www.conf42.com/cloud2025) ran on March 6, 2025 with 81 talks, and the best of them were refreshingly unglamorous. How does a packet actually reach a pod in EKS? How do you rotate a secret every two weeks without restarting the app? Why is the database still the one tier that doesn't scale? Speakers from AWS, HashiCorp, Microsoft, Meta, Mirantis, Fermyon, Comcast, Expedia Group, Booking.com, Salesforce and a strong group of sponsors answered with demos rather than diagrams.

## Know your plumbing

[Dumlu Timuralp](https://www.conf42.com/Cloud_Native_2025_Dumlu_Timuralp_networking_performance_optimization) (AWS) took the packet's-eye view of Amazon EKS, from the internet through Route53, the ALB and the VPC to the pod, pitched as the Magic School Bus for cloud networking. The point is practical: stop being stuck between teams during an outage because nobody can trace the path. [Roman Rastiehaiev](https://www.conf42.com/Cloud_Native_2025_Roman_Rastiehaiev_api_gateways_comparison) (HiBob) compared open source API gateways such as Kong, Traefik and Envoy, and [Akim Mamedov](https://www.conf42.com/Cloud_Native_2025_Akim_Mamedov_p2p_networks_decentralization) explained the principles behind P2P networks like BitTorrent and IPFS.

Sponsor Zuplo added the global angle. [Adrian Machado](https://www.conf42.com/Cloud_Native_2025_Adrian_Machado_api_network_distribution) argued for running auth, validation, rate limiting and caching at the edge while keeping data-bound services near the database, then debugged his own 1.3-second demo live. Sponsor Dimensigon's [Daniel Moya](https://www.conf42.com/Cloud_Native_2025_Daniel_Moya_automation_decentralization_orchestration) showed open source, decentralised automation that moves commands and files between networks that can't see each other, through a bridge node.

## Secrets, segments and the supply of trust

[Rosemary Wang](https://www.conf42.com/Cloud_Native_2025_Rosemary_Wang_secrets_handling_security) (HashiCorp) started from a requirement every security team writes and every app team dreads: rotate the secrets applications use every two weeks without manual restarts. Her answer is automation, comparing application-agnostic and application-aware ways to inject secrets. [Venkata Nedunoori](https://www.conf42.com/Cloud_Native_2025_Venkata_Nedunoori_security_segmentation_optimization) (dentsu international) covered micro-segmentation in cloud environments, and [FNU Parshant](https://www.conf42.com/Cloud_Native_2025_FNU_Parshant_securing_hardware) (Arm) went down to the silicon with dual-state models for hardware security.

## The developer loop and the runtime

[Anita Ihuman](https://www.conf42.com/Cloud_Native_2025_Anita_Ihuman_kubernetes_development_testing) (MetalBear) made the case for "remocal" development: test against a realistic cloud environment from your laptop and cut the inner loop from hours to seconds. [Eti Ijeoma](https://www.conf42.com/Cloud_Native_2025_Eti_Ijeoma_docker_cache_efficiency) (Manufactured) gave a tidy talk on Docker build caching with layer ordering, bind mounts and cache mounts. [Mikkel Mork Hegnhoj](https://www.conf42.com/Cloud_Native_2025_Mikkel_Mork_Hegnhoj_kubernetes_architecture_extensions) (Fermyon) introduced Spin and SpinKube for running WebAssembly apps on Kubernetes, with an honest comparison against containers. [Bharath Nallapeta](https://www.conf42.com/Cloud_Native_2025_Bharath_Nallapeta_cluster_provisioning_scale) (Mirantis) presented k0rdent, which hides the hundreds of lines of YAML Cluster API normally demands, and [Siri Varma Vegiraju](https://www.conf42.com/Cloud_Native_2025_Siri_Varma_Vegiraju_workflow_dapr_failure) (Microsoft) used Dapr workflows so one failed step doesn't force a restart of a long-running process.

## Microservices, defended and questioned

[Chad Green](https://www.conf42.com/Cloud_Native_2025_Chad_Green_microservices_architecture_defense) (Jasper Engines & Transmissions) delivered "In Defense of Microservices", taking the complexity critiques head on with real implementations. [Asher Sterkin](https://www.conf42.com/Cloud_Native_2025_Asher_Sterkin_cloud_flexibility_ports__adapters) argued for applying Ports and Adapters systematically so today's cloud choices don't lock out tomorrow's. [Praful Konduru](https://www.conf42.com/Cloud_Native_2025_Praful_Konduru_resilience_scalability_faulttolerance) (Meta) covered fault-tolerant cloud-native design, and [Prithvi Raj](https://www.conf42.com/Cloud_Native_2025_Prithvi_Raj_community_tales_future) (Mirantis), former community manager of LitmusChaos, told the story of growing the chaos engineering community as the project became CNCF incubating.

## Every cloud has a bill

Cost came up from every direction. [Maksymilian Kalek](https://www.conf42.com/Cloud_Native_2025_Maksymilian_Kalek_aws_cost_efficiency) (Perelyn) built an ultra-budget AWS backend with Lambda and Powertools, self-hosted PostgreSQL on a cheap EC2 instance, and React on S3 and CloudFront. [Seshendranath Balla Venkata](https://www.conf42.com/Cloud_Native_2025_Seshendranath_Balla_Venkata_cost_cloud_efficiency) (Comcast) shared how his team optimised AWS EMR and Databricks workloads, and [Shinu Pushpan](https://www.conf42.com/Cloud_Native_2025_Shinu_Pushpan_saas_multitenancy_security) (Expedia Group) balanced performance, security and cost in multi-tenant SaaS. [Brian Loomis](https://www.conf42.com/Cloud_Native_2025_Brian_Loomis_observability_insights_telemetry) (Progress) used OpenTelemetry for something other than debugging: consumption-based pricing and showing customers what they use.

Gold sponsor Rapydo took on the most expensive tier. [Matan Nataf](https://www.conf42.com/Cloud_Native_2025_Matan_Nataf_rapydo_databases_broken) argued that developers own the queries while CloudOps owns the consequences, then demoed blocking, throttling and caching runaway queries across a fleet of MySQL and PostgreSQL instances.

## People and AI

Not everything was infrastructure. Sponsor Buildly's [Gregory Lind](https://www.conf42.com/Cloud_Native_2025_Gregory_Lind_teams_collaboration_efficiency) made the case for radical transparency in software teams, from one shared backlog to committing code on day one. On the AI side, [Shivay Lamba](https://www.conf42.com/Cloud_Native_2025_Shivay_Lamba_container_ecosystem_automation) (Couchbase) tackled AI projects whose datasets, models and weights live in separate places, using ModelKits to package them, and [Anant Kumar](https://www.conf42.com/Cloud_Native_2025_Anant_Kumar_apache_spark_clusters) (Salesforce) built resilient Apache Spark clusters on Kubernetes for AI workloads.

## Sponsors and where to watch

Thanks to [SREday](https://www.sreday.com/) at Platinum, [Rapydo](https://www.rapydo.io/) at Gold, and [APA Tech](https://apa.at/about/apa-tech/), [Buildly](https://www.buildly.io/), [Dimensigon](https://www.dimensigon.com/), [Jozu](https://jozu.com/) and [Zuplo](https://zuplo.com/) at Silver. All 81 talks are on the [event page](https://www.conf42.com/cloud2025) and in the [YouTube playlist](https://www.youtube.com/playlist?list=PLIuxSyKxlQrDi1jv-thhvcy4pJ3sBeUJr).

The series returns with [Conf42 Cloud Native 2026](https://www.conf42.com/cloud2026).
