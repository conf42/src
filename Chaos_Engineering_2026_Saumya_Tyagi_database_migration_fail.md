# Why Database Migrations Fail Silently

A talk at [Conf42 Chaos Engineering 2026](https://www.conf42.com/chaos2026) by [Saumya Tyagi](https://www.conf42.com/speaker_Saumya_Tyagi) (Principal Software Engineer @ Microsoft AI). Page: https://www.conf42.com/Chaos_Engineering_2026_Saumya_Tyagi_database_migration_fail

## Abstract

A database migration can look successful on launch day and still leave
behind problems that surface weeks later. The new database is running,
traffic has moved, and the dashboards look healthy. Yet some records
may already be inconsistent.

Having worked on large-scale database migrations, I've seen how
difficult it can be to catch these problems before they affect
customers.

In this talk, I'll cover five failure modes that are easy to miss
during zero-downtime migrations, including dual-write inconsistencies,
backfill races, schema drift, delayed events, and incomplete
validation. I'll explain why common checks fail to catch them and how
teams can use fault injection, record-level reconciliation, shadow
reads, and controlled rollouts to uncover problems earlier.

The goal is to give engineers practical ways to test migration safety,
detect silent failures, and know when it's safe to cut over.
