# Serverless databases remove capacity planning, not database engineering

Conf42 Blog, 2026-05-21, updated 2026-11-09. https://www.conf42.com/blog/dbd2026/serverless-databases-still-have-servers

In short: Renato Losio at Conf42 Database DevOps 2026 shares five lessons from five years of Aurora Serverless, DynamoDB and DSQL, from storage to cost forecasting.

Renato Losio once tried to draw the New York City skyline with the capacity graph of Aurora Serverless v2, on stage at re:Invent. At Conf42 Database DevOps 2026, the cloud architect behind cloudiamo.com turns five years of playing with AWS serverless databases into five lessons, and one thesis: "serverless database remove the capacity management, but they don't remove database engineering."

It's an experience talk, not a vendor pitch, and he's openly unimpressed by naming.

## Serverless is an adjective

Lesson one is about labels. Aurora Serverless v1 (GA in 2018) was, as he describes it, roughly an upgraded version of his old auto-scaling Bash and Python scripts, doubling capacity each time; it's now deprecated. DynamoDB On-Demand arrived the same year without the word in its name and is about as serverless as it gets. DocumentDB Serverless doesn't scale to zero. Amazon Aurora DSQL dropped the word entirely. Athena has let you pay per query on S3 for a decade. His advice: stop arguing about the name and ask whether the thing is elastic in the way you need.

## Storage is the bill and the bottleneck

Lesson two has two halves. On a production database he manages, monthly storage and backup costs now exceed compute, on plain GP3. So the CPU line that serverless optimises may not be your main problem.

The second half is a small experiment: insert 100,000 rows one at a time from a stored procedure, default settings, into Aurora Serverless v2 (minimum half an ACU), provisioned Aurora on r8g.large, and RDS for MySQL on the same instance class with 400 GB of GP3. Both Aurora flavours finish in a few seconds. RDS takes about five minutes, and tuning only gets that down to a minute or two. He's clear the workload is unrealistic, but the point lands: Aurora's storage architecture matters far more than whether the compute is serverless.

## Cost forecasting needs a crystal ball

Lesson three: you can't predict serverless cost from a provisioned baseline. One cluster's monthly bill, queried with Athena, had over a thousand line items, because you pay for everything you use: compute units, traffic, multi-AZ, backup, storage type. DSQL's DPU pricing drew the same complaint at launch. That, he argues, isn't the cloud provider being evil; pricing per query shape is hard. His method is empirical: move a replica to serverless, watch the bill, then decide. Anyone quoting you a saving before that is guessing.

## Compatible until it isn't

Lesson four walks the ladder from self-managed Postgres or MySQL on EC2 (most control, least lock-in) through RDS and Aurora to serverless, where you give up more control with each step. Claims of Postgres or MongoDB compatibility hold until your extension isn't supported or an aggregation behaves differently. Compatibility can mean wire protocol, SQL dialect, feature behaviour, the tooling ecosystem or versions, and vendors usually only talk about the first two. He also notes the relational side converging on Postgres, with DSQL Postgres-compatible from day one.

## Horizontal or vertical is a choice, not a verdict

Lesson five: DynamoDB and DSQL scale horizontally behind the scenes; Aurora Serverless scales a single instance vertically. Neither is fake serverless. Most workloads fit comfortably on one big instance with read replicas.

He closes with a line from the Aurora Serverless v2 documentation: if the database won't scale back down, stop and restart it to reclaim fragmented memory, accepting the downtime. Which is where his old scripts started. There's still a MySQL or Postgres engine under there, and a forgotten cron job can keep it awake all month while you blame the scaling algorithm.

## Who should watch

Anyone about to move a relational workload to Aurora Serverless, DSQL or DynamoDB on-demand on the promise of savings. If you already run them, the storage experiment and the billing breakdown are worth the half hour on their own.

## Related Conf42 talks

- [Things Fall Apart: Navigating Managed Databases for Over a Decade as a Non-DBA](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Renato_Losio_things_fall_apart) by Renato Losio, the managed-database prequel.
- [Amazon Aurora DSQL: The Future of Scalable, Distributed Relational Databases](https://www.conf42.com/Site_Reliability_Engineering_SRE_2025_Samuel_Baruffi_amazon_aurora_dsql) by Samuel Baruffi, the AWS view of DSQL.
- [What happens when DynamoDB explodes? A practical guide for developers](https://www.conf42.com/Cloud_Native_2022_Erez_Berkner_dynamodb_explodes_guide) by Erez Berkner, for the horizontal side of the story.

[Watch Renato Losio's talk](https://www.conf42.com/Database_DevOps_2026_Renato_Losio_mistakes_lessons_scaling)

[Watch the talk on YouTube](https://youtu.be/wGuB9vW6ZSY).

## Watch the talk

[Five Hard Lessons from Five Years of So-Called Serverless Databases](https://www.conf42.com/Database_DevOps_2026_Renato_Losio_mistakes_lessons_scaling) at Conf42 Database DevOps 2026.
