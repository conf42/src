# WaitGroup, mutex, atomic or channel? Match the primitive to the job

Conf42 Blog, 2021-06-24. https://www.conf42.com/blog/golang2021/go-concurrency-primitives-which-job

In short: Piyush Verma (Last9.io) at Conf42 Golang 2021 on which Go concurrency primitive solves which problem, and the copy and channel mistakes that bite

Most Go concurrency bugs come from reaching for the wrong primitive, or the right one passed the wrong way. At Conf42 Golang 2021, Piyush Verma, CTO of Last9.io, sorts WaitGroups, mutexes, atomics and channels by the one job each actually does, then walks through a series of short programs that deadlock, race or leak in ways that look perfectly reasonable on first read.

It's a dense, code-first talk. If you've ever refactored a Go program because of a race you didn't see coming, it's aimed squarely at you.

## Why can a goroutine see b before a?

Piyush starts below the primitives, with memory ordering. Function f sets a to 1 then b to 2; function g prints b then a. It's possible for g to print 2 and then 0, because compilers and CPUs may reorder instructions, so what happens in order inside one goroutine isn't necessarily observed in that order from another. That unpredictability is the reason synchronization exists at all.

## Four problems, four kinds of tool

His running example is a fetcher: download a list of URLs through a bounded pool, collect the responses, count total bytes, and block until all are done. That one task contains four distinct concurrency problems:

- **Control handoff**: the main routine waits until the workers are finished.
- **Serialization**: only some work runs at once (the pool limit).
- **Data sharing**: workers send results somewhere others can read them.
- **Data consistency**: everyone sees the same, correctly incremented byte count.

Then the mapping:

| Primitive | What it's for |
|---|---|
| `sync.WaitGroup` | Control handoff only |
| `sync.Mutex` | Serialization and data consistency |
| `sync/atomic` | Data consistency only; the bedrock the others build on |
| Channels | Handoff, serialization and data sharing; not consistency |

Atomics and a lock around an integer increment are the one place the roles overlap. Piyush notes atomics are much faster there, since they go straight to the CPU.

## Primitives have to obey the language too

The best section is the run of what he calls fun mistakes. Two share one root cause: Go copies values.

Pass a WaitGroup by value into ten goroutines and each calls Done on its own copy; the program dies with all goroutines asleep. Give a counter struct an embedded mutex but bind its Value method to a value receiver and you get a data race, even though every access takes the lock: calling the method copies the struct, mutex and all, and the copy reads n while another goroutine holds the lock. Replace the body with a constant return and the race is still there. Pointer receivers fix both.

"So even the synchronization primitives need to cater to the principle of the language," Piyush Verma said at Conf42 Golang 2021.

The atomic examples make a related point. An `atomic.Value` holding a map, copied from the Go documentation, is safe for readers but not for multiple concurrent writers, so the insert path still needs a mutex. And a log call that receives from two channel-returning functions in its arguments runs them one after the other, because arguments are evaluated in order; create both channels first and the work really runs concurrently.

## Channels: who closes, and who's still waiting?

Channels get the most mistakes because they do the most jobs:

- Goroutines writing to a channel nobody reads any more block forever. Wrapping the send in a select with a default branch looks like a fix but can drop the value and leave the reader waiting.
- Closing the channel as soon as the producers' WaitGroup finishes can exit the program before the receiver has processed the last value. Piyush shows two fixes: wait and close in a separate goroutine while main ranges over the channel, or a second done channel so the parent waits for the receivers too.
- A `time.After` inside a loop allocates a new timer channel on every iteration. Create one timer, select on it, and reset it after each pass.

## Sometimes the best lock is no lock

The closing advice is to avoid contention rather than manage it. Generalized lock-free algorithms are hard, he says, but lock-free data structures, usually built on atomics, are a well-studied and more tractable problem.

"Designing lock free data structures is relatively easier," Piyush Verma said at Conf42 Golang 2021.

His simplest example needs no structure at all: if goroutines each process one item of an input slice, have each write to its own index of a pre-sized output slice instead of appending under a mutex. A simple solution beats a smart one.

## Who should watch?

Go developers who know the syntax of goroutines and channels and want the reasoning for choosing between them. Beginners will want an intro first; experienced Gophers will still find at least one of the copy bugs uncomfortably familiar.

Related Conf42 talks: [Jayaganesh Kalyanasundaram's concurrency for beginners](https://www.conf42.com/Golang_2021_Jayaganesh_Kalyanasundaram_concurrency_for_beginners), [Jesus Espino dissecting slices, maps and channels](https://www.conf42.com/Golang_2022_Jesus_Espino_dissecting_slices_maps_channels), and [Oliver Fuerst on running the race detector around the clock](https://www.conf42.com/Golang_2021_Oliver_Fuerst_devops_automation).

[Watch Piyush Verma's talk](https://www.conf42.com/Golang_2021_Piyush_Verma_concurrency_primitives) from [Conf42 Golang 2021](https://www.conf42.com/golang2021).

## From Last9.io

Piyush describes Last9 as an observability company, where he is founder and CTO.

- Last9: [last9.io](https://last9.io)

[Watch the talk on YouTube](https://youtu.be/BeFLnQF78ik).

## Watch the talk

[Concurrency primitives of Golang - how to use and how not to](https://www.conf42.com/Golang_2021_Piyush_Verma_concurrency_primitives) at Conf42 Golang 2021.
