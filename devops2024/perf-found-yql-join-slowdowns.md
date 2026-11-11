# A forgotten debug counter cost YQL half its join speed

Conf42 Blog, 2024-01-24. https://www.conf42.com/devops2024/perf-found-yql-join-slowdowns

In short: Alexey Ozeritskiy (YDB) at Conf42 DevOps 2024 on tuning the YQL distributed SQL engine with TPC-H, perf and stackcount - and the bugs they found.

The biggest speedup in this talk came from deleting code someone forgot to delete. At Conf42 DevOps 2024, Alexey Ozeritskiy, Lead Software Engineer at YDB, walked through a year of optimising YQL, the distributed SQL engine behind YDB, with a benchmark-driven loop: TPC-H in CI, Linux perf for the hot spots, and a habit of not trusting your first theory.

It is an engineering case study with real numbers, perf output and patches, which makes it one of the more satisfying sponsor talks of the event.

## What is YQL, and why do 1% wins matter?

YQL (YDB Query Language) is a library that parses and executes SQL. It runs inside YDB, the open source distributed SQL database; inside YTsaurus, the open source big data platform; inside an internal Yandex service also called YQL; and inside Yandex Query, a BigQuery-like service for Yandex Cloud customers. The internal service alone handles 600,000 queries a day, so even a 1% gain is worth chasing.

The architecture has four layers: a parser that builds the AST, a plan builder that produces and optimises an execution plan, an execution layer that runs it across the cluster, and a compute layer that evaluates filters, projections, expressions, functions and joins. The plan is a graph of stages, each split into tasks, and the tasks are actors, which is what makes the testing trick below possible.

## How do you measure a distributed engine honestly?

Benchmarks first. TPC-H gives 22 queries over nine tables plus a data generator, dbgen; he generated scale-100 data in 100 parallel jobs on MapReduce, converted it to Parquet (Snappy, 60 parts per table) and put it in S3. CI runs scale 10 daily and per commit, with commit-to-commit comparisons.

Because tasks are actors, a tool called dqrun runs the whole distributed engine in one process against Parquet files, without YDB's transaction, replication or storage layers. For network effects, a service node and worker nodes run the same plan distributed. Measurements follow UnixBench: run N times, drop the lowest third, take the geometric mean of the rest. Targets came from a published TPC-H 100 comparison: TiDB 189 s, Greenplum 436 s, Spark 388 s. His bench box: two Xeon Gold 6338 (64 cores, 128 threads), 512 GB of RAM, with taskset for pinning.

## Investigation one: atomics in the hot path

A flame graph of a join-heavy query showed the join algorithm burning CPU, but nothing useful when zoomed. perf report, reading the raw data, pointed at atomic fetch-add inside the add-tuple function. "Someone added to this code these atomic counters for debugging purpose and he forgot to remove it," Alexey Ozeritskiy said at Conf42 DevOps 2024. Removing them took TPC-H 10 query 21 from 15 s to 7 s, and other join queries roughly halved too.

## Investigation two: mmap under lock

Running perf top during benchmarks, he spotted a kernel symbol, osq_lock, near the top. stackcount traced it to mmap calls from YQL's own per-query memory allocator, which exists for good reasons: isolation between queries and freeing everything at query end. The fix was to map 32 pages per call instead of one and cache the spares. TPC-H 100 query 20 went from 36 s to 27 s.

The totals after this work: YQL at 154 s on Parquet, YDB at 209 s on a YDB cluster, against Greenplum's 436 s and Spark's 388 s.

## Investigation three: the pipe that wasn't slow

YQL lets users embed Python in SQL, and a ctypes call can segfault the process and every other user's query with it. So compute was moved into a container per task, talking over a pair of Unix pipes. TPC-H took 561 s. Pipes are slow, he reasoned, citing IPC benchmarks where memory-mapped files win by an order of magnitude, so he tried memory-mapped queues and vmsplice. A day spent, nothing gained. Only then did he run perf, which showed statistics code using string-keyed hash maps, meant to run once per query, being touched on every pipe message. Removing it: 223 s, fully containerised. The lesson is the one every profiler user relearns: measure before you rewrite.

Next on his list: TPC-H at terabyte scales and TPC-DS, with 99 queries and joins across ten tables, where plan-level optimisation matters more.

## Who should watch

Database and systems engineers, and anyone who wants a worked example of perf, perf top and stackcount on a real codebase. Light on slides, heavy on the method.

## Related Conf42 talks

- Yonatan Goldschmidt on [low-overhead application profiling with eBPF](https://www.conf42.com/Python_2022_Yonatan_Goldschmidt_low_overhead_application_profiling_using_ebpf) at Conf42 Python 2022.
- Yashvardhan Kukreja on [profile-guided optimization](https://www.conf42.com/Golang_2024_Yashvardhan_Kukreja_profileguided_optimization) at Conf42 Golang 2024.
- Trista Pan on [a distributed PostgreSQL ecosystem](https://www.conf42.com/Cloud_Native_2022_Trista_Pan_postgresql_distributed_secure_database_ecosystem) at Conf42 Cloud Native 2022.

[Watch Alexey Ozeritskiy's talk](https://www.conf42.com/DevOps_2024_Alexey_Ozeritskiy_distributed_sql_database_optimization)

## From YDB

YDB is an open source distributed SQL database; YQL, dqrun and the patches discussed here live in its public repository.

- [YDB website](https://ydb.tech/?utm_source=conf42)
- [YDB on GitHub](https://github.com/ydb-platform/ydb)

[Watch the talk on YouTube](https://youtu.be/I_UaaqJrxT8).

## Watch the talk

[Enhancing a Distributed SQL Database Engine: A Case Study on Performance Optimization](https://www.conf42.com/DevOps_2024_Alexey_Ozeritskiy_distributed_sql_database_optimization) at Conf42 DevOps 2024.
