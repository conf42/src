# How a skip list rescued real-time leaderboards in two working days

Conf42 Blog, 2026-05-04, updated 2026-11-09. https://www.conf42.com/blog/golang2026/skip-list-leaderboards-in-go

In short: Ivan Balashov of SoftSwiss at Conf42 Golang 2026 on replacing a sorted-slice leaderboard with an indexed skip list in Go after a CPU incident.

The leaderboard was a slice behind a mutex, and every score update walked the whole array and re-sorted it. That worked until a Christmas promo campaign was far more successful than anyone expected. [Ivan Balashov](https://www.conf42.com/Golang_2026_Ivan_Balashov_engineering_high_performance), Senior Software Developer and Team Lead at SoftSwiss, told the story at Conf42 Golang 2026: the fix was an indexed skip list with span counters, written in plain Go and shipped in two working days, not a new Redis cluster.

This is the kind of talk Conf42 Golang does well: one real incident, one data structure, and the reasoning in between.

## The incident

SoftSwiss serves real-time tournament leaderboards for more than 1,500 casino operators, with an SLA of around 50 milliseconds. During the holidays a single leaderboard passed half a million participants. CPU load climbed, Kubernetes started killing pods, and Ivan saw CPU throttling measured not in milliseconds but at around a minute.

The obvious move was more hardware. Pods went from eight CPUs to sixteen, and the service saturated those too. The second time he asked, the infrastructure team said no: fix the code, not the cluster.

## Why not Redis

Sorted sets are exactly what Redis does well, and Ivan considered it. But Redis wasn't in their production stack. The admin team would need to deploy a Sentinel setup, which could take longer than writing the code, and with clusters split across regions, a request from Europe hitting a Redis primary that had failed over to the US would add a round trip that could blow the 50 ms budget. So they went looking for an algorithmic answer instead of a new dependency.

## Linked list, then skip list

A leaderboard is just players sorted by score descending (ties broken by timestamp, so whoever got there first ranks higher). A linked list keeps that order cheaply on update, but finding someone's position means walking from the head, which is O(N) at half a million entries.

A skip list stacks sparser linked lists on top of the base list, so a search starts at the top-left and moves right and down, skipping most nodes. Each node's height comes from a biased coin flip, and Ivan's version uses odds of 75% heads to 25% tails rather than a fair 50/50. A node at height three appears on every level below it too, which is what lets traversal drop down a level safely.

The trick that turns this into a leaderboard is spans: each forward pointer stores how many base-level nodes it skips. Sum the spans along the search path and you have the player's rank in O(log N), instead of scanning. Insert and delete update spans on each affected level. Moving a player is a delete and re-insert, but the code keeps the node's previous levels so it doesn't re-flip its height every time.

Deduplication is deliberately simple: hash the identifiers a client sends (group, user ID, email) to know whose score changed, since operators can integrate through several APIs and sometimes send the same data twice.

## What changed

They tested at three levels: unit tests for the skip list, integration tests to prove the business logic hadn't changed, and manual plus performance tests that tried and failed to overload it. Afterwards, CPU throttling stayed under a millisecond in his observation, OOM kills stopped and pods ran without restarts; the performance tests showed it stable at 100K. In Ivan's words, the system became boring, which is the highest praise an on-call engineer can give.

His lessons: the standard answer isn't always right, data structures are everyday knowledge rather than interview trivia, and profile before you optimise. They now run Pyroscope for continuous flame graphs in production.

## Who should watch

Go backend engineers with anything ranked, sorted or "top N" in a hot path, and anyone tempted to scale an O(N log N)-per-update design with more cores. The diagrams of span recalculation are worth pausing on.

## Related Conf42 talks

- [Go and Redis, better together!](https://www.conf42.com/Golang_2023_Abhishek_Gupta_go_redis_better_together) by Abhishek Gupta, the road SoftSwiss considered and didn't take.
- [Heap Optimizations for Go Systems](https://www.conf42.com/Golang_2023_Nishant_Roy_heap_optimizations) by Nishant Roy, more in-process performance work with Go's memory model.
- [How to make your service more resilient in case of traffic spikes](https://www.conf42.com/Golang_2024_Ivan_Lemeshev_resilient_traffic_spikes) by Ivan Lemeshev, for the promo-campaign surge from the infrastructure side.

[Watch Ivan Balashov's talk](https://www.conf42.com/Golang_2026_Ivan_Balashov_engineering_high_performance)

[Watch the talk on YouTube](https://youtu.be/HoYi90euqvU).

## Watch the talk

[Engineering High-Performance Real-Time Leaderboards: From O(N²) to O(log N)](https://www.conf42.com/Golang_2026_Ivan_Balashov_engineering_high_performance) at Conf42 Golang 2026.
