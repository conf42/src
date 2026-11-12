# 30,000 artifacts, one Mongo document, and every builder waiting on a lock

Conf42 Blog, 2021-04-29. https://www.conf42.com/blog/cloud2021/addtoset-30000-artifacts-mongo-lock

In short: Rob Zuber (CircleCI) at Conf42 Cloud Native 2021 on three CircleCI incidents where the tools worked as built, just not for CircleCI's case

Rob Zuber, CTO of CircleCI, spent his Conf42 Cloud Native 2021 talk on three production problems from CircleCI's own history where a convenient tool did exactly what it was built to do, and that was the problem. A MongoDB array operator, an EBS snapshot restore and a split monolith each looked like magic until scale exposed how they were implemented. His takeaway: do the simple thing, but know when it will break.

He opens in 1998, at his first startup, with no computer science background, asked to fix a page that got slower as users grew. The cause was Java string concatenation in a loop: every plus allocated a new string and threw the old one to the garbage collector, where a StringBuffer would have appended into one growing chunk. Tools let you focus on users, he says, but not knowing how they work degrades things for those same users.

## Why did adding artifacts slow builds to a crawl?

"There's always a schema. It's just a question of where that schema is enforced," Rob Zuber said at Conf42 Cloud Native 2021, about schemaless databases. CircleCI has run on Mongo for a long time, and documents carry every field name, so a record can be about 25% bigger than the same row in a relational table. Mongo stores BSON with no fixed field order, so finding a field means iterating over the document.

With no joins, the recommended pattern is to embed lists, and Mongo's addToSet operator conveniently refuses duplicates. CircleCI used it for build artifacts: an array of small documents with name, S3 path and URL. Fine for a handful. Then customers generated 30,000 or more artifacts per build, often from parallel builds where up to 100 machines write to the same build document.

Each addToSet locks the document and scans the whole array for duplicates before writing. When the array outgrows its space, Mongo allocates new memory, copies the document, and later finds a new extent on disk, all while the other 99 builders wait. The quick fix was swapping addToSet for push, since duplicates never actually mattered. The real fix was rebuilding artifact storage so it no longer lived inside the Mongo document.

## What went wrong with EBS snapshot restores?

Around 2015 CircleCI's Mongo ran with a third-party provider on AWS's largest instances with local SSDs, and it was running out of space even for a single collection. Daily backups took more than 24 hours, so they were stale before they finished, and a restore took two to three days.

Moving Mongo into CircleCI's own AWS account on EBS fixed most of that. Throughput was excellent, latency good enough, snapshots gave consistent backups without stopping Mongo thanks to journaling, and hosts became immutable: build a new machine, attach the volume, throw the old one away. A multi-terabyte volume came back from a snapshot in a couple of minutes.

Then Mongo took minutes to start, and ran slowly as a secondary for a long time after. A restored volume holds references, not data; blocks are fetched from the snapshot on demand, which suits small volumes and sequential reads. A large database with random access from every customer means each read becomes a fetch, decompress and write. CircleCI now runs warming queries for the most recently written data before putting a restored host into production.

His lesson: providers solve the general case, probably by an 80/20 rule, so ask whether you are the target.

## How did a split monolith send statuses out of order?

Early CircleCI was a monolith running as many instances, each grabbing the next job from the database. Contention on the same jobs eventually stopped it scaling, so under time pressure the team started a copy of the monolith as a dispatcher that hands out work. Same code base, different instructions.

Inside one instance, a watcher pushed build status changes to GitHub asynchronously. Split across two, a busy dispatcher could post the started status after a quiet builder had already posted completed on a short build. GitHub does not reorder them, so pull requests sat incomplete forever. Customers did not report the ordering; they reported that the status never completed.

His conclusion: services beget services, and distributed systems are concurrency. Breaking up a system is a conscious decision to take on more complexity.

## Who should watch?

Engineers who lean on managed databases and cloud storage, and anyone splitting a monolith. Three well-told incident stories, each with a fix.

## Related Conf42 talks

- Joe Karlsson on [MongoDB schema design](https://www.conf42.com/JavaScript_2020_Joe_Karlsson_mongodb_schema_design) at Conf42 JavaScript 2020.
- Dmitry Vinnik on [concurrency](https://www.conf42.com/Enterprise_Software_2021_Dmitry_Vinnik_concurrency) at Conf42 Enterprise Software 2021.
- Aleksei Popov on [the maze of complexity in distributed systems](https://www.conf42.com/Site_Reliability_Engineering_SRE_2024_Aleksei_Popov_maze_complexity_distributed_systems) at Conf42 SRE 2024.

[Watch Rob Zuber's talk](https://www.conf42.com/Cloud_Native_2021_Rob_Zuber_cs_fundamentals_fail_us), part of [Conf42 Cloud Native 2021](https://www.conf42.com/cloud2021).

## From CircleCI

CircleCI is the CI/CD platform whose parallel builds and artifact storage feature in these stories. Rob Zuber is its CTO.

- [CircleCI website](https://circleci.com/)

[Watch the talk on YouTube](https://youtu.be/9hD3AQGP8k4).

## Watch the talk

[Low-Level Computing in a Cloud Native World](https://www.conf42.com/Cloud_Native_2021_Rob_Zuber_cs_fundamentals_fail_us) at Conf42 Cloud Native 2021.
