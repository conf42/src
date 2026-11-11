# Your database password is older than half your team

Conf42 Blog, 2022-12-02. https://www.conf42.com/blog/devsecops2022/dynamic-database-credentials-with-vault

In short: Dewan Ahmed (Aiven) at Conf42 DevSecOps 2022 on replacing static database passwords with short-lived, audited credentials from HashiCorp Vault

A national police database with terabytes of data on a billion people leaked because a developer published working Elasticsearch credentials in a blog post, and the credential stayed valid for a year. Dewan Ahmed, Senior Developer Advocate at Aiven, opened his Conf42 DevSecOps 2022 talk with that story and spent the rest of it on the fix: credentials generated on demand, scoped to one job, expired by default and audited, demonstrated with HashiCorp Vault in front of a PostgreSQL database.

He deliberately leaves out physical access, compromised hosts and SQL injection. The talk is about database access alone, because his slides cite the 2021 Verizon Data Breach Investigations Report: 80% of data breaches are the result of poor or reused passwords.

## What is secret sprawl?

His list will be familiar. A CI server somewhere holds the database credential. Someone who left unhappily six months ago may still have access. Teams roll their own encryption service, custom cryptography included, outside their expertise. And his favourite: "Using the same database password since forever." The password under the table, known to everyone in the office.

Handing a credential to an application doesn't solve it either. Dewan Ahmed said at Conf42 DevSecOps 2022: "Applications are not very good at keeping secrets." Sooner or later the secret ends up in a log or some output.

## Authentication, authorisation, auditing

He frames protection with the AAA model and uses Apache Kafka as the warm-up. Authentication: clients prove themselves to brokers with SSL certificates signed by a CA (the common managed setup) or with SASL, which separates the authentication mechanism from the Kafka protocol and is common in Hadoop shops. Authorisation: ACLs, user A can or cannot do operation B on resource C from host D. Auditing: Kafka audit logs, shipped with sink connectors to somewhere like S3, plus the open source Klaw project as a governance and audit layer for topics, ACLs and schemas.

## Why dynamic credentials?

They don't exist until someone asks, they expire, and every use can be audited. The time limit can match the user: an engineer might get a credential good for an eight-hour working day, while an application that makes a few-second call should get one that lives for minutes.

His checklist for picking a tool: flexibility (UI, CLI and API), integrations with the clouds and databases you use, built-in encryption, automatic expiry and revocation after a breach. He picks HashiCorp Vault: dynamic secrets per provider, storage for the long-lived ones too, encryption as a service, leases you can revoke, and acting as a root or intermediate CA so you don't have to manage X.509 certificates by hand.

## The demo: one table yes, the other no

On an Aiven for PostgreSQL service he creates two tables: weekly metrics reporting (downloads, GitHub stars, followers, all public) and employee salary. The goal is an application that can read the first but not the second.

Vault runs in dev mode (unsealed, root token printed, his warning: never in production). Three steps: enable the database secrets engine, configure it with the PostgreSQL plugin and a templated connection URL so no password is hard-coded, and define a role whose creation statement grants access on the metrics table only, with a one-hour TTL. A vault read, or an HTTP API call, returns fresh credentials.

With the admin credential both tables are readable. With the dynamic one, the metrics table works and the salary table returns permission denied.

## How do you audit without leaking the secrets?

Auditing is off by default; he enables a file audit device. Entries show the lease ID, but the secret values are HMAC-SHA256 hashed with a salt, so the audit file is not a second copy of your passwords. To check whether a suspicious username touched something, you send it through Vault's audit-hash endpoint and compare the result with the log entry.

He closes with a question every team should answer before an incident: do you have a break glass procedure for your data infrastructure? The steps are written up in Aiven's blog post on securing a database with Vault, linked from the talk.

## Who should watch

Teams that still keep one shared PostgreSQL password in CI variables, and anyone who has to show auditors who accessed which table. Related talks: [Rosemary Wang on secrets handling](https://www.conf42.com/Cloud_Native_2025_Rosemary_Wang_secrets_handling_security), [Jeroen Willemsen on secrets management](https://www.conf42.com/DevSecOps_2021_Jeroen_Willemsen_secretsmanagement) and [Michael Levan on Kubernetes secret management with Vault](https://www.conf42.com/Cloud_Native_2023_Michael_Levan_kubernetes_secret_management_vault).

[Watch Dewan Ahmed's talk](https://www.conf42.com/DevSecOps_2022_Dewan_Ahmed_managing_credential_managed_database)

## From Aiven

- [Aiven](https://aiven.io): managed open source data infrastructure, including the PostgreSQL service used in the demo.

[Watch the talk on YouTube](https://youtu.be/r7uO0sPQV0c).

## Watch the talk

[Who's managing the credential for your data infrastructure?](https://www.conf42.com/DevSecOps_2022_Dewan_Ahmed_managing_credential_managed_database) at Conf42 DevSecOps 2022.
