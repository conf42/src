# Your database failover is only as fast as your DNS

Conf42 Blog, 2026-06-02, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/active-active-dns-for-database-failover

In short: Surya Lankalapalli (Microsoft) at Conf42 Database DevOps 2026 on active-active multi-provider DNS, deep health checks and records as code for database failover.

Replication is solid, failover is tested, and then the outage hits and clients keep resolving the dead primary. At Conf42 Database DevOps 2026, Surya Lankalapalli, Principal Software Engineer at Microsoft, argues that DNS is the database dependency nobody talks about, and that a single DNS provider is a silent single point of failure that can outlast the database failure itself by minutes.

His fix is active-active DNS across multiple providers, driven by health checks that reflect what the database is actually doing. It's a short, pattern-level talk with no vendor names, and a useful list of pitfalls.

## Two providers, both serving

Traditional setups rely on one DNS provider. When it degrades (DDoS, outage), teams flip to a secondary by hand, and in the meantime clients see stale records for minutes or hours. Active-active means two or more providers serve authoritative answers simultaneously, not one waiting on standby. If one degrades, the other keeps answering without intervention, and each provider's anycast network cuts latency for clients spread around the world.

Surya recommends two providers as the standard. More than two isn't unusual, but operational cost and differences between providers' routing features make it hard to scale beyond that.

## Three endpoints, three routing rules

The integration with replication is a health-check-driven sequence: continuous checks, detect an unhealthy primary, promote a replica, update DNS, reroute clients. He splits DNS into three endpoint types:

- **Write endpoint:** a single CNAME or weighted record that always points at the current primary and must update immediately on promotion.
- **Read endpoint:** round-robin or latency-weighted records across healthy replicas, so reads scale without application changes.
- **Regional endpoint:** geo-routing to the nearest healthy replica to cut cross-region read latency.

His line is that DNS isn't just a naming layer; it's a traffic control plane.

## Health checks are the engine

Active-active DNS is only as fast and reliable as the checks driving it. A real check combines TCP and HTTP probes, replication lag monitoring and node drain detection. Replication lag thresholds stop you promoting a stale replica; role detection stops writes going to a read-only one. The check interval and failure threshold effectively set your RTO. And checks must go to the application level: a shallow probe will cheerfully report healthy while the database isn't.

## Records as code, and the TTL trap

Both providers must hold the same records, so Surya treats DNS records as code in version control, deployed through CI/CD, with a sync engine keeping providers aligned and drift detection alerting on divergence. Manual changes during incidents are too slow and invite fat-fingered mistakes.

His favourite pitfall: lower TTL does not automatically mean faster failover. Low TTLs multiply resolver traffic and can run into provider rate limits, which can cause the outage you were trying to avoid. Set a low SOA TTL so NXDOMAIN answers aren't cached for long, keep replica records pre-warmed and live before you need them, and remember that providers' API limits differ.

## Fencing and the manual fallback

For multi-region setups, write fencing ensures only one region accepts writes after a failover. DNS alone can't prevent split brain, so coordinate it with the database's own fencing. Geo-routed reads trade latency against replication lag, and the acceptable lag depends on your customers. Finally, active-active removes DNS as a single point of failure, but providers can still degrade together, so keep a documented manual runbook.

Observability ties it together: resolution success rates per provider, replication lag exposed as a metric both database monitoring and health checks consume, and a log of every DNS change with timestamp, trigger and database state.

## Who should watch

SREs and database engineers who have tested failover end to end except for the part where clients find the new primary. If you've never looked at the TTL on your write endpoint, start here.

## Related Conf42 talks

- [Conquering Hybrid DNS with Route 53 Resolver](https://www.conf42.com/Platform_Engineering_2024_Atif_Siddiqui_hybrid_dns_route_53) by Atif Siddiqui, DNS resolution across hybrid networks.
- [The Multi-Workload Challenge: Predictable Failover Across the Stack](https://www.conf42.com/DevOps_2026_Akshay_Pratinav_failover_resilience_workloads) by Akshay Pratinav, failover beyond the database tier.
- [Preparing for disaster: going Multi-Region](https://www.conf42.com/Cloud_Native_2022_Ana_Van_Straaten_going_multi_region) by Ana Van Straaten, the multi-region groundwork.

[Watch Surya Lankalapalli's talk](https://www.conf42.com/Database_DevOps_2026_Surya_Lankalapalli_telemetry_analytics_delivery)

[Watch the talk on YouTube](https://youtu.be/9r11FPtfbFk).

## Watch the talk

[Keeping Databases Always Available: Active-Active DNS Strategies for DevOps and Failover](https://www.conf42.com/Database_DevOps_2026_Surya_Lankalapalli_telemetry_analytics_delivery) at Conf42 Database DevOps 2026.
