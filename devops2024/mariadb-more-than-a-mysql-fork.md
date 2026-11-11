# MariaDB started as a MySQL fork and kept going

Conf42 Blog, 2024-01-26. https://www.conf42.com/devops2024/mariadb-more-than-a-mysql-fork

In short: Alejandro Duarte (MariaDB) at Conf42 DevOps 2024 on how MariaDB grew from a MySQL fork into pluggable storage engines, MaxScale and automatic failover.

Is MariaDB just MySQL with a different name? At Conf42 DevOps 2024, Alejandro Duarte, Developer Relations Engineer at MariaDB, answered with a spoiler in the first ten seconds (no) and then spent the talk on why: a history lesson from IDS to SQL, the Oracle acquisition that triggered the fork, and the parts that have since diverged, chiefly pluggable storage engines and the MaxScale database proxy.

It is a vendor talk, but a good-natured and well-told one, and the first third is a compact history of relational databases worth the time on its own.

## From pointers to SQL in ten minutes

Duarte starts with General Electric's Integrated Data Store in the 1960s and the CODASYL model, where developers queried with nested loops and pointers and rewrote code on every schema change. Edgar Codd's relational model, formalised as relational algebra and calculus, made query optimisers possible. IBM's System R, Ingres at Berkeley and Oracle followed; IBM's researchers created SEQUEL, lost the name to a UK trademark, dropped the vowels, and SQL was born. "So far nobody has come up with a better language than SQL," Alejandro Duarte said at Conf42 DevOps 2024.

Then open source: the GPL, Linux, Postgres (open but not SQL at first, and not GPL), mSQL, and finally MySQL from Michael "Monty" Widenius, built for speed and ease of use and a great fit for the early web.

## Why the fork happened

The chain of acquisitions is the plot. Oracle bought Innobase, maker of the InnoDB engine, in 2005. Sun bought MySQL AB in 2008. Oracle bought Sun, closing in 2010, and suddenly owned both the most successful commercial database and the most popular open source one. Widenius forked the code and many of the original MySQL developers moved with him. Duarte keeps the jab gentle: props to Oracle, the project is alive, though he shows a community Slack joke about the 8.1 innovation release being mostly deprecations.

The fun fact: MySQL is named after Widenius's daughter My, MariaDB after his daughter Maria, and MaxScale after his son Max.

MariaDB became the default in many Linux distributions, and Debian's popularity contest shows the server package overtaking MySQL. The MariaDB Foundation exists to keep the code out of any single company's control.

## One database, many storage engines

Engines are modules you add or remove. InnoDB is the default you will use most of the time. Alongside it: ColumnStore for analytics, MyRocks (from Facebook) for write-heavy loads, Aria for read-mostly tables, Memory, CSV, Spider for sharding, and S3 for cheap cloud storage. His example puts a high-volume comments table on MyRocks and a rarely changing categories table on another engine, then joins them in one query. Two engines, one SQL statement.

## MaxScale does the clever bits

MaxScale is a proxy that understands SQL, so it can route queries. With primary-replica replication behind it, it sends writes to the primary and reads to replicas; you add or remove replicas without restarting the application, which still sees one endpoint. "So the application thinks it's talking to a database and it thinks it's talking to one database," Alejandro Duarte said at Conf42 DevOps 2024.

If the primary dies, MaxScale detects it, promotes a replica and later rejoins the recovered node as a replica; writes may pause briefly but do not fail. It can also accept MongoDB query language from an application using the MongoDB driver and store the data in MariaDB, so SQL and NoSQL data join in one query, and it speaks Kafka for change data capture and ingestion. He demos the cluster on a Raspberry Pi setup with Docker Swarm, unplugging cables while it keeps running.

MariaDB Enterprise adds a longer maintenance window (up to eight years, he says, versus roughly a year for community releases; check the policy), non-blocking backups and enterprise audit.

## Migration and who uses it

Moving from MySQL is easy, and setting SQL_MODE to ORACLE gets MariaDB part of the way through Oracle's dialect, with similar modes for PostgreSQL and SQL Server. Named users include Wikipedia, Samsung, Nokia, Red Hat, Google and DBS, which migrated from Oracle. MariaDB's own figures in the talk: 75% of the Fortune 500 and more than a billion Docker Hub downloads. Kubernetes orchestration and AI features were flagged as future work.

## Who should watch

Developers and DBAs who still think of MariaDB as a MySQL alias, and anyone who wants read scaling or failover without changing a connection string.

## Related Conf42 talks

- Lukas Vileikis on [lessons from MySQL records](https://www.conf42.com/Platform_Engineering_2024_Lukas_Vileikis_mysql_records_lessons) at Conf42 Platform Engineering 2024.
- Adam Furmanek on [observability for PostgreSQL and MySQL](https://www.conf42.com/DevOps_2024_Adam_Furmanek_observability_postgresql_mysql) at Conf42 DevOps 2024.
- Alejandro Duarte again, on [vectors and semantic search with LLMs](https://www.conf42.com/Database_DevOps_2026_Alejandro_Duarte_llm_vectors_semantic) at Conf42 Database DevOps 2026.

[Watch Alejandro Duarte's talk](https://www.conf42.com/DevOps_2024_Alejandro_Duarte_mariadb_fork_mysql)

## From MariaDB

MariaDB plc develops MariaDB Enterprise Server and MaxScale on top of the open source MariaDB server.

- [MariaDB website](https://mariadb.com/)

[Watch the talk on YouTube](https://youtu.be/B7FGGACjoVI).

## Watch the talk

[The MariaDB Evolution: Just a Fork of MySQL?](https://www.conf42.com/DevOps_2024_Alejandro_Duarte_mariadb_fork_mysql) at Conf42 DevOps 2024.
