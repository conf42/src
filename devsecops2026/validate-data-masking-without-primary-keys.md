# How to prove data masking worked when the table has no primary key

Conf42 Blog, 2026-09-17, updated 2026-11-09. https://www.conf42.com/devsecops2026/validate-data-masking-without-primary-keys

In short: At Conf42 DevSecOps 2026, CSC's Siyuan Feng shows how to catch masking failures with row counts, element checks and SQL INTERSECT.

Copying production into dev is the fastest way to get realistic test data, and the fastest way to put real customer records behind weaker locks. At Conf42 DevSecOps 2026, Siyuan Feng, Data Analyst at CSC working on test data management, showed how to verify that masking actually happened, including the nasty case where source and target share no key to join on.

## Why test environments are the soft spot

Feng's framing is practical. Developers, QA and demo teams want production volume and production shape, because code that handles a hundred rows in dev may fall over at ten thousand. So teams copy prod. But production has strict access control, audit trails, MFA and firewalls, while dev and UAT have broader access for developers, contractors and vendors, lighter logging and lower security by design. Same customer data, weaker protection.

Masking is the fix: replace real values with useful fakes that keep the format, so an email stays an email and the @ sign stays put. The harder question is how you know the masking ran on every row, not just most of them.

## Three questions before test data ships

Feng reduces delivery to three checks.

**Row counts match, per table.** If the source has 30,000 rows and the target 29,800, two hundred rows probably failed. He stresses comparing table by table: totals can agree while two individual tables are off.

**Database elements match.** Indexes, constraints, triggers and grants must survive the trip. A missing index makes the app slow. A missing foreign key breaks the link between orders and customers. A dropped trigger stops counters updating. A lost grant means a QA engineer who should only read can suddenly change things, which is how a basic test turns into somebody else's outage.

**Every sensitive value changed.** The interesting one. Masking tools fail quietly when a server runs out of memory or a transform chokes on special characters or non-Latin text. His own example is his Chinese name: the tool could not process it, skipped the row, and the original value sailed through to the target untouched.

## Validation depends on what keys you have

With a stable primary key, it is a join: match customer 101 in source and target and compare the email. If they are identical, masking failed.

Without one, build a composite key from stable unmasked columns, such as a batch ID plus a record reference. That works, but searching for a unique combination across a wide table gets expensive fast, and there is no guarantee one exists.

Then there is the case with no usable key at all: decade-old legacy tables, append-only logs that keep duplicates on purpose, small tables where every column is sensitive. Here Feng swaps JOIN for INTERSECT. If passwords were replaced with random strings, the source and target password columns should share nothing. Any overlapping value is a failed row, and a simple lookup on that value finds the rest of the record.

## Dictionary replacement makes overlap legitimate

Random replacement is the easy version. Dictionary replacement is trickier, because the dictionary may already contain real values. Apple can become Oracle, which is good, or Apple can become Apple, which looks exactly like a failure. Intersection alone cannot tell them apart.

His answer is to use intersection as step one, isolate the overlapping candidates, then compare the non-masked columns of those rows. If the same company name now sits next to a different customer name, the row was masked and the collision is legitimate. If everything around it is unchanged, it is a real miss. You only build identifiers for the narrowed subset, not for hundreds of millions of rows.

## The tool and the scope

Feng closes with DBmask, his open-source, MIT-licensed masking tool, at version 0.1.1 and described as an initial framework. It is configured in YAML, targets SQLAlchemy databases including PostgreSQL, MySQL and SQL Server, and produces a validation report covering row counts, element checks and masking completeness.

This is a hands-on talk with SQL-level examples. Test data managers, QA leads and data engineers who sign off on masked copies will get the most from it. If your masking already runs inside a tool with built-in verification, it is still a useful audit of what that verification should be checking.

## Related Conf42 talks

- [Pradeep Kumar Vattumilli on synthetic data for privacy](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Pradeep_Kumar_Vattumilli_synthetic_data_ai), the alternative to copying prod at all.
- [Sunil Kumar Mudusu on data quality and validation in ML pipelines](https://www.conf42.com/Machine_Learning_2025_Sunil_Kumar_Mudusu_data_quality_validation).
- [Sharath Chandra Adupa on protecting PII in cloud environments](https://www.conf42.com/Golang_2025_Sharath_Chandra_Adupa_security_pii_cloud).

[Watch Siyuan Feng's talk](https://www.conf42.com/DevSecOps_2026_Siyuan_Feng_datamasking_testdata_validation)

[Watch the talk on YouTube](https://youtu.be/aSxhDvJyQZE).

## Watch the talk

[Trust but Verify: Catching Data Masking Failures Before Test Data Ships  Talk Type or Format:](https://www.conf42.com/DevSecOps_2026_Siyuan_Feng_datamasking_testdata_validation) at Conf42 DevSecOps 2026.
